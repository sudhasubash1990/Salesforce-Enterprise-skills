---
title: Validation Framework
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
keywords: [validation framework]
tags: [salesforce, business-analyst, brain, validation]
type: brain-module
---

# Validation Framework

## Purpose

Mandatory self-review checklist before presenting any BA deliverable to the user. Implements Sprint 1 Milestone 1.10 (Review & Validation). Run after [reasoning-framework.md](reasoning-framework.md) Stage 12 and before final response.

## Pre-Delivery Validation Checklist

Answer each item. **Fail any critical item → revise before delivery.**

| # | Check | Critical |
|---|-------|----------|
| 1 | Is the business problem clearly defined? | Yes |
| 2 | Are business objectives understood and linked to requirements? | Yes |
| 3 | Are assumptions documented in a dedicated section? | Yes |
| 4 | Are clarification questions required—and either asked or listed as open? | Yes |
| 5 | Is the recommendation aligned with Salesforce best practices? | Yes |
| 6 | Has configuration been preferred over customization where appropriate? | Yes |
| 7 | Are risks documented (or RAID updated)? | Yes |
| 8 | Are assumptions, constraints, and dependencies captured? | Yes |
| 9 | Is the proposed solution traceable to the requirement (IDs linked)? | Yes |
| 10 | Is the output complete per template/artifact type? | Yes |
| 11 | Is the language suitable for the intended audience? | Yes |
| 12 | Are unsupported claims avoided? (see [anti-hallucination.md](anti-hallucination.md)) | Yes |
| 13 | Has the response been checked for internal consistency? | Yes |

## Artifact-Specific Gates

After the universal checklist, run the relevant gate from [../checklists.md](../checklists.md):

| Artifact | Checklist section |
|----------|-------------------|
| BRD | BRD Quality Gate |
| User story | User Story Quality Gate |
| Fit-gap | Fit-Gap Quality Gate |
| Workshop | Workshop Quality Gate |
| UAT | UAT Scenario Quality Gate |

## Risk & Governance Validation (Milestone 1.8)

Confirm coverage when producing analysis or RAID:

| Risk category | Example triggers |
|---------------|------------------|
| Business | Adoption, process change resistance, ROI not achieved |
| Technical | Governor limits, integration failure, technical debt |
| Data | Quality, migration, master data ownership |
| Security | Sharing model, external users, privileged access |
| Compliance | Regulatory TBC, audit trail, data residency |
| Adoption | Training gap, mobile/offline, role change |
| Delivery | Dependency slip, resource, environment readiness |
| Operational | Support model, monitoring, batch windows |

Each material risk: mitigation, owner, review frequency in RAID.

## Validation Outcomes

| Outcome | Action |
|---------|--------|
| **Pass** | Deliver with assumptions, open questions, next steps |
| **Pass with TBC** | Deliver; prominently list TBC items and owners |
| **Fail** | Revise draft; do not present as complete |
| **Blocked** | Ask one clarifying question; do not invent missing context |

## Standard Closing Sections

Every generated deliverable ends with:

```markdown
## Assumptions
- [List]

## Open Questions
- [List with owner if known]

## Suggested Next Steps
- [List]
```

Per [../../shared/output-standards.md](../../shared/output-standards.md).


## Related Knowledge Documents

- [../../docs/quality-framework.md](../../docs/quality-framework.md)
- [../../shared/output-standards.md](../../shared/output-standards.md)




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

- **Previous:** [Reasoning Framework](reasoning-framework.md)
- **Next:** [Readme](README.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
