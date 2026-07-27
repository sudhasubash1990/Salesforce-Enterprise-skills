---
title: FlexCard Rendering
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: Test Scenario
version: 0.22.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [omnistudio-qa, test]
---

# FlexCard Rendering

## Purpose

Validate FlexCard render, visibility, and actions.

## Preconditions

- FlexCard inventory
- Data source available (stub OK)

## Steps

1. Render card
2. Toggle conditional visibility
3. Invoke primary action

## Assertions

- Correct data binding
- Action target correct OS/IP

## Capability Chains

- PTA if restricted fields
- PWR for UI assert patterns

## Notes

- Inventory Business Scenario and OmniStudio Components before expanding detailed cases.
- Do not invent latency, throughput, or SLA percentages.
