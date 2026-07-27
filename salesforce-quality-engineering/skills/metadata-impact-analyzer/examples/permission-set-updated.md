---
title: Permission Set Updated
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

# Permission Set Updated

## Input

**Change:** Permission set `FSL_Dispatcher` granted Edit on `WorkOrder` and FLS Edit on `WorkOrder.Priority__c`.

Permission set assigned to 120 users via Permission Set Group `Field_Service_Ops`.

## Expected Analysis (Dependency First)

- FLS expansion — verify dispatcher personas only.
- WorkOrder sharing still applies — Edit CRUD does not bypass sharing.
- Mobile FSL app may cache permissions — retest mobile.

## Expected Regression

| Scope | Rationale |
|-------|-----------|
| In | Dispatcher edit WorkOrder priority |
| In | Technician without perm set cannot edit |
| In | PSG assignment smoke for sample users |

## Expected Risk

**Rating:** Medium

## Expected SOQL Validations

```sql
SELECT AssigneeId, PermissionSet.Name FROM PermissionSetAssignment WHERE PermissionSet.Name = 'FSL_Dispatcher'
```

## Related Documents

- [SKILL.md](../SKILL.md)
- [examples/README.md](README.md)
