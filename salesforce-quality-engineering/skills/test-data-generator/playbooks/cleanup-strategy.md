---
title: Cleanup Strategy Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.20.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [test-data-generator, playbook]
---

# Cleanup Strategy Playbook

## Objective

Define safe deletion/archive of generated seed data.

**Pointer:** [../soql-validation-assistant/SKILL.md](../../soql-validation-assistant/SKILL.md)

## Inputs

- External ID prefix
- Objects
- Environment

## Validation Workflow

- Identify deletable seed via External ID / naming.
- Order deletes children→parents.
- Verify with SOQL counts.
- Document exceptions (shared reference data).

## Decision Points

- Shared Pricebook entries must remain?

## Deliverables

- Data Cleanup Checklist

## Expected Results

- Seed removable
- Shared refs protected

## Escalation Rules

- Ambiguous delete scope → Release Manager
