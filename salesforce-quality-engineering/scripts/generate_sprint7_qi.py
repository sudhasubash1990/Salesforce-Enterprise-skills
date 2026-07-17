#!/usr/bin/env python3
"""Generate Sprint 7 — Defect Intelligence & Quality Analytics Engine."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QI = ROOT / "quality-intelligence"
VERSION = "0.9.0"
DATE = "2026-07-17"
SPRINT = "Sprint 7"


def cross(prefix: str) -> list[str]:
    return [
        f"[QE Brain (Sprint 1)]({prefix}/brain/README.md)",
        f"[Requirement Analysis (Sprint 2)]({prefix}/knowledge/requirement-analysis.md)",
        f"[Test Design Engine (Sprint 3)]({prefix}/knowledge/test-design-engine.md)",
        f"[Platform Foundation 4A]({prefix}/knowledge/platform/README.md)",
        f"[Enterprise Knowledge 4B]({prefix}/knowledge/clouds/README.md)",
        f"[Documentation Generator (Sprint 5)]({prefix}/templates/README.md)",
        f"[ADO Delivery Intelligence (Sprint 6)]({prefix}/ado/README.md)",
        f"[Defect Report Template]({prefix}/templates/defect-report.md)",
        f"[Defect RCA Template]({prefix}/templates/defect-rca-report.md)",
    ]


CROSS = cross("../..")
CROSS_ROOT = cross("..")


def titleize(slug: str) -> str:
    special = {
        "5-whys": "5 Whys",
        "fmea": "FMEA",
        "dre": "Defect Removal Efficiency (DRE)",
        "mttd": "MTTD",
        "mttr": "MTTR",
        "capa": "Corrective Actions (CAPA)",
        "ui-defects": "UI Defects",
        "fishbone-diagram": "Fishbone Diagram",
        "pareto-analysis": "Pareto Analysis",
        "fault-tree-analysis": "Fault Tree Analysis",
        "salesforce-quality-intelligence": "Salesforce Quality Intelligence",
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
category: Quality Intelligence
document_type: Guide
version: {VERSION}
review_status: Draft
owner: QE Practice Lead
created_date: {DATE}
last_updated: {DATE}
tags: [quality-intelligence, sprint-7, {folder}]
---

# {title}

## Purpose

{purpose}

## Scope

{scope}

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
    purpose = meta["purpose"]
    related = meta.get("related", []) + CROSS + [
        "[README.md](README.md)",
        "[../README.md](../README.md)",
    ]

    def sec(key: str, heading: str, default: list[str] | str) -> str:
        val = meta.get(key, default)
        body = val if isinstance(val, str) else bullets(val)
        return f"## {heading}\n\n{body}\n"

    parts = [
        f"---\ntitle: {title}\nmodule: Salesforce Quality Engineering\n"
        f"category: Quality Intelligence\ndocument_type: Knowledge Article\n"
        f"version: {VERSION}\nreview_status: Draft\nowner: QE Practice Lead\n"
        f"created_date: {DATE}\nlast_updated: {DATE}\n"
        f"tags: [quality-intelligence, sprint-7, {folder}]\n"
        f"keywords: [{slug}, defect-intelligence, quality-analytics]\n---\n\n"
        f"# {title}\n\n"
        f"**Scope:** {SPRINT} Defect Intelligence & Quality Analytics — prevention-first QE advisor. "
        f"Reuse Sprint 5/6 defect templates and ADO bug guidance; do not invent metrics without data.\n\n"
        f"**Version:** {VERSION}\n\n---\n\n",
        sec("purpose", "Purpose", purpose),
        sec(
            "business_context",
            "Business Context",
            [
                "Defects consume cost at every escape stage—prevention beats late detection.",
                "Enterprise governance needs comparable classification, RCA, and trend signals.",
            ],
        ),
        sec(
            "overview",
            "Overview",
            meta.get(
                "overview",
                [
                    f"{title} supports data-driven quality decisions across Salesforce delivery.",
                    "Align with ISTQB Advanced Test Management and TMMi improvement themes.",
                ],
            ),
        ),
        sec(
            "inputs",
            "Inputs",
            meta.get(
                "inputs",
                [
                    "Defect records / bug work items",
                    "Requirement and test evidence",
                    "Environment and release context",
                ],
            ),
        ),
        sec(
            "outputs",
            "Outputs",
            meta.get(
                "outputs",
                [
                    "Classifications, scores, or analysis narrative",
                    "Preventive / corrective recommendations",
                ],
            ),
        ),
        sec(
            "process",
            "Process",
            meta.get(
                "process",
                [
                    "Gather evidence (do not invent counts)",
                    "Classify and analyse",
                    "Recommend actions with owners",
                    "Feed continuous improvement and predictive risk",
                ],
            ),
        ),
        sec(
            "examples",
            "Examples",
            meta.get(
                "examples",
                [
                    "Illustrative only — replace with program data",
                    "Always state data period and source system (ADO/Jira/etc.)",
                ],
            ),
        ),
        sec(
            "practices",
            "Best Practices",
            meta.get(
                "practices",
                [
                    "Separate Severity (impact) from Priority (urgency)",
                    "Link defects to Story/Case IDs",
                    "Prefer prevention actions over retest-only closures",
                ],
            ),
        ),
        sec(
            "mistakes",
            "Common Mistakes",
            meta.get(
                "mistakes",
                [
                    "Inventing coverage or leakage percentages",
                    "RCA that stops at 'developer error' without process cause",
                    "Ignoring environment/config as first-class causes",
                ],
            ),
        ),
        sec(
            "interview",
            "Interview Questions",
            [
                f"How would you apply {title} on a Salesforce release?",
                "What data is required before drawing conclusions?",
                "How does this reduce defect leakage?",
            ],
        ),
        "## Related Documents\n\n" + bullets(related) + "\n\n",
        "## Navigation\n\n"
        f"- **Previous:** [{nav['prev_label']}]({nav['prev']})\n"
        f"- **Next:** [{nav['next_label']}]({nav['next']})\n"
        "- **See Also:** [README.md](README.md)\n\n",
        "## Future Enhancements\n\n"
        "- Deeper Salesforce component pattern catalogs\n"
        "- Optional metric calculators with validated inputs\n",
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


def metric_meta(name: str, definition: str, formula: str) -> dict:
    return {
        "purpose": f"Define and interpret {name} for Salesforce QE governance.",
        "overview": [definition, f"**Formula (conceptual):** {formula}"],
        "process": [
            "Confirm data source and period",
            "Compute only with available counts—never invent",
            "Compare to agreed thresholds; explain drivers",
            "Recommend actions (test, process, automation, env)",
        ],
        "practices": [
            "Publish definition beside the number",
            "Pair with trend, not a single sprint snapshot",
            "Visualization: trend line + threshold band",
        ],
        "examples": [
            f"Interpretation guidance for {name} must cite numerator/denominator sources",
            "Thresholds are program-specific—propose bands, do not assert universal SLAs",
        ],
    }


FOLDERS: dict[str, dict] = {
    "defect-management": {
        "title": "Defect Management",
        "purpose": "Enterprise defect lifecycle, classification, and handling from a QE prevention lens.",
        "scope": "Lifecycle, severity/priority, defect types across functional→production. Cross-link Sprint 5/6 templates.",
        "inputs": ["Bug/defect records", "Environment/build", "Linked stories/cases"],
        "outputs": ["Classified defects", "Workflow recommendations", "Impact statements"],
        "docs": [
            ("defect-lifecycle", "States from discovery to closure", {"purpose": "Define defect lifecycle stages and QE evidence at each state."}),
            ("defect-workflow", "Roles, states, and handoffs", {"purpose": "Describe triage→fix→retest→close workflow and ownership.", "related": ["[../../ado/governance/bug-workflow.md](../../ado/governance/bug-workflow.md)"]}),
            ("severity", "Impact-based severity", {"purpose": "Classify defect severity by business/technical impact—not urgency."}),
            ("priority", "Urgency of fix", {"purpose": "Set fix priority relative to release risk and severity."}),
            ("defect-classification", "Taxonomy overview", {"purpose": "Provide a consistent taxonomy for analytics and pattern detection."}),
            ("functional-defects", "Behaviour vs AC", {"purpose": "Defects where functional outcomes violate acceptance criteria."}),
            ("ui-defects", "Presentation/UX", {"purpose": "Layout, Lightning page, and usability defects—separate from functional failure when possible."}),
            ("integration-defects", "Interface failures", {"purpose": "API/event/middleware defects and contract mismatches."}),
            ("data-defects", "Data integrity/quality", {"purpose": "Incorrect, missing, duplicated, or migrated data defects."}),
            ("security-defects", "Access/visibility", {"purpose": "CRUD/FLS/sharing/auth defects with high audit impact."}),
            ("performance-defects", "Speed/limits", {"purpose": "Timeouts, governor-limit failures, LDV symptoms."}),
            ("regression-defects", "Broken prior behaviour", {"purpose": "Defects introduced or reopened by change—feed regression packs."}),
            ("automation-defects", "Script/framework issues", {"purpose": "Distinguish product bugs from automation false failures."}),
            ("environment-defects", "Env/config drift", {"purpose": "Failures caused by env readiness, credentials, or refresh issues."}),
            ("configuration-defects", "Metadata misconfig", {"purpose": "Wrong VR/Flow/layout/permission configuration outcomes."}),
            ("deployment-defects", "Deploy/package issues", {"purpose": "Post-deploy failures from omitted metadata or order issues."}),
            ("production-defects", "Escaped defects", {"purpose": "Production escapes—mandatory RCA and leakage metrics."}),
        ],
    },
    "root-cause-analysis": {
        "title": "Root Cause Analysis",
        "purpose": "RCA methods and cause categories for escaped and Critical defects.",
        "scope": "5 Whys, Fishbone, Pareto, FTA, FMEA, and Salesforce-relevant cause classes.",
        "inputs": ["Defect evidence", "Timeline", "Process context"],
        "outputs": ["RCA narrative", "Corrective/preventive actions", "Lessons learned inputs"],
        "docs": [
            ("5-whys", "Iterative cause drilling", {"purpose": "Use 5 Whys for focused incident RCA.", "overview": ["Ask why until process/system cause emerges", "Stop at actionable control, not blame"], "process": ["State problem", "Ask why with evidence", "Document chain", "Define CAPA"]}),
            ("fishbone-diagram", "Cause-and-effect", {"purpose": "Structure causes across people/process/tech/data/env categories."}),
            ("pareto-analysis", "Vital few defects", {"purpose": "Focus improvement on the few causes driving most defects."}),
            ("fault-tree-analysis", "Top-down failure logic", {"purpose": "Model how combinations of faults produce a top event."}),
            ("fmea", "FMEA for quality risk", {"purpose": "Anticipate failure modes, effects, and detection controls before release."}),
            ("defect-categorization", "Cause coding", {"purpose": "Standardize RCA categories for analytics."}),
            ("process-failures", "Process as root cause", {"purpose": "Missing reviews, unclear DoD, weak triage."}),
            ("requirement-issues", "Req/AC gaps", {"purpose": "Ambiguous or incomplete requirements causing defects."}),
            ("design-issues", "Solution design gaps", {"purpose": "Incorrect fit-gap or component design choices."}),
            ("development-issues", "Build defects", {"purpose": "Code/config implementation errors."}),
            ("configuration-issues", "Config mistakes", {"purpose": "Metadata misconfiguration root causes."}),
            ("environment-issues", "Env root causes", {"purpose": "Env parity, data, and credential issues."}),
            ("test-data-issues", "Data root causes", {"purpose": "Invalid/masked/incomplete test data causing escapes or noise."}),
            ("integration-issues", "Interface root causes", {"purpose": "Contract, auth, and retry design failures."}),
            ("deployment-issues", "Release root causes", {"purpose": "Deploy omission, sequence, or package upgrade causes."}),
            ("production-issues", "Prod-only causes", {"purpose": "Volume, data, permission drift unique to production."}),
        ],
    },
    "defect-patterns": {
        "title": "Defect Pattern Recognition",
        "purpose": "Detect recurring patterns, hotspots, and leakage signals with confidence and prevention actions.",
        "scope": "Pattern types, detection rules, confidence scoring, preventive actions.",
        "inputs": ["Historical defects", "Component tags", "Release timeline"],
        "outputs": ["Pattern list", "Confidence", "Preventive actions"],
        "docs": [
            ("recurring-defects", "Same failure repeats", {"purpose": "Identify defects that recur across sprints/releases."}),
            ("duplicate-defects", "Same issue logged multiple times", {"purpose": "Detect duplicates to clean analytics and triage."}),
            ("regression-patterns", "Change-induced repeats", {"purpose": "Spot modules that break when adjacent features change."}),
            ("module-hotspots", "Hot component areas", {"purpose": "Rank Salesforce modules/objects with elevated defect density."}),
            ("high-risk-components", "Risk-ranked components", {"purpose": "Combine defect history + change frequency + business criticality."}),
            ("requirement-gaps", "Pattern of AC gaps", {"purpose": "Recurring misses from incomplete requirements/AC."}),
            ("environment-failures", "Env failure clusters", {"purpose": "Cluster failures by environment symptoms."}),
            ("integration-failures", "Interface failure clusters", {"purpose": "Recurring API/event/middleware failure patterns."}),
            ("security-weaknesses", "Access defect patterns", {"purpose": "Recurring FLS/sharing/persona failures."}),
            ("automation-instability", "Flaky automation patterns", {"purpose": "Separate product risk from unstable automation."}),
            ("production-leakage", "Escape patterns", {"purpose": "Where and why defects leak to production."}),
            ("business-rule-violations", "Rule breach patterns", {"purpose": "Repeated business-rule/validation failures."}),
            ("pattern-detection-rules", "Detection rule catalog", {"purpose": "Rules the AI should apply to claim a pattern (min samples, window, similarity)."}),
            ("confidence-score", "Pattern confidence", {"purpose": "Score Low/Medium/High confidence based on sample size and consistency—never fake precision."}),
            ("suggested-preventive-actions", "Prevention catalog", {"purpose": "Map patterns to preventive actions (reviews, tests, automation, gates)."}),
        ],
    },
    "quality-metrics": {
        "title": "Quality Metrics",
        "purpose": "Definitions, formulas, interpretation, and actions for enterprise QA metrics.",
        "scope": "Density, leakage, DRE, coverage, execution, automation, reopen, MTTD/MTTR, indices. No invented values.",
        "inputs": ["Counts from ADO/test tools", "Period definition"],
        "outputs": ["Metric interpretations", "Threshold proposals", "Actions"],
        "docs": [
            ("defect-density", "Defects per size unit", metric_meta("Defect Density", "Defects found relative to size (stories/FP/LOC proxy).", "Defects / Size unit")),
            ("defect-leakage", "Escapes to later phase", metric_meta("Defect Leakage", "Share of defects found in later phases (e.g., prod) vs earlier.", "Phase_n defects / Total defects (define phases)")),
            ("defect-removal-efficiency", "DRE", metric_meta("DRE", "Effectiveness of removing defects before a phase.", "Defects removed before phase / (removed + escaped)")),
            ("requirement-coverage", "Req↔test mapping", metric_meta("Requirement Coverage", "Requirements with linked scenarios/cases.", "Covered reqs / Total in-scope reqs")),
            ("test-coverage", "Designed coverage", metric_meta("Test Coverage", "Scope covered by scenarios/cases (qualitative+linked)—not code % unless measured.", "Linked coverage items / In-scope items")),
            ("execution-progress", "Run progress", metric_meta("Execution Progress", "Executed vs planned cases.", "Executed / Planned")),
            ("pass-rate", "Pass ratio", metric_meta("Pass Rate", "Passed executions / executed.", "Passed / Executed")),
            ("fail-rate", "Fail ratio", metric_meta("Fail Rate", "Failed executions / executed.", "Failed / Executed")),
            ("automation-coverage", "Automated share", metric_meta("Automation Coverage", "Automated cases / automatable candidates (define set).", "Automated / Candidates")),
            ("automation-stability", "Flake rate inverse", metric_meta("Automation Stability", "Stable runs vs flaky failures.", "1 - (Flaky failures / Automation runs)")),
            ("escaped-defects", "Prod/UAT escapes", metric_meta("Escaped Defects", "Count of defects found after exit of intended phase.", "Count of escaped defects (by definition)")),
            ("reopen-rate", "Reopened bugs", metric_meta("Reopen Rate", "Reopened / Closed in period.", "Reopened / Closed")),
            ("mttd", "Mean time to detect", metric_meta("MTTD", "Average time from introduce/deploy to detect.", "Sum(detect - introduce) / n")),
            ("mttr", "Mean time to resolve", metric_meta("MTTR", "Average time from detect to resolve/verify.", "Sum(resolve - detect) / n")),
            ("regression-effectiveness", "Reg pack value", metric_meta("Regression Effectiveness", "Regressions caught by pack vs missed.", "Caught by regression / (Caught + Missed)")),
            ("requirement-volatility", "Churn", metric_meta("Requirement Volatility", "Change rate of requirements in a window.", "Changed reqs / Total reqs")),
            ("sprint-quality-index", "Sprint composite", metric_meta("Sprint Quality Index", "Composite of pass rate, Critical opens, leakage signals (define weights).", "Weighted score (document weights)")),
            ("release-quality-index", "Release composite", metric_meta("Release Quality Index", "Composite readiness/quality score for release.", "Weighted score (document weights)")),
            ("production-stability-index", "Prod stability", metric_meta("Production Stability Index", "Post-go-live incident/defect stability signal.", "Weighted score (document weights)")),
        ],
    },
    "risk-analysis": {
        "title": "Risk Analysis",
        "purpose": "Identify, score, mitigate, monitor, and escalate quality risks.",
        "scope": "Business through dependency risks; scoring and escalation model.",
        "inputs": ["RAID", "Change impact", "Defect/trend signals"],
        "outputs": ["Risk scores", "Mitigations", "Escalations"],
        "docs": [
            ("business-risk", "Outcome/customer risk", {"purpose": "Assess risk to business outcomes and customer journeys."}),
            ("technical-risk", "Solution/tech risk", {"purpose": "Assess platform/customization technical risk."}),
            ("integration-risk", "Interface risk", {"purpose": "Score integration failure and contract risk."}),
            ("data-risk", "Data quality/migration risk", {"purpose": "Score data integrity and migration risk."}),
            ("security-risk", "Access/compliance exposure", {"purpose": "Score security defect and oversharing risk."}),
            ("release-risk", "Go-live risk", {"purpose": "Score release readiness and cutover risk."}),
            ("automation-risk", "Automation program risk", {"purpose": "Score false confidence from unstable automation."}),
            ("regression-risk", "Regressive change risk", {"purpose": "Score likelihood of breaking prior behaviour."}),
            ("performance-risk", "Perf/LDV risk", {"purpose": "Score governor/LDV/concurrency risk."}),
            ("compliance-risk", "Regulatory risk", {"purpose": "Flag compliance risk—confirm with Legal; do not invent regulations."}),
            ("environment-risk", "Env readiness risk", {"purpose": "Score env/data/credential readiness risk."}),
            ("dependency-risk", "External dependency risk", {"purpose": "Score vendor/package/team dependency risk."}),
            ("risk-scoring-model", "Score & prioritize", {"purpose": "Probability × Impact model with monitoring and escalation thresholds."}),
        ],
    },
    "trend-analysis": {
        "title": "Trend Analysis",
        "purpose": "Analyse quality trends across sprints, releases, defects, automation, and production.",
        "scope": "Trend types, visualization, executive interpretation, improvements.",
        "inputs": ["Time-series metrics", "Defect logs"],
        "outputs": ["Trend narratives", "Executive insights", "Improvement actions"],
        "docs": [
            ("sprint-trends", "Sprint-over-sprint", {"purpose": "Interpret quality movement across sprints."}),
            ("release-trends", "Release-over-release", {"purpose": "Compare quality signals across releases."}),
            ("defect-trends", "Defect volume/severity trends", {"purpose": "Track open/closed/severity mix over time."}),
            ("requirement-trends", "Volatility & quality", {"purpose": "Correlate requirement churn with defect injection."}),
            ("regression-trends", "Regression find rate", {"purpose": "Track regression effectiveness and hotspot shifts."}),
            ("automation-trends", "Automation health", {"purpose": "Track coverage vs stability over time."}),
            ("environment-trends", "Env-caused noise", {"purpose": "Track environment-attributed failures over time."}),
            ("production-trends", "Prod incident/defect trends", {"purpose": "Track post-release stability signals."}),
            ("velocity-trends", "Delivery vs quality", {"purpose": "Relate delivery velocity to quality risk (avoid gaming)."}),
            ("quality-trends", "Composite quality", {"purpose": "Roll up indices into an executive quality trend."}),
            ("visualization-guidance", "Charts that help decisions", {"purpose": "Recommend chart types and anti-patterns for exec reporting."}),
            ("executive-reporting", "How to narrate trends", {"purpose": "Executive-ready trend interpretation rules."}),
        ],
    },
    "predictive-quality": {
        "title": "Predictive Quality",
        "purpose": "Predict high-risk stories/components, leakage, and readiness risks with confidence and mitigations.",
        "scope": "Predictions are advisory; require stated confidence and evidence—never claim certainty.",
        "inputs": ["History", "Change impact", "Complexity signals"],
        "outputs": ["Risk predictions", "Confidence", "Mitigation plans"],
        "docs": [
            ("high-risk-user-stories", "Story risk prediction", {"purpose": "Flag stories likely to inject defects (complexity, volatility, integration, security)."}),
            ("high-risk-components", "Component risk prediction", {"purpose": "Predict Salesforce components likely to fail based on history + change."}),
            ("likely-regression-areas", "Regression targeting", {"purpose": "Predict neighbor areas needing regression."}),
            ("likely-production-failures", "Prod failure likelihood", {"purpose": "Predict failure modes under prod volume/permissions."}),
            ("automation-candidates", "What to automate next", {"purpose": "Predict strong automation ROI candidates from stability/frequency."}),
            ("likely-defect-leakage", "Leakage prediction", {"purpose": "Predict where escapes are likely given weak coverage/gates."}),
            ("release-readiness-risks", "Go/No-Go risk prediction", {"purpose": "Predict readiness risk themes for release decisions."}),
            ("quality-gate-failures", "Gate failure prediction", {"purpose": "Predict which entry/exit gates are at risk of failing."}),
            ("confidence-levels", "Prediction confidence", {"purpose": "Express Low/Medium/High confidence with rationale—no false precision."}),
            ("mitigation-plans", "Mitigation playbook", {"purpose": "Recommend mitigations tied to each prediction class."}),
        ],
    },
    "continuous-improvement": {
        "title": "Continuous Improvement",
        "purpose": "Turn RCA and metrics into lasting process, automation, and governance improvements.",
        "scope": "Retros, lessons learned, QIP, CAPA, training, TPI, automation/governance improvements.",
        "inputs": ["RCA", "Metrics", "Retro notes"],
        "outputs": ["Improvement backlog", "CAPA", "Training asks"],
        "docs": [
            ("retrospectives", "Quality-focused retros", {"purpose": "Run retros that produce measurable quality actions."}),
            ("lessons-learned", "Capture & reuse lessons", {"purpose": "Structure lessons for reuse across releases.", "related": ["[../../templates/lessons-learned.md](../../templates/lessons-learned.md)"]}),
            ("quality-improvement-plans", "QIP", {"purpose": "Plan multi-sprint quality improvements with owners/dates."}),
            ("preventive-actions", "Prevent recurrence", {"purpose": "Define preventive controls (reviews, tests, gates)."}),
            ("capa", "Corrective actions", {"purpose": "CAPA structure for Critical escapes and audit needs."}),
            ("knowledge-sharing", "Share findings", {"purpose": "Communities of practice and defect learning loops."}),
            ("training-recommendations", "Upskill signals", {"purpose": "Recommend training from pattern clusters (Flow, security, etc.)."}),
            ("test-process-improvement", "TPI", {"purpose": "Improve analysis→design→execution→reporting process."}),
            ("automation-improvement", "Stabilize & expand", {"purpose": "Improve automation ROI and reduce flake."}),
            ("governance-improvements", "Gate & policy improvements", {"purpose": "Tighten DoR/DoD and quality gates based on evidence."}),
        ],
    },
    "quality-gates": {
        "title": "Quality Gates (Intelligence)",
        "purpose": "Intelligence for when gates should fail/warn based on defect and metric signals.",
        "scope": "Complements Sprint 5 checklists and ado/governance—focus on decision logic.",
        "inputs": ["Open defects", "Metrics", "Readiness checklists"],
        "outputs": ["Gate pass/warn/fail recommendations"],
        "docs": [
            ("gate-decision-logic", "Pass / warn / fail rules", {"purpose": "Define evidence-based gate decisions without silent overrides."}),
            ("entry-gate-intelligence", "Entry criteria intelligence", {"purpose": "When to block phase entry based on readiness signals."}),
            ("exit-gate-intelligence", "Exit criteria intelligence", {"purpose": "When to block phase exit based on residual risk."}),
            ("release-gate-intelligence", "Release gate intelligence", {"purpose": "Go/No-Go signals from defects, leakage, and readiness."}),
        ],
    },
    "knowledge-base": {
        "title": "Salesforce Quality Intelligence KB",
        "purpose": "Salesforce-specific recurring defect areas and executive report standards.",
        "scope": "Component hotspots + executive reporting standards for QI engine.",
        "inputs": ["Defect tags by component", "Program reports"],
        "outputs": ["Hotspot guidance", "Report outlines"],
        "docs": [
            ("salesforce-quality-intelligence", "SF recurring defect areas", {
                "purpose": "Identify recurring defect areas across VR, Flows, Apex, security, integrations, packages, OmniStudio, Agentforce, industry clouds.",
                "overview": [
                    "Scan defects against Salesforce component tags",
                    "Prioritize prevention for high-frequency + high-impact components",
                    "Ground specifics in 4A/4B knowledge articles",
                ],
                "process": [
                    "Tag defects by component family",
                    "Rank by frequency × severity × business criticality",
                    "Recommend targeted tests, reviews, and automation",
                ],
                "related": [
                    "[../../knowledge/automation/README.md](../../knowledge/automation/README.md)",
                    "[../../knowledge/security/README.md](../../knowledge/security/README.md)",
                    "[../../knowledge/clouds/README.md](../../knowledge/clouds/README.md)",
                ],
            }),
            ("quality-health-report", "Quality Health Report standard", {"purpose": "Standard sections for overall quality health narrative."}),
            ("sprint-quality-report", "Sprint Quality Report", {"purpose": "Sprint-level quality report standard."}),
            ("release-quality-report", "Release Quality Report", {"purpose": "Release-level quality report standard."}),
            ("production-quality-report", "Production Quality Report", {"purpose": "Hypercare/production quality report standard."}),
            ("defect-trend-report", "Defect Trend Report", {"purpose": "Trend report standard for defects."}),
            ("executive-qa-dashboard-qi", "Executive QA Dashboard (QI)", {"purpose": "Executive dashboard content from QI signals.", "related": ["[../../templates/executive-qa-dashboard.md](../../templates/executive-qa-dashboard.md)"]}),
            ("rca-report-standard", "RCA Report standard", {"purpose": "Executive/technical RCA report expectations.", "related": ["[../../templates/defect-rca-report.md](../../templates/defect-rca-report.md)"]}),
            ("risk-assessment-report-qi", "Risk Assessment Report", {"purpose": "QI-oriented risk assessment report standard."}),
            ("quality-improvement-report", "Quality Improvement Report", {"purpose": "Report progress against QIP/CAPA."}),
        ],
    },
}


def write_engine_guides() -> None:
    (QI / "defect-intelligence-engine.md").write_text(f"""---
