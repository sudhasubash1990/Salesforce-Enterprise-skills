---
title: Data Migration QA — README
module: Salesforce Quality Engineering
category: QE Specialized Skill
document_type: Guide
version: 0.23.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [data-migration-qa]
---

# Data Migration QA (DMQA)

## Purpose

Enterprise **Salesforce Data Migration Quality Engineering** capability. Validates migration readiness, mapping, transformation, reconciliation, relationships, data quality, security, performance, cutover, rollback, and hypercare — not spreadsheet-only record counts.

Canonical encyclopedia remains in [`../../knowledge/data/`](../../knowledge/data/README.md). This pack holds **DMQA reasoning models**. SOQL depth for reconciliation stubs expands via [SOQL Validation Assistant](../soql-validation-assistant/SKILL.md).

## Capabilities

- Source/target assessment and migration scope  
- Field/relationship mapping and transformation validation  
- Record count, aggregate, and financial reconciliation strategy  
- Data quality (completeness, accuracy, uniqueness, orphans)  
- Security (CRUD/FLS/PII) and performance risk assessment  
- Cutover, rollback, and migration hypercare gates  

## Supported Migration Types

Legacy CRM → Sales Cloud · Service · Experience Users · CPQ/Product · Utilities/billing · Customer master · Contact/Opportunity/Case · Historical data · Custom objects · Attachments/Files · Incremental/delta/full

## Folder Structure

```
skills/data-migration-qa/
├── SKILL.md
├── README.md
├── skill-config.yaml
├── knowledge/       ← 19 reasoning articles
├── playbooks/       ← 8 playbooks
├── templates/       ← 9 templates
├── prompts/         ← 10 prompts
├── examples/        ← 10 examples
└── tests/           ← 12 scenarios
```

## Inputs

| Input | Required |
|-------|----------|
| Migration Scope (objects, waves, volumes) | Yes |
| Source system description | Yes |
| Target Salesforce model | Yes |
| Mapping / transformation rules (sanitized) | Recommended |
| External ID / load order | Recommended |
| Personas / PII classification | When security in scope |
| MIA impact report | When new metadata for migration |

## Outputs

20-section Data Migration QA report — see [SKILL.md](SKILL.md). Primary template: [templates/reconciliation-report.md](templates/reconciliation-report.md).

## Sample Prompt

```
Load skills/data-migration-qa/SKILL.md.
Migration Scope: Legacy CRM Account–Contact–Opportunity to Sales Cloud.
Produce all 20 sections including Mapping, Reconciliation Strategy, Cutover, Rollback, and Hypercare.
Label assumptions; do not invent Bulk API duration %; chain SOVA for section 16 stubs.
```

See [prompts/README.md](prompts/README.md).

## Examples

See [examples/README.md](examples/README.md) — Sales Cloud, Utilities, CPQ, Experience, historical billing.

## Best Practices

- Migration Scope + Source/Target Assessment **before** detailed cases  
- Always validate relationships and External ID upsert strategy  
- Pair section 16 with SOVA for full query packs  
- Chain PTA for Experience/PII; TDG for synthetic dry-run  
- Label assumptions; never invent performance SLAs or GDPR certification  

## Common Migration Risks

- Parent-child load order / orphan lookups  
- Duplicate External IDs / silent upsert collisions  
- Picklist / record type mismatches  
- OwnerId / sharing after migrate  
- Attachment/File content gaps  
- Count match with wrong field values  

## Limitations

- No live load/ETL execution  
- Org-specific API names must be confirmed or labeled TBC  
- Planned siblings (Risk-Based Regression, Production RCA) — cross-link only  

## Future Enhancements

- Deeper Financial Services / Health Cloud migration packs  
- Risk-based regression registry for migration waves  
- Production RCA themes for migration defects  

## Related Documents

- [SKILL.md](SKILL.md)  
- [skill-config.yaml](skill-config.yaml)  
- [Parent skill.md](../../skill.md)  
- [Data Migration Validation (4A)](../../knowledge/data/data-migration-validation.md)  
- [SOQL Validation Assistant](../soql-validation-assistant/SKILL.md)  

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial Data Migration QA capability |
