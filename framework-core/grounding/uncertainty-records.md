---
title: Uncertainty Records
version: 0.3.0
tags: [framework-core, grounding]
status: draft
last_updated: 2026-10-09
---

# Uncertainty Records

## Purpose

Canonical list shapes for **assumptions** and **unknowns** used in the grounding envelope and cross-module handoffs. These records map to claim classifications `assumption` and `open-question` in [evidence-schema.md](evidence-schema.md).

## Assumptions

```yaml
assumptions:
  - id: A-001
    statement: <explicit assumption>
    rationale: <why needed to proceed>
    validation_needed: true
    impact: <what is at risk if wrong>
    related_claim_ids: []   # optional CLM-### links
```

| Field | Rule |
|-------|------|
| `id` | Unique within artifact/session (`A-###`) |
| `statement` | Observable working premise — **MUST NOT** be phrased as a verified fact |
| `rationale` | Why the task cannot proceed without it |
| `validation_needed` | **MUST** be `true` until a human or eligible evidence confirms or rejects |
| `impact` | **SHOULD** state what cannot be concluded or delivered if the assumption is wrong |

## Unknowns

```yaml
unknowns:
  - id: U-001
    question: <missing information>
    impact: <what cannot be concluded without it>
    blocking: true | false
    related_claim_ids: []
```

| Field | Rule |
|-------|------|
| `id` | Unique within artifact/session (`U-###`) |
| `question` | Clarifying question for stakeholders |
| `impact` | What remains unresolved without an answer |
| `blocking` | `true` when the agent **MUST NOT** assert a related conclusion as verified |

## Mapping to claim classification

| Uncertainty record | Claim `classification` | Notes |
|--------------------|------------------------|-------|
| Assumption `A-###` | `assumption` | May appear in both envelope and claim table |
| Unknown `U-###` | `open-question` | Prefer unknowns when evidence is simply missing |
| Conflict `CFG-###` | `conflict_status: conflicting \| unresolved` | See [conflict-resolution.md](conflict-resolution.md) |

## Normative rules

1. Agents **MUST NOT** convert an assumption into a confirmed requirement or verified fact without eligible evidence or human approval.
2. Downstream modules (e.g., QE) **MUST NOT** treat assumptions as requirements when consuming a BA handoff pack. See [../handoffs/ba-qe-handoff.md](../handoffs/ba-qe-handoff.md).
3. Unresolved unknowns with `blocking: true` **MUST** appear in observability traces when traces are produced (`unresolved_unknowns`).

## Related Documents

- [grounding-policy.md](grounding-policy.md)
- [evidence-schema.md](evidence-schema.md)
- [claim-validation.md](claim-validation.md)
- [../handoffs/ba-qe-handoff.md](../handoffs/ba-qe-handoff.md)
