---
title: AI Regression Playbook
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

# AI Regression Playbook

## Objective

Select risk-based Agentforce regression after prompt/topic/action change.

**Pointer:** ../../playbooks/regression-planning.md

## Inputs

- Change list
- Prior conversation packs
- MIA deltas

## Validation Workflow

- Map change to In/Out/Conditional AI scenarios.
- Re-run grounding and guardrail smoke.
- Update AI Regression Checklist.

## Decision Points

- Can any topic be Out of scope?

## Expected Results

- High-risk journeys revalidated
- Hallucination traps re-run

## Deliverables

- AI Regression Checklist
- Regression Scope

## Escalation Rules

- Scope dispute → Test Lead + Agentforce Architect
