---
title: Epic Design
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
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [epic design]
tags: [epic, backlog, story-mapping, release]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Epic Design

## Overview

Structuring epics, features, and capabilities for Salesforce release planning and backlog hierarchy.

## Purpose

Guide decomposition from business capabilities to deliverable epics and sprint-sized stories.

## Why It Matters

Poor epic boundaries cause cross-sprint dependencies, unclear value, and ungovernable backlogs.

## Business Context

Epics represent large business outcomes delivered over multiple sprints or releases.

## Salesforce Context

Epics often align to clouds, channels (Experience Cloud), or integration domains—sequence by dependency and license readiness.

## Core Concepts

**Hierarchy:**

```
Business objective
  └── Epic (EP-xxx)
        └── Feature / capability group
              └── User story (US-xxx)
```

**Story mapping:** User journey steps across backbone; stories placed under releases.

**Release planning:** MoSCoW at BR level; epics tagged R1/R2/R3.

## Key Terminology

| Term | Definition |
|------|------------|
| Epic | Large outcome; multiple stories |
| Feature | Cohesive capability within epic |
| Story map | Visual backlog across journey and releases |

## Frameworks and Models

- Story mapping (Jeff Patton style) in discovery workshops
- WSJF for epic sequencing—see [prioritization-techniques.md](prioritization-techniques.md)

## Enterprise Best Practices

- Epic links to BR ID and measurable outcome
- Defer CPQ-scale epics until foundation stable
- Identify dependencies between epics early

## Common Mistakes

- Epics without measurable outcome
- Single epic spanning unrelated clouds without phasing

## Anti-Patterns

- Epic = one giant story
- Epic titles as technical components ("Apex integration")

## Decision Guidelines

| Epic size signal | Action |
|------------------|--------|
| > 3 sprints of stories | Split by release slice |
| Hard dependency on ERP | Sequence after integration epic |

## Real-World Examples

EP-003 Dealer Portal MVP: authentication, case submit, status view—R3 in Apex Manufacturing sample.

## Industry Considerations

Public sector: epics may align to legislative milestones or funding periods.

## AI Guidance

When user asks for epics, require BR linkage and release hint. Decompose to stories via [user-stories.md](user-stories.md).

## Review Checklist

- [ ] Epic has outcome and BR ref
- [ ] Release phasing documented
- [ ] Dependencies listed

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

- **Previous:** [Domains](domains.md)
- **Next:** [Future State Design](future-state-design.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
