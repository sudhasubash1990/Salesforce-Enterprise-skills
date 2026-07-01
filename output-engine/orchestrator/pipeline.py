"""Conversion pipeline stages."""

from __future__ import annotations

from pathlib import Path

from configuration.config_loader import find_project_override
from conversion_logging.conversion_logger import ConversionLogger
from orchestrator.execution_manager import ExecutionManager
from shared.models import ConversionResult


class ConversionPipeline:
    """Discover, validate, route, convert, and report."""

    def __init__(self, config: dict, routing_rules: dict) -> None:
        self.config = config
        self.routing_rules = routing_rules
        self.executor = ExecutionManager(config, routing_rules)

    def discover(self, root: Path, single_file: Path | None = None) -> list[Path]:
        if single_file:
            return [single_file.resolve()]
        if self.config.get("recursiveScan", True):
            return sorted(root.rglob("*.md"))
        return sorted(root.glob("*.md"))

    def validate(self, md_path: Path) -> list[str]:
        warnings: list[str] = []
        if not md_path.is_file():
            warnings.append(f"File not found: {md_path}")
            return warnings
        try:
            text = md_path.read_text(encoding="utf-8")
            if not text.strip():
                warnings.append(f"Empty file: {md_path}")
        except UnicodeDecodeError:
            warnings.append(f"Invalid UTF-8: {md_path}")
        return warnings

    def run(self, root: Path, single_file: Path | None = None) -> dict:
        root = root.resolve()
        outputs_root = root
        if "outputs" in root.parts:
            idx = root.parts.index("outputs")
            outputs_root = Path(*root.parts[: idx + 1])

        logger = ConversionLogger(root, self.config.get("loggingLevel", "INFO"))
        project_override = find_project_override(
            single_file or root, outputs_root if outputs_root.is_dir() else root
        )
        if project_override is None and root.name != "outputs":
            override_path = root / "format-routing.json"
            if override_path.is_file():
                import json

                project_override = json.loads(override_path.read_text(encoding="utf-8"))

        files = self.discover(root, single_file)
        for md_path in files:
            warnings = self.validate(md_path)
            if any("not found" in w or "Invalid UTF-8" in w for w in warnings):
                result = ConversionResult(
                    source=str(md_path),
                    target="",
                    format="",
                    status="failed",
                    error="; ".join(warnings),
                )
                logger.log_result(result)
                continue
            result = self.executor.process_file(md_path, root, outputs_root, project_override)
            result.warnings = warnings
            logger.log_result(result)

        return logger.write_report()
