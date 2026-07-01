---
title: Versioning
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
keywords: [versioning]
tags: [versioning]
---

# Versioning

## Repository Versioning

Follows [Semantic Versioning](https://semver.org/):

| Bump | When |
|------|------|
| **MAJOR** | Breaking changes to skill interfaces, removed playbooks, schema changes |
| **MINOR** | New playbooks, scenarios, templates, backward-compatible skill additions |
| **PATCH** | Typos, clarifications, non-structural example updates |

Document all changes in root `CHANGELOG.md`.

## Skill Versioning

Each skill maintains its own version in `skill.md` frontmatter and `changelog.md`.

Skill version is independent of repository version but should be noted in root CHANGELOG on releases.

## Document Versioning

Deliverables generated from templates:

- Start at `0.1.0` in draft
- Move to `1.0.0` on formal approval
- Increment MINOR for added sections; PATCH for corrections

## Git Tags

```
v0.1.0          # Repository release
ba-v0.2.0       # Skill-specific tag (optional)
```

## Deprecation Policy

- Announce deprecation one MINOR release ahead
- Mark `status: deprecated` in frontmatter
- Provide migration notes in CHANGELOG

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

- **Previous:** [Security Guidelines](security-guidelines.md)
- **Next:** [Vision](vision.md)
- **See Also:** [cross-linking-framework](cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
