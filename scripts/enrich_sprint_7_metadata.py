"""Sprint 7 — enrich all Markdown files with metadata, related sections, navigation, version history."""
from __future__ import annotations

import os
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BA = REPO / "salesforce-business-analyst"
TODAY = "2026-07-02"
SPRINT_VERSION = "1.3.0"

SKIP_PATH_PARTS = {".cursor/plans", ".git"}
SKIP_FULL_SECTIONS = {"CHANGELOG.md", "changelog.md"}

MANDATORY_SECTIONS = [
    "Related Brain Modules",
    "Related Knowledge",
    "Related Templates",
    "Related Playbooks",
    "Related Industry Scenarios",
    "Related Interview Topics",
    "Related Examples",
    "Related Documents",
]

KNOWLEDGE_INTERVIEW_MAP: dict[str, list[str]] = {
    "business-analysis-fundamentals.md": ["business-analysis.md"],
    "babok-guide.md": ["business-analysis.md"],
    "requirement-types.md": ["requirement-gathering.md"],
    "requirement-elicitation.md": ["requirement-gathering.md"],
    "workshop-facilitation.md": ["requirement-gathering.md"],
    "moscow-prioritization.md": ["requirement-gathering.md"],
    "current-state-analysis.md": ["current-state.md"],
    "process-mapping.md": ["current-state.md", "advanced/whiteboard-exercises.md"],
    "as-is-to-be.md": ["current-state.md", "future-state.md"],
    "future-state-design.md": ["future-state.md"],
    "user-stories.md": ["user-stories.md"],
    "backlog-management.md": ["user-stories.md"],
    "acceptance-criteria.md": ["acceptance-criteria.md"],
    "uat-fundamentals.md": ["acceptance-criteria.md"],
    "stakeholder-analysis.md": ["stakeholders.md"],
    "salesforce-clouds-overview.md": ["salesforce/crm.md"],
    "salesforce-platform.md": ["salesforce/crm.md"],
    "sales-cloud.md": ["salesforce/sales-cloud.md"],
    "service-cloud.md": ["salesforce/service-cloud.md"],
    "experience-cloud.md": ["salesforce/experience-cloud.md"],
    "cpq-fundamentals.md": ["salesforce/cpq.md"],
    "industry-patterns.md": ["salesforce/industries.md"],
    "integration-patterns.md": ["delivery/architecture.md"],
    "security-model.md": ["delivery/architecture.md"],
    "data-migration.md": ["delivery/architecture.md"],
    "agile-fundamentals.md": ["delivery/agile.md"],
    "safe-awareness.md": ["delivery/agile.md"],
    "scrum-fundamentals.md": ["delivery/scrum.md"],
    "risk-management.md": ["delivery/risk-management.md"],
    "raid-management.md": ["delivery/risk-management.md"],
    "executive-communication.md": ["delivery/communication.md", "advanced/executive-communication.md"],
    "change-management.md": ["delivery/leadership.md"],
    "governance-framework.md": ["delivery/leadership.md", "delivery/risk-management.md"],
}

