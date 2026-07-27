"""Generate Salesforce Test Data Generator (TDG) skill pack."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP = ROOT / "skills" / "test-data-generator"
VERSION = "0.20.0"
DATE = "2026-07-27"

OUTPUT_SECTIONS = [
    "Executive Summary",
    "Business Scenario",
    "Data Requirements",
    "Objects Involved",
    "Relationship Diagram (logical)",
    "Generated Test Data Structure",
    "Validation Rule Considerations",
    "Security Considerations",
    "Data Volume Strategy",
    "Automation Opportunities",
    "Recommended SOQL Validation",
    "Cleanup Strategy",
    "Risks",
    "QA Recommendations",
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
    return fm(title, "QE Specialized Skill Knowledge", "Knowledge Article", ["test-data-generator", "knowledge"]) + f"""# {title}

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
    return fm(title, "QE Specialized Skill Playbook", "Playbook", ["test-data-generator", "playbook"]) + f"""# {title}

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
    return fm(title, "QE Specialized Skill Template", "Template", ["test-data-generator", "template"]) + f"""# {title}

{body}

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {VERSION} | {DATE} | QE Practice Lead | Initial template |
"""


def prompt_doc(title, prompt, sections):
    return fm(title, "QE Specialized Skill Prompt", "Prompt", ["test-data-generator", "prompt"]) + f"""# {title}

## Prompt

```
{prompt}
```

## Required Output Sections

{chr(10).join(f"{i}. {s}" for i, s in enumerate(sections, 1))}

## Quality Gate

- Business Scenario, Data Requirements, and Objects/Relationships BEFORE payloads.
- Synthetic data only; never real PII.
- Include Cleanup Strategy and SOQL stubs; label volume assumptions.
"""


def example_doc(title, scenario, objects, relationships, sample, validation, expected, soql, qa):
    return fm(title, "QE Specialized Skill Example", "Example", ["test-data-generator", "example"]) + f"""# {title}

## Business Scenario

{scenario}

## Required Objects

{objects}

## Relationships

{relationships}

## Sample Data (Synthetic)

{sample}

## Validation Rules

{validation}

## Expected Results

{expected}

## Recommended SOQL

```sql
{soql}
```

## QA Recommendations

{qa}
"""


def main() -> None:
    print("Generating Test Data Generator skill pack...")
    CAP.mkdir(parents=True, exist_ok=True)

    write(
        "skill-config.yaml",
        f"""name: test-data-generator
short_id: TDG
version: {VERSION}
parent_module: salesforce-quality-engineering
entry: SKILL.md

routing:
  keywords:
    - Test Data
    - Sample Data
    - Test Records
    - Seed Data
    - Salesforce Data
    - Data Factory
    - Test Setup
    - QA Environment
    - UAT Data
    - SIT Data
    - Regression Data
    - Data Creation
    - Mock Data
    - Bulk Test Data
    - Data Masking
    - Synthetic Data
    - Sandbox Refresh
    - External ID
    - Data Loader
    - Bulk API
    - Apex Test Factory
    - Apex Test Data Factory
    - Test Data Factory
    - CSV Test Data
    - Seed Pack
  primary_support:
    - knowledge/data/
    - templates/test-data-strategy.md
    - automation-intelligence/test-data/
  upstream_skills:
    - skills/metadata-impact-analyzer
  downstream_capabilities:
    - skills/soql-validation-assistant
    - skills/permission-testing-agent
    - skills/agentforce-testing
    - skills/field-service-testing
  downstream_after_analysis:
    - knowledge/test-design-engine.md

output_schema:
  sections:
{chr(10).join(f'    - id: {s.lower().replace(" ", "_").replace("(", "").replace(")", "")}' + chr(10) + f'      title: "{s}"' for s in OUTPUT_SECTIONS)}

quality_gates:
  - business_and_objects_before_payloads
  - synthetic_by_default_no_real_pii
  - referential_integrity_documented
  - validation_rules_respected_unless_negative
  - soql_stubs_for_sova_expansion
  - cleanup_required_for_bulk_ldv
  - volume_assumptions_labeled

escalation:
  - signal: real_pii_or_production_data_requested
    to: Security / Data Governance
  - signal: ldv_without_capacity_evidence
    to: Performance / Solution Architect
  - signal: bulk_without_cleanup_owner
    to: Release Manager
