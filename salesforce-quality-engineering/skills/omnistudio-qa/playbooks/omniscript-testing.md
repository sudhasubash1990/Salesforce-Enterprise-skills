---
title: OmniScript Testing
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

# OmniScript Testing

## Objective

Validate OmniScript journeys end-to-end including Data JSON and submit.

**Pointer:** knowledge/omniscript-design.md

## Inputs

- Business scenario
- OmniScript name/version
- Expected Data JSON samples
- Personas

## Validation Workflow

- Confirm Business Scenario and component inventory.
- Walk steps, conditionals, required fields.
- Validate Save for Later / resume if in scope.
- Capture Data JSON at key steps; validate submit/IP handoff.
- Document negatives and edge cases.

## Decision Points

- Missing JSON samples → request TDG seed or label TBC.
- UI automation needed → chain PWR.

## Deliverables

- 17-section report sections 1–7, 11–12 populated
- SOVA stubs for CRM outcomes

## Expected Results

- Happy path + negatives documented
- No invented latency claims

## Escalation Rules

- Broken submit / data corruption → Critical escalate
