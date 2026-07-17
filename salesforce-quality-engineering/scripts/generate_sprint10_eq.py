#!/usr/bin/env python3
"""Generate Sprint 10 — Enterprise Quality Advisory & Continuous Quality Engineering Platform."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EQ = ROOT / "enterprise-quality"
VERSION = "0.12.0"
DATE = "2026-07-18"
SPRINT = "Sprint 10"


def cross(prefix: str) -> list[str]:
    return [
        f"[QE Brain (Sprint 1)]({prefix}/brain/README.md)",
        f"[Requirement Analysis (Sprint 2)]({prefix}/knowledge/requirement-analysis.md)",
        f"[Test Design Engine (Sprint 3)]({prefix}/knowledge/test-design-engine.md)",
        f"[Platform Foundation 4A]({prefix}/knowledge/platform/README.md)",
        f"[Enterprise Knowledge 4B]({prefix}/knowledge/clouds/README.md)",
        f"[Documentation Generator (Sprint 5)]({prefix}/templates/README.md)",
        f"[ADO Delivery Intelligence (Sprint 6)]({prefix}/ado/README.md)",
        f"[Defect Intelligence (Sprint 7)]({prefix}/quality-intelligence/README.md)",
        f"[Automation Intelligence (Sprint 8)]({prefix}/automation-intelligence/README.md)",
        f"[Production Support (Sprint 9)]({prefix}/production-support/README.md)",
    ]


CROSS = cross("../..")
CROSS_ROOT = cross("..")


def titleize(slug: str) -> str:
    special = {
        "tmmi": "TMMi",
        "istqb-maturity": "ISTQB Maturity",
        "gdpr": "GDPR",
        "soc-2": "SOC 2",
        "iso-27001": "ISO 27001",
        "pci-dss": "PCI DSS",
        "hipaa-overview": "HIPAA (Overview)",
        "wcag": "Accessibility (WCAG)",
        "cio-dashboard": "CIO Dashboard",
        "cto-dashboard": "CTO Dashboard",
        "cqo-dashboard": "CQO Dashboard",
        "coe-dashboard": "Salesforce CoE Dashboard",
        "arb-dashboard": "Architecture Review Board Dashboard",
        "dora": "DORA Concepts",
        "ai-readiness": "AI Readiness",
        "agentforce": "Agentforce",
        "omnistudio": "OmniStudio",
        "experience-cloud": "Experience Cloud",
        "revenue-cloud": "Revenue Cloud",
        "data-cloud": "Data Cloud",
        "field-service": "Field Service",
        "marketing-cloud": "Marketing Cloud",
        "90-day-improvement-plan": "90-Day Improvement Plan",
        "6-month-quality-transformation": "6-Month Quality Transformation",
        "12-month-automation-roadmap": "12-Month Automation Roadmap",
        "togaf-governance-concepts": "TOGAF Governance Concepts",
    }
    return special.get(slug, slug.replace("-", " ").title())


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {i}" for i in items)


def folder_readme(
    folder: str,
    title: str,
    purpose: str,
    scope: str,
    inputs: list[str],
    outputs: list[str],
    articles: list[tuple[str, str]],
    prev: str,
    nxt: str,
) -> str:
    rows = "\n".join(f"| [{titleize(s)}]({s}.md) | {b} |" for s, b in articles)
    return f"""---
title: {title} — README
module: Salesforce Quality Engineering
category: Enterprise Quality
document_type: Guide
version: {VERSION}
review_status: Draft
owner: QE Practice Lead
created_date: {DATE}
last_updated: {DATE}
tags: [enterprise-quality, sprint-10, {folder}]
---

# {title}

## Purpose

{purpose}

## Scope

{scope}

Reuse Sprints 1–9 engines—do not duplicate Requirement Analysis, Defect Intelligence, Automation Review, or Production Ops content; **assess and advise** using them.

## Inputs

{bullets(inputs)}

## Outputs

{bullets(outputs)}

## Available Documents

| Document | Focus |
|----------|-------|
{rows}

## Navigation

- **Previous:** [{prev}]({prev})
- **Next:** [{nxt}]({nxt})
- **See Also:** [../README.md](../README.md)