""",
    )

    data = "../../knowledge/data"
    mia = "../../skills/metadata-impact-analyzer/SKILL.md"
    sova = "../soql-validation-assistant/SKILL.md"
    pta = "../permission-testing-agent/SKILL.md"
    aft = "../agentforce-testing/SKILL.md"
    fsqa = "../field-service-testing/SKILL.md"
    auto_td = "../../automation-intelligence/test-data/README.md"
    sprint5 = "../../templates/test-data-strategy.md"

    knowledge_specs = [
        ("Salesforce Data Model for Test Data", "salesforce-data-model.md",
         "Frame objects/fields as a generation surface before inventing rows.",
         ["Inventory standard vs custom objects in scope.", "Map required vs optional fields and record types.", "Identify formula/rollup fields that must not be written.", "Cross-link Sprint 4A data-model encyclopedia — do not duplicate."],
         [("Data Model", f"{data}/data-model.md"), ("Data Knowledge Index", f"{data}/README.md")],
         ["Never invent undocumented custom objects as fact.", "Confirm edition/licenses before asserting objects exist."]),
        ("Test Data Management Reasoning", "test-data-management.md",
         "Apply TDM discipline: synthetic vs masked, personas, refresh, ownership.",
         ["Classify environment purpose (SIT/UAT/regression/perf).", "Choose synthetic vs masked with justification.", "Define persona packs and ownership model.", "Plan refresh and cleanup cadence."],
         [("Test Data Management", f"{data}/test-data-management.md"), ("Sprint 5 Test Data Strategy", sprint5)],
         ["Real PII → refuse; redirect to synthetic/masking.", "Prefer TDG over encyclopedia when generation intent is clear."]),
        ("Data Factories", "data-factories.md",
         "Design reusable factories (Apex/CLI/Loader) for deterministic seed packs.",
         ["Choose factory approach by volume and reuse need.", "Parameterize personas and record types.", "Keep factories deterministic and cleanup-aware.", "Prefer Apex factories for unit tests; Loader/CLI for env seed."],
         [("Apex Test Data Factory", "apex-test-data-factory.md"), ("Automation Test Data", auto_td)],
         ["Factories must not hardcode production IDs."]),
        ("Synthetic Data", "synthetic-data.md",
         "Generate realistic but non-identifying values by default.",
         ["Use realistic formats (email, phone, address) that are clearly synthetic.", "Avoid names/emails of real customers.", "Document synthetic markers (e.g. @example.test).", "Industry flavor without inventing regulatory claims."],
         [("PII Considerations", f"{data}/pii-considerations.md"), ("GDPR Awareness", f"{data}/gdpr-awareness.md")],
         ["Default = synthetic. Production copy only via approved masking program."]),
        ("Data Masking", "data-masking.md",
         "Guide masking when partial sandbox clones are unavoidable.",
         ["Identify PII/sensitive fields.", "Recommend masking vs regenerate synthetic.", "Preserve referential integrity after mask.", "Document residual risk."],
         [("Data Masking", f"{data}/data-masking.md")],
         ["Masking without integrity plan → Fail."]),
        ("External IDs", "external-ids.md",
         "Use External IDs for upsert, migration rehearsal, and stable seed keys.",
         ["Select External ID fields per object.", "Design upsert order parents → children.", "Document collision rules.", "Recommend SOQL to verify upsert results."],
         [("Data Import", f"{data}/data-import.md"), ("SOQL Validation Assistant", sova)],
         ["Missing External ID on bulk upsert → High risk."]),
        ("Object Relationships", "object-relationships.md",
         "Generate relationship-aware hierarchies with referential integrity.",
         ["Classify lookup vs master-detail vs junction.", "Order inserts correctly.", "Handle many-to-many via junction rows.", "Draw logical relationship diagram before payloads."],
         [("Referential Integrity", f"{data}/referential-integrity.md"), ("Data Integrity", f"{data}/data-integrity.md")],
         ["Orphan children → Fail integrity gate."]),
        ("Record Types", "record-types.md",
         "Align payloads to record types and business processes.",
         ["Map persona journeys to record types.", "Respect picklist value sets per record type.", "Include negative: wrong record type.", "Chain MIA when record type metadata changes."],
         [("Metadata Impact Analyzer", mia)],
         ["Wrong record type causing VR failures → document as data defect or config gap."]),
        ("Validation Rules", "validation-rules.md",
         "Respect VRs for positive data; intentionally violate only for negative packs.",
         ["List known VRs in scope or mark TBC.", "Design compliant happy-path rows.", "Design explicit negative rows with expected error.", "Chain MIA when VR deploy changes payloads."],
         [("Data Validation", f"{data}/data-validation.md"), ("Metadata Impact Analyzer", mia)],
         ["Positive pack that fails known VR → Fail."]),
        ("Data Volume Strategies", "data-volume-strategies.md",
         "Select generation path by volume without inventing capacity numbers.",
         ["Classify single/bulk/LDV/concurrent.", "Recommend Loader vs Bulk API vs Apex.", "State assumptions for row counts.", "Require cleanup for bulk/LDV."],
         [("Large Data Volumes", f"{data}/large-data-volumes.md"), ("Performance Knowledge", "../../knowledge/performance/README.md")],
         ["Do not invent org governor timing SLAs."]),
        ("Bulk API", "bulk-api.md",
         "Advise Bulk API–compatible structures for high-volume seed.",
         ["Prefer Bulk for large inserts/updates.", "Batch sizing guidance as qualitative.", "Error file / retry strategy.", "SOQL validation after load."],
         [("Data Loader", f"{data}/data-loader.md"), ("Data Volume Strategies", "data-volume-strategies.md")],
         ["Bulk without External ID strategy → High risk."]),
        ("Salesforce CLI Data Operations", "salesforce-cli-data-operations.md",
         "Advise `sf data` / tree import patterns as templates only.",
         ["Prefer tree import for small related graphs.", "Document file layout for CLI.", "No live execution claims.", "Cleanup via delete queries labeled for SOVA."],
         [("Data Import", f"{data}/data-import.md")],
         ["CLI templates are advisory — do not claim org success without run evidence."]),
        ("Data Loader", "data-loader.md",
         "Advise Data Loader CSV mapping and insert order.",
         ["Parent CSV before child CSV.", "Mapping checklist for required fields.", "Success/error file review steps.", "Cleanup checklist."],
         [("Data Loader Encyclopedia", f"{data}/data-loader.md")],
         ["Child load before parent → Fail."]),
        ("Apex Test Data Factory", "apex-test-data-factory.md",
         "Design Apex @TestSetup / factory method stubs for unit/integration tests.",
         ["Isolate factories from production data.", "SeeAllData=false by default.", "Cover required relationships.", "Document limitations vs env seed packs."],
         [("Data Factories", "data-factories.md")],
         ["SeeAllData=true without justification → anti-pattern."]),
        ("Sandbox and Environment Strategy", "sandbox-environment-strategy.md",
         "Align seed packs to sandbox type, refresh, and environment purpose.",
         ["Map SIT/UAT/Dev purposes.", "Plan post-refresh reseed.", "Synthetic vs masked decision per env.", "Ownership of seed packs."],
         [("Test Data Management", f"{data}/test-data-management.md"), ("Release Knowledge", "../../knowledge/release/README.md")],
         ["Full copy with unmasked PII → escalate Security."]),
        ("Industry Data Models", "industry-data-models.md",
         "Shape synthetic data with industry context without inventing compliance.",
         ["Select industry scenario pack.", "Map industry objects only when licensed/confirmed.", "Cross-link industry knowledge.", "Flag regulatory themes as TBC."],
         [("Industry Knowledge", "../../knowledge/industry/README.md"), ("Field Service QA", fsqa)],
         ["Do not invent HIPAA/PCI certifications."]),
    ]
    for spec in knowledge_specs:
        write(f"knowledge/{spec[1]}", knowledge_article(*spec))

    write(
        "knowledge/README.md",
        fm("Test Data Generator — Knowledge", "QE Specialized Skill Knowledge", "Guide", ["test-data-generator"])
        + """# Test Data Generator — Knowledge

