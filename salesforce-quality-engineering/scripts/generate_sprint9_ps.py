#!/usr/bin/env python3
"""Generate Sprint 9 — Production Support, Release Operations & Operational Excellence."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PS = ROOT / "production-support"
VERSION = "0.11.0"
DATE = "2026-07-18"
SPRINT = "Sprint 9"


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
    ]


CROSS = cross("../..")
CROSS_ROOT = cross("..")


def titleize(slug: str) -> str:
    special = {
        "go-live": "Go-Live",
        "go-no-go-meeting": "Go/No-Go Meeting",
        "sla-management": "SLA Management",
        "olas": "OLAs",
        "kpis": "KPIs",
        "rfc-process": "RFC Process",
        "cab-meetings": "CAB Meetings",
        "mttr": "MTTR",
        "mtbf": "MTBF",
        "sit": "SIT",
        "uat": "UAT",
        "itil-overview": "ITIL Overview",
        "api-failure": "API Failure",
        "agentforce": "Agentforce",
        "omnistudio": "OmniStudio",
        "experience-cloud": "Experience Cloud",
        "utilities-cloud": "Utilities Cloud",
        "data-cloud": "Data Cloud",
        "marketing-cloud-integrations": "Marketing Cloud Integrations",
        "batch-apex": "Batch Apex",
        "queueable-apex": "Queueable Apex",
        "post-incident-review": "Post-Incident Review",
        "known-error-database": "Known Error Database",
    }
    return special.get(slug, slug.replace("-", " ").title())


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {i}" for i in items)


def folder_readme(
    folder: str,
    title: str,
    purpose: str,
    scope: str,
    articles: list[tuple[str, str]],
    prev: str,
    nxt: str,
) -> str:
    rows = "\n".join(f"| [{titleize(s)}]({s}.md) | {b} |" for s, b in articles)
    return f"""---
title: {title} — README
module: Salesforce Quality Engineering
category: Production Support
document_type: Guide
version: {VERSION}
review_status: Draft
owner: QE Practice Lead
created_date: {DATE}
last_updated: {DATE}
tags: [production-support, sprint-9, {folder}]
---

# {title}

## Purpose

{purpose}

## Scope

{scope}

