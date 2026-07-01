---
title: Requirements Engineering
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
keywords: [requirements engineering]
tags: [requirements-engineering]
---

# Requirements Engineering

> **Sprint 2 hub:** Canonical depth lives in the [knowledge base index](README.md). This file remains a quick-reference elicitation hub.

Methods for eliciting, analyzing, and specifying requirements on Salesforce programs.

## Deep-Dive Articles

| Topic | Article |
|-------|---------|
| Requirement types | [requirement-types.md](requirement-types.md) |
| User stories | [user-stories.md](user-stories.md) |
| Acceptance criteria | [acceptance-criteria.md](acceptance-criteria.md) |
| MoSCoW | [moscow-prioritization.md](moscow-prioritization.md) |
| Prioritization | [prioritization-techniques.md](prioritization-techniques.md) |
| Business rules | [business-rules.md](business-rules.md) |
| Stakeholders | [stakeholder-analysis.md](stakeholder-analysis.md) |

## Elicitation Techniques

| Technique | Best For | Salesforce Tip |
|-----------|----------|----------------|
| Interviews | Deep role understanding | Ask to see actual screens they use today |
| Workshops | Alignment, prioritization | Include admin/developer for feasibility probes |
| Observation | Workflow reality vs stated | Shadow case agents during peak hours |
| Document analysis | Regulations, legacy specs | Mine existing integration specs for entity ownership |
| Prototyping | Validation | Use Salesforce demos or click-through mockups early |

## Requirement Types

### Business Requirements (BR)

- **Why** and **what outcome**
- Technology-agnostic
- Owned by business sponsor

### Functional Requirements (FR)

- **What the system does** in response to events
- May reference Salesforce objects conceptually
- Owned by BA with architect input

### Non-Functional Requirements (NFR)

- Performance, security, availability, usability, compliance
- Must be measurable where possible

## Quality Rules

| Rule | Test |
|------|------|
| Atomic | One requirement, one idea |
| Unambiguous | One interpretation only |
| Testable | UAT scenario can verify |
| Traceable | Source documented |
| Feasible | Validated with platform |

## From Need to Story

```
Pain point (workshop)
    → Business requirement (BR)
    → Fit-gap classification
    → Functional requirement (FR) if needed
    → Epic
    → User stories with AC
    → Test scenarios
```

## Prioritization

**MoSCoW** for release scope. **WSJF** optional for backlog ordering within release.

Always separate:

- **Must for MVP** — go-live blockers
- **Must for program** — may defer to later release

## Conflict Resolution

When stakeholders disagree:

1. Restate shared outcome
2. Document options with impact (time, cost, risk)
3. Escalate to decision forum with recommendation
4. Record in decision log

## Common BA Failure Modes

| Failure | Prevention |
|---------|------------|
| Requirements = UI mockup | Ask "what decision does user make here?" |
| Missing exception paths | "What happens when ERP is down?" |
| Implicit integrations | Document system of record per entity |
| Role soup | Map to Salesforce profiles/permission sets |

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

- **Previous:** [Requirement Types](requirement-types.md)
- **Next:** [Risk Management](risk-management.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
