---
title: Data Reconciliation Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.23.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [data-migration-qa, playbook]
---

# Data Reconciliation Playbook

## Objective

Design and execute reconciliation strategy (counts, aggregates, samples).

**Pointer:** knowledge/reconciliation-techniques.md

## Inputs

- Source totals
- Target SOQL stubs
- Tolerances
- Financial keys if any

## Validation Workflow

- Define reconcile dimensions and tolerances.
- Produce count/aggregate/exception stubs for SOVA.
- Sample business journeys after counts.
- Document residual exceptions.

## Decision Points

- Financial mismatch beyond tolerance → No-Go / escalate.

## Deliverables

- Reconciliation Strategy + Recommended SOQL Validation

## Expected Results

- Tolerances and owners documented

## Escalation Rules

- Unresolved financial variance → Finance + Data Architect
