---
title: Reasoning Framework
module: Salesforce Business Analyst
category: Brain
document_type: Framework
version: 0.2.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/validation-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/business-analysis.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/brain/README.md]
keywords: [reasoning framework]
tags: [salesforce, business-analyst, brain, reasoning]
type: brain-module
---

# Reasoning Framework

## Purpose

The core reasoning engine for Salesforce BA work. Every requirement, analysis, or deliverable request follows this 13-stage flow. Each stage defines purpose, inputs, activities, outputs, validation checks, decision criteria, and escalation conditions.

## Decision Flow Overview

```
Receive Requirement
    ↓
Understand Business Context
    ↓
Identify Business Problem
    ↓
Identify Stakeholders
    ↓
Ask Clarifying Questions
    ↓
Analyze Current State
    ↓
Define Future State
    ↓
Perform Gap Analysis
    ↓
Map Salesforce Capabilities
    ↓
Evaluate Configuration vs Customization
    ↓
Assess Risks
    ↓
Produce Deliverables
    ↓
Self Validate
```

---

## Stage 1: Receive Requirement

| Element | Detail |
|---------|--------|
| **Purpose** | Parse the request; classify deliverable type and urgency |
| **Inputs** | User message, attached context, prior conversation |
| **Activities** | Identify keywords (BRD, story, fit-gap, UAT, workshop); note industry/cloud signals |
| **Outputs** | Task classification, initial scope hypothesis |
| **Validation** | Deliverable type identified or one clarifying question queued |
| **Decision criteria** | Route to [output-framework.md](output-framework.md) artifact map |
| **Escalation** | If request spans BA + architecture + dev, sequence BA first per [.cursor/routing.md](../../.cursor/routing.md) |

---

## Stage 2: Understand Business Context

| Element | Detail |
|---------|--------|
| **Purpose** | Establish industry, clouds, methodology, constraints |
| **Inputs** | User context, `scenarios/<industry>.md`, project charter if provided |
| **Activities** | Confirm or infer industry, clouds in scope, regulated flag, integration landscape |
| **Outputs** | Context table (see [../skill.md](../skill.md) Step 1) |
| **Validation** | At least industry OR explicit "generic enterprise" assumption |
| **Decision criteria** | Load scenario file when industry known |
| **Escalation** | Multi-cloud scope without priority → ask once |

**Defaults if unknown:** Sales + Service + Platform; Agile with BRD anchor; 1 ERP + 1 marketing system.

---

## Stage 3: Identify Business Problem

| Element | Detail |
|---------|--------|
| **Purpose** | Separate symptoms from root business problems |
| **Inputs** | Stated pain points, workshop notes, stakeholder quotes |
| **Activities** | Apply "symptom vs cause" heuristic; state outcome and success measure |
| **Outputs** | Problem statement, business objectives, success criteria |
| **Validation** | Problem is outcome-oriented, not a screen or field request |
| **Decision criteria** | If user asked for a field/object, reframe to underlying need |
| **Escalation** | Conflicting problem definitions across stakeholders → workshop |

---

## Stage 4: Identify Stakeholders

| Element | Detail |
|---------|--------|
| **Purpose** | Know who validates, who uses, who decides |
| **Inputs** | Org chart hints, workshop attendance, RACI if available |
| **Activities** | Map sponsors, owners, users, IT, compliance; note missing voices |
| **Outputs** | Stakeholder map, validation owners per requirement theme |
| **Validation** | Sponsor and PO/business owner identified or flagged TBC |
| **Decision criteria** | Tailor communication per [communication-framework.md](communication-framework.md) |
| **Escalation** | No executive sponsor for major scope → [enterprise-behaviors.md](enterprise-behaviors.md) |

---

## Stage 5: Ask Clarifying Questions

| Element | Detail |
|---------|--------|
| **Purpose** | Fill critical gaps before documenting |
| **Inputs** | Unknowns from stages 2–4 |
| **Activities** | Ask **one** focused question if blocked; otherwise document assumptions |
| **Outputs** | Clarification questions OR assumptions section |
| **Validation** | No silent invention of regulatory, volume, or integration constraints |
| **Decision criteria** | See [../playbooks/requirements-elicitation.md](../playbooks/requirements-elicitation.md) |
| **Escalation** | User cannot answer → TBC with owner and validation date in RAID |

**Requirement discovery coverage (Milestone 1.4):**

| Topic | Guidance location |
|-------|-------------------|
| Elicitation techniques | [../playbooks/requirements-elicitation.md](../playbooks/requirements-elicitation.md) |
| Functional / non-functional requirements | [../knowledge/requirements-engineering.md](../knowledge/requirements-engineering.md) |
| Business rules, assumptions, constraints, dependencies | [../../shared/reusable-components.md](../../shared/reusable-components.md) |
| User stories, epics, features, AC | [../templates/user-story-template.md](../templates/user-story-template.md) |
| Scope boundaries, MoSCoW | [../templates/brd-template.md](../templates/brd-template.md) |
| Quality assessment | [validation-framework.md](validation-framework.md) |

---

## Stage 6: Analyze Current State

| Element | Detail |
|---------|--------|
| **Purpose** | Document AS-IS process, systems, pain points |
| **Inputs** | Interviews, observation, legacy docs |
| **Activities** | Process walkthrough, systems landscape, pain ranking |
| **Outputs** | AS-IS notes, process map inputs, pain point list |
| **Validation** | AS-IS grounded in observed or validated behaviour |
| **Decision criteria** | BPMN awareness for complex flows—see [../templates/process-map.md](../templates/process-map.md) |
| **Escalation** | No access to actual process → document as assumption |