Reuse Sprint 5–8 templates and QI RCA where applicable—avoid duplicating defect/automation engines.

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
    purpose = meta.get("purpose") or f"Provide enterprise guidance on {title} for Salesforce production operations."
    related = meta.get("related", []) + CROSS + [
        "[README.md](README.md)",
        "[../README.md](../README.md)",
        "[../production-support-engine.md](../production-support-engine.md)",
    ]

    def sec(key: str, heading: str, default: list[str] | str) -> str:
        val = meta.get(key, default)
        body = val if isinstance(val, str) else bullets(val)
        return f"## {heading}\n\n{body}\n"

    return (
        f"---\ntitle: {title}\nmodule: Salesforce Quality Engineering\n"
        f"category: Production Support\ndocument_type: Knowledge Article\n"
        f"version: {VERSION}\nreview_status: Draft\nowner: QE Practice Lead\n"
        f"created_date: {DATE}\nlast_updated: {DATE}\n"
        f"tags: [production-support, sprint-9, {folder}]\n"
        f"keywords: [{slug}, production-support, operational-excellence]\n---\n\n"
        f"# {title}\n\n"
        f"**Scope:** {SPRINT} Production Support & Operational Excellence — Production Support Lead posture. "
        f"ITIL 4-aligned; reuse Sprint 7 RCA/defect intelligence and Sprint 5 hypercare/prod-val templates. "
        f"Do not invent SLA/MTTR values without data.\n\n"
        f"**Version:** {VERSION}\n\n---\n\n"
        + sec("purpose", "Purpose", purpose)
        + sec(
            "business_context",
            "Business Context",
            meta.get(
                "business_context",
                [
                    "Production stability protects revenue, trust, and regulatory posture on Salesforce programs.",
                    "Operational excellence closes the loop from go-live through continuous service improvement.",
                ],
            ),
        )
        + sec(
            "lifecycle",
            "Lifecycle",
            meta.get(
                "lifecycle",
                [
                    "Detect / request → Classify → Respond → Resolve / fulfill → Validate → Close → Improve",
                    f"Map {title} into the broader incident–problem–change–release value stream where relevant.",
                ],
            ),
        )
        + sec(
            "roles",
            "Roles",
            meta.get(
                "roles",
                [
                    "Production Support Lead / Service Delivery Lead",
                    "Release Manager / Change Manager",
                    "Incident / Major Incident Manager",
                    "QE / Hypercare Lead",
                    "Business Product Owner / Process Owner",
                    "Platform / Integration / Security specialists",
                ],
            ),
        )
        + sec(
            "responsibilities",
            "Responsibilities",
            meta.get(
                "responsibilities",
                [
                    "Protect production; communicate clearly; restore service first when warranted",
                    "Capture evidence for RCA and known errors; feed preventive actions",
                    "Align with CAB/release governance and agreed SLAs/OLAs",
                ],
            ),
        )
        + sec(
            "inputs",
            "Inputs",
            meta.get(
                "inputs",
                [
                    "Incident/problem/change tickets",
                    "Monitoring alerts and logs",
                    "Release/deploy packages and runbooks",
                    "Business impact statements",
                ],
            ),
        )
        + sec(
            "outputs",
            "Outputs",
            meta.get(
                "outputs",
                [
                    "Operational decisions, checklists, communications, and reports",
                    "Known errors / knowledge articles / improvement actions",
                ],
            ),
        )
        + sec(
            "activities",
            "Activities",
            meta.get(
                "activities",
                [
                    f"Plan and execute {title} activities with clear owners and timeboxes",
                    "Validate outcomes; escalate per matrix; update stakeholders",
                    "Record lessons and feed Sprint 7 QI / continuous improvement",
                ],
            ),
        )
        + sec(
            "kpis",
            "KPIs",
            meta.get(
                "kpis",
                [
                    "Define program KPIs with baselines—do not invent percentages",
                    "Examples: MTTA, MTTR, SLA attainment, reopen rate, change success rate",
                ],
            ),
        )
        + sec(
            "slas",
            "SLAs",
            meta.get(
                "slas",
                [
                    "Use contracted or program SLAs/OLAs; mark TBC if not provided",
                    "Separate response vs resolution targets by severity",
                ],
            ),
        )
        + sec(
            "risks",
            "Risks",
            meta.get(
                "risks",
                [
                    "Incomplete impact assessment or weak rollback readiness",
                    "Communication gaps during major incidents",
                    "Bypassing change control under pressure",
                ],
            ),
        )
        + sec(
            "practices",
            "Best Practices",
            meta.get(
                "practices",
                [
                    "Restore service first for Sev1; schedule deep RCA after stabilization",
                    "Keep war-room / bridge discipline; single source of truth for status",
                    "Link incidents → problems → known errors → changes",
                    "Reuse runbooks; update after every major event",
                ],
            ),
        )
        + sec(
            "examples",
            "Examples",
            meta.get(
                "examples",
                [
                    "Illustrative: Sev1 integration outage → major incident bridge → workaround → PIR → problem record",
                    "Replace with program ticket IDs and real timestamps when available",
                ],
            ),
        )
        + sec(
            "interview",
            "Interview Questions",
            meta.get(
                "interview",
                [
                    f"How do you apply {title} on an enterprise Salesforce program?",
                    "How do ITIL practices interact with Agile/SAFe release trains?",
                    "What evidence proves production is healthy after a release?",
                ],
            ),
        )
        + sec(
            "references",
            "References",
            meta.get(
                "references",
                [
                    "ITIL 4 service value system (practice alignment—not certification dump)",
                    "ISTQB Advanced Test Management (release/ops quality interfaces)",
                    "Salesforce Well-Architected (reliable, secure, performant)",
                    "DevOps / continuous delivery operational feedback loops",
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
                    "Program-specific SLA overlays under outputs/<project>/",
                    "Deeper monitoring tool adapters (optional later)",
                ],
            )
        )
        + "\n"
    )


