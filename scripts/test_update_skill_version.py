"""Tests for scripts/update_skill_version.py"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "update_skill_version.py"

spec = importlib.util.spec_from_file_location("update_skill_version", SCRIPT)
mod = importlib.util.module_from_spec(spec)
sys.modules["update_skill_version"] = mod
assert spec.loader is not None
spec.loader.exec_module(mod)


def test_parse_conventional_feat_minor():
    bump, summary = mod.parse_commit_message("feat(ba): ADO backlog integration and estimation discipline")
    assert bump == "minor"
    assert "ADO backlog" in summary


def test_parse_conventional_fix_patch():
    bump, summary = mod.parse_commit_message("fix(ba): nested AC bullet formatting")
    assert bump == "patch"
    assert summary == "nested AC bullet formatting"


def test_parse_breaking_major():
    bump, _ = mod.parse_commit_message("feat!: remove legacy story template")
    assert bump == "major"


def test_bump_semver():
    assert mod.bump_semver("1.4.0", "patch") == "1.4.1"
    assert mod.bump_semver("1.4.0", "minor") == "1.5.0"
    assert mod.bump_semver("1.4.0", "major") == "2.0.0"


def test_upsert_version_history_inserts_row():
    text = """## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.3.0 | 2026-07-02 | Lead | Old |
"""
    row = mod.VersionUpdate(
        old_version="1.3.0",
        new_version="1.4.0",
        summary="ADO backlog integration",
        bump="minor",
        author="Tester",
        updated_date="2026-07-02",
    )
    out = mod.upsert_version_history(text, row)
    assert "| 1.4.0 | 2026-07-02 | Tester | ADO backlog integration |" in out
    assert "| 1.3.0 |" in out


def test_read_version_from_skill():
    version = mod.read_version_from_skill()
    assert version == "1.4.0"
