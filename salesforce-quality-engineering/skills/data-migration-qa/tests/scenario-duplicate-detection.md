---
title: Duplicate Detection
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

# Duplicate Detection

## Purpose

Detect duplicate External IDs and business keys.

## Preconditions

- External ID fields
- Matching policy

## Steps

1. Query duplicate External IDs
2. Apply business duplicate policy
3. Document exceptions

## Assertions

- Duplicates owned or blocked
- Policy documented

## Capability Chains

- SOVA
- TDG duplicate fixtures

## Notes

- Document Migration Scope and Source/Target Assessment before expanding detailed cases.
- Do not invent throughput, duration, or SLA percentages.
