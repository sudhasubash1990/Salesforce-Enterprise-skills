"""Generate SOQL Validation Assistant skill pack."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP = ROOT / "skills" / "soql-validation-assistant"
VERSION = "0.16.0"
DATE = "2026-07-27"

OUTPUT_SECTIONS = [
    "Validation Objective",
    "Business Context",
    "Recommended SOQL",
    "Query Explanation",
    "Expected Result",
    "Backend Validation Steps",
    "Security Considerations",
    "Performance Considerations",
    "Automation Opportunities",
    "Related Metadata",
    "Negative Validation",
    "Edge Cases",
    "Alternative Queries",
    "QA Recommendations",
]


def fm(title: str, category: str, doc_type: str, tags: list[str]) -> str:
    tag_str = ", ".join(tags)
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
tags: [{tag_str}]
---

"""


def write(rel: str, content: str) -> None:
    path = CAP / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {rel}")


def knowledge_article(title, slug, purpose, reasoning, cross_links, rules):
    links = "\n".join(f"- [{n}]({p})" for n, p in cross_links)
    return fm(title, "QE Specialized Skill Knowledge", "Knowledge Article", ["soql-validation", "knowledge"]) + f"""# {title}

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
    return fm(title, "QE Specialized Skill Playbook", "Playbook", ["soql-validation", "playbook"]) + f"""# {title}

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

## Related Documents

- [SKILL.md](../SKILL.md)
"""


def template_doc(title, sections):
    body = "\n\n".join(f"## {s}\n\n_Complete during validation._" for s in sections)
    return fm(title, "QE Specialized Skill Template", "Template", ["soql-validation", "template"]) + f"""# {title}

**Usage:** Copy to `outputs/<project>/` and complete. Run `python output-engine/convert.py --file <path>` after authoring.

{body}

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {VERSION} | {DATE} | QE Practice Lead | Initial template |
"""


def prompt_doc(title, prompt, sections):
    return fm(title, "QE Specialized Skill Prompt", "Prompt", ["soql-validation", "prompt"]) + f"""# {title}

## Prompt

```
{prompt}
```

## Required Output Sections

{chr(10).join(f"{i}. {s}" for i, s in enumerate(sections, 1))}

## Quality Gate

- Validation Objective and Business Context MUST precede Recommended SOQL.
- Include Security and Performance Considerations for every query.
- Label assumptions; do not invent row counts without stating they are illustrative.
"""


def example_doc(title, scenario, objective, soql, expected, negative, qa):
    return fm(title, "QE Specialized Skill Example", "Example", ["soql-validation", "example"]) + f"""# {title}

## Business Scenario

{scenario}

## Validation Objective

{objective}

## Generated SOQL

```sql
{soql}
```

## Expected Result

{expected}

## Negative Validation

{negative}

## QA Recommendation

{qa}

## Related Documents

- [examples/README.md](README.md)
- [SKILL.md](../SKILL.md)
"""


def main() -> None:
    print("Generating SOQL Validation Assistant skill pack...")
    CAP.mkdir(parents=True, exist_ok=True)

    write(
        "skill-config.yaml",
        f"""# SOQL Validation Assistant — capability configuration
name: soql-validation-assistant
short_id: SOVA
version: {VERSION}
parent_module: salesforce-quality-engineering
entry: SKILL.md

routing:
  keywords:
    - SOQL
    - soql
    - data validation
    - backend validation
    - data verification
    - record verification
    - relationship query
    - parent child
    - child parent
    - aggregate query
    - COUNT
    - GROUP BY
    - duplicate detection
    - data reconciliation
    - bulk validation
    - migration validation
    - integration validation
    - flow validation
    - validation rule verification
    - report validation
    - dashboard validation
    - regression validation
    - release validation
    - smoke testing
    - sanity testing
    - production verification
    - query optimization
    - query review
  primary_support:
    - knowledge/performance/
    - knowledge/data/
    - knowledge/security/
  upstream_skills:
    - skills/metadata-impact-analyzer
  downstream_after_queries:
    - knowledge/test-design-engine.md

