"""Generate Salesforce Field Service (FSL) QA skill pack."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP = ROOT / "skills" / "field-service-testing"
VERSION = "0.19.0"
DATE = "2026-07-27"

OUTPUT_SECTIONS = [
    "Executive Summary",
    "Business Scenario",
    "FSL Components Reviewed",
    "Scheduling Assessment",
    "Dispatcher Assessment",
    "Mobile Assessment",
    "Inventory Assessment",
    "Security Assessment",
    "Performance Assessment",
    "Offline Validation",
    "Negative Test Scenarios",
    "Edge Case Testing",
    "Regression Scope",
    "Automation Opportunities",
    "Recommended SOQL Validation",
    "Deployment Readiness",
    "Risks",
    "Recommendations",
]


def fm(title: str, category: str, doc_type: str, tags: list[str]) -> str:
    return f"""---
title: {title}
module: Salesforce Quality Engineering
category: {category}
document_type: {doc_type}
version: {VERSION}
review_status: Draft
owner: QE Practice Lead
created_date: {DATE}
last_updated: {DATE}
review_cycle: quarterly
tags: [{", ".join(tags)}]
---

"""


def write(rel: str, content: str) -> None:
    path = CAP / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {rel}")


def knowledge_article(title, slug, purpose, reasoning, cross_links, rules):
    links = "\n".join(f"- [{n}]({p})" for n, p in cross_links)
    return fm(title, "QE Specialized Skill Knowledge", "Knowledge Article", ["field-service-qa", "knowledge"]) + f"""# {title}

## Purpose

{purpose}

## Reasoning Model

{chr(10).join(f"{i}. {r}" for i, r in enumerate(reasoning, 1))}

## Decision Rules

{chr(10).join(f"- {r}" for r in rules)}

## Cross-Links (Canonical Depth)

{links}

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {VERSION} | {DATE} | QE Practice Lead | Initial capability knowledge |
"""


def playbook(title, slug, objective, inputs, workflow, decisions, deliverables, expected, escalation, pointer=""):
    ptr = f"\n\n**Pointer:** {pointer}" if pointer else ""
    b = lambda xs: "\n".join(f"- {x}" for x in xs)
    return fm(title, "QE Specialized Skill Playbook", "Playbook", ["field-service-qa", "playbook"]) + f"""# {title}

## Objective

{objective}{ptr}

## Inputs

{b(inputs)}

## Validation Workflow

{b(workflow)}

## Decision Points

{b(decisions)}

## Deliverables

{b(deliverables)}

## Expected Results

{b(expected)}

## Escalation Rules

{b(escalation)}
"""


def template_doc(title, sections):
    body = "\n\n".join(f"## {s}\n\n_Complete during analysis._" for s in sections)
    return fm(title, "QE Specialized Skill Template", "Template", ["field-service-qa", "template"]) + f"""# {title}

{body}

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {VERSION} | {DATE} | QE Practice Lead | Initial template |
"""


def prompt_doc(title, prompt, sections):
    return fm(title, "QE Specialized Skill Prompt", "Prompt", ["field-service-qa", "prompt"]) + f"""# {title}

## Prompt

```
{prompt}
```

## Required Output Sections

{chr(10).join(f"{i}. {s}" for i, s in enumerate(sections, 1))}

## Quality Gate

- Business Scenario and FSL Components Reviewed BEFORE detailed test cases.
- Cover scheduling, mobile/offline, and inventory when in scope.
- Label assumptions; do not invent optimization scores or SLA values.
"""


def example_doc(title, scenario, components, rules, objectives, backend, expected, negative, soql, qa):
    return fm(title, "QE Specialized Skill Example", "Example", ["field-service-qa", "example"]) + f"""# {title}

## Business Scenario

{scenario}

## FSL Components

{components}

## Scheduling Rules

{rules}

## Test Objectives

{objectives}

## Backend Validation

{backend}

## Expected Results

{expected}

## Negative Scenarios

{negative}

## Recommended SOQL

```sql
{soql}
```

## QA Recommendations

{qa}
"""


def main() -> None:
    print("Generating Field Service FSL QA skill pack...")
    CAP.mkdir(parents=True, exist_ok=True)

    write(
        "skill-config.yaml",
        f"""name: field-service-qa
short_id: FSQA
version: {VERSION}
parent_module: salesforce-quality-engineering
entry: SKILL.md

