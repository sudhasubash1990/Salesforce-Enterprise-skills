---
title: Integration Validation Playbook
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

# Integration Validation Playbook

## Objective

Verify integration outcomes via SOQL on persisted records.

**Pointer:** [../../knowledge/integration/](../../knowledge/integration/README.md)

## Inputs

- Integration correlation ID
- External system payload
- Named credential context

## Validation Workflow

- Trace object/field updates from integration.
- Build queries on status/staging fields.
- Validate error records and retries.

## Decision Points

- Sync vs async?
- Idempotency key field?

## Deliverables

- SOQL Validation Report
- Integration exception queries

## Expected Results

- Staging cleared
- Status fields match middleware state

## Escalation Rules

- Persistent errors → Integration Architect

## Related Documents

- [SKILL.md](../SKILL.md)
