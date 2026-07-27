"""Generate Salesforce Data Migration QA (DMQA) skill pack."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP = ROOT / "skills" / "data-migration-qa"
VERSION = "0.23.0"
DATE = "2026-07-27"

OUTPUT_SECTIONS = [
    "Executive Summary",
    "Migration Scope",
    "Source System Assessment",
    "Target System Assessment",
    "Data Mapping Review",
    "Transformation Validation",
    "Relationship Validation",
    "Record Count Validation",
    "Data Quality Assessment",
    "Reconciliation Strategy",
    "Security Assessment",
    "Performance Assessment",
    "Negative Test Scenarios",
    "Regression Scope",
    "Automation Opportunities",
    "Recommended SOQL Validation",
    "Cutover Readiness",
    "Rollback Readiness",
    "Hypercare Validation",
    "Risks and Recommendations",
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
    return fm(title, "QE Specialized Skill Knowledge", "Knowledge Article", ["data-migration-qa", "knowledge"]) + f"""# {title}

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
    return fm(title, "QE Specialized Skill Playbook", "Playbook", ["data-migration-qa", "playbook"]) + f"""# {title}

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
    return fm(title, "QE Specialized Skill Template", "Template", ["data-migration-qa", "template"]) + f"""# {title}

{body}

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {VERSION} | {DATE} | QE Practice Lead | Initial template |
"""


def prompt_doc(title, prompt, sections):
    return fm(title, "QE Specialized Skill Prompt", "Prompt", ["data-migration-qa", "prompt"]) + f"""# {title}

## Prompt

```
{prompt}
```

## Required Output Sections

{chr(10).join(f"{i}. {s}" for i, s in enumerate(sections, 1))}

## Quality Gate

- Migration Scope + Source/Target Assessment BEFORE detailed validation cases.
- Label assumptions; do not invent throughput/duration or SLA percentages.
- Do not claim GDPR certification; flag Legal/Compliance when needed.
- Chain MIA / SOVA / PTA / TDG / PWR / OSQA / AFT when applicable.
"""


def example_doc(title, scenario, source, target, mapping, transform, validation, soql, expected, negatives, qa):
    return fm(title, "QE Specialized Skill Example", "Example", ["data-migration-qa", "example"]) + f"""# {title}

## Business Scenario

{scenario}

## Source Data

{source}

## Target Data Model

{target}

## Mapping Rules

{mapping}

## Transformation Rules

{transform}

## Validation Strategy

{validation}

## SOQL Verification

{soql}

## Expected Results

{expected}

## Negative Scenarios

{negatives}

## QA Recommendations

{qa}
"""


def test_doc(title, purpose, preconditions, steps, asserts, chains):
    return fm(title, "QE Specialized Skill Test", "Test Scenario", ["data-migration-qa", "test"]) + f"""# {title}

## Purpose

{purpose}

## Preconditions

{chr(10).join(f"- {p}" for p in preconditions)}

## Steps

{chr(10).join(f"{i}. {s}" for i, s in enumerate(steps, 1))}

## Assertions

{chr(10).join(f"- {a}" for a in asserts)}

## Capability Chains

{chr(10).join(f"- {c}" for c in chains)}

## Notes

