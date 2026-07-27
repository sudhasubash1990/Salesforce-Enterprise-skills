---
title: Asset Inspection
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

# Asset Inspection

## Business Scenario

Public sector asset inspection with checklist and photos.

## FSL Components

WO, SA, Mobile photos, Service Report, Territory.

## Scheduling Rules

Photos required before Complete; territory match.

## Test Objectives

Cannot complete without photos; territory enforced.

## Backend Validation

ContentDocumentLink or photo custom objects per org.

## Expected Results

Complete blocked until media present.

## Negative Scenarios

Complete without photos via API.

## Recommended SOQL

```sql
SELECT Id FROM ContentDocumentLink WHERE LinkedEntityId = :saId
```

## QA Recommendations

API bypass negative required.
