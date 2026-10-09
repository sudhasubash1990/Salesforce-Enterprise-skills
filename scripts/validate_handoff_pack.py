"""Validate a BA→QE handoff pack against framework-core/handoffs/ba-qe-handoff-schema.yaml."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO / "framework-core" / "handoffs" / "ba-qe-handoff-schema.yaml"


def _load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping in {path}")
    return data


def validate_handoff_pack(path: Path, schema: dict | None = None) -> list[str]:
    """Return list of validation errors (empty = pass)."""
    schema = schema or _load_yaml(SCHEMA_PATH)
    data = _load_yaml(path)
    errors: list[str] = []

    ba = data.get("ba_output") or data.get("ba") or {}
    if not ba and data.get("requirement_id"):
        ba = data
    if not isinstance(ba, dict) or not ba:
        errors.append("missing ba_output (or top-level BA fields)")
        return errors

    for field in schema.get("required_ba_fields") or []:
        if field not in ba:
            errors.append(f"ba_output missing required field: {field}")

    ac = ba.get("acceptance_criteria") or []
    if not isinstance(ac, list) or len(ac) < 1:
        errors.append("acceptance_criteria must be a non-empty list")
    else:
        for i, item in enumerate(ac):
            if not isinstance(item, dict) or "id" not in item or "statement" not in item:
                errors.append(f"acceptance_criteria[{i}] must have id and statement")

    assumptions = ba.get("assumptions") or []
    if not isinstance(assumptions, list):
        errors.append("assumptions must be a list")
    else:
        for i, item in enumerate(assumptions):
            if not isinstance(item, dict):
                errors.append(f"assumptions[{i}] must be a mapping")
                continue
            for key in ("id", "statement", "validation_needed"):
                if key not in item:
                    errors.append(f"assumptions[{i}] missing {key}")

    evidence = ba.get("evidence_refs") or []
    if not isinstance(evidence, list):
        errors.append("evidence_refs must be a list")
    else:
        for i, item in enumerate(evidence):
            if not isinstance(item, dict) or "id" not in item or "source_ref" not in item:
                errors.append(f"evidence_refs[{i}] must have id and source_ref")

    # Optional QE sample — when present, enforce ID preservation and assumption rules
    qe = data.get("sample_qe_input") or data.get("qe_input") or data.get("qe")
    expected = data.get("qe_expected") or {}
    if qe and isinstance(qe, dict):
        for field in schema.get("required_qe_fields") or []:
            if field not in qe:
                errors.append(f"sample_qe_input missing required field: {field}")

        must_preserve = expected.get("must_preserve_ids") or [ba.get("requirement_id")]
        must_preserve = [x for x in must_preserve if x]
        blob = yaml.dump(qe, default_flow_style=False)
        for rid in must_preserve:
            if str(rid) not in blob:
                errors.append(f"QE pack does not preserve id {rid!r}")

        must_not = expected.get("must_not_promote_to_requirement") or []
        req_ids = {ba.get("requirement_id")}
        for ac_item in ac if isinstance(ac, list) else []:
            if isinstance(ac_item, dict) and ac_item.get("id"):
                req_ids.add(ac_item["id"])
        for aid in must_not:
            # Assumption IDs must not appear as requirement_id on scenarios
            for sc in qe.get("test_scenarios") or []:
                if not isinstance(sc, dict):
                    continue
                linked = sc.get("linked_requirement_ids") or []
                if aid in linked:
                    errors.append(
                        f"assumption {aid} promoted into linked_requirement_ids on {sc.get('id')}"
                    )

        if expected.get("coverage_gaps_required") and not (qe.get("coverage_gaps") or []):
            errors.append("coverage_gaps required but missing or empty")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        nargs="?",
        default=str(REPO / "framework-core/evaluation/fixtures/handoff-001-ba-story-pack.yaml"),
        help="Path to handoff pack YAML",
    )
    args = parser.parse_args(argv)
    path = Path(args.path)
    if not path.is_file():
        print(f"FAIL: file not found: {path}", file=sys.stderr)
        return 1
    errors = validate_handoff_pack(path)
    if errors:
        print("FAIL:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"PASS: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
