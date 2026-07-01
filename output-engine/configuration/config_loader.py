"""Configuration loading and format routing."""

from __future__ import annotations

import fnmatch
import json
from pathlib import Path
from typing import Any

ENGINE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG_PATH = ENGINE_DIR / "output-config.json"
DEFAULT_ROUTING_RULES_PATH = ENGINE_DIR / "configuration" / "routing_rules.json"


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_config(path: Path | None = None) -> dict[str, Any]:
    return load_json(path or DEFAULT_CONFIG_PATH)


def load_routing_rules(path: Path | None = None) -> dict[str, Any]:
    return load_json(path or DEFAULT_ROUTING_RULES_PATH)


def find_project_override(md_path: Path, outputs_root: Path) -> dict[str, Any] | None:
    """Load outputs/<project>/format-routing.json if it exists."""
    try:
        rel = md_path.relative_to(outputs_root)
        parts = rel.parts
        if len(parts) < 2:
            project_dir = outputs_root / parts[0]
        else:
            project_dir = outputs_root / parts[0]
        override = project_dir / "format-routing.json"
        if override.is_file():
            return load_json(override)
    except ValueError:
        pass
    return None


def _match_filename_pattern(name: str, pattern: str) -> bool:
    if pattern.startswith("*") and pattern.endswith(".md"):
        return name.endswith(pattern[1:])
    return fnmatch.fnmatch(name, pattern)


def resolve_format(
    rel_path: str,
    meta: dict[str, Any],
    project_override: dict[str, Any] | None,
    routing_rules: dict[str, Any],
) -> str:
    """Resolve target format: project route -> generic rules -> docx."""
    if project_override:
        routes = project_override.get("routes", {})
        if rel_path in routes:
            return routes[rel_path]
        for rule in project_override.get("fallbackRules", []):
            if "default" in rule:
                continue
            pattern = rule.get("pattern", "")
            name = Path(rel_path).name
            if pattern == name or (pattern.startswith("*") and name.endswith(pattern[1:])):
                return rule["format"]

    doc_type = str(meta.get("document_type", ""))
    name = Path(rel_path).name.lower()

    for rule in routing_rules.get("rules", []):
        match_type = rule.get("match")
        if match_type == "default":
            return rule["format"]
        if match_type == "document_type_contains" and rule.get("value", "").lower() in doc_type.lower():
            return rule["format"]
        if match_type == "document_type_in" and doc_type in rule.get("value", []):
            return rule["format"]
        if match_type == "filename_pattern" and _match_filename_pattern(name, rule.get("value", "")):
            return rule["format"]
        if match_type == "filename_equals" and name == rule.get("value", ""):
            return rule["format"]
        if match_type == "filename_contains" and rule.get("value", "").lower() in name:
            return rule["format"]

    if project_override:
        for rule in project_override.get("fallbackRules", []):
            if "default" in rule:
                return rule["format"]

    return "docx"


FORMAT_EXTENSIONS = {"docx": ".docx", "pptx": ".pptx", "xlsx": ".xlsx", "pdf": ".pdf"}
