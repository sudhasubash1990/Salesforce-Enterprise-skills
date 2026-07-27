---
title: Dispatcher Console Testing Playbook
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

# Dispatcher Console Testing Playbook

## Objective

Validate dispatcher assign/reschedule console behavior.

**Pointer:** [../permission-testing-agent/SKILL.md](../../permission-testing-agent/SKILL.md)

## Inputs

- Dispatcher persona
- Gantt/list views
- Alerts

## Validation Workflow

- Assign/unassign/reschedule.
- Filter by territory.
- Negative: unqualified resource.

## Decision Points

- Multi-territory dispatcher?

## Deliverables

- Dispatcher Review Report

## Expected Results

- Assignments persist
- Unauthorized assign blocked

## Escalation Rules

- Access gap → PTA
