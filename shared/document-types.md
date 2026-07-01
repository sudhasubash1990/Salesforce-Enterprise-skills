---
title: Document Types
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
keywords: [document types]
tags: [document-types]
---

# Document Types

Standard document types and their purpose in Salesforce delivery.

| Type | Code | Purpose | Primary Audience |
|------|------|---------|------------------|
| Business Requirements Document | `brd` | Authoritative business needs and scope | Sponsor, PO, BA, Architect |
| Functional Specification | `frs` | Detailed functional behavior | BA, Dev, QA |
| User Story | `user-story` | Agile backlog item with AC | PO, Dev, QA |
| Epic | `epic` | Large feature grouping | PO, Steering |
| Fit-Gap Analysis | `fit-gap` | Standard vs custom decisions | BA, Architect |
| Workshop Notes | `workshop-notes` | Elicitation session output | Core team |
| Process Map | `process-map` | AS-IS / TO-BE visualization | Business, BA |
| Traceability Matrix | `traceability` | Req → story → test mapping | BA, QA, PM |
| Test Scenario | `test-scenario` | UAT execution script | Business, QA |
| Decision Log | `decision-log` | Recorded decisions with rationale | Steering, Architect |
| RAID Log | `raid` | Risks, assumptions, issues, dependencies | PM, Steering |
| Data Dictionary | `data-dictionary` | Field-level definitions | BA, Admin, Integration |
| Release Notes | `release-notes` | What shipped per release | All stakeholders |

## When to Use Which

```
Discovery complete?
    → BRD (business requirements)
    → Process maps (if process transformation)

Solution shaping?
    → Fit-gap analysis
    → Decision log for key forks

Agile delivery?
    → Epics → User stories
    → Traceability matrix (maintain continuously)

Pre-go-live?
    → Test scenarios
    → Release notes
```

## Agent Default Selection

| User asks for... | Default type |
|------------------|--------------|
| "requirements document" | `brd` |
| "stories for sprint" | `user-story` |
| "can Salesforce do X" | `fit-gap` |
| "workshop output" | `workshop-notes` |
| "UAT scripts" | `test-scenario` |

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

- **Previous:** [Consulting Principles](consulting-principles.md)
- **Next:** [Enterprise Standards](enterprise-standards.md)
- **See Also:** [cross-linking-framework](../docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
