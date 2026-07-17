#!/usr/bin/env python3
"""Apply repository quality-audit fixes (links, merges, READMEs, stubs, archive)."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QE = ROOT / "salesforce-quality-engineering"
BA = ROOT / "salesforce-business-analyst"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    print(f"WRITE {path.relative_to(ROOT)}")


def pointer(
    title: str,
    canonical_rel: str,
    lens: str,
    extra: str = "",
) -> str:
    return f"""---
title: {title}
type: pointer
status: redirect
last_updated: 2026-07-18
---

# {title}

**Canonical:** [{canonical_rel}]({canonical_rel})

**Lens:** {lens}

This file is a **thin pointer** under the multi-lens policy. Do not duplicate full content here.
Load the canonical article; add only lens-specific deltas in your response when needed.
{extra}
"""


def fix_output_generation_rule() -> None:
    p = ROOT / ".cursor" / "rules" / "output-generation.mdc"
    text = p.read_text(encoding="utf-8")
    text2 = text.replace("](../output-engine/", "](../../output-engine/")
    if text2 != text:
        p.write_text(text2, encoding="utf-8")
        print(f"FIXED {p.relative_to(ROOT)}")


def fix_qe_links() -> None:
    # ado/README Related block
    ado = QE / "ado" / "README.md"
    text = ado.read_text(encoding="utf-8")
    text = text.replace("](../../brain/", "](../brain/")
    text = text.replace("](../../knowledge/", "](../knowledge/")
    text = text.replace("](../../templates/", "](../templates/")
    text = text.replace(
        "](../../../salesforce-business-analyst/",
        "](../../salesforce-business-analyst/",
    )
    ado.write_text(text, encoding="utf-8")
    print("FIXED ado/README.md Related depths")

    # skill.md cross-module-map
    skill = QE / "skill.md"
    st = skill.read_text(encoding="utf-8")
    st2 = st.replace(
        "](cross-module-map.md)",
        "](brain/cross-module-map.md)",
    )
    if st2 != st:
        skill.write_text(st2, encoding="utf-8")
        print("FIXED skill.md -> brain/cross-module-map.md")

    # knowledge files
    refs = QE / "knowledge" / "references.md"
    t = refs.read_text(encoding="utf-8")
    reps = {
        "](README.md)": "](../README.md)",
        "](skill.md)": "](../skill.md)",
        "](ROADMAP.md)": "](../ROADMAP.md)",
        "](prompts.md)": "](../prompts.md)",
        "](../salesforce-business-analyst/": "](../../salesforce-business-analyst/",
        "](../shared/": "](../../shared/",
        "](../docs/": "](../../docs/",
    }
    # careful: knowledge/README.md should stay as README.md for knowledge index
    # Only fix Related/Navigation that meant module root
    t = t.replace("| QE module landing | [README.md](README.md) |", "| QE module landing | [README.md](../README.md) |")
    t = t.replace("| QE skill skeleton | [skill.md](skill.md) |", "| QE skill skeleton | [skill.md](../skill.md) |")
    t = t.replace(
        "[../salesforce-business-analyst/skill.md](../salesforce-business-analyst/skill.md)",
        "[../../salesforce-business-analyst/skill.md](../../salesforce-business-analyst/skill.md)",
    )
    t = t.replace("[../shared/glossary.md](../shared/glossary.md)", "[../../shared/glossary.md](../../shared/glossary.md)")
    t = t.replace(
        "[../shared/output-standards.md](../shared/output-standards.md)",
        "[../../shared/output-standards.md](../../shared/output-standards.md)",
    )
    t = t.replace(
        "[../shared/salesforce-capability-map.md](../shared/salesforce-capability-map.md)",
        "[../../shared/salesforce-capability-map.md](../../shared/salesforce-capability-map.md)",
    )
    t = t.replace(
        "[../docs/metadata-schema.md](../docs/metadata-schema.md)",
        "[../../docs/metadata-schema.md](../../docs/metadata-schema.md)",
    )
    t = t.replace(
        "[../docs/cross-linking-framework.md](../docs/cross-linking-framework.md)",
        "[../../docs/cross-linking-framework.md](../../docs/cross-linking-framework.md)",
    )
    t = t.replace("- [README.md](README.md)\n- [skill.md](skill.md)\n- [ROADMAP.md](ROADMAP.md)",
                  "- [README.md](../README.md)\n- [skill.md](../skill.md)\n- [ROADMAP.md](../ROADMAP.md)")
    t = t.replace("**Previous:** [skill.md](skill.md)", "**Previous:** [skill.md](../skill.md)")
    t = t.replace("**Next:** [prompts.md](prompts.md)", "**Next:** [prompts.md](../prompts.md)")
    t = t.replace("**See Also:** [README.md](README.md)", "**See Also:** [README.md](../README.md)")
    refs.write_text(t, encoding="utf-8")
    print("FIXED knowledge/references.md")

    ex = QE / "knowledge" / "examples.md"
    t = ex.read_text(encoding="utf-8")
    t = t.replace("[examples/README.md](examples/README.md)", "[../scenarios/README.md](../scenarios/README.md) (QE scenarios hub)")
    t = t.replace("[scenarios/README.md](scenarios/README.md)", "[../scenarios/README.md](../scenarios/README.md)")
    t = t.replace(
        "[../salesforce-business-analyst/scenarios/README.md](../salesforce-business-analyst/scenarios/README.md)",
        "[../../salesforce-business-analyst/scenarios/README.md](../../salesforce-business-analyst/scenarios/README.md)",
    )
    t = t.replace("**Next:** [ROADMAP.md](ROADMAP.md)", "**Next:** [ROADMAP.md](../ROADMAP.md)")
    t = t.replace("**See Also:** [scenarios/README.md](scenarios/README.md)", "**See Also:** [../scenarios/README.md](../scenarios/README.md)")
    ex.write_text(t, encoding="utf-8")
    print("FIXED knowledge/examples.md")

    met = QE / "knowledge" / "metrics.md"
    t = met.read_text(encoding="utf-8")
    t = t.replace("[reports/README.md](reports/README.md)", "[reports/README.md](reports/README.md)")
    t = t.replace("**Previous:** [ROADMAP.md](ROADMAP.md)", "**Previous:** [ROADMAP.md](../ROADMAP.md)")
    t = t.replace("**Next:** [CHANGELOG.md](CHANGELOG.md)", "**Next:** [CHANGELOG.md](../CHANGELOG.md)")
    met.write_text(t, encoding="utf-8")
    print("FIXED knowledge/metrics.md")

    ig = QE / "knowledge" / "interview-guide.md"
    t = ig.read_text(encoding="utf-8")
    t = t.replace("**See Also:** [skill.md](skill.md)", "**See Also:** [skill.md](../skill.md)")
    ig.write_text(t, encoding="utf-8")
    print("FIXED knowledge/interview-guide.md")

    # Root ROADMAP
    rm = ROOT / "ROADMAP.md"
    t = rm.read_text(encoding="utf-8")
    t = t.replace(
        "](salesforce-quality-engineering/interview-guide.md)",
        "](salesforce-quality-engineering/interview-guide.md)",
    )
    # Will create stub at module root; also add knowledge path note in stub
    rm.write_text(t, encoding="utf-8")


def merge_knowledge_overlaps() -> None:
    # Root stubs → pointers to release/
    for name in ("smoke-testing", "sanity-testing", "regression-planning"):
        write(
            QE / "knowledge" / f"{name}.md",
            pointer(
                title=name.replace("-", " ").title(),
                canonical_rel=f"release/{name}.md",
                lens="Sprint 3 technique entry → Sprint 4B release knowledge (canonical)",
            ),
        )

    # automation platform-events → integration (canonical enterprise PE article)
    write(
        QE / "knowledge" / "automation" / "platform-events.md",
        pointer(
            title="Platform Events",
            canonical_rel="../integration/platform-events.md",
            lens="Sprint 4A automation folder → Sprint 4B integration (canonical). Automation readiness deltas belong in response, not a second full article.",
            extra="\nAlso see: [../automation/README.md](../automation/README.md) for automation capability index.\n",
        ),
    )


def multi_lens_pointers() -> None:
    """Convert high-churn multi-lens duplicates to pointers to knowledge canonicals."""
    policy = ROOT / "docs" / "multi-lens-policy.md"
    write(
        policy,
        """---