Canonical encyclopedia: [`../../knowledge/data/`](../../knowledge/data/README.md). These articles provide **TDM generation reasoning models**.

| Document | Focus |
|----------|-------|
| [Salesforce Data Model](salesforce-data-model.md) | Objects/fields for generation |
| [Test Data Management](test-data-management.md) | TDM discipline |
| [Data Factories](data-factories.md) | Reusable factories |
| [Synthetic Data](synthetic-data.md) | Synthetic default |
| [Data Masking](data-masking.md) | Masking guidance |
| [External IDs](external-ids.md) | Upsert keys |
| [Object Relationships](object-relationships.md) | Integrity |
| [Record Types](record-types.md) | Record types |
| [Validation Rules](validation-rules.md) | VR compliance |
| [Data Volume Strategies](data-volume-strategies.md) | Volume |
| [Bulk API](bulk-api.md) | Bulk loads |
| [Salesforce CLI Data Operations](salesforce-cli-data-operations.md) | CLI templates |
| [Data Loader](data-loader.md) | Loader CSVs |
| [Apex Test Data Factory](apex-test-data-factory.md) | Apex factories |
| [Sandbox and Environment Strategy](sandbox-environment-strategy.md) | Env strategy |
| [Industry Data Models](industry-data-models.md) | Industry shaping |
""",
    )

    playbooks = [
        ("Test Data Planning Playbook", "test-data-planning.md",
         "Plan TDM approach before generating payloads.",
         ["Business scenario", "Test phase", "Objects", "Personas", "Volume"],
         ["Confirm synthetic vs masked.", "Inventory objects and relationships.", "Define positive/negative scope.", "Select formats and cleanup owner."],
         ["Full copy sandbox with PII?"],
         ["Test Data Design Document", "14-section report outline"],
         ["Plan approved", "No real PII"],
         ["PII request → Security"],
         f"[{sprint5}]({sprint5})"),
        ("Functional Test Data Playbook", "functional-test-data.md",
         "Generate happy-path and key negative data for functional tests.",
         ["AC / scenarios", "Record types", "Known VRs"],
         ["Map scenarios to objects.", "Build compliant positive rows.", "Add targeted negatives.", "Provide SOQL stubs."],
         ["Automation side effects unknown?"],
         ["Data Generation Report", "Sample CSV/JSON"],
         ["Referential integrity held", "Positive rows VR-compliant"],
         ["Org VR unknown → Admin/BA"],
         ""),
        ("Regression Data Playbook", "regression-data.md",
         "Define reusable baseline seed for regression packs.",
         ["Prior seed pack", "Change deltas", "Critical journeys"],
         ["Identify baseline vs delta data.", "Version External IDs.", "Document refresh steps.", "Link regression checklist."],
         ["Can baseline stay stable across sprints?"],
         ["Regression Data Checklist"],
         ["Baseline reproducible", "Cleanup documented"],
         ["Unowned baseline → Release Manager"],
         ""),
        ("UAT Data Playbook", "uat-data.md",
         "Prepare business-readable UAT seed with persona coverage.",
         ["UAT scripts", "Business personas", "Environment"],
         ["Align data to UAT scripts.", "Synthetic names clear to business.", "Ownership for each persona.", "Sign-off cleanup after UAT."],
         ["Business requires 'realistic' names — still synthetic?"],
         ["UAT seed pack", "Cleanup Strategy"],
         ["Scripts executable", "No production PII"],
         ["PII pressure → Data Governance"],
         ""),
        ("Performance Test Data Playbook", "performance-test-data.md",
         "Design volume strategy for performance/load datasets.",
         ["Target volume (assumption)", "Objects", "Concurrency goals"],
         ["Classify LDV needs.", "Recommend Bulk API path.", "Label assumptions — no invented timings.", "Plan staged load and cleanup."],
         ["Capacity evidence available?"],
         ["Performance Data Plan"],
         ["Volume strategy stated", "Cleanup owner named"],
         ["LDV without evidence → Performance Architect"],
         f"[{data}/large-data-volumes.md]"),
        ("Data Masking Playbook", "data-masking.md",
         "Plan masking when synthetic-only is not feasible.",
         ["Sensitive field list", "Clone type", "Integrity requirements"],
         ["Classify PII fields.", "Choose mask vs regenerate.", "Verify relationships post-mask.", "Document residual risk."],
         ["Any field must remain real for integration?"],
         ["Data Masking Checklist"],
         ["PII fields addressed", "Integrity verified"],
         ["Unmasked PII in shared sandbox → Security"],
         f"[{data}/data-masking.md]"),
        ("Bulk Data Generation Playbook", "bulk-data-generation.md",
         "Produce bulk-ready structures with External IDs and load order.",
         ["Volume", "Objects", "External IDs", "Format"],
         ["Design External ID scheme.", "Order CSVs parents→children.", "Batch/error strategy.", "Post-load SOQL + cleanup."],
         ["Upsert vs insert?"],
         ["Bulk CSV/JSON pack", "Cleanup Strategy"],
         ["Load order correct", "SOQL stubs present"],
         ["Bulk without cleanup → Fail gate"],
         ""),
        ("Cleanup Strategy Playbook", "cleanup-strategy.md",
         "Define safe deletion/archive of generated seed data.",
         ["External ID prefix", "Objects", "Environment"],
         ["Identify deletable seed via External ID / naming.", "Order deletes children→parents.", "Verify with SOQL counts.", "Document exceptions (shared reference data)."],
         ["Shared Pricebook entries must remain?"],
         ["Data Cleanup Checklist"],
         ["Seed removable", "Shared refs protected"],
         ["Ambiguous delete scope → Release Manager"],
         f"[{sova}]({sova})"),
    ]
    for title, slug, *rest in playbooks:
        write(f"playbooks/{slug}", playbook(title, slug, *rest))

    write(
        "playbooks/README.md",
        fm("Test Data Generator — Playbooks", "QE Specialized Skill Playbook", "Guide", ["test-data-generator"])
        + """# Test Data Generator — Playbooks

