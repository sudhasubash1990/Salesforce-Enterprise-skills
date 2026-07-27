---
title: DataRaptor Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.22.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [omnistudio-qa, playbook]
---

# DataRaptor Testing

## Objective

Validate DataRaptor mapping, formulas, null handling, and CRM accuracy.

**Pointer:** knowledge/dataraptor-types.md

## Inputs

- DR type and name
- Input/output samples
- CRM expected outcomes

## Validation Workflow

- Classify Extract/Load/Transform/Turbo.
- Trace mappings and formulas.
- Test null/missing input paths.
- Produce SOVA stubs for Load/CRM writes.
- Note performance risks without inventing timings.

## Decision Points

- Critical Load without SOVA → incomplete Data Validation.

## Deliverables

- Data + JSON Validation sections
- SOVA query stubs

## Expected Results

- Mapping accuracy verified against fixtures

## Escalation Rules

- Silent overwrite of critical fields → Critical
