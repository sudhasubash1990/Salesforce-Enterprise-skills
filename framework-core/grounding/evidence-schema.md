---
title: Evidence Schema
version: 0.3.0
tags: [framework-core, grounding]
status: draft
last_updated: 2026-10-09
---

# Evidence Schema

## Purpose

Machine-readable claim record fields for material statements in SEACF outputs.

## Schema (YAML)

```yaml
claim_id: CLM-001
claim: <material statement>
classification: verified | requirement-derived | repository-guidance | assumption | recommendation | open-question | unverified
claim_family: quantitative | compliance | product-capability | project-decision | other
source_id: <path/url/document-id>
source_class: project-approved | official-product | seacf-approved | historical-example | model-knowledge
evidence_excerpt_or_locator: <reference>
evidence_confidence: high | medium | low | none
model_confidence: high | medium | low | none
conflict_status: none | conflicting | unresolved
review_required: true | false
```

## Field rules

| Field | Rule |
|-------|------|
| `claim_id` | Unique within the artifact or session (e.g., `CLM-001`) |
| `claim` | Observable statement; avoid compound multi-claims |
| `classification` | **MUST** use one of the enumerated values |
| `claim_family` | **SHOULD** set for quantitative, compliance, product-capability, or project-decision claims |
| `source_id` | Required when `classification` is `verified` or `requirement-derived` |
| `source_class` | **MUST** align with [source-authority.md](source-authority.md) |
| `evidence_excerpt_or_locator` | Path, section, requirement ID, or quote locator |
| `evidence_confidence` | Strength of eligible source support — **MUST NOT** be inferred from model certainty alone |
| `model_confidence` | Generation certainty only; **MUST NOT** substitute for evidence (see [claim-validation.md](claim-validation.md)) |
| `conflict_status` | Set `conflicting` or `unresolved` when sources disagree |
| `review_required` | **MUST** be `true` when assumption, open-question, unresolved conflict, or compliance-related |

## Evidence list items (provenance)

When embedding evidence in a grounding envelope (see [grounding-policy.md](grounding-policy.md)), agents **MAY** use:

```yaml
evidence:
  - id: E-001
    source_type: project_context | repository_knowledge | user_input | artifact
    source_ref: <relative-path-or-artifact-id>
    claim: <fact supported by the source>
    confidence: high | medium | low
```

Map `source_type` to `source_class` / claim records when promoting to a full claim table. Assumption and unknown list shapes: [uncertainty-records.md](uncertainty-records.md).

## Embeddings

Agents **MAY** embed claim tables in BRDs, test strategies, and advisory notes. Full YAML blocks are optional when a markdown table covers the same fields.

## Related Documents

- [grounding-policy.md](grounding-policy.md)
- [uncertainty-records.md](uncertainty-records.md)
- [citation-policy.md](citation-policy.md)
- [conflict-resolution.md](conflict-resolution.md)