def runbook(slug: str, meta: dict, nav: dict) -> str:
    title = meta.get("title") or titleize(slug)
    related = CROSS + [
        "[README.md](README.md)",
        "[../README.md](../README.md)",
        "[../production-support-engine.md](../production-support-engine.md)",
    ]
    return f"""---
title: Runbook — {title}
module: Salesforce Quality Engineering
category: Production Support
document_type: Runbook
version: {VERSION}
tags: [production-support, sprint-9, runbooks]
---

# Runbook — {title}

## Purpose

{meta.get("purpose", f"Provide a reusable operational runbook for {title}.")}

## Trigger

{bullets(meta.get("trigger", ["Alert, incident, or scheduled operational event matching this runbook"]))}

## Prerequisites

{bullets(meta.get("prerequisites", ["Access to target org/tools", "On-call / bridge roles assigned", "Latest package/config known"]))}

## Step-by-Step Activities

{bullets(meta.get("steps", ["Confirm trigger and severity", "Stabilize / contain", "Diagnose with evidence", "Apply fix or workaround", "Validate service restoration", "Communicate and document"]))}

## Validation

{bullets(meta.get("validation", ["Business-critical path works for affected personas", "Monitoring returns to green", "No new Sev1/Sev2 introduced"]))}

## Rollback

{bullets(meta.get("rollback", ["Execute approved rollback plan if fix increases risk", "Re-validate after rollback"]))}

## Communication

{bullets(meta.get("communication", ["Initial bridge update", "Cadenced stakeholder updates", "Resolution / PIR notice"]))}

## Escalation

{bullets(meta.get("escalation", ["Per severity matrix to Platform / Integration / Vendor / Exec", "Major Incident Manager owns Sev1 bridges"]))}

## Success Criteria

{bullets(meta.get("success", ["Service restored within SLA or workaround accepted", "Ticket updated with evidence and next actions"]))}

## Lessons Learned

{bullets(meta.get("lessons", ["Capture known error / knowledge article", "Feed problem management and runbook updates"]))}

## Related Documents

{bullets(related)}

## Navigation

- **Previous:** [{nav['prev_title']}]({nav['prev']})
- **Next:** [{nav['next_title']}]({nav['next']})
- **See Also:** [../incident-management/README.md](../incident-management/README.md)

## Future Enhancements

- Link to org-specific alert IDs and CMDBs
"""


