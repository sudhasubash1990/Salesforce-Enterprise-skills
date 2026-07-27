---
title: Test — bulk-data-validation
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: Test Scenario
version: 0.20.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [test-data-generator]
---

# Test Scenario — bulk-data-validation

## Objective

External IDs, batch order, post-load SOQL

## Pass Criteria

- Business Scenario, Data Requirements, and Objects before payloads
- Synthetic-only; assumptions labeled
- SOQL stubs present when backend proof needed
- Cleanup present for bulk/LDV scenarios

## Fail Criteria

- Real PII or production data in sample packs
- Orphan children / ignored known VRs on positive data
- Invented volume/SLA metrics without labeled assumptions
- Missing cleanup for bulk generation