## Related Documents

{bullets(CROSS)}
"""


def article(folder: str, slug: str, meta: dict, nav: dict) -> str:
    title = meta.get("title") or titleize(slug)
    purpose = meta.get("purpose") or f"Provide enterprise advisory guidance on {title}."
    related = meta.get("related", []) + CROSS + [
        "[README.md](README.md)",
        "[../README.md](../README.md)",
        "[../enterprise-quality-advisory-engine.md](../enterprise-quality-advisory-engine.md)",
    ]

    def sec(key: str, heading: str, default: list[str] | str) -> str:
        val = meta.get(key, default)
        body = val if isinstance(val, str) else bullets(val)
        return f"## {heading}\n\n{body}\n"

    return (
        f"---\ntitle: {title}\nmodule: Salesforce Quality Engineering\n"
        f"category: Enterprise Quality\ndocument_type: Knowledge Article\n"
        f"version: {VERSION}\nreview_status: Draft\nowner: QE Practice Lead\n"
        f"created_date: {DATE}\nlast_updated: {DATE}\n"
        f"tags: [enterprise-quality, sprint-10, {folder}]\n"
        f"keywords: [{slug}, enterprise-advisory, quality-maturity]\n---\n\n"
        f"# {title}\n\n"
        f"**Scope:** {SPRINT} Enterprise Quality Advisory Platform — CQO / executive advisory posture. "
        f"Synthesize Sprints 1–9; never invent maturity scores, KPI %, or compliance attestations without evidence. "
        f"Mark regulations as overview / TBC with Legal-Compliance when not confirmed.\n\n"
        f"**Version:** {VERSION}\n\n---\n\n"
        + sec("purpose", "Purpose", purpose)
        + sec(
            "business_context",
            "Business Context",
            meta.get(
                "business_context",
                [
                    "Executives need decision-ready quality advice across portfolio, architecture, delivery, and operations—not raw test counts.",
                    "Enterprise advisory connects Salesforce delivery risk to business outcomes and investment choices.",
                ],
            ),
        )
        + sec(
            "assessment_criteria",
            "Assessment Criteria",
            meta.get(
                "assessment_criteria",
                [
                    "Evidence completeness (High/Medium/Low confidence)",
                    "Business criticality and blast radius",
                    "Maturity vs target state",
                    "Governance and compliance exposure",
                    "Effort vs value of recommended actions",
                ],
            ),
        )
        + sec(
            "inputs",
            "Inputs",
            meta.get(
                "inputs",
                [
                    "Project/portfolio evidence packs",
                    "Metrics from Sprint 7 QI / Sprint 9 ops (when provided)",
                    "Architecture and release notes",
                    "Stakeholder objectives and constraints",
                ],
            ),
        )
        + sec(
            "outputs",
            "Outputs",
            meta.get(
                "outputs",
                [
                    "Assessment scorecard or narrative",
                    "Traffic-light / maturity levels with rationale",
                    "Prioritized executive recommendations",
                    "Open questions and assumptions",
                ],
            ),
        )
        + sec(
            "evaluation_method",
            "Evaluation Method",
            meta.get(
                "evaluation_method",
                [
                    "Gather evidence; mark gaps TBC—do not invent scores",
                    "Score dimensions 1–5 or Red/Amber/Green with criteria",
                    "Synthesize overall status and confidence",
                    "Recommend actions via decision/recommendation engines",
                ],
            ),
        )
        + sec(
            "decision_framework",
            "Decision Framework",
            meta.get(
                "decision_framework",
                [
                    "Proceed / Hold / Escalate / Rollback (when release-related)",
                    "Invest / Defer / Divert (when portfolio-related)",
                    "Always state confidence and residual risk",
                ],
            ),
        )
        + sec(
            "examples",
            "Examples",
            meta.get(
                "examples",
                [
                    "Illustrative: Amber project health due to weak AC coverage + High release risk → Hold non-critical scope; expand regression",
                    "Replace with program evidence; never fabricate maturity indices",
                ],
            ),
        )
        + sec(
            "practices",
            "Best Practices",
            meta.get(
                "practices",
                [
                    "Lead with outcomes and residual risk for executives",
                    "Reuse Sprint 1–9 artifacts instead of re-deriving engines",
                    "Separate facts, assumptions, and recommendations",
                    "Prefer fewer high-impact actions over long laundry lists",
                ],
            ),
        )
        + sec(
            "anti_patterns",
            "Common Anti-Patterns",
            meta.get(
                "anti_patterns",
                [
                    "Greenwashing maturity without evidence",
                    "Inventing compliance certification status",
                    "Duplicating Sprint 7/8/9 deep dives instead of summarizing",
                    "Recommendations without owners or success measures",
                ],
            ),
        )
        + sec(
            "interview",
            "Interview Questions",
            meta.get(
                "interview",
                [
                    f"How would you advise a CIO using {title}?",
                    "How do TMMi / ISTQB / DORA concepts inform Salesforce quality advisory?",
                    "What evidence is mandatory before recommending Hold on a release?",
                ],
            ),
        )
        + "## Related Documents\n\n"
        + bullets(related)
        + "\n\n## Navigation\n\n"
        + f"- **Previous:** [{nav['prev_title']}]({nav['prev']})\n"
        + f"- **Next:** [{nav['next_title']}]({nav['next']})\n"
        + "- **See Also:** [../README.md](../README.md)\n\n"
        + "## Future Enhancements\n\n"
        + bullets(
            meta.get(
                "future",
                [
                    "Program score overlays under outputs/<project>/",
                    "Optional machine-readable scorecard export",
                ],
            )
        )
        + "\n"
    )


FOLDERS: dict[str, dict] = {
    "quality-maturity": {
        "title": "Quality Maturity",
        "purpose": "Assess and advance enterprise quality maturity for Salesforce programs.",
        "scope": "TMMi/ISTQB-aligned maturity, automation/DevOps maturity, CQE, transformation, roadmaps, gaps.",
        "inputs": ["Current practices evidence", "Metrics samples", "Target operating model"],
        "outputs": ["Maturity levels", "Gap assessment", "Improvement roadmap"],
        "docs": [
            ("quality-maturity-models", "Maturity model overview"),
            ("tmmi", "TMMi alignment"),
            ("istqb-maturity", "ISTQB maturity themes"),
            ("automation-maturity", "Automation maturity"),
            ("devops-maturity", "DevOps maturity"),
            ("testing-capability-assessment", "Testing capability"),
            ("quality-capability-assessment", "Quality capability"),
            ("continuous-quality-engineering", "CQE model"),
            ("quality-transformation", "Transformation approach"),
            ("quality-roadmap", "Quality roadmap"),
            ("gap-assessment", "Gap assessment"),
            ("target-state-definition", "Target state"),
            ("improvement-planning", "Improvement planning"),
        ],
    },
    "project-health": {
        "title": "Project Health",
        "purpose": "Score and narrate Salesforce project quality and delivery health for executives.",
        "scope": "Requirements through stakeholder risk, RAG status, executive summary, recommendations.",
        "inputs": ["Requirements/AC evidence", "Coverage/defect/release signals", "RAID"],
        "outputs": ["Health scorecard", "Traffic lights", "Executive summary"],
        "docs": [
            ("requirements-health", "Requirements health"),
            ("test-coverage-health", "Test coverage health"),
            ("automation-coverage-health", "Automation coverage health"),
            ("defect-health", "Defect health"),
            ("release-readiness-health", "Release readiness"),
            ("regression-readiness", "Regression readiness"),
            ("environment-health", "Environment health"),
            ("delivery-health", "Delivery health"),
            ("stakeholder-engagement", "Stakeholder engagement"),
            ("risk-exposure", "Risk exposure"),
            ("overall-project-health-score", "Overall health score"),
            ("traffic-light-indicators", "RAG indicators"),
            ("executive-summary", "Executive summary"),
            ("recommendations", "Project recommendations"),
        ],
    },
    "portfolio-management": {
        "title": "Portfolio Management",
        "purpose": "Govern quality across multi-project Salesforce portfolios.",
        "scope": "Cross-project metrics, heat maps, enterprise risk, strategic recommendations.",
        "inputs": ["Multi-project scorecards", "Release calendars", "Shared risks"],
        "outputs": ["Portfolio dashboard design", "Heat maps", "Strategic actions"],
        "docs": [
            ("multi-project-governance", "Multi-project governance"),
            ("portfolio-quality-dashboard", "Portfolio dashboard"),
            ("cross-project-metrics", "Cross-project metrics"),
            ("enterprise-risk-view", "Enterprise risk view"),
            ("release-portfolio", "Release portfolio"),
            ("quality-heat-maps", "Quality heat maps"),
            ("capability-comparison", "Capability comparison"),
            ("resource-utilization", "Resource utilization"),
            ("quality-trends", "Quality trends"),
            ("lessons-learned-repository", "Lessons learned repo"),
            ("strategic-recommendations", "Strategic recommendations"),
        ],
    },
    "delivery-governance": {
        "title": "Delivery Governance",
        "purpose": "Support quality governance forums, gates, and steering for Salesforce delivery.",
        "scope": "Gates, reviews, steering, audit readiness, decision records, KPIs.",
        "inputs": ["Gate evidence", "Review packs", "RAID/decisions"],
        "outputs": ["Governance advice", "Decision records", "Escalations"],
        "docs": [
            ("quality-gates", "Quality gates"),
            ("governance-reviews", "Governance reviews"),
            ("architecture-reviews", "Architecture reviews"),
            ("release-reviews", "Release reviews"),
            ("risk-reviews", "Risk reviews"),
            ("steering-committee-support", "Steering committee"),
            ("executive-reporting", "Exec reporting cadence"),
            ("audit-readiness", "Audit readiness"),
            ("compliance-tracking", "Compliance tracking"),
            ("decision-records", "Decision records"),
            ("governance-kpis", "Governance KPIs"),
        ],
    },
    "architecture-quality": {
        "title": "Architecture Quality",
        "purpose": "Advise on Salesforce solution and quality architecture fitness.",
        "scope": "SF/integration/security/automation/env/data architecture, debt, risks—not detailed tech design ownership.",
        "inputs": ["Architecture briefs", "Metadata complexity signals", "Debt notes"],
        "outputs": ["Architecture quality view", "Risks", "Recommendations"],
        "docs": [
            ("salesforce-architecture", "Salesforce architecture"),
            ("integration-architecture", "Integration architecture"),
            ("security-architecture", "Security architecture"),
            ("automation-architecture", "Automation architecture"),
            ("environment-architecture", "Environment architecture"),
            ("data-architecture", "Data architecture"),
            ("metadata-quality", "Metadata quality"),
            ("technical-debt", "Technical debt"),
            ("configuration-complexity", "Config complexity"),
            ("scalability", "Scalability"),
            ("maintainability", "Maintainability"),
            ("extensibility", "Extensibility"),
            ("architecture-risks", "Architecture risks"),
            ("recommendations", "Architecture recommendations"),
        ],
    },
    "ai-governance": {
        "title": "AI Governance",
        "purpose": "Govern responsible AI use in Salesforce quality engineering and delivery.",
        "scope": "Responsible AI, AI-assisted testing, prompt/model governance, privacy, oversight, adoption.",
        "inputs": ["AI use cases", "Data classes", "Human oversight model"],
        "outputs": ["AI risk assessment", "Gates", "Adoption guidance"],
        "docs": [
            ("responsible-ai", "Responsible AI"),
            ("ai-assisted-testing", "AI-assisted testing"),
            ("ai-risk-assessment", "AI risk assessment"),
            ("prompt-governance", "Prompt governance"),
            ("model-validation", "Model validation"),
            ("data-privacy", "Data privacy"),
            ("human-oversight", "Human oversight"),
            ("ethical-ai", "Ethical AI"),
            ("ai-metrics", "AI metrics"),
            ("ai-quality-gates", "AI quality gates"),
            ("ai-adoption-strategy", "AI adoption strategy"),
            ("ai-change-management", "AI change management"),
        ],
    },
    "compliance": {
        "title": "Compliance",
        "purpose": "Advise on compliance-aware quality without inventing regulatory requirements.",
        "scope": "GDPR/SOC2/ISO/PCI/HIPAA overview/WCAG awareness, audit evidence, reporting—confirm with Legal/Compliance.",
        "inputs": ["Applicable regulations (confirmed)", "Control evidence", "Test scope"],
        "outputs": ["Compliance risk notes", "Evidence checklist", "TBC items"],
        "docs": [
            ("gdpr", "GDPR awareness"),
            ("soc-2", "SOC 2 awareness"),
            ("iso-27001", "ISO 27001 awareness"),
            ("pci-dss", "PCI DSS awareness"),
            ("hipaa-overview", "HIPAA overview"),
            ("wcag", "WCAG / accessibility"),
            ("audit-readiness", "Audit readiness"),
            ("compliance-testing", "Compliance testing"),
            ("evidence-collection", "Evidence collection"),
            ("risk-assessment", "Compliance risk assessment"),
            ("compliance-reporting", "Compliance reporting"),
        ],
    },
    "quality-audits": {
        "title": "Quality Audits",
        "purpose": "Run structured quality audits with scorecards across the delivery lifecycle.",
        "scope": "Requirement through governance audits; scorecards; reuse Sprint 8 automation review where relevant.",
        "inputs": ["Artifact samples", "Process evidence", "Prior findings"],
        "outputs": ["Audit scorecards", "Findings", "Remediation"],
        "docs": [
            ("requirement-audit", "Requirement audit"),
            ("test-case-audit", "Test case audit"),
            ("automation-audit", "Automation audit"),
            ("release-audit", "Release audit"),
            ("environment-audit", "Environment audit"),
            ("security-audit", "Security audit"),
            ("production-audit", "Production audit"),
            ("defect-audit", "Defect audit"),
            ("documentation-audit", "Documentation audit"),
            ("governance-audit", "Governance audit"),
            ("audit-scorecards", "Audit scorecards"),
        ],
    },
    "executive-reporting": {
        "title": "Executive Reporting",
        "purpose": "Define audience-specific executive quality dashboards and actions.",
        "scope": "CIO through Steering Committee dashboards: KPIs, visuals, thresholds, escalations.",
        "inputs": ["KPI definitions", "Threshold policy", "Audience goals"],
        "outputs": ["Dashboard specs", "Escalation criteria"],
        "docs": [
            ("cio-dashboard", "CIO"),
            ("cto-dashboard", "CTO"),
            ("cqo-dashboard", "CQO"),
            ("program-director-dashboard", "Program Director"),
            ("delivery-director-dashboard", "Delivery Director"),
            ("release-director-dashboard", "Release Director"),
            ("qa-director-dashboard", "QA Director"),
            ("coe-dashboard", "Salesforce CoE"),
            ("arb-dashboard", "Architecture Review Board"),
            ("steering-committee-dashboard", "Executive Steering Committee"),
        ],
    },
    "decision-engine": {
        "title": "Enterprise Decision Engine",
        "purpose": "Recommend executive/delivery decisions with confidence and rationale.",
        "scope": "Proceed/Hold/Escalate/Rollback and related investment decisions.",
        "inputs": ["Health/maturity/risk evidence", "Release context"],
        "outputs": ["Decision + confidence", "Rationale", "Next actions"],
        "docs": [
            ("proceed", "Proceed"),
            ("hold", "Hold"),
            ("escalate", "Escalate"),
            ("rollback", "Rollback"),
            ("increase-automation", "Increase automation"),
            ("expand-regression", "Expand regression"),
            ("delay-release", "Delay release"),
            ("reduce-scope", "Reduce scope"),
            ("increase-testing", "Increase testing"),
            ("architecture-review", "Architecture review"),
            ("security-review", "Security review"),
            ("executive-review", "Executive review"),
            ("decision-confidence", "Confidence scoring"),
        ],
    },
    "recommendation-engine": {
        "title": "Strategic Recommendation Engine",
        "purpose": "Generate prioritized enterprise recommendations from multi-signal evidence.",
        "scope": "Quality/defect/automation/architecture/ops/compliance signals → ranked actions.",
        "inputs": ["Scorecards", "Trends", "Risks", "Constraints"],
        "outputs": ["Prioritized backlog", "Effort vs value view"],
        "docs": [
            ("recommendation-model", "Recommendation model"),
            ("prioritization", "Prioritization"),
            ("effort-vs-value", "Effort vs value"),
            ("dependency-aware-recommendations", "Dependency-aware"),
            ("executive-action-pack", "Executive action pack"),
        ],
    },
    "capability-model": {
        "title": "Capability Model",
        "purpose": "Assess quality capabilities with current/target levels and improvement actions.",
        "scope": "Requirement mgmt through AI adoption capabilities.",
        "inputs": ["Practice evidence", "Target operating model"],
        "outputs": ["Capability levels", "Improvement actions", "Success measures"],
        "docs": [
            ("requirement-management", "Requirement management"),
            ("test-design", "Test design"),
            ("functional-testing", "Functional testing"),
            ("automation", "Automation"),
            ("api-testing", "API testing"),
            ("performance-testing", "Performance testing"),
            ("security-testing", "Security testing"),
            ("release-management", "Release management"),
            ("production-support", "Production support"),
            ("governance", "Governance"),
            ("ai-adoption", "AI adoption"),
            ("capability-assessment-method", "Assessment method"),
        ],
    },
    "benchmarking": {
        "title": "Benchmarking",
        "purpose": "Provide anonymized, generic benchmarking guidance for quality comparison.",
        "scope": "Projects/teams/BUs/industries; DORA-aligned concepts; no org-specific invented numbers.",
        "inputs": ["Comparable peer class", "KPI definitions"],
        "outputs": ["Benchmark framing", "Relative position narrative"],
        "docs": [
            ("project-benchmarking", "Projects"),
            ("team-benchmarking", "Teams"),
            ("business-unit-benchmarking", "Business units"),
            ("industry-benchmarking", "Industries"),
            ("release-performance", "Release performance"),
            ("automation-maturity-benchmarks", "Automation maturity"),
            ("quality-kpi-benchmarks", "Quality KPIs"),
            ("support-kpi-benchmarks", "Support KPIs"),
            ("governance-benchmarks", "Governance"),
            ("dora-concepts", "DORA concepts"),
        ],
    },
    "roadmaps": {
        "title": "Roadmaps",
        "purpose": "Templates and guidance for quality transformation and automation roadmaps.",
        "scope": "90-day through CoE/AI/ops/testing strategy roadmaps.",
        "inputs": ["Current state", "Target state", "Constraints"],
        "outputs": ["Phased roadmap", "Milestones", "Success measures"],
        "docs": [
            ("90-day-improvement-plan", "90-day plan"),
            ("6-month-quality-transformation", "6-month transformation"),
            ("12-month-automation-roadmap", "12-month automation"),
            ("quality-coe-roadmap", "Quality CoE roadmap"),
            ("ai-adoption-roadmap", "AI adoption roadmap"),
            ("operational-excellence-roadmap", "Ops excellence roadmap"),
            ("enterprise-testing-strategy-roadmap", "Enterprise testing strategy"),
        ],
    },
}

SF_DOCS = [
    ("sales-cloud", "Sales Cloud advisory"),
    ("service-cloud", "Service Cloud advisory"),
    ("experience-cloud", "Experience Cloud advisory"),
    ("revenue-cloud", "Revenue Cloud advisory"),
    ("field-service", "Field Service advisory"),
    ("marketing-cloud", "Marketing Cloud advisory"),
    ("data-cloud", "Data Cloud advisory"),
    ("agentforce", "Agentforce advisory"),
    ("omnistudio", "OmniStudio advisory"),
    ("industries-cloud", "Industries Cloud advisory"),
    ("managed-packages", "Managed packages"),
    ("enterprise-integrations", "Enterprise integrations"),
    ("devops-pipelines", "DevOps pipelines"),
    ("production-stability", "Production stability"),
    ("cross-cloud-implementations", "Cross-cloud implementations"),
]


def root_readme() -> str:
    rows = "\n".join(
        f"| [{cfg['title']}]({folder}/README.md) | {cfg['purpose']} |"
        for folder, cfg in FOLDERS.items()
    )
    return f"""---
