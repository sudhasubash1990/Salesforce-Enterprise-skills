---
title: Data Migration Validation Playbook
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

# Data Migration Validation Playbook

## Objective

Reconcile migrated data counts and key fields.

**Pointer:** [../../knowledge/data/data-migration-validation.md](../../knowledge/data/data-migration-validation.md)

## Inputs

- Migration mapping
- Source/target counts
- Key business fields

## Validation Workflow

- Define reconciliation metrics.
- Use aggregate SOQL on both sides (conceptually).
- Sample detail queries for exceptions.
- Document tolerances.

## Decision Points

- Full vs sample reconcile?
- Acceptable variance?

## Deliverables

- Data Verification Report
- Aggregate query pack

## Expected Results

- Counts within tolerance
- Exception queue empty or explained

## Escalation Rules

- Variance over threshold → Migration lead

## Related Documents

- [SKILL.md](../SKILL.md)
