#!/usr/bin/env python3
"""IMAGE + AUDIO → talking-person video with phoneme/viseme-driven mouth motion."""
from __future__ import annotations

import argparse
import math
import re
import subprocess
import sys
import wave
from pathlib import Path

import cv2
import numpy as np


CLOSED = 0.02
VISEME_OPEN = {
    "A": 0.92,
    "E": 0.62,
    "I": 0.48,
    "O": 0.84,
    "U": 0.7,
    "M": 0.0,
    "B": 0.0,
    "P": 0.0,
    "F": 0.22,
    "V": 0.22,
    "W": 0.38,
    "L": 0.4,
    "R": 0.34,
    "S": 0.28,
    "T": 0.3,
    "D": 0.32,
    "N": 0.24,
    "G": 0.36,
    "K": 0.3,
    "Y": 0.42,
    "H": 0.26,
    "Q": 0.55,
}


def load_wav_mono(path: str):
    with wave.open(path, "rb") as handle:
        channels = handle.getnchannels()
        rate = handle.getframerate()
        frames = handle.readframes(handle.getnframes())
        sample_width = handle.getsampwidth()
    if sample_width == 2:
        data = np.frombuffer(frames, dtype=np.int16).astype(np.float32)
    else:
        raise SystemExit("Expected 16-bit PCM WAV")
    if channels > 1:
        data = data.reshape(-1, channels).mean(axis=1)
    data /= 32768.0
    return data, rate


def rms_envelope(samples: np.ndarray, rate: int, fps: int, duration: float) -> np.ndarray:
    frame_count = int(round(duration * fps))
    hop = rate / fps
    env = np.zeros(frame_count, dtype=np.float32)
    window = max(1, int(rate * 0.04))
    for i in range(frame_count):
        start = int(i * hop)
        chunk = samples[start : start + window]
        if chunk.size:
            env[i] = float(np.sqrt(np.mean(chunk * chunk)))
    peak = float(env.max()) or 1.0
    env /= peak
    # Light smoothing to avoid jittery lips.
    kernel = np.ones(3) / 3.0
    env = np.convolve(env, kernel, mode="same")
    return env


def viseme_track(transcript: str, frame_count: int) -> np.ndarray:
    tokens = re.findall(r"[A-Za-z']+", transcript.upper())
    if not tokens:
        return np.zeros(frame_count, dtype=np.float32)
    chars = []
    for token in tokens:
        chars.extend(list(token))
        chars.append(" ")
    track = np.zeros(frame_count, dtype=np.float32)
    for i in range(frame_count):
        idx = int((i / max(1, frame_count - 1)) * (len(chars) - 1))
        ch = chars[idx]
        track[i] = VISEME_OPEN.get(ch, 0.18 if ch != " " else 0.04)
    return track


def mouth_roi(face):
    x, y, w, h = face
    mx = x + int(w * 0.18)
    my = y + int(h * 0.62)
    mw = int(w * 0.64)
    mh = int(h * 0.32)
    return mx, my, mw, mh


def eye_rois(face):
    x, y, w, h = face
    ey = y + int(h * 0.32)
    eh = int(h * 0.13)
    lw = int(w * 0.28)
    return (x + int(w * 0.14), ey, lw, eh), (x + int(w * 0.58), ey, lw, eh)


