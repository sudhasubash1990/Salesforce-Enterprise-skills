---
title: Salesforce Platform
module: Salesforce Business Analyst
category: Knowledge
document_type: Knowledge Article
version: 1.1.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/output-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/salesforce/crm.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [salesforce platform]
tags: [salesforce-platform]
---

# Salesforce Platform — BA Reference

> **Sprint 2 hub:** See [salesforce-clouds-overview.md](salesforce-clouds-overview.md), [security-model.md](security-model.md), [integration-patterns.md](integration-patterns.md). Full index: [README.md](README.md).

Platform knowledge every senior Salesforce BA internalizes.

## Object Model Essentials

| Pattern | Use When |
|---------|----------|
| Standard objects | Process fits Salesforce CRM semantics |
| Custom objects | Net-new entity with lifecycle in Salesforce |
| External objects | OData/SOAP read-only external data |
| Big objects | Archive-scale history (compliance) |
| Platform events | Event-driven integration |

**Rule:** If it looks like Account, Contact, Case, Opportunity, Lead, or Product—justify why standard object won't work before custom.

## Automation Hierarchy

Prefer in order:

1. **Validation rules** — Prevent bad data at entry
2. **Record-triggered Flow** — After/before save logic
3. **Screen Flow** — Guided user processes
4. **Approval processes** — Formal approvals
5. **Apex** — Complex logic, bulk, integration callouts

Retire Process Builder references in new designs—migrate to Flow.

## Security Model (BA Questions)

| Layer | BA Must Ask |
|-------|-------------|
| OWD | Public vs private? Partner access? |
| Role hierarchy | Does reporting structure drive access? |
| Sharing rules | Exceptions to OWD? |
| Permission sets | Which functions need which objects/fields? |
| FLS | Sensitive fields (PII, financial)? |
| Experience Cloud | Guest vs authenticated external users |

## Multi-Org Patterns

| Pattern | When |
|---------|------|
| Single org | Unified process, shared customers |
| Hub-and-spoke | Divisional autonomy with central reporting |
| Multi-org + integration | Regulatory separation, M&A |

Document which org owns which entity as system of record.

## Integration Touchpoints

- REST/SOAP for synchronous
- Platform Events / Change Data Capture for async
- MuleSoft / iPaaS for orchestration
- ETL for bulk migration

BA specifies: trigger event, direction, frequency, error handling, reconciliation.

## Governor Limits (BA Awareness)

Not for coding—but shape requirements:

- Bulk API for large loads
- Avoid real-time sync for high-volume feeds
- Batch windows for heavy processing

## Release Awareness

Note Salesforce seasonal releases may unlock standard features—check before classifying as Gap.

Reference: [shared/salesforce-capability-map.md](../../shared/salesforce-capability-map.md)

## Licensing Implications BA Should Flag

| Need | License / Add-on |
|------|------------------|
| Partner portal | Experience Cloud |
| Field technicians | FSL |
| Complex quoting | CPQ / Revenue Cloud |
| Advanced encryption | Shield |
| Identity for customers | CIAM patterns |

Always mark licensing as "confirm with account team."

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

- [Crm](../interview-guide/salesforce/crm.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md

## Navigation

- **Previous:** [Salesforce Clouds Overview](salesforce-clouds-overview.md)
- **Next:** [Security Model](security-model.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