title: Multi-Lens Documentation Policy
version: 1.0.0
last_updated: 2026-07-18
---

# Multi-Lens Documentation Policy

## Purpose

Prevent duplicate full articles across QE packs (knowledge, ADO, automation-intelligence, production-support, enterprise-quality) while preserving lens-specific advice.

## Rule

1. **One canonical** article owns the full body (usually under `salesforce-quality-engineering/knowledge/`).
2. Other locations keep a **thin pointer** (frontmatter `type: pointer`) plus optional 5–15 line lens delta if truly unique.
3. Agents load the canonical path; they may add lens context in the *response*, not by inventing a second full KB article.

## Canonical map (priority topics)

| Topic | Canonical |
|-------|-----------|
| Quality gates | `salesforce-quality-engineering/knowledge/quality-gates.md` |
| Release readiness | `salesforce-quality-engineering/knowledge/release/release-readiness.md` (fallback: playbooks if release article absent) |
| Cloud products | `salesforce-quality-engineering/knowledge/clouds/<cloud>.md` |
| Platform Events | `salesforce-quality-engineering/knowledge/integration/platform-events.md` |
| Smoke / sanity / regression planning | `salesforce-quality-engineering/knowledge/release/` |
| Consulting principles (enterprise) | `shared/consulting-principles.md` |

