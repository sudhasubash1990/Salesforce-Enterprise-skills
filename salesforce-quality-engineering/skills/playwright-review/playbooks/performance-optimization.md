---
title: Performance Optimization Playbook
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

# Performance Optimization Playbook

## Objective

Reduce slow Playwright Salesforce suites without inventing timings.

## Inputs

- Suite duration signals
- Login pattern
- Parallel config

## Validation Workflow

- Find sleep and serial bottlenecks.
- Recommend storageState and API setup.
- Label duration assumptions.
- Update Performance Analysis.

## Decision Points

- Measured timings available?

## Deliverables

- Performance Review Report

## Expected Results

- Bottlenecks listed
- No invented SLAs

## Escalation Rules

- LDV UI suite without isolation → Performance note
