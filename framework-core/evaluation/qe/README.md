---
title: QE Evaluation Index
version: 0.3.0
tags: [framework-core, evaluation, qe]
status: draft
last_updated: 2026-10-09
---

# QE Evaluation Index

Pointer index for QE-focused AI reliability and module regression. Does **not** duplicate QE Sprint 11 validation packs.

## Core reliability scenarios

| ID | Suite | Fixture / pointer |
|----|-------|-------------------|
| ROUTE-001 | routing | `scripts/test_retrieve_context.py` |
| TOOL-001 | tool_safety | [../../security/fixtures/retrieved-create-work-item.md](../../security/fixtures/retrieved-create-work-item.md) |
| PRIV-001 | privacy | [../fixtures/priv-001-sensitive-fields.md](../fixtures/priv-001-sensitive-fields.md) |
| CTX-001 | context | [../fixtures/ctx-001-wrong-project.md](../fixtures/ctx-001-wrong-project.md) |

Catalog: [../ai-reliability-scenarios.yaml](../ai-reliability-scenarios.yaml).

## Module regression

- [../../../salesforce-quality-engineering/validation/regression-suite/README.md](../../../salesforce-quality-engineering/validation/regression-suite/README.md)
- QE validation: [../../../salesforce-quality-engineering/validation/README.md](../../../salesforce-quality-engineering/validation/README.md)

## Cross-module

- [../cross-module/](../cross-module/) — BA → QE handoff
