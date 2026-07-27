---
title: Bulk Data Generation Playbook
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

# Bulk Data Generation Playbook

## Objective

Produce bulk-ready structures with External IDs and load order.

## Inputs

- Volume
- Objects
- External IDs
- Format

## Validation Workflow

- Design External ID scheme.
- Order CSVs parents→children.
- Batch/error strategy.
- Post-load SOQL + cleanup.

## Decision Points

- Upsert vs insert?

## Deliverables

- Bulk CSV/JSON pack
- Cleanup Strategy

## Expected Results

- Load order correct
- SOQL stubs present

## Escalation Rules

- Bulk without cleanup → Fail gate