FOLDERS: dict[str, dict] = {
    "go-live": {
        "title": "Go-Live",
        "purpose": "Prepare and execute Salesforce go-live with evidence-based Go/No-Go decisions.",
        "scope": "Readiness, checklists, command center, validations, rollback, signoff, communications.",
        "docs": [
            ("go-live-readiness", "Overall readiness assessment"),
            ("go-live-checklist", "Executable checklist"),
            ("go-live-command-center", "Command center / bridge ops"),
            ("deployment-validation", "Technical deploy validation"),
            ("business-validation", "Business validation"),
            ("technical-validation", "Technical validation"),
            ("data-validation", "Data validation"),
            ("rollback-readiness", "Rollback readiness"),
            ("business-signoff", "Business signoff"),
            ("support-readiness", "Support readiness"),
            ("communication-plan", "Go-live communications"),
            ("go-no-go-meeting", "Go/No-Go meeting"),
            ("war-room-management", "War room management"),
            ("success-criteria", "Success criteria"),
        ],
    },
    "hypercare": {
        "title": "Hypercare",
        "purpose": "Stabilize production immediately after go-live with structured hypercare.",
        "scope": "Planning, team, activities, tracking, monitoring, reporting, exit, KT.",
        "docs": [
            ("hypercare-planning", "Hypercare plan"),
            ("hypercare-team", "Team and RACI"),
            ("hypercare-activities", "Daily activities"),
            ("issue-tracking", "Issue tracking"),
            ("business-support", "Business support"),
            ("monitoring", "Hypercare monitoring"),
            ("daily-reporting", "Daily reporting"),
            ("risk-review", "Risk review"),
            ("lessons-learned", "Lessons learned"),
            ("exit-criteria", "Exit criteria"),
            ("knowledge-transfer", "Knowledge transfer"),
        ],
    },
    "incident-management": {
        "title": "Incident Management",
        "purpose": "Restore service quickly with disciplined Salesforce incident management.",
        "scope": "Lifecycle, severity/priority, major incidents, SLA, PIR, knowledge capture.",
        "docs": [
            ("incident-lifecycle", "Incident lifecycle"),
            ("incident-classification", "Classification"),
            ("severity-matrix", "Severity matrix"),
            ("priority-matrix", "Priority matrix"),
            ("major-incidents", "Major incidents"),
            ("incident-escalation", "Escalation"),
            ("incident-communication", "Communication"),
            ("incident-resolution", "Resolution"),
            ("incident-closure", "Closure"),
            ("sla-management", "SLA management"),
            ("business-impact-assessment", "Business impact"),
            ("stakeholder-communication", "Stakeholder communication"),
            ("knowledge-capture", "Knowledge capture"),
            ("post-incident-review", "Post-incident review"),
        ],
    },
    "problem-management": {
        "title": "Problem Management",
        "purpose": "Find and remove root causes; reduce recurring production pain.",
        "scope": "Identification, RCA, known errors, CAPA, closure, CI.",
        "docs": [
            ("problem-identification", "Identify problems"),
            ("root-cause-analysis", "Operational RCA"),
            ("known-error-database", "Known errors"),
            ("trend-analysis", "Problem trends"),
            ("preventive-actions", "Preventive actions"),
            ("corrective-actions", "Corrective actions"),
            ("problem-closure", "Closure"),
            ("knowledge-updates", "Knowledge updates"),
            ("continuous-improvement", "Continuous improvement"),
        ],
    },
    "change-management": {
        "title": "Change Management",
        "purpose": "Control Salesforce production change risk with ITIL-aligned change practice.",
        "scope": "RFC, CAB, change types, risk/impact, validation, rollback, approvals.",
        "docs": [
            ("rfc-process", "RFC process"),
            ("cab-meetings", "CAB meetings"),
            ("emergency-changes", "Emergency changes"),
            ("normal-changes", "Normal changes"),
            ("standard-changes", "Standard changes"),
            ("risk-assessment", "Risk assessment"),
            ("impact-assessment", "Impact assessment"),
            ("change-validation", "Change validation"),
            ("rollback-planning", "Rollback planning"),
            ("approval-workflow", "Approval workflow"),
            ("communication-strategy", "Communication strategy"),
        ],
    },
    "release-operations": {
        "title": "Release Operations",
        "purpose": "Operate Salesforce releases safely from calendar through monitoring and rollback.",
        "scope": "Readiness, deploy validation, smoke, prod val, metrics, governance, env coordination.",
        "docs": [
            ("release-calendar", "Release calendar"),
            ("release-readiness", "Release readiness"),
            ("deployment-validation", "Deployment validation"),
            ("release-communication", "Release communication"),
            ("smoke-testing", "Production smoke"),
            ("production-validation", "Production validation"),
            ("release-monitoring", "Release monitoring"),
            ("rollback", "Rollback ops"),
            ("release-metrics", "Release metrics"),
            ("release-governance", "Release governance"),
            ("environment-coordination", "Environment coordination"),
        ],
    },
    "monitoring": {
        "title": "Monitoring",
        "purpose": "Detect Salesforce production risk early through layered monitoring.",
        "scope": "Health, batch, Flow, events, integrations, API, data, security, performance, alerts.",
        "docs": [
            ("salesforce-health-monitoring", "Org health"),
            ("batch-monitoring", "Batch jobs"),
            ("flow-monitoring", "Flows"),
            ("platform-events", "Platform Events"),
            ("integration-monitoring", "Integrations"),
            ("api-monitoring", "APIs"),
            ("data-monitoring", "Data integrity"),
            ("security-monitoring", "Security"),
            ("login-monitoring", "Logins"),
            ("performance-monitoring", "Performance"),
            ("dashboard-monitoring", "Ops dashboards"),
            ("alert-management", "Alert management"),
            ("threshold-management", "Thresholds"),
        ],
    },
    "service-management": {
        "title": "Service Management",
        "purpose": "Align Salesforce support with ITIL-oriented service management practices.",
        "scope": "ITIL overview, request/incident/problem/change, knowledge, SLA/OLA/KPI, reviews.",
        "docs": [
            ("itil-overview", "ITIL overview for SF ops"),
            ("service-requests", "Service requests"),
            ("incidents", "Incidents practice"),
            ("problems", "Problems practice"),
            ("changes", "Changes practice"),
            ("knowledge-articles", "Knowledge articles"),
            ("slas", "SLAs"),
            ("olas", "OLAs"),
            ("kpis", "Service KPIs"),
            ("service-reviews", "Service reviews"),
            ("operational-metrics", "Operational metrics"),
        ],
    },
    "environment-management": {
        "title": "Environment Management",
        "purpose": "Govern Salesforce environments from Dev through Production.",
        "scope": "Env tiers, refresh, drift, comparison, deploy coordination, readiness.",
        "docs": [
            ("development", "Development orgs"),
            ("qa", "QA"),
            ("sit", "SIT"),
            ("uat", "UAT"),
            ("pre-production", "Pre-production"),
            ("production", "Production"),
            ("sandbox-refresh", "Sandbox refresh"),
            ("data-refresh", "Data refresh"),
            ("configuration-drift", "Config drift"),
            ("environment-comparison", "Env comparison"),
            ("deployment-coordination", "Deploy coordination"),
            ("test-environment-readiness", "Test env readiness"),
        ],
    },
    "knowledge-management": {
        "title": "Knowledge Management",
        "purpose": "Capture and reuse operational knowledge for faster, safer support.",
        "scope": "Articles, known errors, runbook links, KT, searchability, ownership.",
        "docs": [
            ("knowledge-strategy", "KM strategy"),
            ("article-standards", "Article standards"),
            ("known-errors", "Known errors"),
            ("search-and-findability", "Findability"),
            ("ownership-and-review", "Ownership"),
            ("kt-from-incidents", "KT from incidents"),
        ],
    },
    "operational-excellence": {
        "title": "Operational Excellence",
        "purpose": "Drive continuous improvement of Salesforce production reliability and support health.",
        "scope": "KPIs, trends, stability, gates, audits, compliance, CI.",
        "docs": [
            ("operational-kpis", "Operational KPIs"),
            ("support-metrics", "Support metrics"),
            ("incident-trends", "Incident trends"),
            ("release-stability", "Release stability"),
            ("production-stability", "Production stability"),
            ("quality-gates", "Ops quality gates"),
            ("governance-reviews", "Governance reviews"),
            ("support-health-checks", "Support health checks"),
            ("audit-readiness", "Audit readiness"),
            ("compliance", "Compliance awareness"),
            ("continuous-improvement", "Continuous improvement"),
        ],
    },
    "support-playbooks": {
        "title": "Support Playbooks",
        "purpose": "Ceremony and workflow playbooks for production support teams.",
        "scope": "On-call, triage, major incident, hypercare exit, service review playbooks.",
        "docs": [
            ("on-call-playbook", "On-call"),
            ("triage-playbook", "Triage"),
            ("major-incident-playbook", "Major incident"),
            ("hypercare-exit-playbook", "Hypercare exit"),
            ("service-review-playbook", "Service review"),
            ("release-bridge-playbook", "Release bridge"),
        ],
    },
    "operational-analytics": {
        "title": "Operational Analytics",
        "purpose": "Analyze production and support signals for risk and improvement.",
        "scope": "Trends, recurring failures, SLA, MTTR/MTBF, stability, automation opportunities.",
        "docs": [
            ("incident-trends", "Incident trends"),
            ("release-trends", "Release trends"),
            ("support-trends", "Support trends"),
            ("recurring-failures", "Recurring failures"),
            ("high-risk-components", "High-risk components"),
            ("high-volume-incidents", "High-volume incidents"),
            ("sla-breaches", "SLA breaches"),
            ("mttr", "MTTR"),
            ("mtbf", "MTBF"),
            ("production-stability", "Production stability"),
            ("business-impact", "Business impact"),
            ("support-effort", "Support effort"),
            ("automation-opportunities", "Automation opportunities"),
        ],
    },
    "executive-reporting": {
        "title": "Executive Reporting",
        "purpose": "Standard operational and executive reports for Salesforce production support.",
        "scope": "Daily/weekly/health/hypercare/incident/problem/release/dashboards/service review.",
        "docs": [
            ("daily-support-report", "Daily support report"),
            ("weekly-operations-report", "Weekly operations"),
            ("production-health-report", "Production health"),
            ("hypercare-report", "Hypercare report"),
            ("incident-summary", "Incident summary"),
            ("problem-report", "Problem report"),
            ("release-report", "Release report"),
            ("operational-dashboard", "Operational dashboard"),
            ("executive-dashboard", "Executive dashboard"),
            ("service-review-report", "Service review report"),
        ],
    },
}

