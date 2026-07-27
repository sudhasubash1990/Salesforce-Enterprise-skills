---
title: Topic Validation Playbook
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

# Topic Validation Playbook

## Objective

Validate topic classification and routing.

## Inputs

- Topic list
- Sample utterances
- Out-of-scope intents

## Validation Workflow

- Build utterance matrix per topic.
- Test ambiguous and multi-intent utterances.
- Verify clarification/escalation.

## Decision Points

- Is topic taxonomy complete?

## Expected Results

- In-topic correctly routed
- Out-of-topic refused or clarified

## Deliverables

- Topic Classification Validation section

## Escalation Rules

- Systematic misrouting → Agentforce Architect
