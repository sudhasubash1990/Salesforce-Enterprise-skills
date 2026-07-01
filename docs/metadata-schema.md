---
title: Metadata Schema
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
keywords: [metadata schema]
tags: [metadata-schema]
---

# Metadata Schema

YAML frontmatter schema for all generated and authored documents.

Sprint 7 extends Sprint 0–5 with enterprise cross-linking fields. See [cross-linking-framework.md](cross-linking-framework.md).

## Required Fields (All Documents)

```yaml
---
title: string                    # Human-readable document title
module: string                   # e.g., Salesforce Business Analyst
category: string                 # Brain | Knowledge | Template | Playbook | Scenario | Interview | Governance | Shared
document_type: string            # Knowledge Article | Playbook | Template | Guide | Framework | etc.
version: semver                  # e.g., 1.1.0
review_status: enum              # Draft | Review | Approved | Deprecated | Archived
owner: string                    # Responsible team or role
created_date: date                 # YYYY-MM-DD
last_updated: date                 # YYYY-MM-DD
---
```

## Relationship Fields (Sprint 7)

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

## Optional Fields

```yaml
author: string
project: string                  # Anonymized project code
tags: [string]
keywords: [string]
salesforce_cloud: string         # Or list as comma-separated
industry: string
business_domain: string
implementation_phase: string     # discovery | design | build | test | deploy
difficulty: string
review_cycle: string             # quarterly | semi-annual
parent_id: string                # Traceability to parent requirement/doc
reviewers: [string]
```

## Legacy Field Migration

| Legacy (Sprint 3–5) | Sprint 7 |
|---------------------|----------|
| `document-type` | `document_type` |
| `status: approved` | `review_status: Approved` |
| `last-reviewed` | `last_updated` |
| `type` (Sprint 0) | `document_type` |

Enrichment script `scripts/enrich_sprint_7_metadata.py` performs automatic migration.

## Skill File Schema (`skill.md`)

```yaml
---
name: salesforce-business-analyst    # lowercase-hyphen, max 64 chars
description: string                  # Third person, WHAT + WHEN, max 1024 chars
version: semver
---
```

## Requirement Schema (in BRDs)

Each requirement block:

```yaml
id: BR-001
priority: Must | Should | Could | Wont
category: Business | Functional | Non-Functional | Compliance
source: workshop | interview | regulation | assumption
status: proposed | approved | deferred | rejected
```

## User Story Schema

```yaml
id: US-042
epic: EP-005
requirement_refs: [BR-012, FR-003]
story_points: number | t-shirt
sprint: string | backlog
```

## Mandatory Footer Sections

See [cross-linking-framework.md](cross-linking-framework.md). Every document includes Related sections, Version History, and Navigation where applicable.

## Validation Rules

| Rule | Enforcement |
|------|-------------|
| Required YAML fields present | `scripts/validate_metadata.py` |
| `review_status` transitions follow workflow | Review process |
| `version` bump on material change | Contributor responsibility |
| Relative links resolve | `scripts/validate_metadata.py` |
| Related sections populated | `scripts/validate_metadata.py` |
| `description` in skills: third person | PR review |

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

- **Previous:** [Markdown Standards](markdown-standards.md)
- **Next:** [Naming Conventions](naming-conventions.md)
- **See Also:** [cross-linking-framework](cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