RUNBOOKS = [
    ("production-deployment", "Production deployment steps"),
    ("major-incident", "Major incident response"),
    ("integration-failure", "Integration failure"),
    ("batch-failure", "Batch failure"),
    ("api-failure", "API failure"),
    ("permission-issue", "Permission issue"),
    ("flow-failure", "Flow failure"),
    ("validation-rule-failure", "Validation rule failure"),
    ("data-load-failure", "Data load failure"),
    ("environment-failure", "Environment failure"),
    ("rollback", "Rollback execution"),
    ("business-communication", "Business communication"),
    ("emergency-support", "Emergency support"),
]

SF_DOCS = [
    ("flows", "Troubleshoot Flows"),
    ("validation-rules", "Validation rules"),
    ("permission-sets", "Permission sets"),
    ("profiles", "Profiles"),
    ("sharing-rules", "Sharing rules"),
    ("record-types", "Record types"),
    ("reports", "Reports"),
    ("dashboards", "Dashboards"),
    ("experience-cloud", "Experience Cloud"),
    ("agentforce", "Agentforce"),
    ("omnistudio", "OmniStudio"),
    ("platform-events", "Platform Events"),
    ("integrations", "Integrations"),
    ("batch-apex", "Batch Apex"),
    ("scheduled-jobs", "Scheduled Jobs"),
    ("queueable-apex", "Queueable Apex"),
    ("managed-packages", "Managed packages"),
    ("utilities-cloud", "Utilities Cloud"),
    ("data-cloud", "Data Cloud"),
    ("marketing-cloud-integrations", "Marketing Cloud integrations"),
]


