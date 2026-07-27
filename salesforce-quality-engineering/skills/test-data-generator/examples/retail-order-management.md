---
title: Retail Order Management
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

# Retail Order Management

## Business Scenario

Retail order with products for omnichannel SIT.

## Required Objects

Account, Product2, Pricebook2, PricebookEntry, Order, OrderItem

## Relationships

Order→Account; OrderItem→Order/Product via PBE

## Sample Data (Synthetic)

Order TDG-ORD-001; OrderItem qty=2 Product=SKU-TEST-01

## Validation Rules

Standard Pricebook activation assumed in sandbox.

## Expected Results

Order totals consistent with items.

## Recommended SOQL

```sql
SELECT Id, OrderId, Quantity FROM OrderItem WHERE Order.External_Id__c = 'TDG-ORD-001'
```

## QA Recommendations

Load PricebookEntry before OrderItem.
