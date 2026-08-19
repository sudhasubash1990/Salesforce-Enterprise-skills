---
title: Service Cloud Functional Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Guide
document_type: Guide
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, service-cloud-testing]
---

# Service Cloud Functional Testing

## Purpose

Provide testing guidance for Service Cloud objects, features, and automation — Cases, Omni-Channel, Knowledge, Entitlements, SLAs, Email-to-Case, Web-to-Case, escalation, routing, and console.

## Business Context

Service Cloud is the backbone of customer support. Functional defects in case routing, escalation, or SLA tracking directly impact customer satisfaction and SLA compliance. Testing must cover the full case lifecycle including edge cases around assignment, ownership transfer, and entitlement verification.

## Assessment Criteria

- Case lifecycle tested from creation through closure across all channels
- Assignment and escalation rules verified with multiple criteria combinations
- Omni-Channel routing validated per skill, queue, and capacity
- Entitlement and milestone calculations verified against SLA definitions

## Key Areas

- **Case CRUD:** Create, read, update, close, reopen, merge, delete
- **Assignment Rules:** Criteria-based routing, round-robin, queue assignment
- **Escalation Rules:** Time-based escalation, criteria matching, action verification
- **Omni-Channel:** Skill-based routing, capacity, presence, queue priority
- **Email-to-Case:** Inbound parsing, threading, attachment handling, auto-response
- **Web-to-Case:** Form submission, field mapping, spam prevention, duplicate handling
- **Knowledge:** Article search, attach to case, article versioning, channel visibility
- **Entitlements & Milestones:** Entitlement lookup, milestone countdown, violation actions
- **Service Console:** Tab behavior, utility bar, macros, quick text, split view

## Decision Framework

| Scenario | Testing Focus |
|----------|---------------|
| New case channel (email, web, phone) | Channel-specific creation + assignment |
| SLA-critical process | Entitlement + milestone + escalation chain |
| Omni-Channel rollout | Routing, capacity, presence, fallback |
| Console customization | Layout, utility bar, macro execution |

## Best Practices

- Test assignment rules with overlapping criteria to verify precedence
- Validate escalation timing with business-hours vs. 24-hour clock
- Verify Omni-Channel fallback when all agents are at capacity
- Test Email-to-Case threading with reply chains and forwarded messages
- Chain [PTA](../../permission-testing-agent/SKILL.md) for case visibility per profile

## Anti-Patterns

- Testing only manual case creation — ignoring Email-to-Case and Web-to-Case
- Assuming escalation rules fire instantly — time-dependent testing required
- Skipping Omni-Channel capacity overflow scenarios

## Related Documents

- [Service Cloud Knowledge](../../../knowledge/clouds/service-cloud.md)
- [SKILL.md](../SKILL.md)
- [Permission Testing Agent](../../permission-testing-agent/SKILL.md)
