---
title: Future State Design
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
related_interview_topics: [salesforce-business-analyst/interview-guide/future-state.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [future state design]
tags: [future-state, to-be, target-operating-model]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Future State Design

## Overview

TO-BE capabilities, process improvements, automation opportunities, and success measures.

## Purpose

Define target operating model aligned to business objectives before detailed Salesforce design.

## Why It Matters

TO-BE without measurable outcomes and phased releases leads to big-bang failure.

## Business Context

Future state describes how the organization will work—not only which Salesforce features to turn on.

## Salesforce Context

Map TO-BE capabilities to clouds, releases, and integration patterns. Flag adoption and training needs.

## Core Concepts

- **Target capabilities:** Prioritized list with MoSCoW
- **Process improvements:** Eliminate handoffs, automate decisions, self-service
- **Automation candidates:** Flow, assignment rules, Omni-Channel
- **UX principles:** Mobile, portal, unified desktop
- **Success measures:** KPIs per capability

## Key Terminology

| Term | Definition |
|------|------------|
| TOM | Target operating model |
| Release slice | Subset of TO-BE in one go-live |

## Frameworks and Models

- [capability-models.md](capability-models.md)
- [moscow-prioritization.md](moscow-prioritization.md)
- Gap analysis: current → future

## Enterprise Best Practices

- Thin-slice TO-BE into releases
- Include change impact on roles
- Validate TO-BE with demos before BRD sign-off

## Common Mistakes

- TO-BE as unlimited vision without Won't list
- No adoption plan for role changes

## Anti-Patterns

- TO-BE = copy of vendor demo script
- Ignoring offline or field constraints

## Decision Guidelines

Must capabilities in R1 need validated dependencies (data, SSO, integration).

## Real-World Examples

Discovery readout: unified Account from ERP R1; dealer portal cases R3; CPQ Won't R1.

## Industry Considerations

Healthcare: clinician workflow time is a success measure, not only case closure rate.

## AI Guidance

Reasoning Stage 7. Link each TO-BE capability to BR ID and release hint.

## Review Checklist

- [ ] KPI per major capability
- [ ] Release phasing documented
- [ ] Out-of-scope explicit

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

- [Future State](../interview-guide/future-state.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md

## Navigation

- **Previous:** [Epic Design](epic-design.md)
- **Next:** [Governance Framework](governance-framework.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
