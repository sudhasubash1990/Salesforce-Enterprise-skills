---
title: Data Masking Playbook
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

# Data Masking Playbook

## Objective

Plan masking when synthetic-only is not feasible.

**Pointer:** [../../knowledge/data/data-masking.md]

## Inputs

- Sensitive field list
- Clone type
- Integrity requirements

## Validation Workflow

- Classify PII fields.
- Choose mask vs regenerate.
- Verify relationships post-mask.
- Document residual risk.

## Decision Points

- Any field must remain real for integration?

## Deliverables

- Data Masking Checklist

## Expected Results

- PII fields addressed
- Integrity verified

## Escalation Rules

- Unmasked PII in shared sandbox → Security