| Playbook | Focus |
|----------|-------|
| [Test Data Planning](test-data-planning.md) | Planning |
| [Functional Test Data](functional-test-data.md) | Functional |
| [Regression Data](regression-data.md) | Regression baseline |
| [UAT Data](uat-data.md) | UAT seed |
| [Performance Test Data](performance-test-data.md) | Volume/perf |
| [Data Masking](data-masking.md) | Masking |
| [Bulk Data Generation](bulk-data-generation.md) | Bulk |
| [Cleanup Strategy](cleanup-strategy.md) | Cleanup |
""",
    )

    templates = [
        ("Test Data Request Form", ["Requester", "Business Scenario", "Test Phase", "Objects", "Volume", "Personas", "Constraints", "Due Date"]),
        ("Test Data Design Document", ["Purpose", "Scope", "Objects", "Relationships", "Positive Packs", "Negative Packs", "Formats", "Cleanup", "Owners"]),
        ("Object Relationship Matrix", ["Parent Object", "Child Object", "Relationship Type", "Required", "External ID", "Load Order", "Notes"]),
        ("Data Generation Report", OUTPUT_SECTIONS),
        ("Data Cleanup Checklist", ["Environment", "External ID Prefix", "Delete Order", "SOQL Verification", "Shared Refs Protected", "Sign-off"]),
        ("Data Masking Checklist", ["PII Fields", "Mask Method", "Integrity Check", "Residual Risk", "Approver", "Status"]),
        ("Performance Data Plan", ["Objectives", "Volume Assumptions", "Objects", "Load Path", "Concurrency Notes", "Cleanup", "Risks"]),
        ("Regression Data Checklist", ["Baseline Version", "Delta Changes", "Critical Journeys", "Reseed Steps", "SOQL Smoke", "Sign-off"]),
    ]
    for title, sections in templates:
        slug = title.lower().replace(" ", "-") + ".md"
        write(f"templates/{slug}", template_doc(title, sections))

    write(
        "templates/README.md",
        fm("Test Data Generator — Templates", "QE Specialized Skill Template", "Guide", ["test-data-generator"])
        + """# Test Data Generator — Templates

