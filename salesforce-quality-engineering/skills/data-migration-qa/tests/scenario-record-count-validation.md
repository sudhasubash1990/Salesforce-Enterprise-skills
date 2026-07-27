---
title: Record Count Validation
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: Test Scenario
version: 0.23.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [data-migration-qa, test]
---

# Record Count Validation

## Purpose

Validate source vs target counts with tolerances.

## Preconditions

- Migration Scope documented
- Source totals available

## Steps

1. Capture source counts
2. Capture target counts via SOQL stubs
3. Compare to tolerance

## Assertions

- Variance explained or defect logged
- Scope preceded detailed cases

## Capability Chains

- SOVA for query packs

## Notes

- Document Migration Scope and Source/Target Assessment before expanding detailed cases.
- Do not invent throughput, duration, or SLA percentages.