routing:
  keywords:
    - Field Service
    - FSL
    - Work Order
    - Work Order Line Item
    - Service Appointment
    - Service Resource
    - Service Territory
    - Operating Hours
    - Scheduling
    - Dispatcher Console
    - Optimization
    - Mobile App
    - Technician
    - Crew
    - Van Stock
    - Inventory
    - Parts
    - Maintenance Plan
    - Service Report
    - Offline
    - Field Service Mobile
    - Appointment Booking
    - Work Type
    - Skills
    - Skill Requirements
    - Product Request
    - Product Transfer
  primary_support:
    - knowledge/clouds/field-service.md
    - automation-intelligence/mobile-testing/
  upstream_skills:
    - skills/metadata-impact-analyzer
  downstream_capabilities:
    - skills/soql-validation-assistant
    - skills/permission-testing-agent
    - skills/agentforce-testing
  downstream_after_analysis:
    - knowledge/test-design-engine.md

output_schema:
  sections:
{chr(10).join(f'    - id: {s.lower().replace(" ", "_")}' + chr(10) + f'      title: "{s}"' for s in OUTPUT_SECTIONS)}

quality_gates:
  - business_and_components_before_detailed_cases
  - scheduling_mobile_inventory_when_in_scope
  - soql_stubs_for_sova_expansion
  - no_invented_optimization_or_sla_percent
  - chain_mia_sova_pta_aft_when_applicable

escalation:
  - signal: double_booking_or_sla_breach_in_prod
    to: Release Manager + FSL Architect
  - signal: offline_data_loss
    to: Mobile Architect + Security Architect
  - signal: optimization_timeout_ldv
    to: Performance / Solution Architect
