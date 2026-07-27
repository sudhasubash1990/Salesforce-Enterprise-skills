---
title: Test — offline-synchronization
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: Test Scenario
version: 0.19.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [field-service-testing]
---

# Test Scenario — offline-synchronization

## Objective

Offline Validation with conflict path

## Pass Criteria

- Business Scenario and FSL Components Reviewed before detailed cases
- Assumptions labeled; no invented optimization/SLA %
- SOQL stubs present when backend proof needed

## Fail Criteria

- Work Order CRUD-only pack without scheduling/mobile/inventory when in scope
- Invented metrics
- Missing negative scheduling or offline conflict when claimed in scope
