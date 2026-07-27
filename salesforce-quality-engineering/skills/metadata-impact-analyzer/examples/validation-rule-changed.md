---
title: Validation Rule Changed
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

# Validation Rule Changed

## Input

**Change:** Validation rule `Case_Closure_Check` on Case updated to require `Resolution_Code__c` when Status = Closed.

VR formula now references `Resolution_Code__c`. Integration `CaseSync` updates Case status via REST.

## Expected Analysis (Dependency First)

- VR blocks API close without Resolution_Code — integration payloads must include field.
- UI agents see new error on save — training impact.
- Order: field must exist before VR deploy.

## Expected Regression

| Scope | Rationale |
|-------|-----------|
| In | UI close with/without Resolution_Code |
| In | API CaseSync close payloads |
| In | Bulk close data loader scenarios |

## Expected Risk

**Rating:** High

## Expected SOQL Validations

```sql
SELECT Id, Status, Resolution_Code__c FROM Case WHERE Status = 'Closed' AND Resolution_Code__c = null LIMIT 50
```

## Related Documents

- [SKILL.md](../SKILL.md)
- [examples/README.md](README.md)
