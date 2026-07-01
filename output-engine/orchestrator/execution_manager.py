"""Conversion execution with retry and skip logic."""

from __future__ import annotations

import time
from pathlib import Path

from configuration.config_loader import FORMAT_EXTENSIONS, resolve_format
from converters.excel_converter import ExcelConverter
from converters.pdf_converter import PDFConverter
from converters.ppt_converter import PPTConverter
from converters.word_converter import WordConverter
from shared.converter_interface import DocumentConverter
from shared.markdown_parser import parse_frontmatter
from shared.models import ConversionJob, ConversionResult


class ExecutionManager:
    """Runs conversions with retry and overwrite handling."""

    def __init__(self, config: dict, routing_rules: dict) -> None:
        self.config = config
        self.routing_rules = routing_rules
        self.retry_count = int(config.get("retryCount", 2))
        self._converters: dict[str, DocumentConverter] = {
            "docx": WordConverter(),
            "pdf": PDFConverter(),
            "pptx": PPTConverter(),
            "xlsx": ExcelConverter(),
        }

    def _get_converter(self, fmt: str) -> DocumentConverter:
        converter = self._converters.get(fmt)
        if not converter:
            raise ValueError(f"Unsupported format: {fmt}")
        return converter

    def process_file(
        self,
        md_path: Path,
        root: Path,
        outputs_root: Path,
        project_override: dict | None,
    ) -> ConversionResult:
        rel = md_path.relative_to(root).as_posix()
        text = md_path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        fmt = resolve_format(rel, meta, project_override, self.routing_rules)
        ext = FORMAT_EXTENSIONS[fmt]
        out_path = md_path.with_suffix(ext)

        if out_path.exists() and not self.config.get("overwrite", False):
            return ConversionResult(
                source=rel,
                target=out_path.relative_to(root).as_posix(),
                format=fmt,
                status="skipped",
                error="target exists and overwrite=false",
            )

        job = ConversionJob(
            source_path=md_path,
            output_path=out_path,
            root_path=root,
            rel_path=rel,
            format=fmt,
            meta=meta,
            body=body,
            config=self.config,
        )

        converter = self._get_converter(fmt)
        last_result: ConversionResult | None = None
        for attempt in range(self.retry_count + 1):
            result = converter.run(job)
            last_result = result
            if result.status == "success":
                return result
            if attempt < self.retry_count:
                time.sleep(1)
        return last_result or ConversionResult(source=rel, target="", format=fmt, status="failed", error="unknown")
