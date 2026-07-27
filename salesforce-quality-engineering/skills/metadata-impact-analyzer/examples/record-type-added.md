---
title: Record Type Added
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

# Record Type Added

## Input

**Change:** New Record Type `Enterprise_Account` on Account with dedicated page layout and picklist values.

Assigned to Enterprise Sales profile. Existing automation keyed on RecordTypeId.

## Expected Analysis (Dependency First)

- Picklist value sets may be record-type specific.
- Layouts and compact layouts per record type.
- Flows filtering RecordType developer name need regression.

## Expected Regression

| Scope | Rationale |
|-------|-----------|
| In | Create Account with new record type |
| In | Picklist values visible per record type |
| Conditional | Automation branches on RecordType |

## Expected Risk

**Rating:** Medium

## Expected SOQL Validations

```sql
SELECT Id, DeveloperName, SobjectType FROM RecordType WHERE DeveloperName = 'Enterprise_Account'
```

## Related Documents

- [SKILL.md](../SKILL.md)
- [examples/README.md](README.md)
