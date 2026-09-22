#!/usr/bin/env python3
"""Generate UK English neural speech via Microsoft Edge TTS (verbatim paragraphs)."""
from __future__ import annotations

import argparse
import asyncio
import re
import subprocess
import sys
import tempfile
from pathlib import Path


async def synth_paragraphs(voice: str, rate: str, ssml_path: str, out_path: str) -> None:
    try:
        import edge_tts
    except ImportError as exc:  # pragma: no cover
        raise SystemExit("edge-tts is not installed. Run: pip install edge-tts") from exc

    raw = Path(ssml_path).read_text(encoding="utf-8")
    text = re.sub(r"</?speak[^>]*>", "", raw)
    text = re.sub(r"</?p>", "\n\n", text)
    text = re.sub(r"<break[^/]*/>", "\n\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    if not paragraphs:
        raise SystemExit("No narration text found")

    tmp = Path(tempfile.mkdtemp(prefix="nina-tts-"))
    parts = []
    for index, paragraph in enumerate(paragraphs):
        mp3 = tmp / f"p{index:02d}.mp3"
        communicate = edge_tts.Communicate(paragraph, voice=voice, rate=rate)
        await communicate.save(str(mp3))
        parts.append(mp3)
        if index < len(paragraphs) - 1:
            silence = tmp / f"s{index:02d}.mp3"
            subprocess.run(
                [
                    "ffmpeg",
                    "-y",
                    "-f",
                    "lavfi",
                    "-i",
                    "anullsrc=r=24000:cl=mono",
                    "-t",
                    "0.42",
                    "-q:a",
                    "9",
                    str(silence),
                ],
                check=True,
                capture_output=True,
            )
            parts.append(silence)

    concat_list = tmp / "concat.txt"
    concat_list.write_text("".join(f"file '{p}'\n" for p in parts), encoding="utf-8")
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_list),
            "-c:a",
            "libmp3lame",
            "-q:a",
            "2",
            out_path,
        ],
        check=True,
        capture_output=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--voice", required=True)
    parser.add_argument("--rate", default="+0%")
    parser.add_argument("--ssml", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    asyncio.run(synth_paragraphs(args.voice, args.rate, args.ssml, args.out))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:  # pylint: disable=broad-except
        print(str(error), file=sys.stderr)
        sys.exit(1)
