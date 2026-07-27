---
title: Calculation Procedures
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

# Calculation Procedures

## Purpose

Validate Calculation Procedures/Matrices for pricing and scoring journeys.

## Reasoning Model

1. Map inputs, steps, and output fields.
2. Verify calculation accuracy with known fixtures (TDG).
3. Cover zero/null/overflow edges.
4. Do not invent formula results — use provided expected values.

## Decision Rules

- No expected calc fixtures → Block accuracy claims.
- CPQ/EPC calc change → Expand Regression Scope.

## Cross-Links (Canonical Depth)

- [Expression Sets](expression-sets.md)
- [Test Data Generator](../../test-data-generator/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.22.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