def root_readme() -> str:
    rows = "\n".join(
        f"| [{cfg['title']}]({folder}/README.md) | {cfg['purpose']} |" for folder, cfg in FOLDERS.items()
    )
    return f"""---
title: Production Support — README
module: Salesforce Quality Engineering
version: {VERSION}
tags: [production-support, sprint-9]
---

# Production Support, Release Operations & Operational Excellence

## Purpose

Enable the AI to act as a **Production Support Lead / Release Manager / Service Delivery Consultant**: assess go-live readiness, run hypercare, manage incidents/problems/changes, operate releases, monitor health, and drive operational excellence for Salesforce.

## Scope (Sprint 9)

**In scope:** Go-live, hypercare, ITIL-aligned service practices, release operations, monitoring, environments, knowledge, operational excellence, runbooks, Salesforce production intelligence, operational analytics, executive reporting.

**Out of scope:** Inventing SLA/MTTR/KPI values; replacing Sprint 7 defect RCA engine (reuse it); full Apex fix implementation.

## Engine entry

- [production-support-engine.md](production-support-engine.md)

## Folders

| Folder | Focus |
|--------|-------|
{rows}
| [runbooks/](runbooks/README.md) | Reusable operational runbooks |
| [salesforce/](salesforce/README.md) | Salesforce production troubleshooting intelligence |

## ITIL coverage

Incidents · Problems · Changes · Service requests · Knowledge · SLA/OLA · Continual improvement (practice-level alignment).

## Runbook library

See [runbooks/](runbooks/README.md) — deployment, major incident, integration/batch/API/Flow failures, rollback, emergency support, and more.

## Monitoring

Layered Salesforce health, jobs, Flow, events, integrations, security, performance — [monitoring/](monitoring/README.md).

## Navigation

- **Previous:** [../automation-intelligence/README.md](../automation-intelligence/README.md)
- **Next:** [production-support-engine.md](production-support-engine.md)
- **See Also:** [../skill.md](../skill.md)

## Related Documents

{bullets(CROSS_ROOT)}
- [Sprint 5 Hypercare / Prod Val templates](../templates/README.md)
- [Sprint 7 RCA](../quality-intelligence/root-cause-analysis/README.md)
"""