title: Enterprise Quality — README
module: Salesforce Quality Engineering
version: {VERSION}
tags: [enterprise-quality, sprint-10]
---

# Enterprise Quality Advisory & Continuous Quality Engineering Platform

## Purpose

Enable the AI to act as an **Enterprise Quality Advisor / CQO**: assess project and portfolio health, maturity, architecture, AI/compliance posture, and recommend executive actions across the Salesforce lifecycle.

## Scope (Sprint 10)

**In scope:** Quality maturity, project/portfolio health, delivery governance, architecture quality, AI governance, compliance awareness, audits, executive dashboards, decision/recommendation engines, capability model, benchmarking, roadmaps, Salesforce enterprise advisory.

**Out of scope:** Inventing maturity scores, KPI %, compliance certifications, or regulatory requirements; replacing Sprints 1–9 engines (synthesize them).

## Engine entry

- [enterprise-quality-advisory-engine.md](enterprise-quality-advisory-engine.md)

## Folders

| Folder | Focus |
|--------|-------|
{rows}
| [salesforce/](salesforce/README.md) | Salesforce enterprise advisory by cloud/capability |

## Governance coverage

Quality gates · ARB · Steering · Audit readiness · Compliance tracking · AI gates

## Assessment engines

Project Health · Quality/Automation/DevOps Maturity · Architecture Quality · Capability Model · Audits · Decision + Recommendation Engines

