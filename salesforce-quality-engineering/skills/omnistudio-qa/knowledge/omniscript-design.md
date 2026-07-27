---
title: OmniScript Design
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

# OmniScript Design

## Purpose

Validate OmniScript navigation, conditionals, Data JSON, and submit paths.

## Reasoning Model

1. Walk steps, conditional views, and required fields.
2. Validate Save for Later / resume and error messaging.
3. Inspect Data JSON shape at key transitions.
4. Confirm submit/IP handoff and user feedback.

## Decision Rules

- Step-click only without JSON/submit → Fail Functional Validation.
- Missing Save for Later when required → Edge gap.

## Cross-Links (Canonical Depth)

- [OmniStudio Cloud Knowledge](../../knowledge/clouds/omnistudio.md)
- [JSON Structure](json-structure.md)
- [Playwright Review](../../playwright-review/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.22.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
