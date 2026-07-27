---
title: Work Order Testing Playbook
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

# Work Order Testing Playbook

## Objective

Validate WO/WOLI lifecycle from create through close.

**Pointer:** [../../metadata-impact-analyzer/SKILL.md](../../metadata-impact-analyzer/SKILL.md)

## Inputs

- WO types
- Status model
- Linked SA and inventory

## Validation Workflow

- Map status transitions.
- Execute happy path and skip-status negatives.
- Verify child SA and consumption.
- Capture SOQL stubs.

## Decision Points

- Maintenance-generated WO in scope?

## Deliverables

- Work Order Test Report

## Expected Results

- Status transitions enforced
- Child SA linked

## Escalation Rules

- Automation conflict → MIA