| Template | Use |
|----------|-----|
| [Test Data Request Form](test-data-request-form.md) | Intake |
| [Test Data Design Document](test-data-design-document.md) | Design |
| [Object Relationship Matrix](object-relationship-matrix.md) | Relationships |
| [Data Generation Report](data-generation-report.md) | Primary 14-section deliverable |
| [Data Cleanup Checklist](data-cleanup-checklist.md) | Cleanup |
| [Data Masking Checklist](data-masking-checklist.md) | Masking |
| [Performance Data Plan](performance-data-plan.md) | Perf volume |
| [Regression Data Checklist](regression-data-checklist.md) | Regression baseline |
""",
    )

    base = (
        "Act as Salesforce Test Data Generator (TDG). Provide Business Scenario, Data Requirements, "
        "and Objects/Relationships BEFORE record payloads. Produce all 14 sections per SKILL.md. "
        "Synthetic data only; never real PII. Include Cleanup Strategy and SOQL stubs. "
        "Label volume assumptions. Context:\n[paste]"
    )
    prompts = [
        ("Generate Functional Test Data", "generate-functional-test-data.md", base + "\nFocus: functional positive + key negatives.", OUTPUT_SECTIONS),
        ("Generate UAT Data", "generate-uat-data.md", base + "\nFocus: UAT persona seed, business-readable synthetic names.", OUTPUT_SECTIONS),
        ("Generate Bulk Test Data", "generate-bulk-test-data.md", base + "\nFocus: External IDs, load order, Bulk/Data Loader structures, cleanup.", OUTPUT_SECTIONS),
        ("Generate Negative Test Data", "generate-negative-test-data.md", base + "\nFocus: VR violations, missing required, invalid relationships — expected errors.", OUTPUT_SECTIONS),
        ("Generate Industry Test Data", "generate-industry-test-data.md", base + "\nFocus: industry-shaped synthetic objects; no invented compliance.", OUTPUT_SECTIONS),
        ("Generate Salesforce CLI Data", "generate-salesforce-cli-data.md", base + "\nFocus: sf data / tree import file templates (advisory).", OUTPUT_SECTIONS),
        ("Generate Apex Test Data Factory", "generate-apex-test-data-factory.md", base + "\nFocus: Apex factory / @TestSetup stubs; SeeAllData=false.", OUTPUT_SECTIONS),
        ("Generate CSV Test Data", "generate-csv-test-data.md", base + "\nFocus: CSV columns, sample rows, load order.", OUTPUT_SECTIONS),
        ("Generate Data Loader Files", "generate-data-loader-files.md", base + "\nFocus: Data Loader mapping notes + CSV packs.", OUTPUT_SECTIONS),
        ("Review Existing Test Data", "review-existing-test-data.md", base + "\nFocus: review gaps — integrity, PII, VR, cleanup, SOQL.", OUTPUT_SECTIONS),
    ]
    for title, slug, prompt, sections in prompts:
        write(f"prompts/{slug}", prompt_doc(title, prompt, sections))

    write(
        "prompts/README.md",
        fm("Test Data Generator — Prompts", "QE Specialized Skill Prompt", "Guide", ["test-data-generator"])
        + """# Test Data Generator — Prompts

