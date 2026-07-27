---
title: Planned Maintenance Visit
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

# Planned Maintenance Visit

## Business Scenario

HVAC annual maintenance with entitlement SLA window.

## FSL Components

WO, SA, Entitlement, Operating Hours, Service Report.

## Scheduling Rules

Must complete within entitlement window; service report required.

## Test Objectives

SLA window respected; report generated on complete.

## Backend Validation

SA Completed; ServiceReport exists.

## Expected Results

Within window; report attached.

## Negative Scenarios

Complete outside window without override.

## Recommended SOQL

```sql
SELECT Id FROM ServiceReport WHERE ParentId = :saId
```

## QA Recommendations

Do not invent SLA hours—use program entitlement.
