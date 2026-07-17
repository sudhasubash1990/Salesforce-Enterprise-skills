#!/usr/bin/env python3
"""Generate Sprint 4B — Salesforce Enterprise Business Knowledge (QE)."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
VERSION = "0.6.0"
DATE = "2026-07-17"
SPRINT = "Sprint 4B"

REL = {
    "brain": "../../brain/README.md",
    "skill": "../../skill.md",
    "ra": "../requirement-analysis.md",
    "td": "../test-design-engine.md",
    "reg": "../regression-planning.md",
    "risk": "../risk-based-testing.md",
    "p4a": "../platform/README.md",
    "m4a": "../metadata/README.md",
    "a4a": "../automation/README.md",
    "s4a": "../security/README.md",
    "d4a": "../data/README.md",
    "cap": "../../../shared/salesforce-capability-map.md",
}


def titleize(slug: str) -> str:
    special = {
        "revenue-cloud-cpq": "Revenue Cloud / CPQ",
        "financial-services-cloud": "Financial Services Cloud",
        "health-cloud": "Health Cloud",
        "education-cloud": "Education Cloud",
        "net-zero-cloud": "Net Zero Cloud",
        "manufacturing-cloud": "Manufacturing Cloud",
        "consumer-goods-cloud": "Consumer Goods Cloud",
        "utilities-cloud": "Utilities Cloud",
        "go-no-go-decision": "Go / No-Go Decision",
        "ci-cd-overview": "CI/CD Overview",
        "oauth": "OAuth",
        "rest-apis": "REST APIs",
        "soap-apis": "SOAP APIs",
        "bulk-api": "Bulk API",
        "change-data-capture": "Change Data Capture",
        "api-limits": "API Limits",
        "soql-performance": "SOQL Performance",
        "large-data-volumes": "Large Data Volumes",
        "message-queues": "Message Queues",
    }
    return special.get(slug, slug.replace("-", " ").title())


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {i}" for i in items)


def merge(base: dict, override: dict | None) -> dict:
    out = {k: (list(v) if isinstance(v, list) else v) for k, v in base.items()}
    if override:
        out.update(override)
    return out


DEFAULTS = {
    "purpose": "Explain this enterprise Salesforce capability from a Quality Engineering consulting perspective—business purpose, testing strategy, regression, automation readiness, and production risk.",
    "business_context": [
        "Enterprise programs use this capability to deliver measurable business outcomes across personas and channels.",
        "Quality risk concentrates at process handoffs, integrations, permissions, and release boundaries.",
    ],
    "overview": [
        "Confirm licensed products, edition, and org-specific configuration before asserting behaviour.",
        "Cross-check [shared capability map](" + REL["cap"] + ") where applicable; do not invent features.",
    ],
    "architecture": [
        "Built on Salesforce platform metadata, security, automation, and APIs (see Sprint 4A Platform Foundation).",
        "Often spans multiple clouds, packages, and middleware systems in enterprise landscapes.",
    ],
    "business_usage": [
        "Used by named business personas to complete end-to-end journeys.",
        "Success is measured by correct outcomes, not just successful page loads.",
    ],
    "key_components": [
        "Standard/custom objects, automation, security model, UI, integrations, and analytics as applicable",
        "Map components via Requirement Analysis before designing scenarios",
    ],
    "testing": [
        f"Use [{REL['td']}]({REL['td']}) for scenario objectives and coverage matrix",
        f"Ground platform impact in [{REL['p4a']}]({REL['p4a']}) / [{REL['a4a']}]({REL['a4a']}) / [{REL['s4a']}]({REL['s4a']})",
        "Cover happy path, negative, persona/permission, data, and integration paths as applicable",
    ],
    "functional": [
        "Business process outcomes match acceptance criteria for in-scope personas",
        "Object state and notifications/integrations match design intent",
    ],
    "negative": [
        "Unauthorized persona cannot complete restricted actions",
        "Invalid data / failed integration paths are handled per design (no silent corruption)",
    ],
    "regression": [
        f"Apply [{REL['reg']}]({REL['reg']}) — In / Out / Conditional based on process neighbors",
        "Neighbor clouds, packages, reports, and integrations that consume the same objects/fields",
    ],
    "automation_opp": [
        "API-level checks for deterministic rules; UI for journey/UX-critical paths",
        "Smoke pack candidates for release; deep packs for high-risk process changes",
        "Do not automate unstable exploratory or one-off cutover validation",
    ],
    "performance": [
        "Consider volume, concurrency, and governor-limit failure modes when in scope",
        f"See [{REL['risk']}]({REL['risk']}) and performance knowledge for LDV/hotspots",
    ],
    "security": [
        "Validate CRUD/FLS/sharing for every named persona; treat guest/integration users as high risk",
        f"Reuse [{REL['s4a']}]({REL['s4a']}) for platform security patterns",
    ],
    "production": [
        "Silent process failure after deploy",
        "Permission/config drift vs lower environments",
        "Integration backlog / duplicate processing under peak load",
    ],
    "defects": [
        "Works for admin; fails for end-user persona",
        "Process path incomplete across objects or systems",
        "Missing regression on neighbor reports/integrations",
    ],
    "root_causes": [
        "Incomplete requirement analysis (missing persona, exception, or integration contract)",
        "Environment drift (metadata, CMDT, credentials, package versions)",
        "Assumed standard cloud behaviour that was customized or packaged differently",
    ],
    "practices": [
        "Analyse business process + Salesforce components before writing detailed cases",
        "Prefer platform-native fit; document gaps explicitly for SA/BA",
        f"Reason with [{REL['brain']}]({REL['brain']}), [{REL['ra']}]({REL['ra']}), [{REL['td']}]({REL['td']})",
        "Never invent regulatory requirements—mark TBC with Legal/Compliance",
    ],
    "interview": [
        "How would you derive regression scope for a change in this area?",
        "What production defects are most common and how do you detect them?",
        "Which scenarios are automation candidates vs manual-only?",
    ],
    "references": [
        "Salesforce Help / Product documentation (org-confirmed licenses)",
        "Salesforce Well-Architected principles",
        "ISTQB: risk-based testing, equivalence partitioning, boundary analysis",
        f"[QE Brain]({REL['brain']}) · [Requirement Analysis]({REL['ra']}) · [Test Design]({REL['td']}) · [Platform Foundation 4A]({REL['p4a']})",
    ],
}


def render_doc(folder: str, slug: str, meta: dict, nav: dict) -> str:
    title = meta.get("title") or titleize(slug)
    purpose = meta.get("purpose", DEFAULTS["purpose"])
    related = meta.get("related", []) + [
        f"[QE Brain (Sprint 1)]({REL['brain']})",
        f"[Requirement Analysis (Sprint 2)]({REL['ra']})",
        f"[Test Design Engine (Sprint 3)]({REL['td']})",
        f"[Platform Foundation (Sprint 4A)]({REL['p4a']})",
        "[README.md](README.md)",
        "[../README.md](../README.md)",
    ]

    def sec(key: str, heading: str) -> str:
        val = meta.get(key, DEFAULTS[key])
        body = val if isinstance(val, str) else bullets(val)
        return f"## {heading}\n\n{body}\n"

    return f"""---
