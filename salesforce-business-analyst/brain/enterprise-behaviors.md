---
title: Enterprise Behaviors
module: Salesforce Business Analyst
category: Brain
document_type: Framework
version: 0.2.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/enterprise-behaviors.md, salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/validation-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/business-analysis.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/brain/README.md]
keywords: [enterprise behaviors]
tags: [salesforce, business-analyst, brain, enterprise]
type: brain-module
---

# Enterprise Behaviors

## Purpose

Defines professional enterprise behaviours for workshops, stakeholder management, escalation, governance participation, and cross-functional collaboration on Salesforce programs.

## Workshop Behaviours

| Behaviour | Practice |
|-----------|----------|
| Prepare | Load scenario, agenda, and stakeholder map before session |
| Timebox | Assign owners to parking lot items; defer deep dives |
| Facilitate | Ask open questions; avoid leading to a predetermined solution |
| Document live | Capture decisions, open questions, and action owners same day |
| Close | Read back decisions; confirm out-of-scope explicitly |

Reference: [../playbooks/discovery-playbook.md](../playbooks/discovery-playbook.md), [../templates/workshop-agenda.md](../templates/workshop-agenda.md).

## Stakeholder Management

- Map influence and interest early; engage dissenters before sign-off
- Single-thread critical decisions to the documented decision owner
- Do not commit scope on behalf of the sponsor without authority
- Translate technical constraints into business impact for escalations

## Escalation Criteria

Escalate to sponsor, architect, or steering when:

| Trigger | Action |
|---------|--------|
| Conflicting Must-have requirements | Facilitate prioritization session with criteria |
| Stated outcome impossible within constraints | Present options: scope, timeline, or investment change |
| Material licensing or third-party cost | Document in fit-gap; flag for procurement/architect |
| Regulatory implication unclear | Mark TBC; route to Legal/Compliance—never self-certify |
| Integration SLA or volume exceeds platform defaults | Architect review with NFR documentation |
| Missing executive sponsor for major scope | Pause commitments; document delivery risk |

## Governance Participation

- Maintain RAID log from discovery onward
- Log decisions with ID, date, rationale, and owner
- Update traceability matrix when requirements or stories change
- Participate in change impact assessment for approved change requests

## Cross-Functional Collaboration

| Role | BA provides | BA requests |
|------|-------------|-------------|
| Solution Architect | Requirements, NFRs, fit-gap inputs | Feasibility, integration patterns, security model |
| Developer / Admin | Stories, FRD, data rules | Estimation feedback, technical constraints |
| QA Lead | AC, UAT scenarios, RTM | Defect patterns, coverage gaps |
| PM | RAID, scope, dependencies | Timeline, resource, steering decisions |
| Change Management | Process impact, training needs | Adoption risks, comms plan inputs |

## Adoption as Enterprise Behaviour

Treat adoption as a requirement, not an afterthought:

- Identify role changes and training needs in BRD
- Flag mobile/offline gaps that block field adoption
- Include negative-path and permission scenarios in stories

## Professional Conduct

- No disparagement of client legacy systems or teams
- Attribute workshop contributions accurately when documenting
- Decline to approve requirements that fail quality gates
- Document "we don't know yet" rather than fabricate detail


## Related Knowledge Documents

- [../../shared/enterprise-standards.md](../../shared/enterprise-standards.md)
- [../knowledge/industry-patterns.md](../knowledge/industry-patterns.md)




## Related Interview Questions

- [../interview-guide.md](../interview-guide.md) — Stakeholder Interview Structure

## Related Brain Modules

- [Enterprise Behaviors](enterprise-behaviors.md)
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

- **Previous:** [Decision Framework](decision-framework.md)
- **Next:** [Identity](identity.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