""",
    )

    cloud = "../../knowledge/clouds/field-service.md"
    mobile = "../../automation-intelligence/mobile-testing/README.md"
    mia = "../../skills/metadata-impact-analyzer/SKILL.md"
    sova = "../soql-validation-assistant/SKILL.md"
    pta = "../permission-testing-agent/SKILL.md"
    aft = "../agentforce-testing/SKILL.md"
    eq = "../../enterprise-quality/salesforce/field-service.md"

    knowledge_specs = [
        ("Salesforce Field Service Architecture", "field-service-architecture.md",
         "Map WO → SA → Resource → Territory → Policy layers before test design.",
         ["Inventory core objects and personas (dispatcher, technician, crew).", "Separate scheduling, mobile, inventory surfaces.", "Confirm FSL license/features—do not invent capabilities.", "Identify integrations (ERP inventory, GIS, Agentforce booking)."],
         [("Field Service Cloud Knowledge", cloud), ("Enterprise Field Service", eq)],
         ["UI-only WO tests are insufficient for FSL QA.", "Confirm edition before asserting optimization features."]),
        ("Scheduling Engine", "scheduling-engine.md",
         "Validate candidate selection, travel, availability, and conflicts.",
         ["Identify scheduling policy and work rules in scope.", "Design tests for availability, skills, territory, travel.", "Verify double-booking prevention and emergency insert.", "Document expected candidate set qualitatively—no invented scores."],
         [("Field Service Cloud Knowledge", cloud)],
         ["Double booking → Fail scheduling assessment.", "Do not invent optimization scores."]),
        ("Dispatcher Console", "dispatcher-console.md",
         "Validate dispatcher UX for assign, drag-drop, Gantt, and alerts.",
         ["Map dispatcher persona permissions.", "Test assign/unassign/reschedule paths.", "Verify console filters by territory and capacity.", "Capture negative: cannot assign unqualified resource."],
         [("Field Service Cloud Knowledge", cloud), ("Permission Testing Agent", pta)],
         ["Dispatcher without territory visibility → PTA escalation."]),
        ("Scheduling Policies", "scheduling-policies.md",
         "Assess policy rules driving candidate eligibility.",
         ["List policy work rules and objectives in scope.", "Test each major rule with matching/non-matching appointments.", "Validate holiday and operating hours interactions."],
         [("Scheduling Engine", "scheduling-engine.md")],
         ["Policy change without regression pack → High risk."]),
        ("Optimization Rules", "optimization-rules.md",
         "Validate optimization runs and conflict resolution.",
         ["Define optimization scope (territory, date range).", "Compare before/after schedule for conflicts reduced—qualitative.", "Test timeout and partial optimization behavior.", "Do not invent numeric optimization scores."],
         [("Scheduling Engine", "scheduling-engine.md"), ("Performance Knowledge", "../../knowledge/performance/README.md")],
         ["Optimization timeout on LDV → Performance escalation."]),
        ("Service Territories", "service-territories.md",
         "Validate territory membership, coverage, and visibility.",
         ["Map territories and members.", "Test SA scheduling outside territory.", "Validate hierarchy if used.", "Cross-check sharing with PTA."],
         [("Field Service Cloud Knowledge", cloud), ("Permission Testing Agent", pta)],
         ["Resource scheduled outside territory → Fail unless exception rule documented."]),
        ("Skills Management", "skills-management.md",
         "Validate skill requirements vs resource skills.",
         ["Map Work Type / Skill Requirements.", "Test match and mismatch assignment.", "Validate skill level and expiration if configured."],
         [("Field Service Cloud Knowledge", cloud)],
         ["Unskilled assignment allowed → document as defect or approved exception."]),
        ("Work Orders", "work-orders.md",
         "Validate Work Order and WOLI lifecycle.",
         ["Trace create → schedule → execute → close.", "Validate required fields and status transitions.", "Link child SA and inventory consumption.", "Chain MIA when WO automation/metadata changes."],
         [("Field Service Cloud Knowledge", cloud), ("Metadata Impact Analyzer", mia)],
         ["Status skip without business rule → Fail."]),
        ("Service Appointments", "service-appointments.md",
         "Validate SA scheduling, status, and completion.",
         ["Test Scheduled → Dispatched → In Progress → Completed.", "Validate duration, arrival windows, and cannot-complete reasons.", "Backend SOQL for Assigned Resource."],
         [("SOQL Validation Assistant", sova)],
         ["Completed SA without resource → Fail backend validation."]),
        ("Maintenance Plans", "maintenance-plans.md",
         "Validate planned maintenance generation and assets.",
         ["Confirm generation cadence and Work Type.", "Validate Maintenance Assets coverage.", "Test skipped periods and holidays."],
         [("Work Orders", "work-orders.md")],
         ["Missing generated WO for due asset → Fail."]),
        ("Mobile Architecture", "mobile-architecture.md",
         "Validate Field Service Mobile surfaces and flows.",
         ["Map online vs offline capabilities in scope.", "Identify photo, signature, barcode, GPS features.", "Cross-link Sprint 8 mobile testing for automation design only."],
         [("Mobile Testing", mobile), ("Field Service Cloud Knowledge", cloud)],
         ["No full Appium scripts unless explicitly requested."]),
        ("Offline Synchronization", "offline-synchronization.md",
         "Validate offline cache, sync, and conflict handling.",
         ["Design go-offline → mutate → reconnect scenarios.", "Test conflict when desktop and mobile both change SA.", "Verify no silent data loss.", "Security: offline cache must not expose other territories."],
         [("Mobile Architecture", "mobile-architecture.md"), ("Permission Testing Agent", pta)],
         ["Data loss on sync → Critical escalation."]),
        ("Inventory Management", "inventory-management.md",
         "Validate van stock, product requests, consumption, transfers.",
         ["Map Products Consumed on WOLI.", "Test Product Request and Transfer paths.", "Reconcile inventory with SOVA queries.", "Validate returns and shortages."],
         [("SOQL Validation Assistant", sova), ("Data Validation", "../../knowledge/data/data-validation.md")],
         ["Negative stock without override → Fail."]),
        ("Crew Management", "crew-management.md",
         "Validate crews, members, and multi-resource appointments.",
         ["Map Service Crew and members.", "Test crew assignment vs individual.", "Validate capacity when member absent."],
         [("Service Appointments", "service-appointments.md")],
         ["Crew scheduled with unavailable member → Fail unless rule allows."]),
        ("Performance Best Practices", "performance-best-practices.md",
         "Assess FSL performance risks for console, optimization, sync.",
         ["Flag LDV territories and high SA volume.", "Recommend timeboxed optimization scopes.", "Cross-link performance knowledge—no invented timings."],
         [("Performance Knowledge", "../../knowledge/performance/README.md")],
         ["Do not invent response-time SLAs."]),
        ("FSL Deployment Strategy", "fsl-deployment-strategy.md",
         "Align FSL metadata and config deploys with QA gates.",
         ["Inventory FSL settings and permission sets.", "Chain MIA for package.xml FSL components.", "Require mobile regression after policy/permission change."],
         [("Metadata Impact Analyzer", mia), ("Release Readiness", "../../knowledge/release/release-readiness.md")],
         ["Policy deploy without scheduling regression → No-Go."]),
        ("Field Service Testing Best Practices", "field-service-testing-best-practices.md",
         "Synthesize enterprise FSL QA discipline.",
         ["Components before cases.", "Always include negative scheduling and offline conflict.", "Chain SOVA for WO/SA/inventory proofs.", "Chain PTA for dispatcher/technician access.", "Label assumptions."],
         [("Field Service Cloud Knowledge", cloud), ("Test Design Engine", "../../knowledge/test-design-engine.md")],
         ["Every deliverable uses 18-section schema."]),
    ]
    for spec in knowledge_specs:
        write(f"knowledge/{spec[1]}", knowledge_article(*spec))

    write(
        "knowledge/README.md",
        fm("Field Service QA — Knowledge", "QE Specialized Skill Knowledge", "Guide", ["field-service-qa"])
        + """# Field Service QA — Knowledge