## Anti-patterns

- Copy-pasting a full cloud article into automation-intelligence, production-support, and enterprise-quality
- Maintaining divergent versions of the same gate definitions
""",
    )

    # quality-gates pointers
    qg_canon = "../../knowledge/quality-gates.md"
    # from ado/governance (depth 2)
    for rel, depth_canon, lens in [
        ("ado/governance/quality-gates.md", "../../knowledge/quality-gates.md", "ADO governance lens"),
        ("automation-intelligence/ci-cd/quality-gates.md", "../../knowledge/quality-gates.md", "CI/CD automation lens"),
        ("enterprise-quality/delivery-governance/quality-gates.md", "../../knowledge/quality-gates.md", "Enterprise delivery governance lens"),
        ("production-support/operational-excellence/quality-gates.md", "../../knowledge/quality-gates.md", "Production / ops excellence lens"),
    ]:
        write(QE / rel, pointer("Quality Gates", depth_canon, lens))

    # release-readiness — find canonical
    rr_canon = QE / "knowledge" / "release" / "release-readiness.md"
    if not rr_canon.exists():
        # try playbooks
        pb = QE / "playbooks" / "release-readiness.md"
        canon_from = {
            "ado/governance/release-readiness.md": (
                "../../playbooks/release-readiness.md" if pb.exists() else "../../knowledge/release/README.md"
            ),
        }
    # Prefer knowledge/release if exists else playbooks
    if (QE / "knowledge" / "release" / "release-readiness.md").exists():
        rr = "knowledge/release/release-readiness.md"
    elif (QE / "playbooks" / "release-readiness.md").exists():
        rr = "playbooks/release-readiness.md"
    else:
        rr = None

    if rr:
        # Keep the chosen canonical as full content; pointer others
        keep = QE / rr
        for rel, link in [
            ("ado/governance/release-readiness.md", "../../" + rr),
            ("automation-intelligence/automation-governance/release-readiness.md", "../../" + rr),
            ("production-support/release-operations/release-readiness.md", "../../" + rr),
        ]:
            if (QE / rel).resolve() == keep.resolve():
                continue
            # Don't overwrite playbooks if that IS canonical
            if Path(rel).as_posix() == rr:
                continue
            write(QE / rel, pointer("Release Readiness", link, f"Lens file → canonical {rr}"))
        # If playbooks is not canonical, pointer it too when duplicate
        if rr.startswith("knowledge/") and (QE / "playbooks" / "release-readiness.md").exists():
            write(
                QE / "playbooks" / "release-readiness.md",
                pointer("Release Readiness", f"../{rr}", "Playbook ceremony entry → release knowledge canonical"),
            )

    # Cloud articles in EQ / AI / PS → knowledge/clouds
    clouds = [
        "sales-cloud",
        "service-cloud",
        "experience-cloud",
        "field-service",
        "agentforce",
        "omnistudio",
        "marketing-cloud",
        "data-cloud",
        "revenue-cloud",
    ]
    # map EQ revenue-cloud.md → knowledge revenue-cloud-cpq.md if needed
    cloud_map = {
        "revenue-cloud": "revenue-cloud-cpq",
    }

    for cloud in clouds:
        canon_name = cloud_map.get(cloud, cloud)
        canon = QE / "knowledge" / "clouds" / f"{canon_name}.md"
        if not canon.exists():
            continue
        for folder in (
            "enterprise-quality/salesforce",
            "automation-intelligence/salesforce",
            "production-support/salesforce",
        ):
            p = QE / folder / f"{cloud}.md"
            if not p.exists():
                continue
            # Don't pointer if somehow same as canon
            write(
                p,
                pointer(
                    cloud.replace("-", " ").title(),
                    f"../../knowledge/clouds/{canon_name}.md",
                    f"{folder} lens → knowledge/clouds canonical",
                ),
            )


def consulting_principles_canonical() -> None:
    # QE brain → shared + QE delta
    write(
        QE / "brain" / "consulting-principles.md",
        """---
