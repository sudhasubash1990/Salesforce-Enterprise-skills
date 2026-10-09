"""Machine-testable validation for SEACF Framework Core P0+P1 contracts."""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
REGISTRY_PATH = Path(__file__).resolve().parent / "framework_core_contract_registry.yaml"
MANIFEST_PATH = REPO / "framework-core" / "tier-0-manifest.yaml"

SCRIPT = Path(__file__).resolve().parent / "retrieve_context.py"
spec = importlib.util.spec_from_file_location("retrieve_context", SCRIPT)
mod = importlib.util.module_from_spec(spec)
sys.modules["retrieve_context"] = mod
spec.loader.exec_module(mod)

CLAIMS_SCRIPT = Path(__file__).resolve().parent / "validate_claim_records.py"
claims_spec = importlib.util.spec_from_file_location("validate_claim_records", CLAIMS_SCRIPT)
claims_mod = importlib.util.module_from_spec(claims_spec)
sys.modules["validate_claim_records"] = claims_mod
claims_spec.loader.exec_module(claims_mod)


def _load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    assert isinstance(data, dict), f"Expected mapping in {path}"
    return data


def _count_must(text: str) -> int:
    return len(re.findall(r"\bMUST(?:\s+NOT)?\b", text))


def test_tier0_manifest_exists_and_paths_present():
    assert MANIFEST_PATH.is_file(), f"Missing {MANIFEST_PATH}"
    manifest = _load_yaml(MANIFEST_PATH)
    always = manifest.get("always_load") or []
    on_demand = manifest.get("recommended_on_demand") or []
    assert len(always) >= 4, "always_load must include baseline Tier-0 paths"
    missing = [p for p in always + on_demand if not (REPO / p).is_file()]
    assert not missing, f"Manifest references missing files: {missing}"


def test_retrieve_context_tier0_matches_manifest():
    manifest = _load_yaml(MANIFEST_PATH)
    expected = list(manifest["always_load"])
    assert mod.TIER0_CORE == expected, (
        "retrieve_context.TIER0_CORE drifted from framework-core/tier-0-manifest.yaml"
    )


def test_registry_contracts_pass():
    registry = _load_yaml(REGISTRY_PATH)
    failures: list[str] = []
    for entry in registry.get("contracts") or []:
        rel = entry["path"]
        path = REPO / rel
        if not path.is_file():
            failures.append(f"{rel}: file missing")
            continue
        text = path.read_text(encoding="utf-8")
        must_count = _count_must(text)
        min_must = int(entry.get("min_must_count") or 0)
        if must_count < min_must:
            failures.append(f"{rel}: MUST count {must_count} < min {min_must}")
        for needle in entry.get("required_substrings") or []:
            if needle not in text:
                failures.append(f"{rel}: missing substring {needle!r}")
        for pattern in entry.get("required_patterns") or []:
            if not re.search(pattern, text):
                failures.append(f"{rel}: pattern not matched: {pattern}")
    assert not failures, "Contract registry failures:\n" + "\n".join(failures)


def test_tool_manifest_schema_parses_and_has_required_fields():
    registry = _load_yaml(REGISTRY_PATH)
    rel = registry["tool_manifest_schema_path"]
    path = REPO / rel
    assert path.is_file(), f"Missing {rel}"
    data = _load_yaml(path)
    # Schema documents expected keys under required_fields or example.
    required = data.get("required_fields") or data.get("fields") or []
    if isinstance(required, dict):
        keys = set(required.keys())
    else:
        keys = {item if isinstance(item, str) else item.get("name") for item in required}
        keys.discard(None)
    expected = {
        "name",
        "description",
        "risk_tier",
        "allowed_skills",
        "required_inputs",
        "data_classes_allowed",
        "approval_required",
        "side_effects",
        "idempotency",
        "retry_policy",
        "timeout_or_failure_behavior",
        "audit_fields",
    }
    missing = expected - keys
    assert not missing, f"tool-manifest-schema.yaml missing fields: {sorted(missing)}"


