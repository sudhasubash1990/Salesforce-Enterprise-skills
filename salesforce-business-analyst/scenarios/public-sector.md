---
title: Public Sector
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
keywords: [public sector]
tags: [public-sector]
---

# Public Sector Scenario

Industry context for government, education, and nonprofit programs.

## Typical Engagement Profile

- **Clouds:** Service Cloud, Experience Cloud, Public Sector Solutions, Grants (NGO)
- **Drivers:** Constituent experience, case transparency, grant lifecycle, workforce productivity
- **Constraints:** Accessibility (508), public records, procurement, FedRAMP/GCC for federal US

## Common Capability Needs

| Capability | Requirements Themes | Fit-Gap Notes |
|------------|---------------------|---------------|
| Constituent case intake | Web forms, omni-channel | PII minimization |
| Program eligibility | Screening workflows | Integration to benefits systems |
| Grants management | Application, award, reporting | NGO Cloud vs custom |
| Licensing & permitting | Inspections, payments | Public Sector Solutions |
| FOIA / records requests | Case with redaction | Document management |
| Workforce hiring | Recruitment (if HR scope) | Often separate HCM |

## Stakeholder Map (Typical)

| Role | Focus |
|------|-------|
| Program director | Service levels, outcomes |
| CIO / IT security | GCC, ATO, identity |
| Legal / records | FOIA, retention |
| Accessibility coordinator | WCAG / 508 compliance |

## Regulatory BA Language

- Section 508 / WCAG for digital accessibility
- Public records and redaction workflows
- FedRAMP for federal cloud authorization (confirm deployment model)

## Sample Requirements

**BR-PS-001:** Constituents must apply for program benefits online, save draft applications, and receive status updates without creating duplicate person records.

**BR-PS-002:** Caseworkers must route cases by jurisdiction and program type with workload balancing across queues.

## Integration Hot Spots

- Legacy mainframe eligibility systems
- Payment gateways (government procurement rules)
- Document repositories
- GIS for jurisdiction routing

## Workshop Prompts

- "What must be public record vs confidential?"
- "How do you handle non-English constituents?"
- "What is the appeals process and timeline?"

## Pitfalls

- Underestimating accessibility testing in UAT
- Custom forms collecting excessive PII
- Ignoring seasonal volume spikes (tax season, enrollment)

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

- **Previous:** [Manufacturing](manufacturing.md)
- **Next:** [Readme](README.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
