#!/usr/bin/env python3
"""Generate Sprint 4A — Salesforce Platform Foundation (QE Knowledge Base)."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
VERSION = "0.5.1"
DATE = "2026-07-17"
SPRINT = "Sprint 4A"

REL = {
    "ra": "../requirement-analysis.md",
    "td": "../test-design-engine.md",
    "cov": "../test-coverage-model.md",
    "risk": "../risk-based-testing.md",
    "reg": "../regression-planning.md",
    "brain": "../../brain/README.md",
    "skill": "../../skill.md",
}


def titleize(slug: str) -> str:
    special = {
        "mfa": "MFA",
        "pii-considerations": "PII Considerations",
        "gdpr-awareness": "GDPR Awareness",
        "omni-channel-routing": "Omni-Channel Routing",
        "salesforce-platform-overview": "Salesforce Platform Overview",
        "multi-tenant-architecture": "Multi-Tenant Architecture",
        "metadata-driven-architecture": "Metadata-Driven Architecture",
        "configuration-vs-customization": "Configuration vs Customization",
        "object-level-security": "Object Level Security",
        "field-level-security": "Field Level Security",
        "organization-wide-defaults": "Organization-Wide Defaults",
        "large-data-volumes": "Large Data Volumes",
        "change-data-capture": "Change Data Capture",
        "apex-triggers": "Apex Triggers",
        "record-triggered-flows": "Record-Triggered Flows",
        "auto-launched-flows": "Auto-Launched Flows",
        "screen-flows": "Screen Flows",
        "scheduled-flows": "Scheduled Flows",
    }
    return special.get(slug, slug.replace("-", " ").title())


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {i}" for i in items)


def merge(base: dict, override: dict | None) -> dict:
    out = {k: (list(v) if isinstance(v, list) else v) for k, v in base.items()}
    if not override:
        return out
    for k, v in override.items():
        out[k] = v
    return out


DEFAULTS = {
    "purpose": "Explain this Salesforce capability from an enterprise Quality Engineering perspective so the AI can decide what to test, why, and what risks and regression apply.",
    "business_context": [
        "Business outcomes depend on correct platform behaviour for the right personas and data.",
        "Defects often appear as wrong visibility, silent automation side effects, or data integrity breaks—not only UI errors.",
    ],
    "overview": [
        "Salesforce exposes this capability as configurable metadata (and sometimes data) on a multi-tenant platform.",
        "Confirm edition, licenses, and org-specific configuration before asserting behaviour.",
    ],
    "architecture": [
        "Interacts with data model, UI, automation order of execution, security, and APIs.",
        "Changes are typically metadata deployments with environment promotion risk.",
    ],
    "business_usage": [
        "Supports enterprise CRM / service / industry processes on Salesforce.",
        "Used by named personas with least-privilege access expectations.",
    ],
    "req_analysis": [
        f"Map story AC to this component using [{REL['ra']}]({REL['ra']})",
        "Ask: which objects/fields/personas/channels (UI vs API) are in scope?",
        "Flag untestable language and missing negative/permission paths.",
    ],
    "testing": [
        f"Design scenario objectives via [{REL['td']}]({REL['td']}) before detailed cases",
        "Cover happy path, negative, boundary, and persona/permission paths",
        "Evidence: persona, data, environment, expected vs actual",
    ],
    "functional": [
        "Observable outcomes match acceptance criteria for in-scope personas",
        "State after save/action matches business rules",
    ],
    "negative": [
        "Unauthorized persona cannot complete restricted action",
        "Invalid/missing data is blocked with a clear, testable message",
    ],
    "boundary": [
        "Field length, numeric edges, date edges, picklist subsets, null/blank",
        "Volume edges where platform limits may surface (document assumptions)",
    ],
    "regression": [
        f"Apply [{REL['reg']}]({REL['reg']}) — In / Out / Conditional scope",
        "Neighbor automation, layouts, reports, and integrations that consume the same fields",
    ],
    "automation_opp": [
        "API-level checks for deterministic rules (preferred over brittle UI)",
        "Smoke candidates for high-frequency create/update paths",
        "Do not automate unstable exploratory or one-off migration validation",
    ],
    "security": [
        "Validate CRUD/FLS/sharing for every persona named in the requirement",
        "Treat View All / Modify All / guest access as high-risk exceptions",
    ],
    "performance": [
        "Consider bulk behaviour and governor-limit failure modes when volume is in scope",
        "LDV and selective queries matter for list views, roll-ups, sharing, and batches",
    ],
    "production": [
        "Silent behaviour change after deploy (no error, wrong outcome)",
        "Permission or data drift between sandboxes and production",
    ],
    "defects": [
        "Works for System Admin; fails for end-user persona",
        "Order-of-execution conflict between automation components",
        "Missing regression on neighbor reports/integrations",
    ],
    "root_causes": [
        "Incomplete requirement analysis (missing persona, data, or exception path)",
        "Environment config drift (FLS, assignment, CMDT, custom settings)",
        "Assumed standard behaviour that was customized",
    ],
    "practices": [
        "Analyse requirements and Salesforce impact before writing detailed cases",
        "Prefer platform-native fit when confirmed; document gaps explicitly",
        "Keep evidence packs suitable for Go/No-Go and audit",
        f"Reason with [{REL['brain']}]({REL['brain']}) and [{REL['skill']}]({REL['skill']})",
    ],
    "interview": [
        "How would you decide regression scope when this component changes?",
        "What negative and permission scenarios are mandatory?",
        "Which failures are common in production and how do you detect them?",
    ],
    "references": [
        "Salesforce Help / Release Notes (org-confirmed edition)",
        "ISTQB: risk-based testing, equivalence partitioning, boundary value analysis",
        f"[Requirement Analysis]({REL['ra']}) · [Test Design Engine]({REL['td']})",
    ],
}


def render_doc(folder: str, slug: str, meta: dict, nav: dict) -> str:
    title = meta.get("title") or titleize(slug)
    purpose = meta.get("purpose", DEFAULTS["purpose"])
    related = meta.get("related", []) + [
        f"[Requirement Analysis]({REL['ra']})",
        f"[Test Design Engine]({REL['td']})",
        f"[QE Brain]({REL['brain']})",
        f"[Risk-Based Testing]({REL['risk']})",
        "[README.md](README.md)",
        "[../README.md](../README.md)",
    ]

    def sec(key: str, heading: str) -> str:
        val = meta.get(key, DEFAULTS[key])
        if isinstance(val, str):
            body = val
        else:
            body = bullets(val)
        return f"## {heading}\n\n{body}\n"

    body = f"""---
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
  - salesforce-quality-engineering/brain/README.md
