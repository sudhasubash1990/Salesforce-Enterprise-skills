---
title: Utilities Domain Validation
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

# Utilities Domain Validation

## Business Scenario

Utility account billing hold flag.

## Validation Objective

Active billing accounts not on hold unless exception reason set.

## Generated SOQL

```sql
SELECT Id FROM Account WHERE RecordType.DeveloperName = 'Utility_Account' AND Billing_Hold__c = true AND Hold_Reason__c = null LIMIT 50
```

## Expected Result

Zero rows.

## Negative Validation

Inactive accounts may be on hold without reason per BR.

## QA Recommendation

Cross-link utilities industry scenarios.

## Related Documents

- [examples/README.md](README.md)
- [SKILL.md](../SKILL.md)
