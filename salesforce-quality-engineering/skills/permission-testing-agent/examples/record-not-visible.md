---
title: Record Not Visible
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.17.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [permission-testing, example]
---

# Record Not Visible

## Business Scenario

Private OWD Account — user not in share.

## Security Requirement

Record not visible without share/role.

## Validation Strategy

Sharing validation negative test.

## Expected Result

User cannot see record in UI/search.

## Negative Validation

Owner can see.

## Recommended SOQL

```sql
SELECT Id FROM Account WHERE Id = :recordId — expect 0 rows as test user
```

## QA Recommendations

Document sharing path when visible.
