---
title: Lead Qualification Agent
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.18.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [agentforce-testing, example]
---

# Lead Qualification Agent

## Business Scenario

Marketing agent scores inbound chat leads.

## Agent Configuration

Topics: Qualify. Actions: CreateLead. Prompt: required fields list.

## Sample Conversation

User: Interested in product X.
Agent: captures fields…

## Expected Response

Creates Lead only with required fields; no duplicate spam.

## Grounding Validation

Lead create via action evidence.

## Guardrail Validation

No auto-email spam without consent flag.

## Negative Tests

Inject script into name field.

## Edge Cases

Duplicate email leads.

## QA Recommendations

SOVA duplicate detection; MIA for Lead validation rules.