output_schema:
  sections:
{chr(10).join(f"    - id: {s.lower().replace(' ', '_')}" + chr(10) + f'      title: "{s}"' for s in OUTPUT_SECTIONS)}

performance_risk:
  scale: [Low, Medium, High]
  rules:
    - Assess selectivity and relationship depth before recommending query
    - Flag non-selective filters and missing LIMIT on large objects
    - Cross-link knowledge/performance/query-selectivity.md for depth

security_warnings:
  - FLS may hide fields — state run-as user context
  - Sharing may exclude records — warn on misleading zero-row results
  - API-only users may differ from UI personas

quality_gates:
  - validation_objective_before_soql
  - all_fourteen_sections_present
  - security_and_performance_sections_required
  - assumptions_labeled
""",
    )

    knowledge_specs = [
        ("SOQL Fundamentals", "soql-fundamentals.md", "Establish validation intent and query type before writing SOQL.",
         ["Clarify business question the query must answer.", "Choose query type: list, relationship, aggregate, count.", "Identify object, fields, filters, and run-as persona.", "Only then draft SOQL."],
         [("Data Validation", "../../knowledge/data/data-validation.md"), ("Data Model", "../../knowledge/data/data-model.md")],
         ["Never output SOQL without Validation Objective.", "Prefer selective filters on indexed fields."]),
        ("Relationship Queries", "relationship-queries.md", "Reason about parent-child and child-parent SOQL for backend validation.",
         ["Map relationship name and cardinality.", "Choose parent-to-child (subquery) vs child-to-parent (dot notation).", "Limit relationship depth; flag performance on deep trees."],
         [("Referential Integrity", "../../knowledge/data/referential-integrity.md")],
         ["Master-detail subqueries respect sharing — note persona.", "Polymorphic lookups need TYPEOF or separate queries."]),
        ("Aggregate Functions", "aggregate-functions.md", "Use COUNT, SUM, GROUP BY, HAVING for reconciliation and duplicate detection.",
         ["Define aggregation purpose (reconcile, detect duplicates, smoke metric).", "Choose GROUP BY keys aligned to business rule.", "Add HAVING for post-aggregate filters."],
         [("Data Reconciliation", "../../knowledge/data/data-reconciliation.md")],
         ["COUNT() vs COUNT(Id) — document null handling.", "GROUP BY picklist — watch record-type specific values."]),
        ("Date Literals", "date-literals.md", "Apply date literals and functions for time-bound validation.",
         ["Confirm timezone and business date boundaries.", "Use LAST_N_DAYS, THIS_MONTH, etc. with explicit business meaning.", "Compare CreatedDate vs custom date fields per requirement."],
         [("Release Validation", "../../knowledge/release/post-deployment-validation.md")],
         ["Date-only vs datetime — document truncation risk."]),
        ("Governor Limits", "governor-limits.md", "Evaluate query impact on SOQL rows and limits.",
         ["Estimate row volume; apply LIMIT for exploratory queries.", "Flag queries in loops (Apex/integration context).", "Recommend batch for large reconciliations."],
         [("Governor Limits", "../../knowledge/performance/governor-limits.md")],
         ["More than 50k rows scanned → High performance risk."]),
        ("Query Selectivity", "query-selectivity.md", "Ensure filters use selective predicates.",
         ["Prefer Id, Name (if indexed), foreign keys, standard indexed fields.", "Avoid leading-wildcard LIKE on large objects.", "Document when filter may be non-selective."],
         [("Query Selectivity", "../../knowledge/performance/query-selectivity.md")],
         ["Custom field without index + high cardinality → warn and suggest alternative."]),
        ("Large Data Volumes", "large-data-volumes.md", "Adapt validation queries for LDV contexts.",
         ["Use narrow filters, LIMIT, and aggregate rollups.", "Recommend parallel batch validation for full reconciliation.", "Avoid full-table scans in production."],
         [("Large Data Volumes", "../../knowledge/performance/large-data-volumes.md"), ("LDV Data", "../../knowledge/data/large-data-volumes.md")],
         ["Production full reconcile → No-Go without batch plan."]),
        ("Indexing", "indexing.md", "Relate filter fields to index availability for QE advice.",
         ["Ask whether custom fields are indexed when filtering LDV.", "Note standard indexed fields (Id, Name, OwnerId, foreign keys).", "Recommend SA confirmation for custom index needs."],
         [("Indexing Concepts", "../../knowledge/performance/indexing-concepts.md")],
         ["Do not assume custom field is indexed."]),
        ("Query Optimization", "query-optimization.md", "Recommend improvements to proposed SOQL.",
         ["Reduce selected fields to validation minimum.", "Replace non-selective filters where possible.", "Suggest alternative queries in section 13."],
         [("SOQL Performance", "../../knowledge/performance/soql-performance.md")],
         ["Optimize only after validation objective is clear."]),
        ("Security Considerations", "security-considerations.md", "Warn when query results may mislead due to security.",
         ["State run-as user/profile/permission set.", "Note CRUD, FLS, sharing, and sharing-only records.", "Zero rows may mean hidden data — not always clean validation."],
         [("Security Knowledge", "../../knowledge/security/README.md"), ("Sharing Security Testing", "../../knowledge/sharing-security-testing.md")],
         ["Always include Security Considerations section."]),
        ("Formula Fields", "formula-fields.md", "Validate via SOQL limitations on formula and roll-up fields.",
         ["Formula fields queryable but not filterable in all cases — check filter rules.", "Roll-up summary only on master-detail parent.", "Cross-object formulas — document limitations."],
         [("Platform Knowledge", "../../knowledge/platform/README.md")],
         ["Cannot filter on some formula types — use alternative query path."]),
        ("Polymorphic Relationships", "polymorphic-relationships.md", "Handle WhoId, WhatId, and polymorphic lookups in validation SOQL.",
         ["Use TYPEOF when multiple object types in one field.", "Split queries per object type when simpler.", "Document which types are in scope."],
         [("Platform Knowledge", "../../knowledge/platform/README.md")],
         ["Task.WhoId / WhatId — specify Person Account vs Contact scenarios."]),
        ("Tooling API Queries", "tooling-api-queries.md", "Advise Tooling API SOQL for metadata dependency evidence.",
         ["Use for Flow, Apex, ValidationRule dependency discovery.", "Not for business data validation — separate from data SOQL.", "Human/tool executes in org; skill recommends query text."],
         [("MIA Tooling API", "../../skills/metadata-impact-analyzer/knowledge/tooling-api.md")],
         ["Label Tooling vs data SOQL explicitly."]),
        ("Metadata API Queries", "metadata-api-queries.md", "Advise metadata retrieval patterns for validation context.",
         ["Support deploy verification themes — not live API from skill.", "Cross-link deployment validation knowledge."],
         [("MIA Metadata API", "../../skills/metadata-impact-analyzer/knowledge/metadata-api.md"), ("Deployment Validation", "../../knowledge/release/deployment-validation.md")],
         ["No credentials or live API calls in skill pack."]),
        ("Query Best Practices", "query-best-practices.md", "Synthesize enterprise SOQL validation discipline.",
         ["Objective → context → query → explain → expected → security → performance.", "Provide negative validation and alternatives.", "Link automation opportunities without writing scripts."],
         [("Data Validation", "../../knowledge/data/data-validation.md"), ("SOQL Performance", "../../knowledge/performance/soql-performance.md")],
         ["Every deliverable uses 14-section schema."]),
    ]
    for spec in knowledge_specs:
        write(f"knowledge/{spec[1]}", knowledge_article(*spec))

    write("knowledge/README.md", fm("SOQL Validation — Knowledge", "QE Specialized Skill Knowledge", "Guide", ["soql-validation", "knowledge-index"]) + """# SOQL Validation — Knowledge

