---
title: Multi-Day Field Project
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

# Multi-Day Field Project

## Business Scenario

Manufacturing plant shutdown multi-day crew project.

## FSL Components

WO, Crew, multiple SA, Optimization optional, Inventory staging.

## Scheduling Rules

Crew capacity across days; staged parts available Day1.

## Test Objectives

Crew scheduled all days; inventory staged.

## Backend Validation

Crew members AssignedResource; ProductRequest fulfilled.

## Expected Results

No missing day; parts available.

## Negative Scenarios

Optimization moves Day3 over capacity.

## Recommended SOQL

```sql
SELECT ServiceResourceId FROM AssignedResource WHERE ServiceAppointmentId IN :saIds
```

## QA Recommendations

Optimization qualitative only—no invented scores.
