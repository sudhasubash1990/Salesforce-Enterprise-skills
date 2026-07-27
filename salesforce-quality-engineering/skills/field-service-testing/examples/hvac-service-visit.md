---
title: HVAC Service Visit
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.19.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [field-service-testing, example]
---

# HVAC Service Visit

## Business Scenario

Break-fix HVAC with parts transfer from warehouse to van.

## FSL Components

WO, Product Transfer, Product Request, Mobile offline.

## Scheduling Rules

Parts transfer before dispatch; offline complete allowed.

## Test Objectives

Transfer completed; offline sync preserves consumption.

## Backend Validation

ProductTransfer status; Products Consumed.

## Expected Results

Stock moved; SA completed after sync.

## Negative Scenarios

Offline complete then desktop deletes SA.

## Recommended SOQL

```sql
SELECT Id, QuantityConsumed FROM ProductConsumed WHERE WorkOrderId = :woId
```

## QA Recommendations

Offline conflict Critical if data loss.
