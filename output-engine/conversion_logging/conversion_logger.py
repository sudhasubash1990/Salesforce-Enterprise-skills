"""Conversion logging and reporting."""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from shared.models import ConversionResult


class ConversionLogger:
    """Enterprise logging for conversion runs."""

    def __init__(self, root: Path, level: str = "INFO") -> None:
        self.root = root
        self.results: list[ConversionResult] = []
        self.log_path = root / "conversion.log"
        self.report_path = root / "conversion_report.json"
        logging.basicConfig(
            filename=self.log_path,
            level=getattr(logging, level.upper(), logging.INFO),
            format="%(asctime)s %(levelname)s %(message)s",
            force=True,
        )
        self.logger = logging.getLogger("output_engine")

    def log_result(self, result: ConversionResult) -> None:
        self.results.append(result)
        if result.status == "success":
            self.logger.info("Converted %s -> %s (%s)", result.source, result.target, result.format)
        elif result.status == "skipped":
            self.logger.warning("Skipped %s: %s", result.source, result.error)
        else:
            self.logger.error("Failed %s: %s", result.source, result.error)

    def write_report(self) -> dict[str, Any]:
        report = {
            "generatedAt": datetime.now(timezone.utc).isoformat(),
            "root": str(self.root),
            "total": len(self.results),
            "success": sum(1 for r in self.results if r.status == "success"),
            "failed": sum(1 for r in self.results if r.status == "failed"),
            "skipped": sum(1 for r in self.results if r.status == "skipped"),
            "conversions": [
                {
                    "source": r.source,
                    "target": r.target,
                    "format": r.format,
                    "status": r.status,
                    "converter": r.converter,
                    "error": r.error,
                    "warnings": r.warnings,
                }
                for r in self.results
            ],
        }
        self.report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        return report
