---
title: Validation Rule Verification
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

# Validation Rule Verification

## Business Scenario

VR blocks discount > 40%.

## Validation Objective

No Opportunity with Discount__c > 0.40.

## Generated SOQL

```sql
SELECT Id, Discount__c FROM Opportunity WHERE Discount__c > 0.40 LIMIT 10
```

## Expected Result

Zero rows.

## Negative Validation

VR bypass user — run as standard sales user.

## QA Recommendation

Run as integration user separately.

## Related Documents

- [examples/README.md](README.md)
- [SKILL.md](../SKILL.md)
