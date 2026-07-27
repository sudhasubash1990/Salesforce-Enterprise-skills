---
title: Regression Testing Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.19.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [field-service-testing, playbook]
---

# Regression Testing Playbook

## Objective

Select risk-based FSL regression after config/metadata change.

**Pointer:** ../../playbooks/regression-planning.md

## Inputs

- Change list
- Prior packs
- MIA deltas

## Validation Workflow

- Map change to In/Out/Conditional.
- Re-run scheduling + offline smoke.
- Update regression checklist.

## Decision Points

- Can any territory be Out?

## Deliverables

- Regression Checklist
- Regression Scope

## Expected Results

- High-risk journeys revalidated

## Escalation Rules

- Scope dispute → Test Lead + FSL Architect