title: Consulting Principles (QE)
module: Salesforce Quality Engineering
category: Brain
document_type: Framework
version: 0.12.2
status: draft
last_updated: 2026-07-18
tags: [brain, consulting]
---

# Consulting Principles (QE)

**Enterprise canonical:** [shared/consulting-principles.md](../../shared/consulting-principles.md)

Load the shared principles first. This file adds the **QE-specific** consulting delta only.

## QE consulting mindset

You are a trusted Quality Engineering advisor. You challenge incomplete work, surface risk early, and protect customer and release outcomes.

| Do | Don't |
|----|-------|
| Challenge incomplete requirements and AC | Accept vague stories and invent silent scope |
| Recommend risk-based coverage | Equate “more cases” with quality |
| Separate facts vs assumptions | Invent pass rates, SLA, or maturity scores |
| Prefer platform-native testability | Prescribe Apex/LWC unless constrained |
| Advise automation purpose and architecture | Generate full automation scripts by default |

## Behaviour rules

1. Shift-left: requirement analysis before detailed cases.
2. Evidence over opinion for release and readiness.
3. Persona and permission paths when Salesforce UI/data access is involved.
4. Route via [enterprise-orchestrator/](../enterprise-orchestrator/README.md) before deep packs.

## Related

- [shared/consulting-principles.md](../../shared/consulting-principles.md)
- [quality-philosophy.md](quality-philosophy.md)
- [response-guidelines.md](response-guidelines.md)
""",
    )

    ba_cp = BA / "brain" / "consulting-principles.md"
    if ba_cp.exists():
        write(
            ba_cp,
            """---
title: Consulting Principles (BA)
module: Salesforce Business Analyst
category: Brain
document_type: Framework
version: 1.2.0
status: draft
last_updated: 2026-07-18
tags: [brain, consulting]
---

# Consulting Principles (BA)

**Enterprise canonical:** [shared/consulting-principles.md](../../shared/consulting-principles.md)

