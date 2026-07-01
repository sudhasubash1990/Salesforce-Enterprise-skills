---
title: Decision Framework
module: Salesforce Business Analyst
category: Brain
document_type: Framework
version: 0.2.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/decision-framework.md, salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/validation-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/business-analysis.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/brain/README.md]
keywords: [decision framework]
tags: [salesforce, business-analyst, brain, decision]
type: brain-module
---

# Decision Framework

## Purpose

Governs how the BA evaluates and recommends Salesforce solution approaches—configuration versus customization—and scores options against enterprise criteria. Implements Sprint 1 Milestones 1.7 (Solution Decision) and supports reasoning Stage 10.

## Solution Hierarchy

Evaluate options in this order. **Document why a lower layer was chosen** when a higher layer could apply.

| Priority | Layer | Examples |
|----------|-------|----------|
| 1 | **Standard Salesforce functionality** | Standard objects, native features, AppExchange where appropriate |
| 2 | **Configuration** | Record types, page layouts, picklists, validation rules, sharing rules |
| 3 | **Flow automation** | Record-triggered Flow, screen Flow, scheduled Flow |
| 4 | **Declarative platform capabilities** | Omni-Channel, entitlement processes, Experience Builder, approval processes |
| 5 | **Apex customization** | Triggers, services, batch—when declarative limits exceeded |
| 6 | **Integration** | MuleSoft, API, middleware, event-driven sync |
| 7 | **Custom UI** | LWC replacing standard UX where declarative insufficient |
| 8 | **External systems** | Third-party CPQ, billing, MDM when Salesforce not best fit |

## Fit-Gap Classification

Map hierarchy outcomes to fit-gap classes used in deliverables:

| Class | Hierarchy layers | Meaning |
|-------|------------------|---------|
| Standard | 1 | Native feature, minimal setup |
| Config | 2–4 | Declarative customization |
| Extend | 5–7 | Code or deep platform extension |
| Gap | 6–8 + process change | Third-party, major integration, or org change |
| Defer | — | Valid need, not this release |

Detailed playbook: [../playbooks/fit-gap-analysis.md](../playbooks/fit-gap-analysis.md).

## Evaluation Criteria

Score each option (Low / Medium / High or qualitative narrative):

| Criterion | Questions to ask |
|-----------|------------------|
| **Business value** | Does this directly enable the stated outcome? What is the ROI or risk reduction? |
| **Cost** | License, implementation, ongoing admin, and support cost? |
| **Complexity** | Skills required, number of moving parts, cross-team dependencies? |
| **Maintainability** | Can client admins own this post-go-live? Upgrade impact? |
| **Scalability** | Volume, users, geographies, data growth? |
| **User experience** | Adoption fit, mobile, offline, channel consistency? |
| **Technical debt** | One-off workarounds vs sustainable pattern? |
| **Governance impact** | Security, compliance, change control, release train fit? |

## Decision Record Template

For material decisions, log:

```markdown
| Decision ID | D-xxx |
| Requirement | BR-xxx |
| Options | A: [standard/config], B: [extend], C: [gap/defer] |
| Recommendation | [option] |
| Rationale | [criteria scores summary] |
| Owner | [role] |
| Status | Proposed / Approved / Deferred |
```

## Common Decision Patterns

| Situation | Default bias | Exception trigger |
|-----------|--------------|-------------------|
| New data entity | Use standard object if semantically fits | True net-new domain entity |
| Approval workflow | Flow or standard approval | Complex dynamic routing |
| External user access | Experience Cloud | Simple community with license constraints |
| Complex quoting | Evaluate CPQ / Revenue Cloud | Simple line items on Opportunity |
| High-volume integration | Platform Events, bulk patterns | Real-time sub-second sync needs |
| Reporting | Standard reports/dashboards | Embedded analytics, Data Cloud segmentation |

## Capability Mapping Link

Before classifying, map need to capability per [../../shared/salesforce-capability-map.md](../../shared/salesforce-capability-map.md) and [../knowledge/salesforce-platform.md](../knowledge/salesforce-platform.md).


## Related Knowledge Documents

- [../../shared/salesforce-capability-map.md](../../shared/salesforce-capability-map.md)
- [../knowledge/salesforce-platform.md](../knowledge/salesforce-platform.md)
- [../knowledge/domains.md](../knowledge/domains.md)




## Related Interview Questions

- [../interview-guide.md](../interview-guide.md) — Hiring: "Translates business need to platform-aware options"

## Related Brain Modules

- [Decision Framework](decision-framework.md)
- [Reasoning Framework](reasoning-framework.md)
- [Validation Framework](validation-framework.md)

## Related Knowledge

- [Readme](../knowledge/README.md)

## Related Templates

- [Readme](../templates/README.md)

## Related Playbooks

- [Readme](../playbooks/README.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [Business Analysis](../interview-guide/business-analysis.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Governance standards | **Downstream:** Knowledge, playbooks, templates | **Validation:** validation-framework.md

## Navigation

- **Previous:** [Consulting Principles](consulting-principles.md)
- **Next:** [Enterprise Behaviors](enterprise-behaviors.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
