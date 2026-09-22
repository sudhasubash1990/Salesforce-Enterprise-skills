#!/usr/bin/env python3
"""Composite Nina talking layer over the original still with subtle camera + icon highlights."""
from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np


def load_layout(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def lerp(a, b, t):
    return a + (b - a) * t


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def scene_at(t: float, duration: float, scenes: list[dict]) -> dict:
    for scene in scenes:
        start = scene["startSec"] / 67.0 * duration
        end = scene["endSec"] / 67.0 * duration
        if start <= t < end:
            return {**scene, "start": start, "end": end}
    last = scenes[-1]
    return {**last, "start": last["startSec"] / 67.0 * duration, "end": duration}


def camera_rect(layout, scene, t, width, height):
    nina = layout.get("ninaDetected") or layout["nina"]
    alex = layout["alex"]
    harvey = layout["harvey"]

    def box(x, y, w, h, zoom):
        return {"x": x, "y": y, "w": w, "h": h, "zoom": zoom}

    full = box(0, 0, width, height, 1.0)
    nina_focus = box(0, 0, min(width, nina["w"] + 980), height, 1.04)
    journey = box(380, 60, width - 400, height - 70, 1.07)
    alex_f = box(max(0, alex["x"] - 70), max(0, alex["y"] - 30), min(width, alex["w"] + 240), min(height, alex["h"] + 140), 1.1)
    harvey_f = box(max(0, harvey["x"] - 70), max(0, harvey["y"] - 30), min(width, harvey["w"] + 240), min(height, harvey["h"] + 160), 1.1)
    self_f = box(500, 500, width - 520, 540, 1.08)

    start, end = scene["start"], scene["end"]
    local_t = clamp((t - start) / max(0.01, end - start), 0, 1)
    eased = local_t * local_t * (3 - 2 * local_t)
    cam = scene.get("camera")
    if cam == "nina":
        src, dst = full, nina_focus
    elif cam == "journey":
        src, dst = nina_focus, journey
    elif cam == "cast":
        src, dst = (journey, alex_f) if t < (start + end) / 2 else (alex_f, harvey_f)
    elif cam == "selfservice":
        src, dst = journey, self_f
    elif cam == "nina-end":
        src, dst = self_f, nina_focus
    else:
        src, dst = full, nina_focus

    return {
        "x": lerp(src["x"], dst["x"], eased),
        "y": lerp(src["y"], dst["y"], eased),
        "w": lerp(src["w"], dst["w"], eased),
        "h": lerp(src["h"], dst["h"], eased),
    }


def crop_zoom(frame, cam, out_w, out_h):
    h, w = frame.shape[:2]
    target_aspect = out_w / out_h
    cx = cam["x"] + cam["w"] / 2.0
    cy = cam["y"] + cam["h"] / 2.0
    cw = float(max(64, cam["w"]))
    ch = float(max(64, cam["h"]))
    if cw / ch < target_aspect:
        cw = ch * target_aspect
    else:
        ch = cw / target_aspect
    if cw > w:
        cw = float(w)
        ch = cw / target_aspect
    if ch > h:
        ch = float(h)
        cw = ch * target_aspect
    x = int(clamp(cx - cw / 2.0, 0, w - cw))
    y = int(clamp(cy - ch / 2.0, 0, h - ch))
    cropped = frame[y : y + int(ch), x : x + int(cw)]
    return cv2.resize(cropped, (out_w, out_h), interpolation=cv2.INTER_CUBIC)


def overlay_nina(base, nina_frame, box, mask_path: str | None):
    x, y, w, h = int(box["x"]), int(box["y"]), int(box["w"]), int(box["h"])
    h_img, w_img = base.shape[:2]
    w = min(w, w_img - x)
    h = min(h, h_img - y)
    if w <= 1 or h <= 1:
        return base
    resized = cv2.resize(nina_frame, (w, h), interpolation=cv2.INTER_CUBIC)
    if mask_path and Path(mask_path).exists():
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
        mask = cv2.resize(mask, (w, h), interpolation=cv2.INTER_LINEAR)
    else:
        mask = np.full((h, w), 255, dtype=np.uint8)
        fade = max(8, w // 16)
        for i in range(fade):
            alpha = int(255 * (i / fade))
            mask[:, i] = np.minimum(mask[:, i], alpha)
            mask[:, w - 1 - i] = np.minimum(mask[:, w - 1 - i], alpha)
        mask[:, int(w * 0.9) :] = (mask[:, int(w * 0.9) :].astype(np.float32) * np.linspace(1, 0, w - int(w * 0.9))).astype(
            np.uint8
        )
    alpha = (mask.astype(np.float32) / 255.0)[:, :, None]
    region = base[y : y + h, x : x + w].astype(np.float32)
    blended = region * (1 - alpha) + resized.astype(np.float32) * alpha
    base[y : y + h, x : x + w] = blended.astype(np.uint8)
    return base


def draw_icon_highlights(frame, layout, scene, t):
    highlight = scene.get("highlight")
    if not highlight:
        return frame
    icons = layout.get("icons") or []
    if highlight == "cast":
        start, end = scene["start"], scene["end"]
        mid = (start + end) / 2
        target = layout["alex"] if t < mid else layout["harvey"]
        overlay = frame.copy()
        x, y, w, h = int(target["x"]), int(target["y"]), int(target["w"]), int(target["h"])
        cv2.rectangle(overlay, (x, y), (x + w, y + h), (0, 180, 230), 3)
        return cv2.addWeighted(overlay, 0.35, frame, 0.65, 0)

    group = "movein" if highlight == "movein" else "selfservice"
    group_icons = [i for i in icons if i.get("group") == group]
    if not group_icons:
        return frame
    local_t = clamp((t - scene["start"]) / max(0.01, scene["end"] - scene["start"]), 0, 1)
    idx = min(len(group_icons) - 1, int(local_t * len(group_icons)))
    icon = group_icons[idx]
    overlay = frame.copy()
    x, y, w, h = int(icon["x"]), int(icon["y"]), int(icon["w"]), int(icon["h"])
    cv2.rectangle(overlay, (x - 4, y - 4), (x + w + 4, y + h + 4), (0, 210, 240), 2)
    glow = overlay.copy()
    cv2.rectangle(glow, (x, y), (x + w, y + h), (40, 160, 200), -1)
    overlay = cv2.addWeighted(glow, 0.18, overlay, 0.82, 0)
    return cv2.addWeighted(overlay, 0.85, frame, 0.15, 0)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--nina-video", required=True)
    parser.add_argument("--audio", required=True)
    parser.add_argument("--layout", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--width", type=int, default=1920)
    parser.add_argument("--height", type=int, default=1080)
    parser.add_argument("--duration", type=float, default=0)
    args = parser.parse_args()

    layout = load_layout(args.layout)
    source = cv2.imread(args.source, cv2.IMREAD_COLOR)
    if source is None:
        raise SystemExit(f"Unable to read {args.source}")
    source = cv2.resize(source, (args.width, args.height), interpolation=cv2.INTER_CUBIC)

    cap = cv2.VideoCapture(args.nina_video)
    if not cap.isOpened():
        raise SystemExit(f"Unable to open {args.nina_video}")
    nina_fps = cap.get(cv2.CAP_PROP_FPS) or args.fps
    nina_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    nina_duration = nina_frames / nina_fps if nina_fps else 0
    duration = args.duration or nina_duration
    frame_count = int(round(duration * args.fps))

    scenes = [
        {"id": "opening", "startSec": 0, "endSec": 8, "camera": "nina", "highlight": None},
        {"id": "journey-intro", "startSec": 8, "endSec": 18, "camera": "journey", "highlight": None},
        {"id": "introduce-cast", "startSec": 18, "endSec": 31, "camera": "cast", "highlight": "cast"},
        {"id": "realtime", "startSec": 31, "endSec": 38, "camera": "nina", "highlight": None},
        {"id": "move-in", "startSec": 38, "endSec": 50, "camera": "journey", "highlight": "movein"},
        {"id": "self-service", "startSec": 50, "endSec": 62, "camera": "selfservice", "highlight": "selfservice"},
        {"id": "join-call", "startSec": 62, "endSec": 67, "camera": "nina-end", "highlight": None},
    ]

    tmp_avi = str(Path(args.out).with_suffix(".avi"))
    writer = cv2.VideoWriter(tmp_avi, cv2.VideoWriter_fourcc(*"XVID"), args.fps, (args.width, args.height))
    nina_box = layout.get("ninaDetected") or layout["nina"]
    mask_path = str(Path(args.layout).parent / "nina-mask.png")

    last_nina = None
    nina_pos = 0
    for i in range(frame_count):
        t = i / args.fps
        target_nina = min(max(nina_frames - 1, 0), int(t * nina_fps)) if nina_frames else i
        while nina_pos <= target_nina:
            ok, grabbed = cap.read()
            nina_pos += 1
            if ok:
                last_nina = grabbed
            else:
                break
        nina_frame = last_nina if last_nina is not None else source
        composed = source.copy()
        composed = overlay_nina(composed, nina_frame, nina_box, mask_path)
        scene = scene_at(t, duration, scenes)
        composed = draw_icon_highlights(composed, layout, scene, t)
        cam = camera_rect(layout, scene, t, args.width, args.height)
        out = crop_zoom(composed, cam, args.width, args.height)
        if scene.get("camera") == "nina-end":
            fade = clamp((t - scene["start"]) / max(0.01, scene["end"] - scene["start"]), 0, 1)
            if fade > 0.75:
                black = np.zeros_like(out)
                amt = (fade - 0.75) / 0.25
                out = cv2.addWeighted(out, 1 - amt, black, amt, 0)
        writer.write(out)

    writer.release()
    cap.release()

    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        tmp_avi,
        "-i",
        args.audio,
        "-map",
        "0:v:0",
        "-map",
        "1:a:0",
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "-preset",
        "medium",
        "-crf",
        "18",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-ar",
        "48000",
        "-shortest",
        "-movflags",
        "+faststart",
        args.out,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(proc.stderr[-4000:])


if __name__ == "__main__":
    try:
        main()
    except Exception as error:  # pylint: disable=broad-except
        print(str(error), file=sys.stderr)
        sys.exit(1)
