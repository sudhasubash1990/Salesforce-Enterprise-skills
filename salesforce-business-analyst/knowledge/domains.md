---
title: Domains
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
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [domains]
tags: [domains]
---

# Salesforce Domains — BA Lens

Domain-specific BA considerations beyond industry verticals.

## Sales Domain

**Key questions:**

- Lead conversion rules and duplicate handling?
- Opportunity stages aligned to forecast categories?
- Product hierarchy source of truth?
- Territory management model?

**Common gaps:** Quoting complexity exceeds native Quotes → CPQ evaluation.

## Service Domain

**Key questions:**

- Case record types by channel/product?
- Entitlements and SLA calendars?
- Omni-Channel routing (skills, priority)?
- Knowledge authoring workflow?

**Common gaps:** Legacy email-to-case rules undocumented.

## Marketing Alignment

Even without Marketing Cloud in scope:

- Lead source attribution requirements?
- Consent and opt-in capture?
- Handoff from marketing to sales?

## Commerce

B2B vs B2C commerce affects Experience Cloud and order models—clarify early.

## Revenue / Billing

Subscription vs one-time? Amendment workflows? ERP billing sync?

## Field Service

Work orders, scheduling, parts inventory—FSL licensing and mobile offline.

## Data & Analytics

| Need | Path |
|------|------|
| Operational reporting | Reports & dashboards |
| Executive analytics | CRM Analytics |
| Unified customer profile | Data Cloud |
| AI use cases | Einstein features—validate data readiness |

## BA Deliverable per Domain

For each domain in scope, BRD should include:

1. AS-IS / TO-BE process summary
2. Key objects and relationships (conceptual)
3. Integration points
4. Reporting KPIs
5. Role-based access summary

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

- [Interview Index](../interview-guide/interview-index.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md

## Navigation

- **Previous:** [Dependency Management](dependency-management.md)
- **Next:** [Epic Design](epic-design.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
