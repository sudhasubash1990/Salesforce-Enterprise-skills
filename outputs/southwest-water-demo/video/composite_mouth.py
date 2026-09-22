#!/usr/bin/env python3
"""
Composite only the mouth region of a Wav2Lip output back onto the original still image,
optionally after GFPGAN face restoration and temporal smoothing.

Why: Wav2Lip regenerates the whole face at 96x96, which blurs and subtly morphs the
nose/cheeks every frame and smears the teeth. Restoring the generated face with GFPGAN,
smoothing it over neighbouring frames, and blending back only the lips/jaw keeps the
original high-resolution face fully stable while the mouth stays sharp and readable.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time

import cv2
import numpy as np


def build_mask(h: int, w: int, cx: int, cy: int, ax: int, ay: int, feather: float) -> np.ndarray:
    m = np.zeros((h, w), dtype=np.float32)
    cv2.ellipse(m, (cx, cy), (ax, ay), 0, 0, 360, 1.0, -1)
    m = cv2.GaussianBlur(m, (0, 0), feather)
    return m[..., None]


def sharpen(img: np.ndarray, amount: float) -> np.ndarray:
    if amount <= 0:
        return img
    blur = cv2.GaussianBlur(img, (0, 0), 1.2)
    return cv2.addWeighted(img, 1 + amount, blur, -amount, 0)


def color_match(gen: np.ndarray, ref: np.ndarray, ring: np.ndarray) -> np.ndarray:
    """Shift generated colours so the skin around the mouth matches the original."""
    wsum = ring.sum()
    if wsum < 1:
        return gen
    diff = ((ref - gen) * ring).reshape(-1, 3).sum(0) / wsum
    return gen + diff


class Restorer:
    def __init__(self, model_path: str, cx: int, cy: int, half: int, weight: float) -> None:
        import torch
        from gfpgan import GFPGANer

        torch.set_num_threads(max(1, torch.get_num_threads()))
        self.r = GFPGANer(model_path=model_path, upscale=1, arch="clean", channel_multiplier=2,
                          bg_upsampler=None, device="cpu")
        self.cx, self.cy, self.half, self.weight = cx, cy, half, weight

    def __call__(self, frame: np.ndarray) -> np.ndarray:
        cx, cy, s = self.cx, self.cy, self.half
        crop = frame[cy - s:cy + s, cx - s:cx + s]
        c512 = cv2.resize(crop, (512, 512), interpolation=cv2.INTER_CUBIC)
        _, restored, _ = self.r.enhance(c512, has_aligned=True, only_center_face=True,
                                        paste_back=False, weight=self.weight)
        out = frame.copy()
        out[cy - s:cy + s, cx - s:cx + s] = cv2.resize(restored[0], (2 * s, 2 * s), interpolation=cv2.INTER_AREA)
        return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, help="original still image")
    ap.add_argument("--wav2lip", required=True, help="Wav2Lip output video")
    ap.add_argument("--audio", required=True, help="audio to mux (mp3/wav)")
    ap.add_argument("--out", required=True, help="output .mkv")
    ap.add_argument("--mouth", required=True, help="cx,cy,ax,ay ellipse in source pixels")
    ap.add_argument("--feather", type=float, default=6.0)
    ap.add_argument("--sharpen", type=float, default=0.0)
    ap.add_argument("--gfpgan", default="", help="path to GFPGANv1.4.pth (enables restoration)")
    ap.add_argument("--face", default="", help="cx,cy,half of square face crop for GFPGAN")
    ap.add_argument("--gfpgan-weight", type=float, default=0.5)
    ap.add_argument("--smooth", type=float, default=0.2,
                    help="weight of each neighbour frame in 3-tap temporal smoothing (0 disables)")
    ap.add_argument("--audio-filter", default="")
    args = ap.parse_args()

    cx, cy, ax, ay = (int(v) for v in args.mouth.split(","))
    base = cv2.imread(args.source)
    cap = cv2.VideoCapture(args.wav2lip)
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    ok, first = cap.read()
    if not ok:
        sys.exit("cannot read wav2lip video")
    h, w = first.shape[:2]
    if base.shape[:2] != (h, w):
        base = cv2.resize(base, (w, h), interpolation=cv2.INTER_AREA)
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    mask = build_mask(h, w, cx, cy, ax, ay, args.feather)
    # ring: soft edge of the mask where original skin and generated skin meet
    ring = np.clip(mask, 0, 1) * (1 - np.clip(mask, 0, 1)) * 4
    base_f = base.astype(np.float32)

    restorer = None
    if args.gfpgan:
        fcx, fcy, fhalf = (int(v) for v in args.face.split(","))
        restorer = Restorer(args.gfpgan, fcx, fcy, fhalf, args.gfpgan_weight)

    # Pass 1: read + restore every frame (kept in memory; 60 s @ 25 fps of 760x530 is ~1.8 GB float-free uint8)
    frames: list[np.ndarray] = []
    t0 = time.time()
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if restorer is not None:
            frame = restorer(frame)
        frames.append(frame)
        if len(frames) % 100 == 0:
            el = time.time() - t0
            print(f"restored {len(frames)}/{n} ({el:.0f}s, eta {el / len(frames) * (n - len(frames)):.0f}s)", flush=True)
    cap.release()
    print(f"pass 1 done: {len(frames)} frames in {time.time() - t0:.0f}s", flush=True)

    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{w}x{h}", "-r", f"{fps:g}", "-i", "-",
        "-i", args.audio,
        "-map", "0:v:0", "-map", "1:a:0", "-sn",
        "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
    ]
    if args.audio_filter:
        cmd += ["-af", args.audio_filter]
    cmd += ["-shortest", "-metadata", "title=Southwest Water Customer Journey Demonstration - Nina Intro", args.out]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    assert proc.stdin

    # Pass 2: temporal smoothing + colour match + mouth-only blend
    s = args.smooth
    for i, frame in enumerate(frames):
        gen = frame.astype(np.float32)
        if s > 0 and len(frames) > 1:
            prev = frames[max(i - 1, 0)].astype(np.float32)
            nxt = frames[min(i + 1, len(frames) - 1)].astype(np.float32)
            gen = prev * s + gen * (1 - 2 * s) + nxt * s
        gen = color_match(gen, base_f, ring)
        gen = sharpen(gen, args.sharpen)
        out = base_f * (1 - mask) + gen * mask
        proc.stdin.write(np.clip(out, 0, 255).astype(np.uint8).tobytes())
    proc.stdin.close()
    rc = proc.wait()
    print(f"frames={len(frames)}/{n} rc={rc} -> {args.out}")


if __name__ == "__main__":
    main()