title: {title}
module: Salesforce Quality Engineering
category: Knowledge
document_type: Knowledge Article
version: {VERSION}
review_status: Draft
owner: QE Practice Lead
created_date: {DATE}
last_updated: {DATE}
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/knowledge/{folder}/{slug}.md
  - salesforce-quality-engineering/knowledge/requirement-analysis.md
  - salesforce-quality-engineering/knowledge/test-design-engine.md
  - salesforce-quality-engineering/knowledge/platform/README.md
  - salesforce-quality-engineering/brain/README.md
keywords: [{slug}, salesforce, quality-engineering, enterprise]
tags: [knowledge, sprint-4b, {folder}]
---

# {title}

**Purpose:** {purpose}

**Scope:** {SPRINT} Enterprise Business Knowledge — QE lens. Not Admin/Developer how-to. No templates, playbooks, or ADO artifacts.

**Owner:** QE Practice Lead

**Version:** {VERSION}

**Status:** Draft ({SPRINT})

---

{sec("purpose", "Purpose")}
{sec("business_context", "Business Context")}
{sec("overview", "Overview")}
{sec("architecture", "Architecture")}
{sec("business_usage", "Business Usage")}
{sec("key_components", "Key Components")}
{sec("testing", "Testing Considerations")}
{sec("functional", "Functional Testing")}
{sec("negative", "Negative Testing")}
{sec("regression", "Regression Scope")}
{sec("automation_opp", "Automation Opportunities")}
{sec("performance", "Performance Considerations")}
{sec("security", "Security Considerations")}
{sec("production", "Production Risks")}
{sec("defects", "Common Defects")}
{sec("root_causes", "Root Cause Examples")}
{sec("practices", "Best Practices")}
{sec("interview", "Interview Questions")}
{sec("references", "References")}

