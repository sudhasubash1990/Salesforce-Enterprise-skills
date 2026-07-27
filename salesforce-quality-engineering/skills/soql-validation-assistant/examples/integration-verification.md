---
title: Integration Verification
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

# Integration Verification

## Business Scenario

ERP sync sets External_Id__c.

## Validation Objective

Synced records have External_Id__c populated.

## Generated SOQL

```sql
SELECT Id FROM Order WHERE Sync_Status__c = 'Synced' AND External_Id__c = null LIMIT 20
```

## Expected Result

Zero rows.

## Negative Validation

Pending sync rows may legitimately lack ID.

## QA Recommendation

Correlate with middleware error logs.

## Related Documents

- [examples/README.md](README.md)
- [SKILL.md](../SKILL.md)