keywords: [{slug}, salesforce, quality-engineering, platform-foundation]
tags: [knowledge, sprint-4a, {folder}]
---

# {title}

**Purpose:** {purpose}

**Scope:** {SPRINT} Platform Foundation — QE lens (analysis, test design, regression, automation readiness, production validation). Not Admin/Developer how-to.

**Owner:** QE Practice Lead

**Version:** {VERSION}

**Status:** Draft ({SPRINT})

---

{sec("purpose", "Purpose")}
{sec("business_context", "Business Context")}
{sec("overview", "Salesforce Overview")}
{sec("architecture", "Architecture")}
{sec("business_usage", "Business Usage")}
{sec("req_analysis", "Requirement Analysis Guidance")}
{sec("testing", "Testing Considerations")}
{sec("functional", "Functional Testing")}
{sec("negative", "Negative Testing")}
{sec("boundary", "Boundary Testing")}
{sec("regression", "Regression Testing")}
{sec("automation_opp", "Automation Opportunities")}
{sec("security", "Security Considerations")}
{sec("performance", "Performance Considerations")}
{sec("production", "Production Risks")}
{sec("defects", "Common Defects")}
{sec("root_causes", "Common Root Causes")}
{sec("practices", "Best Practices")}
{sec("interview", "Interview Questions")}
{sec("references", "References")}

## Related Documents

{bullets(related)}

## Navigation

- **Previous:** [{nav['prev_label']}]({nav['prev']})
- **Next:** [{nav['next_label']}]({nav['next']})
- **See Also:** [README.md](README.md) · [Test Design Engine]({REL['td']})

## Future Enhancements

