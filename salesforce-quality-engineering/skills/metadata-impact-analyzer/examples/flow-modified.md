---
title: Flow Modified
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

# Flow Modified

## Input

**Change:** Record-Triggered Flow `Opportunity_Auto_Approve` modified: new decision branch calls Apex `ApprovalService`.

Flow version 3 adds Apex action. Class `ApprovalService` already in org. Subflow `Notify_Sales_Manager` referenced.

## Expected Analysis (Dependency First)

- Apex action adds governor and exception surface.
- Subflow dependency — both must be active.
- Trigger on Opportunity may interact — check order of execution.

## Expected Regression

| Scope | Rationale |
|-------|-----------|
| In | Opportunity amounts triggering each branch |
| In | Apex fault path |
| Conditional | Email alert recipients if subflow changes |

## Expected Risk

**Rating:** High

## Expected SOQL Validations

```sql
SELECT Id, VersionNumber, Status FROM Flow WHERE Definition.DeveloperName = 'Opportunity_Auto_Approve'
```

## Related Documents

- [SKILL.md](../SKILL.md)
- [examples/README.md](README.md)