Load the shared principles first. This file adds the **BA-specific** consulting delta only.

## BA consulting mindset

| Do | Don't |
|----|-------|
| Outcomes over feature lists | Document for documentation’s sake |
| Traceable, testable requirements | Invent regulatory requirements |
| Platform-native before custom | Bypass security / sharing controls |
| Flag assumptions and out-of-scope | Silent scope expansion |

## Related

- [shared/consulting-principles.md](../../shared/consulting-principles.md)
- [identity.md](identity.md)
- [reasoning-framework.md](reasoning-framework.md)
""",
        )

    # Update shared frontmatter related_brain_modules note
    shared = ROOT / "shared" / "consulting-principles.md"
    t = shared.read_text(encoding="utf-8")
    if "Canonical enterprise consulting principles" not in t:
        t = t.replace(
            "# Consulting Principles\n\nEnterprise consulting principles applied across all Salesforce skills.",
            "# Consulting Principles\n\n**Canonical** enterprise consulting principles for all Salesforce skills. Module brains (`salesforce-business-analyst/brain/consulting-principles.md`, `salesforce-quality-engineering/brain/consulting-principles.md`) hold role-specific deltas only.",
        )
        shared.write_text(t, encoding="utf-8")
        print("UPDATED shared/consulting-principles.md canonical banner")


def add_readmes() -> None:
    stubs = [
        (BA / "examples" / "README.md", "BA Examples", "Sample BA artifacts for training and demos.", "../skill.md"),
        (BA / "interview-guide" / "advanced" / "README.md", "Interview Guide — Advanced", "Advanced BA interview topics.", "../interview-index.md"),
        (BA / "interview-guide" / "delivery" / "README.md", "Interview Guide — Delivery", "Delivery-focused interview topics.", "../interview-index.md"),
        (BA / "interview-guide" / "salesforce" / "README.md", "Interview Guide — Salesforce", "Salesforce-specific interview topics.", "../interview-index.md"),
        (ROOT / "shared" / "README.md", "Shared", "Cross-skill glossary, standards, capability map, and shared principles.", "../README.md"),
        (ROOT / "docs" / "README.md", "Docs", "Repository governance, metadata schema, architecture, and cross-linking.", "../README.md"),
        (ROOT / "examples" / "README.md", "Examples", "Anonymized sample project artifacts (BRD, stories, workshops).", "../README.md"),
        (ROOT / "examples" / "sample-brd" / "README.md", "Sample BRD", "Example business requirements pack.", "../README.md"),
        (ROOT / "examples" / "sample-user-story" / "README.md", "Sample User Story", "Example user story pack.", "../README.md"),
        (ROOT / "examples" / "sample-workshop" / "README.md", "Sample Workshop", "Example workshop notes/agenda.", "../README.md"),
        (ROOT / "scripts" / "README.md", "Scripts", "Repo utilities (context retrieval, metadata validation, generators).", "../README.md"),
        (QE / "scripts" / "README.md", "QE Scripts", "Sprint knowledge generators for the QE module.", "../README.md"),
        (ROOT / ".cursor" / "README.md", "Cursor Config", "Cursor rules and skill discovery stubs for this repository.", "../README.md"),
        (ROOT / ".cursor" / "rules" / "README.md", "Cursor Rules", "Persistent agent rules (routing, BA instructions, output engine).", "../README.md"),
        (ROOT / ".cursor" / "skills" / "README.md", "Cursor Skills", "Thin discovery stubs. Canonical skills live under module folders.", "../README.md"),
        (ROOT / ".cursor" / "skills" / "salesforce-quality-engineering" / "README.md", "QE Cursor Skill Stub", "Discovery stub → `salesforce-quality-engineering/skill.md`.", "../../../../salesforce-quality-engineering/skill.md"),
        (ROOT / "output-engine" / "configuration" / "README.md", "Output Engine — Configuration", "Routing rules and conversion config.", "../README.md"),
        (ROOT / "output-engine" / "conversion_logging" / "README.md", "Output Engine — Conversion Logging", "Conversion report helpers.", "../README.md"),
        (ROOT / "output-engine" / "converters" / "README.md", "Output Engine — Converters", "Format converters (docx, pptx, xlsx, pdf).", "../README.md"),
        (ROOT / "output-engine" / "orchestrator" / "README.md", "Output Engine — Orchestrator", "Batch/single-file conversion orchestration.", "../README.md"),
        (ROOT / "output-engine" / "shared" / "README.md", "Output Engine — Shared", "Shared conversion utilities.", "../README.md"),
        (ROOT / "output-engine" / "tests" / "README.md", "Output Engine — Tests", "Unit/integration tests for converters.", "../README.md"),
        (ROOT / "output-engine" / "tests" / "fixtures" / "README.md", "Output Engine — Test Fixtures", "Fixture files for converter tests.", "../README.md"),
    ]

    industries = ["banking", "healthcare", "insurance", "retail", "telecom", "utilities"]
    for ind in industries:
        stubs.append(
            (
                BA / "scenarios" / ind / "README.md",
                f"BA Scenarios — {ind.title()}",
                f"Industry scenario pack for {ind}.",
                "../README.md",
            )
        )

    for path, title, purpose, up in stubs:
        if path.exists() and path.stat().st_size > 80:
            print(f"SKIP existing {path.relative_to(ROOT)}")
            continue
        write(
            path,
            f"""---
