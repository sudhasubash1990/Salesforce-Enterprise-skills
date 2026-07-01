---
title: Security Guidelines
module: Salesforce Business Analyst
category: Governance
document_type: Framework
version: 1.1.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [docs/metadata-schema.md, docs/cross-linking-framework.md]
keywords: [security guidelines]
tags: [security-guidelines]
---

# Security Guidelines

Security expectations for content and generated deliverables in this repository.

## Repository Security

- **Never commit** credentials, tokens, `.env` files, or org URLs with instance identifiers tied to real clients
- Use fictional org names in examples: `acme--dev.sandbox.example` pattern only if needed
- Scrub exports from real Salesforce orgs before using as examples

## Requirements Security

When authoring BA artifacts, always address:

| Topic | BA Responsibility |
|-------|-------------------|
| **Authentication** | Identify SSO, MFA, session policies—not just "users log in" |
| **Authorization** | Role-based access, sharing rules, field-level security |
| **Data classification** | PII, PHI, PCI—mark fields and retention needs |
| **Audit** | Who changed what, when—especially for regulated industries |
| **Integration** | API authentication model, encryption in transit/at rest |

## Prohibited Recommendations

Agents and contributors must not recommend:

- Disabling Salesforce security features to "simplify" requirements
- Storing secrets in custom fields or metadata without Vault pattern
- `View All Data` or `Modify All Data` as default permission strategy
- Guest user access beyond documented Experience Cloud minimum necessary

## Compliance Language

Use precise phrasing:

- ✅ "Must comply with client-defined retention policy (to be confirmed with Legal)"
- ❌ "Must be HIPAA compliant" (without scoped controls and client validation)

## Data in Examples

- Synthetic names: "Jane Doe", "John Smith" only in clearly fictional contexts
- No real SSN, credit card, or medical record numbers—even masked

## Incident Response

If real credentials or client data are committed:

1. Rotate credentials immediately
2. Remove from history per org policy
3. Notify repository maintainer

## Security Review Trigger

Escalate to security architect when requirements involve:

- Payment processing
- Health data (PHI)
- Government classified or CJIS contexts
- Customer-facing unauthenticated forms collecting sensitive data

## Related Brain Modules

N/A — no direct relationships for this document type.

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

- [Metadata Schema](metadata-schema.md)
- [Cross Linking Framework](cross-linking-framework.md)

## Traceability

**Upstream:** — | **Downstream:** All repository documents | **Validation:** validate_metadata.py

## Navigation

- **Previous:** [Review Process](review-process.md)
- **Next:** [Versioning](versioning.md)
- **See Also:** [cross-linking-framework](cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