title: Defect Intelligence Engine
version: {VERSION}
tags: [quality-intelligence, sprint-7]
---

# Defect Intelligence Engine

## Purpose

Orchestrate analysis → classification → RCA → patterns → metrics → prediction → prevention for Salesforce QE.

## Process

```
Ingest defect / quality signals
    ↓
Classify (type, severity, priority)
    ↓
RCA (method selection)
    ↓
Pattern detection + confidence
    ↓
Metrics & trends (no invented %)
    ↓
Predictive risk (confidence stated)
    ↓
Preventive / corrective actions
    ↓
Executive reporting & continuous improvement
```

## Rules

1. Prevention over detection-only advice.  
2. Never invent metric values—ask for counts or mark TBC.  
3. Reuse Sprint 5 defect/RCA templates and Sprint 6 bug guidance.  
4. Tie Salesforce hotspots to 4A/4B knowledge.  

## Related

{bullets(CROSS_ROOT)}
""", encoding="utf-8")


def main() -> None:
    QI.mkdir(parents=True, exist_ok=True)
    write_engine_guides()

    folder_order = [
        "defect-management",
        "root-cause-analysis",
        "defect-patterns",
        "quality-metrics",
        "risk-analysis",
        "trend-analysis",
        "predictive-quality",
        "continuous-improvement",
        "quality-gates",
        "knowledge-base",
    ]

    (QI / "README.md").write_text(f"""---