title: {title}
last_updated: 2026-07-18
---

# {title}

## Purpose

{purpose}

## Scope

Navigation and ownership for this folder. Content files in this directory are authoritative for their topics.

## Inputs / Outputs

- **Inputs:** Linked skill, brain, and knowledge modules
- **Outputs:** Documents and guidance contained in this folder

## Navigation

- **Up:** [{up}]({up})
- **Repo root:** [README.md]({"../" * (len(path.relative_to(ROOT).parts) - 1)}README.md)

## Related Documents

See parent module README. Multi-lens topics: `docs/multi-lens-policy.md`.
""",
        )


def resolve_stubs_and_archive() -> None:
    # QE interview-guide stub at module root
    write(
        QE / "interview-guide.md",
        """---
title: QE Interview Guide (Entry)
type: pointer
status: redirect
last_updated: 2026-07-18
---

# QE Interview Guide

**Canonical:** [knowledge/interview-guide.md](knowledge/interview-guide.md)

Also cross-link BA interviews: [../salesforce-business-analyst/interview-guide/interview-index.md](../salesforce-business-analyst/interview-guide/interview-index.md)
""",
    )

    # knowledge/reports hub
    write(
        QE / "knowledge" / "reports" / "README.md",
        """---
title: QE Knowledge — Reports
last_updated: 2026-07-18
---

# Reports (Knowledge Hub)

## Purpose

Index reporting guidance for Salesforce QE. Detailed ADO reporting lives under `ado/reports/`; executive dashboards under `enterprise-quality/executive-reporting/`.

## Scope

Pointers only — do not invent KPI values.

## Navigation

- [ADO Reports](../../ado/reports/README.md)
- [Executive Reporting](../../enterprise-quality/executive-reporting/README.md)
- [Metrics](../metrics.md)
- [Quality Gates](../quality-gates.md)

## Related

- [Multi-Lens Policy](../../../docs/multi-lens-policy.md)
""",
    )

    # QE scenarios — populate as hub pointing to BA + QE industry knowledge
    write(
        QE / "scenarios" / "README.md",
        """---
title: QE Scenarios
version: 0.12.2
last_updated: 2026-07-18
---

# QE Scenarios

## Purpose

Industry and journey scenario entry points for Quality Engineering. Prefer reuse of BA scenario packs plus QE industry knowledge — do not duplicate full narratives.

## Scope

