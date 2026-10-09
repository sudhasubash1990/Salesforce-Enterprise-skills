---
title: Claim Validation
version: 0.3.0
tags: [framework-core, grounding, claim-validation]
status: draft
last_updated: 2026-10-09
---

# Claim Validation

## Purpose

Extend Tier-0 grounding with claim-level checks for material statements before delivery.

## Scope

**In:** Pre-delivery claim checklist; evidence vs model confidence; fail-closed rules for `verified` claims.  
**Out:** BA anti-hallucination narrative depth ([anti-hallucination.md](../../salesforce-business-analyst/brain/anti-hallucination.md)); QE Agentforce product grounding packs.

Builds on [grounding-policy.md](grounding-policy.md) and [evidence-schema.md](evidence-schema.md).

## Pre-delivery claim check

For every material claim in a deliverable, agents **MUST** complete:

- [ ] Important claim identified
- [ ] Classification assigned
- [ ] Eligible source linked
- [ ] Source explicitly supports claim
- [ ] Conflicts checked
- [ ] Assumption/recommendation clearly labelled
- [ ] Human review flagged when required

## Normative rules

1. Material claims **MUST** run the pre-delivery claim check above before delivery.
2. When the workflow claims **factual certainty**, quantitative, compliance, product-capability, and project-decision claims **MUST** cite eligible evidence (`project-approved` or `official-product` per [source-authority.md](source-authority.md)).
3. Agents **MUST** distinguish **evidence_confidence** (source eligibility + support) from **model_confidence** (generation certainty). Model confidence **MUST NOT** substitute for eligible evidence.
4. Agents **MUST** fail validation when a material claim is labelled `verified` but has no eligible evidence or locator.
5. Agents **MUST** set `review_required: true` for compliance claims, unresolved conflicts, or assumptions presented as if fact.
6. Claim records **SHOULD** include `claim_family` when the claim is quantitative, compliance, product-capability, or project-decision. See [evidence-schema.md](evidence-schema.md).

## Fail-closed examples

| Claim | Classification | Result |
|-------|----------------|--------|
| “SLA is 99.9%” with no source | `verified` | **FAIL** |
| “SLA is 99.9%” labelled assumption | `assumption` | Pass with review_required |
| Feature capability from official docs with locator | `verified` | Pass |

Executable checker: [../../scripts/validate_claim_records.py](../../scripts/validate_claim_records.py). Negative fixture: [examples/verified-sla-no-source.yaml](examples/verified-sla-no-source.yaml).

## Module application

- BA: [validation-framework.md](../../salesforce-business-analyst/brain/validation-framework.md) gate 12a + this checklist; [anti-hallucination.md](../../salesforce-business-analyst/brain/anti-hallucination.md).
- QE: apply claim-validation for material KPI / coverage / certification assertions in advisory and test strategy outputs.

## Related Documents

- [grounding-policy.md](grounding-policy.md)
- [evidence-schema.md](evidence-schema.md)
- [conflict-resolution.md](conflict-resolution.md)
- [../orchestration/execution-state-model.md](../orchestration/execution-state-model.md)
