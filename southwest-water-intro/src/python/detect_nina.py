#!/usr/bin/env python3
"""Detect the leftmost presenter (Nina) and export crop + feathered mask."""
from __future__ import annotations

import argparse
import json
import sys

import cv2
import numpy as np


def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(cascade_path)
    faces = cascade.detectMultiScale(gray, scaleFactor=1.08, minNeighbors=5, minSize=(80, 80))
    return [(int(x), int(y), int(w), int(h)) for x, y, w, h in faces]


def pick_nina(faces, hint, image_shape):
    if not faces:
        return hint
    # Prefer the largest face whose centre sits in the left 55% of the frame.
    height, width = image_shape[:2]
    left_faces = [f for f in faces if (f[0] + f[2] / 2) < width * 0.55]
    pool = left_faces or faces
    pool.sort(key=lambda f: f[2] * f[3], reverse=True)
    x, y, w, h = pool[0]
    pad_x = int(w * 0.55)
    pad_y_top = int(h * 0.55)
    pad_y_bot = int(h * 1.35)
    nx = max(0, x - pad_x)
    ny = max(0, y - pad_y_top)
    nw = min(width - nx, w + pad_x * 2)
    nh = min(height - ny, h + pad_y_top + pad_y_bot)
    # Keep the nameplate on the static background so labels do not animate.
    nh = min(nh, max(120, height - 80 - ny))
    return {"x": nx, "y": ny, "w": nw, "h": nh, "face": {"x": x, "y": y, "w": w, "h": h}}


def feather_mask(width, height):
    mask = np.ones((height, width), dtype=np.float32)
    fade = max(12, width // 18)
    for i in range(fade):
        alpha = i / fade
        mask[:, i] *= alpha
        mask[:, width - 1 - i] *= alpha
        if i < height:
            mask[i, :] *= alpha
            mask[height - 1 - i, :] *= min(1.0, 0.35 + alpha)
    mask[:, int(width * 0.88) :] *= np.linspace(1.0, 0.0, width - int(width * 0.88))[None, :]
    return (mask * 255).astype(np.uint8)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--hint-x", type=int, required=True)
    parser.add_argument("--hint-y", type=int, required=True)
    parser.add_argument("--hint-w", type=int, required=True)
    parser.add_argument("--hint-h", type=int, required=True)
    parser.add_argument("--crop-out", required=True)
    parser.add_argument("--mask-out", required=True)
    args = parser.parse_args()

    image = cv2.imread(args.image, cv2.IMREAD_COLOR)
    if image is None:
        raise SystemExit(f"Unable to read {args.image}")

    hint = {"x": args.hint_x, "y": args.hint_y, "w": args.hint_w, "h": args.hint_h, "method": "hint"}
    faces = detect_faces(image)
    box = pick_nina(faces, hint, image.shape)
    box["method"] = "haar" if faces else "hint"

    crop = image[box["y"] : box["y"] + box["h"], box["x"] : box["x"] + box["w"]]
    cv2.imwrite(args.crop_out, crop)
    mask = feather_mask(box["w"], box["h"])
    cv2.imwrite(args.mask_out, mask)
    print(json.dumps(box))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:  # pylint: disable=broad-except
        print(str(error), file=sys.stderr)
        sys.exit(1)
