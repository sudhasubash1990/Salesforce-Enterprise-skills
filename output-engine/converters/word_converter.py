"""Word document converter using Pandoc."""

from __future__ import annotations

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
        extra_args = ["--standalone"]
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
