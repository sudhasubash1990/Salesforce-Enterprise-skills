---
title: Emergency Utility Outage
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

# Emergency Utility Outage

## Business Scenario

Storm outage requires emergency SA insert ahead of planned work.

## FSL Components

WO, SA, Emergency Work Type, Territory, Scheduling Policy, Dispatcher Console.

## Scheduling Rules

Emergency priority overrides planned; same resource cannot double-book.

## Test Objectives

Prove emergency SA scheduled; planned SA rescheduled or flagged.

## Backend Validation

Assigned Resource set; Status transitions valid.

## Expected Results

Emergency SA assigned; no overlapping SA for resource.

## Negative Scenarios

Assign emergency to resource already In Progress without rule.

## Recommended SOQL

```sql
SELECT Id, Status, SchedStartTime, SchedEndTime FROM ServiceAppointment WHERE WorkType.Name = 'Emergency' LIMIT 20
```

## QA Recommendations

Chain PTA for dispatcher; SOVA for overlap detection.