| Prompt | File |
|--------|------|
| Generate Functional Test Data | [generate-functional-test-data.md](generate-functional-test-data.md) |
| Generate UAT Data | [generate-uat-data.md](generate-uat-data.md) |
| Generate Bulk Test Data | [generate-bulk-test-data.md](generate-bulk-test-data.md) |
| Generate Negative Test Data | [generate-negative-test-data.md](generate-negative-test-data.md) |
| Generate Industry Test Data | [generate-industry-test-data.md](generate-industry-test-data.md) |
| Generate Salesforce CLI Data | [generate-salesforce-cli-data.md](generate-salesforce-cli-data.md) |
| Generate Apex Test Data Factory | [generate-apex-test-data-factory.md](generate-apex-test-data-factory.md) |
| Generate CSV Test Data | [generate-csv-test-data.md](generate-csv-test-data.md) |
| Generate Data Loader Files | [generate-data-loader-files.md](generate-data-loader-files.md) |
| Review Existing Test Data | [review-existing-test-data.md](review-existing-test-data.md) |
""",
    )

    examples = [
        ("Account and Contact Data", "account-and-contact-data.md",
         "Seed B2B accounts with related contacts for SIT smoke.",
         "Account, Contact",
         "Account 1—M Contact (lookup)",
         "Account: Acme Test Co (External_Id__c=TDG-ACC-001); Contact: Jane Tester jane.tester@example.test",
         "Contact must have AccountId; Email format valid.",
         "Contacts linked; no orphans.",
         "SELECT Id, AccountId FROM Contact WHERE Email LIKE '%@example.test'",
         "Chain SOVA for counts; PTA if private OWD."),
        ("Opportunity Sales Pipeline", "opportunity-sales-pipeline.md",
         "UAT pipeline with Open and Closed Won opportunities.",
         "Account, Contact, Opportunity, OpportunityContactRole",
         "Account→Opportunity; Contact via OCR",
         "Opp TDG-OPP-001 Stage=Prospecting; TDG-OPP-002 Stage=Closed Won Amount=10000",
         "Amount required when Closed Won (assume org VR).",
         "Stages valid; Closed Won has Amount.",
         "SELECT Id, StageName, Amount FROM Opportunity WHERE External_Id__c LIKE 'TDG-OPP-%'",
         "Negative pack: Closed Won with null Amount."),
        ("Service Cloud Case Lifecycle", "service-cloud-case-lifecycle.md",
         "Case create→work→close with Account/Contact.",
         "Account, Contact, Case",
         "Account→Case; Contact→Case",
         "Case TDG-CASE-001 Status=New Origin=Phone; TDG-CASE-002 Status=Closed",
         "Closed requires Reason (assumption — label if TBC).",
         "Statuses transition; Contact linked.",
         "SELECT Id, Status, ContactId FROM Case WHERE Subject LIKE 'TDG%'",
         "Include entitlement only if licensed."),
        ("Utility Customer and Meter Data", "utility-customer-and-meter-data.md",
         "Utilities synthetic customer with service point/meter placeholders.",
         "Account, Contact, Asset (Meter), Case (optional)",
         "Account→Asset; Account→Case",
         "Account TDG-UTIL-001; Asset SerialNumber=MTR-TEST-1001",
         "Do not invent Industries Cloud objects unless confirmed.",
         "Customer+meter linked synthetically.",
         "SELECT Id, AccountId FROM Asset WHERE SerialNumber LIKE 'MTR-TEST-%'",
         "Chain FSQA if Work Orders added later."),
        ("Retail Order Management", "retail-order-management.md",
         "Retail order with products for omnichannel SIT.",
         "Account, Product2, Pricebook2, PricebookEntry, Order, OrderItem",
         "Order→Account; OrderItem→Order/Product via PBE",
         "Order TDG-ORD-001; OrderItem qty=2 Product=SKU-TEST-01",
         "Standard Pricebook activation assumed in sandbox.",
         "Order totals consistent with items.",
         "SELECT Id, OrderId, Quantity FROM OrderItem WHERE Order.External_Id__c = 'TDG-ORD-001'",
         "Load PricebookEntry before OrderItem."),
        ("Product and Price Book Setup", "product-and-price-book-setup.md",
         "Baseline catalog for sales and service tests.",
         "Product2, Pricebook2, PricebookEntry",
         "PBE links Product to Pricebook",
         "Product SKU-TEST-01 Active; Custom Pricebook TDG-PB-01; PBE UnitPrice=99",
         "Active product required for PBE.",
         "Catalog usable by Opportunity/Order examples.",
         "SELECT Id, UnitPrice FROM PricebookEntry WHERE Pricebook2.Name = 'TDG-PB-01'",
         "Treat as shared reference — protect in cleanup."),
        ("Quote to Cash", "quote-to-cash.md",
         "Quote from Opportunity through Order handoff (synthetic).",
         "Account, Opportunity, Quote, QuoteLineItem, Order",
         "Opp→Quote→QLI; Order from Opp/Account",
         "Quote TDG-QT-001 Status=Draft; QLI for SKU-TEST-01",
         "Synced quote fields org-specific — label assumptions.",
         "Quote lines reference valid PBE.",
         "SELECT Id, QuoteId FROM QuoteLineItem WHERE Quote.External_Id__c = 'TDG-QT-001'",
         "CPQ objects only if licensed — otherwise standard Quote."),
        ("Lead Conversion", "lead-conversion.md",
         "Lead ready for conversion testing plus converted outcome set.",
         "Lead, Account, Contact, Opportunity",
         "Conversion creates Account/Contact/Opp",
         "Lead TDG-LEAD-001 Company=Test Co Email=lead@example.test",
         "Required Company/Email; duplicate rules may block — plan unique emails.",
         "Convert succeeds; related records created.",
         "SELECT Id, IsConverted, ConvertedAccountId FROM Lead WHERE Email = 'lead@example.test'",
         "Negative: duplicate Lead email."),
        ("Asset Management", "asset-management.md",
         "Installed asset under Account for service journeys.",
         "Account, Contact, Asset, Product2",
         "Asset→Account, Asset→Product2, Asset→Contact optional",
         "Asset TDG-AST-001 Status=Installed SerialNumber=AST-TEST-55",
         "Serial uniqueness if org-enforced.",
         "Asset visible under Account.",
         "SELECT Id, AccountId, Status FROM Asset WHERE SerialNumber = 'AST-TEST-55'",
         "Chain Case example for break-fix."),
        ("Experience Cloud Users", "experience-cloud-users.md",
         "Community user seed linked to Contact/Account for portal tests.",
         "Account, Contact, User (community), Profile/Perm Set refs",
         "User→Contact→Account",
         "Contact portal.user@example.test; User Username unique in org",
         "License and profile must exist — do not invent.",
         "User active and linked to Contact.",
         "SELECT Id, ContactId, IsActive FROM User WHERE Username LIKE 'portal.user%@example.test'",
         "Chain PTA for guest vs member access; never real emails."),
        ("Agentforce Test Data", "agentforce-test-data.md",
         "CRM records for Agentforce conversation actions (read/update Case).",
         "Account, Contact, Case, Knowledge (optional)",
         "Case→Account/Contact; Knowledge for grounding (if used)",
         "Case TDG-AF-001 Subject='Billing question TEST'; Knowledge title synthetic",
         "No real customer utterances with PII.",
         "Agent can resolve Case Id via SOQL stub.",
         "SELECT Id, Subject, Status FROM Case WHERE External_Id__c = 'TDG-AF-001'",
         "Chain AFT for conversation QA; TDG owns seed only."),
        ("OmniStudio Journey Data", "omnistudio-journey-data.md",
         "JSON-shaped input payloads for OmniScript/DataRaptor rehearsal (advisory).",
         "Account, Contact, Case (targets); OmniStudio components as config (not data rows)",
         "Payload maps to Account/Contact create then Case",
         "Sample JSON keys: AccountName, ContactEmail=@example.test, CaseSubject",
         "Confirm OmniStudio licensed; do not invent DataRaptor names as fact.",
         "Payload structure ready for SIT; objects creatable in order.",
         "SELECT Id FROM Account WHERE Name = 'TDG Omni Test Account'",
         "Cross-link future OmniStudio QA; until then use clouds/OmniStudio knowledge."),
    ]
    for title, slug, scenario, objects, relationships, sample, validation, expected, soql, qa in examples:
        write(f"examples/{slug}", example_doc(title, scenario, objects, relationships, sample, validation, expected, soql, qa))

    write(
        "examples/README.md",
        fm("Test Data Generator — Examples", "QE Specialized Skill Example", "Guide", ["test-data-generator"])
        + """# Test Data Generator — Examples

