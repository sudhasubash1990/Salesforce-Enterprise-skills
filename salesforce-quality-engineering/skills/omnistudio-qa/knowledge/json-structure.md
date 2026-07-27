---
title: JSON Structure
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

# JSON Structure

## Purpose

Validate OmniScript Data JSON and IP response JSON contracts.

## Reasoning Model

1. Define expected keys at step boundaries.
2. Validate types, arrays, and nested nodes.
3. Detect orphan keys and overwrite collisions.
4. Recommend TDG seed JSON for repeatable tests.

## Decision Rules

- Missing JSON Validation section when OS in scope → Fail quality gate.

## Cross-Links (Canonical Depth)

- [OmniScript Design](omniscript-design.md)
- [Test Data Generator](../../test-data-generator/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.22.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
