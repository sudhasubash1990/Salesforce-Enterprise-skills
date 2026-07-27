---
title: Custom Object Added
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

# Custom Object Added

## Input

**Change:** New custom object `Service_Contract__c` with master-detail to Account, two validation rules, and tab.

Sharing controlled by parent Account. Integration will sync contracts nightly.

## Expected Analysis (Dependency First)

- MD relationship drives sharing and delete behavior.
- New tab and app visibility via profiles/perm sets.
- Integration must respect VR and required fields.

## Expected Regression

| Scope | Rationale |
|-------|-----------|
| In | CRUD and sharing via Account parent |
| In | VR on create/update |
| In | Integration upsert payload |

## Expected Risk

**Rating:** High

## Expected SOQL Validations

```sql
SELECT Id, Account__c FROM Service_Contract__c LIMIT 10
```

## Related Documents

- [SKILL.md](../SKILL.md)
- [examples/README.md](README.md)
