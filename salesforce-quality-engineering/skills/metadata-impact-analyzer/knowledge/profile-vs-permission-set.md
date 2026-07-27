---
title: Profile vs Permission Set
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

# Profile vs Permission Set

## Purpose

Apply least-privilege analysis when profiles or permission sets change.

## Reasoning Model

1. Prefer permission set delta analysis over full profile rewrites.
2. Document which permissions moved between profile and permission set.
3. Identify users affected via PermissionSetAssignment queries.
4. Flag View All / Modify All / Author Apex as exceptional permissions.

## Decision Rules

- Profile narrowing → verify no business process breakage for standard users.
- Permission set expansion → security review required before deploy.

## Cross-Links (Canonical Depth)

- [Security Knowledge](../../knowledge/security/README.md)
- [Permission Set Testing](../../knowledge/permission-set-testing.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)
- [../../knowledge/metadata/README.md](../../knowledge/metadata/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial specialized skill knowledge |
