#!/usr/bin/env python3
"""Generate Sprint 4 Salesforce QE Knowledge Base articles under knowledge/."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
VERSION = "0.5.0"
DATE = "2026-07-17"

# Cross-links to Sprint 2/3 engines (from knowledge/<folder>/)
REL_ENGINE = {
    "requirement_analysis": "../../knowledge/requirement-analysis.md",
    "test_design": "../../knowledge/test-design-engine.md",
    "coverage": "../../knowledge/test-coverage-model.md",
    "risk": "../../knowledge/risk-based-testing.md",
    "regression": "../../knowledge/regression-planning.md",
    "security_testing": "../../knowledge/security-testing.md",
    "integration_testing": "../../knowledge/integration-testing.md",
    "flow_testing": "../../knowledge/flow-testing.md",
    "vr_testing": "../../knowledge/validation-rule-testing.md",
    "sharing_testing": "../../knowledge/sharing-security-testing.md",
    "report_testing": "../../knowledge/report-testing.md",
    "api_testing": "../../knowledge/api-testing.md",
    "uat": "../../knowledge/uat-testing.md",
    "capability_map": "../../../shared/salesforce-capability-map.md",
}

# Fix relative paths - articles are under knowledge/<folder>/ so engines are ../
REL = {
    "requirement_analysis": "../requirement-analysis.md",
    "test_design": "../test-design-engine.md",
    "coverage": "../test-coverage-model.md",
    "risk": "../risk-based-testing.md",
    "regression": "../regression-planning.md",
    "security_testing": "../security-testing.md",
    "integration_testing": "../integration-testing.md",
    "flow_testing": "../flow-testing.md",
    "vr_testing": "../validation-rule-testing.md",
    "sharing_testing": "../sharing-security-testing.md",
    "report_testing": "../report-testing.md",
    "dashboard_testing": "../dashboard-testing.md",
    "api_testing": "../api-testing.md",
    "uat": "../uat-testing.md",
    "smoke": "../smoke-testing.md",
    "sanity": "../sanity-testing.md",
    "capability_map": "../../../shared/salesforce-capability-map.md",
}


def slug_title(slug: str) -> str:
    special = {
        "mfa": "MFA",
        "soql-limits": "SOQL Limits",
        "rest-apis": "REST APIs",
        "soap-apis": "SOAP APIs",
        "bulk-api": "Bulk API",
        "cpq": "CPQ",
        "go-no-go-validation": "Go / No-Go Validation",
        "revenue-cloud-cpq": "Revenue Cloud / CPQ",
        "change-data-capture": "Change Data Capture",
    }
    if slug in special:
        return special[slug]
    return slug.replace("-", " ").title()


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {i}" for i in items)


def doc_body(folder: str, slug: str, meta: dict, nav: dict) -> str:
    title = meta.get("title") or slug_title(slug)
    purpose = meta.get(
        "purpose",
        f"Explain {title} from a Quality Engineering perspective so analysis, design, and validation decisions are evidence-based.",
    )
    business = meta.get(
        "business_context",
        [
            f"{title} affects how business users complete journeys and how defects surface in production.",
            "QE must connect business outcomes to Salesforce configuration and automation behaviour.",
        ],
    )
    overview = meta.get(
        "overview",
        [
            f"Salesforce provides {title} as a platform capability used across clouds and industries.",
            "Treat product details as org-confirmed; do not invent edition-specific features.",
        ],
    )
    features = meta.get(
        "features",
        [
            "Configurable behaviour driven by metadata and permissions",
            "Impacts create/read/update/delete journeys and reporting visibility",
            "Interacts with automation, security, and integrations",
        ],
    )
    where_used = meta.get(
        "where_used",
        [
            "Enterprise Salesforce programs during discovery, build, UAT, and hypercare",
            "Impact analysis when stories change related metadata",
        ],
    )
    examples = meta.get(
        "business_examples",
        [
            "Retail: CSR updates customer preference and downstream Case routing changes",
            "Utilities: field update drives work-order eligibility or billing hold",
            "Banking: permission or validation change blocks a regulated update path",
        ],
    )
    testing = meta.get(
        "testing",
        [
            "Confirm requirement intent maps to this component before designing scenarios",
            "Cover happy path, negative path, persona/permission path, and data boundary path",
            "Validate order-of-execution interactions with related automation",
            f"Use [{REL['test_design']}]({REL['test_design']}) for scenario objectives and coverage matrix",
        ],
    )
    functional = meta.get(
        "functional",
        [
            "Observable outcome matches acceptance criteria for in-scope personas",
            "Field/object state after save matches business rules",
            "UI/API pathways produce equivalent business results where both are in scope",
        ],
    )
    negative = meta.get(
        "negative",
        [
            "Invalid input / missing required data blocked with clear message",
            "Unauthorized persona cannot complete restricted action",
            "Partial failure does not leave inconsistent record state (or is documented)",
        ],
    )
    regression = meta.get(
        "regression",
        [
            "Neighbor objects, layouts, automation, and reports that consume the same fields",
            "Sharing/visibility side effects after metadata deploy",
            f"Apply [{REL['regression']}]({REL['regression']}) for In / Out / Conditional scope",
        ],
    )
    auto_opp = meta.get(
        "automation_opportunities",
        [
            "API-level checks for deterministic rules (preferred over brittle UI)",
            "Smoke pack candidates for high-frequency create/update paths",
            "Do not automate unstable exploratory or one-off migration validation",
        ],
    )
    prod = meta.get(
        "production_risks",
        [
            "Silent behaviour change after deploy (no error, wrong outcome)",
            "Permission drift between sandboxes and production",
            "Volume/concurrency differences vs test data",
        ],
    )
    defects = meta.get(
        "common_defects",
        [
            "Requirement assumed standard behaviour that is actually custom",
            "Missing persona coverage (works for admin, fails for end user)",
            "Automation order-of-execution conflict",
            "Report/dashboard filters not updated with field changes",
        ],
    )
    practices = meta.get(
        "best_practices",
        [
            "Analyse requirements and Salesforce impact before writing detailed cases",
            "Prefer platform-native configuration over custom when fit is confirmed",
            "Keep evidence: persona, data, environment, expected vs actual",
            "Cross-link BA artifacts; do not rewrite BA requirements as QE truth",
        ],
    )
    interview = meta.get(
        "interview_tips",
        [
            f"Explain how you would test {title} without jumping to click-paths first",
            "Describe risks, regression neighbors, and automation candidates with rationale",
        ],
    )
    related = meta.get("related", [])
    related_lines = related + [
        f"[Requirement Analysis]({REL['requirement_analysis']})",
        f"[Test Design Engine]({REL['test_design']})",
        f"[Test Coverage Model]({REL['coverage']})",
        f"[Risk-Based Testing]({REL['risk']})",
        "[../README.md](../README.md)",
        f"[README.md](README.md)",
    ]

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
keywords: [{slug}, salesforce, quality-engineering]
tags: [knowledge, sprint-4, {folder}]
---

# {title}

**Purpose:** {purpose}

**Scope:** Salesforce QE knowledge — requirement analysis, testing strategy, regression, UAT, automation readiness, and production validation. Not an Admin or Developer how-to.

**Owner:** QE Practice Lead

**Version:** {VERSION}

**Status:** Draft (Sprint 4)

---

## Purpose

{purpose}

## Business Context

{bullets(business)}

## Salesforce Overview

{bullets(overview)}

## Key Features

{bullets(features)}

## Where Used

{bullets(where_used)}

## Business Examples

{bullets(examples)}

## Testing Considerations

{bullets(testing)}

## Functional Test Focus

{bullets(functional)}

## Negative Test Focus

{bullets(negative)}

## Regression Considerations

{bullets(regression)}

## Automation Opportunities

{bullets(auto_opp)}

## Production Risks

{bullets(prod)}

## Common Defects

{bullets(defects)}

## Best Practices

{bullets(practices)}

## Interview Tips

{bullets(interview)}

## Related Documents

{bullets(related_lines)}

## Future Enhancements

- Deepen org-edition notes and industry examples in later sprints
- Link detailed case templates when Sprint 5 lands

## Navigation

- **Previous:** [{nav['prev_label']}]({nav['prev']})
- **Next:** [{nav['next_label']}]({nav['next']})
- **See Also:** [README.md](README.md) · [Test Design Engine]({REL['test_design']})
"""


