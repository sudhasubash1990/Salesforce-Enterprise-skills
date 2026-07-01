---
title: Taxonomy
module: Salesforce Business Analyst
category: Shared
document_type: Reference
version: 1.1.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/consulting-principles.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [docs/metadata-schema.md, shared/traceability-model.md]
keywords: [taxonomy]
tags: [taxonomy]
---

# Taxonomy

Classification system for content and requirements in Salesforce Enterprise Skills.

## Content Taxonomy

```
Repository
├── Governance (docs/, .cursor/)
├── Shared Reference (shared/)
├── Skills (salesforce-business-analyst/, future skills)
│   ├── Entry (skill.md)
│   ├── Knowledge (domain reference)
│   ├── Playbooks (procedures)
│   ├── Templates (artifacts)
│   ├── Scenarios (context)
│   └── Examples (worked samples)
└── Examples (cross-skill samples)
```

## Requirement Taxonomy

| Level | Type | Granularity |
|-------|------|-------------|
| L0 | Business outcome | Strategic goal |
| L1 | Business requirement (BR) | Capability need |
| L2 | Functional requirement (FR) | System behavior |
| L3 | User story (US) | Deliverable increment |
| L4 | Acceptance criteria | Testable condition |
| L5 | Test scenario (TS) | UAT execution step |

## Salesforce Cloud Taxonomy

| Cloud | Primary Objects / Capabilities |
|-------|-------------------------------|
| Sales Cloud | Lead, Account, Contact, Opportunity, Forecasting |
| Service Cloud | Case, Knowledge, Omni-Channel, Entitlements |
| Marketing Cloud | Journeys, Email, Data Extensions (engagement model) |
| Commerce Cloud | B2B/B2C storefront, catalogs, orders |
| Experience Cloud | Portals, communities, external users |
| Revenue Cloud | CPQ, Billing, Subscription management |
| Data Cloud | Identity resolution, segments, activation |
| Platform | Custom objects, Flow, Apex, LWC, integration |

## Industry Taxonomy

| Sector | Sub-sectors in Repository |
|--------|---------------------------|
| Financial Services | Banking, Insurance, Wealth |
| Healthcare & Life Sciences | Provider, Payer, Pharma |
| Manufacturing | Discrete, process, aftermarket |
| Public Sector | Federal, state/local, education |

## Fit-Gap Taxonomy

See `.cursor/rules.md` — Standard, Config, Extend, Gap, Defer.

## Priority Taxonomy (MoSCoW)

| Priority | Meaning |
|----------|---------|
| Must | Release blocker |
| Should | Important; workaround exists |
| Could | Desirable if capacity |
| Won't | Explicitly out of this release |

## Related Brain Modules

- [Consulting Principles](../salesforce-business-analyst/brain/consulting-principles.md)

## Related Knowledge

- [Readme](../salesforce-business-analyst/knowledge/README.md)

## Related Templates

- [Readme](../salesforce-business-analyst/templates/README.md)

## Related Playbooks

- [Readme](../salesforce-business-analyst/playbooks/README.md)

## Related Industry Scenarios

- [Readme](../salesforce-business-analyst/scenarios/README.md)

## Related Interview Topics

- [Interview Index](../salesforce-business-analyst/interview-guide/interview-index.md)

## Related Examples

- [Readme](../examples/sample-project/README.md)

## Related Documents

- [Metadata Schema](../docs/metadata-schema.md)
- [Traceability Model](traceability-model.md)

## Traceability

**Upstream:** Governance | **Downstream:** All modules | **Validation:** glossary consistency

## Navigation

- **Previous:** [Salesforce Capability Map](salesforce-capability-map.md)
- **Next:** [Traceability Model](traceability-model.md)
- **See Also:** [cross-linking-framework](../docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
