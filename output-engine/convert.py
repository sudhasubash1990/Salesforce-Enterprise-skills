#!/usr/bin/env python3
"""CLI entry point for the Enterprise Output Engine."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ENGINE_DIR))

from orchestrator.output_orchestrator import OutputOrchestrator  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Output Engine — convert markdown to office formats")
    parser.add_argument("--root", help="Root folder to scan for markdown files")
    parser.add_argument("--file", help="Convert a single markdown file (post-write hook)")
    parser.add_argument("--config", default=str(ENGINE_DIR / "output-config.json"), help="Config path")
    parser.add_argument("--routing-rules", default=str(ENGINE_DIR / "configuration" / "routing_rules.json"))
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing outputs")
    args = parser.parse_args()

    if not args.root and not args.file:
        parser.error("Either --root or --file is required")

    orchestrator = OutputOrchestrator(
        config_path=Path(args.config),
        routing_rules_path=Path(args.routing_rules),
    )

    root = Path(args.root).resolve() if args.root else None
    single = Path(args.file).resolve() if args.file else None

    if single and not single.is_file():
        print(f"File not found: {single}", file=sys.stderr)
        return 1

    report = orchestrator.run(root=root, single_file=single, overwrite=args.overwrite)
    print(
        json.dumps(
            {
                "report": str(Path(report["root"]) / "conversion_report.json"),
                "success": report["success"],
                "failed": report["failed"],
                "skipped": report["skipped"],
            },
            indent=2,
        )
    )
    return 0 if report["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
