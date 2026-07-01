---
title: Salesforce Capability Map
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
keywords: [salesforce capability map]
tags: [salesforce-capability-map]
---

# Salesforce Capability Map

High-level map of Salesforce capabilities for BA fit-gap and scoping discussions.

## Sales Cloud

| Capability | Standard Features | Common Extensions |
|------------|-------------------|-------------------|
| Lead management | Lead object, assignment rules, conversion | Custom lead scoring, external enrichment |
| Account & contact | Person accounts, hierarchies, duplicate rules | MDM integration |
| Opportunity management | Stages, products, forecasts | CPQ, complex pricing |
| Quoting | Native quotes | Salesforce CPQ / Revenue Cloud |
| Activity management | Tasks, events, Activity timeline | Einstein Activity Capture |
| Mobile sales | Salesforce Mobile | Offline considerations |

## Service Cloud

| Capability | Standard Features | Common Extensions |
|------------|-------------------|-------------------|
| Case management | Case, queues, assignment, escalation | Custom case types, swarming |
| Knowledge | Knowledge articles, data categories | External knowledge sync |
| Omni-Channel | Routing, presence, skills | Workforce management integration |
| Entitlements | Entitlements, milestones, SLAs | Complex SLA calendars |
| Self-service | Experience Cloud, deflection | Chatbot (Einstein Bot) |
| Field service | FSL (add-on) | Scheduling optimization |

## Platform

| Capability | Standard Features | Common Extensions |
|------------|-------------------|-------------------|
| Automation | Flow, approval processes | Apex triggers (last resort) |
| UI | Lightning pages, dynamic forms | LWC custom components |
| Security | Profiles, permission sets, sharing | Shield, event monitoring |
| Integration | REST/SOAP API, Platform Events, MuleSoft | ETL, iPaaS |
| Reporting | Reports, dashboards, CRM Analytics | Data Cloud activation |
| Data model | Custom objects, relationships, record types | Big objects, external objects |

## Experience Cloud

| Capability | Standard Features | Common Extensions |
|------------|-------------------|-------------------|
| Partner portal | Partner Community licenses | PRM workflows |
| Customer portal | Customer Community | Order status, case deflection |
| Authentication | SSO, social login | CIAM solutions |

## Revenue Cloud (when licensed)

| Capability | Standard Features | Common Extensions |
|------------|-------------------|-------------------|
| Configure price quote | CPQ quotes, products, bundles | Complex constraints |
| Billing | Invoicing, payment terms | ERP integration |
| Subscription | Assets, renewals, amendments | Usage-based rating |

## Data Cloud (when licensed)

| Capability | Standard Features | Common Extensions |
|------------|-------------------|-------------------|
| Identity resolution | Unified profiles | Cross-cloud identity |
| Segmentation | Segments, activation | Marketing activation |
| Ingestion | Connectors, streams | Zero-copy patterns |

## BA Usage Guide

1. Start fit-gap at **Standard** column
2. Move to **Extensions** only with documented gap
3. Flag licensing implications (FSL, CPQ, Data Cloud, Shield)
4. Link requirements to capability row in fit-gap matrix

## Cross-Cutting Concerns

Always map requirements to:

- Sharing and visibility
- Audit and field history
- Localization (multi-currency, language)
- Sandbox strategy for validation
- Governor limit sensitivity (bulk, integration volume)

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

- **Previous:** [Reusable Components](reusable-components.md)
- **Next:** [Taxonomy](taxonomy.md)
- **See Also:** [cross-linking-framework](../docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