Canonical product overview: [`../../knowledge/clouds/field-service.md`](../../knowledge/clouds/field-service.md). These articles provide **FSL QA reasoning models**.

| Document | Focus |
|----------|-------|
| [Field Service Architecture](field-service-architecture.md) | Layered model |
| [Scheduling Engine](scheduling-engine.md) | Candidates/conflicts |
| [Dispatcher Console](dispatcher-console.md) | Dispatch UX |
| [Scheduling Policies](scheduling-policies.md) | Policies |
| [Optimization Rules](optimization-rules.md) | Optimization |
| [Service Territories](service-territories.md) | Territories |
| [Skills Management](skills-management.md) | Skills |
| [Work Orders](work-orders.md) | WO lifecycle |
| [Service Appointments](service-appointments.md) | SA lifecycle |
| [Maintenance Plans](maintenance-plans.md) | Planned work |
| [Mobile Architecture](mobile-architecture.md) | Mobile |
| [Offline Synchronization](offline-synchronization.md) | Offline sync |
| [Inventory Management](inventory-management.md) | Parts/van stock |
| [Crew Management](crew-management.md) | Crews |
| [Performance Best Practices](performance-best-practices.md) | Performance |
| [FSL Deployment Strategy](fsl-deployment-strategy.md) | Deploy gates |
| [Field Service Testing Best Practices](field-service-testing-best-practices.md) | Synthesis |
""",
    )

    playbooks = [
        ("Work Order Testing Playbook", "work-order-testing.md",
         "Validate WO/WOLI lifecycle from create through close.",
         ["WO types", "Status model", "Linked SA and inventory"],
         ["Map status transitions.", "Execute happy path and skip-status negatives.", "Verify child SA and consumption.", "Capture SOQL stubs."],
         ["Maintenance-generated WO in scope?"],
         ["Work Order Test Report"],
         ["Status transitions enforced", "Child SA linked"],
         ["Automation conflict → MIA"],
         f"[{mia}]({mia})"),
        ("Scheduling Validation Playbook", "scheduling-validation.md",
         "Validate scheduling policy, candidates, and conflicts.",
         ["Scheduling policy", "Resources", "Territory and skills"],
         ["Build candidate eligibility matrix.", "Test conflicts and emergency insert.", "Document Scheduling Assessment."],
         ["Optimization in scope this release?"],
         ["Scheduling Validation Report"],
         ["No double booking", "Skills/territory enforced"],
         ["Systemic mis-schedule → FSL Architect"],
         ""),
        ("Dispatcher Console Testing Playbook", "dispatcher-console-testing.md",
         "Validate dispatcher assign/reschedule console behavior.",
         ["Dispatcher persona", "Gantt/list views", "Alerts"],
         ["Assign/unassign/reschedule.", "Filter by territory.", "Negative: unqualified resource."],
         ["Multi-territory dispatcher?"],
         ["Dispatcher Review Report"],
         ["Assignments persist", "Unauthorized assign blocked"],
         ["Access gap → PTA"],
         f"[{pta}]({pta})"),
        ("Mobile Offline Testing Playbook", "mobile-offline-testing.md",
         "Validate offline execution and sync integrity.",
         ["Mobile build", "Offline dataset", "Conflict scenarios"],
         ["Go offline → complete SA → sync.", "Induce conflict with desktop change.", "Verify photos/signatures if in scope."],
         ["Background sync enabled?"],
         ["Offline Validation Checklist", "Mobile Testing Checklist"],
         ["No data loss", "Conflicts resolved per design"],
         ["Data loss → Critical"],
         f"[{mobile}]({mobile})"),
        ("Inventory Testing Playbook", "inventory-testing.md",
         "Validate van stock, requests, consumption, transfers.",
         ["Products", "Locations", "WOLI consumption"],
         ["Consume parts on completion.", "Request/transfer stock.", "Reconcile with SOQL."],
         ["Serialized parts?"],
         ["Inventory Validation Report"],
         ["Stock balances correct", "Shortage handled"],
         ["Reconciliation fail → Data/Integration lead"],
         f"[{sova}]({sova})"),
        ("Crew Management Testing Playbook", "crew-management-testing.md",
         "Validate crew composition and multi-resource scheduling.",
         ["Crews", "Members", "Capacity rules"],
         ["Schedule crew SA.", "Remove member mid-plan.", "Validate capacity."],
         ["Mixed skill crews?"],
         ["Crew section in FSL report"],
         ["Unavailable member blocked"],
         ["Capacity defect → FSL Architect"],
         ""),
        ("Optimization Testing Playbook", "optimization-testing.md",
         "Validate optimization runs without inventing scores.",
         ["Optimization scope", "Baseline schedule", "Timeout policy"],
         ["Run optimization in sandbox.", "Compare conflict reduction qualitatively.", "Test timeout/partial results."],
         ["LDV territory?"],
         ["Optimization section + Performance Assessment"],
         ["Conflicts reduced or explained", "Timeout handled"],
         ["Timeout → Performance Architect"],
         ""),
        ("Regression Testing Playbook", "regression-testing.md",
         "Select risk-based FSL regression after config/metadata change.",
         ["Change list", "Prior packs", "MIA deltas"],
         ["Map change to In/Out/Conditional.", "Re-run scheduling + offline smoke.", "Update regression checklist."],
         ["Can any territory be Out?"],
         ["Regression Checklist", "Regression Scope"],
         ["High-risk journeys revalidated"],
         ["Scope dispute → Test Lead + FSL Architect"],
         "../../playbooks/regression-planning.md"),
        ("Release Readiness Playbook", "release-readiness.md",
         "Assemble FSL release evidence and Go/No-Go.",
         ["18-section report", "Mobile evidence", "Open defects"],
         ["Complete Deployment Readiness Checklist.", "Confirm Critical=0 or accepted.", "Issue recommendation."],
         ["Residual risk accepted?"],
         ["Deployment Readiness Checklist"],
         ["Checklist complete", "Critical risks closed or accepted"],
         ["Critical open → No-Go"],
         "../../knowledge/release/release-readiness.md"),
    ]
    for title, slug, *rest in playbooks:
        write(f"playbooks/{slug}", playbook(title, slug, *rest))

    write(
        "playbooks/README.md",
        fm("Field Service QA — Playbooks", "QE Specialized Skill Playbook", "Guide", ["field-service-qa"])
        + """# Field Service QA — Playbooks

