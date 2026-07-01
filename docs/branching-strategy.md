---
title: Branching Strategy
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
keywords: [branching strategy]
tags: [branching-strategy]
---

# Branching Strategy

Git branching model for Salesforce Enterprise Skills.

## Main Branches

| Branch | Purpose |
|--------|---------|
| `main` | Production-ready, tagged releases |
| `develop` | Integration branch (optional for larger teams) |

## Supporting Branches

| Type | Branch From | Merge To | Naming |
|------|-------------|----------|--------|
| Feature | `main` | `main` | `feature/<description>` |
| Fix | `main` | `main` | `fix/<description>` |
| Docs | `main` | `main` | `docs/<description>` |
| Skill | `main` | `main` | `skill/<skill>/<description>` |

## Workflow

1. Create branch from latest `main`
2. Make focused commits (one logical change per commit when possible)
3. Open PR with checklist from CONTRIBUTING.md
4. Squash merge preferred for feature branches
5. Tag release on `main` after CHANGELOG update

## Release Branches

For coordinated releases (optional):

```
release/0.2.0
```

Only bug fixes and changelog updates allowed on release branches.

## Hotfix

```
hotfix/<critical-fix>
```

Branch from `main`, merge back to `main`, tag PATCH release immediately.

## Protected Branch Rules (Recommended)

- `main`: require PR, 1 approval, passing checks (future)
- No force push to `main`

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

- **Previous:** [Architecture](architecture.md)
- **Next:** [Continuous Knowledge Management](continuous-knowledge-management.md)
- **See Also:** [cross-linking-framework](cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
