---
title: Discovery Playbook
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
keywords: [discovery playbook]
tags: [discovery-playbook]
---

# Discovery Playbook

> **Sprint 4:** Detailed methodology in [discovery-workshop-playbook.md](discovery-workshop-playbook.md). This file remains a quick-reference execution guide.

Structured discovery for enterprise Salesforce engagements.

## Objectives

- Understand business drivers and success metrics
- Map stakeholders and decision rights
- Document AS-IS processes and pain points
- Establish initial scope boundaries
- Identify risks, assumptions, and dependencies

## Phase Timeline (Typical)

| Week | Activity | Output |
|------|----------|--------|
| 1 | Kickoff, stakeholder map | RACI, comms plan |
| 1–2 | Executive interviews | Objectives, constraints |
| 2–3 | Functional workshops | AS-IS notes, pain points |
| 3 | Systems & data inventory | Integration map draft |
| 4 | Discovery readout | BRD outline, RAID log |

## Step 1: Stakeholder Mapping

Identify:

- **Executive sponsor** — funding and escalation
- **Product owner** — backlog authority
- **SMEs** — process truth
- **IT** — integration, security, environments
- **Change management** — adoption and training
- **End users** — validation participants

Template RACI per major process area.

## Step 2: Executive Interviews

Questions:

1. What does success look like in 12 months? How measured?
2. What failed in prior CRM initiatives?
3. Non-negotiable constraints (budget, date, compliance)?
4. What is explicitly out of scope?

## Step 3: Functional Workshops

Use [workshop-agenda.md](../templates/workshop-agenda.md).

Facilitation tips:

- Ground in scenarios: "Walk me through last Tuesday's escalation"
- Capture verbatim quotes for pain points
- Park solutioning—capture needs first
- Timebox debates; log decisions or defer with owner

## Step 4: Systems Inventory

| System | Owner | Entities | Direction | Notes |
|--------|-------|----------|-----------|-------|
| ERP | | Account, Order | Bidirectional | |
| Marketing | | Lead | Inbound | |

## Step 5: AS-IS / TO-BE

Document at capability level before screen level.

Use [process-map.md](../templates/process-map.md).

## Step 6: Discovery Readout

Present:

1. Objectives and scope hypothesis
2. Top 10 requirements themes (MoSCoW draft)
3. RAID log top items
4. Recommended next phase plan

Get explicit alignment on scope boundaries.

## Discovery Exit Criteria

- [ ] Signed charter or SOW alignment
- [ ] Stakeholder RACI approved
- [ ] BRD outline with numbered requirements started
- [ ] Integration inventory draft
- [ ] No unresolved executive blockers

## Artifacts

- Workshop notes → `examples/sample-workshop/`
- BRD sections 1–8 → [brd-template.md](../templates/brd-template.md)

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

- **Previous:** [Current State Assessment Playbook](current-state-assessment-playbook.md)
- **Next:** [Discovery Workshop Playbook](discovery-workshop-playbook.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