## Related Documents

{bullets(related)}

## Navigation

- **Previous:** [{nav['prev_label']}]({nav['prev']})
- **Next:** [{nav['next_label']}]({nav['next']})
- **See Also:** [README.md](README.md) · [Platform Foundation 4A]({REL['p4a']})

## Future Enhancements

- Deepen org-edition notes and industry scenario packs under `scenarios/`
- Link Sprint 5 documentation templates to scenario objectives herein
"""


def folder_readme(folder: str, title: str, purpose: str, scope: str, articles: list[tuple[str, str]], prev_f: str | None, next_f: str | None) -> str:
    rows = "\n".join(f"| [{titleize(s)}]({s}.md) | {b} |" for s, b in articles)
    prev = f"[{prev_f}/](../{prev_f}/README.md)" if prev_f else "[../platform/README.md](../platform/README.md)"
    nxt = f"[{next_f}/](../{next_f}/README.md)" if next_f else "[../README.md](../README.md)"
    return f"""---
title: {title} — README
module: Salesforce Quality Engineering
category: Knowledge
document_type: Guide
version: {VERSION}
review_status: Draft
owner: QE Practice Lead
created_date: {DATE}
last_updated: {DATE}
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/knowledge/README.md
keywords: [{folder}, knowledge-index, sprint-4b]
tags: [knowledge, sprint-4b, {folder}]
---

# {title}

## Purpose

{purpose}

## Scope

{scope}

**In scope ({SPRINT}):** This folder (enterprise QE knowledge).  
**Out of scope:** Templates, playbooks, ADO artifacts, detailed test case generation (Sprint 5+).

## Available Documents

| Document | Focus |
|----------|-------|
{rows}

## Navigation

- **Previous:** {prev}
- **Next:** {nxt}
- **See Also:** [{REL['skill']}]({REL['skill']}) · [../README.md](../README.md)

## Related Documents

