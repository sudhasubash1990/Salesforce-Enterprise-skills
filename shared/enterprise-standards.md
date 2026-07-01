---
title: Enterprise Standards
module: Salesforce Business Analyst
category: Shared
document_type: Reference
version: 1.1.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/consulting-principles.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [docs/metadata-schema.md, shared/traceability-model.md]
keywords: [enterprise standards]
tags: [enterprise-standards]
---

# Enterprise Standards

Standards for enterprise-scale Salesforce programs.

## Program Scale Indicators

An engagement is "enterprise" when three or more apply:

- Multiple business units or geographies
- Multiple Salesforce clouds or orgs
- Integration with 3+ enterprise systems
- Regulated industry (FS, HLS, Public Sector)
- 500+ users or complex sharing model
- Data migration > 1M records

## Documentation Standards

| Artifact | Minimum Standard |
|----------|------------------|
| BRD | Executive summary, scope, requirements with IDs, assumptions, appendices |
| User stories | Jira/ADO-ready with AC, refs, definition of done |
| Fit-gap | Standard/config/extend/gap classification per requirement |
| Decision log | Dated entries with decision maker |
| Traceability matrix | BR → US → TS minimum |

## Non-Functional Requirements (Enterprise)

Always consider:

- **Performance** — Page load, batch windows, API volume
- **Availability** — Business hours, maintenance windows
- **Scalability** — User growth, data growth
- **Security** — SSO, MFA, encryption, audit
- **Compliance** — Retention, residency, industry rules
- **Operability** — Monitoring, support tiers, runbooks
- **Localization** — Multi-language, currency, timezone

## Integration Standards

- Prefer event-driven and platform APIs over point-to-point where appropriate
- Define system of record per entity
- Document error handling, idempotency, and reconciliation

## Data Standards

- Data dictionary for custom objects/fields
- Migration: extract-transform-load mapping with validation rules
- Master data management strategy for Account, Contact, Product

## Release Standards

- Sandbox promotion path documented
- Release notes tied to requirement IDs
- Regression scope defined per release

## Steering and RAID

Maintain:

- **R**isks with owners and mitigation
- **A**ssumptions validated on schedule
- **I**ssues with resolution SLAs
- **D**ependencies across workstreams

## Related Brain Modules

- [Consulting Principles](../salesforce-business-analyst/brain/consulting-principles.md)

## Related Knowledge

- [Readme](../salesforce-business-analyst/knowledge/README.md)

## Related Templates

- [Readme](../salesforce-business-analyst/templates/README.md)

## Related Playbooks

- [Readme](../salesforce-business-analyst/playbooks/README.md)

## Related Industry Scenarios

- [Readme](../salesforce-business-analyst/scenarios/README.md)

## Related Interview Topics

- [Interview Index](../salesforce-business-analyst/interview-guide/interview-index.md)

## Related Examples

- [Readme](../examples/sample-project/README.md)

## Related Documents

- [Metadata Schema](../docs/metadata-schema.md)
- [Traceability Model](traceability-model.md)

## Traceability

**Upstream:** Governance | **Downstream:** All modules | **Validation:** glossary consistency

## Navigation

- **Previous:** [Document Types](document-types.md)
- **Next:** [Glossary](glossary.md)
- **See Also:** [cross-linking-framework](../docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