- Deepen industry examples in Sprint 4B where cloud-specific
- Link Sprint 5 case templates to scenario objectives herein
"""
    # purpose appears twice (header + section) - user asked for Purpose as section; OK
    # Fix: first sec("purpose") duplicates - the DEFAULTS purpose key works
    return body


def folder_readme(folder: str, title: str, purpose: str, scope: str, articles: list[tuple[str, str]], prev_f: str | None, next_f: str | None) -> str:
    rows = "\n".join(f"| [{titleize(s)}]({s}.md) | {b} |" for s, b in articles)
    prev = f"[{prev_f}/](../{prev_f}/README.md)" if prev_f else "[../README.md](../README.md)"
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
keywords: [{folder}, knowledge-index, sprint-4a]
tags: [knowledge, sprint-4a, {folder}]
---

# {title}

## Purpose

{purpose}

## Scope

{scope}

**In scope ({SPRINT}):** This folder.  
**Out of scope ({SPRINT}):** Clouds, industries, CPQ, Agentforce, OmniStudio, managed packages, production-support deep dives → **Sprint 4B**.

## Available Documents

| Document | Focus |
|----------|-------|
{rows}

## Navigation

- **Previous:** {prev}
- **Next:** {nxt}
- **See Also:** [{REL['skill']}]({REL['skill']}) · [../README.md](../README.md)

## Related Knowledge

- [Requirement Analysis]({REL['ra']})
- [Test Design Engine]({REL['td']})
- [QE Brain]({REL['brain']})
- [Risk-Based Testing]({REL['risk']})
- [Regression Planning]({REL['reg']})
- Sibling foundation folders: [platform](../platform/README.md) · [metadata](../metadata/README.md) · [automation](../automation/README.md) · [security](../security/README.md) · [data](../data/README.md)
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

PLATFORM = [
    ("salesforce-platform-overview", "Platform building blocks and QE impact model", {
        "purpose": "Give QE a coherent mental model of Salesforce so every requirement maps to objects, UI, automation, security, data, and integrations.",
        "architecture": [
            "Multi-tenant CRM application platform: data + UI + automation + security + APIs + analytics",
            "Metadata-driven configuration promoted across environments",
            "Quality risk concentrates where metadata, automation, and persona permissions intersect",
        ],
        "related": ["[Multi-Tenant Architecture](multi-tenant-architecture.md)", "[Metadata-Driven Architecture](metadata-driven-architecture.md)"],
    }),
    ("multi-tenant-architecture", "Shared platform implications for testing and risk", {
        "purpose": "Explain multi-tenancy impacts on isolation, limits, performance testing realism, and production risk.",
        "architecture": [
            "Orgs share infrastructure with logical isolation",
            "Governor limits and noisy-neighbor constraints shape what performance tests can prove",
            "Feature availability varies by edition/license—never invent capabilities",
        ],
        "performance": [
            "Do not assume dedicated hardware performance characteristics",
            "Focus on selective queries, bulkification, and user-concurrency at business volumes",
        ],
        "production": [
            "Limit exceptions and timeouts under peak load",
            "Release windows and maintenance awareness for cutover planning",
        ],
    }),
    ("metadata-driven-architecture", "Why almost every change is metadata", {
        "purpose": "Connect metadata-driven design to impact analysis, deploy validation, and regression selection.",
        "related": ["[../metadata/README.md](../metadata/README.md)", "[../metadata/metadata-impact-analysis.md](../metadata/metadata-impact-analysis.md)"],
        "req_analysis": [
            "Translate stories into likely metadata types early",
            "Ask which environments and promotion path will carry the change",
        ],
    }),
    ("standard-objects", "Core CRM standard objects", {
        "purpose": "Guide QE on standard object semantics, extensions, and failure modes.",
        "related": ["[Custom Objects](custom-objects.md)", "[Record Types](record-types.md)"],
    }),
    ("custom-objects", "Custom schema objects", {
        "purpose": "Cover custom object CRUD, sharing, UI, and automation surfaces.",
    }),
    ("fields", "Field types and constraints", {
        "purpose": "Map field requirements to validation, FLS, layout, formula, and history tracking.",
        "boundary": ["Max length, precision/scale, unique/external ID collisions", "Picklist restricted vs unrestricted", "Default value vs null on API insert"],
    }),
    ("relationships", "Relationship model overview", {
        "purpose": "Orient QE to relationship types before deep lookup/MD articles.",
        "related": ["[Lookup Relationships](lookup-relationships.md)", "[Master-Detail Relationships](master-detail-relationships.md)"],
    }),
    ("lookup-relationships", "Lookup relationship testing", {
        "purpose": "Validate optional/required lookups, filters, and delete constraints.",
        "functional": ["Lookup filter true/false paths", "Clearing optional lookup", "Related list visibility"],
        "negative": ["Invalid Id", "Lookup filter blocks intended parent", "Delete parent when children exist (per setting)"],
    }),
    ("master-detail-relationships", "Master-detail relationship testing", {
        "purpose": "Validate ownership cascade, roll-up eligibility, and cascade delete risk.",
        "related": ["[Roll-Up Summary Fields](roll-up-summary-fields.md)"],
        "security": ["Child access often inherits master—validate persona visibility carefully"],
    }),
    ("record-types", "Record type variation", {
        "purpose": "Test record-type assignment, picklist subsets, layouts, and process differences.",
    }),
    ("business-processes", "Sales/Support process stages", {
        "purpose": "Validate stage paths and closed reasons against AC and reporting.",
    }),
    ("page-layouts", "Layout assignment and requiredness", {
        "purpose": "Verify layout-driven required fields and related lists per persona.",
        "related": ["[Lightning Record Pages](lightning-record-pages.md)"],
    }),
    ("lightning-record-pages", "Lightning App Builder pages", {
        "purpose": "Test component visibility, dynamic display, and app/profile activation.",
    }),
    ("compact-layouts", "Highlight panel / mobile compact fields", {
        "purpose": "Confirm compact fields support triage without leaking restricted data.",
    }),
    ("quick-actions", "Object quick actions", {
        "purpose": "Test action field sets, prefill, publisher layout, and success behaviour.",
    }),
    ("global-actions", "Global actions", {
        "purpose": "Validate global action availability, defaults, and permission prerequisites.",
    }),
    ("formula-fields", "Calculated fields", {
        "purpose": "Test formula correctness, null handling, and downstream consumers.",
        "performance": ["Compile size / reference limits", "Avoid assuming real-time heavy cross-object formulas at LDV"],
    }),
    ("roll-up-summary-fields", "Master-detail roll-ups", {
        "purpose": "Validate roll-up filters, recalculation timing, and LDV risk.",
        "related": ["[Master-Detail Relationships](master-detail-relationships.md)", "[../data/large-data-volumes.md](../data/large-data-volumes.md)"],
    }),
    ("external-objects", "Salesforce Connect external objects", {
        "purpose": "Test availability, latency, CRUD limits, and auth failure modes.",
    }),
    ("big-objects", "Big Object patterns", {
        "purpose": "Validate insert/query patterns and reporting limitations.",
    }),
    ("custom-metadata-types", "CMDT configuration", {
        "purpose": "Treat CMDT as testable configuration consumed by automation.",
        "regression": ["Missing CMDT in lower envs", "Package upgrade value changes"],
    }),
    ("custom-settings", "Hierarchy/list custom settings", {
        "purpose": "Validate hierarchy overrides and environment seeding of settings.",
        "practices": ["Prefer CMDT for new packaged config; document remaining custom settings debt"],
    }),
]

METADATA = [
    ("metadata-overview", "Metadata as the QE impact surface", {
        "purpose": "Teach QE to think in metadata types for coverage and deploy risk.",
    }),
    ("metadata-types", "Common metadata types and QE meaning", {
        "purpose": "Catalog major metadata types QE must recognize in impact analysis.",
        "overview": [
            "Examples: CustomObject, CustomField, Layout, FlexiPage, Flow, ValidationRule, Profile, PermissionSet, RemoteSiteSetting, NamedCredential, Report, Dashboard",
            "Map each story change to one or more types before designing regression",
        ],
    }),
    ("metadata-dependencies", "Reference and dependency risk", {
        "purpose": "Highlight broken references, inactive versions, and cross-component dependency failures.",
    }),
    ("deployment-considerations", "Deploy validation from a QE lens", {
        "purpose": "Connect deployment mechanics to smoke, PPV, and Go/No-Go evidence.",
        "testing": ["Validate deploy success AND functional smoke", "Confirm profiles/permission sets and assignments if in package", "Watch for destructive changes and renamed API names"],
    }),
    ("metadata-relationships", "How metadata components reference each other", {
        "purpose": "Explain reference graphs (field→VR→Flow→Layout→Report) for regression neighbor discovery.",
    }),
    ("configuration-vs-customization", "Config vs custom and test depth", {
        "purpose": "Guide QE on risk/depth differences between declarative config and code customization.",
        "req_analysis": ["Classify Standard / Config / Extend / Gap for each need (align with BA fit-gap language)", "Custom Apex generally needs stronger negative, bulk, and regression coverage"],
    }),
    ("metadata-impact-analysis", "Change → component → scenario model", {
        "purpose": "Provide a repeatable impact model from metadata diff to test scope.",
        "testing": [
            "Classify: data model / UI / automation / security / integration / analytics",
            "Identify consumers of changed fields",
            "Select smoke vs deep regression using risk",
        ],
        "related": ["[Regression Impact Analysis](regression-impact-analysis.md)"],
    }),
    ("metadata-testing-strategy", "How to test metadata changes", {
        "purpose": "Define layered strategy: static review, config validation, functional, persona, regression.",
    }),
    ("regression-impact-analysis", "Regression scope from metadata", {
        "purpose": "Translate metadata impact into In/Out/Conditional regression packs.",
        "related": [f"[Regression Planning]({REL['reg']})"],
    }),
    ("metadata-comparison", "Comparing metadata across orgs/releases", {
        "purpose": "Use comparison (manifest diffs, DevOps center, unlocked package diffs) as QE input—not as pass/fail alone.",
    }),
    ("metadata-migration", "Moving metadata across environments", {
        "purpose": "Validate promotion path, dependency order, and post-migrate functional checks.",
    }),
    ("metadata-validation", "Validation before/after deploy", {
        "purpose": "Define validation evidence: compile, retrieve, smoke journeys, permission spot checks.",
    }),
    ("metadata-best-practices", "Enterprise metadata hygiene for quality", {
        "purpose": "Document practices that reduce defect escape: naming, inactive cleanup, env parity.",
    }),
    ("metadata-risks", "Metadata risk catalog", {
        "purpose": "Catalog high-frequency metadata risks for RAID and test planning.",
        "production": ["Partial deploy leaving inconsistent state", "Profile/FLS omitted from package", "Hard-coded IDs in Flow/Apex"],
    }),
]

AUTOMATION = [
    ("validation-rules", "Declarative validation", {
        "purpose": "QE guidance for VR formulas, bypass patterns, and message testability.",
        "architecture": ["Fires on save before many after-save automations—understand order of execution", "May be bypassed by specific integration designs—confirm explicitly"],
        "related": ["[../validation-rule-testing.md](../validation-rule-testing.md)"],
    }),
    ("record-triggered-flows", "Before/after save and async Flow", {
        "purpose": "Validate entry criteria, recursion controls, async paths, and bulk assumptions.",
        "architecture": ["Before-save vs after-save vs async paths have different testing implications", "Coexistence with Apex triggers is a primary defect source"],
        "related": ["[../flow-testing.md](../flow-testing.md)"],
    }),
    ("scheduled-flows", "Time-based Flow schedules", {
        "purpose": "Test schedule frequency, filters, bulk batches, and missed-run behaviour.",
    }),
    ("auto-launched-flows", "Invocable / autolaunched Flow", {
        "purpose": "Validate inputs/outputs, subflow contracts, and invocation from Apex/API/Flow.",
    }),
    ("screen-flows", "Guided UI Flow", {
        "purpose": "Test screens, decisions, fault paths, finish behaviour, and run permissions.",
    }),
    ("approval-processes", "Approvals", {
        "purpose": "Cover submit/approve/reject/recall, reassignment, and notification side effects.",
    }),
    ("workflow-rules", "Legacy workflow", {
        "purpose": "Test remaining Workflow Rules and double-fire risk during Flow migration.",
    }),
    ("process-builder", "Legacy Process Builder", {
        "purpose": "Validate remaining PB and coexistence with Flow/Apex.",
    }),
    ("apex-triggers", "Trigger logic", {
        "purpose": "QE focus on events, bulkification, recursion, and Flow coexistence.",
    }),
    ("batch-apex", "Batchable jobs", {
        "purpose": "Test scope queries, chunk failures, monitoring, and restart behaviour.",
    }),
    ("queueable-apex", "Queueable async", {
        "purpose": "Validate enqueue conditions, chaining limits, and failure observation.",
    }),
    ("scheduled-apex", "Cron Apex", {
        "purpose": "Confirm schedule registration and timezone/next-fire assumptions.",
    }),
    ("platform-events", "Platform Events automation", {
        "purpose": "Test publish/subscribe, replay, and subscriber failure isolation.",
    }),
    ("change-data-capture", "CDC", {
        "purpose": "Validate enablement, event shape, and downstream consumer behaviour.",
    }),
    ("duplicate-rules", "Duplicate prevention/allow", {
        "purpose": "Validate alert vs block, matching interplay, and bypass roles.",
        "related": ["[Matching Rules](matching-rules.md)", "[../data/duplicate-rules.md](../data/duplicate-rules.md)"],
    }),
    ("matching-rules", "Matching criteria for duplicates", {
        "purpose": "Test match strength and false positive/negative tradeoffs.",
        "related": ["[../data/matching-rules.md](../data/matching-rules.md)"],
    }),
    ("assignment-rules", "Lead/Case assignment", {
        "purpose": "Validate rule order, criteria, default owner/queue, and API bypass behaviour.",
        "architecture": ["Order of rules matters; first match typically wins", "Assignment on create vs update paths differ—confirm requirement"],
    }),
    ("escalation-rules", "Case escalation", {
        "purpose": "Test age criteria, business hours, escalation actions, and re-escalation.",
    }),
    ("auto-response-rules", "Auto-response emails", {
        "purpose": "Validate rule criteria, templates, and when responses must NOT send.",
    }),
    ("omni-channel-routing", "Omni-Channel routing overview", {
        "purpose": "Overview-only QE guidance for routing/work distribution (deep Service Cloud in Sprint 4B).",
        "overview": [
            "Omni-Channel routes work items to agents based on capacity and skills",
            "Sprint 4A covers testing themes only; Service Cloud depth is Sprint 4B",
        ],
        "testing": ["Presence/capacity changes", "Skill mismatch", "Queue overflow / backlog behaviour", "Permission to own routed work"],
    }),
]

SECURITY = [
    ("profiles", "Baseline persona access", {
        "purpose": "Test profile CRUD/FLS/app access as least-privilege baseline.",
        "related": ["[Permission Sets](permission-sets.md)", "[../security-testing.md](../security-testing.md)"],
    }),
    ("permission-sets", "Additive access", {
        "purpose": "Validate assignment/revoke effects and additive grants.",
        "related": ["[../permission-set-testing.md](../permission-set-testing.md)"],
    }),
    ("permission-set-groups", "Bundled permission sets", {
        "purpose": "Test mute permissions and persona packaging via groups.",
    }),
    ("field-level-security", "Field visibility/editability", {
        "purpose": "Ensure FLS matches persona needs across UI, API, reports, and list views.",
    }),
    ("object-level-security", "Object CRUD and View All/Modify All", {
        "purpose": "Validate object-level CRUD and escalate View All/Modify All as high risk.",
        "related": ["[Field Level Security](field-level-security.md)"],
    }),
    ("role-hierarchy", "Role-based visibility", {
        "purpose": "Validate hierarchy visibility and Grant Access Using Hierarchies.",
    }),
    ("sharing-rules", "Criteria/owner sharing", {
        "purpose": "Test share expansion/revocation when criteria change.",
        "related": ["[../sharing-security-testing.md](../sharing-security-testing.md)"],
    }),
    ("manual-sharing", "Ad-hoc shares", {
        "purpose": "Confirm manual share create/revoke and UI availability.",
    }),
    ("public-groups", "Group membership", {
        "purpose": "Validate membership ripple to sharing, queues, and list views.",
    }),
    ("queues", "Queue ownership", {
        "purpose": "Test queue membership, assignment, and access to queued records.",
    }),
    ("organization-wide-defaults", "OWD baseline", {
        "purpose": "Treat OWD changes as high regression risk across the org.",
    }),
    ("restriction-rules", "Negative access filters", {
        "purpose": "Test restriction filters and coexistence with sharing grants.",
    }),
    ("territory-management", "Territory management overview", {
        "purpose": "Overview of territory-based visibility for QE impact (confirm licensed model).",
        "overview": ["Territory models affect Account/Opportunity visibility in many sales orgs", "Confirm Enterprise Territory Management vs legacy—do not invent model details"],
        "testing": ["User in/out of territory", "Account alignment changes", "Forecast/visibility side effects"],
    }),
    ("login-policies", "Login IP/hours controls", {
        "purpose": "Validate login restrictions without locking out test/integration users unexpectedly.",
    }),
    ("session-policies", "Session security settings", {
        "purpose": "Confirm session timeout and high-assurance session requirements.",
    }),
    ("mfa", "Multi-factor authentication", {
        "purpose": "Validate MFA enforcement, exemptions, and break-glass for test users.",
    }),
    ("audit-trail", "Setup Audit Trail", {
        "purpose": "Use Setup Audit Trail as investigation/deploy evidence—not as functional AC alone.",
        "related": ["[../data/audit-trail.md](../data/audit-trail.md)"],
    }),
    ("login-history", "Login History monitoring", {
        "purpose": "QE use of Login History for security incidents and access validation evidence.",
    }),
    ("field-history-tracking", "Field history for security/audit", {
        "purpose": "Validate tracked fields and history visibility for audit scenarios.",
        "related": ["[../data/field-history-tracking.md](../data/field-history-tracking.md)"],
    }),
]

DATA = [
    ("data-model", "Enterprise data model for QE", {
        "purpose": "Frame objects/relationships/fields as a testable data model for journeys and integrity.",
        "related": ["[../platform/relationships.md](../platform/relationships.md)", "[Referential Integrity](referential-integrity.md)"],
    }),
    ("data-quality", "Completeness, accuracy, consistency", {
        "purpose": "Define DQ checks QE can evidence in UAT and hypercare.",
    }),
    ("data-validation", "Validation of data rules", {
        "purpose": "Connect VR, requiredness, duplicates, and integration validation into a data validation strategy.",
        "related": ["[../automation/validation-rules.md](../automation/validation-rules.md)"],
    }),
    ("data-import", "Import paths", {"purpose": "Validate mapping, partial success, and duplicate handling on import."}),
    ("data-export", "Export paths", {"purpose": "Confirm export completeness, encoding, and access controls."}),
    ("data-loader", "Data Loader / bulk tools", {"purpose": "Test upsert keys, error CSVs, and batch sizes."}),
    ("duplicate-rules", "Duplicate rules (data lens)", {
        "purpose": "Data-quality view of duplicate prevention during entry and migration.",
        "related": ["[../automation/duplicate-rules.md](../automation/duplicate-rules.md)"],
    }),
    ("matching-rules", "Matching rules (data lens)", {
        "purpose": "Data-quality view of matching accuracy and migration false matches.",
        "related": ["[../automation/matching-rules.md](../automation/matching-rules.md)"],
    }),
    ("field-history-tracking", "Field history (data lens)", {
        "purpose": "Validate history capture for business-critical fields.",
        "related": ["[../security/field-history-tracking.md](../security/field-history-tracking.md)"],
    }),
    ("audit-trail", "Audit trail (data/governance lens)", {
        "purpose": "Evidence setup changes affecting data behaviour.",
        "related": ["[../security/audit-trail.md](../security/audit-trail.md)"],
    }),
    ("recycle-bin", "Soft delete and restore", {
        "purpose": "Test delete → recycle bin → restore integrity and related-record behaviour.",
        "negative": ["Restore without parent", "Hard delete irreversibility where applicable"],
    }),
    ("data-archiving", "Archive patterns", {
        "purpose": "Validate archive criteria, access to archived data, and reporting impact.",
    }),
    ("data-retention", "Retention policies", {
        "purpose": "Frame retention testing; confirm legal/policy requirements with Compliance—do not invent regulations.",
    }),
    ("data-migration-validation", "Migration cutover validation", {
        "purpose": "Reconcile volumes, keys, relationships, and sample journeys post-migration.",
    }),
    ("data-reconciliation", "Source vs Salesforce balances", {
        "purpose": "Define reconciliation queries and tolerance rules.",
    }),
    ("test-data-management", "TDM for sandboxes", {
        "purpose": "Advise synthetic vs masked data, referential integrity, and persona packs.",
    }),
    ("data-masking", "Sandbox masking", {
        "purpose": "Validate masking completeness for sensitive data and broken-reference risks.",
    }),
    ("pii-considerations", "PII handling for QE", {
        "purpose": "Guide PII minimization in test data and evidence packs; confirm classifications with the program.",
        "practices": ["Never put real PII in prompts, repos, or shared evidence without approval", "Prefer synthetic or masked data in lower environments"],
    }),
    ("gdpr-awareness", "GDPR awareness for QE", {
        "purpose": "Awareness-only: subject rights and retention themes affecting test design—confirm with Legal; do not invent legal advice.",
        "req_analysis": ["Flag stories implying erasure, export, or consent without Legal confirmation", "Mark regulatory claims as TBC with Compliance"],
    }),
    ("data-integrity", "Integrity across processes", {
        "purpose": "Ensure multi-step processes leave consistent object graphs.",
    }),
    ("referential-integrity", "Parent-child integrity", {
        "purpose": "Validate relationship constraints, orphans, and cascade behaviour.",
        "related": ["[../platform/lookup-relationships.md](../platform/lookup-relationships.md)", "[../platform/master-detail-relationships.md](../platform/master-detail-relationships.md)"],
    }),
    ("large-data-volumes", "LDV for data testing", {
        "purpose": "Plan LDV scenarios for queries, sharing, roll-ups, batches, and list views.",
        "related": ["[../performance/large-data-volumes.md](../performance/large-data-volumes.md)"],
        "performance": ["Selective filters", "Skinny tables/indexes are architecture topics—flag for SA", "Avoid unrealistic full-org clones as the only strategy"],
    }),
]

FOLDERS = [
    (
        "platform",
        "Platform Knowledge",
        "Salesforce platform foundation for enterprise Quality Engineering decisions.",
        "Platform architecture, data model building blocks, UI metadata, formulas, and configuration types—from a QE lens.",
        PLATFORM,
    ),
    (
        "metadata",
        "Metadata Knowledge",
        "Metadata awareness for impact analysis, deployment risk, and regression selection.",
        "Metadata types, dependencies, comparison, migration, validation, and risk—excluding cloud product encyclopedias (Sprint 4B).",
        METADATA,
    ),
    (
        "automation",
        "Automation Knowledge",
        "Declarative and programmatic automation technologies for QE test design and risk analysis.",
        "Validation, Flow family, legacy automation, Apex async, events, duplicate/assignment/escalation/auto-response, Omni-Channel overview.",
        AUTOMATION,
    ),
    (
        "security",
        "Security Knowledge",
        "Access control, sharing, identity, and audit surfaces for persona-based quality risk.",
        "Profiles through MFA, sharing model, territory overview, audit/login/field history—from a testing lens.",
        SECURITY,
    ),
    (
        "data",
        "Data Knowledge",
        "Enterprise data quality, migration, privacy awareness, and integrity for QE.",
        "Data model through LDV, masking, PII/GDPR awareness, reconciliation, and TDM.",
        DATA,
    ),
]


def main() -> None:
    # Remove obsolete Sprint-4-only files in these folders that are superseded/renamed
    obsolete = {
        "platform": ["dynamic-forms.md"],  # not in 4A list; keep? User didn't list it — remove to match scope
        "metadata": [
            "metadata-change-impact.md",
            "metadata-deployment-awareness.md",
        ],
        "automation": ["flows.md"],  # overview replaced by typed Flow docs
        "security": ["object-permissions.md", "data-visibility.md"],  # replaced by object-level-security
        "data": ["archiving.md", "data-privacy.md"],  # replaced by data-archiving, pii/gdpr
    }

    folder_names = [f[0] for f in FOLDERS]
    count = 0
    for i, (folder, title, purpose, scope, articles) in enumerate(FOLDERS):
        folder_path = KNOWLEDGE / folder
        folder_path.mkdir(parents=True, exist_ok=True)

        for name in obsolete.get(folder, []):
            p = folder_path / name
            if p.exists():
                p.unlink()
                print(f"Removed obsolete {folder}/{name}")

        # Also remove any leftover md not in catalog (except we only remove known obsolete)
        # Keep unknown files? Safer: rewrite catalog only; delete files not in new set for these 5 folders
        keep = {a[0] + ".md" for a in articles} | {"README.md"}
        for p in folder_path.glob("*.md"):
            if p.name not in keep:
                p.unlink()
                print(f"Removed out-of-scope {folder}/{p.name}")

        norm = []
        for slug, blurb, *rest in articles:
            meta = merge(DEFAULTS, rest[0] if rest else {})
            meta["title"] = meta.get("title") or titleize(slug)
            # purpose field: if override has purpose string, also use for header
            norm.append((slug, blurb, meta))

        prev_f = folder_names[i - 1] if i > 0 else None
        next_f = folder_names[i + 1] if i < len(folder_names) - 1 else None
        (folder_path / "README.md").write_text(
            folder_readme(folder, title, purpose, scope, [(s, b) for s, b, _ in norm], prev_f, next_f),
            encoding="utf-8",
        )
        count += 1

        slugs = [s for s, _, _ in norm]
        for idx, (slug, blurb, meta) in enumerate(norm):
            (folder_path / f"{slug}.md").write_text(
                render_doc(folder, slug, meta, nav_for(slugs, idx)),
                encoding="utf-8",
            )
            count += 1

    print(f"Wrote {count} files for {SPRINT}")


if __name__ == "__main__":
    main()
