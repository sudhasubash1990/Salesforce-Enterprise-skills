---
title: Quality Framework
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
keywords: [quality framework]
tags: [quality-framework]
---

# Quality Framework

Quality dimensions and gates for repository content and generated deliverables.

## Quality Dimensions

| Dimension | Definition | Weight |
|-----------|------------|--------|
| **Accuracy** | Technically and business-correct for Salesforce | 25% |
| **Completeness** | All required sections and metadata present | 20% |
| **Traceability** | IDs link across BRD → stories → tests | 20% |
| **Clarity** | Unambiguous, testable language | 20% |
| **Consistency** | Terminology and format match standards | 15% |

## Content Quality Gates

### Gate 1: Author Self-Review

- [ ] Frontmatter complete
- [ ] Follows markdown standards
- [ ] No PII or client identifiers
- [ ] Terminology matches glossary

### Gate 2: Peer Review

- [ ] BA peer review for skill/playbook changes
- [ ] Maintainer review for governance changes
- [ ] At least one worked example updated if template changed

### Gate 3: Pilot Validation (for MAJOR/MINOR skill releases)

- [ ] Used on at least one anonymized engagement scenario
- [ ] Feedback incorporated

## Deliverable Quality Rubric (Generated Artifacts)

### BRD Requirements

| Score | Criteria |
|-------|----------|
| Pass | Outcome stated, uniquely ID'd, prioritized, sourced |
| Fail | Screen specification without business rule; duplicate IDs |

### User Stories

| Score | Criteria |
|-------|----------|
| Pass | INVEST; 3+ acceptance criteria; refs to BR/FR |
| Fail | Epic-sized; no testable criteria; missing role/benefit |

### Fit-Gap

| Score | Criteria |
|-------|----------|
| Pass | Each gap has classification, recommendation, owner |
| Fail | "Custom" without exploring standard alternatives |

## Continuous Improvement

- Track defect categories from pilot programs
- Quarterly review of checklists and rubrics
- Update scenarios when Salesforce seasonal releases change standard capabilities

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

- **Previous:** [Naming Conventions](naming-conventions.md)
- **Next:** [Release Process](release-process.md)
- **See Also:** [cross-linking-framework](cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