- Document Migration Scope and Source/Target Assessment before expanding detailed cases.
- Do not invent throughput, duration, or SLA percentages.
"""


def main() -> None:
    print("Generating Data Migration QA skill pack...")
    CAP.mkdir(parents=True, exist_ok=True)

    data = "../../knowledge/data"
    mig = f"{data}/data-migration-validation.md"
    recon = f"{data}/data-reconciliation.md"
    dq = f"{data}/data-quality.md"
    loader = f"{data}/data-loader.md"
    refint = f"{data}/referential-integrity.md"
    pii = f"{data}/pii-considerations.md"
    gdpr = f"{data}/gdpr-awareness.md"
    ldv = f"{data}/large-data-volumes.md"
    mask = f"{data}/data-masking.md"
    mia = "../../skills/metadata-impact-analyzer/SKILL.md"
    sova = "../soql-validation-assistant/SKILL.md"
    pta = "../permission-testing-agent/SKILL.md"
    tdg = "../test-data-generator/SKILL.md"
    pwr = "../playwright-review/SKILL.md"
    osqa = "../omnistudio-qa/SKILL.md"
    aft = "../agentforce-testing/SKILL.md"
    sprint9 = "../../production-support/README.md"

    knowledge_specs = [
        (
            "Salesforce Data Migration Architecture",
            "salesforce-data-migration-architecture.md",
            "Assess end-to-end migration architecture before detailed validation cases.",
            [
                "Define waves, objects, volumes, and freeze windows.",
                "Map staging → transform → load → reconcile layers.",
                "Identify External ID strategy and load order.",
                "Cross-link Sprint 4A data encyclopedia — do not duplicate.",
            ],
            [("Data Migration Validation", mig), ("Large Data Volumes", ldv), ("Metadata Impact Analyzer", mia)],
            ["No Migration Scope → incomplete report.", "Missing load order → High relationship risk."],
        ),
        (
            "Migration Strategies",
            "migration-strategies.md",
            "Select and validate big-bang vs phased vs parallel-run strategies.",
            [
                "Classify full refresh vs incremental/delta.",
                "Assess business freeze and coexistence needs.",
                "Define success criteria per wave.",
                "Document residual risk for deferred history.",
            ],
            [("Data Migration Validation", mig), ("Cutover Planning", "cutover-planning.md")],
            ["Phased without delta rules → Incomplete Reconciliation Strategy."],
        ),
        (
            "ETL Fundamentals",
            "etl-fundamentals.md",
            "Validate extract/transform/load contracts and error handling.",
            [
                "Inventory extract filters and source of truth.",
                "Validate transform rules against fixtures.",
                "Confirm reject/quarantine and retry paths.",
                "Label middleware tool names TBC when unknown.",
            ],
            [("Data Mapping Best Practices", "data-mapping-best-practices.md"), ("Error Handling via pitfalls", "common-migration-pitfalls.md")],
            ["Happy-path-only ETL → Fail Negative Test Scenarios."],
        ),
        (
            "Bulk API",
            "bulk-api.md",
            "Assess Bulk API usage for migration loads without inventing timings.",
            [
                "Confirm Bulk API 1.0/2.0 intent and job design.",
                "Review batch sizing and parallelism assumptions.",
                "Flag API limit and governor risks.",
                "Require measured evidence for duration claims.",
            ],
            [("Data Loader", "data-loader.md"), ("Migration Performance", "migration-performance.md"), ("Large Data Volumes", ldv)],
            ["Invented job duration % → Anti-pattern."],
        ),
        (
            "Data Loader",
            "data-loader.md",
            "Validate Data Loader / Import Wizard patterns for controlled loads.",
            [
                "Confirm insert vs upsert vs update vs delete operations.",
                "Validate CSV headers and External ID columns.",
                "Review success/error file triage process.",
                "Prefer Bulk for LDV; document tool choice rationale.",
            ],
            [("Data Loader Encyclopedia", loader), ("External IDs", "external-ids.md")],
            ["UI Import Wizard for LDV without rationale → Performance risk."],
        ),
        (
            "External IDs",
            "external-ids.md",
            "Validate External ID uniqueness and upsert keys.",
            [
                "Inventory External ID fields per object.",
                "Test uniqueness and null External ID behavior.",
                "Confirm upsert matching rules.",
                "Recommend SOVA stubs for duplicate External IDs.",
            ],
            [("Upsert Strategy", "upsert-strategy.md"), ("SOQL Validation Assistant", sova)],
            ["Non-unique External ID → Critical integrity risk."],
        ),
        (
            "Upsert Strategy",
            "upsert-strategy.md",
            "Validate upsert vs insert/update decisioning for re-runs and deltas.",
            [
                "Define idempotent re-run rules.",
                "Cover insert-only vs upsert collision paths.",
                "Document merge/delete policies separately.",
                "Align with incremental/delta strategy.",
            ],
            [("External IDs", "external-ids.md"), ("Migration Strategies", "migration-strategies.md")],
            ["Re-run without upsert plan → Cutover No-Go risk."],
        ),
        (
            "Record Ownership",
            "record-ownership.md",
            "Validate OwnerId mapping, queues, and post-migrate sharing impact.",
            [
                "Map legacy owners to Salesforce users/queues.",
                "Validate inactive user / default owner rules.",
                "Assess OWD/sharing after ownership change.",
                "Chain PTA for persona visibility.",
            ],
            [("Permission Testing Agent", pta), ("Migration Security", "migration-security.md")],
            ["All records owned by admin → Security/visibility defect."],
        ),
        (
            "Relationship Migration",
            "relationship-migration.md",
            "Validate parent-child load order and relationship integrity.",
            [
                "Document dependency graph (Account→Contact→Opportunity…).",
                "Validate lookup vs master-detail behaviors.",
                "Detect orphans and broken references.",
                "Include ContentDocumentLink / attachment parents.",
            ],
            [("Lookup Resolution", "lookup-resolution.md"), ("Referential Integrity", refint)],
            ["Child before parent without External ID resolve → Fail Relationship Validation."],
        ),
        (
            "Lookup Resolution",
            "lookup-resolution.md",
            "Validate how lookups are resolved via External ID, staging keys, or post-update.",
            [
                "Classify resolve-at-load vs two-pass update.",
                "Test missing-parent and multi-match cases.",
                "Document default/null lookup policy.",
                "Recommend exception reports for unresolved keys.",
            ],
            [("Relationship Migration", "relationship-migration.md"), ("SOQL Validation Assistant", sova)],
            ["Silent null on required lookup → Critical."],
        ),
        (
            "Data Mapping Best Practices",
            "data-mapping-best-practices.md",
            "Assess field-level mapping completeness and business correctness.",
            [
                "Trace source→target for every in-scope field.",
                "Flag unmapped mandatory and unused targets.",
                "Validate picklist/record type maps.",
                "Chain MIA when new fields required for migration.",
            ],
            [("Data Migration Validation", mig), ("Metadata Impact Analyzer", mia)],
            ["Mapping gaps on required fields → Block Cutover Readiness."],
        ),
        (
            "Data Quality Framework",
            "data-quality-framework.md",
            "Evaluate completeness, accuracy, consistency, validity, uniqueness, timeliness.",
            [
                "Profile nulls, formats, and duplicates pre-load.",
                "Validate cleansing rules with fixtures.",
                "Define DQ thresholds and exception owners.",
                "Do not invent DQ % without evidence.",
            ],
            [("Data Quality Encyclopedia", dq), ("Common Migration Pitfalls", "common-migration-pitfalls.md")],
            ["No DQ Assessment when cleansing claimed → Incomplete."],
        ),
        (
            "Reconciliation Techniques",
            "reconciliation-techniques.md",
            "Design count, aggregate, financial, and sample-journey reconciliation.",
            [
                "Define tolerances and exception criteria.",
                "Produce SOQL stubs for SOVA expansion.",
                "Cover delta/incremental reconcile.",
                "Include business journey smoke after counts.",
            ],
            [("Data Reconciliation Encyclopedia", recon), ("SOQL Validation Assistant", sova)],
            ["Counts-only with no field sample → Weak Reconciliation Strategy."],
        ),
        (
            "Migration Performance",
            "migration-performance.md",
            "Assess batch size, parallelism, API limits without inventing SLAs.",
            [
                "Identify LDV and chatty transform risks.",
                "Document batch/parallel assumptions.",
                "Recommend measurement plan.",
                "Label any duration claims as assumptions or evidence.",
            ],
            [("Large Data Volumes", ldv), ("Bulk API", "bulk-api.md")],
            ["Invented throughput % → Anti-pattern."],
        ),
        (
            "Migration Security",
            "migration-security.md",
            "Assess CRUD/FLS, PII, masking, and audit field handling.",
            [
                "Classify PII fields; prefer masked dry-run (TDG).",
                "Validate CRUD/FLS for post-migrate personas (PTA).",
                "Review encryption/audit field expectations.",
                "Never claim GDPR certification — escalate Legal/Compliance.",
            ],
            [("PII Considerations", pii), ("GDPR Awareness", gdpr), ("Data Masking", mask), ("Permission Testing Agent", pta), ("Test Data Generator", tdg)],
            ["Production PII in dry-run artifacts → Critical escalate Security."],
        ),
        (
            "Cutover Planning",
            "cutover-planning.md",
            "Assess cutover readiness gates and freeze windows.",
            [
                "Confirm Migration Scope and mapping gates passed.",
                "Define Go / Conditional Go / No-Go criteria.",
                "Document communications and ownership.",
                "Link Rollback and Hypercare plans.",
            ],
            [("Rollback Planning", "rollback-planning.md"), ("Hypercare Activities", "hypercare-activities.md")],
            ["Open Critical integrity defects → No-Go."],
        ),
        (
            "Rollback Planning",
            "rollback-planning.md",
            "Validate rollback triggers, restore approach, and residual risk.",
            [
                "Define rollback triggers and decision owner.",
                "Document restore vs compensate strategies.",
                "Test rollback validation scenarios (advisory).",
                "Note irreversible deletes / merges.",
            ],
            [("Cutover Planning", "cutover-planning.md")],
            ["No rollback plan for production cutover → No-Go."],
        ),
        (
            "Hypercare Activities",
            "hypercare-activities.md",
            "Define migration Day-1–N validation vs general ops hypercare.",
            [
                "List Day-1 count/DQ/journey checks.",
                "Define defect triage themes for migration issues.",
                "Chain Sprint 9 for Sev1 ops; keep migration DQ in DMQA.",
                "Do not invent MTTR/SLA values.",
            ],
            [("Production Support", sprint9), ("Reconciliation Techniques", "reconciliation-techniques.md")],
            ["General outage without migration context → Sprint 9 primary."],
        ),
        (
            "Common Migration Pitfalls",
            "common-migration-pitfalls.md",
            "Catalog frequent migration defects and preventive checks.",
            [
                "Duplicates, orphans, wrong owners, picklist mismatches.",
                "Silent upsert collisions and partial batch failures.",
                "Attachment/File gaps and ContentDocumentLink misses.",
                "Count match with wrong field values.",
            ],
            [("Data Quality Framework", "data-quality-framework.md"), ("Relationship Migration", "relationship-migration.md")],
            ["Every DMQA report should address applicable pitfalls explicitly."],
        ),
    ]
    for spec in knowledge_specs:
        write(f"knowledge/{spec[1]}", knowledge_article(*spec))

    write(
        "knowledge/README.md",
        fm("Data Migration QA — Knowledge", "QE Specialized Skill Knowledge", "Guide", ["data-migration-qa"])
        + """# Data Migration QA — Knowledge

