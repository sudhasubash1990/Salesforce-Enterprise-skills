---
title: Fit Gap Analysis
module: Salesforce Business Analyst
category: Playbook
document_type: Consulting Methodology
version: 1.1.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/enterprise-behaviors.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/advanced/scenario-questions.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/playbooks/README.md]
keywords: [fit gap analysis]
tags: [fit-gap-analysis]
---

# Fit-Gap Analysis Playbook

> **Sprint 4:** Extended methodology in [gap-analysis-playbook.md](gap-analysis-playbook.md) and [solution-recommendation-playbook.md](solution-recommendation-playbook.md).

Platform-aware fit-gap for Salesforce requirements.

## Purpose

For each requirement, determine how Salesforce meets the need and what delivery approach is required—before backlog commitment.

## Classification Model

| Class | Definition | Typical Effort |
|-------|------------|----------------|
| **Standard** | Turn on feature; setup only | S |
| **Config** | Flows, validation, layouts, record types | S–M |
| **Extend** | Apex, LWC, complex Flow | M–L |
| **Gap** | Not native; needs ISV, custom app, or process change | L–XL |
| **Defer** | Valid; not this release | — |

## Analysis Workflow

```
For each BR/FR (Must + Should):
    1. Restate need in outcome language
    2. Search capability map for standard feature
    3. If partial → document gap portion only
    4. Propose recommendation (min 2 options for Gap)
    5. Note licensing, NFR, integration impacts
    6. Architect review for Extend/Gap
    7. Record classification in matrix
```

## Fit-Gap Matrix Template

| Req ID | Need Summary | Standard Feature | Class | Recommendation | Effort | Risk | Decision |
|--------|--------------|------------------|-------|----------------|--------|------|----------|
| BR-001 | Single customer view | Account + integration | Config | Nightly ERP sync | M | Med | Approved |
| BR-012 | Complex bundle pricing | CPQ | Gap | Evaluate CPQ license | L | High | Pending |

## Decision Rules (Senior BA)

1. **Standard before Config** — Prove standard insufficient.
2. **Config before Extend** — Code carries maintenance tax.
3. **Gap requires business case** — Cost, license, timeline.
4. **Defer is valid** — Better than over-scoping MVP.
5. **Process change is an option** — Sometimes the gap is the process, not Salesforce.

## Common Misclassifications

| Stated need | Often actually |
|-------------|----------------|
| Custom object for "Projects" | Standard Project management / PSA / custom after review |
| Apex trigger for validation | Validation rule or before-save Flow |
| Real-time ERP sync for all orders | Batch + exceptions for high-value orders |
| New portal from scratch | Experience Cloud template |

## Workshop: Fit-Gap Review

**Attendees:** BA, Architect, Admin, PO

**Agenda:** 2 hours per release slice

1. Walk matrix row by row
2. Challenge Extend/Gap classifications
3. Capture decisions in decision log
4. Update story estimates

## Outputs

- Approved fit-gap matrix
- Decision log entries for Gap items
- Updated BRD section or appendix
- Epic-level effort rollup for roadmap

Reference: [shared/salesforce-capability-map.md](../../shared/salesforce-capability-map.md)

## Related Brain Modules

- [Reasoning Framework](../brain/reasoning-framework.md)
- [Enterprise Behaviors](../brain/enterprise-behaviors.md)

## Related Knowledge

- [Readme](../knowledge/README.md)

## Related Templates

- [Readme](../templates/README.md)

## Related Playbooks

- [Readme](README.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [Scenario Questions](../interview-guide/advanced/scenario-questions.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Knowledge, templates | **Downstream:** Scenarios, workshop outputs | **Validation:** checklists.md

## Navigation

- **Previous:** [Executive Presentation Playbook](executive-presentation-playbook.md)
- **Next:** [Gap Analysis Playbook](gap-analysis-playbook.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
