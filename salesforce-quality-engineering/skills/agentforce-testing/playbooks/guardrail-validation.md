---
title: Guardrail Validation Playbook
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

# Guardrail Validation Playbook

## Objective

Validate safety and policy guardrails.

**Pointer:** [../permission-testing-agent/SKILL.md](../../permission-testing-agent/SKILL.md)

## Inputs

- Disallowed topics
- PII classes
- Jailbreak samples

## Validation Workflow

- Attempt policy bypass.
- Request sensitive data.
- Verify refusal and escalation.

## Decision Points

- Guest/community channel in scope?

## Expected Results

- Guardrails enforce refusals
- No PII leakage

## Deliverables

- Guardrail Assessment Report

## Escalation Rules

- Bypass → Security Architect
