---
title: Observability
version: 0.3.0
tags: [framework-core, observability]
status: draft
last_updated: 2026-10-09
---

# Observability

## Purpose

Make important agent decisions explainable without exposing hidden chain-of-thought. Store concise decision records, evidence references, and tool outcomes.

## Documents

| Document | Role |
|----------|------|
| [trace-contract.md](trace-contract.md) | Normative trace fields, redaction, retention |
| [trace-schema.yaml](trace-schema.yaml) | Machine-readable schema |

## When to emit traces

| Audience | Behavior |
|----------|----------|
| Maintainer / debug / evaluation | Emit full trace including optional `context_bundles`, `routing_outcome`, `unresolved_unknowns`, `human_review_triggers` |
| Normal BA/QE business deliverable | Do **not** paste internal routing/context dumps into the artifact unless the user asks for diagnostics |

## Rules (summary)

- Agents **MUST NOT** store hidden chain-of-thought or unnecessary sensitive Class D/G task content in traces.
- Default retention is session-only unless project policy requests an audit copy under `outputs/<project>/`.
- Required fields remain stable; optional diagnostic fields are additive (see [trace-schema.yaml](trace-schema.yaml)).

## Related Documents

- [../orchestration/execution-state-model.md](../orchestration/execution-state-model.md)
- [../responsible-ai/privacy-and-data-handling.md](../responsible-ai/privacy-and-data-handling.md)
- [../security/secrets-and-data-handling.md](../security/secrets-and-data-handling.md)

## Navigation

- **Up:** [../README.md](../README.md)
