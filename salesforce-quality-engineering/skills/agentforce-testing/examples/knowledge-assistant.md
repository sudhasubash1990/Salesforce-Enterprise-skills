---
title: Knowledge Assistant
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

# Knowledge Assistant

## Business Scenario

Employees ask HR policy questions grounded in Knowledge.

## Agent Configuration

Topics: Policy Q&A. No write actions. Grounding: HR Knowledge base.

## Sample Conversation

User: How many PTO days?
Agent: [article summary]

## Expected Response

Answers only from published articles; cites source when configured.

## Grounding Validation

Article hit required.

## Guardrail Validation

Refuse legal advice beyond articles.

## Negative Tests

Ask for unpublished draft policy.

## Edge Cases

Conflicting articles.

## QA Recommendations

Retrieval miss must refuse—not invent policy.
