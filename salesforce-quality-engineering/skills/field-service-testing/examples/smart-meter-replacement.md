---
title: Smart Meter Replacement
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

# Smart Meter Replacement

## Business Scenario

Utilities planned replacement with maintenance plan generation.

## FSL Components

Maintenance Plan, Maintenance Asset, WO, SA, Work Type.

## Scheduling Rules

Monthly generation; asset coverage complete.

## Test Objectives

Generated WO exists for due assets; appointments created.

## Backend Validation

WO Parent MaintenancePlanId populated.

## Expected Results

Due assets have open WO; none missing.

## Negative Scenarios

Asset due with no WO generated.

## Recommended SOQL

```sql
SELECT Id FROM WorkOrder WHERE MaintenancePlanId = :mpId
```

## QA Recommendations

Regression after maintenance plan config change.
