---
title: Customer Community User
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

# Customer Community User

## Business Scenario

Customers view own Cases.

## Security Requirement

Read own Cases via account contact relationship.

## Validation Strategy

Contact/Account linkage visibility.

## Expected Result

Own cases visible.

## Negative Validation

Other customer cases hidden.

## Recommended SOQL

```sql
SELECT Id, ContactId FROM Case WHERE ContactId = :contactId
```

## QA Recommendations

Profile change Critical risk.
