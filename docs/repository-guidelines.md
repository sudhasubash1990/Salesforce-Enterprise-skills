---
title: Repository Guidelines
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
keywords: [repository guidelines]
tags: [repository-guidelines]
---

# Repository Guidelines

Standards for maintaining Salesforce Enterprise Skills.

## Repository Purpose

This is a **knowledge and skill repository**, not an application codebase. Primary artifacts are Markdown files, templates, and examples.

## Folder Ownership

| Folder | Owner Role | Change Frequency |
|--------|------------|------------------|
| `salesforce-business-analyst/` | BA Practice Lead | High |
| `shared/` | Enterprise Architecture / PMO | Medium |
| `docs/` | Repository Maintainers | Low–Medium |
| `.cursor/` | Agent Enablement Lead | Medium |
| `examples/` | BA + QA Leads | Medium |

## File Naming

- Lowercase with hyphens: `fit-gap-analysis.md`
- No spaces or underscores in filenames
- Templates suffix: `-template.md`
- Scenarios: industry or domain name

## Content Anonymization

All examples must:

- Use fictional company names (e.g., "Apex Manufacturing", "Summit Health")
- Use synthetic data for names, emails, account numbers
- Remove client-specific branding and proprietary process names

## Linking Convention

- Use relative links only
- Link from skill entry points one level deep into playbooks/templates
- Avoid circular links between governance docs

## Adding a New Skill

1. Create folder at repository root: `<skill-name>/`
2. Include minimum: `README.md`, `skill.md`, `checklists.md`
3. Register in root `README.md` and `.cursor/rules/routing.mdc`
4. Add entry to `ROADMAP.md` and `CHANGELOG.md`
5. Follow [metadata-schema.md](metadata-schema.md)

## Deprecation

Deprecated files move to a `deprecated/` subfolder with a redirect notice at the original path for one release cycle.

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

- **Previous:** [Release Process](release-process.md)
- **Next:** [Review Process](review-process.md)
- **See Also:** [cross-linking-framework](cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
