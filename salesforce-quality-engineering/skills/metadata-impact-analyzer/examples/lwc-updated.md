---
title: LWC Updated
module: Salesforce Quality Engineering
category: Specialized Skill Example
document_type: Example
version: 0.15.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [metadata-impact-analyzer, example]
---

# LWC Updated

## Input

**Change:** LWC `accountHealthScore` updated to call Apex `HealthScoreController` with new `@AuraEnabled` method.

Component on Account Lightning record page. Guest users not in scope.

## Expected Analysis (Dependency First)

- Apex API change — controller method signature.
- FLS enforced in Apex with sharing.
- Jest tests advisory; manual on record page required.

## Expected Regression

| Scope | Rationale |
|-------|-----------|
| In | Component load and score display |
| In | Error handling when Apex throws |
| Conditional | Performance on list views if embedded elsewhere |

## Expected Risk

**Rating:** Medium

## Expected SOQL Validations

```sql
SELECT Id, Name FROM Account WHERE Id IN (SELECT ParentId FROM AccountContactRelation LIMIT 1)
```

## Related Documents

- [SKILL.md](../SKILL.md)
- [examples/README.md](README.md)
