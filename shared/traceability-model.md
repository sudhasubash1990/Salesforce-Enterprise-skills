---
title: Traceability Model
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
keywords: [traceability model]
tags: [traceability-model]
---

# Traceability Model

End-to-end requirement and delivery traceability for Salesforce enterprise programs.

## Traceability Chain

```
Business Requirement
        │
        ▼
Current State
        │
        ▼
Future State
        │
        ▼
Gap Analysis
        │
        ▼
Capability Assessment
        │
        ▼
Epic
        │
        ▼
Feature
        │
        ▼
User Story
        │
        ▼
Acceptance Criteria
        │
        ▼
Test Scenario
        │
        ▼
Test Case
        │
        ▼
RTM (Requirements Traceability Matrix)
        │
        ▼
Deployment Checklist
        │
        ▼
Production Validation
        │
        ▼
Lessons Learned
```

## Artifact Traceability by Document Category

| Category | Upstream artifacts | Downstream artifacts | Validation artifacts |
|----------|-------------------|---------------------|---------------------|
| Brain | Governance, consulting principles | Knowledge, playbooks, templates | validation-framework.md |
| Knowledge | Brain modules | Templates, playbooks, scenarios | checklists.md |
| Template | Knowledge, brain | Playbooks, deliverables | validation-framework.md |
| Playbook | Knowledge, templates | Scenarios, deliverables | checklists.md |
| Scenario | Knowledge, playbooks | Interview topics, BRD examples | fit-gap outputs |
| Interview | Brain, knowledge, scenarios | Candidate assessment | scorecard / rubric |
| Governance | — | All categories | validate_metadata.py |

## Forward Traceability

Every business requirement should trace forward to:

1. Functional requirements (if separated)
2. Fit-gap classification
3. Epic / feature / user story
4. Acceptance criteria
5. Test scenarios
6. RTM row
7. Deployment and production validation

## Backward Traceability

Every user story and test scenario should trace backward to:

1. Parent epic or feature
2. Business requirement ID
3. Source (workshop, regulation, assumption)
4. Stakeholder owner

## Validation Artifacts

| Gate | Artifact | Owner |
|------|----------|-------|
| Requirements complete | BRD/FRD sign-off | Business Owner |
| Backlog ready | Refined stories + AC | Product Owner / BA |
| Build complete | Unit/integration test results | Dev lead |
| UAT complete | Test scenarios + defects closed | BA / QA |
| Go-live | Deployment checklist | Release manager |
| Post-go-live | Benefits / adoption metrics | Sponsor |

## Repository Mapping

| Delivery artifact | Repository template |
|-------------------|---------------------|
| BRD | templates/brd-template.md |
| FRD | templates/frd-template.md |
| User story | templates/user-story-template.md |
| RAID | templates/raid-log-template.md |
| RTM | templates/traceability-matrix-template.md |
| Deployment | templates/deployment-checklist-template.md |

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

- **Previous:** [Taxonomy](taxonomy.md)
- **Next:** —
- **See Also:** [cross-linking-framework](../docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