Canonical encyclopedia: [`../../knowledge/data/`](../../knowledge/data/README.md). These articles provide **DMQA reasoning models** only — do not duplicate encyclopedia bodies. SOQL depth: [SOQL Validation Assistant](../soql-validation-assistant/SKILL.md).

| Document | Focus |
|----------|-------|
| [Salesforce Data Migration Architecture](salesforce-data-migration-architecture.md) | End-to-end architecture |
| [Migration Strategies](migration-strategies.md) | Big-bang / phased / delta |
| [ETL Fundamentals](etl-fundamentals.md) | Extract / transform / load |
| [Bulk API](bulk-api.md) | Bulk load design |
| [Data Loader](data-loader.md) | Loader / Import Wizard |
| [External IDs](external-ids.md) | Upsert keys |
| [Upsert Strategy](upsert-strategy.md) | Idempotent loads |
| [Record Ownership](record-ownership.md) | OwnerId / queues |
| [Relationship Migration](relationship-migration.md) | Load order / integrity |
| [Lookup Resolution](lookup-resolution.md) | Parent key resolve |
| [Data Mapping Best Practices](data-mapping-best-practices.md) | Field maps |
| [Data Quality Framework](data-quality-framework.md) | DQ dimensions |
| [Reconciliation Techniques](reconciliation-techniques.md) | Counts / aggregates |
| [Migration Performance](migration-performance.md) | Perf risks (no invented %) |
| [Migration Security](migration-security.md) | PII / FLS / compliance advisory |
| [Cutover Planning](cutover-planning.md) | Go / No-Go |
| [Rollback Planning](rollback-planning.md) | Rollback readiness |
| [Hypercare Activities](hypercare-activities.md) | Day-1–N migration checks |
| [Common Migration Pitfalls](common-migration-pitfalls.md) | Defect themes |

## Related Documents