| Playbook | Focus |
|----------|-------|
| [Work Order Testing](work-order-testing.md) | WO lifecycle |
| [Scheduling Validation](scheduling-validation.md) | Scheduling |
| [Dispatcher Console Testing](dispatcher-console-testing.md) | Dispatch |
| [Mobile Offline Testing](mobile-offline-testing.md) | Offline sync |
| [Inventory Testing](inventory-testing.md) | Parts/van stock |
| [Crew Management Testing](crew-management-testing.md) | Crews |
| [Optimization Testing](optimization-testing.md) | Optimization |
| [Regression Testing](regression-testing.md) | Regression |
| [Release Readiness](release-readiness.md) | Go/No-Go |
""",
    )

    templates = [
        ("FSL Test Strategy", ["Purpose", "Scope", "Component Inventory", "Personas", "Environments", "Risks", "Entry/Exit", "Governance"]),
        ("Work Order Test Report", OUTPUT_SECTIONS),
        ("Scheduling Validation Report", ["Policy", "Candidates", "Conflicts", "Emergency", "Results", "Gaps"]),
        ("Dispatcher Review Report", ["Persona", "Assign Paths", "Filters", "Negatives", "Access Issues", "Recommendations"]),
        ("Mobile Testing Checklist", ["Login", "Online", "Offline", "GPS", "Media", "Performance", "Status"]),
        ("Offline Validation Checklist", ["Dataset", "Mutations Offline", "Sync", "Conflicts", "Data Loss Check", "Sign-off"]),
        ("Inventory Validation Report", ["Locations", "Consumption", "Requests", "Transfers", "Reconciliation", "Gaps"]),
        ("Regression Checklist", ["Change Summary", "In Scope", "Scheduling Smoke", "Offline Smoke", "Inventory Smoke", "Sign-off"]),
        ("Deployment Readiness Checklist", ["Config Complete", "Scheduling Evidence", "Mobile Evidence", "Security Sign-off", "Open Defects", "Go/No-Go"]),
    ]
    for title, sections in templates:
        slug = title.lower().replace(" ", "-") + ".md"
        write(f"templates/{slug}", template_doc(title, sections))

    write(
        "templates/README.md",
        fm("Field Service QA — Templates", "QE Specialized Skill Template", "Guide", ["field-service-qa"])
        + """# Field Service QA — Templates