def engine_md() -> str:
    return f"""---
title: Production Support Engine
version: {VERSION}
tags: [production-support, sprint-9]
---

# Production Support & Operational Excellence Engine

## Purpose

Orchestrate go-live → hypercare → incident/problem/change → release ops → monitoring → service improvement for Salesforce production.

## Process

```
Go-Live readiness & Go/No-Go
    ↓
Deploy + production validation
    ↓
Hypercare (stabilize)
    ↓
Steady-state: Incident / Request / Change / Release
    ↓
Problem management + known errors
    ↓
Monitoring & operational analytics
    ↓
Executive reporting + continual improvement
```

## Hard rules

1. Restore service first for Sev1; deep RCA after stabilization (reuse Sprint 7 methods).  
2. Never invent SLA, MTTR, MTBF, or KPI values—ask or mark TBC.  
3. Prefer runbooks; update them after major events.  
4. Emergency change ≠ no documentation.  
5. Cross-link 4A/4B for Salesforce component troubleshooting.  

## Capabilities

| Capability | Path |
|------------|------|
| Production Intelligence | [salesforce/](salesforce/README.md) |
| Incident Intelligence | [incident-management/](incident-management/README.md) |
| Operational Excellence | [operational-excellence/](operational-excellence/README.md) |
| ITIL Awareness | [service-management/](service-management/README.md) |
| Release Operations | [release-operations/](release-operations/README.md) |
| Support Analytics | [operational-analytics/](operational-analytics/README.md) |
| Monitoring Intelligence | [monitoring/](monitoring/README.md) |
| Runbook Intelligence | [runbooks/](runbooks/README.md) |

## Related

{bullets(CROSS_ROOT)}
"""