Skill-specific reasoning for validation SOQL. Canonical performance/data depth: [`../../knowledge/performance/`](../../knowledge/performance/README.md) · [`../../knowledge/data/`](../../knowledge/data/README.md).

| Document | Focus |
|----------|-------|
| [SOQL Fundamentals](soql-fundamentals.md) | Intent before query |
| [Relationship Queries](relationship-queries.md) | Parent/child SOQL |
| [Aggregate Functions](aggregate-functions.md) | COUNT, GROUP BY |
| [Date Literals](date-literals.md) | Time-bound validation |
| [Governor Limits](governor-limits.md) | Limit awareness |
| [Query Selectivity](query-selectivity.md) | Selective filters |
| [Large Data Volumes](large-data-volumes.md) | LDV patterns |
| [Indexing](indexing.md) | Index-aware filters |
| [Query Optimization](query-optimization.md) | Improve queries |
| [Security Considerations](security-considerations.md) | FLS/sharing warnings |
| [Formula Fields](formula-fields.md) | Formula query rules |
| [Polymorphic Relationships](polymorphic-relationships.md) | WhoId/WhatId |
| [Tooling API Queries](tooling-api-queries.md) | Metadata deps |
| [Metadata API Queries](metadata-api-queries.md) | Deploy context |
| [Query Best Practices](query-best-practices.md) | Synthesis |
""")

    playbooks = [
        ("Functional Validation Playbook", "functional-validation.md", "Validate business outcomes via backend SOQL after functional actions.",
         ["User story / AC", "Object and persona", "Test data identifiers"],
         ["Define validation objective per AC.", "Draft SOQL with run-as context.", "Document expected vs actual interpretation.", "Log negative validation."],
         ["Does UI-only proof suffice?", "Is backend SOQL necessary?"],
         ["SOQL Validation Report", "Backend Validation Checklist"],
         ["Query returns expected row set or count", "Negative path shows blocked or excluded records"],
         ["Ambiguous AC → BA clarification", "Security mismatch → Security Architect"],
         "[../../playbooks/test-design-review.md](../../playbooks/test-design-review.md)"),
        ("Backend Validation Playbook", "backend-validation.md", "Verify server-side state without relying on UI alone.",
         ["Automation or Flow under test", "Record IDs or correlation keys"],
         ["Identify persisted fields and related records.", "Build selective SOQL.", "Assess security and performance.", "Compare to expected backend state."],
         ["API vs UI channel?", "Bulk vs single record?"],
         ["SOQL Validation Report", "Query Review Template"],
         ["Field values match business rule", "Related records created/updated correctly"],
         ["Governor risk in prod → Performance review"],
         ""),
        ("Data Migration Validation Playbook", "data-migration-validation.md", "Reconcile migrated data counts and key fields.",
         ["Migration mapping", "Source/target counts", "Key business fields"],
         ["Define reconciliation metrics.", "Use aggregate SOQL on both sides (conceptually).", "Sample detail queries for exceptions.", "Document tolerances."],
         ["Full vs sample reconcile?", "Acceptable variance?"],
         ["Data Verification Report", "Aggregate query pack"],
         ["Counts within tolerance", "Exception queue empty or explained"],
         ["Variance over threshold → Migration lead"],
         "[../../knowledge/data/data-migration-validation.md](../../knowledge/data/data-migration-validation.md)"),
        ("Regression Validation Playbook", "regression-validation.md", "SOQL smoke pack for regression scope from impact or release.",
         ["Regression scope list", "Changed metadata", "Environment"],
         ["Map components to validation queries.", "Prioritize High risk objects.", "Produce regression validation report."],
         ["In vs Conditional scope?", "[../../playbooks/regression-planning.md](../../playbooks/regression-planning.md)"],
         ["Regression Validation Report"],
         ["Smoke queries pass in target sandbox", "No unexpected nulls or orphans"],
         ["Failure → Test Lead + dev owner"],
         ""),
        ("Release Validation Playbook", "release-validation.md", "Post-deploy SOQL verification for release gate.",
         ["Release notes", "Deploy manifest", "Smoke personas"],
         ["Execute release validation checklist queries.", "Compare to pre-deploy baseline where available.", "Support Go/No-Go with evidence."],
         ["Production query allowed?", "[../../knowledge/release/production-verification.md](../../knowledge/release/production-verification.md)"],
         ["Release Validation Checklist", "SOQL Validation Report"],
         ["Critical metrics green", "No orphan or duplicate anomalies"],
         ["Production anomaly → Release Manager Sev2"],
         ""),
        ("Integration Validation Playbook", "integration-validation.md", "Verify integration outcomes via SOQL on persisted records.",
         ["Integration correlation ID", "External system payload", "Named credential context"],
         ["Trace object/field updates from integration.", "Build queries on status/staging fields.", "Validate error records and retries."],
         ["Sync vs async?", "Idempotency key field?"],
         ["SOQL Validation Report", "Integration exception queries"],
         ["Staging cleared", "Status fields match middleware state"],
         ["Persistent errors → Integration Architect"],
         "[../../knowledge/integration/](../../knowledge/integration/README.md)"),
    ]
    for pb in playbooks:
        write(f"playbooks/{pb[1]}", playbook(*pb))

    write("playbooks/README.md", fm("SOQL Validation — Playbooks", "QE Specialized Skill Playbook", "Guide", ["soql-validation"]) + """# SOQL Validation — Playbooks

