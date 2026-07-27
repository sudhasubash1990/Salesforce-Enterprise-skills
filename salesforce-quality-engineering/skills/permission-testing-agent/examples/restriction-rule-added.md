---
title: Restriction Rule Added
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

# Restriction Rule Added

## Business Scenario

Hide high-value Accounts from standard sales.

## Security Requirement

Accounts with Tier=Platinum hidden except exec role.

## Validation Strategy

Restriction + role exception tests.

## Expected Result

Standard user cannot see Platinum.

## Negative Validation

Exec role can see.

## Recommended SOQL

```sql
SELECT Id FROM Account WHERE Tier__c = 'Platinum'
```

## QA Recommendations

Combine with sharing rules in test plan.
