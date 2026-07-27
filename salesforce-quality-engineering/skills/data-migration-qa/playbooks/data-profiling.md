---
title: Data Profiling Playbook
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

# Data Profiling Playbook

## Objective

Profile source data quality before mapping and load.

**Pointer:** knowledge/data-quality-framework.md

## Inputs

- Source extracts (sanitized)
- Volume estimates
- PII classification

## Validation Workflow

- Confirm Migration Scope.
- Profile nulls, formats, duplicates, orphans.
- Document DQ risks and cleansing candidates.
- Recommend TDG/masking for dry-run if PII present.

## Decision Points

- Production PII in samples → escalate Security; use masked data.

## Deliverables

- Source System Assessment + Data Quality Assessment sections

## Expected Results

- Profiling findings with owners
- Assumptions labeled

## Escalation Rules

- Critical PII exposure → Security / Data Governance
