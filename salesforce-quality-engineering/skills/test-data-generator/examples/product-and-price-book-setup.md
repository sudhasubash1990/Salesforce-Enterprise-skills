---
title: Product and Price Book Setup
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

# Product and Price Book Setup

## Business Scenario

Baseline catalog for sales and service tests.

## Required Objects

Product2, Pricebook2, PricebookEntry

## Relationships

PBE links Product to Pricebook

## Sample Data (Synthetic)

Product SKU-TEST-01 Active; Custom Pricebook TDG-PB-01; PBE UnitPrice=99

## Validation Rules

Active product required for PBE.

## Expected Results

Catalog usable by Opportunity/Order examples.

## Recommended SOQL

```sql
SELECT Id, UnitPrice FROM PricebookEntry WHERE Pricebook2.Name = 'TDG-PB-01'
```

## QA Recommendations

Treat as shared reference — protect in cleanup.
