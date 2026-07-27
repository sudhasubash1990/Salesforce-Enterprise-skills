---
title: Error Handling
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.22.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [omnistudio-qa, knowledge]
---

# Error Handling

## Purpose

Validate user-visible and orchestration error paths.

## Reasoning Model

1. Map validation, remote, and system errors to UX messages.
2. Confirm IP failure branches and OS catch paths.
3. Ensure no silent data loss on partial failure.
4. Document retry vs fail-fast policy.

## Decision Rules

- Happy path only → Fail Negative Test Scenarios gate.

## Cross-Links (Canonical Depth)

- [Integration Procedures](integration-procedures.md)
- [OmniScript Design](omniscript-design.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.22.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