| Example | Domain |
|---------|--------|
| [Account and Contact Data](account-and-contact-data.md) | CRM |
| [Opportunity Sales Pipeline](opportunity-sales-pipeline.md) | Sales |
| [Service Cloud Case Lifecycle](service-cloud-case-lifecycle.md) | Service |
| [Utility Customer and Meter Data](utility-customer-and-meter-data.md) | Utilities |
| [Retail Order Management](retail-order-management.md) | Retail |
| [Product and Price Book Setup](product-and-price-book-setup.md) | Catalog |
| [Quote to Cash](quote-to-cash.md) | Q2C |
| [Lead Conversion](lead-conversion.md) | Lead |
| [Asset Management](asset-management.md) | Assets |
| [Experience Cloud Users](experience-cloud-users.md) | Experience |
| [Agentforce Test Data](agentforce-test-data.md) | Agentforce |
| [OmniStudio Journey Data](omnistudio-journey-data.md) | OmniStudio |
""",
    )

    tests = [
        ("parent-child-integrity", "Parents before children; no orphans"),
        ("validation-rule-compliance", "Positive rows satisfy known VRs; negatives explicit"),
        ("relationship-validation", "Lookup/MD/junction documented and load-ordered"),
        ("duplicate-detection", "Unique synthetic keys; duplicate negatives intentional"),
        ("record-ownership", "OwnerId/persona assignment for ownership tests"),
        ("sharing-validation", "Sharing persona packs ready for PTA chain"),
        ("bulk-data-validation", "External IDs, batch order, post-load SOQL"),
        ("performance-data-validation", "Volume strategy labeled; no invented timings"),
        ("data-cleanup", "Cleanup Strategy with child→parent delete order"),
        ("security-validation", "No real PII; sensitive fields synthetic/masked"),
        ("industry-specific-data-validation", "Industry objects only when confirmed; compliance TBC"),
    ]
    for slug, desc in tests:
        write(
            f"tests/scenario-{slug}.md",
            fm(f"Test — {slug}", "QE Specialized Skill Test", "Test Scenario", ["test-data-generator"])
            + f"""# Test Scenario — {slug}

