---
title: Utility Customer and Meter Data
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

# Utility Customer and Meter Data

## Business Scenario

Utilities synthetic customer with service point/meter placeholders.

## Required Objects

Account, Contact, Asset (Meter), Case (optional)

## Relationships

Account→Asset; Account→Case

## Sample Data (Synthetic)

Account TDG-UTIL-001; Asset SerialNumber=MTR-TEST-1001

## Validation Rules

Do not invent Industries Cloud objects unless confirmed.

## Expected Results

Customer+meter linked synthetically.

## Recommended SOQL

```sql
SELECT Id, AccountId FROM Asset WHERE SerialNumber LIKE 'MTR-TEST-%'
```

## QA Recommendations

Chain FSQA if Work Orders added later.