| Playbook | Focus |
|----------|-------|
| [Functional Validation](functional-validation.md) | AC backend proof |
| [Backend Validation](backend-validation.md) | Server-side state |
| [Data Migration Validation](data-migration-validation.md) | Reconciliation |
| [Regression Validation](regression-validation.md) | Regression smoke SOQL |
| [Release Validation](release-validation.md) | Post-deploy |
| [Integration Validation](integration-validation.md) | Integration outcomes |
""")

    templates = [
        ("SOQL Validation Report", "soql-validation-report.md", OUTPUT_SECTIONS),
        ("Backend Validation Checklist", "backend-validation-checklist.md", ["Objective", "Record Context", "Queries", "Expected", "Actual", "Pass/Fail", "Owner"]),
        ("Data Verification Report", "data-verification-report.md", ["Reconciliation Scope", "Source Metrics", "Target Metrics", "Variance", "Exception Queries", "Sign-off"]),
        ("Regression Validation Report", "regression-validation-report.md", ["Scope", "Queries Executed", "Results", "Failures", "Recommendations"]),
        ("Release Validation Checklist", "release-validation-checklist.md", ["Pre-Deploy Baseline", "Post-Deploy Queries", "Smoke Results", "Open Issues", "Go/No-Go"]),
        ("Query Review Template", "query-review-template.md", ["Original Query", "Objective", "Selectivity Review", "Security Review", "Recommended Changes", "Approved Query"]),
    ]
    for title, slug, sections in templates:
        write(f"templates/{slug}", template_doc(title, sections))

    write("templates/README.md", fm("SOQL Validation — Templates", "QE Specialized Skill Template", "Guide", ["soql-validation"]) + """# SOQL Validation — Templates

