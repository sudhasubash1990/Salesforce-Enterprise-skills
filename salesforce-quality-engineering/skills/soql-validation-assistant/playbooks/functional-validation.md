---
title: Functional Validation Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.16.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [soql-validation, playbook]
---

# Functional Validation Playbook

## Objective

Validate business outcomes via backend SOQL after functional actions.

**Pointer:** [../../playbooks/test-design-review.md](../../playbooks/test-design-review.md)

## Inputs

- User story / AC
- Object and persona
- Test data identifiers

## Validation Workflow

- Define validation objective per AC.
- Draft SOQL with run-as context.
- Document expected vs actual interpretation.
- Log negative validation.

## Decision Points

- Does UI-only proof suffice?
- Is backend SOQL necessary?

## Deliverables

- SOQL Validation Report
- Backend Validation Checklist

## Expected Results

- Query returns expected row set or count
- Negative path shows blocked or excluded records

## Escalation Rules

- Ambiguous AC → BA clarification
- Security mismatch → Security Architect

## Related Documents

- [SKILL.md](../SKILL.md)