- [SKILL.md](../SKILL.md)
""",
    )

    playbook_specs = [
        (
            "Data Profiling Playbook",
            "data-profiling.md",
            "Profile source data quality before mapping and load.",
            ["Source extracts (sanitized)", "Volume estimates", "PII classification"],
            [
                "Confirm Migration Scope.",
                "Profile nulls, formats, duplicates, orphans.",
                "Document DQ risks and cleansing candidates.",
                "Recommend TDG/masking for dry-run if PII present.",
            ],
            ["Production PII in samples → escalate Security; use masked data."],
            ["Source System Assessment + Data Quality Assessment sections"],
            ["Profiling findings with owners", "Assumptions labeled"],
            ["Critical PII exposure → Security / Data Governance"],
            "knowledge/data-quality-framework.md",
        ),
        (
            "Data Mapping Review Playbook",
            "data-mapping-review.md",
            "Review field and relationship mapping completeness and correctness.",
            ["Mapping workbook", "Target schema", "Mandatory fields / VRs"],
            [
                "Trace source→target for in-scope objects.",
                "Validate picklist/record type maps.",
                "Flag gaps on required fields.",
                "Chain MIA if new metadata needed.",
            ],
            ["Required field unmapped → Block Cutover."],
            ["Data Mapping Review section", "Transformation Validation notes"],
            ["Mapping coverage documented"],
            ["Schema mismatch blocking load → Data Architect"],
            "knowledge/data-mapping-best-practices.md",
        ),
        (
            "Data Migration Validation Playbook",
            "data-migration-validation.md",
            "Validate end-to-end migration lifecycle (mapping through load outcomes).",
            ["Scope", "Mapping", "Load results / error files", "Personas"],
            [
                "Confirm Scope + Source/Target Assessment.",
                "Validate transforms and relationships.",
                "Review counts and sample field accuracy.",
                "Populate negatives and SOQL stubs.",
            ],
            ["Count-only pack when mapping in scope → Fail quality gate."],
            ["20-section report draft", "SOVA stubs"],
            ["Lifecycle coverage evidenced"],
            ["Critical integrity fail → Release Manager"],
            "knowledge/salesforce-data-migration-architecture.md",
        ),
        (
            "Data Reconciliation Playbook",
            "data-reconciliation.md",
            "Design and execute reconciliation strategy (counts, aggregates, samples).",
            ["Source totals", "Target SOQL stubs", "Tolerances", "Financial keys if any"],
            [
                "Define reconcile dimensions and tolerances.",
                "Produce count/aggregate/exception stubs for SOVA.",
                "Sample business journeys after counts.",
                "Document residual exceptions.",
            ],
            ["Financial mismatch beyond tolerance → No-Go / escalate."],
            ["Reconciliation Strategy + Recommended SOQL Validation"],
            ["Tolerances and owners documented"],
            ["Unresolved financial variance → Finance + Data Architect"],
            "knowledge/reconciliation-techniques.md",
        ),
        (
            "Cutover Readiness Playbook",
            "cutover-readiness.md",
            "Assess Go / Conditional Go / No-Go for migration cutover.",
            ["Validation evidence", "Defect residual risk", "Freeze window", "Rollback plan"],
            [
                "Confirm gates: mapping, relationships, reconciliation, security.",
                "Review Performance residual risk (labeled).",
                "Confirm Rollback Readiness present.",
                "Record decision with owners.",
            ],
            ["Open Critical defects → No-Go."],
            ["Cutover Readiness + Risks and Recommendations"],
            ["Decision recorded with evidence links"],
            ["PII / integrity Critical open → Security + Release Manager"],
            "knowledge/cutover-planning.md",
        ),
        (
            "Rollback Validation Playbook",
            "rollback-validation.md",
            "Validate rollback triggers, restore approach, and verification.",
            ["Rollback plan", "Irreversible operations list", "Backup/staging evidence"],
            [
                "Enumerate rollback triggers.",
                "Validate restore vs compensate paths.",
                "Define post-rollback reconcile checks.",
                "Document residual risk if rollback partial.",
            ],
            ["No rollback for prod cutover → No-Go."],
            ["Rollback Readiness section"],
            ["Triggers and owners clear"],
            ["Irreversible merge without approve → Release Manager"],
            "knowledge/rollback-planning.md",
        ),
        (
            "Hypercare Validation Playbook",
            "hypercare-validation.md",
            "Define Day-1–N migration hypercare validation vs Sprint 9 ops hypercare.",
            ["Cutover decision", "Day-1 checklist", "Defect channels"],
            [
                "List Day-1 count/DQ/journey checks.",
                "Define escalation for migration vs Sev1 ops.",
                "Chain Sprint 9 for outages; keep DQ in DMQA.",
                "Do not invent MTTR/SLA.",
            ],
            ["Sev1 outage → Sprint 9 primary with DMQA support if data-caused."],
            ["Hypercare Validation section"],
            ["Day-1–N checks owned"],
            ["Data corruption in prod → Data Architect + Release Manager"],
            "knowledge/hypercare-activities.md",
        ),
        (
            "Post Migration QA Playbook",
            "post-migration-qa.md",
            "Validate post-load business correctness, regression, and automation opportunities.",
            ["Reconcile results", "Critical journeys", "Personas"],
            [
                "Re-run sample journeys (PWR design if UI).",
                "Validate persona visibility (PTA).",
                "Expand SOVA for lingering exceptions.",
                "Update Regression Scope and Automation Opportunities.",
            ],
            ["Journey fail after count pass → expand Regression Scope."],
            ["Regression Scope + Automation Opportunities + Risks"],
            ["Post-migrate business outcomes verified or residual risk listed"],
            ["Systemic post-migrate failure → Release Manager"],
            "knowledge/common-migration-pitfalls.md",
        ),
    ]
    for spec in playbook_specs:
        write(f"playbooks/{spec[1]}", playbook(*spec))

    write(
        "playbooks/README.md",
        fm("Data Migration QA — Playbooks", "QE Specialized Skill Playbook", "Guide", ["data-migration-qa"])
        + """# Data Migration QA — Playbooks

| Playbook | Focus |
|----------|-------|
| [Data Profiling](data-profiling.md) | Source DQ profile |
| [Data Mapping Review](data-mapping-review.md) | Field/relationship maps |
| [Data Migration Validation](data-migration-validation.md) | Lifecycle validation |
| [Data Reconciliation](data-reconciliation.md) | Counts / aggregates |
| [Cutover Readiness](cutover-readiness.md) | Go / No-Go |
| [Rollback Validation](rollback-validation.md) | Rollback gates |
| [Hypercare Validation](hypercare-validation.md) | Day-1–N |
| [Post Migration QA](post-migration-qa.md) | Post-load business QA |

## Related Documents

