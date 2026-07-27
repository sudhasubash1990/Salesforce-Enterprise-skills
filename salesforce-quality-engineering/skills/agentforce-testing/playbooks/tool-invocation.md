---
title: Tool Invocation Playbook
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

# Tool Invocation Playbook

## Objective

Validate correct tool selection and execution.

**Pointer:** [../../metadata-impact-analyzer/SKILL.md](../../metadata-impact-analyzer/SKILL.md)

## Inputs

- Action inventory
- Input schemas
- Failure modes

## Validation Workflow

- Test correct tool for intent.
- Test wrong-tool avoidance.
- Validate Flow/Apex/API outcomes.
- Chain MIA/SOVA/PTA as needed.

## Decision Points

- Does action mutate data?

## Expected Results

- Correct tool invoked
- Faults communicated without hallucination

## Deliverables

- Tool Invocation Validation section

## Escalation Rules

- Unexpected DML → MIA + Release Manager
