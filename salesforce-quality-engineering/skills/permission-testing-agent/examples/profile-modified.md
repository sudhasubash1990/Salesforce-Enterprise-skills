---
title: Profile Modified
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

# Profile Modified

## Business Scenario

Community profile Case CRUD reduced to Read.

## Security Requirement

Portal users read-only Case.

## Validation Strategy

Community profile CRUD matrix.

## Expected Result

Edit blocked with clear error.

## Negative Validation

Internal profile unchanged.

## Recommended SOQL

```sql
ObjectPermissions query for community profile Case Edit=false
```

## QA Recommendations

Critical deploy risk.
