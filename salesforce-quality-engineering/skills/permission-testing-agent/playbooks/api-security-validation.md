---
title: API Security Validation Playbook
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

# API Security Validation Playbook

## Objective

Validate integration and API user permissions.

**Pointer:** [../soql-validation-assistant/SKILL.md](../../soql-validation-assistant/SKILL.md)

## Inputs

- Integration user identity
- Connected apps
- Named credentials

## Validation Workflow

- CRUD/FLS for API user.
- Compare API response to UI.
- OAuth scope review.

## Decision Points

- Bulk API in scope?
- Modify All on integration user?

## Deliverables

- API Security Validation section

## Expected Results

- API least privilege
- No excessive scope

## Escalation Rules

- Scope expansion → Integration Architect