title: Quality Intelligence — README
module: Salesforce Quality Engineering
version: {VERSION}
tags: [quality-intelligence, sprint-7]
---

# Defect Intelligence & Quality Analytics Engine

## Purpose

Enable the AI to act as a **Quality Advisor**: analyse defects, perform RCA, detect patterns, interpret metrics, predict risk, and recommend prevention across Salesforce delivery.

## Scope ({SPRINT})

**In scope:** Defect management, RCA methods, patterns, metrics, risk/trend/predictive analytics, continuous improvement, Salesforce hotspot intelligence, executive report standards.  

**Out of scope:** Fabricating metrics without data; replacing Sprint 5 templates (reuse them).

## Engine entry

- [defect-intelligence-engine.md](defect-intelligence-engine.md)

## Folders

| Folder | Focus |
|--------|-------|
| [defect-management/](defect-management/README.md) | Lifecycle, severity, defect types |
| [root-cause-analysis/](root-cause-analysis/README.md) | 5 Whys, Fishbone, Pareto, FMEA, cause classes |
| [defect-patterns/](defect-patterns/README.md) | Pattern detection & prevention |
| [quality-metrics/](quality-metrics/README.md) | DRE, leakage, coverage, indices |
| [risk-analysis/](risk-analysis/README.md) | Risk types & scoring |
| [trend-analysis/](trend-analysis/README.md) | Sprint/release/prod trends |
| [predictive-quality/](predictive-quality/README.md) | Predictions + confidence + mitigations |
| [continuous-improvement/](continuous-improvement/README.md) | Retro, CAPA, QIP, TPI |
| [quality-gates/](quality-gates/README.md) | Gate decision intelligence |
| [knowledge-base/](knowledge-base/README.md) | SF hotspots + executive reports |

