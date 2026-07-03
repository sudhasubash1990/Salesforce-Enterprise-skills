---
title: Change Management
module: Salesforce Business Analyst
category: Playbook
document_type: Consulting Methodology
version: 1.0.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-03
last_updated: 2026-07-03
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/enterprise-behaviors.md, salesforce-business-analyst/brain/communication-framework.md, salesforce-business-analyst/brain/consulting-principles.md]
related_knowledge: [salesforce-business-analyst/knowledge/stakeholder-analysis.md, salesforce-business-analyst/knowledge/governance-framework.md, salesforce-business-analyst/knowledge/constraints-management.md]
related_templates: [salesforce-business-analyst/templates/comms-upskilling-plan-template.md, salesforce-business-analyst/templates/stakeholder-matrix-template.md, salesforce-business-analyst/templates/raid-log-template.md]
related_playbooks: [salesforce-business-analyst/playbooks/digital-transformation-strategy-playbook.md, salesforce-business-analyst/playbooks/production-readiness-playbook.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/stakeholders.md, salesforce-business-analyst/interview-guide/advanced/behavioral.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/playbooks/README.md]
keywords: [change management playbook, ocm, resistance analysis, upskilling, adoption, role transition, communications]
tags: [change-management, ocm, adoption]
---

# Change Management

## Purpose

Repeatable methodology for organizational change management (OCM) on enterprise Salesforce and transformation programmes: resistance analysis, mitigation planning (early comms, upskilling, role transition), and adoption tracking through hypercare.

**Scope note:** this playbook covers *people/organizational* change. For technical change requests (CRs) and the Change Control Board, see [../knowledge/governance-framework.md](../knowledge/governance-framework.md).

## Business Objectives

- Surface and address resistance before it becomes a delivery or adoption risk
- Transition automation-impacted roles with dignity and a clear path (e.g. into exception management)
- Achieve adoption targets so business-case benefits are actually realized
- Keep stakeholders informed early and continuously — no surprises at go-live

## Success Criteria

- Change impact assessment completed and signed off per impacted group
- Comms and upskilling plan published and executing on schedule
- Adoption / readiness metrics at or above target during hypercare
- No unmitigated Red resistance items at go-live gate

## Scope

Applies to Salesforce implementation and legacy-modernization programmes with material process, role, or automation impact. Delivery method agnostic (Agile, hybrid, waterfall).

## Prerequisites

- Stakeholder map available ([../templates/stakeholder-matrix-template.md](../templates/stakeholder-matrix-template.md))
- AS-IS / TO-BE process definition (impact source)
- Executive sponsor identified and engaged
- Access to [../brain/enterprise-behaviors.md](../brain/enterprise-behaviors.md) and [../brain/communication-framework.md](../brain/communication-framework.md)

## Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| Executive Sponsor | Visible advocacy, message delivery to leadership and workforce |
| Change Lead | Owns strategy, comms calendar, readiness metrics |
| BA Lead | Impact assessment from AS-IS/TO-BE deltas, traceability |
| HR / People Partner | Role transition, upskilling programmes, union/works-council liaison |
| Operations Managers | Champion network, team-level messaging, feedback loop |

## Inputs

- AS-IS / TO-BE process maps and value-chain analysis
- Stakeholder matrix with influence/impact ratings
- Automation scope (which activities are being automated)
- Business case adoption assumptions

## Entry Criteria

- [ ] TO-BE design stable enough to assess role impact
- [ ] Sponsor committed to visible participation
- [ ] Change lead assigned

## Methodology Overview

Five stages: **Impact assessment → Resistance analysis → Mitigation planning → Execution (comms + upskilling) → Adoption tracking.**

## Detailed Activities

1. **Change impact assessment** — from AS-IS/TO-BE deltas, catalogue what changes per role/team: process, tooling, KPIs, reporting lines, headcount-neutral role shifts.
2. **Resistance analysis** — for each impacted group, assess sentiment, root cause of resistance, and severity. Common patterns:

   | Resistance Pattern | Typical Root Cause | Severity Signal |
   |--------------------|--------------------|-----------------|
   | Operations team resistance | Loss of familiar process control; distrust of new system accuracy | Workshop non-attendance, passive UAT participation |
   | Fear of automation replacing jobs | No communicated role-transition path | Rumours, attrition spikes, union queries |
   | Middle-management blocking | KPI/status loss in TO-BE structure | Delayed sign-offs, escalation churn |
   | Regional divergence | "Our region is different" exceptionalism | Requests for local exceptions to standard process |

3. **Mitigation planning** — pair every Red/Amber resistance item with a mitigation:

   | Mitigation | Description |
   |------------|-------------|
   | Early communications | First message before design freeze; honest about what changes and what does not |
   | Early upskilling | Training starts during build, not at go-live; sandbox access for hands-on familiarity |
   | Automation strategy transparency | Publish which activities are automated and why; quantify the repetitive work removed |
   | Role transition into exception management | Map automation-impacted roles to exception-management and quality-control roles with a shadow → dual-run → transition path |
   | Champion network | Respected team members recruited as change champions with early access |

