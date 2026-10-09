---
title: Standard Skill Contract
version: 0.3.0
tags: [framework-core, governance, skill-contract]
status: draft
last_updated: 2026-10-09
---

# Standard Skill Contract

## Purpose

Adopt a shared schema for new SEACF skills and gradually align current BA/QE skills **without** breaking Cursor discovery stubs, Layer 2 retrievers, or the QE Enterprise Orchestrator.

## Schema

Machine schema: [skill-contract-schema.yaml](skill-contract-schema.yaml).

```yaml
skill:
  name:
  version:
  purpose:
  triggers: []
  non_triggers: []
  required_inputs: []
  optional_inputs: []
  context_required: []
  authoritative_sources: []
  grounding_policy:
  allowed_tools: []
  max_action_risk:
  human_approval_conditions: []
  outputs: []
  assumptions_policy:
  validation_checks: []
  failure_conditions: []
  related_skills: []
```

## Normative rules

1. **New** module skills **MUST** publish a `skill-contract.yaml` (or equivalent) conforming to this schema beside the skill entry, or reference one from `skill.md`.
2. Existing BA/QE skills **SHOULD** add a thin contract file that **points** at Tier-0 policies and existing gates — **MUST NOT** replace `skill.md`, `.cursor/skills/*/SKILL.md`, or retriever seeds.
3. `grounding_policy` **MUST** reference [../grounding/grounding-policy.md](../grounding/grounding-policy.md) and [../grounding/claim-validation.md](../grounding/claim-validation.md) (or a module specialization that applies them).
4. `max_action_risk` **MUST** use T0–T4 from [../tools/action-risk-model.md](../tools/action-risk-model.md).
5. `context_required` **SHOULD** list context classes A–H from [../orchestration/context-policy.md](../orchestration/context-policy.md) and/or Tier-0 manifest paths.
6. `assumptions_policy` **MUST** require labelling unknowns; **MUST NOT** invent project facts.
7. `validation_checks` **MUST** include pre-delivery validation appropriate to the skill (e.g., BA validation-framework; QE pack gates).
8. Retrieved content listed under `authoritative_sources` remains Priority 6 **DATA** per [instruction-precedence.md](instruction-precedence.md) unless it is an approved project or official-product source class.

## Alignment status (Active modules)

| Module | Contract file | Discovery preserved |
|--------|---------------|---------------------|
| BA | [../../salesforce-business-analyst/skill-contract.yaml](../../salesforce-business-analyst/skill-contract.yaml) | `skill.md` + `.cursor/skills/salesforce-business-analyst/SKILL.md` |
| QE | [../../salesforce-quality-engineering/skill-contract.yaml](../../salesforce-quality-engineering/skill-contract.yaml) | `skill.md` + Enterprise Orchestrator + Cursor stub |

## Related Documents

- [prompt-contract.md](prompt-contract.md)
- [hardening-program.md](hardening-program.md)
- [../MODULE-INTEGRATION.md](../MODULE-INTEGRATION.md)