- [SKILL.md](../SKILL.md)
""",
    )

    write("templates/data-migration-test-strategy.md", template_doc(
        "Data Migration Test Strategy",
        [
            "Program Context",
            "In-Scope Waves and Objects",
            "Source and Target Overview",
            "Mapping and Transformation Approach",
            "Reconciliation Approach",
            "Security and PII Approach",
            "Performance Approach",
            "Environments and Entry/Exit Criteria",
            "Cutover / Rollback / Hypercare Overview",
            "Roles and RACI",
            "Risks and Assumptions",
            "Traceability",
        ],
    ))
    write("templates/data-mapping-review-report.md", template_doc(
        "Data Mapping Review Report",
        [
            "Executive Summary",
            "Migration Scope",
            "Object Inventory",
            "Field Mapping Assessment",
            "Picklist and Record Type Maps",
            "Relationship Mapping",
            "Transformation Notes",
            "Gaps and Risks",
            "Recommendations",
        ],
    ))
    write("templates/reconciliation-report.md", template_doc(
        "Data Migration Reconciliation / QA Report",
        OUTPUT_SECTIONS,
    ))
    write("templates/migration-validation-checklist.md", template_doc(
        "Migration Validation Checklist",
        [
            "Scope Confirmed",
            "Source/Target Assessed",
            "Mapping Complete",
            "Transforms Validated",
            "Relationships Validated",
            "Counts / Aggregates",
            "DQ Exceptions Owned",
            "Security / PII Gates",
            "SOQL Stubs Ready",
            "Sign-Off",
        ],
    ))
    write("templates/cutover-checklist.md", template_doc(
        "Cutover Checklist",
        [
            "Freeze Window",
            "Pre-Cutover Validation Gates",
            "Load Sequence",
            "Reconcile Gates",
            "Communications",
            "Go / Conditional Go / No-Go",
            "Hypercare Handoff",
        ],
    ))
    write("templates/rollback-checklist.md", template_doc(
        "Rollback Checklist",
        [
            "Rollback Triggers",
            "Decision Owner",
            "Restore / Compensate Steps",
            "Irreversible Operations",
            "Post-Rollback Reconcile",
            "Communications",
            "Residual Risk",
        ],
    ))
    write("templates/hypercare-checklist.md", template_doc(
        "Hypercare Checklist",
        [
            "Day-1 Count Checks",
            "Day-1 DQ / Exception Triage",
            "Day-1 Journey Smoke",
            "Day-2–N Monitoring Themes",
            "Defect Channels",
            "Escalation (DMQA vs Sprint 9)",
            "Exit Criteria",
        ],
    ))
    write("templates/migration-defect-log.md", template_doc(
        "Migration Defect Log",
        [
            "Defect ID",
            "Wave / Object",
            "Category (Mapping / Transform / Relationship / DQ / Perf / Security)",
            "Severity",
            "Observed vs Expected",
            "Root Cause Hypothesis",
            "Fix Verification",
            "Regression Addition",
            "Status",
        ],
    ))
    write("templates/data-quality-assessment-report.md", template_doc(
        "Data Quality Assessment Report",
        [
            "Executive Summary",
            "Scope",
            "Completeness",
            "Accuracy",
            "Consistency",
            "Validity",
            "Uniqueness",
            "Timeliness",
            "Orphans / Broken References",
            "Recommended Corrective Actions",
            "Risks",
        ],
    ))
    write(
        "templates/README.md",
        fm("Data Migration QA — Templates", "QE Specialized Skill Template", "Guide", ["data-migration-qa"])
        + """# Data Migration QA — Templates

| Template | Use |
|----------|-----|
| [Data Migration Test Strategy](data-migration-test-strategy.md) | Program-level strategy |
| [Data Mapping Review Report](data-mapping-review-report.md) | Mapping-focused |
| [Reconciliation Report](reconciliation-report.md) | **Primary 20-section QA report** |
| [Migration Validation Checklist](migration-validation-checklist.md) | Validation gates |
| [Cutover Checklist](cutover-checklist.md) | Cutover |
| [Rollback Checklist](rollback-checklist.md) | Rollback |
| [Hypercare Checklist](hypercare-checklist.md) | Day-1–N |
| [Migration Defect Log](migration-defect-log.md) | Defect tracking |
| [Data Quality Assessment Report](data-quality-assessment-report.md) | DQ-focused |

## Related Documents

