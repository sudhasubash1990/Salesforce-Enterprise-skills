---
title: Regression Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.22.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [omnistudio-qa, playbook]
---

# Regression Testing

## Objective

Define OmniStudio regression scope after component or metadata change.

**Pointer:** knowledge/omnistudio-testing-best-practices.md

## Inputs

- MIA impact (if any)
- Changed components
- Dependent journeys

## Validation Workflow

- Start from MIA/component delta.
- Map consumers (reusable OS, shared DR/IP).
- Prioritize critical journeys.
- Link TDG seed packs and automation opportunities.

## Decision Points

- Reusable OS changed → expand consumer regression.

## Deliverables

- Regression Scope section
- Automation Opportunities

## Expected Results

- Critical journeys listed with residual risk

## Escalation Rules

- Unscoped high-risk shared IP → No-Go until owned
