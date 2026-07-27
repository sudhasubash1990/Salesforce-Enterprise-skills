---
title: Water Meter Installation
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

# Water Meter Installation

## Business Scenario

New residential meter install with skill Plumber and van parts.

## FSL Components

WO, WOLI, SA, Skill Requirements, Product Required, Mobile.

## Scheduling Rules

Skill match required; operating hours 8–17; parts reserved.

## Test Objectives

Skill enforcement; parts consumption on complete; mobile photo.

## Backend Validation

Products Consumed rows; Assigned Resource skills.

## Expected Results

Only plumber resources candidates; stock decremented.

## Negative Scenarios

Unskilled tech assigned; complete without consuming part.

## Recommended SOQL

```sql
SELECT Id FROM AssignedResource WHERE ServiceResourceId = :resId
```

## QA Recommendations

Inventory reconciliation via SOVA.
