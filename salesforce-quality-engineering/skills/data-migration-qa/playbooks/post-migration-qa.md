---
title: Post Migration QA Playbook
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

# Post Migration QA Playbook

## Objective

Validate post-load business correctness, regression, and automation opportunities.

**Pointer:** knowledge/common-migration-pitfalls.md

## Inputs

- Reconcile results
- Critical journeys
- Personas

## Validation Workflow

- Re-run sample journeys (PWR design if UI).
- Validate persona visibility (PTA).
- Expand SOVA for lingering exceptions.
- Update Regression Scope and Automation Opportunities.

## Decision Points

- Journey fail after count pass → expand Regression Scope.

## Deliverables

- Regression Scope + Automation Opportunities + Risks

## Expected Results

- Post-migrate business outcomes verified or residual risk listed

## Escalation Rules

- Systemic post-migrate failure → Release Manager