def folder_readme(folder: str, title: str, purpose: str, articles: list[tuple[str, str]], prev_folder: str | None, next_folder: str | None) -> str:
    rows = "\n".join(f"| [{slug_title(s)}]({s}.md) | {blurb} |" for s, blurb in articles)
    prev = f"[{prev_folder}/](../{prev_folder}/README.md)" if prev_folder else "[../README.md](../README.md)"
    nxt = f"[{next_folder}/](../{next_folder}/README.md)" if next_folder else "[../README.md](../README.md)"
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
keywords: [{folder}, knowledge-index]
tags: [knowledge, sprint-4, {folder}]
---

# {title}

**Purpose:** {purpose}

**Scope:** QE-oriented Salesforce knowledge for analysis, design, regression, and production validation.

**Owner:** QE Practice Lead

**Version:** {VERSION}

**Status:** Draft (Sprint 4)

## Articles

| Article | Focus |
|---------|-------|
{rows}

## Related Engines

- [Requirement Analysis](../requirement-analysis.md)
- [Test Design Engine](../test-design-engine.md)
- [knowledge/README.md](../README.md)

## Navigation

- **Previous:** {prev}
- **Next:** {nxt}
- **See Also:** [../../skill.md](../../skill.md)
"""


# ---------------------------------------------------------------------------
# Topic catalogs: (slug, short blurb, optional content overrides)
# ---------------------------------------------------------------------------

PLATFORM = [
    ("salesforce-platform-overview", "Multi-tenant platform building blocks and QE impact model", {
        "purpose": "Give QE a coherent mental model of the Salesforce platform so every requirement can be mapped to objects, UI, automation, security, data, and integrations.",
        "overview": [
            "Salesforce is a multi-tenant CRM/application platform: data model + UI + automation + security + APIs + analytics.",
            "Quality risk concentrates where metadata, automation, and persona permissions intersect.",
            "Cross-check high-level capabilities with [shared capability map](../../../shared/salesforce-capability-map.md); confirm org edition and licensed products.",
        ],
        "features": [
            "Standard and custom data model",
            "Lightning Experience / mobile / Experience sites",
            "Declarative automation and Apex extensibility",
            "Sharing model and identity controls",
            "APIs, events, and middleware patterns",
        ],
        "testing": [
            "Start with business journey → objects/fields → automation → security → integrations → reports",
            "Always ask which personas and channels (UI/API/Experience/mobile)",
            "Flag multi-cloud and package dependencies early",
        ],
    }),
    ("standard-objects", "Account, Contact, Case, Opportunity and core CRM objects", {
        "purpose": "Guide QE on how standard objects behave, extend, and fail so tests respect platform semantics.",
        "features": ["Standard fields and relationships", "Record types and business processes", "Activities, history, and related lists"],
        "functional": ["CRUD per persona on standard objects", "Required standard fields and conversion paths (e.g., Lead→Account/Contact/Opp)", "Related list and lookup integrity"],
        "related": ["[Custom Objects](custom-objects.md)", "[Record Types](record-types.md)"],
    }),
    ("custom-objects", "Custom data model objects and testing implications", {
        "purpose": "Explain custom object risk: schema, sharing, UI, and automation surfaces that QE must cover.",
        "negative": ["Create without required custom fields", "Orphan child records when master deleted (per relationship type)", "Unauthorized object access"],
        "related": ["[Fields](fields.md)", "[Relationships](relationships.md)"],
    }),
    ("fields", "Field types, requiredness, uniqueness, and UI behaviour", {
        "purpose": "Map field-level requirements to validation, FLS, layout, formula, and history tracking test needs.",
        "features": ["Data types and length", "Required / unique / external ID", "Help text, defaults, picklists"],
        "related": ["[Formula Fields](formula-fields.md)", "[Field Level Security](../security/field-level-security.md)"],
    }),
    ("relationships", "Lookup, master-detail, many-to-many, hierarchical", {
        "purpose": "Ensure QE validates referential integrity, cascade behaviour, and roll-up eligibility.",
        "functional": ["Parent-child create/update paths", "Cascade delete / restrict delete behaviour", "Junction object many-to-many journeys"],
        "related": ["[Roll-Up Summary Fields](roll-up-summary-fields.md)"],
    }),
    ("record-types", "Record type driven process and layout variation", {
        "purpose": "Test record-type assignment, picklist subsets, layouts, and process differences per persona.",
        "negative": ["Wrong record type available to persona", "Picklist value not in record-type subset", "Business process stage mismatch"],
        "related": ["[Business Processes](business-processes.md)", "[Page Layouts](page-layouts.md)"],
    }),
    ("business-processes", "Sales/Support processes and stage models", {
        "purpose": "Validate stage paths, closed reasons, and process alignment to AC and reporting.",
        "regression": ["Forecast/report filters tied to stages", "Automation entry criteria on StageName/Status"],
    }),
    ("page-layouts", "Classic/Lightning layout assignment and requiredness", {
        "purpose": "Verify layout-driven required fields, related lists, and persona-specific UX against AC.",
        "related": ["[Lightning Record Pages](lightning-record-pages.md)", "[Dynamic Forms](dynamic-forms.md)"],
    }),
    ("lightning-record-pages", "App Builder record pages, visibility, and components", {
        "purpose": "Test LRP component visibility, dynamic display, and persona/app assignment.",
        "common_defects": ["Component visible to wrong persona", "Missing related list after migration to LRP", "Activation not assigned to correct app/profile"],
    }),
    ("compact-layouts", "Highlight panel fields and mobile/search impact", {
        "purpose": "Confirm compact layout fields support agent/mobile triage without leaking restricted data.",
    }),
    ("global-actions", "Global create/log actions available from utility bar", {
        "purpose": "Validate global action availability, defaults, and permission prerequisites.",
    }),
    ("quick-actions", "Object-specific actions and publisher layout", {
        "purpose": "Test quick action field sets, prefill, and success behaviour per object/persona.",
    }),
    ("dynamic-forms", "Field visibility and section rules on LRP", {
        "purpose": "Validate visibility rules, requiredness, and migration from page layout fields.",
        "negative": ["Field hidden but still required via other path", "Rule evaluates wrong for null/blank"],
    }),
    ("formula-fields", "Calculated fields and cross-object formulas", {
        "purpose": "Test formula correctness, null handling, and downstream automation/report use.",
        "production_risks": ["Formula compile size / reference limits", "Stale assumptions when referenced fields change"],
    }),
    ("roll-up-summary-fields", "MD roll-ups and recalculation behaviour", {
        "purpose": "Validate roll-up filters, recalculation timing, and LDV performance risk.",
        "related": ["[Relationships](relationships.md)", "[../performance/large-data-volumes.md](../performance/large-data-volumes.md)"],
    }),
    ("external-objects", "Salesforce Connect / external data surfaces", {
        "purpose": "Test external object availability, latency, CRUD limits, and auth failures.",
        "related": ["[../integration/named-credentials.md](../integration/named-credentials.md)"],
    }),
    ("big-objects", "High-volume archival storage patterns", {
        "purpose": "Validate insert paths, query patterns, and reporting limitations for Big Objects.",
    }),
    ("custom-metadata-types", "CMDT-driven configuration used by automation", {
        "purpose": "Treat CMDT as testable configuration: values, packaging, and runtime consumption.",
        "regression": ["Automation that reads CMDT after package upgrade", "Missing CMDT records in lower environments"],
    }),
    ("custom-settings", "Hierarchy/list settings (legacy config patterns)", {
        "purpose": "Validate hierarchy vs list settings behaviour and org/user/profile overrides.",
        "best_practices": ["Prefer CMDT for packaged config when designing new solutions", "Document which settings are required in each environment"],
    }),
]

METADATA = [
    ("metadata-overview", "What metadata means for QE impact analysis", {
        "purpose": "Teach QE to think in metadata types when assessing change impact, deploy risk, and regression scope.",
        "overview": [
            "Almost every Salesforce change is metadata (or data). QE maps stories to metadata types for coverage.",
            "Use Setup/Audit Trail, change sets/DevOps center diffs, and package manifests as impact inputs.",
        ],
        "related": ["[Metadata Change Impact](metadata-change-impact.md)", "[Metadata Dependencies](metadata-dependencies.md)"],
    }),
    ("metadata-change-impact", "How to translate metadata diffs into test scope", {
        "purpose": "Provide a repeatable impact model from metadata change → components → scenarios → regression.",
        "testing": [
            "Classify change: data model / UI / automation / security / integration / analytics",
            "Identify consumers (Flows, Apex, reports) of changed fields",
            "Select smoke vs deep regression based on risk",
        ],
    }),
    ("metadata-dependencies", "Dependency and reference risk across components", {
        "purpose": "Highlight broken references, inactive versions, and cross-package dependency failures.",
    }),
    ("metadata-deployment-awareness", "Deploy validation from a QE lens", {
        "purpose": "Connect deployment metadata validation to smoke, post-deploy checks, and Go/No-Go evidence.",
        "related": ["[../release/deployment-validation.md](../release/deployment-validation.md)"],
    }),
]

AUTOMATION = [
    ("validation-rules", "Declarative field/record validation", {
        "purpose": "QE guidance for validation rules: formula edge cases, bypass patterns, and UX messages.",
        "related": [f"[Validation Rule Testing]({REL['vr_testing']})"],
        "testing": ["True/false formula partitions", "Bypass for integration user if required by design", "Error message clarity for UAT"],
    }),
    ("flows", "Flow family overview for QE", {
        "purpose": "Orient QE to Flow types, order of execution, and fault handling before deep type articles.",
        "related": [f"[Flow Testing]({REL['flow_testing']})", "[Record-Triggered Flows](record-triggered-flows.md)", "[Screen Flows](screen-flows.md)"],
    }),
    ("workflow-rules", "Legacy workflow rules", {
        "purpose": "Test remaining Workflow Rules and plan migration risk to Flow.",
        "production_risks": ["Legacy rule still firing after Flow migration (double action)", "Time-based queue backlog"],
    }),
    ("approval-processes", "Approval steps, recalls, and notifications", {
        "purpose": "Cover submit/approve/reject/recall, reassign, and email/notification side effects.",
        "negative": ["Submit without required criteria", "Approve as unauthorized user", "Recall after final approval (if blocked)"],
    }),
    ("process-builder", "Legacy Process Builder", {
        "purpose": "Validate remaining PB processes and coexistence risks with Flow/Apex.",
        "best_practices": ["Prefer documenting migration debt; avoid new PB builds", "Regression both PB and Flow during coexistence"],
    }),
    ("scheduled-flows", "Time-based Flow schedules", {
        "purpose": "Test schedule frequency, filter criteria, bulk batches, and missed-run behaviour.",
    }),
    ("record-triggered-flows", "Before/after save and async paths", {
        "purpose": "Validate entry criteria, recursion controls, async paths, and bulkification assumptions.",
        "related": [f"[Flow Testing]({REL['flow_testing']})", "[../performance/flow-performance.md](../performance/flow-performance.md)"],
    }),
    ("screen-flows", "Guided UI Flows", {
        "purpose": "Test screens, decisions, fault screens, finish behaviour, and permission to run.",
    }),
    ("auto-launched-flows", "Invocable / autolaunched Flow", {
        "purpose": "Validate invocable inputs/outputs, subflow contracts, and API/Apex invocation paths.",
    }),
    ("apex-triggers", "Trigger frameworks and handler logic", {
        "purpose": "QE focus on trigger events, bulkification, recursion, and coexistence with Flow.",
        "related": ["[../performance/governor-limits.md](../performance/governor-limits.md)"],
    }),
    ("batch-apex", "Batchable jobs", {
        "purpose": "Test batch scope queries, chunk failures, stateful patterns, and monitoring.",
        "related": ["[../performance/batch-performance.md](../performance/batch-performance.md)"],
    }),
    ("queueable-apex", "Async chainable jobs", {
        "purpose": "Validate enqueue conditions, chaining limits, and failure/retry observation.",
    }),
    ("scheduled-apex", "Cron-scheduled Apex", {
        "purpose": "Confirm schedule registration, next-fire expectations, and timezone assumptions.",
    }),
    ("platform-events", "Event-driven automation", {
        "purpose": "Test publish/subscribe, replay, and subscriber failure isolation.",
        "related": ["[../integration/platform-events.md](../integration/platform-events.md)"],
    }),
    ("change-data-capture", "CDC change events", {
        "purpose": "Validate CDC enablement, event shape, and downstream consumer behaviour.",
    }),
]

SECURITY = [
    ("profiles", "Base persona access", {
        "purpose": "Test profile baseline CRUD/FLS/app access and least-privilege alignment.",
        "related": [f"[Security Testing]({REL['security_testing']})", "[Permission Sets](permission-sets.md)"],
    }),
    ("permission-sets", "Additive access grants", {
        "purpose": "Validate permission set assignment effects and revoke paths.",
        "related": ["[../permission-set-testing.md](../permission-set-testing.md)"],
    }),
    ("permission-set-groups", "Bundled permission sets", {
        "purpose": "Test mute permissions, group assignment, and persona packing.",
    }),
    ("field-level-security", "Field visibility and editability", {
        "purpose": "Ensure FLS matches persona needs across UI, API, reports, and list views.",
    }),
    ("object-permissions", "Object CRUD and View All/Modify All risk", {
        "purpose": "Validate object CRUD and escalate View All/Modify All as high-risk exceptions.",
    }),
    ("sharing-rules", "Criteria/owner-based sharing", {
        "purpose": "Test share expansion and revocation when criteria change.",
        "related": [f"[Sharing Security Testing]({REL['sharing_testing']})"],
    }),
    ("role-hierarchy", "Role-based visibility", {
        "purpose": "Validate hierarchy visibility assumptions and Grant Access Using Hierarchies.",
    }),
    ("queues", "Queue ownership and membership", {
        "purpose": "Test queue assignment, member access, and email-to-case/queue routing.",
    }),
    ("public-groups", "Group membership for sharing/queues", {
        "purpose": "Validate group membership changes ripple to sharing and list views.",
    }),
    ("manual-sharing", "Ad-hoc share records", {
        "purpose": "Confirm manual share create/revoke and UI availability rules.",
    }),
    ("organization-wide-defaults", "OWD baseline sharing", {
        "purpose": "Treat OWD changes as high regression risk; validate open/private impacts.",
    }),
    ("restriction-rules", "Negative access filters", {
        "purpose": "Test restriction rule filter logic and coexistence with sharing grants.",
    }),
    ("login-policies", "Login IP/hours and related controls", {
        "purpose": "Validate login restrictions without locking out UAT/integration users unexpectedly.",
    }),
    ("session-policies", "Session timeout and security settings", {
        "purpose": "Confirm session policies for high-risk personas and Experience users.",
    }),
    ("mfa", "Multi-factor authentication", {
        "purpose": "Validate MFA enforcement, exemptions, and break-glass procedures for test users.",
    }),
    ("data-visibility", "End-to-end visibility model", {
        "purpose": "Synthesize OWD + role + sharing + teams + restriction into persona visibility tests.",
        "related": [f"[Sharing Security Testing]({REL['sharing_testing']})", "[Organization Wide Defaults](organization-wide-defaults.md)"],
    }),
]

INTEGRATION = [
    ("rest-apis", "REST resource testing", {
        "purpose": "Guide REST contract, auth, status codes, and idempotency checks for QE.",
        "related": [f"[API Testing]({REL['api_testing']})", f"[Integration Testing]({REL['integration_testing']})"],
    }),
    ("soap-apis", "SOAP enterprise/partner API patterns", {
        "purpose": "Cover SOAP login, CRUD, and fault handling where still in use.",
    }),
    ("bulk-api", "Bulk v1/v2 data APIs", {
        "purpose": "Validate job lifecycle, error files, and partial success behaviour.",
    }),
    ("platform-events", "Integration via platform events", {
        "purpose": "Test event contracts and subscriber processing across system boundaries.",
        "related": ["[../automation/platform-events.md](../automation/platform-events.md)"],
    }),
    ("outbound-messages", "Workflow outbound messages", {
        "purpose": "Validate delivery, acknowledgement, and endpoint failure handling.",
    }),
    ("named-credentials", "Secure callout endpoints", {
        "purpose": "Test auth protocols, endpoint env mapping, and secret rotation impact.",
    }),
    ("external-services", "Declarative OpenAPI callouts", {
        "purpose": "Validate External Service actions from Flow and error mapping.",
    }),
    ("middleware-integration", "MuleSoft/other middleware patterns", {
        "purpose": "Define QE responsibilities across Salesforce vs middleware vs target system.",
        "testing": ["Contract tests at boundaries", "End-to-end with controlled test doubles when needed", "Ownership of failures (source vs hop vs target)"],
    }),
    ("error-handling", "Integration error patterns", {
        "purpose": "Ensure errors are logged, retried, and surfaced per design—not silently dropped.",
    }),
    ("retry-mechanisms", "Retry/backoff and poison messages", {
        "purpose": "Validate retry limits, dead-letter behaviour, and duplicate side effects.",
    }),
    ("authentication", "OAuth/JWT/session auth for integrations", {
        "purpose": "Test token lifecycle, scopes, and expired-credential failure modes.",
    }),
    ("authorization", "Connected app and user context authorization", {
        "purpose": "Confirm principle of least privilege for integration users and named principals.",
    }),
    ("integration-monitoring", "Observability for interfaces", {
        "purpose": "Define evidence: logs, event monitoring, middleware dashboards, and alert thresholds.",
    }),
    ("testing-strategy", "Overall integration test strategy", {
        "purpose": "Layer contract, component, E2E, and production-validation approaches for integrations.",
        "related": [f"[Integration Testing]({REL['integration_testing']})"],
    }),
    ("mocking", "Mocks/stubs/virtualization", {
        "purpose": "Advise when to mock vs hit lower environments; avoid false confidence.",
    }),
    ("regression-impact", "Integration regression after Salesforce change", {
        "purpose": "Map Salesforce field/API/event changes to external consumer regression.",
        "related": [f"[Regression Planning]({REL['regression']})"],
    }),
]

CLOUDS = [
    ("sales-cloud", "Lead-to-cash CRM core", {
        "purpose": "QE lens on Sales Cloud journeys, objects, and regression hotspots.",
        "features": ["Lead, Account, Contact, Opportunity, Quote", "Forecasting, products, price books", "Activities and path/guidance"],
        "related": [f"[Capability Map]({REL['capability_map']})"],
    }),
    ("service-cloud", "Case and service operations", {
        "purpose": "Cover Case lifecycle, Omni-Channel, entitlements, Knowledge from QE view.",
        "features": ["Case, Entitlement, Milestone", "Omni-Channel routing", "Knowledge, macros, service console"],
        "related": ["[../../salesforce-business-analyst/knowledge/service-cloud-patterns.md](../../../salesforce-business-analyst/knowledge/service-cloud-patterns.md) (BA patterns—do not duplicate)"],
    }),
    ("experience-cloud", "Digital experiences / portals", {
        "purpose": "Test persona access, guest vs authenticated, sharing, and branded journeys.",
        "production_risks": ["Guest user oversharing", "Self-registration/profile assignment errors"],
    }),
    ("field-service", "Field Service / workforce", {
        "purpose": "Validate work orders, scheduling, mobile offline, and inventory impacts.",
    }),
    ("revenue-cloud-cpq", "CPQ / Revenue Cloud quoting", {
        "purpose": "Test product rules, pricing, guided selling, and quote-to-order handoffs.",
        "regression": ["Price rule interactions", "Product bundle constraints", "Amendment/renewal paths"],
    }),
    ("marketing-cloud", "Marketing Cloud functional overview for QE", {
        "purpose": "Functional overview of journeys/audiences for Salesforce CRM sync testing—not full MC admin.",
        "overview": ["Focus on CRM connector sync, consent flags, and journey entry criteria that touch CRM data.", "Defer deep MC studio configuration to marketing specialists."],
    }),
    ("data-cloud", "Data Cloud functional overview for QE", {
        "purpose": "QE focus on identity resolution, segments, activation, and data quality touchpoints.",
    }),
    ("agentforce", "AI agents and grounded actions", {
        "purpose": "Validate agent actions, grounding, guardrails, escalation, and auditability.",
        "negative": ["Out-of-policy action attempted", "Hallucinated data not grounded", "Escalation to human fails"],
    }),
    ("omnistudio", "FlexCards, Omniscripts, DataRaptors, IPs", {
        "purpose": "Test Omniscript paths, DataRaptor transforms, and Integration Procedure contracts.",
    }),
    ("industries", "Industries Cloud common patterns", {
        "purpose": "Orient QE to Industries frameworks and when industry-specific clouds apply.",
        "related": ["[Utilities Cloud](utilities-cloud.md)", "[../industry/README.md](../industry/README.md)"],
    }),
    ("utilities-cloud", "Utilities industry cloud patterns", {
        "purpose": "QE guidance for utilities processes (service, meter, outage themes) on Salesforce.",
        "related": ["[../industry/utilities.md](../industry/utilities.md)"],
    }),
]

REPORTING = [
    ("reports", "Report builder and folders", {
        "purpose": "Validate report filters, fields, folders, and persona visibility.",
        "related": [f"[Report Testing]({REL['report_testing']})"],
    }),
    ("dashboards", "Dashboard components and running user", {
        "purpose": "Test dashboard running user, component filters, and refresh behaviour.",
        "related": [f"[Dashboard Testing]({REL['dashboard_testing']})"],
    }),
    ("report-types", "Custom report types", {
        "purpose": "Confirm CRT object joins and field availability match stakeholder needs.",
    }),
    ("joined-reports", "Multi-block joined reports", {
        "purpose": "Validate block filters and common dimension assumptions.",
    }),
    ("matrix-reports", "Matrix grouping reports", {
        "purpose": "Test row/column groupings and grand totals against known datasets.",
    }),
    ("summary-reports", "Summary aggregates", {
        "purpose": "Validate groupings, summaries, and chart source data.",
    }),
    ("charts", "Report/dashboard charts", {
        "purpose": "Confirm chart type, axis fields, and filter interaction.",
    }),
    ("scheduling", "Scheduled report runs", {
        "purpose": "Test schedule timing, recipients, and failure notification.",
    }),
    ("subscriptions", "Report/dashboard subscriptions", {
        "purpose": "Validate subscription recipients and attachment/link formats.",
    }),
    ("testing-approach", "Overall reporting test approach", {
        "purpose": "Define data fixtures, expected aggregates, and persona checks for analytics.",
        "related": [f"[Report Testing]({REL['report_testing']})"],
    }),
    ("validation-strategy", "How to prove report correctness", {
        "purpose": "Reconcile report output to SOQL/export or source-of-truth samples.",
    }),
    ("common-risks", "Reporting quality risks", {
        "purpose": "Catalog filter mistakes, running-user issues, and folder sharing leaks.",
    }),
]

DATA = [
    ("data-import", "Import wizards and ingest paths", {"purpose": "Validate import mapping, partial success, and duplicate handling."}),
    ("data-export", "Export and weekly export", {"purpose": "Confirm export completeness, encoding, and access controls."}),
    ("data-loader", "Data Loader / bulk tools", {"purpose": "Test upsert keys, error CSVs, and batch sizes."}),
    ("duplicate-rules", "Duplicate prevention/allow", {"purpose": "Validate alert vs block behaviour and bypass roles."}),
    ("matching-rules", "Matching criteria", {"purpose": "Test match strength and false positive/negative tradeoffs."}),
    ("data-quality", "Completeness/accuracy/consistency", {"purpose": "Define DQ checks QE can evidence during UAT and hypercare."}),
    ("field-history-tracking", "Field history", {"purpose": "Confirm tracked fields, retention expectations, and UI history."}),
    ("audit-trail", "Setup Audit Trail", {"purpose": "Use Audit Trail as deploy/investigation evidence—not as functional AC."}),
    ("archiving", "Archive/purge patterns", {"purpose": "Validate archive criteria and restore/read-only expectations."}),
    ("data-migration-validation", "Migration cutover validation", {"purpose": "Reconcile volumes, key fields, relationships, and sample business journeys."}),
    ("data-reconciliation", "Source vs Salesforce balances", {"purpose": "Define reconciliation queries and tolerance rules."}),
    ("test-data-management", "TDM for sandboxes", {"purpose": "Advise synthetic vs masked data, referential integrity, and persona packs."}),
    ("data-masking", "Sandbox masking", {"purpose": "Validate masking completeness for PII/PHI and broken-reference risks."}),
    ("data-privacy", "Privacy/compliance testing lens", {"purpose": "Flag consent, retention, and subject-request paths; confirm with Legal—do not invent regulations."}),
]

RELEASE = [
    ("deployment-validation", "Pre/during deploy checks", {
        "purpose": "Define QE evidence for successful metadata/data deploy validation.",
        "related": ["[Post Deployment Validation](post-deployment-validation.md)"],
    }),
    ("post-deployment-validation", "Immediate post-deploy checks", {
        "purpose": "Structured PPV: smoke, key journeys, integrations, permissions.",
    }),
    ("smoke-testing", "Release smoke pack", {
        "purpose": "Minimal critical-path confidence after deploy.",
        "related": [f"[Smoke Testing (design)]({REL['smoke']})"],
    }),
    ("sanity-testing", "Narrow change confirmation", {
        "purpose": "Targeted sanity around the change set vs full regression.",
        "related": [f"[Sanity Testing (design)]({REL['sanity']})"],
    }),
    ("hypercare", "Post-go-live support window", {
        "purpose": "Define monitoring, triage SLAs, and feedback into defect intelligence.",
    }),
    ("rollback-validation", "Rollback/backout verification", {
        "purpose": "Validate backout plan tests: data integrity and feature restore.",
    }),
    ("release-readiness", "Readiness assessment inputs", {
        "purpose": "Evidence checklist for exit criteria, open risks, and sign-off.",
    }),
    ("regression-planning", "Release regression planning", {
        "purpose": "Release-level regression packs and risk-based selection.",
        "related": [f"[Regression Planning]({REL['regression']})"],
    }),
    ("cutover-support", "Cutover weekend QE role", {
        "purpose": "QE activities during cutover: checks, war-room, decision logs.",
    }),
    ("go-no-go-validation", "Go/No-Go evidence", {
        "purpose": "Structure Go/No-Go recommendation from test evidence and residual risk.",
    }),
]

PERFORMANCE = [
    ("governor-limits", "Platform governor limits", {
        "purpose": "Teach QE which limits matter in scenarios and how failures present.",
    }),
    ("performance-testing-considerations", "When/how to performance-test Salesforce", {
        "purpose": "Scope performance testing realistically for shared multi-tenant constraints.",
    }),
    ("soql-limits", "SOQL row/query limits", {
        "purpose": "Validate query volume risks in automation and integrations.",
    }),
    ("query-selectivity", "Selective filters and indexes", {
        "purpose": "Advise on selective filter tests and LDV query plans.",
    }),
    ("large-data-volumes", "LDV testing considerations", {
        "purpose": "Plan LDV scenarios for list views, roll-ups, sharing recalc, and batches.",
    }),
    ("record-locking", "Row lock errors", {
        "purpose": "Reproduce and mitigate record lock contention in parallel updates.",
    }),
    ("concurrency", "Concurrent user/update behaviour", {
        "purpose": "Design concurrency scenarios for queues, inventory, and approvals.",
    }),
    ("batch-performance", "Batch job duration and failures", {
        "purpose": "Measure batch throughput and failure isolation.",
        "related": ["[../automation/batch-apex.md](../automation/batch-apex.md)"],
    }),
    ("report-performance", "Slow reports/dashboards", {
        "purpose": "Identify report timeout risks and filter/index mitigations.",
    }),
    ("flow-performance", "Flow bulk and DML risks", {
        "purpose": "Test Flow bulkification and element limits under volume.",
        "related": ["[../automation/record-triggered-flows.md](../automation/record-triggered-flows.md)"],
    }),
]

PACKAGES = [
    ("managed-packages", "Managed package fundamentals for QE", {
        "purpose": "Explain managed package upgrade/testing constraints for enterprise QE.",
    }),
    ("unlocked-packages", "Unlocked package testing", {
        "purpose": "Validate unlocked package install/upgrade and org customizations coexistence.",
    }),
    ("package-upgrades", "Upgrade validation strategy", {
        "purpose": "Define pre/post upgrade smoke, data, and automation regression.",
    }),
    ("package-dependencies", "Dependency graphs and install order", {
        "purpose": "Test dependency prerequisites and broken subscriber overrides.",
    }),
    ("namespace-prefixes", "Namespace impact on Apex/API/tests", {
        "purpose": "Ensure tests and integrations handle namespaced components correctly.",
    }),
    ("package-testing", "Package test strategy", {
        "purpose": "Combine vendor release notes with subscriber org regression.",
    }),
    ("regression-risks", "Package regression hotspots", {
        "purpose": "Catalog typical breakages after package upgrades.",
        "related": [f"[Regression Planning]({REL['regression']})"],
    }),
    ("version-compatibility", "API/package version compatibility", {
        "purpose": "Track API versions, package versions, and deprecated components.",
    }),
    ("troubleshooting", "Package install/upgrade troubleshooting", {
        "purpose": "QE checklist for install errors, missing access, and post-upgrade defects.",
    }),
]

INDUSTRY = [
    ("utilities", "Utilities Salesforce programs", {
        "purpose": "Starter QE industry lens for utilities on Salesforce.",
        "business_examples": [
            "Service request / outage Case journeys",
            "Field work order completion and billing handoff themes",
            "Customer portal self-service for meter/account inquiries",
        ],
        "testing": ["High-risk: integrations to CIS/MDM/OMS", "Persona: CSR, field tech, portal customer", "Regression: billing-critical field updates"],
    }),
    ("retail", "Retail / consumer programs", {
        "purpose": "Starter QE industry lens for retail CRM/service on Salesforce.",
        "business_examples": ["Omnichannel Case + Order inquiry", "Loyalty preference updates", "Store associate console journeys"],
    }),
    ("banking", "Banking / FS programs", {
        "purpose": "Starter QE lens for banking CRM; confirm regulatory constraints with Compliance—do not invent rules.",
        "production_risks": ["Unauthorized visibility of financial data", "Incorrect KYC/status updates", "Integration failures to core banking"],
    }),
    ("insurance", "Insurance programs", {
        "purpose": "Starter QE lens for policy/claim-oriented Salesforce programs.",
        "business_examples": ["FNOL Case intake", "Policy inquiry console", "Producer/partner community access"],
    }),
    ("healthcare", "Healthcare programs", {
        "purpose": "Starter QE lens; treat PHI/HIPAA as Legal/Compliance-confirmed constraints.",
        "best_practices": ["Never invent regulatory requirements", "Emphasize access control and audit evidence"],
    }),
    ("manufacturing", "Manufacturing / dealer programs", {
        "purpose": "Starter QE lens for dealer, asset, and supply-chain adjacent CRM.",
    }),
    ("telecommunications", "Telecom programs", {
        "purpose": "Starter QE lens for provisioning/activation-adjacent CRM/service.",
        "testing": ["Order/status sync with BSS/OSS", "High volume Case/Omni routing", "Portal self-care journeys"],
    }),
    ("public-sector", "Public sector / constituent programs", {
        "purpose": "Starter QE lens for case/grant/constituent service patterns.",
        "production_risks": ["Incorrect constituent data visibility", "FOIA/audit trail gaps (confirm locally)", "Portal accessibility and access control"],
    }),
]

FOLDERS: list[tuple[str, str, str, list]] = [
    ("platform", "Platform Knowledge", "Core Salesforce platform building blocks for QE decisions.", PLATFORM),
    ("metadata", "Metadata Knowledge", "Metadata awareness for impact analysis and deployment risk.", METADATA),
    ("clouds", "Clouds Knowledge", "Salesforce Cloud product knowledge for QE.", CLOUDS),
    ("automation", "Automation Knowledge", "Declarative and programmatic automation from a testing lens.", AUTOMATION),
    ("security", "Security Knowledge", "Access, sharing, and identity controls for QE.", SECURITY),
    ("integration", "Integration Knowledge", "APIs, events, middleware, and interface quality.", INTEGRATION),
    ("data", "Data Knowledge", "Data quality, migration, privacy, and test data.", DATA),
    ("reporting", "Reporting Knowledge", "Reports, dashboards, and analytics validation.", REPORTING),
    ("release", "Release Knowledge", "Deploy, smoke, hypercare, and Go/No-Go.", RELEASE),
    ("performance", "Performance Knowledge", "Governor limits, LDV, concurrency, and performance risk.", PERFORMANCE),
    ("managed-packages", "Managed Package Knowledge", "Packages, upgrades, namespaces, and subscriber testing.", PACKAGES),
    ("industry", "Industry Knowledge", "Industry starter packs for QE scenario design.", INDUSTRY),
]


def nav_for(articles: list, idx: int) -> dict:
    slugs = [a[0] for a in articles]
    prev_slug = slugs[idx - 1] if idx > 0 else None
    next_slug = slugs[idx + 1] if idx < len(slugs) - 1 else None
    return {
        "prev": f"{prev_slug}.md" if prev_slug else "README.md",
        "prev_label": slug_title(prev_slug) if prev_slug else "README",
        "next": f"{next_slug}.md" if next_slug else "README.md",
        "next_label": slug_title(next_slug) if next_slug else "README",
    }


def main() -> None:
    folder_names = [f[0] for f in FOLDERS]
    count = 0
    for i, (folder, title, purpose, articles) in enumerate(FOLDERS):
        folder_path = KNOWLEDGE / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        norm = []
        for item in articles:
            slug, blurb = item[0], item[1]
            meta = dict(item[2]) if len(item) > 2 else {}
            meta.setdefault("title", slug_title(slug))
            norm.append((slug, blurb, meta))

        prev_f = folder_names[i - 1] if i > 0 else None
        next_f = folder_names[i + 1] if i < len(folder_names) - 1 else None
        readme = folder_readme(
            folder,
            title,
            purpose,
            [(s, b) for s, b, _ in norm],
            prev_f,
            next_f,
        )
        (folder_path / "README.md").write_text(readme, encoding="utf-8")
        count += 1

        for idx, (slug, blurb, meta) in enumerate(norm):
            body = doc_body(folder, slug, meta, nav_for(norm, idx))
            (folder_path / f"{slug}.md").write_text(body, encoding="utf-8")
            count += 1

    print(f"Wrote {count} files under {KNOWLEDGE}")


if __name__ == "__main__":
    main()
