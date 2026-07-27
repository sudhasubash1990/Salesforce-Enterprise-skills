---
title: Sales Agent
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

# Sales Agent

## Business Scenario

Inside sales uses agent to qualify inbound leads.

## Agent Configuration

Topics: Lead Qualify. Actions: UpdateLead Apex. Prompt requires BANT checklist.

## Sample Conversation

User: Qualify Acme lead.
Agent: asks budget/authority…
User: budget unknown.

## Expected Response

Does not mark MQL without required fields; asks follow-ups.

## Grounding Validation

Lead fields from CRM; no invented revenue.

## Guardrail Validation

No PII dump of unrelated leads.

## Negative Tests

Request to mark Closed Won without opportunity.

## Edge Cases

Partial BANT; conflicting answers.

## QA Recommendations

MIA if Apex Lead update changes validation rules.
