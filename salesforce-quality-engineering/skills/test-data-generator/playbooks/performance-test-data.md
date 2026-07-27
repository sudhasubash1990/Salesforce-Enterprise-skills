---
title: Performance Test Data Playbook
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

# Performance Test Data Playbook

## Objective

Design volume strategy for performance/load datasets.

**Pointer:** [../../knowledge/data/large-data-volumes.md]

## Inputs

- Target volume (assumption)
- Objects
- Concurrency goals

## Validation Workflow

- Classify LDV needs.
- Recommend Bulk API path.
- Label assumptions — no invented timings.
- Plan staged load and cleanup.

## Decision Points

- Capacity evidence available?

## Deliverables

- Performance Data Plan

## Expected Results

- Volume strategy stated
- Cleanup owner named

## Escalation Rules

- LDV without evidence → Performance Architect