4. **Execution** — instantiate [../templates/comms-upskilling-plan-template.md](../templates/comms-upskilling-plan-template.md); run the comms calendar and training matrix; log resistance items in the RAID log.
5. **Adoption tracking** — readiness surveys pre-go-live; usage and support-ticket metrics through hypercare; feed results to governance calls and KPI dashboards.

## Deliverables

| Change impact assessment | Resistance and mitigation register | Comms and upskilling plan | Role transition plan | Adoption metrics dashboard |

## Decision Gates

| Gate | Criteria | Owner |
|------|----------|-------|
| Design close | Impact assessment signed off; comms plan drafted | Change Lead |
| Go-live readiness | Training completion ≥ target; no unmitigated Red resistance | Sponsor / Steering |
| Hypercare exit | Adoption metrics at target for [n] consecutive weeks | Change Lead / PM |

## Risks

| Risk | Mitigation |
|------|------------|
| Comms start too late; rumours fill the vacuum | Calendar anchored to design milestones, not go-live |
| Training treated as one-off event | Phased upskilling with sandbox practice and floor support |
| Role transition promises not honoured | HR co-owns transition plan; commitments in writing |
| Champion network tokenistic | Champions get early access, real feedback influence |

## Mitigation Strategies

Anchor every mitigation to a named owner and date in the RAID log; review resistance register at each weekly status call; escalate unmitigated Red items to steering.

## Quality Checks

- [ ] [../brain/validation-framework.md](../brain/validation-framework.md)
- [ ] [../checklists.md](../checklists.md) applicable sections
- [ ] Every impacted group has sentiment, root cause, mitigation, owner

## Outputs

Listed under Deliverables; file in project repository with metadata. Save engagement instances under `outputs/<project>/` per output-generation rules.

## Exit Criteria

- [ ] Adoption metrics at target through hypercare
- [ ] Role transitions completed or on committed schedule
- [ ] Lessons learned captured for the change approach

## Lessons Learned

Capture at retrospective: which resistance patterns were missed, which comms landed, upskilling effectiveness.

## Best Practices

- Communicate what does NOT change as clearly as what does
- Treat resistance as data, not disloyalty — root-cause it
- Upskill before cutover; people should meet the new system before it meets them
- Make the sponsor visible at every major milestone

## Anti-Patterns

- Announcing automation without a role-transition story
- One mass email counted as "communications done"
- Training scheduled only in the go-live week
- Ignoring middle management (the layer that makes or breaks adoption)

## AI Execution Guidance

**Ask before proceeding:** impacted groups and sizes, automation scope, union/works-council constraints, regional spread, sponsor availability.

**Decision points:** resistance severity ratings, mitigation selection, go-live readiness call.

**Escalate when:** headcount reduction is implied (HR/legal territory), union consultation required, sponsor disengaged, Red resistance unmitigated at gate.

**Validate:** anti-hallucination + validation framework before client delivery. Never fabricate sentiment data — mark as TBC until surveyed.

## Related Brain Modules

- [Enterprise Behaviors](../brain/enterprise-behaviors.md)
- [Communication Framework](../brain/communication-framework.md)
- [Consulting Principles](../brain/consulting-principles.md)

## Related Knowledge

- [Stakeholder Analysis](../knowledge/stakeholder-analysis.md)
- [Governance Framework](../knowledge/governance-framework.md)
- [Constraints Management](../knowledge/constraints-management.md)

## Related Templates

- [Comms and Upskilling Plan Template](../templates/comms-upskilling-plan-template.md)
- [Stakeholder Matrix Template](../templates/stakeholder-matrix-template.md)
- [Raid Log Template](../templates/raid-log-template.md)

## Related Playbooks

- [Digital Transformation Strategy Playbook](digital-transformation-strategy-playbook.md)
- [Production Readiness Playbook](production-readiness-playbook.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [Stakeholders](../interview-guide/stakeholders.md)
- [Behavioral](../interview-guide/advanced/behavioral.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** AS-IS/TO-BE analysis, stakeholder matrix, automation scope | **Downstream:** Comms plan, training delivery, adoption dashboards, hypercare | **Validation:** checklists.md

## Navigation

- **Previous:** [Business Capability Assessment Playbook](business-capability-assessment-playbook.md)
- **Next:** [Current State Assessment Playbook](current-state-assessment-playbook.md)
- **See Also:** [Comms and Upskilling Plan Template](../templates/comms-upskilling-plan-template.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | BA Practice Lead | Initial change management playbook (resistance analysis, mitigation, comms/upskilling execution, adoption tracking) |
