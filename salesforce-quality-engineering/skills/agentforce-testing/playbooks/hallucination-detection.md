---
title: Hallucination Detection Playbook
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

# Hallucination Detection Playbook

## Objective

Detect ungrounded or fabricated responses.

## Inputs

- Trap questions
- Source corpus
- Regulated topics

## Validation Workflow

- Ask questions with no source.
- Ask contradictory facts.
- Score Hallucination Risk.

## Decision Points

- Is refuse/escalate configured?

## Expected Results

- Ungrounded answers refused
- No fabricated IDs/amounts

## Deliverables

- Hallucination Review

## Escalation Rules

- Critical hallucination → block deploy
