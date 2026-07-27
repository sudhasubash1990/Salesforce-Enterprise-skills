---
title: Regression Security Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.17.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [permission-testing, playbook]
---

# Regression Security Playbook

## Objective

Security regression scope from metadata or release changes.

**Pointer:** [../../playbooks/regression-planning.md](../../playbooks/regression-planning.md)

## Inputs

- Changed security metadata
- Persona inventory

## Validation Workflow

- Map change to impacted personas/objects.
- In/Out/Conditional security tests.
- Link SOVA for backend proofs.

## Decision Points

- Can any persona be Out of scope?

## Deliverables

- Regression Scope section
- Security Test Checklist

## Expected Results

- High-risk personas covered
- Negative paths included

## Escalation Rules

- Scope dispute → Test Lead + Security Architect
