"""Tests for markdown parser."""

from __future__ import annotations

import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_DIR))

from shared.markdown_parser import parse_frontmatter, parse_table_block, parse_user_stories  # noqa: E402


def test_parse_frontmatter():
    text = "---\ntitle: Test\ndocument_type: BRD\n---\n\n# Body\n"
    meta, body = parse_frontmatter(text)
    assert meta["title"] == "Test"
    assert meta["document_type"] == "BRD"
    assert body.strip().startswith("# Body")


def test_parse_table_block():
    lines = [
        "| A | B |",
        "|---|---|",
        "| 1 | 2 |",
    ]
    rows = parse_table_block(lines)
    assert rows == [["A", "B"], ["1", "2"]]


def test_parse_user_stories():
    body = """
### US-001: Test story

**As a** agent,
**I want** to test,
**So that** it works.

**Requirement refs:** BR-001

**Acceptance criteria:**
1. Given a test, when run, then pass.
"""
    stories = parse_user_stories(body)
    assert len(stories) == 1
    assert stories[0]["US-ID"] == "US-001"
    assert "agent" in stories[0]["As a"]
