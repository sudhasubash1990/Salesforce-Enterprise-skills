"""Bump and sync Salesforce BA skill version across README and changelog files.

Usage:
  python scripts/update_skill_version.py --message "feat(ba): ADO backlog integration"
  python scripts/update_skill_version.py --from-last-commit
  python scripts/update_skill_version.py --sync-only
  python scripts/update_skill_version.py --dry-run --message "fix(ba): AC formatting"
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL_MD = REPO / "salesforce-business-analyst" / "skill.md"
ROOT_README = REPO / "README.md"
SKILL_README = REPO / "salesforce-business-analyst" / "README.md"
SKILL_CHANGELOG = REPO / "salesforce-business-analyst" / "changelog.md"
ROOT_CHANGELOG = REPO / "CHANGELOG.md"

SKILL_PATH_PREFIXES = (
    "salesforce-business-analyst/",
    ".cursor/rules/userstory-generation.mdc",
)

CONVENTIONAL_RE = re.compile(
    r"^(?P<type>\w+)(?:\((?P<scope>[^)]+)\))?(?P<breaking>!)?:\s*(?P<summary>.+)$",
    re.IGNORECASE,
)
VERSION_RE = re.compile(r"^version:\s*(\d+\.\d+\.\d+)\s*$", re.MULTILINE)
VERSION_HISTORY_HEADER = "| Version | Date | Author | Summary |"


@dataclass
class VersionUpdate:
    old_version: str
    new_version: str
    summary: str
    bump: str
    author: str
    updated_date: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update skill version from commit message")
    parser.add_argument("--message", "-m", help="Commit message (conventional commit)")
    parser.add_argument(
        "--from-last-commit",
        action="store_true",
        help="Use subject line of HEAD commit",
    )
    parser.add_argument(
        "--sync-only",
        action="store_true",
        help="Sync README/changelog to version in skill.md without bumping",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print changes only")
    parser.add_argument("--author", default=None, help="Author for version history row")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Run even if no skill-path changes detected",
    )
    return parser.parse_args()


def run_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return ""
    return (result.stdout or "").strip()


def skill_paths_changed(staged: bool = True) -> bool:
    diff_cmd = ["diff", "--cached", "--name-only"] if staged else ["diff", "--name-only", "HEAD"]
    names = run_git(*diff_cmd).splitlines()
    if not names:
        names = run_git("status", "--porcelain").splitlines()
        names = [n[3:].strip() for n in names if n.strip()]
    for name in names:
        normalized = name.replace("\\", "/")
        for prefix in SKILL_PATH_PREFIXES:
            if normalized.startswith(prefix):
                return True
    return False


def read_version_from_skill() -> str:
    text = SKILL_MD.read_text(encoding="utf-8")
    match = VERSION_RE.search(text)
    if not match:
        raise ValueError(f"Could not find version in {SKILL_MD}")
    return match.group(1)


def parse_commit_message(message: str) -> tuple[str, str]:
    """Return (bump_kind, summary). bump_kind: major|minor|patch."""
    first_line = message.strip().splitlines()[0].strip()
    match = CONVENTIONAL_RE.match(first_line)
    if not match:
        return "patch", first_line

    commit_type = match.group("type").lower()
    summary = match.group("summary").strip()
    if match.group("breaking"):
        return "major", summary

    if commit_type in {"feat", "feature"}:
        return "minor", summary
    if commit_type in {"fix", "docs", "refactor", "chore", "style", "test", "skill"}:
        return "patch", summary
    return "patch", summary


def bump_semver(version: str, kind: str) -> str:
    major, minor, patch = (int(x) for x in version.split("."))
    if kind == "major":
        return f"{major + 1}.0.0"
    if kind == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def git_author() -> str:
    name = run_git("config", "user.name")
    return name or "Contributor"


def replace_frontmatter_version(text: str, new_version: str) -> str:
    if not VERSION_RE.search(text):
        return text
    text = VERSION_RE.sub(f"version: {new_version}", text, count=1)
    text = re.sub(
        r"^last_updated:\s*.+$",
        f"last_updated: {date.today().isoformat()}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    return text


def upsert_version_history(text: str, row: VersionUpdate) -> str:
    line = f"| {row.new_version} | {row.updated_date} | {row.author} | {row.summary} |"
    if VERSION_HISTORY_HEADER not in text:
        return text

    # Skip if exact version row already exists with same summary
    if f"| {row.new_version} |" in text and row.summary in text:
        return text

    pattern = re.compile(
        rf"({re.escape(VERSION_HISTORY_HEADER)}\n\|[-| ]+\|\n)",
        re.MULTILINE,
    )
    if not pattern.search(text):
        return text

    # Remove existing row for same version (replace summary)
    text = re.sub(
        rf"\| {re.escape(row.new_version)} \|[^\n]+\n",
        "",
        text,
    )

    return pattern.sub(rf"\1{line}\n", text, count=1)


def update_active_skill_line(text: str, version: str) -> str:
    return re.sub(
        r"(Salesforce Business Analyst \| Active \(v)\d+\.\d+\.\d+(\))",
        rf"\g<1>{version}\2",
        text,
    )


def update_skill_readme_version_line(text: str, version: str) -> str:
    return re.sub(
        r"Current skill version: \*\*\d+\.\d+\.\d+\*\*",
        f"Current skill version: **{version}**",
        text,
    )


def prepend_skill_changelog(text: str, row: VersionUpdate) -> str:
    marker = "## [Unreleased]"
    if marker not in text:
        return text
    entry = (
        f"\n## [{row.new_version}] - {row.updated_date}\n\n"
        f"### Changed\n\n"
        f"- {row.summary}\n"
    )
    if f"## [{row.new_version}]" in text:
        return text
    return text.replace(marker, marker + entry, 1)


def prepend_root_changelog(text: str, row: VersionUpdate) -> str:
    marker = "## [Unreleased]"
    if marker not in text:
        return text
    entry = (
        f"\n## [{row.new_version}] - {row.updated_date}\n\n"
        f"### Changed\n\n"
        f"- Salesforce Business Analyst skill {row.new_version}: {row.summary}\n"
    )
    if f"## [{row.new_version}]" in text:
        return text
    return text.replace(marker, marker + entry, 1)


def apply_update(path: Path, transform, dry_run: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = transform(original)
    if updated == original:
        return False
    if dry_run:
        print(f"[dry-run] would update {path.relative_to(REPO)}")
    else:
        path.write_text(updated, encoding="utf-8", newline="\n")
        print(f"updated {path.relative_to(REPO)}")
    return True


def main() -> int:
    args = parse_args()

    if args.from_last_commit:
        message = run_git("log", "-1", "--pretty=%s")
        if not message:
            print("ERROR: could not read last commit message", file=sys.stderr)
            return 1
    elif args.message:
        message = args.message
    elif args.sync_only:
        message = "chore: sync skill version metadata"
    else:
        print("ERROR: provide --message, --from-last-commit, or --sync-only", file=sys.stderr)
        return 1

    if not args.force and not args.sync_only and not skill_paths_changed(staged=True):
        if not skill_paths_changed(staged=False):
            print("No skill-path changes detected. Use --force to run anyway.")
            return 0

    current = read_version_from_skill()
    bump_kind, summary = parse_commit_message(message)
    new_version = current if args.sync_only else bump_semver(current, bump_kind)
    author = args.author or git_author()
    today = date.today().isoformat()

    row = VersionUpdate(
        old_version=current,
        new_version=new_version,
        summary=summary,
        bump="sync" if args.sync_only else bump_kind,
        author=author,
        updated_date=today,
    )

    print(f"Skill version: {current} -> {new_version} ({row.bump})")
    print(f"Summary: {summary}")

    transforms: list[tuple[Path, object]] = [
        (
            SKILL_MD,
            lambda t: upsert_version_history(
                replace_frontmatter_version(t, new_version), row
            )
            if not args.sync_only
            else replace_frontmatter_version(t, new_version),
        ),
        (
            ROOT_README,
            lambda t: upsert_version_history(
                update_active_skill_line(replace_frontmatter_version(t, new_version), new_version),
                row,
            ),
        ),
        (
            SKILL_README,
            lambda t: upsert_version_history(
                update_skill_readme_version_line(replace_frontmatter_version(t, new_version), new_version),
                row,
            ),
        ),
        (
            SKILL_CHANGELOG,
            lambda t: prepend_skill_changelog(t, row) if not args.sync_only else t,
        ),
        (
            ROOT_CHANGELOG,
            lambda t: prepend_root_changelog(t, row) if not args.sync_only else t,
        ),
    ]

    changed = False
    for path, transform in transforms:
        if path.is_file():
            changed = apply_update(path, transform, args.dry_run) or changed

    if args.dry_run:
        print("Dry run complete.")
        return 0

    if not changed and args.sync_only:
        print("All version metadata already in sync.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
