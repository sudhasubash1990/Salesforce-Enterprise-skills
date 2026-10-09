---
title: BA Evaluation Index
version: 0.3.0
tags: [framework-core, evaluation, ba]
status: draft
last_updated: 2026-10-09
---

# BA Evaluation Index

Pointer index for BA-focused AI reliability and module golden scenarios. Does **not** duplicate BA validation packs.

## Core reliability scenarios

| ID | Suite | Fixture / pointer |
|----|-------|-------------------|
| GRD-001 | grounding | [../fixtures/grd-001-grounding-assumption.md](../fixtures/grd-001-grounding-assumption.md) |
| CONF-001 | conflict | [../fixtures/conf-001-conflicting-requirements.md](../fixtures/conf-001-conflicting-requirements.md) |
| HALL-001 | hallucination | [../fixtures/hall-001-invented-sla.md](../fixtures/hall-001-invented-sla.md) |

Catalog: [../ai-reliability-scenarios.yaml](../ai-reliability-scenarios.yaml).

## Module golden / benchmark

- [../../../salesforce-business-analyst/validation/benchmark-scenarios.md](../../../salesforce-business-analyst/validation/benchmark-scenarios.md)
- BA validation pack: [../../../salesforce-business-analyst/validation/README.md](../../../salesforce-business-analyst/validation/README.md)

## Cross-module

- [../cross-module/](../cross-module/) — BA → QE handoff
