---
title: Data Migration Reconciliation
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.16.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [soql-validation, example]
---

# Data Migration Reconciliation

## Business Scenario

Migrate 50k Asset records.

## Validation Objective

Target count matches source within tolerance.

## Generated SOQL

```sql
SELECT COUNT() FROM Asset WHERE Migrated__c = true
```

## Expected Result

Count matches migration manifest ± agreed tolerance.

## Negative Validation

Assets excluded by filter documented.

## QA Recommendation

Full count in sandbox; sample in prod if LDV.

## Related Documents

- [examples/README.md](README.md)
- [SKILL.md](../SKILL.md)
