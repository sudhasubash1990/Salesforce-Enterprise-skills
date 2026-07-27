---
title: Sales Cloud Validation
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

# Sales Cloud Validation

## Business Scenario

Quote synced to Opportunity amount.

## Validation Objective

Primary quote amount matches Opportunity Amount.

## Generated SOQL

```sql
SELECT Id, Amount FROM Opportunity WHERE Id IN (SELECT OpportunityId FROM Quote WHERE IsSyncing = true AND TotalPrice != Opportunity.Amount) LIMIT 20
```

## Expected Result

Zero rows — adjust for org quote model.

## Negative Validation

Opportunities without quotes.

## QA Recommendation

Validate CPQ vs standard Quote objects per org.

## Related Documents

- [examples/README.md](README.md)
- [SKILL.md](../SKILL.md)
