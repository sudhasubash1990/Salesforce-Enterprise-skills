---
title: Flaky Test Investigation Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.21.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [playwright-review, playbook]
---

# Flaky Test Investigation Playbook

## Objective

Investigate flake root causes before raising retries.

**Pointer:** [../../automation-intelligence/review-engine/flaky-and-stability-review.md]

## Inputs

- Failure history
- Traces
- Parallel settings

## Validation Workflow

- Cluster flake themes (sync, data, env).
- Reproduce with trace.
- Fix root cause; limit retries.
- Document Flaky Test Analysis.

## Decision Points

- Infra vs app flake?

## Deliverables

- Flaky Test Investigation Report

## Expected Results

- Root cause hypothesized with evidence
- No invented flake %

## Escalation Rules

- Release-blocking flake → Release Manager