## Navigation

- **Previous:** [../production-support/README.md](../production-support/README.md)
- **Next:** [enterprise-quality-advisory-engine.md](enterprise-quality-advisory-engine.md)
- **See Also:** [../skill.md](../skill.md)

## Related Documents

{bullets(CROSS_ROOT)}
"""


def engine_md() -> str:
    return f"""---
title: Enterprise Quality Advisory Engine
version: {VERSION}
tags: [enterprise-quality, sprint-10]
---

# Enterprise Quality Advisory Engine

## Purpose

Synthesize Sprints 1–9 into executive-grade assessments and decisions for Salesforce programs and portfolios.

## Process

```
Ingest evidence (project / portfolio / architecture / ops / AI / compliance)
    ↓
Assess maturity + project/portfolio health
    ↓
Architecture / AI / compliance / audit lenses
    ↓
Capability model + benchmarks (generic)
    ↓
Decision engine (Proceed/Hold/Escalate/…)
    ↓
Recommendation engine (prioritized)
    ↓
Executive dashboards / roadmaps
```

## Hard rules

1. **Never invent** maturity scores, KPI %, DORA numbers, or compliance attestations.  
2. Regulations = overview / TBC with Legal-Compliance unless cited.  
3. Reuse Sprint 7 QI, Sprint 8 automation review, Sprint 9 ops intelligence—do not duplicate.  
4. Always state confidence and residual risk.  
5. Align with ISTQB ATM, TMMi, Well-Architected, ITIL 4, DORA concepts, TOGAF governance themes, Responsible AI.  

