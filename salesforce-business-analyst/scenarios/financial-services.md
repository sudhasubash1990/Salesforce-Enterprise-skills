---
title: Financial Services
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
keywords: [financial services]
tags: [financial-services]
---

# Financial Services Scenario

> **Sprint 5:** Banking scenarios in [banking/](banking/) — KYC, loan origination, credit, collections. Insurance in [insurance/](insurance/).

Industry context for Salesforce BA work in banking, insurance, and wealth.

## Typical Engagement Profile

- **Clouds:** Sales Cloud, Service Cloud, FSC (if licensed), Experience Cloud
- **Drivers:** Client 360, regulatory complaints, cross-sell governance, advisor productivity
- **Constraints:** KYC/AML, audit, data residency, model risk

## Common Capability Needs

| Capability | Requirements Themes | Fit-Gap Notes |
|------------|---------------------|---------------|
| Client / household view | BR: unified profile | FSC Households vs custom |
| Onboarding / KYC | BR: due diligence workflow | Often vendor integration |
| Policy / account servicing | Case, entitlements | Service Cloud + industry objects |
| Complaints management | Regulatory timelines | Milestones, reporting |
| Advisor book management | Household, goals | FSC features vs custom |
| Consent & marketing | Opt-in capture | Marketing Cloud handoff |

## Regulatory BA Language

Never assert compliance. Use:

> "Support [specific control] as defined by client Compliance policy [ref TBC]."

Common areas: GDPR, PCI (if payments), local banking regulators, NAIC (insurance US).

## Stakeholder Map (Typical)

| Role | Focus |
|------|-------|
| Chief Compliance Officer | Audit, retention, surveillance |
| Distribution head | Advisor adoption, pipeline |
| Operations | Case SLAs, back-office integration |
| CISO | SSO, MFA, encryption |

## Sample Requirements

**BR-FS-001:** Relationship managers must view household AUM, open service cases, and compliance flags on a single screen before client meetings.

**BR-FS-002:** Complaints must be logged with category, regulatory clock start, and immutable audit trail.

## Integration Hot Spots

- Core banking / policy admin system
- KYC / sanctions screening
- Document management
- Data warehouse for regulatory reporting

## Workshop Prompts

- "What triggers a suspicious activity report workflow?"
- "How do you prove who saw what client data when?"
- "What breaks today during month-end or policy renewal peaks?"

## Pitfalls

- Underestimating sharing complexity across branches and advisors
- Custom objects duplicating FSC when licensed
- Real-time core banking sync without volume analysis

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

- **Previous:** [Readme](README.md)
- **Next:** [Healthcare](healthcare.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
