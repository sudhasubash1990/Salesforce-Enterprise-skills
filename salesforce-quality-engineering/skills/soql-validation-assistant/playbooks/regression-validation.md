---
title: Regression Validation Playbook
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

# Regression Validation Playbook

## Objective

SOQL smoke pack for regression scope from impact or release.

## Inputs

- Regression scope list
- Changed metadata
- Environment

## Validation Workflow

- Map components to validation queries.
- Prioritize High risk objects.
- Produce regression validation report.

## Decision Points

- In vs Conditional scope?
- [../../playbooks/regression-planning.md](../../playbooks/regression-planning.md)

## Deliverables

- Regression Validation Report

## Expected Results

- Smoke queries pass in target sandbox
- No unexpected nulls or orphans

## Escalation Rules

- Failure → Test Lead + dev owner

## Related Documents

- [SKILL.md](../SKILL.md)
