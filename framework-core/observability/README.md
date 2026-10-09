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

## Rules (summary)

- Agents **MUST NOT** store hidden chain-of-thought or unnecessary sensitive Class D/G task content in traces.
- Default retention is session-only unless project policy requests an audit copy under `outputs/<project>/`.

## Related Documents

- [../orchestration/execution-state-model.md](../orchestration/execution-state-model.md)
- [../responsible-ai/privacy-and-data-handling.md](../responsible-ai/privacy-and-data-handling.md)
- [../security/secrets-and-data-handling.md](../security/secrets-and-data-handling.md)

## Navigation

- **Up:** [../README.md](../README.md)
