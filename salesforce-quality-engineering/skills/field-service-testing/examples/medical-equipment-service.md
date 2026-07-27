---
title: Medical Equipment Service
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

# Medical Equipment Service

## Business Scenario

Healthcare biomedical device PM with regulated access.

## FSL Components

WO, SA, Restricted sharing, Technician perm set, Service Report.

## Scheduling Rules

Only certified tech; PHI fields hidden.

## Test Objectives

PTA for FLS/sharing; certified skill enforced.

## Backend Validation

Skill match; FLS on patient fields.

## Expected Results

Unauthorized tech cannot see PHI.

## Negative Scenarios

Dispatcher assigns uncertified tech.

## Recommended SOQL

```sql
SELECT Id FROM ServiceResourceSkill WHERE Skill.DeveloperName = 'Biomed'
```

## QA Recommendations

Chain PTA; compliance advisory for PHI.
