---
title: Profile Updated
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

# Profile Updated

## Input

**Change:** Standard profile `Customer Community User` tab visibility changed; Object CRUD on `Case` reduced from Edit to Read.

Experience Cloud site `Support Portal` uses this profile.

## Expected Analysis (Dependency First)

- Community users lose Case edit — self-service flows may break.
- LWC components checking edit access need review.
- High visibility / reputational risk if portal breaks at deploy.

## Expected Regression

| Scope | Rationale |
|-------|-----------|
| In | Portal user Case create/update paths |
| In | Negative: edit denied with clear message |
| Out | Internal agent Case edit (unaffected profile) |

## Expected Risk

**Rating:** Critical

## Expected SOQL Validations

```sql
SELECT Id, SobjectType, PermissionsEdit FROM ObjectPermissions WHERE Parent.Profile.Name = 'Customer Community User' AND SobjectType = 'Case'
```

## Related Documents

- [SKILL.md](../SKILL.md)
- [examples/README.md](README.md)
