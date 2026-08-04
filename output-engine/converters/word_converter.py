"""Word document converter using Pandoc."""

from __future__ import annotations

import os
import re
from pathlib import Path

try:
    import pypandoc
except ImportError:
    pypandoc = None  # type: ignore

from shared.converter_interface import DocumentConverter
from shared.file_utils import write_via_temp
from shared.markdown_parser import build_cover_md
from shared.models import ConversionJob


class WordConverter(DocumentConverter):
    format_ext = ".docx"
    format_name = "docx"

    def convert(self, job: ConversionJob) -> None:
        if pypandoc is None:
            raise RuntimeError("pypandoc is not installed")
        content = job.body
        if job.config.get("generateCoverPage", True):
            content = build_cover_md(job.meta) + job.body

        # Resolve relative image paths against the markdown source directory
        source_dir = job.source_path.parent.resolve()

        def _abs_img(match: re.Match[str]) -> str:
            alt, src = match.group(1), match.group(2)
            if src.startswith(("http://", "https://", "data:")):
                return match.group(0)
            candidate = Path(src)
            if not candidate.is_absolute():
                candidate = (source_dir / src).resolve()
            if candidate.exists():
                return f"![{alt}]({candidate.as_posix()})"
            return match.group(0)

        content = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", _abs_img, content)

        resource_path = os.pathsep.join(
            [
                str(source_dir),
                str(job.root_path.resolve()),
                str((job.root_path / "diagrams").resolve()),
                str((job.root_path / "diagrams" / "png").resolve()),
            ]
        )
        extra_args = ["--standalone", f"--resource-path={resource_path}"]
        if job.config.get("generateTOC", True):
            extra_args.append("--toc")

        def _write(target: Path) -> None:
            pypandoc.convert_text(
                content,
                "docx",
                format="md",
                outputfile=str(target),
                extra_args=extra_args,
            )

        write_via_temp(job.output_path, _write)
