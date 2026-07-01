---
title: Markdown Standards
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
keywords: [markdown standards]
tags: [markdown-standards]
---

# Markdown Standards

Formatting standards for all repository content.

## Structure

1. Single H1 per file (the title)
2. Logical H2/H3 hierarchy—no skipped levels
3. Table of contents only for files > 200 lines

## Writing Style

- Active voice, present tense for instructions
- Second person for playbooks ("Review the stakeholder map")
- Third person for skill descriptions
- Short paragraphs (3–5 sentences max)
- Bullets for lists; numbered lists for sequences

## Code and Examples

- Fenced code blocks with language identifier
- Sample data clearly labeled as fictional
- No horizontal rules except in templates

## Tables

Use tables for:

- Comparison matrices (fit-gap, options)
- RACI mappings
- Traceability matrices

## Diagrams

- Prefer Mermaid for flowcharts in architecture and process docs
- ASCII diagrams acceptable for simple flows in plain-text contexts

## Links

```markdown
[Discovery Playbook](../salesforce-business-analyst/playbooks/discovery-playbook.md)
```

## Frontmatter

Every deliverable template starts with YAML frontmatter per [metadata-schema.md](metadata-schema.md).

## Prohibited

- HTML except in rare table formatting cases
- Embedded images without alt text (prefer Mermaid)
- ALL CAPS for emphasis (use bold sparingly)

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

- **Previous:** [Cross Linking Framework](cross-linking-framework.md)
- **Next:** [Metadata Schema](metadata-schema.md)
- **See Also:** [cross-linking-framework](cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
