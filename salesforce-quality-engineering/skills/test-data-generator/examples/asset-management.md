---
title: Asset Management
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

# Asset Management

## Business Scenario

Installed asset under Account for service journeys.

## Required Objects

Account, Contact, Asset, Product2

## Relationships

Asset→Account, Asset→Product2, Asset→Contact optional

## Sample Data (Synthetic)

Asset TDG-AST-001 Status=Installed SerialNumber=AST-TEST-55

## Validation Rules

Serial uniqueness if org-enforced.

## Expected Results

Asset visible under Account.

## Recommended SOQL

```sql
SELECT Id, AccountId, Status FROM Asset WHERE SerialNumber = 'AST-TEST-55'
```

## QA Recommendations

Chain Case example for break-fix.
