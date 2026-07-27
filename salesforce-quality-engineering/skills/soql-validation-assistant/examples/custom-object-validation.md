---
title: Custom Object Validation
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

# Custom Object Validation

## Business Scenario

Service_Contract__c synced from ERP.

## Validation Objective

Each contract links to Account.

## Generated SOQL

```sql
SELECT Id FROM Service_Contract__c WHERE Account__c = null LIMIT 10
```

## Expected Result

Zero rows.

## Negative Validation

Contracts in recycle bin excluded if filter added.

## QA Recommendation

Block deploy if orphans exist.

## Related Documents

- [examples/README.md](README.md)
- [SKILL.md](../SKILL.md)
