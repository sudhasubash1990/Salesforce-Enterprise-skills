---
title: Naming Conventions
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
keywords: [naming conventions]
tags: [naming-conventions]
---

# Naming Conventions

## Files and Folders

| Element | Convention | Example |
|---------|------------|---------|
| Folders | lowercase, hyphen-separated | `salesforce-business-analyst` |
| Markdown files | lowercase, hyphen-separated | `fit-gap-analysis.md` |
| Templates | `<artifact>-template.md` | `brd-template.md` |
| Scenarios | `<industry-or-domain>.md` | `financial-services.md` |

## Requirement IDs

| Prefix | Meaning | Example |
|--------|---------|---------|
| `BR-` | Business requirement | BR-001 |
| `FR-` | Functional requirement | FR-014 |
| `NFR-` | Non-functional requirement | NFR-003 |
| `CR-` | Compliance/regulatory | CR-002 |
| `US-` | User story | US-042 |
| `TS-` | Test scenario | TS-018 |
| `EP-` | Epic | EP-005 |

Number sequentially within project; zero-pad to 3 digits.

## Salesforce Artifacts

| Artifact | Convention |
|----------|------------|
| Custom objects | `ObjectName__c` — PascalCase |
| Custom fields | `Field_Name__c` — describe business meaning in BRD |
| Record types | Match business process name |
| Flows | `Object_Action_Purpose` |
| Permission sets | `PS_Function_Role` |

Document API names in a glossary table when introduced in requirements.

## Project Codes (Examples)

Use fictional codes: `PRJ-ACME-001`, `PRJ-SUMMIT-HLS-002`

## Branch and Tag Names

See [branching-strategy.md](branching-strategy.md) and [versioning.md](versioning.md).

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

- **Previous:** [Metadata Schema](metadata-schema.md)
- **Next:** [Quality Framework](quality-framework.md)
- **See Also:** [cross-linking-framework](cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
