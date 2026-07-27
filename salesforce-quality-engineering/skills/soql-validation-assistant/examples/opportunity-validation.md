---
title: Opportunity Validation
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

# Opportunity Validation

## Business Scenario

Opportunity stage automation sets Probability.

## Validation Objective

Closed Won opportunities have Probability = 100.

## Generated SOQL

```sql
SELECT Id, StageName, Probability FROM Opportunity WHERE StageName = 'Closed Won' AND Probability != 100 LIMIT 100
```

## Expected Result

Zero rows.

## Negative Validation

Open opportunities with 100 probability — separate query.

## QA Recommendation

Pair with Flow debug for stage transitions.

## Related Documents

- [examples/README.md](README.md)
- [SKILL.md](../SKILL.md)
