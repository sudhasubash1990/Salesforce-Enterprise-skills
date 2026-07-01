"""Tests for format routing."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_DIR))

from configuration.config_loader import load_routing_rules, resolve_format  # noqa: E402


@pytest.fixture
def routing_rules():
    return load_routing_rules()


def test_brd_routes_to_pdf(routing_rules):
    fmt = resolve_format("03-requirements/brd.md", {"document_type": "BRD"}, None, routing_rules)
    assert fmt == "pdf"


def test_presentation_routes_to_pptx(routing_rules):
    fmt = resolve_format(
        "08-executive/deck.md",
        {"document_type": "Presentation Outline"},
        None,
        routing_rules,
    )
    assert fmt == "pptx"


def test_raid_log_routes_to_xlsx(routing_rules):
    fmt = resolve_format(
        "04-governance/raid-log.md",
        {"document_type": "RAID Log"},
        None,
        routing_rules,
    )
    assert fmt == "xlsx"


def test_default_routes_to_docx(routing_rules):
    fmt = resolve_format("01-discovery/scope.md", {"document_type": "Scope Document"}, None, routing_rules)
    assert fmt == "docx"


def test_project_override_takes_precedence(routing_rules):
    override = {"routes": {"custom.md": "pptx"}, "fallbackRules": [{"default": "docx"}]}
    fmt = resolve_format("custom.md", {}, override, routing_rules)
    assert fmt == "pptx"