| Template | Use |
|----------|-----|
| [SOQL Validation Report](soql-validation-report.md) | Primary 14-section deliverable |
| [Backend Validation Checklist](backend-validation-checklist.md) | Backend proof |
| [Data Verification Report](data-verification-report.md) | Migration reconcile |
| [Regression Validation Report](regression-validation-report.md) | Regression SOQL |
| [Release Validation Checklist](release-validation-checklist.md) | Release gate |
| [Query Review Template](query-review-template.md) | Optimize/review |
""")

    base = (
        "Act as SOQL Validation Assistant. State Validation Objective and Business Context BEFORE any SOQL. "
        "Produce all 14 sections per SKILL.md. Include Security and Performance Considerations. "
        "Label assumptions. Context:\n[paste]"
    )
    prompts = [
        ("Generate Validation SOQL", "generate-validation-soql.md", base, OUTPUT_SECTIONS),
        ("Review Existing SOQL", "review-existing-soql.md", base + "\nReview this query for objective, selectivity, security:\n[paste SOQL]", OUTPUT_SECTIONS),
        ("Optimize SOQL", "optimize-soql.md", base + "\nOptimize for selectivity and governors:\n[paste SOQL]", ["Validation Objective", "Recommended SOQL", "Performance Considerations", "Alternative Queries", "QA Recommendations"]),
        ("Validate Data Migration", "validate-data-migration.md", base + "\nFocus: migration reconciliation aggregates and exception samples.", OUTPUT_SECTIONS),
        ("Validate Integration", "validate-integration.md", base + "\nFocus: integration staging/status fields and correlation IDs.", OUTPUT_SECTIONS),
        ("Verify Flow Results", "verify-flow-results.md", base + "\nFocus: records created/updated by Flow; related object state.", OUTPUT_SECTIONS),
        ("Verify Reports", "verify-reports.md", base + "\nFocus: underlying report type fields vs SOQL row counts/filters.", OUTPUT_SECTIONS),
        ("Verify Dashboard Data", "verify-dashboard-data.md", base + "\nFocus: dashboard component metrics vs aggregate SOQL.", OUTPUT_SECTIONS),
        ("Validate Bulk Operations", "validate-bulk-operations.md", base + "\nFocus: bulk job results, partial failures, governor-safe sampling.", OUTPUT_SECTIONS),
        ("Generate Aggregate Queries", "generate-aggregate-queries.md", base + "\nFocus: COUNT, GROUP BY, HAVING for duplicate detection or reconcile.", OUTPUT_SECTIONS),
    ]
    for title, slug, prompt, sections in prompts:
        write(f"prompts/{slug}", prompt_doc(title, prompt, sections))

    write("prompts/README.md", fm("SOQL Validation — Prompts", "QE Specialized Skill Prompt", "Guide", ["soql-validation"]) + """# SOQL Validation — Prompts