- [SKILL.md](../SKILL.md)
""",
    )

    prompts = [
        (
            "Review Data Mapping",
            "review-data-mapping.md",
            "Load skills/data-migration-qa/SKILL.md.\nReview data mapping for migration: {{MigrationName}}.\nObjects: {{ObjectList}}.\nProduce all 20 sections with emphasis on Data Mapping Review and Transformation Validation.\nLabel assumptions; chain MIA if new fields needed.",
        ),
        (
            "Validate Migration",
            "validate-migration.md",
            "Load skills/data-migration-qa/SKILL.md.\nValidate migration lifecycle for: {{MigrationName}}.\nMigration Scope: {{Scope}}.\nProduce all 20 sections. Migration Scope + Source/Target Assessment BEFORE detailed cases.\nDo not invent throughput %.",
        ),
        (
            "Generate Reconciliation Queries",
            "generate-reconciliation-queries.md",
            "Load skills/data-migration-qa/SKILL.md.\nProduce Reconciliation Strategy and Recommended SOQL Validation stubs for {{Objects}}.\nChain SOVA for full 14-section query packs. Label tolerances and assumptions.",
        ),
        (
            "Review Transformation Rules",
            "review-transformation-rules.md",
            "Load skills/data-migration-qa/SKILL.md.\nReview transformation rules: {{TransformRules}}.\nCover null handling, type conversion, defaults, and negatives. Do not invent expected business values — use fixtures or label TBC.",
        ),
        (
            "Validate Relationships",
            "validate-relationships.md",
            "Load skills/data-migration-qa/SKILL.md.\nValidate relationship migration and lookup resolution for {{ObjectGraph}}.\nInclude load order, orphans, External ID resolve, and SOQL stubs.",
        ),
        (
            "Detect Duplicate Records",
            "detect-duplicate-records.md",
            "Load skills/data-migration-qa/SKILL.md.\nAssess duplicate detection for {{Objects}} using External ID and matching themes.\nRecommend SOVA stubs; chain TDG for synthetic duplicate fixtures if needed.",
        ),
        (
            "Validate Bulk Loads",
            "validate-bulk-loads.md",
            "Load skills/data-migration-qa/SKILL.md.\nValidate Bulk API / Data Loader design for {{Wave}}.\nCover batch size, error files, retries — no invented duration or error-rate %.",
        ),
        (
            "Assess Cutover Readiness",
            "assess-cutover-readiness.md",
            "Load skills/data-migration-qa/SKILL.md.\nAssess Cutover Readiness for {{ReleaseId}}.\nConfirm gates, residual risk, Rollback Readiness, and Go / Conditional Go / No-Go.",
        ),
        (
            "Assess Rollback Readiness",
            "assess-rollback-readiness.md",
            "Load skills/data-migration-qa/SKILL.md.\nAssess Rollback Readiness for {{MigrationName}}.\nDocument triggers, restore/compensate approach, irreversible ops, and post-rollback reconcile.",
        ),
        (
            "Generate Migration Test Cases",
            "generate-migration-test-cases.md",
            "Load skills/data-migration-qa/SKILL.md.\nMigration Scope: {{Scope}}.\nGenerate test cases ONLY after Migration Scope + Source/Target Assessment.\nInclude mapping, relationships, counts, DQ, negatives, cutover/rollback/hypercare themes.",
        ),
    ]
    for title, slug, prompt in prompts:
        write(f"prompts/{slug}", prompt_doc(title, prompt, OUTPUT_SECTIONS))

    write(
        "prompts/README.md",
        fm("Data Migration QA — Prompts", "QE Specialized Skill Prompt", "Guide", ["data-migration-qa"])
        + """# Data Migration QA — Prompts

| Prompt | File |
|--------|------|
| Review Data Mapping | [review-data-mapping.md](review-data-mapping.md) |
| Validate Migration | [validate-migration.md](validate-migration.md) |
| Generate Reconciliation Queries | [generate-reconciliation-queries.md](generate-reconciliation-queries.md) |
| Review Transformation Rules | [review-transformation-rules.md](review-transformation-rules.md) |
| Validate Relationships | [validate-relationships.md](validate-relationships.md) |
| Detect Duplicate Records | [detect-duplicate-records.md](detect-duplicate-records.md) |
| Validate Bulk Loads | [validate-bulk-loads.md](validate-bulk-loads.md) |
| Assess Cutover Readiness | [assess-cutover-readiness.md](assess-cutover-readiness.md) |
| Assess Rollback Readiness | [assess-rollback-readiness.md](assess-rollback-readiness.md) |
| Generate Migration Test Cases | [generate-migration-test-cases.md](generate-migration-test-cases.md) |

## Related Documents

