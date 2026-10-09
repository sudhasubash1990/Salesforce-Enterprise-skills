"""Validate SEACF claim records against Tier-0 claim-validation rules (no LLM)."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent

ELIGIBLE_FOR_VERIFIED = {"project-approved", "official-product"}
FAIL_CLASSIFICATIONS_NEEDING_SOURCE = {"verified", "requirement-derived"}


def load_claims(path: Path | str) -> list[dict[str, Any]]:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    if data is None:
        return []
    if isinstance(data, list):
        return [c for c in data if isinstance(c, dict)]
    if isinstance(data, dict):
        claims = data.get("claims") or data.get("claim_records") or []
        if isinstance(claims, dict):
            return [claims]
        return [c for c in claims if isinstance(c, dict)]
    raise ValueError(f"Unsupported claim file shape: {path}")


def validate_claim(claim: dict[str, Any]) -> list[str]:
    """Return list of validation error strings (empty = pass)."""
    errors: list[str] = []
    cid = claim.get("claim_id") or "<unknown>"
    classification = (claim.get("classification") or "").strip().lower()
    source_id = claim.get("source_id")
    source_class = (claim.get("source_class") or "").strip().lower()
    locator = claim.get("evidence_excerpt_or_locator")
    evidence_conf = (claim.get("evidence_confidence") or "").strip().lower()

    if classification in FAIL_CLASSIFICATIONS_NEEDING_SOURCE:
        if not source_id:
            errors.append(f"{cid}: {classification} requires source_id")
        if classification == "verified" and source_class not in ELIGIBLE_FOR_VERIFIED:
            errors.append(
                f"{cid}: verified requires eligible source_class "
                f"(project-approved|official-product), got {source_class!r}"
            )
        if classification == "verified" and not locator and not source_id:
            errors.append(f"{cid}: verified requires evidence locator or source_id")

    if classification == "assumption" and evidence_conf in {"high", "verified"}:
        errors.append(
            f"{cid}: evidence_confidence={evidence_conf!r} incompatible with assumption"
        )

    return errors


def validate_claim_file(path: Path | str) -> list[str]:
    errors: list[str] = []
    for claim in load_claims(path):
        errors.extend(validate_claim(claim))
    return errors


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Validate SEACF claim YAML records")
    parser.add_argument("paths", nargs="+", help="YAML claim files")
    args = parser.parse_args()
    all_errors: list[str] = []
    for p in args.paths:
        errs = validate_claim_file(p)
        if errs:
            all_errors.extend(f"{p}: {e}" for e in errs)
        else:
            print(f"PASS {p}")
    if all_errors:
        print("FAIL")
        for e in all_errors:
            print(e)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