def test_adversarial_scenarios_and_fixtures_exist():
    registry = _load_yaml(REGISTRY_PATH)
    rel = registry["adversarial_scenarios_path"]
    path = REPO / rel
    assert path.is_file(), f"Missing {rel}"
    data = _load_yaml(path)
    scenarios = data.get("scenarios") or []
    assert len(scenarios) >= 5, "Expected at least 5 adversarial scenarios from P0 spec"
    missing_fixtures = []
    for sc in scenarios:
        assert sc.get("id"), "scenario missing id"
        assert sc.get("expected_behavior"), f"{sc.get('id')}: missing expected_behavior"
        fixture = sc.get("fixture")
        if fixture and not (REPO / fixture).is_file():
            missing_fixtures.append(f"{sc['id']}: {fixture}")
    assert not missing_fixtures, f"Missing adversarial fixtures: {missing_fixtures}"


def test_prompt_injection_doc_references_scenario_ids():
    registry = _load_yaml(REGISTRY_PATH)
    scenarios_path = REPO / registry["adversarial_scenarios_path"]
    data = _load_yaml(scenarios_path)
    ids = [sc["id"] for sc in data.get("scenarios") or []]
    defence = (REPO / "framework-core/security/prompt-injection-defence.md").read_text(
        encoding="utf-8"
    )
    missing = [sid for sid in ids if sid not in defence]
    assert not missing, f"prompt-injection-defence.md missing scenario ids: {missing}"


def test_execution_states_graph():
    registry = _load_yaml(REGISTRY_PATH)
    rel = registry["execution_states_path"]
    data = _load_yaml(REPO / rel)
    required = data.get("required_state_names") or []
    states = data.get("states") or {}
    missing = [s for s in required if s not in states]
    assert not missing, f"execution-states.yaml missing states: {missing}"
    for name, meta in states.items():
        assert "allowed_next" in meta, f"{name}: missing allowed_next"
        for nxt in meta["allowed_next"]:
            assert nxt in states, f"{name}: unknown next state {nxt}"
    exec_meta = states["EXECUTING_ACTION"]
    preds = exec_meta.get("predecessors_for_entry") or []
    assert "HUMAN_APPROVAL_REQUIRED" in preds
    assert "risk_tier_assigned" in (exec_meta.get("requires") or [])
    assert states["COMPLETED"].get("requires_validators_passed") is True
    # COMPLETED must not be the only exit from VALIDATING on failure path
    assert "FAILED_SAFELY" in states["VALIDATING"]["allowed_next"]


def test_trace_schema_required_fields():
    registry = _load_yaml(REGISTRY_PATH)
    rel = registry["trace_schema_path"]
    data = _load_yaml(REPO / rel)
    required = set(data.get("required_fields") or [])
    expected = {
        "trace_id",
        "request_class",
        "selected_skills",
        "evidence_ids",
        "assumptions",
        "policy_decisions",
        "tool_events",
        "approval_events",
        "validation_results",
        "output_artifacts",
        "status",
    }
    assert expected <= required, f"trace-schema missing fields: {sorted(expected - required)}"
    # Optional diagnostic fields must not be promoted into required_fields
    optional = set(data.get("optional_fields") or [])
    for opt in (
        "context_bundles",
        "routing_outcome",
        "unresolved_unknowns",
        "human_review_triggers",
    ):
        assert opt in optional, f"trace-schema missing optional field {opt}"
        assert opt not in required, f"optional field {opt} must not be required"
    prohibited = data.get("prohibited") or []
    assert any("chain" in str(p).lower() or "reasoning" in str(p).lower() for p in prohibited)