**Business analysis methods (Milestone 1.5):** current state assessment, capability assessment, value stream thinking, opportunity identification—detailed in [../playbooks/discovery-playbook.md](../playbooks/discovery-playbook.md).

---

## Stage 7: Define Future State

| Element | Detail |
|---------|--------|
| **Purpose** | TO-BE capabilities aligned to business objectives |
| **Inputs** | Objectives, pain points, platform constraints |
| **Activities** | Capability list, TO-BE process, release phasing hints |
| **Outputs** | TO-BE process map, capability table with priority |
| **Validation** | Each capability links to a business objective |
| **Decision criteria** | Thin slices over big bang per consulting principles |
| **Escalation** | TO-BE exceeds budget/timeline → MoSCoW re-prioritization session |

---

## Stage 8: Perform Gap Analysis

| Element | Detail |
|---------|--------|
| **Purpose** | AS-IS vs TO-BE delta |
| **Inputs** | Stages 6 and 7 outputs |
| **Activities** | Gap list with business impact; process vs system gaps |
| **Outputs** | Gap themes feeding requirements and fit-gap |
| **Validation** | Gaps stated as business capability gaps, not "need Salesforce field X" |
| **Decision criteria** | Feed [../playbooks/fit-gap-analysis.md](../playbooks/fit-gap-analysis.md) |
| **Escalation** | Gap requires organizational change outside Salesforce → flag in RAID |

---

## Stage 9: Map Salesforce Capabilities

| Element | Detail |
|---------|--------|
| **Purpose** | Translate business needs to platform capabilities (Milestone 1.6) |
| **Inputs** | Gap list, clouds in scope |
| **Activities** | Map to capability map; identify cloud, object, feature area |
| **Outputs** | Capability mapping table, licensing flags |
| **Validation** | Mapping is capability-level, not feature memorization |
| **Decision criteria** | [../../shared/salesforce-capability-map.md](../../shared/salesforce-capability-map.md), [../knowledge/salesforce-platform.md](../knowledge/salesforce-platform.md) |

**Coverage areas:** Sales Cloud, Service Cloud, Experience Cloud, Field Service, Industries Cloud, Marketing Cloud, Data Cloud, Platform (Flow, security, reporting), integration patterns, OmniStudio where applicable.

---

## Stage 10: Evaluate Configuration vs Customization

| Element | Detail |
|---------|--------|
| **Purpose** | Apply solution decision hierarchy |
| **Inputs** | Capability mapping, constraints |
| **Activities** | Classify Standard / Config / Extend / Gap / Defer |
| **Outputs** | Fit-gap rows with recommendation |
| **Validation** | Standard option explored before custom |
| **Decision criteria** | [decision-framework.md](decision-framework.md) |
| **Escalation** | Extend/Gap with high risk → architect review |

---

## Stage 11: Assess Risks

| Element | Detail |
|---------|--------|
| **Purpose** | Identify and document delivery and solution risks (Milestone 1.8) |
| **Inputs** | Fit-gap, constraints, stakeholder map |
| **Activities** | Categorize business, technical, data, security, compliance, adoption, delivery, operational risks |
| **Outputs** | RAID entries with mitigation and owner |
| **Validation** | Top risks have mitigation and owner |
| **Decision criteria** | [../templates/raid-log-template.md](../templates/raid-log-template.md) |
| **Escalation** | Compliance risk → Legal/Compliance TBC |

---

## Stage 12: Produce Deliverables

| Element | Detail |
|---------|--------|
| **Purpose** | Generate enterprise artifacts |
| **Inputs** | All prior stage outputs |
| **Activities** | Select template; apply metadata; cross-reference IDs |
| **Outputs** | BRD, FRD, stories, fit-gap, RTM, workshop notes, etc. |
| **Validation** | Template used; metadata complete |
| **Decision criteria** | [output-framework.md](output-framework.md) |
| **Escalation** | Incomplete inputs → deliver draft with explicit TBC sections |

---

## Stage 13: Self Validate

| Element | Detail |
|---------|--------|
| **Purpose** | Quality gate before presenting to user |
| **Inputs** | Draft deliverable |
| **Activities** | Run [validation-framework.md](validation-framework.md) and [anti-hallucination.md](anti-hallucination.md) |
| **Outputs** | Validated deliverable + assumptions + open questions + next steps |
| **Validation** | All critical checklist items pass or exceptions documented |
| **Decision criteria** | [../checklists.md](../checklists.md) for artifact-specific gates |
| **Escalation** | Critical validation fail → revise before delivery |

---


## Related Knowledge Documents

- [knowledge/README.md](../knowledge/README.md) — Sprint 2 enterprise knowledge base (27 articles)
- [knowledge/requirement-types.md](../knowledge/requirement-types.md)
- [knowledge/salesforce-clouds-overview.md](../knowledge/salesforce-clouds-overview.md)
- [knowledge/integration-patterns.md](../knowledge/integration-patterns.md)
- [../knowledge/requirements-engineering.md](../knowledge/requirements-engineering.md)




## Related Interview Questions

- [../interview-guide.md](../interview-guide.md)

## Related Brain Modules

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

- **Previous:** [Output Framework](output-framework.md)
- **Next:** [Validation Framework](validation-framework.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
