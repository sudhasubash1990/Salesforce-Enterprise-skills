"""Tests for the deterministic context retriever."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "retrieve_context.py"
spec = importlib.util.spec_from_file_location("retrieve_context", SCRIPT)
mod = importlib.util.module_from_spec(spec)
sys.modules["retrieve_context"] = mod
spec.loader.exec_module(mod)


def test_all_rule_seeds_exist():
    """Every seed referenced by any rule must exist in the repository."""
    missing = []
    for rule in mod.TASK_RULES + mod.CLOUD_RULES + mod.INDUSTRY_RULES:
        for seed in rule["seeds"]:
            if not (mod.REPO / seed).exists():
                missing.append(f"{rule.get('task') or rule.get('cloud') or rule.get('industry')}: {seed}")
    for seed in mod.ALWAYS_LOAD:
        if not (mod.REPO / seed).exists():
            missing.append(f"ALWAYS_LOAD: {seed}")
    assert not missing, f"Rules reference missing files: {missing}"


def test_user_story_query_routes_correctly():
    result = mod.retrieve("create a user story with acceptance criteria")
    assert "user-story" in result["matched_tasks"]
    files = result["files"]
    assert "salesforce-business-analyst/templates/user-story-template.md" in files
    assert "salesforce-business-analyst/knowledge/user-stories.md" in files
    assert ".cursor/rules/userstory-generation.mdc" in files


def test_core_bundle_always_present():
    result = mod.retrieve("create a user story")
    for core in mod.ALWAYS_LOAD:
        assert core in result["files"], f"core file missing from bundle: {core}"


def test_service_cloud_detection():
    result = mod.retrieve("record complaints as cases in Service Cloud")
    assert "Service Cloud" in result["matched_clouds"]
    assert "salesforce-business-analyst/knowledge/service-cloud-patterns.md" in result["files"]


def test_industry_directory_expansion():
    result = mod.retrieve("fit-gap for utilities meter-to-cash")
    assert "utilities" in result["matched_industries"]
    assert "salesforce-business-analyst/scenarios/utilities/meter-to-cash.md" in result["files"]


def test_unmatched_query_returns_fallback():
    result = mod.retrieve("what is the weather today")
    assert result["matched_tasks"] == []
    assert set(result["files"]) >= set(mod.ALWAYS_LOAD)
    # Fallback should stay small — Tier-0 + BA core plus at most a few graph hops.
    assert len(result["files"]) < 25


def test_qe_redirect_for_quality_engineering():
    result = mod.retrieve("draft a Salesforce test strategy using the QE enterprise orchestrator")
    assert result["matched_tasks"] == ["qe-redirect"]
    assert result.get("redirect") == "salesforce-quality-engineering"
    assert "salesforce-quality-engineering/skill.md" in result["files"]
    assert "framework-core/README.md" in result["files"]
    assert "salesforce-business-analyst/templates/user-story-template.md" not in result["files"]


def test_ba_uat_not_redirected_to_qe():
    result = mod.retrieve("create UAT test scenarios for the billing user story")
    assert "qe-redirect" not in result["matched_tasks"]
    assert result.get("redirect") is None


def test_no_duplicates_in_bundle():
    result = mod.retrieve("user story for banking loan with fit-gap and UAT")
    assert len(result["files"]) == len(set(result["files"]))


def test_bundle_is_deterministic():
    query = "create user stories for insurance FNOL intake"
    assert mod.retrieve(query)["files"] == mod.retrieve(query)["files"]


def test_no_expand_produces_subset():
    query = "create a user story"
    expanded = mod.retrieve(query, expand=True)["files"]
    seeds_only = mod.retrieve(query, expand=False)["files"]
    assert set(seeds_only) <= set(expanded)
    assert len(seeds_only) <= len(expanded)


def test_missing_report_empty_for_known_queries():
    result = mod.retrieve("brd with fit-gap, raid log, uat plan and data migration")
    assert result["missing"] == []


def test_kpi_baseline_query_routes_correctly():
    result = mod.retrieve("define KPI baselines and target outcomes for downtime and reconciliation")
    assert "kpi-baseline" in result["matched_tasks"]
    assert "salesforce-business-analyst/templates/kpi-baseline-template.md" in result["files"]


def test_change_management_query_routes_correctly():
    result = mod.retrieve("change management strategy to handle resistance and upskilling of operations team")
    assert "change-management" in result["matched_tasks"]
    files = result["files"]
    assert "salesforce-business-analyst/playbooks/change-management-playbook.md" in files
    assert "salesforce-business-analyst/templates/comms-upskilling-plan-template.md" in files


def test_digital_transformation_query_routes_correctly():
    result = mod.retrieve("digital reinvention strategy with digital-first architecture and automation strategy")
    assert "digital-transformation" in result["matched_tasks"]
    files = result["files"]
    assert "salesforce-business-analyst/playbooks/digital-transformation-strategy-playbook.md" in files
    assert "salesforce-business-analyst/templates/kpi-baseline-template.md" in files