CATEGORY_DEFAULTS: dict[str, dict] = {
    "Brain": {
        "document_type": "Framework",
        "related_brain_modules": [
            "salesforce-business-analyst/brain/reasoning-framework.md",
            "salesforce-business-analyst/brain/validation-framework.md",
        ],
        "related_knowledge": ["salesforce-business-analyst/knowledge/README.md"],
        "related_templates": ["salesforce-business-analyst/templates/README.md"],
        "related_playbooks": ["salesforce-business-analyst/playbooks/README.md"],
        "related_scenarios": ["salesforce-business-analyst/scenarios/README.md"],
        "related_interview_topics": ["salesforce-business-analyst/interview-guide/business-analysis.md"],
        "related_examples": ["examples/sample-project/README.md"],
        "related_documents": ["salesforce-business-analyst/skill.md", "salesforce-business-analyst/brain/README.md"],
    },
    "Knowledge": {
        "document_type": "Knowledge Article",
        "related_brain_modules": [
            "salesforce-business-analyst/brain/reasoning-framework.md",
            "salesforce-business-analyst/brain/output-framework.md",
        ],
        "related_knowledge": ["salesforce-business-analyst/knowledge/README.md"],
        "related_templates": ["salesforce-business-analyst/templates/README.md"],
        "related_playbooks": ["salesforce-business-analyst/playbooks/README.md"],
        "related_scenarios": ["salesforce-business-analyst/scenarios/README.md"],
        "related_interview_topics": ["salesforce-business-analyst/interview-guide/interview-index.md"],
        "related_examples": ["examples/sample-project/README.md"],
        "related_documents": ["salesforce-business-analyst/skill.md", "salesforce-business-analyst/knowledge/README.md"],
    },
    "Template": {
        "document_type": "Template",
        "related_brain_modules": [
            "salesforce-business-analyst/brain/output-framework.md",
            "salesforce-business-analyst/brain/validation-framework.md",
        ],
        "related_knowledge": ["salesforce-business-analyst/knowledge/README.md"],
        "related_templates": ["salesforce-business-analyst/templates/README.md"],
        "related_playbooks": ["salesforce-business-analyst/playbooks/README.md"],
        "related_scenarios": ["salesforce-business-analyst/scenarios/README.md"],
        "related_interview_topics": ["salesforce-business-analyst/interview-guide/user-stories.md"],
        "related_examples": ["examples/sample-brd/brd-excerpt.md"],
        "related_documents": ["salesforce-business-analyst/skill.md", "salesforce-business-analyst/templates/README.md"],
    },
    "Playbook": {
        "document_type": "Consulting Methodology",
        "related_brain_modules": [
            "salesforce-business-analyst/brain/reasoning-framework.md",
            "salesforce-business-analyst/brain/enterprise-behaviors.md",
        ],
        "related_knowledge": ["salesforce-business-analyst/knowledge/README.md"],
        "related_templates": ["salesforce-business-analyst/templates/README.md"],
        "related_playbooks": ["salesforce-business-analyst/playbooks/README.md"],
        "related_scenarios": ["salesforce-business-analyst/scenarios/README.md"],
        "related_interview_topics": ["salesforce-business-analyst/interview-guide/advanced/scenario-questions.md"],
        "related_examples": ["examples/sample-project/README.md"],
        "related_documents": ["salesforce-business-analyst/skill.md", "salesforce-business-analyst/playbooks/README.md"],
    },
    "Scenario": {
        "document_type": "Enterprise Scenario",
        "related_brain_modules": [
            "salesforce-business-analyst/brain/reasoning-framework.md",
            "salesforce-business-analyst/brain/decision-framework.md",
        ],
        "related_knowledge": ["salesforce-business-analyst/knowledge/industry-patterns.md"],
        "related_templates": ["salesforce-business-analyst/templates/brd-template.md"],
        "related_playbooks": ["salesforce-business-analyst/playbooks/discovery-workshop-playbook.md"],
        "related_scenarios": ["salesforce-business-analyst/scenarios/README.md"],
        "related_interview_topics": ["salesforce-business-analyst/interview-guide/advanced/scenario-questions.md"],
        "related_examples": ["examples/sample-project/README.md"],
        "related_documents": ["salesforce-business-analyst/skill.md", "salesforce-business-analyst/scenarios/README.md"],
    },
    "Interview": {
        "document_type": "Interview Framework",
        "related_brain_modules": [
            "salesforce-business-analyst/brain/communication-framework.md",
            "salesforce-business-analyst/brain/reasoning-framework.md",
        ],
        "related_knowledge": ["salesforce-business-analyst/knowledge/README.md"],
        "related_templates": ["salesforce-business-analyst/templates/README.md"],
        "related_playbooks": ["salesforce-business-analyst/playbooks/README.md"],
        "related_scenarios": ["salesforce-business-analyst/scenarios/README.md"],
        "related_interview_topics": ["salesforce-business-analyst/interview-guide/interview-index.md"],
        "related_examples": ["examples/sample-project/README.md"],
        "related_documents": ["salesforce-business-analyst/skill.md", "salesforce-business-analyst/interview-guide/README.md"],
    },
    "Validation": {
        "document_type": "Framework",
        "related_brain_modules": [
            "salesforce-business-analyst/brain/validation-framework.md",
            "salesforce-business-analyst/brain/anti-hallucination.md",
        ],
        "related_knowledge": ["salesforce-business-analyst/knowledge/governance-framework.md"],
        "related_templates": ["salesforce-business-analyst/templates/README.md"],
        "related_playbooks": ["salesforce-business-analyst/playbooks/production-readiness-playbook.md"],
        "related_scenarios": ["salesforce-business-analyst/scenarios/README.md"],
        "related_interview_topics": ["salesforce-business-analyst/interview-guide/interview-index.md"],
        "related_examples": ["examples/sample-project/README.md"],
        "related_documents": [
            "salesforce-business-analyst/validation/README.md",
            "docs/quality-framework.md",
            "scripts/validate_repository.py",
        ],
    },
    "Governance": {
        "document_type": "Framework",
        "related_brain_modules": [],
        "related_knowledge": ["salesforce-business-analyst/knowledge/README.md"],
        "related_templates": ["salesforce-business-analyst/templates/README.md"],
        "related_playbooks": ["salesforce-business-analyst/playbooks/README.md"],
        "related_scenarios": ["salesforce-business-analyst/scenarios/README.md"],
        "related_interview_topics": ["salesforce-business-analyst/interview-guide/interview-index.md"],
        "related_examples": ["examples/sample-project/README.md"],
        "related_documents": ["docs/metadata-schema.md", "docs/cross-linking-framework.md"],
    },
    "Shared": {
        "document_type": "Reference",
        "related_brain_modules": ["salesforce-business-analyst/brain/consulting-principles.md"],
        "related_knowledge": ["salesforce-business-analyst/knowledge/README.md"],
        "related_templates": ["salesforce-business-analyst/templates/README.md"],
        "related_playbooks": ["salesforce-business-analyst/playbooks/README.md"],
        "related_scenarios": ["salesforce-business-analyst/scenarios/README.md"],
        "related_interview_topics": ["salesforce-business-analyst/interview-guide/interview-index.md"],
        "related_examples": ["examples/sample-project/README.md"],
        "related_documents": ["docs/metadata-schema.md", "shared/traceability-model.md"],
    },
    "Root": {
        "document_type": "Guide",
        "related_brain_modules": ["salesforce-business-analyst/brain/README.md"],
        "related_knowledge": ["salesforce-business-analyst/knowledge/README.md"],
        "related_templates": ["salesforce-business-analyst/templates/README.md"],
        "related_playbooks": ["salesforce-business-analyst/playbooks/README.md"],
        "related_scenarios": ["salesforce-business-analyst/scenarios/README.md"],
        "related_interview_topics": ["salesforce-business-analyst/interview-guide/interview-index.md"],
        "related_examples": ["examples/sample-project/README.md"],
        "related_documents": ["docs/cross-linking-framework.md", "ROADMAP.md"],
    },
}

