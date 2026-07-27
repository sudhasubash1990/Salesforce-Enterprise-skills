---
title: Metadata Impact Analyzer — Tests
module: Salesforce Quality Engineering
category: Specialized Skill Test
document_type: Guide
version: 0.15.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [metadata-impact-analyzer, test-index]
---

# Metadata Impact Analyzer — Validation Tests

## Purpose

Manual and agent regression scenarios verifying structured output and analysis discipline.

## How to Run

1. Load [../SKILL.md](../SKILL.md) and [../prompts/impact-analysis.md](../prompts/impact-analysis.md).
2. Execute each `scenario-*.md` with matching [../examples/](../examples/README.md) fixture.
3. Record Pass/Partial/Fail in a test log under `outputs/<project>/`.

## Scenarios

| Scenario | Focus |
|----------|-------|
| [dependency-before-tests](scenario-dependency-before-tests.md) | Section ordering |
| [sixteen-sections](scenario-sixteen-sections.md) | Completeness |
| [risk-evidence](scenario-risk-evidence.md) | Risk discipline |
| [custom-field](scenario-custom-field.md) | Field dependencies |
| [security-profile](scenario-security-profile.md) | Profile risk |
| [integration-vr](scenario-integration-vr.md) | VR + API |
