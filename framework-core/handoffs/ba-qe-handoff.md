---
title: BA to QE Handoff Contract
version: 0.3.0
tags: [framework-core, handoffs, ba, qe]
status: draft
last_updated: 2026-10-09
---

# BA → QE Handoff Contract

> **Alias:** Spec path `handoffs/BA-QE-HANDOFF.md`. Complements [../../shared/traceability-model.md](../../shared/traceability-model.md); does not replace BA story templates or QE test-design engines.

## Purpose

Define a stable handoff model so upstream BA analysis becomes downstream QE coverage without manual reinterpretation or loss of identifiers.

## Handoff flow

```text
BA output
  requirement_id
  requirement_statement
  acceptance_criteria[]
  business_rules[]
  non_functional_requirements[]
  risks[]
  assumptions[]
  evidence_refs[]
        │
        ▼
QE input
  test_scenarios[]
  positive_negative_coverage
  integration_coverage
  data_coverage
  automation_candidate
  traceability_refs[]
  coverage_gaps[]   # questions / requirement defects back to BA
```

Machine schema: [ba-qe-handoff-schema.yaml](ba-qe-handoff-schema.yaml).

## Normative rules

1. Agents **MUST** preserve `requirement_id` and acceptance-criteria identifiers across the handoff.
2. QE agents **MUST NOT** convert a BA `assumption` into a confirmed requirement.
3. QE agents **MUST** expose coverage gaps back to BA as open questions or requirement defects (`coverage_gaps[]`).
4. Assumptions and unknowns in the handoff pack **MUST** retain their IDs (`A-###`, `U-###`) per [../grounding/uncertainty-records.md](../grounding/uncertainty-records.md).
5. Evidence references **SHOULD** be carried forward so QE claims remain grounded.
6. Agents **MUST NOT** invent Salesforce configuration or SLAs to fill gaps — record unknowns instead.

## Field mapping (BA story → QE)

| BA source | Handoff field | QE consumer |
|-----------|---------------|-------------|
| Requirement / story ID | `requirement_id` | RTM / test scenario parent |
| Title + Description | `requirement_statement` | Scenario intent |
| Acceptance Criteria (AC1…) | `acceptance_criteria[]` | Positive/negative cases |
| Business Rules (BR1…) | `business_rules[]` | Rule-based scenarios |
| NFRs / Security | `non_functional_requirements[]` | NFR / permission tests |
| Dependencies / Risks | `risks[]` | Risk-based priority |
| Assumptions | `assumptions[]` | Provisional coverage only |
| Evidence / provenance | `evidence_refs[]` | Grounding for test claims |

## Evaluation

Cross-module regression scenario **HANDOFF-001**: [../evaluation/cross-module/ba-to-qe-handoff.yaml](../evaluation/cross-module/ba-to-qe-handoff.yaml).

## Module wiring

- BA: produce handoff-ready identifiers in stories/BRDs; see Pre-Execution Gate in [../../salesforce-business-analyst/skill.md](../../salesforce-business-analyst/skill.md).
- QE: consume handoff pack before inventing scope; see [../../salesforce-quality-engineering/skill.md](../../salesforce-quality-engineering/skill.md) and Enterprise Orchestrator.

## Related Documents

- [../../shared/traceability-model.md](../../shared/traceability-model.md)
- [../../salesforce-quality-engineering/knowledge/traceability.md](../../salesforce-quality-engineering/knowledge/traceability.md)
- [../grounding/grounding-policy.md](../grounding/grounding-policy.md)