TRACEABILITY: dict[str, str] = {
    "Brain": "**Upstream:** Governance standards | **Downstream:** Knowledge, playbooks, templates | **Validation:** validation-framework.md",
    "Knowledge": "**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md",
    "Template": "**Upstream:** Knowledge, BRD/FRD | **Downstream:** Playbooks, user stories, RTM | **Validation:** validation-framework.md",
    "Playbook": "**Upstream:** Knowledge, templates | **Downstream:** Scenarios, workshop outputs | **Validation:** checklists.md",
    "Scenario": "**Upstream:** Knowledge, playbooks | **Downstream:** BRD examples, interview scenarios | **Validation:** fit-gap analysis",
    "Interview": "**Upstream:** Brain, knowledge, scenarios | **Downstream:** Assessment scorecards | **Validation:** interview rubric",
    "Validation": "**Upstream:** Brain validation, governance | **Downstream:** Certification, maturity assessments | **Validation:** validate_repository.py",
    "Governance": "**Upstream:** — | **Downstream:** All repository documents | **Validation:** validate_metadata.py",
    "Shared": "**Upstream:** Governance | **Downstream:** All modules | **Validation:** glossary consistency",
    "Root": "**Upstream:** — | **Downstream:** All skills | **Validation:** ROADMAP alignment",
}


def should_skip(path: Path) -> bool:
    s = path.as_posix()
    return any(part in s for part in SKIP_PATH_PARTS)