- **In:** Links to BA scenarios and QE `knowledge/industry/` articles; QE testing overlays
- **Out:** Inventing client-specific scenarios or full BA story authorship

## Scenario sources

| Source | Path |
|--------|------|
| BA industry scenarios | [../../salesforce-business-analyst/scenarios/](../../salesforce-business-analyst/scenarios/README.md) |
| QE industry knowledge | [../knowledge/industry/](../knowledge/industry/README.md) |
| Cloud product knowledge | [../knowledge/clouds/](../knowledge/clouds/README.md) |

## How to use

1. Load BA scenario for business context.
2. Overlay QE risks, test design, regression, and automation readiness via engines.
3. For executive portfolio views, route via [enterprise-orchestrator/](../enterprise-orchestrator/README.md) → Sprint 10.

## Navigation

- **Up:** [../README.md](../README.md)
- **Next:** [../knowledge/industry/README.md](../knowledge/industry/README.md)
""",
    )

    # automation/ pointer — strengthen and mark intentional
    write(
        QE / "automation" / "README.md",
        """---
title: Automation (Legacy Path)
type: pointer
status: redirect
last_updated: 2026-07-18
---

# Automation (Legacy Path)

**Canonical pack:** [../automation-intelligence/](../automation-intelligence/README.md)

This folder is retained as a **legacy redirect** for older links. Do not add new articles here.

Sprint 4A platform automation knowledge (Flows, Apex, etc.) remains under [../knowledge/automation/](../knowledge/automation/README.md) — that is a different folder.
""",
    )

    # Archive zzz folder
    src = ROOT / "zzz_ImplmentationGuide"
    dest = ROOT / "archive" / "implementation-guide-legacy"
    if src.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            print("ARCHIVE target already exists - skip move")
        else:
            shutil.move(str(src), str(dest))
            print(f"MOVED zzz_ImplmentationGuide -> {dest.relative_to(ROOT)}")
        write(
            ROOT / "archive" / "README.md",
            """---
title: Archive
last_updated: 2026-07-18
---

# Archive

Legacy materials retained for reference. **Not** part of the active skill loading path.

| Folder | Note |
|--------|------|
| [implementation-guide-legacy/](implementation-guide-legacy/) | Former `zzz_ImplmentationGuide/` (typo name corrected on archive) |

Active guidance lives under `salesforce-business-analyst/`, `salesforce-quality-engineering/`, `docs/`, and `shared/`.
""",
        )


def ba_cursor_skill() -> None:
    stub = ROOT / ".cursor" / "skills" / "salesforce-business-analyst" / "SKILL.md"
    write(
        stub,
        """---
name: salesforce-business-analyst
description: >-
  Salesforce Business Analyst skill for discovery, BRD/FRD, user stories,
  fit-gap, workshops, RTM, RAID, and ADO backlog guidance. Load
  salesforce-business-analyst/skill.md and brain modules. Prefer platform-native
  solutions; never invent regulatory requirements or bypass security.
version: 1.1.0
---

# Salesforce Business Analyst (Cursor Discovery Stub)

## Canonical location

**[`salesforce-business-analyst/`](../../../salesforce-business-analyst/README.md)**

| Priority | Path |
|----------|------|
| Skill entry | [`skill.md`](../../../salesforce-business-analyst/skill.md) |
| Brain | [`brain/`](../../../salesforce-business-analyst/brain/README.md) |
| Knowledge | [`knowledge/`](../../../salesforce-business-analyst/knowledge/README.md) |
| Templates | [`templates/`](../../../salesforce-business-analyst/templates/README.md) |
| Playbooks | [`playbooks/`](../../../salesforce-business-analyst/playbooks/README.md) |
| Scenarios | [`scenarios/`](../../../salesforce-business-analyst/scenarios/README.md) |
| Interview guide | [`interview-guide/`](../../../salesforce-business-analyst/interview-guide/interview-index.md) |
| Prompts | [`prompts.md`](../../../salesforce-business-analyst/prompts.md) |

