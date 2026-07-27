---
title: FLS Validation Playbook
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

# FLS Validation Playbook

## Objective

Validate field read/edit/hidden per persona.

## Inputs

- Sensitive field list
- Layouts/Dynamic Forms
- Personas

## Validation Workflow

- Map FLS per field.
- UI verify hidden/read-only.
- API field-level check via SOVA.

## Decision Points

- Encrypted fields?
- Formula fields read-only?

## Deliverables

- FLS Validation Matrix

## Expected Results

- Sensitive fields protected
- No leakage via related lists

## Escalation Rules

- Sensitive exposure → Compliance advisory
