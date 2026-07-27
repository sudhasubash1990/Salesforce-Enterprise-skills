---
title: Case Resolution Agent
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

# Case Resolution Agent

## Business Scenario

Service agent proposes Case resolution steps and can update Case status via Flow.

## Agent Configuration

Topics: Troubleshoot, Close Case. Actions: UpdateCaseStatus Flow.

## Sample Conversation

User: Modem offline.
Agent: troubleshooting steps…
User: Resolved—close case.

## Expected Response

Status update only after confirmation; correct status value.

## Grounding Validation

Case fields from CRM; troubleshooting from Knowledge.

## Guardrail Validation

No close without confirmation.

## Negative Tests

Close someone else's Case.

## Edge Cases

Case already Closed; Flow fault.

## QA Recommendations

Chain MIA for Case status automation; SOVA for status proof.