| Template | Use |
|----------|-----|
| [FSL Test Strategy](fsl-test-strategy.md) | Program strategy |
| [Work Order Test Report](work-order-test-report.md) | Primary 18-section deliverable |
| [Scheduling Validation Report](scheduling-validation-report.md) | Scheduling |
| [Dispatcher Review Report](dispatcher-review-report.md) | Dispatch |
| [Mobile Testing Checklist](mobile-testing-checklist.md) | Mobile |
| [Offline Validation Checklist](offline-validation-checklist.md) | Offline |
| [Inventory Validation Report](inventory-validation-report.md) | Inventory |
| [Regression Checklist](regression-checklist.md) | Regression |
| [Deployment Readiness Checklist](deployment-readiness-checklist.md) | Release |
""",
    )

    base = (
        "Act as Salesforce Field Service QA capability. Provide Business Scenario and FSL Components Reviewed "
        "BEFORE detailed test cases. Produce all 18 sections per SKILL.md. Cover scheduling, mobile/offline, "
        "and inventory when in scope. Label assumptions; do not invent optimization scores or SLA values. Context:\n[paste]"
    )
    prompts = [
        ("Review Work Order Flow", "review-work-order-flow.md", base, OUTPUT_SECTIONS),
        ("Validate Scheduling Policy", "validate-scheduling-policy.md", base + "\nFocus: Scheduling Assessment and policy rules.", OUTPUT_SECTIONS),
        ("Review Dispatcher Console", "review-dispatcher-console.md", base + "\nFocus: Dispatcher Assessment and access.", OUTPUT_SECTIONS),
        ("Validate Mobile Offline Sync", "validate-mobile-offline-sync.md", base + "\nFocus: Mobile Assessment and Offline Validation.", OUTPUT_SECTIONS),
        ("Review Inventory Process", "review-inventory-process.md", base + "\nFocus: Inventory Assessment and SOQL stubs.", OUTPUT_SECTIONS),
        ("Review Crew Scheduling", "review-crew-scheduling.md", base + "\nFocus: Crew assignment and capacity.", OUTPUT_SECTIONS),
        ("Validate Optimization Rules", "validate-optimization-rules.md", base + "\nFocus: Optimization and Performance Assessment.", OUTPUT_SECTIONS),
        ("Generate FSL Test Cases", "generate-fsl-test-cases.md", base + "\nFocus: Negative and Edge Case sections after component inventory.", OUTPUT_SECTIONS),
        ("Assess Production Readiness", "assess-production-readiness.md", base + "\nFocus: Deployment Readiness, Risks, Recommendations.", OUTPUT_SECTIONS),
        ("Analyze FSL Defects", "analyze-fsl-defects.md", base + "\nFocus: defect clustering across schedule/mobile/inventory; recommend RCA themes.", OUTPUT_SECTIONS),
    ]
    for title, slug, prompt, sections in prompts:
        write(f"prompts/{slug}", prompt_doc(title, prompt, sections))

    write(
        "prompts/README.md",
        fm("Field Service QA — Prompts", "QE Specialized Skill Prompt", "Guide", ["field-service-qa"])
        + """# Field Service QA — Prompts

