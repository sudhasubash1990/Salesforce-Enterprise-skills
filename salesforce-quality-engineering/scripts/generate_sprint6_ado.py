#!/usr/bin/env python3
"""Generate Sprint 6 — Azure DevOps Delivery Intelligence (no API publish)."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADO = ROOT / "ado"
VERSION = "0.8.0"
DATE = "2026-07-17"
SPRINT = "Sprint 6"

def cross_links(prefix: str) -> list[str]:
    """prefix: '..' from ado/*.md, '../..' from ado/<folder>/*.md"""
    return [
        f"[QE Brain (Sprint 1)]({prefix}/brain/README.md)",
        f"[Requirement Analysis (Sprint 2)]({prefix}/knowledge/requirement-analysis.md)",
        f"[Test Design Engine (Sprint 3)]({prefix}/knowledge/test-design-engine.md)",
        f"[Platform Foundation 4A]({prefix}/knowledge/platform/README.md)",
        f"[Enterprise Knowledge 4B]({prefix}/knowledge/clouds/README.md)",
        f"[Documentation Generator (Sprint 5)]({prefix}/templates/README.md)",
        f"[BA ADO Backlog Integration]({prefix}/../salesforce-business-analyst/knowledge/ado-backlog-integration.md) (sibling—do not duplicate)",
    ]


CROSS = cross_links("../..")  # default for folder docs
CROSS_ROOT = cross_links("..")  # for ado/*.md


def titleize(slug: str) -> str:
    special = {
        "user-story": "User Story",
        "test-plan": "Test Plan",
        "test-suite": "Test Suite",
        "test-case": "Test Case",
        "shared-steps": "Shared Steps",
        "area-path": "Area Path",
        "definition-of-ready": "Definition of Ready",
        "definition-of-done": "Definition of Done",
        "qa-lead-dashboard": "QA Lead Dashboard",
        "test-manager-dashboard": "Test Manager Dashboard",
        "project-manager-dashboard": "Project Manager Dashboard",
        "release-manager-dashboard": "Release Manager Dashboard",
        "delivery-manager-dashboard": "Delivery Manager Dashboard",
        "executive-dashboard": "Executive Leadership Dashboard",
    }
    return special.get(slug, slug.replace("-", " ").title())


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {i}" for i in items)


def folder_readme(folder: str, title: str, purpose: str, when: str, inputs: list[str], outputs: list[str], practices: list[str], articles: list[tuple[str, str]], prev: str, nxt: str) -> str:
    rows = "\n".join(f"| [{titleize(s)}]({s}.md) | {b} |" for s, b in articles) if articles else "| — | See folder guidance |"
    return f"""---
title: {title} — README
module: Salesforce Quality Engineering
category: ADO
document_type: Guide
version: {VERSION}
review_status: Draft
owner: QE Practice Lead
created_date: {DATE}
last_updated: {DATE}
tags: [ado, sprint-6, {folder}]
---

# {title}

## Purpose

{purpose}

## When Used

{when}

## Inputs

{bullets(inputs)}

## Outputs

{bullets(outputs)}

## Best Practices

{bullets(practices)}

## Available Documents

| Document | Focus |
|----------|-------|
{rows}

## Scope note

**{SPRINT} focuses on Delivery Intelligence** — work item quality, relationships, and ADO-ready artifact content.  
**Not in scope:** Azure DevOps REST API automation / auto-publish (optional later enhancement).

## Navigation

- **Previous:** [{prev}]({prev})
- **Next:** [{nxt}]({nxt})
- **See Also:** [../README.md](../README.md) · [../relationship-model.md](../relationship-model.md)

## Related Documents

{bullets(CROSS)}
"""  # CROSS is correct for folder READMEs (ado/<folder>/)


def knowledge_doc(folder: str, slug: str, meta: dict, nav: dict) -> str:
    title = meta.get("title") or titleize(slug)
    purpose = meta["purpose"]
    related = meta.get("related", []) + CROSS + [
        "[README.md](README.md)",
        "[../README.md](../README.md)",
        "[../relationship-model.md](../relationship-model.md)",
    ]

    def sec(key: str, heading: str, default: list[str] | str) -> str:
        val = meta.get(key, default)
        body = val if isinstance(val, str) else bullets(val)
        return f"## {heading}\n\n{body}\n"

    default_practices = [
        "One outcome per work item where practical",
        "Link, do not duplicate BA story content",
        "Use tags for Smoke/Regression/UAT/Automation",
    ]
    default_mistakes = [
        "Orphan work items with no parent/links",
        "Tasks that are epics in disguise",
        "Bugs without repro steps or environment",
        "Test cases without requirement mapping",
    ]
    default_qe = [
        "Work items are the backbone of evidence—not just task tracking.",
        "QE ensures testability, traceability, and release readiness signals in ADO.",
    ]

    parts = [
        f"---\ntitle: {title}\nmodule: Salesforce Quality Engineering\ncategory: ADO\n"
        f"document_type: Knowledge Article\nversion: {VERSION}\nreview_status: Draft\n"
        f"owner: QE Practice Lead\ncreated_date: {DATE}\nlast_updated: {DATE}\n"
        f"tags: [ado, sprint-6, {folder}]\nkeywords: [{slug}, azure-devops, quality-engineering]\n---\n\n"
        f"# {title}\n\n"
        f"**Scope:** {SPRINT} Azure DevOps Delivery Intelligence — QE lens. "
        f"Artifact content quality, not ADO admin or API automation.\n\n"
        f"**Version:** {VERSION}\n\n---\n\n",
        sec("purpose", "Purpose", purpose),
        sec(
            "business_context",
            "Business Context",
            [
                "Supports enterprise Salesforce delivery governance and traceability.",
                "Aligns BA backlog language with QE evidence.",
            ],
        ),
        sec(
            "lifecycle",
            "Lifecycle",
            [
                "Created → Active → Resolved/Closed (or Done) per process template",
                "Link upward to parent and downward to children/tests/bugs",
            ],
        ),
        sec(
            "inputs",
            "Inputs",
            [
                "Scope / requirements",
                "Prior analysis or design artifacts",
                "Area Path / Iteration context",
            ],
        ),
        sec(
            "outputs",
            "Outputs",
            [
                f"Well-formed {title} ready to paste into Azure DevOps",
                "Links for traceability",
            ],
        ),
        sec(
            "relationships",
            "Relationships",
            ["See [Relationship Model](../relationship-model.md)"],
        ),
        sec(
            "examples",
            "Examples",
            [
                "Title pattern: `<Capability> - <Outcome>`",
                "Keep descriptions scannable with headings and bullets",
            ],
        ),
        sec(
            "testing",
            "Testing Considerations",
            [
                "Every User Story should drive scenarios/cases",
                "Bugs must link to failing case/story when known",
                "Test Plans organize evidence for release gates",
            ],
        ),
        sec(
            "governance",
            "Governance",
            [
                "Respect DoR/DoD",
                "Area Path and Iteration required for reporting",
                "No client PII/credentials in work item fields",
            ],
        ),
        sec("practices", "Best Practices", meta.get("practices", default_practices)),
        sec("mistakes", "Common Mistakes", meta.get("mistakes", default_mistakes)),
        sec(
            "qe_perspective",
            "Quality Engineering Perspective",
            meta.get("qe", default_qe),
        ),
        sec(
            "interview",
            "Interview Questions",
            [
                "How does this work item type support end-to-end traceability?",
                "What fields are mandatory for QE reporting?",
                "How do you avoid duplicate BA vs QE content?",
            ],
        ),
        "## Related Documents\n\n" + bullets(related) + "\n\n",
        "## Navigation\n\n"
        f"- **Previous:** [{nav['prev_label']}]({nav['prev']})\n"
        f"- **Next:** [{nav['next_label']}]({nav['next']})\n"
        "- **See Also:** [README.md](README.md)\n\n",
        "## Future Enhancements\n\n"
        "- Optional API publish helpers (post–Delivery Intelligence)\n"
        "- Project-specific process template mapping examples\n",
    ]
    return "".join(parts)


def nav_for(slugs: list[str], idx: int) -> dict:
    prev_slug = slugs[idx - 1] if idx > 0 else None
    next_slug = slugs[idx + 1] if idx < len(slugs) - 1 else None
    return {
        "prev": f"{prev_slug}.md" if prev_slug else "README.md",
        "prev_label": titleize(prev_slug) if prev_slug else "README",
        "next": f"{next_slug}.md" if next_slug else "README.md",
        "next_label": titleize(next_slug) if next_slug else "README",
    }


# Folder content catalogs: folder -> (title, purpose, when, inputs, outputs, practices, [(slug, blurb, meta)])
FOLDERS: dict[str, dict] = {
    "epics": {
        "title": "Epics",
        "purpose": "Portfolio-level outcomes that span multiple features for Salesforce programs.",
        "when": "Program initiation, PI planning, or when a large business outcome needs decomposition.",
        "inputs": ["Business outcomes", "Roadmap themes", "Cloud/industry context"],
        "outputs": ["Epic work items", "Child Feature links"],
        "practices": ["Outcome-oriented titles", "Measurable success criteria", "Link Features; avoid task-level detail"],
        "docs": [("epic", "Epic work item guidance", {
            "purpose": "Define a large business outcome that will be delivered through Features and Stories.",
            "relationships": ["Parent: Portfolio/Initiative (process-dependent)", "Children: Features", "Related: Risks, Releases"],
            "qe": ["Epic success criteria inform Test Strategy and Release RTM views", "Do not put test steps on Epics"],
        })],
    },
    "features": {
        "title": "Features",
        "purpose": "Capability slices under Epics that deliver shippable value when completed.",
        "when": "When decomposing Epics into deliverable capabilities for a PI/release.",
        "inputs": ["Epic", "Capability needs", "Dependencies"],
        "outputs": ["Feature work items", "Child User Stories"],
        "practices": ["Ship-oriented scope", "Clear acceptance themes", "Link Stories and Test Plans where useful"],
        "docs": [("feature", "Feature work item guidance", {
            "purpose": "Describe a capability that groups User Stories toward an Epic outcome.",
            "relationships": ["Parent: Epic", "Children: User Stories", "Related: Features (dependencies)"],
        })],
    },
    "user-stories": {
        "title": "User Stories",
        "purpose": "INVEST stories with testable AC—primary QE object for scenarios and cases.",
        "when": "Backlog refinement and sprint planning for Salesforce delivery teams.",
        "inputs": ["Feature", "BA story pack / AC", "Sprint 2 analysis"],
        "outputs": ["ADO User Story fields", "Links to cases/bugs"],
        "practices": ["Reuse BA story content; enrich with QE links", "AC in nested bullets", "DoR before pull"],
        "docs": [("user-story", "User Story work item guidance", {
            "purpose": "Capture role/goal/benefit and testable acceptance criteria for a shippable increment.",
            "relationships": ["Parent: Feature", "Children: Tasks", "Tests: Test Cases", "Defects: Bugs"],
            "qe": ["Primary hook for Test Design Engine and Sprint 5 case templates", "Link AC ↔ scenarios ↔ cases"],
            "related": ["[../../templates/test-scenario-document.md](../../templates/test-scenario-document.md)", "[../../templates/test-case-document.md](../../templates/test-case-document.md)"],
        })],
    },
    "tasks": {
        "title": "Tasks",
        "purpose": "Implementation/test activities that complete a User Story.",
        "when": "Sprint planning/breakdown for build, config, or test execution work.",
        "inputs": ["User Story", "Team capacity"],
        "outputs": ["Task work items with remaining work"],
        "practices": ["Small, completable in a sprint", "Separate test tasks from build tasks when useful", "Never hide a story inside a task"],
        "docs": [("task", "Task work item guidance", {
            "purpose": "Track concrete work to deliver or validate a User Story.",
            "mistakes": ["Tasks without parent Story", "Mega-tasks spanning multiple stories", "Using Tasks instead of Bugs for defects"],
        })],
    },
    "bugs": {
        "title": "Bugs",
        "purpose": "Defect work items with enterprise repro quality and release impact.",
        "when": "When verified failures are found in any environment.",
        "inputs": ["Failing case/scenario", "Environment/build", "Evidence"],
        "outputs": ["Bug work item", "Links to Story/Case", "Retest notes"],
        "practices": ["Severity ≠ Priority", "Always include Expected vs Actual", "Assess regression impact"],
        "docs": [
            ("bug", "Bug work item / Bug Intelligence", {
                "purpose": "Create enterprise-quality bug reports suitable for triage and release decisions.",
                "practices": [
                    "Title: concise failure statement",
                    "Fields: Environment, Area, Iteration, Build/Release, Steps, Expected, Actual, Severity, Priority, Business Impact, Evidence, Regression Impact, Retest Guidance",
                    "Link to Test Case and User Story when known",
                ],
                "related": ["[../../templates/defect-report.md](../../templates/defect-report.md)", "[../../guidelines/defect-documentation-standards.md](../../guidelines/defect-documentation-standards.md)"],
            }),
        ],
    },
    "test-plans": {
        "title": "Test Plans",
        "purpose": "Container for suites and cases used to evidence a sprint/release/UAT cycle.",
        "when": "Per sprint, release, SIT, UAT, or production validation cycle.",
        "inputs": ["Test Plan intent", "Scope", "Area/Iteration", "Suite strategy"],
        "outputs": ["Test Plan", "Suite structure", "Execution evidence"],
        "practices": ["One clear purpose per plan", "Align naming to release/sprint", "See suite organization guide"],
        "docs": [
            ("test-plan", "Test Plan work item / artifact", {
                "purpose": "Organize test execution for a defined scope and cadence.",
                "related": ["[../test-suites/README.md](../test-suites/README.md)", "[test-plans-organization.md](../test-plans-organization.md)"],
            }),
        ],
    },
    "test-suites": {
        "title": "Test Suites",
        "purpose": "Organize cases inside plans: static, requirement-based, query-based, and purpose packs.",
        "when": "When structuring execution for smoke, regression, UAT, release, or requirement coverage.",
        "inputs": ["Test Plan", "Requirements/stories", "Query criteria"],
        "outputs": ["Suites with cases assigned"],
        "practices": ["Prefer requirement-based for coverage", "Query-based for dynamic packs", "Static for curated smoke"],
        "docs": [
            ("test-suite", "Test Suite types and organization", {
                "purpose": "Explain Static, Requirement-Based, Query-Based suites and purpose packs (Smoke, Regression, UAT, Release).",
                "examples": [
                    "Static: curated Smoke suite",
                    "Requirement-based: auto-associate cases to Stories",
                    "Query-based: tag=Regression AND Area Path under Service",
                ],
            }),
        ],
    },
    "test-cases": {
        "title": "Test Cases",
        "purpose": "Executable ADO test cases with enterprise fields and tags.",
        "when": "After scenario objectives exist; for manual or automated execution in Test Plans.",
        "inputs": ["User Story/AC", "Scenario", "Sprint 5 case template"],
        "outputs": ["ADO Test Case steps", "Links to requirements", "Suite membership"],
        "practices": ["Map to Story/AC", "Tag Smoke/Regression/UAT", "Keep steps observable"],
        "docs": [
            ("test-case", "ADO Test Case generation guidance", {
                "purpose": "Generate enterprise-quality Azure DevOps test cases (content-ready for paste or later API).",
                "practices": [
                    "Fields: Title, Objective, Area Path, Iteration, Priority, Requirement Mapping, Preconditions, Test Data, Steps, Expected Results, Postconditions, Automation Status, Tags, Risk, Owner",
                    "Reuse [Sprint 5 test-case template](../../templates/test-case-document.md)",
                ],
            }),
            ("shared-steps", "Shared Steps", {
                "purpose": "Reusable step blocks for login, navigation, or common setup to reduce duplication.",
                "practices": ["Stable, high-reuse only", "Version carefully when setup changes"],
            }),
        ],
    },
    "queries": {
        "title": "Queries",
        "purpose": "Query strategy for delivery and quality visibility (no saved WIQL files in this sprint).",
        "when": "Dashboards, triage, release readiness, and daily execution stand-ups.",
        "inputs": ["Reporting need", "Area/Iteration", "Tags/states"],
        "outputs": ["Query design recommendations", "Filter/KPI definitions"],
        "practices": ["Start from decision needed", "Prefer shared queries under governance folders", "Document intent beside WIQL later"],
        "docs": [("query-intelligence", "Query strategy catalog", {
            "purpose": "Teach query strategy for Open Bugs, Blocked Cases, Failed Tests, Sprint/Regression/UAT progress, Release Readiness, High Severity, Unassigned, Automation Candidates, Production Validation—without creating actual WIQL yet.",
            "examples": [
                "Open Bugs: Work Item Type=Bug AND State not in Closed",
                "High Severity: Severity in 1-Critical,2-High AND State active",
                "Automation Candidates: Tag Contains AutomationCandidate",
            ],
        })],
    },
    "dashboards": {
        "title": "Dashboards",
        "purpose": "Role-based dashboard designs with KPIs and decision support.",
        "when": "Team, release, and executive governance cadences.",
        "inputs": ["Audience", "Decisions to support", "Available queries/widgets"],
        "outputs": ["Dashboard design specs (not widget JSON)"],
        "practices": ["One primary decision per dashboard", "Show residual risk, not vanity metrics", "Align filters to Area/Iteration"],
        "docs": [
            ("qa-lead-dashboard", "QA Lead dashboard design", {"purpose": "Day-to-day execution: pass rate, blockers, open bugs, case progress.", "practices": ["KPIs: executed vs planned, blocked count, Critical bugs", "Charts: burndown of cases, severity pie", "Filters: Iteration + Area"]}),
            ("test-manager-dashboard", "Test Manager dashboard design", {"purpose": "Cross-sprint quality and coverage posture.", "practices": ["KPIs: coverage themes, escape rate inputs, automation ratio", "Decision: deepen regression vs proceed"]}),
            ("project-manager-dashboard", "Project Manager dashboard design", {"purpose": "Delivery progress and quality risk for PM cadence.", "practices": ["KPIs: story done %, test progress, top risks"]}),
            ("release-manager-dashboard", "Release Manager dashboard design", {"purpose": "Go/No-Go evidence: readiness, open Critical/High, smoke results.", "practices": ["KPIs: readiness checklist status, failed smoke, rollback readiness"]}),
            ("delivery-manager-dashboard", "Delivery Manager dashboard design", {"purpose": "Program-level quality and dependency risk.", "practices": ["KPIs: PI objectives risk, cross-team defects, environment blockers"]}),
            ("executive-dashboard", "Executive Leadership dashboard design", {"purpose": "Outcome and residual risk view for steering.", "practices": ["KPIs: release recommendation, top 3 risks, customer-impacting defects", "Avoid raw case counts without context"]}),
        ],
    },
    "reports": {
        "title": "Reports",
        "purpose": "ADO-oriented reporting packages that complement Sprint 5 report templates.",
        "when": "Sprint end, release gates, executive reviews.",
        "inputs": ["Execution data", "Defects", "RTM/coverage"],
        "outputs": ["Report outlines mapped to ADO queries/dashboards"],
        "practices": ["Reuse Sprint 5 report templates", "Cite query sources", "No invented metrics"],
        "docs": [("ado-reporting", "ADO reporting guidance", {
            "purpose": "Map Sprint 5 reports (Daily/Weekly/Summary/Executive) to ADO queries and dashboards.",
            "related": ["[../../guidelines/reporting-standards.md](../../guidelines/reporting-standards.md)"],
        })],
    },
    "governance": {
        "title": "Governance",
        "purpose": "DoR/DoD, workflows, quality gates, and audit readiness for ADO-based delivery.",
        "when": "Process setup and every sprint/release gate.",
        "inputs": ["Methodology (Agile/Scrum/SAFe)", "Org standards"],
        "outputs": ["Gate checklists", "Workflow expectations"],
        "practices": ["Keep gates evidence-based", "Align with Sprint 5 checklists", "Audit: who/when/what linked"],
        "docs": [
            ("definition-of-ready", "Definition of Ready", {"purpose": "Criteria before a Story may be pulled into a sprint."}),
            ("definition-of-done", "Definition of Done", {"purpose": "Criteria before Story/Feature is Done—including test evidence."}),
            ("bug-workflow", "Bug workflow", {"purpose": "States, owners, and retest expectations for bugs."}),
            ("test-case-review", "Test case review", {"purpose": "Peer review expectations before suite inclusion."}),
            ("requirement-review", "Requirement review in ADO", {"purpose": "How QE review outcomes attach to Stories (links/comments)."}),
            ("sprint-readiness", "Sprint readiness", {"purpose": "Team ready to start sprint execution with environments/data/cases."}),
            ("release-readiness", "Release readiness (ADO view)", {"purpose": "ADO evidence pack for Go/No-Go.", "related": ["[../../templates/release-readiness-checklist.md](../../templates/release-readiness-checklist.md)"]}),
            ("quality-gates", "Quality gates", {"purpose": "Entry/exit gates mapped to ADO states and checklists."}),
            ("approval-workflow", "Approval workflow", {"purpose": "Who approves plans, UAT sign-off, and release recommendation."}),
            ("audit-readiness", "Audit readiness", {"purpose": "Traceability and evidence expectations for audits."}),
        ],
    },
    "work-items": {
        "title": "Additional Work Items & Constructs",
        "purpose": "Supporting ADO constructs used in enterprise delivery (Issue, Risk, Requirement, Iteration, etc.).",
        "when": "Whenever process templates use these types or planning constructs.",
        "inputs": ["Process template", "Program structure"],
        "outputs": ["Guidance for correct usage from QE lens"],
        "practices": ["Follow org process template", "Link Risks to Epics/Features", "Keep Area/Iteration clean for reporting"],
        "docs": [
            ("issue", "Issue work item", {"purpose": "Track impediments/issues that are not product bugs."}),
            ("risk", "Risk work item", {"purpose": "Track delivery/quality risks with mitigation owners."}),
            ("requirement", "Requirement work item", {"purpose": "Formal requirement type when used (CMMI/legacy); else map via Story/AC."}),
            ("iteration", "Iteration paths", {"purpose": "Timeboxes for sprint/PI planning and reporting filters."}),
            ("area-path", "Area Paths", {"purpose": "Team/product ownership structure for work and tests."}),
            ("build", "Build", {"purpose": "Associate bugs/tests with build numbers for evidence."}),
            ("release", "Release", {"purpose": "Release object/pipeline awareness for validation tagging."}),
            ("pipeline", "Pipeline (overview)", {"purpose": "QE awareness of CI/CD pipelines—gates and smoke hooks (not YAML authoring)."}),
            ("sprint", "Sprint construct", {"purpose": "Sprint as planning container: goals, capacity, quality exit."}),
            ("backlog", "Backlog", {"purpose": "Ordered work; QE ensures testability before commit."}),
            ("board", "Board", {"purpose": "Visual flow; WIP and blocked columns matter for QE daily management."}),
            ("query", "Query construct", {"purpose": "Saved query concept—see Query Intelligence for strategies."}),
            ("dashboard", "Dashboard construct", {"purpose": "Widget host—see role-based dashboard designs."}),
        ],
    },
}


def write_root_guides() -> None:
    (ADO / "relationship-model.md").write_text(f"""---
title: Azure DevOps Relationship Model
version: {VERSION}
tags: [ado, sprint-6]
---

# Azure DevOps Relationship Model

## Purpose

Teach end-to-end hierarchy and traceability for Salesforce QE delivery in Azure DevOps.

## Hierarchy

```
Portfolio / Initiative (optional)
        ↓
      Epic
        ↓
     Feature
        ↓
   User Story
        ↓
      Task
        ↓
    Test Case  ←── Shared Steps
        ↓
       Bug
        ↓
   Regression pack (suites/tags)
        ↓
     Release
        ↓
Production Validation
```

## Traceability across levels

| From | To | Why it matters |
|------|----|----------------|
| Epic | Feature | Outcome decomposition |
| Feature | User Story | Shippable increments |
| User Story | AC / Business Rule | Testability |
| User Story | Test Scenario / Case | Coverage evidence |
| Test Case | Bug | Failure linkage |
| Bug | Regression | Prevent recurrence |
| Release | Prod Validation | Go-live evidence |

## Quality Engineering Perspective

Without links, dashboards lie and audits fail. QE owns the integrity of the chain from requirement intent to production validation.

## Related Documents

{bullets(CROSS_ROOT)}
- [traceability-intelligence.md](traceability-intelligence.md)
- [artifact-generation.md](artifact-generation.md)

## Navigation

- **Previous:** [README.md](README.md)
- **Next:** [traceability-intelligence.md](traceability-intelligence.md)
""", encoding="utf-8")

    (ADO / "traceability-intelligence.md").write_text(f"""---
title: Traceability Intelligence
version: {VERSION}
tags: [ado, sprint-6]
---

# Traceability Intelligence

## Purpose

Automatically reason about mappings:

**Epic → Feature → User Story → Acceptance Criteria → Business Rule → Test Scenario → Test Case → Bug → Regression → Release → Production Validation**

## Why it matters

- Proves coverage for release decisions  
- Accelerates impact analysis when stories change  
- Supports audit and hypercare  
- Prevents orphan tests and silent scope  

## How the AI should map

1. Start from Story/AC (or Epic/Feature if portfolio view).  
2. Attach Salesforce components (4A/4B).  
3. Ensure scenarios exist (Sprint 3) before cases (Sprint 5/6).  
4. Link bugs to cases/stories.  
5. Tag regression; place in suites.  
6. Roll evidence into Release Readiness / Go-No-Go.  

## Related

- [relationship-model.md](relationship-model.md)
- [../templates/rtm.md](../templates/rtm.md)
- [../document-generation/rtm-generator.md](../document-generation/rtm-generator.md)
{bullets(CROSS_ROOT)}
""", encoding="utf-8")

    (ADO / "artifact-generation.md").write_text(f"""---
title: ADO Artifact Generation
version: {VERSION}
tags: [ado, sprint-6]
---

# Artifact Generation

## Purpose

Teach the AI to generate **ADO-ready content** (titles, descriptions, AC, steps)—not API calls.

## Artifacts

| Artifact | Guidance folder / doc |
|----------|------------------------|
| Epic | [epics/epic.md](epics/epic.md) |
| Feature | [features/feature.md](features/feature.md) |
| User Story | [user-stories/user-story.md](user-stories/user-story.md) |
| Task | [tasks/task.md](tasks/task.md) |
| Bug | [bugs/bug.md](bugs/bug.md) |
| Risk / Issue | [work-items/](work-items/README.md) |
| Test Plan / Suite / Case / Shared Steps | [test-plans/](test-plans/README.md) · [test-suites/](test-suites/README.md) · [test-cases/](test-cases/README.md) |
| Acceptance Criteria | Nested Given/When/Then; align userstory-generation rules |
| Definition of Ready / Done | [governance/](governance/README.md) |
| Release Notes | Summarize Stories Done + known limitations + test evidence themes |
| Deployment Validation | Link [../../templates/deployment-validation-checklist.md](../../templates/deployment-validation-checklist.md) |

## Rules

- Reuse Sprint 2/3/5 outputs; do not rewrite BA stories unless asked.  
- Follow INVEST for stories; nested AC bullets.  
- Leave Story Points empty unless user asks for indicative value.  
- Structure HTML-friendly headings/lists for ADO Description fields.  

## Related

{bullets(CROSS_ROOT)}
""", encoding="utf-8")

    (ADO / "test-plans-organization.md").write_text(f"""---
title: Azure DevOps Test Plans Organization
version: {VERSION}
tags: [ado, sprint-6]
---

# Azure DevOps Test Plans Organization

## When to create Test Plans

| Trigger | Plan intent |
|---------|-------------|
| Sprint start | Sprint execution plan |
| Release train | Release regression + smoke |
| SIT window | Integration suites |
| UAT start | Business validation suites |
| Prod deploy | Production validation / hypercare smoke |

## Suite strategies

| Suite type | Use |
|------------|-----|
| **Static** | Curated Smoke / critical path |
| **Requirement-based** | Coverage vs Stories/Requirements |
| **Query-based** | Dynamic packs by tag/Area/Iteration |
| **Regression** | Risk-based prior scope |
| **Smoke** | Post-deploy confidence |
| **UAT** | Business scenarios |
| **Release** | Full release evidence set |

## Organization tips

- Name: `YYYY.MM - <Release/Sprint> - <Purpose>`  
- Separate Automation vs Manual suites if helpful  
- Keep Smoke small and stable  

## Related

- [test-plans/README.md](test-plans/README.md)
- [test-suites/README.md](test-suites/README.md)
""", encoding="utf-8")


def main() -> None:
    ADO.mkdir(parents=True, exist_ok=True)
    write_root_guides()

    folder_order = [
        "epics", "features", "user-stories", "tasks", "bugs",
        "test-plans", "test-suites", "test-cases", "queries",
        "dashboards", "reports", "governance", "work-items",
    ]

    # Main ado README
    (ADO / "README.md").write_text(f"""---
title: Azure DevOps Delivery Intelligence — README
module: Salesforce Quality Engineering
version: {VERSION}
tags: [ado, sprint-6]
---

# Azure DevOps Delivery Intelligence

## Purpose

Enable the AI to guide Salesforce QA teams through the Agile delivery lifecycle in Azure DevOps—with enterprise-quality work items, test artifacts, traceability, dashboards, and governance.

## Scope ({SPRINT})

**In scope:** Work item hierarchy, relationships, ADO-ready artifact generation, Test Plans/Suites/Cases, bug intelligence, query/dashboard strategy, governance.  

**Out of scope:** Azure DevOps REST API automation / automatic work-item publish (optional later). Cross-link BA backlog integration; do not duplicate.

## Folder map

| Folder | Focus |
|--------|-------|
| [epics/](epics/README.md) | Epics |
| [features/](features/README.md) | Features |
| [user-stories/](user-stories/README.md) | User Stories |
| [tasks/](tasks/README.md) | Tasks |
| [bugs/](bugs/README.md) | Bugs |
| [test-plans/](test-plans/README.md) | Test Plans |
| [test-suites/](test-suites/README.md) | Test Suites |
| [test-cases/](test-cases/README.md) | Test Cases & Shared Steps |
| [queries/](queries/README.md) | Query intelligence |
| [dashboards/](dashboards/README.md) | Role-based dashboards |
| [reports/](reports/README.md) | ADO reporting |
| [governance/](governance/README.md) | DoR/DoD, gates, audit |
| [work-items/](work-items/README.md) | Issue, Risk, Iteration, Area, Build, Release, … |

## Core guides

| Guide | Focus |
|-------|-------|
| [relationship-model.md](relationship-model.md) | Hierarchy & links |
| [traceability-intelligence.md](traceability-intelligence.md) | E2E mapping |
| [artifact-generation.md](artifact-generation.md) | How to generate ADO artifacts |
| [test-plans-organization.md](test-plans-organization.md) | Plans & suite strategies |

## Navigation

- **Previous:** [../playbooks/README.md](../playbooks/README.md)
- **Next:** [relationship-model.md](relationship-model.md)
- **See Also:** [../skill.md](../skill.md) · [../templates/README.md](../templates/README.md)

## Related Documents

{bullets(CROSS_ROOT)}
""", encoding="utf-8")

    count = 1
    for i, folder in enumerate(folder_order):
        cfg = FOLDERS[folder]
        path = ADO / folder
        path.mkdir(parents=True, exist_ok=True)
        prev = f"../{folder_order[i-1]}/README.md" if i > 0 else "../README.md"
        nxt = f"../{folder_order[i+1]}/README.md" if i < len(folder_order) - 1 else "../README.md"
        articles = [(s, b) for s, b, _ in cfg["docs"]]
        (path / "README.md").write_text(
            folder_readme(
                folder, cfg["title"], cfg["purpose"], cfg["when"],
                cfg["inputs"], cfg["outputs"], cfg["practices"],
                articles, prev, nxt,
            ),
            encoding="utf-8",
        )
        count += 1
        slugs = [s for s, _, _ in cfg["docs"]]
        for idx, (slug, blurb, meta) in enumerate(cfg["docs"]):
            meta = {**meta, "title": meta.get("title") or titleize(slug)}
            (path / f"{slug}.md").write_text(
                knowledge_doc(folder, slug, meta, nav_for(slugs, idx)),
                encoding="utf-8",
            )
            count += 1

    print(f"Wrote ~{count} files + root guides under {ADO}")


if __name__ == "__main__":
    main()
