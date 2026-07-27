---
title: Prompt Validation Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.18.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [agentforce-testing, playbook]
---

# Prompt Validation Playbook

## Objective

Validate prompt templates for clarity, safety, and adherence.

**Pointer:** [../../enterprise-quality/ai-governance/README.md](../../enterprise-quality/ai-governance/README.md)

## Inputs

- Prompt template text
- Variables and data bindings
- Disallowed topics

## Validation Workflow

- Review instructions vs user prompt.
- Check conflicts and missing constraints.
- Design adherence and jailbreak tests.
- Document Prompt Analysis section.

## Decision Points

- Prompt ready for release?
- Sensitive variables exposed?

## Expected Results

- Prompt adherence scenarios defined
- Safety constraints explicit

## Deliverables

- Prompt Review Report

## Escalation Rules

- Conflicting instructions → Prompt Engineer + SA
