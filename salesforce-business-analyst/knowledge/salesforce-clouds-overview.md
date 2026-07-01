---
title: Salesforce Clouds Overview
module: Salesforce Business Analyst
category: Knowledge
document_type: Knowledge Article
version: 0.3.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
difficulty: foundational
industry: all
related_brain_modules: [salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/output-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/salesforce/crm.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [salesforce clouds overview]
tags: [salesforce, clouds, capabilities]
review-cycle: quarterly
salesforce-cloud: Sales Cloud, Service Cloud, Experience Cloud, Data Cloud, Platform
---

# Salesforce Clouds Overview

## Overview

Business capability overview of Salesforce clouds—outcomes, not product marketing.

## Purpose

Help BAs map business needs to the right cloud and flag licensing implications.

## Why It Matters

Wrong cloud scope drives cost, rework, and failed adoption.

## Business Context

Clouds align to customer-facing capabilities: sell, serve, engage, field work, industry depth, data activation.

## Salesforce Context

Programs often combine Sales + Service + Experience + Platform; Marketing and Data Cloud for engagement and unified profiles.

## Core Concepts

| Cloud | Business outcomes | Typical objects / capabilities |
|-------|-------------------|------------------------------|
| **Sales Cloud** | Revenue, pipeline, forecasting | Lead, Account, Opportunity, Quotes |
| **Service Cloud** | Case resolution, knowledge, SLAs | Case, Knowledge, Omni-Channel |
| **Experience Cloud** | Partner/customer self-service | Portals, communities, external users |
| **Field Service** | Dispatch, mobile workforce | Work orders, scheduling, assets |
| **Industries Cloud** | Vertical processes | FSC, Health Cloud, Mfg Cloud patterns |
| **Marketing Cloud** | Campaign engagement | Journeys (engagement model) |
| **Data Cloud** | Unified profile, segmentation | Identity resolution, activation |
| **Platform** | Custom processes, integration | Flow, Apex, LWC, events |

**BA focus:** capability fit, not feature lists. Deep dive: [salesforce-platform.md](salesforce-platform.md), [../../shared/salesforce-capability-map.md](../../shared/salesforce-capability-map.md).

## Key Terminology

See [../../shared/taxonomy.md](../../shared/taxonomy.md#salesforce-cloud-taxonomy).

## Frameworks and Models

Capability mapping → fit-gap → cloud licensing review with architect.

## Enterprise Best Practices

- Confirm clouds in scope in discovery
- Flag cross-cloud dependencies (e.g., portal + Service)
- Defer optional clouds to later release with Won't

## Common Mistakes

- Marketing Cloud for CRM process gaps
- Custom build when Experience Cloud fits

## Anti-Patterns

- Cloud selection by brand preference without capability map

## Decision Guidelines

Start with outcome; select cloud; validate license and edition with admin/architect.

## Real-World Examples

Apex Manufacturing: Sales + Service + Experience for dealer portal; ERP integration on Platform.

## Industry Considerations

Financial services: Industries Cloud for householding; strong compliance on external access.

## AI Guidance

Reasoning Stage 9. Do not invent edition-specific features—mark TBC.

## Review Checklist

- [ ] Clouds match capability themes
- [ ] Licensing flagged for CPQ, FSL, Data Cloud
- [ ] Cross-links to capability map

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

- **Previous:** [Risk Management](risk-management.md)
- **Next:** [Salesforce Platform](salesforce-platform.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
