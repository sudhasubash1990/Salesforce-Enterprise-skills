---
title: Trace Viewer
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.21.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [playwright-review, knowledge]
---

# Trace Viewer

## Purpose

Ensure traces/screenshots/video support triage.

## Reasoning Model

1. Traces on failure in CI.
2. Retention policy documented.
3. PII in traces — scrub or restrict access.
4. Link reporting observability.

## Decision Rules

- No artifacts on CI fail → CI/CD gap.

## Cross-Links (Canonical Depth)

- [Tracing](../../automation-intelligence/playwright/tracing.md)
- [Reporting and Observability](../../automation-intelligence/review-engine/reporting-observability.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