| Prompt | File |
|--------|------|
| Generate Validation SOQL | [generate-validation-soql.md](generate-validation-soql.md) |
| Review Existing SOQL | [review-existing-soql.md](review-existing-soql.md) |
| Optimize SOQL | [optimize-soql.md](optimize-soql.md) |
| Validate Data Migration | [validate-data-migration.md](validate-data-migration.md) |
| Validate Integration | [validate-integration.md](validate-integration.md) |
| Verify Flow Results | [verify-flow-results.md](verify-flow-results.md) |
| Verify Reports | [verify-reports.md](verify-reports.md) |
| Verify Dashboard Data | [verify-dashboard-data.md](verify-dashboard-data.md) |
| Validate Bulk Operations | [validate-bulk-operations.md](validate-bulk-operations.md) |
| Generate Aggregate Queries | [generate-aggregate-queries.md](generate-aggregate-queries.md) |
""")

    examples = [
        ("Account Validation", "account-validation.md", "Enterprise customer tier assignment after nightly batch.", "Verify Account.Service_Tier__c populated for active customers.",
         "SELECT Id, Name, Service_Tier__c FROM Account WHERE Active__c = true AND Service_Tier__c = null LIMIT 200",
         "Zero rows — all active accounts tiered.", "Inactive account with null tier excluded by filter.", "If rows returned, rerun batch or fix mapping."),
        ("Opportunity Validation", "opportunity-validation.md", "Opportunity stage automation sets Probability.", "Closed Won opportunities have Probability = 100.",
         "SELECT Id, StageName, Probability FROM Opportunity WHERE StageName = 'Closed Won' AND Probability != 100 LIMIT 100",
         "Zero rows.", "Open opportunities with 100 probability — separate query.", "Pair with Flow debug for stage transitions."),
        ("Case Validation", "case-validation.md", "Case closure requires Resolution Code.", "No closed Case missing Resolution_Code__c.",
         "SELECT Id, Status, Resolution_Code__c FROM Case WHERE Status = 'Closed' AND Resolution_Code__c = null LIMIT 50",
         "Zero rows.", "Non-closed cases with null code allowed.", "Critical for Service Cloud regression."),
        ("Contact Validation", "contact-validation.md", "Primary contact flag unique per Account.", "At most one Primary_Contact__c per Account.",
         "SELECT AccountId, COUNT(Id) cnt FROM Contact WHERE Primary_Contact__c = true GROUP BY AccountId HAVING COUNT(Id) > 1",
         "Zero groups.", "Accounts with zero primary — business rule dependent.", "Fix duplicate primaries before release."),
        ("Custom Object Validation", "custom-object-validation.md", "Service_Contract__c synced from ERP.", "Each contract links to Account.",
         "SELECT Id FROM Service_Contract__c WHERE Account__c = null LIMIT 10", "Zero rows.", "Contracts in recycle bin excluded if filter added.", "Block deploy if orphans exist."),
        ("Flow Validation", "flow-validation.md", "Flow creates Task on Case update.", "Cases updated today have follow-up Task.",
         "SELECT Id FROM Case WHERE Id NOT IN (SELECT WhatId FROM Task WHERE CreatedDate = TODAY) AND Status = 'Working' LIMIT 20",
         "Sample set empty or explained by flow criteria.", "Cases outside flow criteria.", "Tune filter to flow entry conditions."),
        ("Validation Rule Verification", "validation-rule-verification.md", "VR blocks discount > 40%.", "No Opportunity with Discount__c > 0.40.",
         "SELECT Id, Discount__c FROM Opportunity WHERE Discount__c > 0.40 LIMIT 10", "Zero rows.", "VR bypass user — run as standard sales user.", "Run as integration user separately."),
        ("Integration Verification", "integration-verification.md", "ERP sync sets External_Id__c.", "Synced records have External_Id__c populated.",
         "SELECT Id FROM Order WHERE Sync_Status__c = 'Synced' AND External_Id__c = null LIMIT 20", "Zero rows.", "Pending sync rows may legitimately lack ID.", "Correlate with middleware error logs."),
        ("Bulk Data Validation", "bulk-data-validation.md", "Data Loader upsert 10k Contacts.", "No duplicate emails in batch scope.",
         "SELECT Email, COUNT(Id) FROM Contact WHERE LastModifiedDate = TODAY GROUP BY Email HAVING COUNT(Id) > 1", "Zero duplicate emails in scope.", "Null emails grouped separately.", "Sample LIMIT if LDV."),
        ("Data Migration Reconciliation", "data-migration-reconciliation.md", "Migrate 50k Asset records.", "Target count matches source within tolerance.",
         "SELECT COUNT() FROM Asset WHERE Migrated__c = true", "Count matches migration manifest ± agreed tolerance.", "Assets excluded by filter documented.", "Full count in sandbox; sample in prod if LDV."),
        ("Utilities Domain Validation", "utilities-domain-validation.md", "Utility account billing hold flag.", "Active billing accounts not on hold unless exception reason set.",
         "SELECT Id FROM Account WHERE RecordType.DeveloperName = 'Utility_Account' AND Billing_Hold__c = true AND Hold_Reason__c = null LIMIT 50",
         "Zero rows.", "Inactive accounts may be on hold without reason per BR.", "Cross-link utilities industry scenarios."),
        ("Service Cloud Validation", "service-cloud-validation.md", "Entitlement consumed on Case close.", "Closed Cases have Entitlement consumed or waived.",
         "SELECT Id FROM Case WHERE Status = 'Closed' AND Entitlement_Status__c = null LIMIT 30", "Zero rows per entitlement model.", "Cases without entitlement product.", "Confirm entitlement model in org."),
        ("Sales Cloud Validation", "sales-cloud-validation.md", "Quote synced to Opportunity amount.", "Primary quote amount matches Opportunity Amount.",
         "SELECT Id, Amount FROM Opportunity WHERE Id IN (SELECT OpportunityId FROM Quote WHERE IsSyncing = true AND TotalPrice != Opportunity.Amount) LIMIT 20",
         "Zero rows — adjust for org quote model.", "Opportunities without quotes.", "Validate CPQ vs standard Quote objects per org."),
    ]
    for title, slug, scenario, objective, soql, expected, negative, qa in examples:
        write(f"examples/{slug}", example_doc(title, scenario, objective, soql, expected, negative, qa))

    write("examples/README.md", fm("SOQL Validation — Examples", "QE Specialized Skill Example", "Guide", ["soql-validation"]) + """# SOQL Validation — Examples

