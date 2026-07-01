---
title: Brd Excerpt
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
keywords: [brd excerpt]
tags: [brd-excerpt]
---

# BRD Excerpt — Apex Manufacturing

---
title: Business Requirements Document — Excerpt
type: brd
version: 0.9.0
status: review
last_updated: 2026-06-01
project: PRJ-APEX-MFG-001
---

## 1. Executive Summary

Apex Manufacturing will implement Salesforce Sales Cloud, Service Cloud, and Experience Cloud to unify customer data, streamline lead-to-cash handoffs with ERP, and enable dealer self-service. Expected outcomes: 15% reduction in average handle time, 25% reduction in dealer inbound calls, improved forecast accuracy.

## 2. Scope

### In Scope

- Account, Contact, Lead, Opportunity management
- Case management with dealer-specific record type
- ERP integration for Account and Order sync
- Dealer Experience Cloud portal (cases, orders, knowledge)
- Mobile sales for field representatives

### Out of Scope

- Marketing Cloud campaigns (Phase 2)
- CPQ implementation (evaluation only in R2)
- ERP replacement

## 3. Assumptions

1. ERP provides nightly batch API for Account and Order extracts
2. Dealer users < 2,000 for initial portal rollout
3. SSO available via corporate IdP for internal users; dealers use Experience Cloud login

## 4. Business Requirements

#### BR-001: Unified customer account record

| Attribute | Value |
|-----------|-------|
| Priority | Must |
| Source | Discovery workshop 2026-05-18 |
| Owner | Sales Operations |

**Statement:** The organization must maintain a single authoritative Account record in Salesforce for each sold-to customer, synchronized from ERP, enriched with CRM relationship data.

**Success measure:** Duplicate account rate < 2% within 60 days of R1 go-live.

---

#### BR-005: Dealer case submission

| Attribute | Value |
|-----------|-------|
| Priority | Must |
| Source | Discovery workshop |
| Owner | Service Operations |

**Statement:** Authorized dealer users must submit and track support cases through a secure portal without requiring phone or email contact.

**Success measure:** 40% of dealer cases originated via portal within 90 days of R3.

---

#### BR-006: Dealer order visibility

| Attribute | Value |
|-----------|-------|
| Priority | Should |
| Source | Service Director interview |
| Owner | Channel Operations |

**Statement:** Dealers must view order status and shipment tracking for their account through the portal.

**Success measure:** 25% reduction in order-status inbound calls.

## 5. Non-Functional Requirements

#### NFR-004: Integration latency

**Statement:** Order data displayed in portal must reflect ERP state within 24 hours under normal batch operations.

## 6. Open Questions

| # | Question | Owner |
|---|----------|-------|
| 1 | CPQ vs ERP quoting for complex bundles | Product Owner |
| 2 | EU dealer data residency | Legal |

## 7. Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Product Owner | James Okonkwo | | |
| Executive Sponsor | Maria Chen | | |

## Related Brain Modules

- [Consulting Principles](../../salesforce-business-analyst/brain/consulting-principles.md)

## Related Knowledge

- [Readme](../../salesforce-business-analyst/knowledge/README.md)

## Related Templates

- [Readme](../../salesforce-business-analyst/templates/README.md)

## Related Playbooks

- [Readme](../../salesforce-business-analyst/playbooks/README.md)

## Related Industry Scenarios

- [Readme](../../salesforce-business-analyst/scenarios/README.md)

## Related Interview Topics

- [Interview Index](../../salesforce-business-analyst/interview-guide/interview-index.md)

## Related Examples

- [Readme](../sample-project/README.md)

## Related Documents

- [Metadata Schema](../../docs/metadata-schema.md)
- [Traceability Model](../../shared/traceability-model.md)

## Traceability

**Upstream:** Governance | **Downstream:** All modules | **Validation:** glossary consistency

## Navigation

- **Previous:** —
- **Next:** —
- **See Also:** [cross-linking-framework](../../docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
