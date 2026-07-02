"""Validate Sprint 7 metadata, related sections, and relative links."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

SKIP_PATH_PARTS = {".cursor/plans", ".git"}
# Directories whose contents are generated, third-party, or internal-only —
# the enterprise document schema does not apply to them.
SKIP_DIRS = {
    ".pytest_cache",
    "outputs",
    "output-engine",
    "zzz_ImplmentationGuide",
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
}
SKIP_FULL = {"CHANGELOG.md", "changelog.md"}

REQUIRED_YAML = {"title", "module", "category", "document_type", "version", "review_status", "last_updated"}
SKILL_REQUIRED = {"name", "description", "version"}

MANDATORY_SECTIONS = [
    "Related Brain Modules",
    "Related Knowledge",
    "Related Templates",
    "Related Playbooks",
    "Related Industry Scenarios",
    "Related Interview Topics",
    "Related Examples",
    "Related Documents",
    "Version History",
]


def should_skip(path: Path) -> bool:
    posix = path.as_posix()
    if any(p in posix for p in SKIP_PATH_PARTS):
        return True
    rel_parts = path.relative_to(REPO).parts
    return any(part in SKIP_DIRS for part in rel_parts)


def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    if not content.startswith("---"):
        return {}, content
    end = content.find("\n---", 3)
    if end == -1:
        return {}, content
    fm = content[3:end]
    body = content[end + 4 :]
    meta = {}
    for line in fm.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, body


def extract_links(body: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", body)


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    rel = path.relative_to(REPO)
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as e:
        return [f"{rel}: read error {e}"]

    meta, body = parse_frontmatter(content)

    if path.name == "skill.md":
        for f in SKILL_REQUIRED:
            if f not in meta:
                errors.append(f"{rel}: missing skill field `{f}`")
    elif path.name not in SKIP_FULL:
        # title can be from name for skill only
        for f in REQUIRED_YAML:
            alt = f.replace("_", "-")
            if f not in meta and alt not in meta and f != "title":
                errors.append(f"{rel}: missing metadata `{f}`")
            elif f == "title" and "title" not in meta and "name" not in meta:
                errors.append(f"{rel}: missing title or name")

        for section in MANDATORY_SECTIONS:
            if not re.search(rf"^## {re.escape(section)}\s*$", body, re.MULTILINE):
                errors.append(f"{rel}: missing section `## {section}`")

    for link in extract_links(body):
        if link.startswith("http") or link.startswith("#"):
            continue
        link_path = link.split("#", 1)[0]
        if not link_path:
            continue
        target = (path.parent / link_path).resolve()
        if not target.exists():
            errors.append(f"{rel}: broken link `{link}`")

    return errors


def main() -> int:
    all_errors: list[str] = []
    total = 0
    for path in sorted(REPO.rglob("*.md")):
        if should_skip(path):
            continue
        total += 1
        all_errors.extend(validate_file(path))

    print(f"Validated {total} Markdown files.")
    if all_errors:
        print(f"FAILURES: {len(all_errors)}")
        for e in all_errors[:100]:
            print(f"  - {e}")
        if len(all_errors) > 100:
            print(f"  ... and {len(all_errors) - 100} more")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
