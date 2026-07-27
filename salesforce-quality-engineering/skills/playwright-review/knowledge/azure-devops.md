---
title: Azure DevOps Pipelines
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

# Azure DevOps Pipelines

## Purpose

Review ADO YAML for Playwright jobs and Test Plans linkage.

## Reasoning Model

1. Check pool, Node version, cache.
2. Publish HTML/JUnit.
3. Variable groups for secrets.
4. Do not invent ADO publish API unless requested.

## Decision Rules

- Hardcoded PAT in YAML → Critical Security.

## Cross-Links (Canonical Depth)

- [CI/CD Integration](cicd-integration.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
