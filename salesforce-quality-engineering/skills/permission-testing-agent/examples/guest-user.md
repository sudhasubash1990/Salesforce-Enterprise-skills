---
title: Guest User
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

# Guest User

## Business Scenario

Public knowledge articles only.

## Security Requirement

Guest cannot access CRM objects.

## Validation Strategy

Minimal guest profile audit.

## Expected Result

Only public content accessible.

## Negative Validation

Any CRM object access fails.

## Recommended SOQL

```sql
Verify no object CRUD on guest profile via setup metadata review
```

## QA Recommendations

Critical — Legal/Security review for guest changes.