## Hard rules

1. Complete Pre-Execution Gate in skill.md before deliverables.
2. Traceable requirement IDs; INVEST stories; Given/When/Then AC.
3. Never invent regulatory requirements — cite or mark TBC with Legal/Compliance.
4. Prefer standard Salesforce features before custom build.
5. Save outputs under `outputs/<project>/` and run the output engine when publishing artifacts.
""",
    )
    write(
        ROOT / ".cursor" / "skills" / "salesforce-business-analyst" / "README.md",
        """---
title: BA Cursor Skill Stub
last_updated: 2026-07-18
---

# BA Cursor Skill Stub

Discovery stub → [`salesforce-business-analyst/skill.md`](../../../salesforce-business-analyst/skill.md).
""",
    )


def naming_ba_changelog() -> None:
    """Normalize BA changelog filename. On Windows, use git mv (case-only rename)."""
    import subprocess

    ba_dir = BA
    # Prefer git mv for case-only rename on case-insensitive FS
    lower = ba_dir / "changelog.md"
    # If content looks like a mistaken self-pointer, restore is caller's job
    try:
        r = subprocess.run(
            ["git", "mv", "salesforce-business-analyst/changelog.md", "salesforce-business-analyst/CHANGELOG.md"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if r.returncode == 0:
            print("RENAMED BA changelog.md -> CHANGELOG.md via git mv")
        else:
            print(f"BA changelog rename skipped: {r.stderr.strip() or r.stdout.strip()}")
    except Exception as e:
        print(f"BA changelog rename skipped: {e}")
    _ = lower  # keep lint calm


def bump_changelog() -> None:
    cl = QE / "CHANGELOG.md"
    t = cl.read_text(encoding="utf-8")
    if "0.12.2" in t:
        print("CHANGELOG already has 0.12.2")
        return
    entry = """## [0.12.2] - 2026-07-18

### Fixed

- Repository quality audit remediation:
  - Cursor rules Related links (`../../` depth)
  - QE `ado/README.md` and `knowledge/{references,examples,metrics,interview-guide}.md` link depths
  - `skill.md` → `brain/cross-module-map.md`
  - Knowledge root smoke/sanity/regression → `knowledge/release/` pointers
  - Dual `platform-events` → integration canonical
  - Multi-lens pointers for quality-gates, release-readiness, cloud articles
  - Shared consulting-principles as enterprise canonical; BA/QE brain deltas
  - Missing READMEs; BA Cursor skill stub; QE scenarios hub; `knowledge/reports/`
  - Module-root `interview-guide.md` pointer; archived `zzz_ImplmentationGuide/` → `archive/implementation-guide-legacy/`
  - BA `CHANGELOG.md` case normalization
  - [docs/multi-lens-policy.md](../docs/multi-lens-policy.md)

"""
    t = t.replace("## [Unreleased]\n\n", f"## [Unreleased]\n\n{entry}")
    t = t.replace("version: 0.12.1", "version: 0.12.2", 1)
    t = t.replace("**Version:** 0.12.1", "**Version:** 0.12.2", 1)
    cl.write_text(t, encoding="utf-8")
    print("UPDATED QE CHANGELOG 0.12.2")


def main() -> None:
    fix_output_generation_rule()
    fix_qe_links()
    merge_knowledge_overlaps()
    multi_lens_pointers()
    consulting_principles_canonical()
    add_readmes()
    resolve_stubs_and_archive()
    ba_cursor_skill()
    naming_ba_changelog()
    bump_changelog()
    # version bump skill/readme lightly
    for rel in ("skill.md", "README.md"):
        p = QE / rel
        t = p.read_text(encoding="utf-8")
        t2 = t.replace("0.12.1", "0.12.2")
        if t2 != t:
            p.write_text(t2, encoding="utf-8")
            print(f"BUMPED {rel} -> 0.12.2")
    print("DONE")


if __name__ == "__main__":
    main()
