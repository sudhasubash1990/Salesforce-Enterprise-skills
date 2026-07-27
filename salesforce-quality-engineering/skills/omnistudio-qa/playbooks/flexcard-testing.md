---
title: FlexCard Testing
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

# FlexCard Testing

## Objective

Validate FlexCard render, actions, binding, and child cards.

**Pointer:** knowledge/flexcard-architecture.md

## Inputs

- Card inventory
- Data sources
- Action targets
- Personas

## Validation Workflow

- Inventory cards and data sources.
- Validate render and conditional visibility.
- Exercise actions (OS/IP/nav).
- Check refresh/pagination; note perf risks.
- Chain PTA if restricted fields visible.

## Decision Points

- Wrong action target → Fail Functional Validation.
- PII exposure → escalate PTA/Security.

## Deliverables

- FlexCard findings in Architecture/Functional/Security sections

## Expected Results

- Actions resolve to correct OS/IP versions

## Escalation Rules

- Experience PII leak → Security Architect