## Navigation

- **Previous:** [../ado/README.md](../ado/README.md)
- **Next:** [defect-intelligence-engine.md](defect-intelligence-engine.md)
- **See Also:** [../skill.md](../skill.md)

## Related Documents

{bullets(CROSS_ROOT)}
""", encoding="utf-8")

    count = 2
    for i, folder in enumerate(folder_order):
        cfg = FOLDERS[folder]
        path = QI / folder
        path.mkdir(parents=True, exist_ok=True)
        prev = f"../{folder_order[i-1]}/README.md" if i > 0 else "../README.md"
        nxt = f"../{folder_order[i+1]}/README.md" if i < len(folder_order) - 1 else "../README.md"
        docs = []
        for item in cfg["docs"]:
            slug, blurb = item[0], item[1]
            meta = dict(item[2]) if len(item) > 2 else {}
            docs.append((slug, blurb, meta))

        (path / "README.md").write_text(
            folder_readme(
                folder,
                cfg["title"],
                cfg["purpose"],
                cfg["scope"],
                cfg["inputs"],
                cfg["outputs"],
                [(s, b) for s, b, _ in docs],
                prev,
                nxt,
            ),
            encoding="utf-8",
        )
        count += 1
        slugs = [s for s, _, _ in docs]
        for idx, (slug, blurb, meta) in enumerate(docs):
            meta = {**meta, "title": meta.get("title") or titleize(slug)}
            if "purpose" not in meta:
                meta["purpose"] = blurb
            (path / f"{slug}.md").write_text(
                article(folder, slug, meta, nav_for(slugs, idx)),
                encoding="utf-8",
            )
            count += 1

    print(f"Wrote ~{count} files under {QI}")


if __name__ == "__main__":
    main()