| Prompt | File |
|--------|------|
| Review Work Order Flow | [review-work-order-flow.md](review-work-order-flow.md) |
| Validate Scheduling Policy | [validate-scheduling-policy.md](validate-scheduling-policy.md) |
| Review Dispatcher Console | [review-dispatcher-console.md](review-dispatcher-console.md) |
| Validate Mobile Offline Sync | [validate-mobile-offline-sync.md](validate-mobile-offline-sync.md) |
| Review Inventory Process | [review-inventory-process.md](review-inventory-process.md) |
| Review Crew Scheduling | [review-crew-scheduling.md](review-crew-scheduling.md) |
| Validate Optimization Rules | [validate-optimization-rules.md](validate-optimization-rules.md) |
| Generate FSL Test Cases | [generate-fsl-test-cases.md](generate-fsl-test-cases.md) |
| Assess Production Readiness | [assess-production-readiness.md](assess-production-readiness.md) |
| Analyze FSL Defects | [analyze-fsl-defects.md](analyze-fsl-defects.md) |
""",
    )

    examples = [
        ("Emergency Utility Outage", "emergency-utility-outage.md",
         "Storm outage requires emergency SA insert ahead of planned work.",
         "WO, SA, Emergency Work Type, Territory, Scheduling Policy, Dispatcher Console.",
         "Emergency priority overrides planned; same resource cannot double-book.",
         "Prove emergency SA scheduled; planned SA rescheduled or flagged.",
         "Assigned Resource set; Status transitions valid.",
         "Emergency SA assigned; no overlapping SA for resource.",
         "Assign emergency to resource already In Progress without rule.",
         "SELECT Id, Status, SchedStartTime, SchedEndTime FROM ServiceAppointment WHERE WorkType.Name = 'Emergency' LIMIT 20",
         "Chain PTA for dispatcher; SOVA for overlap detection."),
        ("Water Meter Installation", "water-meter-installation.md",
         "New residential meter install with skill Plumber and van parts.",
         "WO, WOLI, SA, Skill Requirements, Product Required, Mobile.",
         "Skill match required; operating hours 8–17; parts reserved.",
         "Skill enforcement; parts consumption on complete; mobile photo.",
         "Products Consumed rows; Assigned Resource skills.",
         "Only plumber resources candidates; stock decremented.",
         "Unskilled tech assigned; complete without consuming part.",
         "SELECT Id FROM AssignedResource WHERE ServiceResourceId = :resId",
         "Inventory reconciliation via SOVA."),
        ("Smart Meter Replacement", "smart-meter-replacement.md",
         "Utilities planned replacement with maintenance plan generation.",
         "Maintenance Plan, Maintenance Asset, WO, SA, Work Type.",
         "Monthly generation; asset coverage complete.",
         "Generated WO exists for due assets; appointments created.",
         "WO Parent MaintenancePlanId populated.",
         "Due assets have open WO; none missing.",
         "Asset due with no WO generated.",
         "SELECT Id FROM WorkOrder WHERE MaintenancePlanId = :mpId",
         "Regression after maintenance plan config change."),
        ("Planned Maintenance Visit", "planned-maintenance-visit.md",
         "HVAC annual maintenance with entitlement SLA window.",
         "WO, SA, Entitlement, Operating Hours, Service Report.",
         "Must complete within entitlement window; service report required.",
         "SLA window respected; report generated on complete.",
         "SA Completed; ServiceReport exists.",
         "Within window; report attached.",
         "Complete outside window without override.",
         "SELECT Id FROM ServiceReport WHERE ParentId = :saId",
         "Do not invent SLA hours—use program entitlement."),
        ("Broadband Installation", "broadband-installation.md",
         "Telecom install requiring two-day multi-appointment project.",
         "WO, multiple SA, Crew optional, Territory.",
         "Day1 survey + Day2 install; same customer address.",
         "Sequence preserved; resources available both days.",
         "SA Parent WorkOrderId; dates sequential.",
         "No overlapping day conflict; status flow correct.",
         "Day2 before Day1 scheduled.",
         "SELECT Id, SchedStartTime FROM ServiceAppointment WHERE ParentRecordId = :woId ORDER BY SchedStartTime",
         "Edge: weather cancel and reschedule."),
        ("HVAC Service Visit", "hvac-service-visit.md",
         "Break-fix HVAC with parts transfer from warehouse to van.",
         "WO, Product Transfer, Product Request, Mobile offline.",
         "Parts transfer before dispatch; offline complete allowed.",
         "Transfer completed; offline sync preserves consumption.",
         "ProductTransfer status; Products Consumed.",
         "Stock moved; SA completed after sync.",
         "Offline complete then desktop deletes SA.",
         "SELECT Id, QuantityConsumed FROM ProductConsumed WHERE WorkOrderId = :woId",
         "Offline conflict Critical if data loss."),
        ("Telecom Field Repair", "telecom-field-repair.md",
         "Network node repair with GPS and barcode scan of asset.",
         "SA, Asset, Mobile GPS, Barcode, Service Report.",
         "Must scan correct asset tag; GPS near site.",
         "Wrong barcode blocked; GPS captured if configured.",
         "AssetId on WO; geolocation fields if used.",
         "Correct asset linked; report filed.",
         "Scan unrelated asset succeeds incorrectly.",
         "SELECT Id, AssetId FROM WorkOrder WHERE Id = :woId",
         "Mobile performance on poor network."),
        ("Medical Equipment Service", "medical-equipment-service.md",
         "Healthcare biomedical device PM with regulated access.",
         "WO, SA, Restricted sharing, Technician perm set, Service Report.",
         "Only certified tech; PHI fields hidden.",
         "PTA for FLS/sharing; certified skill enforced.",
         "Skill match; FLS on patient fields.",
         "Unauthorized tech cannot see PHI.",
         "Dispatcher assigns uncertified tech.",
         "SELECT Id FROM ServiceResourceSkill WHERE Skill.DeveloperName = 'Biomed'",
         "Chain PTA; compliance advisory for PHI."),
        ("Asset Inspection", "asset-inspection.md",
         "Public sector asset inspection with checklist and photos.",
         "WO, SA, Mobile photos, Service Report, Territory.",
         "Photos required before Complete; territory match.",
         "Cannot complete without photos; territory enforced.",
         "ContentDocumentLink or photo custom objects per org.",
         "Complete blocked until media present.",
         "Complete without photos via API.",
         "SELECT Id FROM ContentDocumentLink WHERE LinkedEntityId = :saId",
         "API bypass negative required."),
        ("Multi-Day Field Project", "multi-day-field-project.md",
         "Manufacturing plant shutdown multi-day crew project.",
         "WO, Crew, multiple SA, Optimization optional, Inventory staging.",
         "Crew capacity across days; staged parts available Day1.",
         "Crew scheduled all days; inventory staged.",
         "Crew members AssignedResource; ProductRequest fulfilled.",
         "No missing day; parts available.",
         "Optimization moves Day3 over capacity.",
         "SELECT ServiceResourceId FROM AssignedResource WHERE ServiceAppointmentId IN :saIds",
         "Optimization qualitative only—no invented scores."),
    ]
    for title, slug, scenario, components, rules, objectives, backend, expected, negative, soql, qa in examples:
        write(f"examples/{slug}", example_doc(title, scenario, components, rules, objectives, backend, expected, negative, soql, qa))

    write(
        "examples/README.md",
        fm("Field Service QA — Examples", "QE Specialized Skill Example", "Guide", ["field-service-qa"])
        + """# Field Service QA — Examples

