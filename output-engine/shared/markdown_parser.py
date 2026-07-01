"""Reusable markdown parsing utilities."""

from __future__ import annotations

import re
from typing import Any

import yaml

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
SLIDE_RE = re.compile(r"^##\s+Slide\s+(\d+)\s*[—\-]\s*(.+)$", re.MULTILINE)
TABLE_ROW_RE = re.compile(r"^\|(.+)\|\s*$")
TABLE_SEP_RE = re.compile(r"^\|[\s\-:|]+\|\s*$")


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    meta = yaml.safe_load(match.group(1)) or {}
    body = text[match.end() :]
    return meta, body


def parse_table_block(lines: list[str]) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in lines:
        if not TABLE_ROW_RE.match(line):
            continue
        if TABLE_SEP_RE.match(line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append(cells)
    return rows


def extract_sections(body: str) -> list[tuple[str, str]]:
    parts = re.split(r"^(##\s+.+)$", body, flags=re.MULTILINE)
    if not parts:
        return [("", body)]
    sections: list[tuple[str, str]] = []
    if parts[0].strip():
        sections.append(("Introduction", parts[0]))
    i = 1
    while i < len(parts):
        heading = parts[i].strip().lstrip("#").strip()
        content = parts[i + 1] if i + 1 < len(parts) else ""
        sections.append((heading, content))
        i += 2
    return sections


def sanitize_sheet_name(name: str) -> str:
    invalid = ":\\/?*[]"
    cleaned = "".join(c for c in name if c not in invalid)[:31]
    return cleaned or "Sheet1"


def parse_key_value_block(block: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in block.splitlines():
        m = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", line.strip())
        if m:
            data[m.group(1).strip()] = m.group(2).strip()
    rows = parse_table_block([line for line in block.splitlines() if line.strip().startswith("|")])
    for row in rows:
        if len(row) >= 2:
            key = row[0].strip("* ")
            data[key] = row[1]
    return data


def parse_user_stories(body: str) -> list[dict[str, str]]:
    stories: list[dict[str, str]] = []
    chunks = re.split(r"^###\s+(US-\d+):\s*(.+)$", body, flags=re.MULTILINE)
    i = 1
    while i < len(chunks):
        us_id = chunks[i]
        title = chunks[i + 1].strip()
        block = chunks[i + 2] if i + 2 < len(chunks) else ""
        i += 3
        as_a = i_want = so_that = refs = ac = priority = ""
        m = re.search(
            r"\*\*As a\*\*\s*(.+?),\s*\n\*\*I want\*\*\s*(.+?),\s*\n\*\*So that\*\*\s*(.+?)(?:\.|\n)",
            block,
            re.DOTALL | re.IGNORECASE,
        )
        if m:
            as_a, i_want, so_that = (x.strip() for x in m.groups())
        m2 = re.search(r"\*\*Requirement refs?:\*\*\s*(.+)$", block, re.MULTILINE | re.IGNORECASE)
        if m2:
            refs = m2.group(1).strip()
        m3 = re.search(r"\*\*Priority:\*\*\s*(\w+)", block, re.IGNORECASE)
        if m3:
            priority = m3.group(1)
        ac_lines = re.findall(r"^\d+\.\s+Given\s+.+$", block, re.MULTILINE | re.IGNORECASE)
        ac = "\n".join(ac_lines)
        stories.append(
            {
                "US-ID": us_id,
                "Title": title,
                "As a": as_a,
                "I want": i_want,
                "So that": so_that,
                "Priority": priority,
                "Requirement refs": refs,
                "Acceptance Criteria": ac,
            }
        )
    return stories


def parse_test_scenarios(body: str) -> list[dict[str, str]]:
    scenarios: list[dict[str, str]] = []
    chunks = re.split(r"^###\s+(TS-\d+):\s*(.+)$", body, flags=re.MULTILINE)
    i = 1
    while i < len(chunks):
        ts_id = chunks[i]
        title = chunks[i + 1].strip()
        block = chunks[i + 2] if i + 2 < len(chunks) else ""
        i += 3
        kv = parse_key_value_block(block)
        steps = ""
        m = re.search(r"\*\*Test steps:\*\*\s*\n((?:\d+\..+\n?)+)", block, re.IGNORECASE)
        if m:
            steps = m.group(1).strip()
        scenarios.append(
            {
                "TS-ID": ts_id,
                "Title": title,
                "Release": kv.get("Release", ""),
                "Priority": kv.get("Priority", ""),
                "Business Scenario": kv.get("Business scenario description", ""),
                "Preconditions": kv.get("Preconditions", ""),
                "Test Steps": steps,
                "Expected Result": kv.get("Expected result", ""),
                "Linked Requirements": kv.get("Linked requirements", ""),
            }
        )
    return scenarios


def build_cover_md(meta: dict[str, Any]) -> str:
    title = meta.get("title", "Document")
    lines = [
        f"% {title}",
        "",
        f"**Project:** {meta.get('project', '')}  ",
        f"**Version:** {meta.get('version', '')}  ",
        f"**Status:** {meta.get('review_status', meta.get('status', ''))}  ",
        f"**Date:** {meta.get('last_updated', meta.get('created_date', ''))}  ",
        "",
        "\\newpage",
        "",
    ]
    return "\n".join(lines)
