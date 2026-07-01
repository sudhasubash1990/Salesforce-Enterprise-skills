---
title: Readme
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
keywords: [README]
tags: [README]
---

# Sample Project: Apex Manufacturing CRM Transformation

Fictional enterprise project demonstrating repository artifact linkage.

## Project Overview

| Attribute | Value |
|-----------|-------|
| Client | Apex Manufacturing (fictional) |
| Industry | Discrete manufacturing, B2B |
| Project code | PRJ-APEX-MFG-001 |
| Clouds | Sales Cloud, Service Cloud, Experience Cloud |
| Duration | 9 months, 3 releases |

## Business Drivers

- Fragmented customer data across ERP and legacy CRM
- Dealer channel lacks visibility into order and case status
- Sales reps spending 30% of time on non-selling activities

## Stakeholders

| Role | Name (fictional) | Interest |
|------|------------------|----------|
| Executive Sponsor | Maria Chen, VP Sales | Revenue growth, forecast accuracy |
| Product Owner | James Okonkwo | Backlog priority, UAT sign-off |
| Service Director | Elena Vasquez | Case resolution, dealer satisfaction |
| IT Integration Lead | David Park | ERP sync, data quality |

## Artifact Index

| Artifact | Location |
|----------|----------|
| BRD excerpt | `../sample-brd/brd-excerpt.md` |
| User stories | `../sample-user-story/dealer-portal-stories.md` |
| Workshop output | `../sample-workshop/discovery-workshop-notes.md` |

## Release Plan

| Release | Theme | Key capabilities |
|---------|-------|------------------|
| R1 | Core CRM | Account hierarchy, Lead-to-Opportunity, ERP account sync |
| R2 | Service | Case management, dealer queue, knowledge |
| R3 | Experience | Dealer portal, order status, case submission |

## Traceability Snapshot

| BR ID | Epic | Stories | Status |
|-------|------|---------|--------|
| BR-001 | EP-001 | US-001, US-002 | Released R1 |
| BR-005 | EP-003 | US-015, US-016 | Released R3 |

## Lessons Learned (Anonymized)

1. Dealer portal authentication required SSO decision in week 2—not week 12
2. Product hierarchy from ERP needed data steward before migration
3. Case auto-routing rules needed workshop with actual tier 2 agents

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

- [Readme](README.md)

## Related Documents

- [Metadata Schema](../../docs/metadata-schema.md)
- [Traceability Model](../../shared/traceability-model.md)

## Traceability

**Upstream:** Governance | **Downstream:** All modules | **Validation:** glossary consistency

## Navigation

- **Previous:** [Readme](README.md)
- **Next:** [Readme](README.md)
- **See Also:** [cross-linking-framework](../../docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
