---
title: Manufacturing
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
keywords: [manufacturing]
tags: [manufacturing]
---

# Manufacturing Scenario

Industry context for discrete and process manufacturing, B2B, and aftermarket.

## Typical Engagement Profile

- **Clouds:** Sales Cloud, Service Cloud, Experience Cloud, FSL (field service)
- **Drivers:** Dealer/channel management, ERP alignment, warranty/service, configure-to-order
- **Constraints:** ERP as product master, global sites, channel partner access boundaries

## Common Capability Needs

| Capability | Requirements Themes | Fit-Gap Notes |
|------------|---------------------|---------------|
| Account hierarchy | Sold-to, ship-to, dealer | ERP sync |
| Lead to quote | Opportunity, ERP quote | CPQ vs ERP-led |
| Order visibility | Portal, integration | Custom Order object |
| Warranty / claims | Cases, Assets | Asset lifecycle |
| Field service | Work orders, parts | FSL licensing |
| Dealer portal | Partner community | Sharing by account |

## Stakeholder Map (Typical)

| Role | Focus |
|------|-------|
| VP Sales / Channel | Dealer satisfaction, pipeline |
| Service director | Warranty, parts, SLA |
| Supply chain IT | ERP integration |
| Quality | Recall / defect cases |

## Sample Requirements

See worked examples: [examples/sample-brd/](../../examples/sample-brd/brd-excerpt.md), [examples/sample-user-story/](../../examples/sample-user-story/dealer-portal-stories.md).

**BR-MFG-001:** Sales reps must create opportunities with ERP-validated product codes without re-keying catalog data.

**BR-MFG-002:** Dealers must open warranty cases linked to serial numbers validated against shipment records.

## Integration Hot Spots

- ERP (SAP, Oracle, Dynamics) — Account, Product, Order, Invoice
- PLM for engineering changes
- Dealer management systems

## Workshop Prompts

- "Who owns the product hierarchy—ERP or CRM?"
- "What can a dealer see vs your direct sales team?"
- "How do recalls propagate to field service?"

## Pitfalls

- Bi-directional product sync without conflict rules
- Dealer users over-provisioned access
- Quoting complexity discovered after Release 1 scope frozen

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

- **Previous:** [Healthcare](healthcare.md)
- **Next:** [Public Sector](public-sector.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
