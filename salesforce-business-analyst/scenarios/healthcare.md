---
title: Healthcare
module: Salesforce Business Analyst
category: Scenario
document_type: Enterprise Scenario
version: 1.1.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/decision-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/industry-patterns.md]
related_templates: [salesforce-business-analyst/templates/brd-template.md]
related_playbooks: [salesforce-business-analyst/playbooks/discovery-workshop-playbook.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/advanced/scenario-questions.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/scenarios/README.md]
keywords: [healthcare]
tags: [healthcare]
---

# Healthcare Scenario

> **Sprint 5:** Process scenarios in [healthcare/](healthcare/) — patient onboarding, appointments, claims, care management.

Industry context for provider, payer, and life sciences Salesforce programs.

## Typical Engagement Profile

- **Clouds:** Health Cloud (if licensed), Service Cloud, Experience Cloud, Sales Cloud (pharma)
- **Drivers:** Patient/member 360, care coordination, contact center efficiency, field rep effectiveness
- **Constraints:** HIPAA, minimum necessary, BAAs, PHI handling

## Common Capability Needs

| Capability | Requirements Themes | Fit-Gap Notes |
|------------|---------------------|---------------|
| Patient / member profile | Person Account, Health Cloud | De-identification rules |
| Care plans | Care teams, goals | Health Cloud vs custom |
| Prior authorization | Case workflow | Integration to claims |
| Provider network | Account hierarchy | Credentialing data |
| Patient portal | Experience Cloud | Authentication, consent |
| HCP engagement (pharma) | Calls, samples compliance | Industry Cloud features |

## HIPAA BA Discipline

- Document which fields are PHI
- Specify role-based access and break-glass if applicable
- No PHI in email alerts without client approval
- Confirm BAA coverage for Salesforce products in use

## Stakeholder Map (Typical)

| Role | Focus |
|------|-------|
| Chief Medical / Clinical ops | Care workflow |
| Privacy Officer | HIPAA controls |
| Contact center director | Case routing, AHT |
| HIM / data governance | Master patient index |

## Sample Requirements

**BR-HC-001:** Care coordinators must view open care plan tasks, recent encounters (from EHR integration), and authorized contacts on one member record.

**BR-HC-002:** Members must submit non-urgent inquiries via portal without exposing PHI to unauthorized household members.

## Integration Hot Spots

- EHR / EMR (Epic, Cerner patterns)
- Claims / eligibility (payer)
- Identity management for members
- HIE connectivity

## Workshop Prompts

- "What constitutes minimum necessary for this role?"
- "How are duplicates handled between MPI and Salesforce?"
- "What is the escalation path for clinical vs administrative cases?"

## Pitfalls

- Storing clinical documents without DMS strategy
- Portal authentication that doesn't match member identity proofing
- Ignoring nurse/licensee workflow variations by state

## Related Brain Modules

- [Reasoning Framework](../brain/reasoning-framework.md)
- [Decision Framework](../brain/decision-framework.md)

## Related Knowledge

- [Industry Patterns](../knowledge/industry-patterns.md)

## Related Templates

- [Brd Template](../templates/brd-template.md)

## Related Playbooks

- [Discovery Workshop Playbook](../playbooks/discovery-workshop-playbook.md)

## Related Industry Scenarios

- [Readme](README.md)

## Related Interview Topics

- [Scenario Questions](../interview-guide/advanced/scenario-questions.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Knowledge, playbooks | **Downstream:** BRD examples, interview scenarios | **Validation:** fit-gap analysis

## Navigation

- **Previous:** [Financial Services](financial-services.md)
- **Next:** [Manufacturing](manufacturing.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
