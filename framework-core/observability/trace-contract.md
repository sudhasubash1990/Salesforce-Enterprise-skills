---
title: Trace Contract
version: 0.3.0
tags: [framework-core, observability, audit]
status: draft
last_updated: 2026-10-09
---

# Trace Contract

## Purpose

Define the minimum decision/audit trace for SEACF agent runs without storing private reasoning traces.

## Schema (required fields)

```yaml
trace_id:
request_class:
selected_skills: []
evidence_ids: []
assumptions: []
policy_decisions: []
tool_events: []
approval_events: []
validation_results: []
output_artifacts: []
status:
```

Machine schema: [trace-schema.yaml](trace-schema.yaml).

## Field guidance

| Field | Content |
|-------|---------|
| `trace_id` | Unique run identifier |
| `request_class` | Discipline/capability (e.g., BA user-story, QE test-strategy) |
| `selected_skills` | Skill paths activated |
| `evidence_ids` | Claim/evidence IDs or locators used |
| `assumptions` | Recorded assumptions (IDs or short text) |
| `policy_decisions` | Major precedence, fit-gap, risk-tier, or routing decisions |
| `tool_events` | Tool name, risk tier, outcome (success/fail/blocked) |
| `approval_events` | Approval requested/granted/denied |
| `validation_results` | Validator name, pass/fail |
| `output_artifacts` | Paths or IDs of delivered artifacts |
| `status` | Execution-state name: `COMPLETED` or `FAILED_SAFELY` (see [execution-state-model.md](../orchestration/execution-state-model.md)) |

## Normative rules

1. Agents **MUST** record request identity, selected skills, evidence IDs, major policy decisions, assumptions, tool call outcomes, approval state, validation results, and final artifact IDs when a trace is produced.
2. Agents **MUST NOT** store hidden chain-of-thought or private step-by-step reasoning traces.
3. Agents **MUST NOT** store unnecessary sensitive Class D/G task content; apply redaction (`redacted`) or omit.
4. Default retention **MUST** be in-session only. Persist under `outputs/<project>/` **only** when the user or project policy requests an audit copy.
5. Trace redaction and retention policies **MUST** align with [../responsible-ai/privacy-and-data-handling.md](../responsible-ai/privacy-and-data-handling.md) and [../security/secrets-and-data-handling.md](../security/secrets-and-data-handling.md).
6. `status` **MUST** use execution-state names from [../orchestration/execution-state-model.md](../orchestration/execution-state-model.md).

## Runtime note

This increment defines the contract and schema only. A persistent trace collector service is deferred.

## Related Documents

- [README.md](README.md)
- [trace-schema.yaml](trace-schema.yaml)
- [../orchestration/context-policy.md](../orchestration/context-policy.md)