## Objective

{desc}

## Pass Criteria

- Business Scenario, Data Requirements, and Objects before payloads
- Synthetic-only; assumptions labeled
- SOQL stubs present when backend proof needed
- Cleanup present for bulk/LDV scenarios

## Fail Criteria

- Real PII or production data in sample packs
- Orphan children / ignored known VRs on positive data
- Invented volume/SLA metrics without labeled assumptions
- Missing cleanup for bulk generation
""",
        )

    write(
        "tests/README.md",
        fm("Test Data Generator — Tests", "QE Specialized Skill Test", "Guide", ["test-data-generator"])
        + """# Test Data Generator — Tests

| Scenario | Focus |
|----------|-------|
| [parent-child-integrity](scenario-parent-child-integrity.md) | Integrity |
| [validation-rule-compliance](scenario-validation-rule-compliance.md) | VRs |
| [relationship-validation](scenario-relationship-validation.md) | Relationships |
| [duplicate-detection](scenario-duplicate-detection.md) | Duplicates |
| [record-ownership](scenario-record-ownership.md) | Ownership |
| [sharing-validation](scenario-sharing-validation.md) | Sharing |
| [bulk-data-validation](scenario-bulk-data-validation.md) | Bulk |
| [performance-data-validation](scenario-performance-data-validation.md) | Perf volume |
| [data-cleanup](scenario-data-cleanup.md) | Cleanup |
| [security-validation](scenario-security-validation.md) | Security/PII |
| [industry-specific-data-validation](scenario-industry-specific-data-validation.md) | Industry |
""",
    )

    print("Done.")


if __name__ == "__main__":
    main()