def main() -> None:
    PS.mkdir(parents=True, exist_ok=True)
    (PS / "README.md").write_text(root_readme(), encoding="utf-8")
    (PS / "production-support-engine.md").write_text(engine_md(), encoding="utf-8")

    folder_order = list(FOLDERS.keys())
    for i, folder in enumerate(folder_order):
        cfg = FOLDERS[folder]
        path = PS / folder
        path.mkdir(parents=True, exist_ok=True)
        docs = list(cfg["docs"])
        prev = f"../{folder_order[i-1]}/README.md" if i > 0 else "../README.md"
        nxt = (
            f"../{folder_order[i+1]}/README.md"
            if i < len(folder_order) - 1
            else "../runbooks/README.md"
        )
        (path / "README.md").write_text(
            folder_readme(folder, cfg["title"], cfg["purpose"], cfg["scope"], docs, prev, nxt),
            encoding="utf-8",
        )
        for j, (slug, _b) in enumerate(docs):
            meta: dict = {}
            if folder == "problem-management" and slug == "root-cause-analysis":
                meta = {
                    "purpose": "Apply operational RCA for production problems; reuse Sprint 7 QI RCA methods.",
                    "activities": [
                        "Select 5 Whys / Fishbone / Pareto / FMEA as appropriate",
                        "Link to incident evidence; avoid blame",
                        "Create known error and CAPA",
                    ],
                    "related": [
                        "[Sprint 7 RCA](../../quality-intelligence/root-cause-analysis/README.md)",
                    ],
                }
            if folder == "go-live" and slug == "go-live-checklist":
                meta = {
                    "purpose": "Provide a structured go-live checklist covering tech, data, business, support, and rollback.",
                    "outputs": ["Completed checklist with owners", "Open risks and Go/No-Go recommendation"],
                }
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

    # Runbooks
    rb = PS / "runbooks"
    rb.mkdir(parents=True, exist_ok=True)
    (rb / "README.md").write_text(
        folder_readme(
            "runbooks",
            "Runbooks",
            "Reusable step-by-step operational runbooks for Salesforce production support.",
            "Deployment, major incident, platform failures, rollback, communications—trigger to success criteria.",
            RUNBOOKS,
            "../executive-reporting/README.md",
            "../salesforce/README.md",
        ),
        encoding="utf-8",
    )
    for j, (slug, blurb) in enumerate(RUNBOOKS):
        meta = {
            "purpose": f"Operational runbook: {blurb}.",
            "trigger": [f"Event matching: {blurb}"],
        }
        if slug == "major-incident":
            meta["steps"] = [
                "Declare major incident; open bridge",
                "Assign MIM / scribe / technical lead",
                "Stabilize / workaround",
                "Communicate on cadence",
                "Resolve or rollback",
                "Validate; schedule PIR",
            ]
        if slug == "rollback":
            meta["steps"] = [
                "Confirm rollback approval",
                "Execute rollback package/plan",
                "Validate critical journeys",
                "Communicate status",
                "Raise problem/follow-up change",
            ]
        prev_s = RUNBOOKS[j - 1][0] + ".md" if j > 0 else "README.md"
        next_s = RUNBOOKS[j + 1][0] + ".md" if j < len(RUNBOOKS) - 1 else "README.md"
        (rb / f"{slug}.md").write_text(
            runbook(
                slug,
                meta,
                {
                    "prev": prev_s,
                    "next": next_s,
                    "prev_title": titleize(RUNBOOKS[j - 1][0]) if j > 0 else "README",
                    "next_title": titleize(RUNBOOKS[j + 1][0]) if j < len(RUNBOOKS) - 1 else "README",
                },
            ),
            encoding="utf-8",
        )

    # Salesforce production intelligence
    sf = PS / "salesforce"
    sf.mkdir(parents=True, exist_ok=True)
    (sf / "README.md").write_text(
        folder_readme(
            "salesforce",
            "Salesforce Production Intelligence",
            "Troubleshoot recurring Salesforce production failure areas with ops-oriented guidance.",
            "Flows through Marketing Cloud integrations—link 4A/4B; do not invent product bugs.",
            SF_DOCS,
            "../runbooks/README.md",
            "../README.md",
        ),
        encoding="utf-8",
    )
    for j, (slug, _b) in enumerate(SF_DOCS):
        meta = {
            "purpose": f"Guide production troubleshooting for Salesforce {titleize(slug)}.",
            "activities": [
                "Confirm symptoms, persona, time window, and recent changes",
                "Check monitoring/logs; isolate config vs code vs data vs integration",
                "Apply workaround; open problem if recurring",
                "Update knowledge / runbook",
            ],
            "related": [
                "[4A/4B knowledge](../../knowledge/README.md)",
                "[Sprint 7 Salesforce QI hotspots](../../quality-intelligence/knowledge-base/salesforce-quality-intelligence.md)",
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

    count = sum(1 for _ in PS.rglob("*.md"))
    print(f"Wrote ~{count} files under {PS}")


if __name__ == "__main__":
    main()
