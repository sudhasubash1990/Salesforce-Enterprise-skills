---
title: Account and Contact Data
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.20.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [test-data-generator, example]
---

# Account and Contact Data

## Business Scenario

Seed B2B accounts with related contacts for SIT smoke.

## Required Objects

Account, Contact

## Relationships

Account 1—M Contact (lookup)

## Sample Data (Synthetic)

Account: Acme Test Co (External_Id__c=TDG-ACC-001); Contact: Jane Tester jane.tester@example.test

## Validation Rules

Contact must have AccountId; Email format valid.

## Expected Results

Contacts linked; no orphans.

## Recommended SOQL

```sql
SELECT Id, AccountId FROM Contact WHERE Email LIKE '%@example.test'
```

## QA Recommendations

Chain SOVA for counts; PTA if private OWD.
