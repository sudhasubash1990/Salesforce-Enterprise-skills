---
title: Dealer Portal Stories
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
keywords: [dealer portal stories]
tags: [dealer-portal-stories]
---

# Dealer Portal User Stories — Apex Manufacturing

---
title: Dealer Portal User Stories
type: user-story
version: 1.0.0
status: approved
last_updated: 2026-06-10
project: PRJ-APEX-MFG-001
epic: EP-003
---

## Epic EP-003: Dealer Self-Service Portal

**Outcome:** Dealers resolve issues and track orders without calling support, reducing inbound volume by 25%.

---

### US-015: Submit support case via portal

**As a** Dealer User,
**I want** to submit a support case with category, description, and attachments,
**So that** I receive tracked support without phone wait times.

**Requirement refs:** BR-005

**Acceptance criteria:**

1. Given an authenticated dealer user, when they complete the case form with required fields (Category, Subject, Description), then a Case is created linked to their Account.
2. Given a file under 10MB in allowed formats (PDF, PNG, JPG), when attached to submission, then the file is stored on the Case.
3. Given successful submission, when the case is created, then the dealer receives email confirmation with Case number.
4. Given missing required fields, when user attempts submit, then inline validation prevents submission.

**Data considerations:** Case.RecordType = Dealer; Case.Origin = Portal; Experience Cloud user license

**Notes:** Confirm case categories with Service Operations

---

### US-016: View order status in portal

**As a** Dealer User,
**I want** to view status of my open orders,
**So that** I can inform my customers without contacting Apex support.

**Requirement refs:** BR-006

**Acceptance criteria:**

1. Given orders synced from ERP within last 24 hours, when dealer views Order list, then orders for their Account only are displayed.
2. Given an order in status Shipped, when viewing order detail, then tracking number and ship date are visible.
3. Given a dealer user for Account A, when attempting URL access to Order for Account B, then access is denied.

**Data considerations:** Custom object Order__c or OMS integration; sharing via Account relationship

**Notes:** ERP sync frequency SLA = 24h (NFR-004)

---

### US-017: Search knowledge articles

**As a** Dealer User,
**I want** to search published knowledge articles,
**So that** I can self-resolve common issues before opening a case.

**Requirement refs:** BR-007

**Acceptance criteria:**

1. Given published articles with Data Category "Dealer", when user searches by keyword, then matching articles display title and summary.
2. Given article marked Internal Only, when dealer searches, then article is excluded from results.
3. Given user views article, when article is displayed, then view count increments for analytics.

**Notes:** Content authoring workflow out of scope for R3; marketing provides initial 20 articles

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
