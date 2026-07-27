---
title: Grounding Validation Playbook
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

# Grounding Validation Playbook

## Objective

Prove answers are grounded in approved sources.

## Inputs

- Knowledge corpus
- CRM data scope
- Retrieval config

## Validation Workflow

- Design hit/miss retrieval tests.
- Compare claims to sources.
- Document Grounding Assessment.

## Decision Points

- Source of truth identified?

## Expected Results

- No ungrounded policy claims
- Miss path refuses or escalates

## Deliverables

- Knowledge Grounding Assessment

## Escalation Rules

- Regulated hallucination → Compliance advisory
