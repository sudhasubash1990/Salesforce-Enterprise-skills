---
title: Project Memory Contract
version: 0.3.0
tags: [framework-core, memory]
status: draft
last_updated: 2026-10-09
---

# Project Memory Contract

> **Alias:** Spec path `memory/PROJECT-MEMORY-CONTRACT.md`. Complements root [PROJECT_CONTEXT.md](../../PROJECT_CONTEXT.md) (human-readable summary). Structured state lives locally under `outputs/<project>/project-memory.yaml` — **MUST NOT** commit client-sensitive data to the public repository.

## Purpose

Treat project memory as structured state, not as an uncontrolled conversation transcript.

## Schema

```yaml
project_memory:
  project_code: <anonymized>
  status: draft | active | archived
  approved_decisions: []
  requirements: []
  assumptions: []
  open_questions: []
  solution_decisions: []
  test_decisions: []
  rejected_options: []
  superseded_items: []
  provenance: []
```

### Mutable item shape

Every mutable item **MUST** have an ID and status:

```yaml
- id: DEC-001
  statement: <decision or item text>
  status: proposed | approved | rejected | superseded | open
  provenance: [E-001]   # evidence or source refs
  supersedes: []        # prior item IDs when replacing
  superseded_by: null
  last_updated: YYYY-MM-DD
```

## Normative rules

1. Every mutable item **MUST** have a unique `id` and `status`.
2. Approved decisions **MUST** override obsolete drafts for agent reasoning, while retaining supersession history (`supersedes` / `superseded_by`).
3. Memory entries **MUST** include provenance (or an explicit unknown) and **MUST NOT** silently overwrite conflicting facts — surface conflict per [../grounding/conflict-resolution.md](../grounding/conflict-resolution.md).
4. Class D/G sensitive task content **MUST NOT** persist into project memory by default. See [../orchestration/context-policy.md](../orchestration/context-policy.md).
5. Public examples **MUST** use synthetic / anonymized data only. See [../../examples/project-memory.example.yaml](../../examples/project-memory.example.yaml).
6. [PROJECT_CONTEXT.md](../../PROJECT_CONTEXT.md) **MAY** mirror a short approved subset for agent efficiency; the YAML file is the structured source of truth when both exist.

## Relationship to context classes

| Memory bucket | Context class when loaded |
|---------------|---------------------------|
| `approved_decisions`, `solution_decisions`, `test_decisions` | **C** (project) |
| `assumptions`, `open_questions` | **C** + grounding envelope |
| `rejected_options`, `superseded_items` | **C** (historical; do not treat as current fact) |
| `provenance` | Links to Class **E** evidence |

## Related Documents

- [../orchestration/context-engineering-contract.md](../orchestration/context-engineering-contract.md)
- [../grounding/uncertainty-records.md](../grounding/uncertainty-records.md)
- [../../.cursor/rules/project-context.mdc](../../.cursor/rules/project-context.mdc)
