---
title: Backend Validation Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.16.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [soql-validation, playbook]
---

# Backend Validation Playbook

## Objective

Verify server-side state without relying on UI alone.

## Inputs

- Automation or Flow under test
- Record IDs or correlation keys

## Validation Workflow

- Identify persisted fields and related records.
- Build selective SOQL.
- Assess security and performance.
- Compare to expected backend state.

## Decision Points

- API vs UI channel?
- Bulk vs single record?

## Deliverables

- SOQL Validation Report
- Query Review Template

## Expected Results

- Field values match business rule
- Related records created/updated correctly

## Escalation Rules

- Governor risk in prod → Performance review

## Related Documents

- [SKILL.md](../SKILL.md)
