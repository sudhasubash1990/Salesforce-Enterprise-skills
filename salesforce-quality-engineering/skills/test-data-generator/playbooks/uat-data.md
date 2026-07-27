---
title: UAT Data Playbook
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

# UAT Data Playbook

## Objective

Prepare business-readable UAT seed with persona coverage.

## Inputs

- UAT scripts
- Business personas
- Environment

## Validation Workflow

- Align data to UAT scripts.
- Synthetic names clear to business.
- Ownership for each persona.
- Sign-off cleanup after UAT.

## Decision Points

- Business requires 'realistic' names — still synthetic?

## Deliverables

- UAT seed pack
- Cleanup Strategy

## Expected Results

- Scripts executable
- No production PII

## Escalation Rules

- PII pressure → Data Governance
