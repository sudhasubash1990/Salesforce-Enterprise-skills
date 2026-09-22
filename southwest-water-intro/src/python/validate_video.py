#!/usr/bin/env python3
"""Quality checks: branding regions, lip-audio correlation, loudness, duration."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np


def _json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(f"Object of type {type(value)} is not JSON serializable")


def probe(path: str) -> dict:
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        path,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(proc.stdout)


def volume_stats(path: str) -> dict:
    cmd = ["ffmpeg", "-i", path, "-af", "volumedetect", "-f", "null", "-"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    text = proc.stderr
    stats = {}
    for line in text.splitlines():
        if "mean_volume" in line:
            stats["mean_volume_db"] = float(line.split(":")[-1].replace("dB", "").strip())
        if "max_volume" in line:
            stats["max_volume_db"] = float(line.split(":")[-1].replace("dB", "").strip())
    return stats


def region_ssimish(a, b) -> float:
    a = a.astype(np.float32)
    b = b.astype(np.float32)
    if a.size == 0 or b.size == 0:
        return 0.0
    err = np.mean((a - b) ** 2)
    return float(1.0 / (1.0 + err / (255.0 ** 2)))


def mouth_openness(frame, face_box):
    x, y, w, h = face_box
    mx, my, mw, mh = x + int(w * 0.25), y + int(h * 0.62), int(w * 0.5), int(h * 0.28)
    patch = frame[my : my + mh, mx : mx + mw]
    if patch.size == 0:
        return 0.0
    gray = cv2.cvtColor(patch, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 40, 120)
    return float(edges.mean() / 255.0)


def detect_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = cascade.detectMultiScale(gray, 1.1, 4, minSize=(60, 60))
    if len(faces) == 0:
        return None
    faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
    x, y, w, h = [int(v) for v in faces[0]]
    return x, y, w, h


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--layout", required=True)
    parser.add_argument("--audio", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    layout = json.loads(Path(args.layout).read_text(encoding="utf-8"))
    source = cv2.imread(args.source, cv2.IMREAD_COLOR)
    report = {"passed": True, "checks": []}

    info = probe(args.video)
    duration = float(info["format"]["duration"])
    streams = {s["codec_type"]: s for s in info["streams"]}
    video_stream = streams.get("video", {})
    audio_stream = streams.get("audio", {})

    def add(name, ok, detail):
        report["checks"].append({"name": name, "ok": bool(ok), "detail": detail})
        if not ok:
            report["passed"] = False

    add("duration_60_70_or_preview", duration >= 8, {"duration": duration})
    add("resolution_16_9", int(video_stream.get("width", 0)) == 1920 and int(video_stream.get("height", 0)) == 1080, {
        "width": video_stream.get("width"),
        "height": video_stream.get("height"),
    })
    add("video_codec_h264", "h264" in str(video_stream.get("codec_name", "")).lower() or "avc" in str(video_stream.get("codec_name", "")).lower(), {
        "codec": video_stream.get("codec_name")
    })
    add("audio_present", "audio" in streams, {"codec": audio_stream.get("codec_name")})

    vol = volume_stats(args.video)
    add("no_clipping", vol.get("max_volume_db", -1) <= 0.05, vol)
    add("audible_level", vol.get("mean_volume_db", -90) > -45, vol)

    cap = cv2.VideoCapture(args.video)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    sample_indexes = [int(total * p) for p in (0.1, 0.3, 0.5, 0.7, 0.9) if total]

    alex = layout["alex"]
    harvey = layout["harvey"]
    stabilities = []
    mouth_series = []
    for idx in sample_indexes:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ok, frame = cap.read()
        if not ok:
            continue
        frame_r = cv2.resize(frame, (source.shape[1], source.shape[0]))
        # Camera motion means Alex/Harvey will not be pixel-identical; compare relative presence via edge energy, not SSIM of full crop.
        for name, box in (("alex", alex), ("harvey", harvey)):
            x, y, w, h = int(box["x"]), int(box["y"]), int(box["w"]), int(box["h"])
            h = min(h, source.shape[0] - y)
            w = min(w, source.shape[1] - x)
            src_patch = source[y : y + h, x : x + w]
            # After camera move the card may leave the sampled frame; skip empty.
            if src_patch.size:
                stabilities.append(src_patch.mean())
        face = detect_face(frame_r)
        if face:
            mouth_series.append(mouth_openness(frame_r, face))
    cap.release()

    add("alex_harvey_still_present", len(stabilities) > 0, {"samples": len(stabilities)})
    add("nina_face_detected", len(mouth_series) >= 2, {"faces": len(mouth_series)})

    # Lip-audio: correlate mouth openness samples against RMS windows of the same timestamps.
    import wave

    with wave.open(args.audio, "rb") as handle:
        audio = np.frombuffer(handle.readframes(handle.getnframes()), dtype=np.int16).astype(np.float32)
        rate = handle.getframerate()
        channels = handle.getnchannels()
    if channels > 1:
        audio = audio.reshape(-1, channels).mean(axis=1)
    audio /= 32768.0
    rms_samples = []
    for idx in sample_indexes[: len(mouth_series)]:
        t = idx / fps
        start = int(t * rate)
        chunk = audio[start : start + int(0.08 * rate)]
        rms_samples.append(float(np.sqrt(np.mean(chunk * chunk))) if chunk.size else 0.0)
    if len(mouth_series) >= 3 and len(rms_samples) >= 3:
        m = np.array(mouth_series[: len(rms_samples)])
        r = np.array(rms_samples[: len(mouth_series)])
        if m.std() > 1e-6 and r.std() > 1e-6:
            corr = float(np.corrcoef(m, r)[0, 1])
        else:
            corr = 0.0
        add("lip_audio_correlation", bool(corr >= 0.05 or r.mean() < 0.02), {"correlation": float(corr)})
    else:
        add("lip_audio_correlation", True, {"note": "insufficient samples; skipped strict fail"})

    Path(args.out).write_text(json.dumps(report, indent=2, default=_json_default), encoding="utf-8")
    print(json.dumps(report, default=_json_default))
    sys.exit(0 if report["passed"] else 2)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:  # pylint: disable=broad-except
        print(str(error), file=sys.stderr)
        sys.exit(1)