| Example | Domain |
|---------|--------|
| [Account Validation](account-validation.md) | Account |
| [Opportunity Validation](opportunity-validation.md) | Sales |
| [Case Validation](case-validation.md) | Service |
| [Contact Validation](contact-validation.md) | Data quality |
| [Custom Object Validation](custom-object-validation.md) | Custom object |
| [Flow Validation](flow-validation.md) | Automation |
| [Validation Rule Verification](validation-rule-verification.md) | VR |
| [Integration Verification](integration-verification.md) | Integration |
| [Bulk Data Validation](bulk-data-validation.md) | Bulk |
| [Data Migration Reconciliation](data-migration-reconciliation.md) | Migration |
| [Utilities Domain Validation](utilities-domain-validation.md) | Utilities |
| [Service Cloud Validation](service-cloud-validation.md) | Service Cloud |
| [Sales Cloud Validation](sales-cloud-validation.md) | Sales Cloud |
""")

    tests = [
        ("query-accuracy", "SOQL matches stated validation objective and filters"),
        ("business-logic", "Validation Objective ties to business rule before query"),
        ("relationship", "Relationship query documents parent/child direction"),
        ("aggregate", "Aggregate query includes GROUP BY/HAVING rationale"),
        ("security", "Security Considerations warn on FLS/sharing"),
        ("performance", "Performance Considerations address selectivity/LIMIT"),
        ("data-reconciliation", "Migration example includes tolerance language"),
        ("duplicate-detection", "Duplicate query uses HAVING COUNT > 1 pattern"),
        ("release-validation", "Release playbook queries support Go/No-Go"),
    ]
    for slug, desc in tests:
        write(f"tests/scenario-{slug}.md", fm(f"Test — {slug}", "QE Specialized Skill Test", "Test Scenario", ["soql-validation"]) + f"""# Test Scenario — {slug}

## Objective

{desc}

## Pass Criteria

- Validation Objective before Recommended SOQL
- Sections 7–8 present
- Assumptions labeled

## Fail Criteria

- Raw SOQL without objective
- Missing security or performance section
""")

    write("tests/README.md", fm("SOQL Validation — Tests", "QE Specialized Skill Test", "Guide", ["soql-validation"]) + """# SOQL Validation — Tests

Run with [../prompts/generate-validation-soql.md](../prompts/generate-validation-soql.md) and [../examples/](../examples/README.md).

| Scenario | Focus |
|----------|-------|
| [query-accuracy](scenario-query-accuracy.md) | Query matches objective |
| [business-logic](scenario-business-logic.md) | Objective first |
| [relationship](scenario-relationship.md) | Relationship SOQL |
| [aggregate](scenario-aggregate.md) | Aggregates |
| [security](scenario-security.md) | FLS/sharing |
| [performance](scenario-performance.md) | Selectivity |
| [data-reconciliation](scenario-data-reconciliation.md) | Migration |
| [duplicate-detection](scenario-duplicate-detection.md) | Duplicates |
| [release-validation](scenario-release-validation.md) | Release gate |
""")

    print("Done.")


if __name__ == "__main__":
    main()
