---
title: Cross Linking Framework
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
keywords: [cross linking framework]
tags: [cross-linking-framework]
---

# Enterprise Cross-Linking Framework

Sprint 7 governance for repository-wide document relationships and AI retrieval optimization.

## Purpose

Transform isolated Markdown files into a **connected enterprise knowledge graph** where every document participates in traceability and references canonical artifacts.

## Mandatory Document Sections

Every Markdown document (except justified exceptions) shall end with these sections in order:

1. **Related Brain Modules**
2. **Related Knowledge**
3. **Related Templates**
4. **Related Playbooks**
5. **Related Industry Scenarios**
6. **Related Interview Topics**
7. **Related Examples**
8. **Related Documents**

Optional when applicable:

- **Traceability** (upstream / downstream / validation artifacts)
- **Navigation** (Previous / Next / See Also)
- **Version History**

### Justified Exceptions

| Document type | Omitted sections | Justification |
|---------------|------------------|---------------|
| `CHANGELOG.md` | Related sections | Version log, not domain knowledge |
| Redirect stubs | Partial | Points to canonical document |

Use `N/A — [reason]` only when a section truly has no logical relationships.

## Linking Standards

- Use **relative** Markdown links only
- Link to files, not line anchors (unless citing code)
- Avoid duplicate references in the same section
- Reference canonical documents—do not duplicate foundational knowledge

Example:

```markdown

## Knowledge Graph Rules

Each document should identify relationships:

| Relationship | Meaning |
|--------------|---------|
| Parent | Governing or containing document |
| Child | Detailed derivative |
| Peer | Same tier, complementary topic |
| Supporting | Reference depth (knowledge, templates) |
| Governance | Standards, schema, architecture |

Avoid circular duplication: interview questions reference knowledge articles; knowledge articles reference interview topics for assessment—not full question text.

## Metadata Requirements

All documents use Sprint 7 YAML per [metadata-schema.md](metadata-schema.md).

Key relationship fields:

```yaml
related_brain_modules: [file.md]
related_knowledge: [file.md]
related_templates: [file.md]
related_playbooks: [file.md]
related_scenarios: [path/file.md]
related_interview_topics: [path/file.md]
related_examples: [path/file.md]
related_documents: [path/file.md]
```

Legacy hyphenated fields (`document-type`, `last-reviewed`) are normalized to `document_type`, `last_updated`, `review_status` during enrichment.

## Review Workflow

```
Draft → Peer Review → Technical Review → Business Review → Approved → Release → Maintenance → Archive
```

`review_status` values: `Draft`, `Review`, `Approved`, `Deprecated`, `Archived`.

## AI Retrieval Optimization

Documents shall:

- Focus on one primary topic
- Use predictable H2/H3 headings
- Reference canonical sources instead of repeating content
- Include `keywords` and `tags` in metadata
- Keep entry orchestrators (skill.md, README indexes) under ~500 lines

Agents should load **Related** sections from the current document before generating deliverables.

## Navigation Blocks

Index and sequential documents include:

```markdown

## Quality Gates

Before approval:

- [ ] Metadata complete per schema
- [ ] All mandatory Related sections populated or justified
- [ ] Relative links resolve
- [ ] Version History present
- [ ] No duplicate canonical content
- [ ] `scripts/validate_metadata.py` passes

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

- **Previous:** [Continuous Knowledge Management](continuous-knowledge-management.md)
- **Next:** [Markdown Standards](markdown-standards.md)
- **See Also:** [cross-linking-framework](cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
