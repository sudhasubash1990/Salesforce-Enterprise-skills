---
title: Integration Patterns
module: Salesforce Business Analyst
category: Knowledge
document_type: Knowledge Article
version: 0.3.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
difficulty: intermediate
industry: all
related_brain_modules: [salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/output-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/delivery/architecture.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [integration patterns]
tags: [integration, api, middleware, events]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Integration Patterns

## Overview

Enterprise integration patterns for Salesforce BA requirements—not prescriptive technical design.

## Purpose

Describe integration needs with SLAs, volumes, and error behaviour for architect implementation.

## Why It Matters

Vague "integrate with ERP" requirements cause production failures and data corruption.

## Business Context

Integrations synchronize master data, transactions, and events across systems of record.

## Salesforce Context

Patterns: REST/SOAP APIs, Platform Events, Change Data Capture, batch, middleware (MuleSoft), ETL for migration vs sync.

## Core Concepts

| Pattern | Use when | BA specifies |
|---------|----------|--------------|
| Request/response | Real-time query/update | Entity, direction, SLA, error handling |
| Event-driven | Loose coupling, notifications | Event name, payload fields, subscribers |
| Batch | Large volume, scheduled windows | Volume, frequency, reconciliation |
| Pub/sub | Multiple consumers | Topic, durability, retry |
| File-based | Legacy batch feeds | Format, schedule, validation |

**Requirement pattern:** When [event] in [system], Salesforce must [action] within [SLA].

See [../../shared/reusable-components.md](../../shared/reusable-components.md#integration-pattern).

## Key Terminology

| Term | Definition |
|------|------------|
| System of record | Authoritative source per entity |
| Idempotency | Safe retry without duplicate effect |

## Frameworks and Models

INT-xxx rows in [../templates/frd-template.md](../templates/frd-template.md).

## Enterprise Best Practices

- Define system of record per entity
- Error handling and monitoring in requirements
- Reconciliation reports for batch
- Volume and peak load documented

## Common Mistakes

- Point-to-point without error strategy
- Real-time assumed when batch sufficient

## Anti-Patterns

- Integration scope without API availability dependency

## Decision Guidelines

BA documents need; architect selects pattern. Escalate high-volume or sub-second sync.

## Real-World Examples

ERP publishes Account upsert nightly batch; Case status webhook to dealer portal in near-real-time.

## Industry Considerations

Banking: payment integrations need idempotency and audit in requirements.

## AI Guidance

Do not design Apex or MuleSoft flows—document behaviour and NFRs.

## Review Checklist

- [ ] Direction and entity clear
- [ ] SLA or volume stated
- [ ] Error handling required
- [ ] Dependency on external API logged

## Related Brain Modules

- [Reasoning Framework](../brain/reasoning-framework.md)
- [Output Framework](../brain/output-framework.md)

## Related Knowledge

- [Readme](README.md)

## Related Templates

- [Readme](../templates/README.md)

## Related Playbooks

- [Readme](../playbooks/README.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [Architecture](../interview-guide/delivery/architecture.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md

## Navigation

- **Previous:** [Industry Patterns](industry-patterns.md)
- **Next:** [Kano Model](kano-model.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