- [SKILL.md](../SKILL.md)
""",
    )

    examples = [
        (
            "Legacy CRM to Sales Cloud",
            "legacy-crm-to-sales-cloud.md",
            "Migrate Accounts, Contacts, and Opportunities from legacy CRM to Sales Cloud.",
            "Legacy Account/Contact/Opportunity tables with legacy keys.",
            "Account, Contact, Opportunity; External ID LegacyCRM_Id__c.",
            "Legacy key → External ID; Owner map; Stage map.",
            "Currency normalize; closed date timezone; Stage picklist map.",
            "Counts by object; parent-child integrity; sample Opportunity amounts.",
            "SOVA stubs: COUNT by External ID; orphan Opportunity; duplicate External ID.",
            "Counts within tolerance; no orphans; stages mapped.",
            "Duplicate External ID; inactive owner; missing parent Account.",
            "Chain MIA for External ID fields; PTA for sales personas; SOVA for section 16.",
        ),
        (
            "Utilities Billing Migration",
            "utilities-billing-migration.md",
            "Migrate customer and billing account history for utilities Industries org.",
            "CIS billing accounts, service points, historical invoices (summarized).",
            "Account, custom Billing objects (API TBC), Service Point references.",
            "CIS ID → External ID; service point lookup resolve.",
            "Tariff code map; invoice status map; amount scale.",
            "Financial aggregate reconcile; relationship integrity; sample invoice.",
            "SOVA: SUM(Amount) by period; unresolved service point lookups.",
            "Financial totals within tolerance; lookups resolved.",
            "Currency scale error; orphan invoice; PII in free text.",
            "Label utility object APIs TBC; chain OSQA if Omni journeys consume billing data.",
        ),
        (
            "Customer Master Migration",
            "customer-master-migration.md",
            "Golden customer master load into Account (Household/Business).",
            "MDM customer export with survivorship flags.",
            "Account (+ record types); Contact optional link.",
            "MDM ID → External ID; record type map; address standardization.",
            "Survivorship rules; name/address cleanse.",
            "Uniqueness on External ID; DQ completeness; ownership.",
            "SOVA: duplicate External ID; null required Name.",
            "One Account per MDM ID; cleansed addresses.",
            "Conflicting survivorship; blank Name; wrong record type.",
            "Chain TDG for masked dry-run; PTA for customer service visibility.",
        ),
        (
            "Contact Migration",
            "contact-migration.md",
            "Migrate Contacts linked to migrated Accounts.",
            "Legacy Contact with Account foreign key.",
            "Contact; AccountId via External ID upsert.",
            "Email/phone normalize; Account External ID resolve.",
            "Primary flag; email lowercase; phone E.164 (if required).",
            "Parent resolve; duplicate email policy; FLS on email.",
            "SOVA: Contacts with null AccountId; duplicate Email.",
            "All Contacts linked; duplicates per policy.",
            "Missing parent; invalid email; PII in notes.",
            "Chain PTA for email FLS; SOVA for orphans.",
        ),
        (
            "Opportunity Migration",
            "opportunity-migration.md",
            "Migrate open and closed Opportunities with products optional.",
            "Legacy Opportunity + line items (optional wave).",
            "Opportunity; OpportunityLineItem if in scope.",
            "Stage/probability map; Amount; CloseDate; Account External ID.",
            "Closed Won/Lost reason map; currency convert.",
            "Amount aggregates; stage distribution; Account link.",
            "SOVA: SUM(Amount) by Stage; orphan Opportunity.",
            "Totals match fixtures; stages mapped.",
            "Negative Amount; future CloseDate on Closed Won; missing Account.",
            "Do not invent pricing; use fixtures; chain PWR for quote-to-cash journeys if UI critical.",
        ),
        (
            "Case Migration",
            "case-migration.md",
            "Migrate open and historical Cases to Service Cloud.",
            "Legacy tickets with customer/account keys.",
            "Case; Account/Contact lookups; Status/Origin maps.",
            "Legacy ticket # → External ID; Status map; Priority map.",
            "Closed Date rules; comment migration policy (TBC).",
            "Open vs closed counts; entitlement fields if any (TBC).",
            "SOVA: Case by Status; null AccountId; duplicate External ID.",
            "Statuses mapped; parents resolved.",
            "Unauthorized agent sees Cases (PTA); attachment missing.",
            "Chain PTA for agent profiles; Sprint 9 if post-go-live Case Sev1.",
        ),
        (
            "Product Migration",
            "product-migration.md",
            "Migrate Product2 / PricebookEntry catalog.",
            "Legacy product catalog and price lists.",
            "Product2; Pricebook2; PricebookEntry.",
            "SKU → ProductCode/External ID; pricebook map.",
            "Active flags; currency; unit of measure.",
            "SKU uniqueness; pricebook completeness.",
            "SOVA: duplicate ProductCode; missing standard PBE.",
            "Catalog complete per scope; prices match fixtures.",
            "Inactive product still sold; currency mismatch.",
            "Chain MIA for product custom fields; CPQ example if package data.",
        ),
        (
            "CPQ Data Migration",
            "cpq-data-migration.md",
            "Migrate CPQ product options / quote-related reference data (labels TBC).",
            "Legacy CPQ-like option/price rules export.",
            "CPQ objects as configured (API TBC) + Product2.",
            "Option relationships; price rule keys; External IDs.",
            "Option constraints; price calculation fixtures.",
            "Relationship integrity; sample quote calc (fixtures only).",
            "SOVA stubs for option parents; duplicate keys.",
            "Options resolve; fixtures match — no invented prices.",
            "Broken option parent; rule priority conflict.",
            "Label CPQ APIs TBC; chain OSQA if Omni product config journeys.",
        ),
        (
            "Experience Cloud User Migration",
            "experience-cloud-user-migration.md",
            "Migrate community users and Contact/Account links.",
            "Legacy portal users with email and profile keys.",
            "User; Contact; Account; Profile/Permission Set assignment.",
            "Email → Username policy; Contact External ID; profile map.",
            "Activation flags; locale/timezone defaults.",
            "Login persona visibility; FLS; no PII leakage in error logs.",
            "SOVA: User-Contact link; duplicate Username.",
            "Users linked; profiles correct.",
            "Guest sees restricted data; duplicate Username; inactive Contact.",
            "Chain PTA heavily; never migrate real passwords — document IdP approach TBC.",
        ),
        (
            "Historical Billing Data Migration",
            "historical-billing-data-migration.md",
            "Archive/historical invoice lines into Salesforce custom objects or Big Object (TBC).",
            "Multi-year invoice history extracts.",
            "Custom historical objects or Big Object (confirm with Architect).",
            "Invoice # + line → External ID; Account External ID.",
            "Period bucketing; amount scale; status archive map.",
            "Volume reconcile by year; sample line accuracy; performance assumptions labeled.",
            "SOVA: COUNT by Year__c; SUM(Amount); unresolved Account.",
            "Yearly totals within tolerance; samples accurate.",
            "LDV timeout (label assumption); wrong year bucket; PII in memo.",
            "Do not invent load duration; chain LDV knowledge; confirm Big Object vs custom.",
        ),
    ]
    for row in examples:
        write(f"examples/{row[1]}", example_doc(row[0], *row[2:]))

    write(
        "examples/README.md",
        fm("Data Migration QA — Examples", "QE Specialized Skill Example", "Guide", ["data-migration-qa"])
        + """# Data Migration QA — Examples

| Example | Domain |
|---------|--------|
| [Legacy CRM to Sales Cloud](legacy-crm-to-sales-cloud.md) | Sales Cloud |
| [Utilities Billing Migration](utilities-billing-migration.md) | Utilities |
| [Customer Master Migration](customer-master-migration.md) | Master data |
| [Contact Migration](contact-migration.md) | Contacts |
| [Opportunity Migration](opportunity-migration.md) | Opportunities |
| [Case Migration](case-migration.md) | Service Cloud |
| [Product Migration](product-migration.md) | Product |
| [CPQ Data Migration](cpq-data-migration.md) | CPQ |
| [Experience Cloud User Migration](experience-cloud-user-migration.md) | Experience |
| [Historical Billing Data Migration](historical-billing-data-migration.md) | Historical / LDV |

## Related Documents

