---
title: Account Validation
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

# Account Validation

## Business Scenario

Enterprise customer tier assignment after nightly batch.

## Validation Objective

Verify Account.Service_Tier__c populated for active customers.

## Generated SOQL

```sql
SELECT Id, Name, Service_Tier__c FROM Account WHERE Active__c = true AND Service_Tier__c = null LIMIT 200
```

## Expected Result

Zero rows — all active accounts tiered.

## Negative Validation

Inactive account with null tier excluded by filter.

## QA Recommendation

If rows returned, rerun batch or fix mapping.

## Related Documents

- [examples/README.md](README.md)
- [SKILL.md](../SKILL.md)
