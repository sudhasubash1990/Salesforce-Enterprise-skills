---
title: Build Standards
module: Salesforce Business Analyst
category: Root
document_type: Framework
version: 1.3.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/README.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [docs/cross-linking-framework.md, ROADMAP.md]
keywords: [build standards]
tags: [build-standards, metadata, validation]
---

# Build Standards

Standards for generating, enriching, and merging repository content.

## Before You Add Content

1. Search for existing canonical documents — **extend, do not duplicate**
2. Read [docs/metadata-schema.md](../../docs/metadata-schema.md) and [docs/cross-linking-framework.md](../../docs/cross-linking-framework.md)
3. Identify the correct folder per [docs/architecture.md](../../docs/architecture.md)

## Metadata Enrichment

Run the enrichment script on new or updated Markdown:

```bash
python scripts/enrich_sprint_7_metadata.py
```

The script:

- Infers category from path (brain, knowledge, templates, playbooks, scenarios, interview-guide, validation)
- Adds mandatory Related sections, Traceability, Navigation, Version History
- Preserves `skill.md` agent frontmatter (`name`, `description`, `version`)

## Validation Before Merge

Run both validators:

```bash
python scripts/validate_metadata.py
python scripts/validate_repository.py
```

**Exit code 0** on `validate_repository.py` = enterprise-ready.

### Structure Checks (`validate_repository.py`)

Required BA directories: `brain/`, `knowledge/`, `templates/`, `playbooks/`, `scenarios/`, `interview-guide/`, `validation/`

Required files include `skill.md`, `validation/README.md`, `brain/validation-framework.md`

## Generator Patterns

| Generator | Purpose |
|-----------|---------|
| `scripts/generate_sprint_6_interview_guide.py` | Regenerate interview-guide topic files |
| `scripts/enrich_sprint_7_metadata.py` | Metadata and Related sections |
| `scripts/validate_metadata.py` | Link and section validation |
| `scripts/validate_repository.py` | Full repo health (Sprint 8+) |

When adding generators:

- Use repo-relative paths
- Document in this file and [design-decisions.md](design-decisions.md)
- Idempotent runs preferred

## Document Structure

Every enriched Markdown file should include:

1. YAML frontmatter per metadata schema
2. Primary content (H1 + sections)
3. `## Related *` sections (8 categories)
4. `## Traceability`
5. `## Navigation`
6. `## Version History`

## Naming

Follow [docs/naming-conventions.md](../../docs/naming-conventions.md) — lowercase kebab-case for files.

## Version Bumps

- Patch: typo fixes, link repairs
- Minor: new articles, templates, scenarios within existing sprints
- Major: new sprint modules, breaking structural changes

Update [skill.md](../skill.md) version, [changelog.md](../changelog.md), and root [CHANGELOG.md](../../CHANGELOG.md).

## Related Brain Modules

- [Readme](../brain/README.md)

## Related Knowledge

- [Readme](../knowledge/README.md)

## Related Templates

- [Readme](../templates/README.md)

## Related Playbooks

- [Readme](../playbooks/README.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [Interview Index](../interview-guide/interview-index.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Cross Linking Framework](../../docs/cross-linking-framework.md)
- [Roadmap](../../ROADMAP.md)

## Traceability

**Upstream:** — | **Downstream:** All skills | **Validation:** ROADMAP alignment

## Navigation

- **Previous:** [Readme](README.md)
- **Next:** [Design Decisions](design-decisions.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