- [SKILL.md](../SKILL.md)
- [SOVA Data Migration Reconciliation](../soql-validation-assistant/examples/data-migration-reconciliation.md)
""",
    )

    tests = [
        (
            "Record Count Validation",
            "scenario-record-count-validation.md",
            "Validate source vs target counts with tolerances.",
            ["Migration Scope documented", "Source totals available"],
            ["Capture source counts", "Capture target counts via SOQL stubs", "Compare to tolerance"],
            ["Variance explained or defect logged", "Scope preceded detailed cases"],
            ["SOVA for query packs"],
        ),
        (
            "Data Mapping Validation",
            "scenario-data-mapping-validation.md",
            "Validate field mapping completeness and sample accuracy.",
            ["Mapping workbook", "Sample fixtures"],
            ["Trace mandatory fields", "Sample transform outcomes", "Flag unmapped required"],
            ["No required gaps", "Samples match fixtures"],
            ["MIA if new fields"],
        ),
        (
            "Relationship Validation",
            "scenario-relationship-validation.md",
            "Validate parent-child integrity and lookup resolution.",
            ["Object graph", "External ID strategy"],
            ["Verify load order", "Query orphans", "Test missing parent"],
            ["No unexpected orphans", "Unresolved keys reported"],
            ["SOVA stubs", "Referential integrity knowledge"],
        ),
        (
            "Duplicate Detection",
            "scenario-duplicate-detection.md",
            "Detect duplicate External IDs and business keys.",
            ["External ID fields", "Matching policy"],
            ["Query duplicate External IDs", "Apply business duplicate policy", "Document exceptions"],
            ["Duplicates owned or blocked", "Policy documented"],
            ["SOVA", "TDG duplicate fixtures"],
        ),
        (
            "Transformation Validation",
            "scenario-transformation-validation.md",
            "Validate transform rules with known fixtures.",
            ["Transform rules", "Expected fixtures"],
            ["Apply happy transforms", "Null/default paths", "Invalid format negatives"],
            ["Results match fixtures only", "Negatives documented"],
            ["No invented business values"],
        ),
        (
            "Data Quality Validation",
            "scenario-data-quality-validation.md",
            "Validate DQ dimensions and cleansing outcomes.",
            ["DQ thresholds", "Profiling results"],
            ["Check completeness", "Check uniqueness", "Check orphans"],
            ["Exceptions owned", "No invented DQ %"],
            ["Data quality framework"],
        ),
        (
            "Bulk Load Validation",
            "scenario-bulk-load-validation.md",
            "Validate Bulk/Data Loader job design and error handling.",
            ["Job design", "Error file process"],
            ["Review batch assumptions", "Simulate/partial fail triage", "Confirm retry policy"],
            ["Assumptions labeled", "No invented duration %"],
            ["Bulk API / Data Loader knowledge"],
        ),
        (
            "Cutover Validation",
            "scenario-cutover-validation.md",
            "Validate cutover readiness gates.",
            ["Validation evidence", "Rollback plan"],
            ["Check mapping/reconcile/security gates", "Confirm freeze window", "Record Go decision"],
            ["Critical open → No-Go", "Decision evidenced"],
            ["Cutover planning"],
        ),
        (
            "Rollback Validation",
            "scenario-rollback-validation.md",
            "Validate rollback readiness and verification.",
            ["Rollback plan", "Irreversible ops list"],
            ["List triggers", "Walk restore/compensate", "Define post-rollback reconcile"],
            ["Triggers owned", "Residual risk documented"],
            ["Rollback planning"],
        ),
        (
            "Hypercare Validation",
            "scenario-hypercare-validation.md",
            "Validate Day-1–N migration hypercare checks.",
            ["Cutover complete", "Day-1 checklist"],
            ["Run Day-1 counts", "Triage DQ exceptions", "Smoke critical journeys"],
            ["Checks owned", "Sev1 ops → Sprint 9"],
            ["Hypercare activities", "Sprint 9 support"],
        ),
        (
            "Security Validation",
            "scenario-security-validation.md",
            "Validate post-migrate CRUD/FLS/PII themes.",
            ["Personas", "PII field list"],
            ["Run authorized persona", "Run unauthorized", "Check masked dry-run policy"],
            ["Unauthorized blocked", "No GDPR certification claim"],
            ["PTA", "Migration security"],
        ),
        (
            "Performance Validation",
            "scenario-performance-validation.md",
            "Document performance risk assessment without inventing timings.",
            ["Volume estimates", "Optional measured evidence"],
            ["Identify LDV risks", "Review batch/parallel assumptions", "Recommend measurement"],
            ["Assumptions labeled", "No invented SLA %"],
            ["Migration performance", "LDV knowledge"],
        ),
    ]
    for title, slug, purpose, preconditions, steps, asserts, chains in tests:
        write(f"tests/{slug}", test_doc(title, purpose, preconditions, steps, asserts, chains))

    write(
        "tests/README.md",
        fm("Data Migration QA — Tests", "QE Specialized Skill Test", "Guide", ["data-migration-qa"])
        + """# Data Migration QA — Tests

| Scenario | File |
|----------|------|
| Record Count Validation | [scenario-record-count-validation.md](scenario-record-count-validation.md) |
| Data Mapping Validation | [scenario-data-mapping-validation.md](scenario-data-mapping-validation.md) |
| Relationship Validation | [scenario-relationship-validation.md](scenario-relationship-validation.md) |
| Duplicate Detection | [scenario-duplicate-detection.md](scenario-duplicate-detection.md) |
| Transformation Validation | [scenario-transformation-validation.md](scenario-transformation-validation.md) |
| Data Quality Validation | [scenario-data-quality-validation.md](scenario-data-quality-validation.md) |
| Bulk Load Validation | [scenario-bulk-load-validation.md](scenario-bulk-load-validation.md) |
| Cutover Validation | [scenario-cutover-validation.md](scenario-cutover-validation.md) |
| Rollback Validation | [scenario-rollback-validation.md](scenario-rollback-validation.md) |
| Hypercare Validation | [scenario-hypercare-validation.md](scenario-hypercare-validation.md) |
| Security Validation | [scenario-security-validation.md](scenario-security-validation.md) |
| Performance Validation | [scenario-performance-validation.md](scenario-performance-validation.md) |

## Related Documents

- [SKILL.md](../SKILL.md)
""",
    )

    print("Done.")


if __name__ == "__main__":
    main()
