---
title: Failure and Retry Policy
version: 0.2.0
tags: [framework-core, tools]
status: draft
last_updated: 2026-10-09
---

# Failure and Retry Policy

## Purpose

Define timeout, retry, idempotency, and audit expectations for governed tools.

## Normative rules

1. Agents **MUST** surface the actual tool error on failure; they **MUST NOT** invent success IDs (e.g., fabricated ADO work item IDs).
2. Agents **SHOULD** retry only when the operation is known idempotent or the retry policy explicitly allows it.
3. Agents **MUST NOT** auto-retry T3+ writes when success is unknown (timeout without confirmation).
4. Timeout behavior **MUST** be documented in the tool manifest (`timeout_or_failure_behavior`).
5. Audit fields for T2+ **SHOULD** include tool name, risk tier, actor, timestamp, input summary, and result or error.
6. After exhausted retries, agents **MUST** stop mutation attempts and report failure with residual risk.

## Idempotency guidance

| Class | Retry |
|-------|-------|
| idempotent | Safe to retry with same inputs |
| conditional | Retry only with explicit confirmation / key check |
| non-idempotent | No automatic retry |
| unknown | Treat as non-idempotent |

## Related Documents

- [tool-governance.md](tool-governance.md)
- [tool-manifest-schema.yaml](tool-manifest-schema.yaml)
- [action-risk-model.md](action-risk-model.md)