## Capabilities

| Capability | Path |
|------------|------|
| Enterprise Advisory | [README.md](README.md) |
| Executive Decision Support | [decision-engine/](decision-engine/README.md) |
| Quality Maturity Assessment | [quality-maturity/](quality-maturity/README.md) |
| Portfolio Intelligence | [portfolio-management/](portfolio-management/README.md) |
| Architecture Quality Assessment | [architecture-quality/](architecture-quality/README.md) |
| AI Governance | [ai-governance/](ai-governance/README.md) |
| Compliance Awareness | [compliance/](compliance/README.md) |
| Capability Assessment | [capability-model/](capability-model/README.md) |
| Strategic Recommendation Engine | [recommendation-engine/](recommendation-engine/README.md) |

## Related

{bullets(CROSS_ROOT)}
"""


def main() -> None:
    EQ.mkdir(parents=True, exist_ok=True)
    (EQ / "README.md").write_text(root_readme(), encoding="utf-8")
    (EQ / "enterprise-quality-advisory-engine.md").write_text(engine_md(), encoding="utf-8")

    folder_order = list(FOLDERS.keys())
    for i, folder in enumerate(folder_order):
        cfg = FOLDERS[folder]
        path = EQ / folder
        path.mkdir(parents=True, exist_ok=True)
        docs = list(cfg["docs"])
        prev = f"../{folder_order[i-1]}/README.md" if i > 0 else "../README.md"
        nxt = (
            f"../{folder_order[i+1]}/README.md"
            if i < len(folder_order) - 1
            else "../salesforce/README.md"
        )
        (path / "README.md").write_text(
            folder_readme(
                folder,
                cfg["title"],
                cfg["purpose"],
                cfg["scope"],
                cfg["inputs"],
                cfg["outputs"],
                docs,
                prev,
                nxt,
            ),
            encoding="utf-8",
        )
        for j, (slug, _b) in enumerate(docs):
            meta: dict = {}
            if folder == "compliance":
                meta["assessment_criteria"] = [
                    "Confirmed applicability with Legal/Compliance",
                    "Evidence of controls and test coverage",
                    "Residual risk and TBC items explicit",
                ]
                meta["anti_patterns"] = [
                    "Claiming certified compliance without evidence",
                    "Inventing regulatory requirements",
                ]
            if folder == "decision-engine" and slug != "decision-confidence":
                meta["purpose"] = f"When and how to recommend the executive decision: {titleize(slug)}."
                meta["decision_framework"] = [
                    f"Trigger criteria for {titleize(slug)}",
                    "Required evidence and confidence",
                    "Communication and escalation path",
                ]
            if folder == "executive-reporting":
                meta["outputs"] = [
                    "Audience",
                    "KPIs (definitions only—values from data)",
                    "Visualization ideas",
                    "Thresholds (program-set)",
                    "Actions",
                    "Escalation criteria",
                ]
            if folder == "capability-model" and slug != "capability-assessment-method":
                meta["outputs"] = [
                    "Current level (evidence-based)",
                    "Target level",
                    "Assessment criteria",
                    "Improvement actions",
                    "Success measures",
                ]
            prev_s = docs[j - 1][0] + ".md" if j > 0 else "README.md"
            next_s = docs[j + 1][0] + ".md" if j < len(docs) - 1 else "README.md"
            (path / f"{slug}.md").write_text(
                article(
                    folder,
                    slug,
                    meta,
                    {
                        "prev": prev_s,
                        "next": next_s,
                        "prev_title": titleize(docs[j - 1][0]) if j > 0 else "README",
                        "next_title": titleize(docs[j + 1][0]) if j < len(docs) - 1 else "README",
                    },
                ),
                encoding="utf-8",
            )

    sf = EQ / "salesforce"
    sf.mkdir(parents=True, exist_ok=True)
    (sf / "README.md").write_text(
        folder_readme(
            "salesforce",
            "Salesforce Enterprise Advisory",
            "Evaluate Salesforce clouds and enterprise capabilities from a quality advisory lens.",
            "Cloud/capability quality risks and recommendations—load 4B articles; do not invent product features.",
            ["Cloud context", "Release/ops evidence", "Architecture notes"],
            ["Advisory findings", "Risks", "Recommendations"],
            SF_DOCS,
            "../roadmaps/README.md",
            "../README.md",
        ),
        encoding="utf-8",
    )
    for j, (slug, _b) in enumerate(SF_DOCS):
        meta = {
            "purpose": f"Advise executives on quality risks and readiness for Salesforce {titleize(slug)}.",
            "related": [
                "[4B Clouds](../../knowledge/clouds/README.md)",
                "[Architecture Quality](../architecture-quality/README.md)",
            ],
        }
        prev_s = SF_DOCS[j - 1][0] + ".md" if j > 0 else "README.md"
        next_s = SF_DOCS[j + 1][0] + ".md" if j < len(SF_DOCS) - 1 else "README.md"
        (sf / f"{slug}.md").write_text(
            article(
                "salesforce",
                slug,
                meta,
                {
                    "prev": prev_s,
                    "next": next_s,
                    "prev_title": titleize(SF_DOCS[j - 1][0]) if j > 0 else "README",
                    "next_title": titleize(SF_DOCS[j + 1][0]) if j < len(SF_DOCS) - 1 else "README",
                },
            ),
            encoding="utf-8",
        )

    count = sum(1 for _ in EQ.rglob("*.md"))
    print(f"Wrote ~{count} files under {EQ}")


if __name__ == "__main__":
    main()