def split_frontmatter(content: str) -> tuple[dict[str, str], str, bool]:
    if not content.startswith("---"):
        return {}, content, False
    end = content.find("\n---", 3)
    if end == -1:
        return {}, content, False
    fm_text = content[3:end].strip()
    body = content[end + 4 :].lstrip("\n")
    meta: dict[str, str] = {}
    for line in fm_text.splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        meta[key.strip()] = val.strip()
    return meta, body, True


def infer_category(path: Path) -> str:
    rel = path.relative_to(REPO).as_posix()
    if rel.startswith("salesforce-business-analyst/brain/"):
        return "Brain"
    if rel.startswith("salesforce-business-analyst/knowledge/"):
        return "Knowledge"
    if rel.startswith("salesforce-business-analyst/templates/"):
        return "Template"
    if rel.startswith("salesforce-business-analyst/playbooks/"):
        return "Playbook"
    if rel.startswith("salesforce-business-analyst/scenarios/"):
        return "Scenario"
    if rel.startswith("salesforce-business-analyst/interview-guide/"):
        return "Interview"
    if rel.startswith("salesforce-business-analyst/validation/"):
        return "Validation"
    if rel.startswith("salesforce-business-analyst/learning-paths/"):
        return "Root"
    if rel.startswith("salesforce-business-analyst/implementation/"):
        return "Root"
    if rel.startswith("docs/"):
        return "Governance"
    if rel.startswith("shared/"):
        return "Shared"
    if rel.startswith(".cursor/"):
        return "Governance"
    if path.parent == REPO:
        return "Root"
    if rel.startswith("salesforce-business-analyst/"):
        return "Root"
    if rel.startswith("examples/"):
        return "Shared"
    return "Root"


def normalize_meta(meta: dict[str, str], path: Path, category: str) -> dict[str, str]:
    defaults = CATEGORY_DEFAULTS.get(category, CATEGORY_DEFAULTS["Root"])
    out: dict[str, str] = dict(meta)

    # Legacy migration
    if "document-type" in out and "document_type" not in out:
        out["document_type"] = out.pop("document-type")
    if "status" in out and "review_status" not in out:
        status_map = {"approved": "Approved", "draft": "Draft", "review": "Review", "deprecated": "Deprecated"}
        out["review_status"] = status_map.get(out.pop("status").lower(), "Approved")
    if "last-reviewed" in out and "last_updated" not in out:
        out["last_updated"] = out.pop("last-reviewed")

    title = out.get("title") or out.get("name") or path.stem.replace("-", " ").title()
    out["title"] = title.strip('"')

    if path.name == "skill.md":
        out.setdefault("module", "Salesforce Business Analyst")
        out.setdefault("category", "Root")
        out.setdefault("document_type", "Skill")
    else:
        out.setdefault("module", "Salesforce Business Analyst")
        out.setdefault("category", category)
        out.setdefault("document_type", defaults.get("document_type", "Guide"))

    out.setdefault("version", SPRINT_VERSION)
    out.setdefault("review_status", "Approved")
    out.setdefault("owner", "BA Practice Lead")
    out.setdefault("created_date", TODAY)
    out.setdefault("last_updated", TODAY)
    out.setdefault("review_cycle", "quarterly")

    for key in [
        "related_brain_modules",
        "related_knowledge",
        "related_templates",
        "related_playbooks",
        "related_scenarios",
        "related_interview_topics",
        "related_examples",
        "related_documents",
    ]:
        legacy = key.replace("_", "-")
        if legacy in out:
            out.pop(legacy, None)
        val = defaults.get(key, [])
        if val:
            out[key] = list(val)

    # Knowledge-specific interview topic override
    if category == "Knowledge" and path.name in KNOWLEDGE_INTERVIEW_MAP:
        topics = KNOWLEDGE_INTERVIEW_MAP[path.name]
        out["related_interview_topics"] = [
            f"salesforce-business-analyst/interview-guide/{t}" for t in topics
        ]

    # Brain module self-reference: include current file for peers
    if category == "Brain" and path.name != "README.md":
        peers = [
            "salesforce-business-analyst/brain/reasoning-framework.md",
            "salesforce-business-analyst/brain/validation-framework.md",
        ]
        if f"salesforce-business-analyst/brain/{path.name}" not in peers:
            peers.insert(0, f"salesforce-business-analyst/brain/{path.name}")
        out["related_brain_modules"] = peers[:3]

    if "tags" not in out:
        out["tags"] = f"[{path.stem}]"
    if "keywords" not in out:
        out["keywords"] = f"[{path.stem.replace('-', ' ')}]"

    return out


