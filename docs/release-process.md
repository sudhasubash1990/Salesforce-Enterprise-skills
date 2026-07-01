---
title: Release Process
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
keywords: [release process]
tags: [release-process]
---

# Release Process

## Release Cadence

- **PATCH**: as needed for corrections
- **MINOR**: monthly or when a meaningful skill/playbook pack is ready
- **MAJOR**: rare; breaking schema or skill restructuring

## Release Checklist

### Pre-Release

- [ ] All merged PRs documented in `CHANGELOG.md`
- [ ] Version bumped in relevant `skill.md` files
- [ ] `salesforce-business-analyst/changelog.md` updated
- [ ] Links validated (no broken relative paths)
- [ ] No confidential or client-specific content
- [ ] ROADMAP.md reflects completed items

### Release Steps

1. Create PR: `release/<version>` or release directly from `main`
2. Final review by repository maintainer
3. Merge to `main`
4. Tag: `git tag v0.x.x`
5. Push tag (when remote configured)
6. Update ROADMAP checkboxes

### Post-Release

- Announce in team channel / internal wiki
- Capture feedback for next MINOR

## Version Number Assignment

| Change Type | Version Bump |
|-------------|--------------|
| New industry scenario | MINOR |
| New template or playbook | MINOR |
| Skill description or routing update | MINOR |
| Typo fix in examples | PATCH |
| Remove or restructure skill entry point | MAJOR |

## Rollback

Revert commit on `main` and tag PATCH with fix note. Do not delete tags.

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

- **Previous:** [Quality Framework](quality-framework.md)
- **Next:** [Repository Guidelines](repository-guidelines.md)
- **See Also:** [cross-linking-framework](cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