def warp_mouth(frame, roi, open_amt: float):
    mx, my, mw, mh = roi
    h, w = frame.shape[:2]
    mx = max(0, mx)
    my = max(0, my)
    mw = min(mw, w - mx)
    mh = min(mh, h - my)
    if mw < 8 or mh < 8:
        return frame
    patch = frame[my : my + mh, mx : mx + mw].copy()
    scale_y = 1.0 + 0.38 * open_amt
    scale_x = 1.0 + 0.08 * open_amt
    new_w = max(8, int(mw * scale_x))
    new_h = max(8, int(mh * scale_y))
    stretched = cv2.resize(patch, (new_w, new_h), interpolation=cv2.INTER_CUBIC)
    # Centre the stretched mouth back into the ROI without changing identity much.
    y0 = max(0, my - (new_h - mh) // 3)
    x0 = max(0, mx - (new_w - mw) // 2)
    y1 = min(h, y0 + new_h)
    x1 = min(w, x0 + new_w)
    crop = stretched[: y1 - y0, : x1 - x0]
    # Feathered blend to avoid a rectangular mouth artefact.
    mask = np.zeros((y1 - y0, x1 - x0), dtype=np.float32)
    cv2.ellipse(
        mask,
        ((x1 - x0) // 2, int((y1 - y0) * 0.55)),
        (int((x1 - x0) * 0.42), int((y1 - y0) * 0.38)),
        0,
        0,
        360,
        1.0,
        -1,
    )
    mask = cv2.GaussianBlur(mask, (21, 21), 0)
    mask3 = mask[:, :, None]
    region = frame[y0:y1, x0:x1].astype(np.float32)
    blended = region * (1 - mask3) + crop.astype(np.float32) * mask3
    frame[y0:y1, x0:x1] = blended.astype(np.uint8)
    return frame


def blink_eyes(frame, rois, amount: float):
    if amount <= 0:
        return frame
    for ex, ey, ew, eh in rois:
        lid = int(eh * (0.15 + 0.75 * amount))
        y1 = min(frame.shape[0], ey + lid)
        x1 = min(frame.shape[1], ex + ew)
        if y1 <= ey or x1 <= ex:
            continue
        patch = frame[ey:y1, ex:x1]
        darkened = (patch.astype(np.float32) * (1.0 - 0.55 * amount)).astype(np.uint8)
        frame[ey:y1, ex:x1] = darkened
    return frame


def detect_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = cascade.detectMultiScale(gray, 1.08, 5, minSize=(70, 70))
    if len(faces) == 0:
        h, w = image.shape[:2]
        return int(w * 0.2), int(h * 0.12), int(w * 0.6), int(h * 0.58)
    faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
    x, y, w, h = [int(v) for v in faces[0]]
    return x, y, w, h


def encode_video(tmp_video: str, fps: int, out_path: str, audio: str) -> None:
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        tmp_video,
        "-i",
        audio,
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "aac",
        "-shortest",
        "-movflags",
        "+faststart",
        out_path,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(proc.stderr[-4000:])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--audio", required=True)
    parser.add_argument("--transcript", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--fps", type=int, default=30)
    args = parser.parse_args()

    image = cv2.imread(args.image, cv2.IMREAD_COLOR)
    if image is None:
        raise SystemExit(f"Unable to read {args.image}")

    samples, rate = load_wav_mono(args.audio)
    duration = len(samples) / float(rate)
    fps = args.fps
    frame_count = int(round(duration * fps))
    env = rms_envelope(samples, rate, fps, duration)
    visemes = viseme_track(args.transcript, frame_count)
    face = detect_face(image)
    mouth = mouth_roi(face)
    eyes = eye_rois(face)

    h, w = image.shape[:2]
    tmp_video = str(Path(args.out).with_suffix(".raw.avi"))
    Path(tmp_video).parent.mkdir(parents=True, exist_ok=True)
    writer = cv2.VideoWriter(tmp_video, cv2.VideoWriter_fourcc(*"XVID"), fps, (w, h))
    if not writer.isOpened():
        tmp_video = str(Path(args.out).with_suffix(".raw.mp4"))
        writer = cv2.VideoWriter(tmp_video, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))
    if not writer.isOpened():
        raise SystemExit("Unable to open VideoWriter for talking-avatar frames")

    for i in range(frame_count):
        frame = image.copy()
        t = i / fps
        dx = int(round(math.sin(t * 1.15) * 2.2))
        dy = int(round(math.sin(t * 0.7) * 1.6))
        m = np.float32([[1, 0, dx], [0, 1, dy]])
        frame = cv2.warpAffine(frame, m, (w, h), borderMode=cv2.BORDER_REFLECT)

        open_amt = float(np.clip(0.15 * env[i] + 0.85 * visemes[i] * (0.35 + 0.65 * env[i]), 0, 1))
        if env[i] < 0.04:
            open_amt *= 0.15
        frame = warp_mouth(frame, mouth, open_amt)

        blink_cycle = t % 3.6
        blink_amt = 0.0
        if 0.0 < blink_cycle < 0.12:
            blink_amt = blink_cycle / 0.12
        elif 0.12 <= blink_cycle < 0.22:
            blink_amt = 1.0 - ((blink_cycle - 0.12) / 0.10)
        frame = blink_eyes(frame, eyes, max(0.0, blink_amt))
        writer.write(frame)

    writer.release()
    encode_video(tmp_video, fps, args.out, args.audio)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:  # pylint: disable=broad-except
        print(str(error), file=sys.stderr)
        sys.exit(1)
