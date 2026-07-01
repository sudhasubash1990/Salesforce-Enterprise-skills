"""Central output orchestrator."""

from __future__ import annotations

import os
import shutil
from pathlib import Path

from configuration.config_loader import load_config, load_routing_rules
from orchestrator.pipeline import ConversionPipeline

ENGINE_DIR = Path(__file__).resolve().parent.parent


def ensure_pandoc_on_path() -> None:
    if shutil.which("pandoc") is None:
        for candidate in [
            Path(r"C:\Program Files\Pandoc\pandoc.exe"),
            Path.home() / "AppData/Local/Pandoc/pandoc.exe",
        ]:
            if candidate.exists():
                os.environ["PATH"] = str(candidate.parent) + os.pathsep + os.environ.get("PATH", "")
                break


class OutputOrchestrator:
    """Central controller for markdown-to-office conversion."""

    def __init__(
        self,
        config_path: Path | None = None,
        routing_rules_path: Path | None = None,
    ) -> None:
        self.config = load_config(config_path)
        self.routing_rules = load_routing_rules(routing_rules_path)
        self.pipeline = ConversionPipeline(self.config, self.routing_rules)

    @staticmethod
    def _resolve_project_root(md_path: Path) -> Path:
        candidate = md_path.parent
        while candidate.parent != candidate:
            if (candidate / "format-routing.json").is_file():
                return candidate
            if candidate.name == "outputs":
                return md_path.parent
            candidate = candidate.parent
        return md_path.parent

    def run(
        self,
        root: Path | None = None,
        single_file: Path | None = None,
        overwrite: bool = False,
    ) -> dict:
        ensure_pandoc_on_path()
        if overwrite:
            self.config["overwrite"] = True
        if single_file:
            single_file = single_file.resolve()
            scan_root = self._resolve_project_root(single_file)
            return self.pipeline.run(scan_root, single_file)
        input_folder = self.config.get("inputFolder", "outputs")
        scan_root = (root or Path(input_folder)).resolve()
        if not scan_root.is_dir():
            raise FileNotFoundError(f"Scan root not found: {scan_root}")
        return self.pipeline.run(scan_root)