def format_frontmatter(meta: dict[str, str], path: Path) -> str:
    if path.name == "skill.md" and "name" in meta:
        lines = ["---"]
        for key in ("name", "description", "version"):
            if key in meta:
                val = meta[key]
                if key == "description" and "\n" not in val and len(val) > 80:
                    lines.append(f"description: >-")
                    lines.append(f"  {val}")
                else:
                    lines.append(f"{key}: {val}")
        lines.append("---")
        return "\n".join(lines) + "\n\n"

    order = [
        "title", "name", "description", "module", "category", "document_type",
        "version", "review_status", "owner", "created_date", "last_updated", "review_cycle",
        "difficulty", "industry", "business_domain", "salesforce_cloud", "implementation_phase",
        "related_brain_modules", "related_knowledge", "related_templates", "related_playbooks",
        "related_scenarios", "related_interview_topics", "related_examples", "related_documents",
        "keywords", "tags",
    ]
    lines = ["---"]
    used = set()
    for key in order:
        if key in meta:
            val = meta[key]
            if key.startswith("related_") and isinstance(val, list):
                lines.append(f"{key}: [{', '.join(val)}]")
            else:
                lines.append(f"{key}: {val}")
            used.add(key)
    for key, val in meta.items():
        if key not in used:
            lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def has_section(body: str, section: str) -> bool:
    return re.search(rf"^## {re.escape(section)}\s*$", body, re.MULTILINE) is not None


def strip_existing_sprint7_sections(body: str) -> str:
    """Remove auto-generated sections to allow idempotent re-run."""
    patterns = MANDATORY_SECTIONS + ["Traceability", "Navigation", "Version History"]
    for section in patterns:
        body = re.sub(
            rf"\n## {re.escape(section)}\n.*?(?=\n## |\Z)",
            "\n",
            body,
            flags=re.DOTALL,
        )
    return body.rstrip() + "\n"


def clean_path_item(s: str) -> str:
    return s.strip().strip("'\"").strip()


def to_repo_target(from_path: Path, target: str) -> str:
    target = clean_path_item(target)
    if target.startswith("http"):
        return target
    if target in {"ROADMAP.md", "README.md", "CHANGELOG.md"}:
        return target
    if "/" in target and not target.startswith(".."):
        return target.lstrip("./")
    resolved = (from_path.parent / target).resolve()
    try:
        return resolved.relative_to(REPO).as_posix()
    except ValueError:
        return target


def to_rel_href(from_path: Path, repo_target: str) -> str:
    if repo_target.startswith("http"):
        return repo_target
    dest = REPO / repo_target
    return os.path.relpath(dest, from_path.parent).replace("\\", "/")


def link_line(from_path: Path, target: str, label: str | None = None) -> str:
    if target.startswith("http"):
        return f"- {target}"
    repo_target = to_repo_target(from_path, target)
    label = label or Path(repo_target).stem.replace("-", " ").title()
    href = to_rel_href(from_path, repo_target)
    return f"- [{label}]({href})"


def nav_link(from_path: Path, to_path: Path, label: str | None = None) -> str:
    label = label or to_path.stem.replace("-", " ").title()
    href = os.path.relpath(to_path, from_path.parent).replace("\\", "/")
    return f"[{label}]({href})"


def build_section(title: str, links: list[str]) -> str:
    if not links:
        return f"## {title}\n\nN/A — no direct relationships for this document type.\n"
    return f"## {title}\n\n" + "\n".join(links) + "\n"


def get_siblings(path: Path) -> list[Path]:
    if not path.parent.exists():
        return []
    files = sorted(
        p for p in path.parent.glob("*.md") if p.name != "README.md" and p.is_file()
    )
    return files