| Example | Domain |
|---------|--------|
| [Emergency Utility Outage](emergency-utility-outage.md) | Utilities |
| [Water Meter Installation](water-meter-installation.md) | Utilities |
| [Smart Meter Replacement](smart-meter-replacement.md) | Utilities |
| [Planned Maintenance Visit](planned-maintenance-visit.md) | Maintenance |
| [Broadband Installation](broadband-installation.md) | Telecom |
| [HVAC Service Visit](hvac-service-visit.md) | Facilities |
| [Telecom Field Repair](telecom-field-repair.md) | Telecom |
| [Medical Equipment Service](medical-equipment-service.md) | Healthcare |
| [Asset Inspection](asset-inspection.md) | Public Sector |
| [Multi-Day Field Project](multi-day-field-project.md) | Manufacturing |
""",
    )

    tests = [
        ("work-order-lifecycle", "WO status transitions before case laundry list"),
        ("appointment-scheduling", "Scheduling Assessment with conflict negatives"),
        ("dispatcher-assignment", "Dispatcher Assessment and access"),
        ("territory-rules", "Territory enforcement tested"),
        ("skills-matching", "Skill match/mismatch covered"),
        ("crew-scheduling", "Crew capacity scenarios present"),
        ("offline-synchronization", "Offline Validation with conflict path"),
        ("inventory-consumption", "Inventory Assessment with SOQL stubs"),
        ("mobile-performance", "Mobile Assessment notes perf risks without invented timings"),
        ("security", "Security Assessment chains PTA themes"),
        ("regression", "Regression Scope In/Out/Conditional"),
        ("production-readiness", "Deployment Readiness with Go/No-Go rationale"),
    ]
    for slug, desc in tests:
        write(
            f"tests/scenario-{slug}.md",
            fm(f"Test — {slug}", "QE Specialized Skill Test", "Test Scenario", ["field-service-qa"])
            + f"""# Test Scenario — {slug}

## Objective

{desc}

## Pass Criteria

- Business Scenario and FSL Components Reviewed before detailed cases
- Assumptions labeled; no invented optimization/SLA %
- SOQL stubs present when backend proof needed

## Fail Criteria

- Work Order CRUD-only pack without scheduling/mobile/inventory when in scope
- Invented metrics
- Missing negative scheduling or offline conflict when claimed in scope
""",
        )

    write(
        "tests/README.md",
        fm("Field Service QA — Tests", "QE Specialized Skill Test", "Guide", ["field-service-qa"])
        + """# Field Service QA — Tests

| Scenario | Focus |
|----------|-------|
| [work-order-lifecycle](scenario-work-order-lifecycle.md) | WO lifecycle |
| [appointment-scheduling](scenario-appointment-scheduling.md) | Scheduling |
| [dispatcher-assignment](scenario-dispatcher-assignment.md) | Dispatch |
| [territory-rules](scenario-territory-rules.md) | Territory |
| [skills-matching](scenario-skills-matching.md) | Skills |
| [crew-scheduling](scenario-crew-scheduling.md) | Crews |
| [offline-synchronization](scenario-offline-synchronization.md) | Offline |
| [inventory-consumption](scenario-inventory-consumption.md) | Inventory |
| [mobile-performance](scenario-mobile-performance.md) | Mobile perf |
| [security](scenario-security.md) | Security |
| [regression](scenario-regression.md) | Regression |
| [production-readiness](scenario-production-readiness.md) | Release |
""",
    )

    print("Done.")


if __name__ == "__main__":
    main()
