---
title: Deployment Best Practices
module: Salesforce Quality Engineering
category: Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.15.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [metadata-impact-analyzer, knowledge]
---

# Deployment Best Practices

## Purpose

Apply QE deployment validation patterns before production promotion.

## Reasoning Model

1. Validate deployment manifest completeness vs dependency graph.
2. Confirm test execution evidence in target sandbox.
3. Check deployment window, rollback plan, and post-deploy smoke scope.
4. Align with release train and change advisory board requirements.

## Decision Rules

- Missing dependency in package → Fail deployment readiness.
- No rollback story for data model change → No-Go until documented.

## Cross-Links (Canonical Depth)

- [Deployment Considerations](../../knowledge/metadata/deployment-considerations.md)
- [Release Readiness](../../knowledge/release/release-readiness.md)
- [Metadata Validation](../../knowledge/metadata/metadata-validation.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)
- [../../knowledge/metadata/README.md](../../knowledge/metadata/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial specialized skill knowledge |
