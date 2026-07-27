---
title: Case Validation
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

# Case Validation

## Business Scenario

Case closure requires Resolution Code.

## Validation Objective

No closed Case missing Resolution_Code__c.

## Generated SOQL

```sql
SELECT Id, Status, Resolution_Code__c FROM Case WHERE Status = 'Closed' AND Resolution_Code__c = null LIMIT 50
```

## Expected Result

Zero rows.

## Negative Validation

Non-closed cases with null code allowed.

## QA Recommendation

Critical for Service Cloud regression.

## Related Documents

- [examples/README.md](README.md)
- [SKILL.md](../SKILL.md)
