---
title: Industry Patterns
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
related_interview_topics: [salesforce-business-analyst/interview-guide/salesforce/industries.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [industry patterns]
tags: [industry-patterns]
---

# Industry Patterns

Cross-industry patterns for Salesforce BA work.

## Financial Services

| Pattern | Salesforce Approach |
|---------|---------------------|
| KYC / due diligence | Custom objects or FSC if licensed; integration to KYC vendor |
| Household / relationship | Account hierarchies, FSC Households |
| Case for complaints | Service Cloud with regulatory timelines |
| Audit trail | Field history, Shield Event Monitoring for sensitive |

**BA focus:** Regulatory language TBC with Compliance; never invent retention periods.

## Healthcare & Life Sciences

| Pattern | Salesforce Approach |
|---------|---------------------|
| Patient vs member | Person Account or Health Cloud patterns |
| Care teams | Account teams, Care plans (Health Cloud) |
| HIPAA | Minimum necessary access, BAA with Salesforce, no PHI in unapproved channels |

**BA focus:** De-identification, consent, break-glass access procedures.

## Manufacturing & B2B

| Pattern | Salesforce Approach |
|---------|---------------------|
| Dealer / distributor | Partner Community, account-based sharing |
| ERP integration | Account, Order, Invoice sync |
| Service assets | Assets, warranties, work orders (FSL) |
| Complex catalogs | ERP product master; Salesforce for relationship |

**BA focus:** Channel partner visibility boundaries.

## Public Sector

| Pattern | Salesforce Approach |
|---------|---------------------|
| Constituent services | Case management, Experience Cloud |
| Grants | Grantmaking objects (NGO) or custom |
| FOIA / records | Case with redaction workflow |
| FedRAMP / GCC | Government cloud deployment constraints |

**BA focus:** Accessibility (Section 508), public records, procurement constraints.

## Cross-Industry

| Pattern | Notes |
|---------|-------|
| SSO / MFA | Enterprise IdP standard |
| Data migration | Always plan validation and reconciliation |
| Change management | Adoption requirements in BRD |
| Reporting | Define KPIs in requirements, not post-go-live |

See detailed scenarios in `../scenarios/`.

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

- [Industries](../interview-guide/salesforce/industries.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md

## Navigation

- **Previous:** [Governance Framework](governance-framework.md)
- **Next:** [Integration Patterns](integration-patterns.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