def navigation_block(path: Path) -> str:
    siblings = get_siblings(path)
    if "salesforce-business-analyst" in path.as_posix():
        see_also = nav_link(path, BA / "skill.md", "skill.md")
    else:
        see_also = nav_link(path, REPO / "docs" / "cross-linking-framework.md", "cross-linking-framework")

    readme = path.parent / "README.md"
    if len(siblings) >= 2 and path in siblings:
        idx = siblings.index(path)
        prev_p = siblings[idx - 1] if idx > 0 else (readme if readme.exists() else None)
        next_p = siblings[idx + 1] if idx < len(siblings) - 1 else (readme if readme.exists() else None)
        prev_l = nav_link(path, prev_p) if isinstance(prev_p, Path) else "—"
        next_l = nav_link(path, next_p) if isinstance(next_p, Path) else "—"
    elif path.parent.name == "docs":
        prev_l = nav_link(path, REPO / "README.md", "Repository README")
        next_l = nav_link(path, REPO / "docs" / "architecture.md", "architecture")
    elif path.parent.name == ".cursor":
        prev_l = nav_link(path, REPO / "README.md", "Repository README")
        next_l = nav_link(path, REPO / ".cursor" / "instructions.md", "instructions")
    else:
        prev_l = nav_link(path, readme) if readme.exists() else "—"
        next_l = prev_l

    return f"""## Navigation

- **Previous:** {prev_l}
- **Next:** {next_l}
- **See Also:** {see_also}
"""


def enrich_body(path: Path, body: str, category: str, meta: dict[str, str]) -> str:
    if path.name in SKIP_FULL_SECTIONS:
        return body

    body = strip_existing_sprint7_sections(body)
    defaults = CATEGORY_DEFAULTS.get(category, CATEGORY_DEFAULTS["Root"])

    def links_for(key: str) -> list[str]:
        raw = meta.get(key) or defaults.get(key, [])
        if isinstance(raw, str):
            raw = re.findall(r"[^\[\],]+", raw)
        raw = [clean_path_item(x) for x in raw if clean_path_item(x)]
        return [link_line(path, p) for p in raw]

    sections = []
    for title, key in zip(
        MANDATORY_SECTIONS,
        [
            "related_brain_modules",
            "related_knowledge",
            "related_templates",
            "related_playbooks",
            "related_scenarios",
            "related_interview_topics",
            "related_examples",
            "related_documents",
        ],
    ):
        if not has_section(body, title):
            sections.append(build_section(title, links_for(key)))

    trace = TRACEABILITY.get(category, TRACEABILITY["Root"])
    sections.append(f"## Traceability\n\n{trace}\n")
    sections.append(navigation_block(path))
    sections.append(
        f"""## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {SPRINT_VERSION} | {TODAY} | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
"""
    )
    return body.rstrip() + "\n\n" + "\n".join(sections)


def enrich_file(path: Path) -> bool:
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return False
    category = infer_category(path)
    meta, body, had_fm = split_frontmatter(content)
    if path.name == "skill.md":
        meta.setdefault("name", "salesforce-business-analyst")
        meta.setdefault("version", SPRINT_VERSION)
        if "description" not in meta or len(meta.get("description", "")) < 20:
            meta["description"] = (
                "Produces enterprise Salesforce business analysis deliverables including BRDs, "
                "FRDs, user stories, fit-gap analysis, workshop outputs, process maps, RAID logs, "
                "traceability matrices, and UAT scenarios. Orchestrates the BA Brain reasoning engine "
                "for discovery, requirements engineering, MoSCoW prioritization, INVEST stories, "
                "platform-aware fit-gap classification, and self-validation. Use when the user asks "
                "for Salesforce BA work, requirements, business requirements document, functional "
                "requirements, user stories, acceptance criteria, discovery, stakeholder workshops, "
                "AS-IS TO-BE process, fit-gap, gap analysis, scope definition, backlog grooming, "
                "RAID, traceability matrix, UAT test scenarios, interview prep, or mock interviews."
            )
    meta = normalize_meta(meta, path, category)
    if path.name == "skill.md":
        meta["version"] = SPRINT_VERSION
    new_body = enrich_body(path, body, category, meta)
    new_content = format_frontmatter(meta, path) + new_body
    if new_content != content:
        path.write_text(new_content, encoding="utf-8")
        return True
    return False


def main() -> None:
    updated = 0
    total = 0
    for path in sorted(REPO.rglob("*.md")):
        if should_skip(path):
            continue
        total += 1
        if enrich_file(path):
            updated += 1
            print(f"  enriched {path.relative_to(REPO)}")
    print(f"Done. {updated}/{total} files updated.")


if __name__ == "__main__":
    main()
