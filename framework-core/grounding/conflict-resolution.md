---
title: Conflict Resolution
version: 0.2.0
tags: [framework-core, grounding]
status: draft
last_updated: 2026-10-09
---

# Conflict Resolution

## Purpose

Handle conflicting authoritative sources without silent selection or guessing.

## Normative rules

1. When two or more sources that are material to a conclusion disagree, agents **MUST** create an explicit conflict record.
2. Agents **MUST NOT** silently pick one conflicting source when both remain in scope and authoritative.
3. Agents **MUST** provide a clarification or escalation path for unresolved conflicts.
4. Agents **SHOULD** continue analysis on non-conflicting topics while flagging the conflict.

## Conflict record template

```yaml
conflict_id: CFG-001
topic: <short description>
sources:
  - source_id: <path-or-id>
    source_class: project-approved | official-product | seacf-approved | ...
    position: <summary of claim>
  - source_id: <path-or-id>
    source_class: ...
    position: <summary of claim>
conflict_status: conflicting | unresolved
impact: <delivery / compliance / scope impact>
escalation_path: <owner role or forum>
clarification_question: <single precise question>
```

## Escalation path

Default escalation owners (adjust per project RACI):

| Conflict type | Escalate to |
|---------------|-------------|
| Requirements conflict | Product Owner / Business Sponsor |
| Platform capability conflict | Solution Architect + official product docs |
| Compliance conflict | Legal / Compliance (TBC) |
| SEACF vs project convention | Project governance + SEACF Practice Lead |

Agents **MUST** report conflicts that cannot be resolved mechanically; they **MUST NOT** invent a resolution.

## Related Documents

- [grounding-policy.md](grounding-policy.md)
- [source-authority.md](source-authority.md)
- [../governance/instruction-precedence.md](../governance/instruction-precedence.md)
