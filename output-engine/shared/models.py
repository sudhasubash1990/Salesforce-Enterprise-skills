"""Data models for the Output Engine."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class ConversionJob:
    """Input for a single markdown-to-office conversion."""

    source_path: Path
    output_path: Path
    root_path: Path
    rel_path: str
    format: str
    meta: dict[str, Any]
    body: str
    config: dict[str, Any]


@dataclass
class ConversionResult:
    """Result of a conversion attempt."""

    source: str
    target: str
    format: str
    status: str
    error: str | None = None
    converter: str | None = None
    warnings: list[str] = field(default_factory=list)