def test_handoff_schema_and_fixture():
    registry = _load_yaml(REGISTRY_PATH)
    schema_rel = registry["handoff_schema_path"]
    fixture_rel = registry["handoff_fixture_path"]
    schema = _load_yaml(REPO / schema_rel)
    for key in (
        "required_ba_fields",
        "required_qe_fields",
        "constraints",
    ):
        assert key in schema, f"handoff schema missing {key}"
    assert "requirement_id" in (schema.get("required_ba_fields") or [])
    assert schema.get("constraints", {}).get("assumption_must_not_become_requirement") is True

    handoff_spec = importlib.util.spec_from_file_location(
        "validate_handoff_pack", REPO / "scripts" / "validate_handoff_pack.py"
    )
    handoff_mod = importlib.util.module_from_spec(handoff_spec)
    handoff_spec.loader.exec_module(handoff_mod)
    errors = handoff_mod.validate_handoff_pack(REPO / fixture_rel, schema)
    assert not errors, "HANDOFF-001 fixture failed validation:\n" + "\n".join(errors)


def test_ai_reliability_scenarios_cover_suites_and_fixtures():
    registry = _load_yaml(REGISTRY_PATH)
    rel = registry["ai_reliability_scenarios_path"]
    data = _load_yaml(REPO / rel)
    suites = set(data.get("suites") or [])
    expected_suites = {
        "grounding",
        "injection",
        "context",
        "tool_safety",
        "hallucination",
        "conflict",
        "privacy",
        "routing",
        "regression",
        "cross_module",
    }
    assert expected_suites <= suites, f"missing suites: {sorted(expected_suites - suites)}"
    scenarios = data.get("scenarios") or []
    by_suite: dict[str, int] = {}
    missing_fixtures: list[str] = []
    for sc in scenarios:
        suite = sc.get("suite")
        by_suite[suite] = by_suite.get(suite, 0) + 1
        fixture = sc.get("fixture")
        if fixture and not (REPO / fixture).is_file():
            missing_fixtures.append(f"{sc.get('id')}: {fixture}")
    assert not missing_fixtures, f"Missing reliability fixtures: {missing_fixtures}"
    for suite in expected_suites:
        assert by_suite.get(suite, 0) >= 1, f"suite {suite} has no scenarios"
    handoff_ids = [sc.get("id") for sc in scenarios if sc.get("id") == "HANDOFF-001"]
    assert handoff_ids, "HANDOFF-001 scenario missing from ai-reliability-scenarios.yaml"


def test_negative_claim_fixture_fails_validation():
    registry = _load_yaml(REGISTRY_PATH)
    rel = registry["claim_negative_fixture_path"]
    path = REPO / rel
    assert path.is_file(), f"Missing {rel}"
    errors = claims_mod.validate_claim_file(path)
    assert errors, "verified-sla-no-source.yaml must fail claim validation"


def test_skill_contract_schema_and_module_contracts():
    registry = _load_yaml(REGISTRY_PATH)
    schema_rel = registry["skill_contract_schema_path"]
    schema = _load_yaml(REPO / schema_rel)
    required = set(schema.get("required_fields") or [])
    expected = {
        "name",
        "version",
        "purpose",
        "triggers",
        "non_triggers",
        "required_inputs",
        "optional_inputs",
        "context_required",
        "authoritative_sources",
        "grounding_policy",
        "allowed_tools",
        "max_action_risk",
        "human_approval_conditions",
        "outputs",
        "assumptions_policy",
        "validation_checks",
        "failure_conditions",
        "related_skills",
    }
    assert expected <= required, f"skill schema missing: {sorted(expected - required)}"
    for rel in registry.get("module_skill_contracts") or []:
        path = REPO / rel
        assert path.is_file(), f"Missing module skill contract {rel}"
        data = _load_yaml(path)
        skill = data.get("skill") or data
        missing = [f for f in expected if f not in skill]
        assert not missing, f"{rel} missing skill fields: {missing}"
        risk = skill.get("max_action_risk")
        assert risk in (schema.get("max_action_risk_enum") or ["T0", "T1", "T2", "T3", "T4"])
