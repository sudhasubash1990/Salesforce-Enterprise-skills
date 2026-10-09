---
title: Grounding and Evidence
version: 0.2.0
tags: [framework-core, grounding]
status: draft
last_updated: 2026-10-09
---

# Grounding and Evidence

## Purpose

Cross-module contracts so material outputs distinguish verified evidence from assumptions, recommendations, and model knowledge.

## Scope

**In:** Source authority, evidence schema, citation, conflict resolution, retrieval quality.  
**Out:** Module-specific claim checklists (BA anti-hallucination, QE Agentforce grounding assessment).

## Documents

| Document | Role | Load |
|----------|------|------|
| [grounding-policy.md](grounding-policy.md) | Normative MUST/MUST NOT | Tier-0 always |
| [claim-validation.md](claim-validation.md) | Pre-delivery claim checklist; evidence vs model confidence | On demand |
| [source-authority.md](source-authority.md) | `source_class` taxonomy | On demand |
| [evidence-schema.md](evidence-schema.md) | Claim record fields | On demand |
| [citation-policy.md](citation-policy.md) | When and how to cite | On demand |
| [conflict-resolution.md](conflict-resolution.md) | Conflict records + escalation | On demand |
| [retrieval-quality-checklist.md](retrieval-quality-checklist.md) | Pre-evidence retrieval checks | On demand |

## Module specializations

- BA: [anti-hallucination.md](../../salesforce-business-analyst/brain/anti-hallucination.md)
- QE Agentforce: [knowledge-grounding.md](../../salesforce-quality-engineering/skills/agentforce-testing/knowledge/knowledge-grounding.md)

## Non-authoritative examples

[examples/](examples/) illustrate claim classification. Examples **MUST NOT** be treated as project facts.

## Navigation

- **Up:** [../README.md](../README.md)
- **Related:** [../governance/instruction-precedence.md](../governance/instruction-precedence.md)
