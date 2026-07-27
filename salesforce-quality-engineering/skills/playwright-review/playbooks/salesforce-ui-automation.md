---
title: Salesforce UI Automation Playbook
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

# Salesforce UI Automation Playbook

## Objective

Review Salesforce-specific UI automation patterns.

**Pointer:** [../../automation-intelligence/playwright/salesforce-best-practices.md]

## Inputs

- LEX/Experience/Console scope
- Auth approach
- Sample flows

## Validation Workflow

- Assess sync helpers.
- Check console/related list handling.
- Chain AFT for Agentforce UI.
- Chain PTA for persona UI.

## Decision Points

- Agentforce in scope?

## Deliverables

- Salesforce Compatibility Review section

## Expected Results

- SF sync strategy present
- Persona coverage noted

## Escalation Rules

- No sync strategy → SF Automation Architect
