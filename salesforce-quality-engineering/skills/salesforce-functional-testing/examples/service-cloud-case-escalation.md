---
title: Service Cloud Case Escalation — Example
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, service-cloud-case-escalation]
---

# Service Cloud Case Escalation

## Business Scenario

High-priority cases that remain unresolved beyond the SLA threshold must escalate automatically. Escalation rules trigger based on case age, priority, and status. Escalated cases notify the service manager and reassign to a senior queue.

## Cloud

Service Cloud

## Objects

Case, CaseHistory, Entitlement, Milestone, Queue, Task (notification)

## Test Scenarios

### Positive

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| CE-P01 | High-priority case unresolved after 4 business hours | Escalation rule fires, case reassigned to Senior Queue |
| CE-P02 | Escalation triggers email notification to Service Manager | Email delivered with case details |
| CE-P03 | Entitlement milestone reaches warning threshold | Milestone status changes to In Jeopardy |

### Negative

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| CE-N01 | Case resolved before escalation threshold | Escalation rule does not fire |
| CE-N02 | Low-priority case exceeds same time threshold | No escalation (rule criteria exclude Low priority) |
| CE-N03 | Case already escalated — second escalation attempt | No duplicate escalation action |

### Boundary

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| CE-B01 | Case reaches escalation threshold at exactly business-hours boundary | Escalation fires at next business-hours evaluation |
| CE-B02 | Multiple cases escalate simultaneously | All cases processed without queue lock or failure |

### Permission

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| CE-PM01 | Agent attempts manual escalation without permission | Escalation action blocked |

## Expected Results

Escalation timing, reassignment, and notification verified against SLA configuration.

## Chain Skills

- [PTA](../../permission-testing-agent/SKILL.md) — escalation action permissions
- [SOVA](../../soql-validation-assistant/SKILL.md) — verify CaseHistory and Milestone records

## Related Documents

- [Service Cloud Testing Knowledge](../knowledge/service-cloud-testing.md)
- [E2E Testing Knowledge](../knowledge/salesforce-e2e-testing.md)
