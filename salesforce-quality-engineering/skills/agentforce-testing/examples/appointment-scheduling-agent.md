---
title: Appointment Scheduling Agent
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

# Appointment Scheduling Agent

## Business Scenario

Customers schedule Field Service appointments.

## Agent Configuration

Topics: Schedule. Actions: BookAppointment Flow.

## Sample Conversation

User: Book Friday AM.
Agent: offers slots…
User: Confirm 10am.

## Expected Response

Books only available slots; confirms details.

## Grounding Validation

Slots from FSL/Flow data.

## Guardrail Validation

No booking for other accounts.

## Negative Tests

Book without authentication.

## Edge Cases

No slots available; timezone edge.

## QA Recommendations

PTA for Experience Cloud customer persona.
