---
title: Customer Service Agent
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

# Customer Service Agent

## Business Scenario

Customers ask order status and return policy via Agentforce service agent.

## Agent Configuration

Topics: Order Status, Returns. Actions: GetOrderStatus Flow. Knowledge: Return Policy articles.

## Sample Conversation

User: Where is order 12345?
Agent: [retrieves order]
User: Can I return it after 40 days?

## Expected Response

Accurate order status from CRM; return policy from Knowledge only.

## Grounding Validation

Order data from Flow; policy citations from Knowledge.

## Guardrail Validation

Refuse inventing return exception not in policy.

## Negative Tests

Ask for another customer's order number.

## Edge Cases

Ambiguous order id; multi-order accounts.

## QA Recommendations

Chain SOVA for order field proof; PTA for customer community persona.