- [QE Brain]({REL['brain']})
- [Requirement Analysis]({REL['ra']})
- [Test Design Engine]({REL['td']})
- [Platform Foundation (4A)]({REL['p4a']})
- Sibling 4B folders: [clouds](../clouds/README.md) · [managed-packages](../managed-packages/README.md) · [integration](../integration/README.md) · [performance](../performance/README.md) · [release](../release/README.md) · [industry](../industry/README.md)
"""


def nav_for(slugs: list[str], idx: int) -> dict:
    prev_slug = slugs[idx - 1] if idx > 0 else None
    next_slug = slugs[idx + 1] if idx < len(slugs) - 1 else None
    return {
        "prev": f"{prev_slug}.md" if prev_slug else "README.md",
        "prev_label": titleize(prev_slug) if prev_slug else "README",
        "next": f"{next_slug}.md" if next_slug else "README.md",
        "next_label": titleize(next_slug) if next_slug else "README",
    }


# ---------------------------------------------------------------------------
# Catalogs
# ---------------------------------------------------------------------------

CLOUDS = [
    ("sales-cloud", "Lead-to-cash CRM core", {
        "purpose": "QE guidance for Sales Cloud journeys, objects, and enterprise regression hotspots.",
        "key_components": ["Lead, Account, Contact, Opportunity, Quote, Product, Price Book", "Path, forecasting, activities", "Sharing/teams often critical"],
        "business_usage": ["Lead capture → qualify → opportunity → quote/order handoff", "Sales managers forecast; ops govern stages"],
        "related": [f"[Capability Map]({REL['cap']})", "[Revenue Cloud / CPQ](revenue-cloud-cpq.md)"],
    }),
    ("service-cloud", "Case and service operations", {
        "purpose": "Cover Case lifecycle, Omni-Channel, entitlements, Knowledge from a QE lens.",
        "key_components": ["Case, Entitlement, Milestone, Knowledge", "Omni-Channel, macros, service console", "Assignment/escalation/auto-response rules"],
        "related": ["[../../../salesforce-business-analyst/knowledge/service-cloud-patterns.md](../../../salesforce-business-analyst/knowledge/service-cloud-patterns.md) (BA—do not duplicate)"],
    }),
    ("experience-cloud", "Digital experiences / portals", {
        "purpose": "Test persona access, guest vs authenticated, sharing, and branded journeys.",
        "security": ["Guest user oversharing is a top enterprise risk", "Profile/permission set assignment on self-registration"],
        "production": ["Broken public pages after deploy", "Incorrect record visibility for partners/customers"],
    }),
    ("field-service", "Field workforce / work orders", {
        "purpose": "Validate work orders, scheduling, mobile/offline, and inventory impacts.",
        "key_components": ["Work Order, Service Appointment, Service Resource", "Scheduling, optimization, mobile app themes"],
    }),
    ("revenue-cloud-cpq", "CPQ / Revenue Cloud quoting", {
        "purpose": "Test product rules, pricing, guided selling, quote-to-order handoffs.",
        "regression": ["Price/product rule interactions", "Bundle constraints", "Amendment/renewal paths"],
    }),
    ("marketing-cloud", "Marketing Cloud functional overview", {
        "purpose": "Functional overview for CRM sync, journeys, and consent touchpoints—not full MC admin.",
        "overview": ["Focus QE on CRM connector sync, journey entry, and consent flags touching Salesforce data", "Defer deep Studio configuration to marketing specialists"],
    }),
    ("data-cloud", "Data Cloud functional overview", {
        "purpose": "QE focus on identity resolution, segments, activation, and data quality touchpoints.",
    }),
    ("agentforce", "AI agents and grounded actions", {
        "purpose": "Validate agent actions, grounding, guardrails, escalation, and auditability.",
        "negative": ["Out-of-policy action", "Ungrounded / incorrect data use", "Failed human escalation"],
    }),
    ("omnistudio", "FlexCards, Omniscripts, DataRaptors, IPs", {
        "purpose": "Test Omniscript paths, DataRaptor transforms, and Integration Procedure contracts.",
        "related": [f"[Integration knowledge](../integration/README.md)"],
    }),
    ("financial-services-cloud", "FSC overview for QE", {
        "purpose": "Overview of Financial Services Cloud patterns; confirm regulatory constraints with Compliance.",
        "practices": ["Never invent KYC/AML/regulatory rules—mark TBC with Legal/Compliance"],
    }),
    ("health-cloud", "Health Cloud overview for QE", {
        "purpose": "Overview of care/patient-adjacent CRM patterns; PHI/HIPAA constraints are Legal-confirmed.",
        "security": ["Access control and audit evidence are primary QE themes", "Do not invent clinical workflows"],
    }),
    ("education-cloud", "Education Cloud overview", {
        "purpose": "Overview of education constituent/recruitment/service themes for QE impact.",
    }),
    ("net-zero-cloud", "Net Zero Cloud overview", {
        "purpose": "Overview of sustainability data/process themes relevant to QE validation.",
    }),
    ("manufacturing-cloud", "Manufacturing Cloud overview", {
        "purpose": "Overview of account-based forecasting / manufacturing CRM themes for QE.",
        "related": ["[../industry/manufacturing.md](../industry/manufacturing.md)"],
    }),
    ("consumer-goods-cloud", "Consumer Goods Cloud overview", {
        "purpose": "Overview of retail execution / CG cloud themes for QE.",
        "related": ["[../industry/consumer-goods.md](../industry/consumer-goods.md)"],
    }),
    ("utilities-cloud", "Utilities Cloud / industry cloud", {
        "purpose": "QE guidance for utilities processes on Salesforce (service, meter, outage themes).",
        "related": ["[../industry/utilities.md](../industry/utilities.md)", "[../industry/energy.md](../industry/energy.md)"],
    }),
]

PACKAGES = [
    ("managed-packages", "Managed package fundamentals for QE", {
        "purpose": "Explain managed package constraints, upgrade risk, and subscriber testing strategy.",
    }),
    ("unlocked-packages", "Unlocked package testing", {
        "purpose": "Validate unlocked package install/upgrade and coexistence with org customizations.",
    }),
    ("namespace-prefixes", "Namespace impact on tests/integrations", {
        "purpose": "Ensure API/Apex/Flow references handle namespaced components correctly.",
    }),
    ("package-dependencies", "Dependency graphs and install order", {
        "purpose": "Test prerequisites and broken subscriber overrides after dependency changes.",
    }),
    ("package-upgrades", "Upgrade validation strategy", {
        "purpose": "Define pre/post upgrade smoke, data, automation, and permission regression.",
    }),
    ("version-compatibility", "API/package version compatibility", {
        "purpose": "Track package versions, deprecated components, and API version drift.",
    }),
    ("custom-objects-in-packages", "Packaged custom objects", {
        "purpose": "QE focus on packaged schema, subscriber extensions, and layout/FLS after upgrade.",
    }),
    ("packaged-apex", "Packaged Apex behaviour", {
        "purpose": "Validate packaged Apex interactions with subscriber automation and governors.",
    }),
    ("packaged-flows", "Packaged Flow behaviour", {
        "purpose": "Test packaged Flow entry criteria, versions, and subscriber overrides/extensions.",
    }),
    ("packaged-validation-rules", "Packaged validation rules", {
        "purpose": "Validate packaged VR messages, bypass patterns, and upgrade changes.",
    }),
    ("packaged-metadata", "Other packaged metadata", {
        "purpose": "Cover layouts, permission sets, reports, and settings shipped in packages.",
        "related": [f"[Metadata 4A]({REL['m4a']})"],
    }),
    ("testing-managed-packages", "Package test strategy", {
        "purpose": "Combine vendor release notes with subscriber-org process regression.",
    }),
    ("regression-strategy", "Package regression strategy", {
        "purpose": "Risk-based regression packs around package upgrades and subscriber customizations.",
        "related": [f"[Regression Planning]({REL['reg']})"],
    }),
    ("upgrade-testing", "Upgrade testing playbook (knowledge)", {
        "purpose": "Structured upgrade test themes: install, config, process, integration, security.",
    }),
    ("troubleshooting", "Install/upgrade troubleshooting for QE", {
        "purpose": "QE checklist for install errors, missing access, and post-upgrade defects.",
    }),
    ("vendor-coordination", "Vendor coordination for quality", {
        "purpose": "How QE engages ISV vendors: release notes, known issues, sandbox timing, escalation.",
    }),
]

INTEGRATION = [
    ("rest-apis", "REST API testing", {
        "purpose": "Guide REST contract, auth, status codes, and idempotency checks for QE.",
        "related": ["[../api-testing.md](../api-testing.md)", "[../integration-testing.md](../integration-testing.md)"],
    }),
    ("soap-apis", "SOAP API patterns", {"purpose": "Cover SOAP login, CRUD, and fault handling where still in use."}),
    ("bulk-api", "Bulk API jobs", {"purpose": "Validate job lifecycle, error files, and partial success."}),
    ("platform-events", "Event-driven integration", {
        "purpose": "Test publish/subscribe contracts and subscriber failure isolation.",
        "related": ["[../automation/platform-events.md](../automation/platform-events.md)"],
    }),
    ("change-data-capture", "CDC integration", {
        "purpose": "Validate CDC enablement, event shape, and downstream consumers.",
        "related": ["[../automation/change-data-capture.md](../automation/change-data-capture.md)"],
    }),
    ("middleware", "MuleSoft / Boomi / Informatica patterns", {
        "purpose": "Define QE responsibilities across Salesforce vs middleware vs target systems.",
        "testing": ["Contract tests at boundaries", "E2E with controlled doubles when needed", "Clear failure ownership per hop"],
    }),
    ("named-credentials", "Secure callout endpoints", {"purpose": "Test auth protocols, env mapping, and secret rotation impact."}),
    ("external-services", "Declarative OpenAPI callouts", {"purpose": "Validate External Service actions from Flow and error mapping."}),
    ("authentication", "Integration authentication", {"purpose": "Test token lifecycle and expired-credential failure modes."}),
    ("authorization", "Integration authorization", {"purpose": "Least privilege for integration users and connected apps."}),
    ("oauth", "OAuth flows for integrations", {"purpose": "Validate OAuth grant types in scope, refresh, and scope misuse negatives."}),
    ("error-handling", "Integration error patterns", {"purpose": "Ensure errors are logged, surfaced, and do not corrupt data silently."}),
    ("retry-logic", "Retry / backoff", {"purpose": "Validate retry limits, poison messages, and duplicate side effects."}),
    ("timeout-handling", "Timeouts and partial failures", {"purpose": "Test timeout behaviour and compensating actions."}),
    ("monitoring", "Integration monitoring", {"purpose": "Evidence: logs, event monitoring, middleware dashboards, alert thresholds."}),
    ("logging", "Integration logging standards", {"purpose": "What QE expects in logs for triage without exposing secrets/PII."}),
    ("api-limits", "API limit risk", {"purpose": "Validate limit awareness, bursting, and degradation behaviour."}),
    ("data-synchronization", "Sync patterns", {"purpose": "Test near-real-time vs batch sync, conflict resolution, and drift detection."}),
    ("message-queues", "Message queues overview", {"purpose": "Overview of queue-based integration testing themes (ordering, DLQ, idempotency)."}),
]

PERFORMANCE = [
    ("governor-limits", "Platform governor limits", {
        "purpose": "Teach which limits matter in scenarios and how failures present.",
        "related": [f"[Platform 4A]({REL['p4a']})"],
    }),
    ("soql-performance", "SOQL performance risk", {"purpose": "Validate query volume/cost risks in automation and integrations."}),
    ("query-selectivity", "Selective filters", {"purpose": "Advise selective filter tests and LDV query plans."}),
    ("indexing-concepts", "Index concepts for QE", {"purpose": "QE awareness of selective fields/indexes—flag architecture needs to SA."}),
    ("flow-performance", "Flow bulk/DML risk", {
        "purpose": "Test Flow bulkification and element limits under volume.",
        "related": ["[../automation/record-triggered-flows.md](../automation/record-triggered-flows.md)"],
    }),
    ("batch-processing", "Batch job performance", {"purpose": "Measure throughput, chunk failures, and restart behaviour."}),
    ("large-data-volumes", "LDV considerations", {
        "purpose": "Plan LDV for list views, roll-ups, sharing, batches, and reports.",
        "related": ["[../data/large-data-volumes.md](../data/large-data-volumes.md)"],
    }),
    ("record-locking", "Row lock errors", {"purpose": "Reproduce and mitigate lock contention in parallel updates."}),
    ("concurrent-users", "Concurrency behaviour", {"purpose": "Design concurrency scenarios for queues, inventory, approvals."}),
    ("report-performance", "Slow reports", {"purpose": "Identify timeout risks and filter/index mitigations."}),
    ("dashboard-performance", "Dashboard refresh cost", {"purpose": "Validate running user, component load, and refresh behaviour under load."}),
    ("integration-performance", "Interface performance", {"purpose": "Latency, throughput, and backpressure across integrations."}),
    ("performance-testing-considerations", "When/how to performance-test SF", {
        "purpose": "Scope performance testing realistically for multi-tenant constraints.",
    }),
    ("scalability", "Scalability themes", {"purpose": "Growth in users/data/transactions—what QE should evidence."}),
    ("performance-risks", "Performance risk catalog", {"purpose": "Catalog high-frequency performance risks for RAID and planning."}),
]

RELEASE = [
    ("release-planning", "Release planning for QE", {
        "purpose": "Define QE inputs to release plans: scope, risk, environments, evidence.",
    }),
    ("deployment-strategy", "Deployment strategy awareness", {
        "purpose": "How deploy approach (big-bang, phased, toggle) changes test strategy.",
    }),
    ("change-sets", "Change sets (knowledge)", {
        "purpose": "QE risks with change sets: omissions, order, and validation gaps.",
    }),
    ("devops-center", "DevOps Center overview", {
        "purpose": "QE use of work items/pipelines as impact and evidence inputs.",
    }),
    ("ci-cd-overview", "CI/CD overview for QE", {
        "purpose": "Where automated quality gates fit; what remains manual/UAT.",
    }),
    ("deployment-validation", "Pre/during deploy validation", {
        "purpose": "Evidence for successful metadata/data deploy validation.",
    }),
    ("post-deployment-validation", "Immediate PPV", {
        "purpose": "Structured post-deploy: smoke, key journeys, integrations, permissions.",
    }),
    ("smoke-testing", "Release smoke pack", {
        "purpose": "Minimal critical-path confidence after deploy.",
        "related": ["[../smoke-testing.md](../smoke-testing.md)"],
    }),
    ("sanity-testing", "Narrow change confirmation", {
        "purpose": "Targeted sanity around the change vs full regression.",
        "related": ["[../sanity-testing.md](../sanity-testing.md)"],
    }),
    ("regression-planning", "Release regression planning", {
        "purpose": "Release-level regression packs and risk-based selection.",
        "related": [f"[Regression Planning]({REL['reg']})"],
    }),
    ("release-readiness", "Release readiness assessment", {
        "purpose": "Evidence checklist for exit criteria, open risks, and sign-off inputs.",
    }),
    ("go-no-go-decision", "Go/No-Go evidence", {
        "purpose": "Structure Go/No-Go recommendation from test evidence and residual risk.",
    }),
    ("rollback-strategy", "Rollback / backout", {
        "purpose": "Validate backout plan tests: data integrity and feature restore.",
    }),
    ("cutover-planning", "Cutover weekend QE role", {
        "purpose": "QE activities during cutover: checks, war-room, decision logs.",
    }),
    ("hypercare", "Post-go-live hypercare", {
        "purpose": "Monitoring, triage SLAs, and feedback into defect intelligence.",
    }),
    ("production-verification", "Production verification checks", {
        "purpose": "Post-go-live verification themes distinct from full UAT re-run.",
    }),
    ("production-readiness", "Production readiness (knowledge)", {
        "purpose": "Knowledge-only production readiness themes for QE—gates, evidence, residual risk (no playbook templates).",
        "testing": ["Entry/exit criteria awareness", "Open defect policy", "Monitoring and rollback readiness", "Support model handoff"],
        "practices": ["This is knowledge for reasoning—not a formal production-readiness playbook (Sprint later / BA OCM as applicable)"],
    }),
    ("environment-strategy", "Env strategy for quality", {
        "purpose": "How sandbox strategy affects test confidence and data realism.",
    }),
    ("environment-refresh", "Refresh impacts on testing", {
        "purpose": "Validate post-refresh reconfig, credentials, and smoke after refresh.",
    }),
    ("feature-toggles", "Feature toggles overview", {
        "purpose": "Overview of toggle-driven release testing (on/off, partial cohorts).",
    }),
]

INDUSTRY = [
    ("utilities", "Utilities programs", {
        "purpose": "Starter QE industry lens for utilities on Salesforce.",
        "key_components": ["Service Cloud / Utilities Cloud themes", "CIS/MDM/OMS integrations often critical", "Field + portal personas"],
        "related": ["[../clouds/utilities-cloud.md](../clouds/utilities-cloud.md)"],
    }),
    ("retail", "Retail / consumer", {
        "purpose": "Starter QE lens for retail CRM/service and omnichannel.",
    }),
    ("banking", "Banking / FS", {
        "purpose": "Starter QE lens; confirm regulatory constraints with Compliance.",
        "related": ["[../clouds/financial-services-cloud.md](../clouds/financial-services-cloud.md)"],
        "practices": ["Never invent KYC/AML rules"],
    }),
    ("insurance", "Insurance", {
        "purpose": "Starter QE lens for policy/claim-oriented Salesforce programs.",
    }),
    ("healthcare", "Healthcare", {
        "purpose": "Starter QE lens; PHI/HIPAA are Legal-confirmed constraints.",
        "related": ["[../clouds/health-cloud.md](../clouds/health-cloud.md)"],
    }),
    ("manufacturing", "Manufacturing / dealer", {
        "purpose": "Starter QE lens for dealer, asset, and supply-chain adjacent CRM.",
        "related": ["[../clouds/manufacturing-cloud.md](../clouds/manufacturing-cloud.md)"],
    }),
    ("telecommunications", "Telecom", {
        "purpose": "Starter QE lens for provisioning/activation-adjacent CRM/service.",
    }),
    ("public-sector", "Public sector / constituent", {
        "purpose": "Starter QE lens for case/grant/constituent service patterns.",
    }),
    ("energy", "Energy (adjacent to utilities)", {
        "purpose": "Starter QE lens for energy retail/generation CRM themes overlapping utilities patterns.",
        "related": ["[utilities.md](utilities.md)", "[../clouds/utilities-cloud.md](../clouds/utilities-cloud.md)"],
    }),
    ("consumer-goods", "Consumer goods", {
        "purpose": "Starter QE lens for CG retail execution and account management themes.",
        "related": ["[../clouds/consumer-goods-cloud.md](../clouds/consumer-goods-cloud.md)"],
    }),
]

FOLDERS = [
    ("clouds", "Clouds Knowledge", "Salesforce Cloud product knowledge for enterprise QE decisions.",
     "Cloud encyclopedias from a QE lens: processes, objects, testing, regression, production risk. Platform depth remains in Sprint 4A.", CLOUDS),
    ("managed-packages", "Managed Package Knowledge", "Package and upgrade quality risk for subscriber orgs.",
     "Managed/unlocked packages, namespaces, packaged metadata, upgrade/regression, vendor coordination.", PACKAGES),
    ("integration", "Integration Knowledge", "Enterprise integration patterns for Salesforce QE.",
     "APIs, events, middleware, auth, errors/retries, monitoring, sync, API limits.", INTEGRATION),
    ("performance", "Performance Knowledge", "Performance and scalability risk for Salesforce QE.",
     "Governors, SOQL, LDV, locking, Flow/batch/report/integration performance.", PERFORMANCE),
    ("release", "Release Knowledge", "Release engineering and production readiness knowledge for QE.",
     "Planning, deploy, smoke/sanity, readiness, Go/No-Go, rollback, cutover, hypercare, env strategy. Knowledge only—no playbooks/templates.", RELEASE),
    ("industry", "Industry Knowledge", "Industry starter packs for enterprise QE scenario design.",
     "Utilities through Consumer Goods: processes, integrations, regression hotspots, production risks.", INDUSTRY),
]


def main() -> None:
    folder_names = [f[0] for f in FOLDERS]
    count = 0
    for i, (folder, title, purpose, scope, articles) in enumerate(FOLDERS):
        folder_path = KNOWLEDGE / folder
        folder_path.mkdir(parents=True, exist_ok=True)

        keep = {a[0] + ".md" for a in articles} | {"README.md"}
        for p in folder_path.glob("*.md"):
            if p.name not in keep:
                p.unlink()
                print(f"Removed {folder}/{p.name}")

        norm = []
        for item in articles:
            slug, blurb = item[0], item[1]
            meta = merge(DEFAULTS, item[2] if len(item) > 2 else {})
            meta.setdefault("title", titleize(slug))
            norm.append((slug, blurb, meta))

        prev_f = folder_names[i - 1] if i > 0 else None
        next_f = folder_names[i + 1] if i < len(folder_names) - 1 else None
        (folder_path / "README.md").write_text(
            folder_readme(folder, title, purpose, scope, [(s, b) for s, b, _ in norm], prev_f, next_f),
            encoding="utf-8",
        )
        count += 1

        slugs = [s for s, _, _ in norm]
        for idx, (slug, _, meta) in enumerate(norm):
            (folder_path / f"{slug}.md").write_text(
                render_doc(folder, slug, meta, nav_for(slugs, idx)),
                encoding="utf-8",
            )
            count += 1

    print(f"Wrote {count} files for {SPRINT}")


if __name__ == "__main__":
    main()
