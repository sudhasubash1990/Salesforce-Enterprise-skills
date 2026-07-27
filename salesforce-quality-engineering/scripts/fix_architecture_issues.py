"""Fix post-migration architecture issues in QE skills (v0.24.0 follow-up)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
TEXT_EXTS = {".md", ".yaml", ".yml", ".py", ".mdc"}

SKILL_DIRS = [
    "metadata-impact-analyzer",
    "soql-validation-assistant",
    "permission-testing-agent",
    "agentforce-testing",
    "playwright-review",
    "omnistudio-qa",
    "data-migration-qa",
    "test-data-generator",
    "field-service-testing",
    "production-rca",
    "risk-based-regression",
]

SHORT_IDS = {
    "metadata-impact-analyzer": "MIA",
    "soql-validation-assistant": "SOVA",
    "permission-testing-agent": "PTA",
    "agentforce-testing": "AFT",
    "playwright-review": "PWR",
    "omnistudio-qa": "OSQA",
    "data-migration-qa": "DMQA",
    "test-data-generator": "TDG",
    "field-service-testing": "FSQA",
    "production-rca": "PRCA",
    "risk-based-regression": "RBRR",
}

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def rel_to(from_file: Path, to_file: Path) -> str:
    import os

    rel = os.path.relpath(str(Path(to_file).resolve()), str(from_file.parent.resolve()))
    return Path(rel).as_posix()


def repair_file_links(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    def repl(m: re.Match[str]) -> str:
        label, href_full = m.group(1), m.group(2)
        href, frag = (href_full.split("#", 1) + [""])[:2]
        frag = f"#{frag}" if frag else ""
        if not href or href.startswith(("http://", "https://", "mailto:")):
            return m.group(0)

        target = (path.parent / href).resolve()
        if target.exists():
            return m.group(0)

        # Try to map to a known skill entry or path inside skills/
        new_href = None

        # Pattern: .../skills/<skill>/...
        m_skills = re.search(r"(?:^|/)skills/([^/]+)(/.*)?$", href.replace("\\", "/"))
        if m_skills:
            skill, rest = m_skills.group(1), m_skills.group(2) or "/SKILL.md"
            if skill in SKILL_DIRS:
                dest = SKILLS / skill / rest.lstrip("/")
                if dest.exists() or (SKILLS / skill / "SKILL.md").exists():
                    if not dest.exists():
                        dest = SKILLS / skill / "SKILL.md"
                    new_href = rel_to(path, dest)

        # Pattern: ../<skill>/... or ../../<skill>/...
        if new_href is None:
            for skill in SKILL_DIRS:
                if f"/{skill}/" in f"/{href}" or href.startswith(f"{skill}/") or href.endswith(f"{skill}/SKILL.md"):
                    # extract rest after skill name
                    idx = href.replace("\\", "/").find(skill)
                    if idx >= 0:
                        rest = href.replace("\\", "/")[idx + len(skill) :]
                        rest = rest if rest else "/SKILL.md"
                        dest = SKILLS / skill / rest.lstrip("/")
                        if not dest.exists():
                            # try SKILL.md
                            dest = SKILLS / skill / "SKILL.md"
                        if dest.exists():
                            new_href = rel_to(path, dest)
                            break

        # Pattern: ../SKILL.md broken wrongly — leave alone if own skill
        if new_href is None and "SKILL.md" in href:
            # if any skill name substring
            for skill in SKILL_DIRS:
                if skill in href:
                    dest = SKILLS / skill / "SKILL.md"
                    if dest.exists():
                        new_href = rel_to(path, dest)
                        break

        if new_href:
            return f"[{label}]({new_href}{frag})"
        return m.group(0)

    updated = LINK_RE.sub(repl, text)

    # Also plain-path fixes for common wrong prefixes in non-markdown contexts
    # Fix ../../skills/<name> -> correct relative when appearing outside links too
    for skill in SKILL_DIRS:
        wrong = f"../../skills/{skill}/"
        if wrong in updated:
            dest_root = SKILLS / skill
            # approximate: from nested knowledge/playbooks (ups=2)
            if path.parent.name in {
                "knowledge",
                "playbooks",
                "templates",
                "prompts",
                "examples",
                "tests",
            }:
                updated = updated.replace(wrong, f"../../{skill}/")
            elif path.parent == SKILLS / path.relative_to(SKILLS).parts[0]:
                updated = updated.replace(wrong, f"../{skill}/")

    if updated != original:
        path.write_text(updated, encoding="utf-8", newline="\n")
        return True
    return False


def repair_all_links() -> tuple[int, list[str]]:
    changed = 0
    for path in SKILLS.rglob("*.md"):
        if repair_file_links(path):
            changed += 1

    broken: list[str] = []
    for path in SKILLS.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for m in LINK_RE.finditer(text):
            href = m.group(2).split("#")[0].strip()
            if not href or href.startswith(("http://", "https://", "mailto:")):
                continue
            if not any(s in href for s in SKILL_DIRS) and "SKILL.md" not in href:
                continue
            if not (path.parent / href).resolve().exists():
                broken.append(f"{path.relative_to(ROOT)} -> {href}")
    return changed, broken


def normalize_skill_config(path: Path, folder_name: str, short_id: str) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    # Flatten capability: root (2-space indent children)
    if re.match(r"^capability:\s*$", text, re.M) or text.lstrip().startswith("capability:"):
        lines = text.splitlines()
        out: list[str] = []
        under_cap = False
        for line in lines:
            if re.match(r"^capability:\s*$", line):
                under_cap = True
                continue
            if under_cap:
                if line.startswith("  ") and not line.startswith("    "):
                    out.append(line[2:])
                    continue
                if line.startswith("    "):
                    out.append(line[2:])
                    continue
                if line.strip() == "":
                    out.append(line)
                    continue
                # left capability block
                under_cap = False
            out.append(line)
        text = "\n".join(out)
        if original.endswith("\n"):
            text += "\n"

    # Map id: -> keep; ensure name
    if re.search(r"^id:\s*", text, re.M) and not re.search(r"^name:\s*", text, re.M):
        text = re.sub(r"^id:\s*(.*)$", rf"name: {folder_name}\nid: \1", text, count=1, flags=re.M)
    if not re.search(r"^name:\s*", text, re.M):
        text = f"name: {folder_name}\n{text}"
    else:
        text = re.sub(r"^name:\s*.*$", f"name: {folder_name}", text, count=1, flags=re.M)

    if not re.search(r"^short_id:\s*", text, re.M):
        if re.search(r"^short_name:\s*", text, re.M):
            text = re.sub(r"^short_name:\s*.*$", f"short_id: {short_id}", text, count=1, flags=re.M)
        else:
            text = re.sub(r"^(name:\s*.*)$", rf"\1\nshort_id: {short_id}", text, count=1, flags=re.M)

    # version without quotes preferred
    text = re.sub(r'^version:\s*"([^"]+)"\s*$', r"version: \1", text, flags=re.M)
    if not re.search(r"^version:\s*", text, re.M):
        text = re.sub(r"^(short_id:\s*.*)$", r"\1\nversion: 0.24.0", text, count=1, flags=re.M)

    if "entry: SKILL.md" not in text and not re.search(r"^entry:\s*", text, re.M):
        text = re.sub(r"^(version:\s*.*)$", r"\1\nentry: SKILL.md", text, count=1, flags=re.M)
    else:
        text = re.sub(r"^entry:\s*.*$", "entry: SKILL.md", text, count=1, flags=re.M)

    if not re.search(r"^parent_module:\s*", text, re.M):
        text = re.sub(
            r"^(entry:\s*.*)$",
            r"\1\nparent_module: salesforce-quality-engineering",
            text,
            count=1,
            flags=re.M,
        )

    text = re.sub(
        r"^# (.+) — capability configuration",
        r"# \1 — skill configuration",
        text,
        count=1,
        flags=re.M,
    )
    text = text.replace("upstream_capabilities:", "upstream_skills:")

    # Add architecture_release marker once
    if "architecture_release:" not in text:
        text = re.sub(
            r"^(version:\s*.*)$",
            r"\1\narchitecture_release: 0.24.0",
            text,
            count=1,
            flags=re.M,
        )

    if text != original:
        path.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


def normalize_all_configs() -> int:
    n = 0
    for folder, sid in SHORT_IDS.items():
        cfg = SKILLS / folder / "skill-config.yaml"
        if cfg.exists() and normalize_skill_config(cfg, folder, sid):
            n += 1
            print(f"  normalized {folder}/skill-config.yaml")
    return n


def replace_terminology() -> int:
    skip_names = {
        "CHANGELOG.md",
        "fix_architecture_issues.py",
    }
    count_files = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTS:
            continue
        if path.name in skip_names:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        original = text
        text = text.replace("QE Capability Knowledge", "QE Specialized Skill Knowledge")
        text = text.replace("QE Capability Playbook", "QE Specialized Skill Playbook")
        text = text.replace("QE Capability Template", "QE Specialized Skill Template")
        text = text.replace("QE Capability Prompt", "QE Specialized Skill Prompt")
        text = text.replace("QE Capability Example", "QE Specialized Skill Example")
        text = text.replace("QE Capability Test", "QE Specialized Skill Test")
        text = text.replace("QE Capability Guide", "QE Specialized Skill Guide")
        text = text.replace("category: QE Capability", "category: QE Specialized Skill")
        text = text.replace("QE Capabilities", "Specialized Skills")
        # after specific phrases, generic
        text = text.replace("QE Capability", "Specialized Skill")
        text = text.replace("upstream_capabilities:", "upstream_skills:")
        if text != original:
            path.write_text(text, encoding="utf-8", newline="\n")
            count_files += 1
    return count_files


def main() -> None:
    print("=== Repair cross-links ===")
    changed, broken = repair_all_links()
    print(f"Files updated: {changed}")
    print(f"Remaining broken skill-related links: {len(broken)}")
    for b in broken[:40]:
        print(" ", b)

    print("=== Normalize skill-configs ===")
    print(f"Configs updated: {normalize_all_configs()}")

    print("=== Terminology sweep ===")
    print(f"Files updated: {replace_terminology()}")
    print("=== DONE ===")


if __name__ == "__main__":
    main()
