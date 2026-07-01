---
title: Relationship Matrix
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
keywords: [relationship matrix]
tags: [relationship-matrix]
---

# Relationship Matrix

Document-to-document relationship rules for the enterprise knowledge graph (Sprint 7).

## Primary Relationships

| Document | Upstream | Downstream |
|----------|----------|------------|
| BRD | Discovery outputs, workshops | FRD, fit-gap, epics |
| FRD | BRD | User stories, integration specs |
| User Story | Epic, FR, BR | Acceptance criteria |
| Acceptance Criteria | User story | Test scenarios |
| Test Scenario | Acceptance criteria | RTM |
| RTM | Requirements, tests | Deployment checklist |
| Deployment Checklist | RTM, release plan | Production validation |

## Cross-Module Relationships

| Source category | Typically links to |
|-----------------|-------------------|
| Brain | Knowledge (depth), templates (output), playbooks (method) |
| Knowledge | Brain (reasoning), templates, playbooks, scenarios |
| Templates | Knowledge, playbooks, brain/output-framework |
| Playbooks | Knowledge, templates, scenarios |
| Scenarios | Knowledge, playbooks, templates, interview-guide |
| Interview Guide | Brain, knowledge, templates, playbooks, scenarios |

## Interview Topic Mapping (inverse)

| Knowledge / domain | Interview topics |
|--------------------|------------------|
| requirement-types, requirement-elicitation | requirement-gathering.md |
| current-state-analysis, process-mapping | current-state.md |
| future-state-design | future-state.md |
| user-stories, backlog-management | user-stories.md |
| acceptance-criteria | acceptance-criteria.md |
| stakeholder-analysis | stakeholders.md |
| salesforce-clouds-overview, salesforce-platform | salesforce/crm.md |
| sales-cloud, lead-to-cash | sales-cloud.md |
| service-cloud, case-management | service-cloud.md |
| experience-cloud | experience-cloud.md |
| cpq-fundamentals | salesforce/cpq.md |
| industry-patterns | salesforce/industries.md |
| integration-patterns, security-model | delivery/architecture.md |
| agile-fundamentals, safe-awareness | delivery/agile.md |
| scrum-fundamentals | delivery/scrum.md |
| risk-management, raid-management | delivery/risk-management.md |
| executive-communication | delivery/communication.md, advanced/executive-communication.md |
| change-management, governance-framework | delivery/leadership.md |
| business-analysis-fundamentals, babok-guide | business-analysis.md |

## Peer Document Rules

- Templates for the same deliverable family are peers (e.g., brd-template ↔ frd-template)
- Playbooks in the same phase are peers (discovery ↔ requirement workshop)
- Scenarios in the same industry folder are peers

## Governance Documents

| Document | Role |
|----------|------|
| docs/metadata-schema.md | Metadata standard |
| docs/cross-linking-framework.md | Linking rules |
| shared/traceability-model.md | End-to-end traceability |
| shared/relationship-matrix.md | This matrix |

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

- **Previous:** [Output Standards](output-standards.md)
- **Next:** [Reusable Components](reusable-components.md)
- **See Also:** [cross-linking-framework](../docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
