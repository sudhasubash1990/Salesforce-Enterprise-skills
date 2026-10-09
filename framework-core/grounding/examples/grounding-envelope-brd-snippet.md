---
title: Grounding Envelope BRD Snippet (Non-Authoritative Example)
version: 0.3.0
tags: [framework-core, grounding, example]
status: draft
last_updated: 2026-10-09
---

# Grounding Envelope — Mini BRD Snippet

**WARNING:** Historical-example only. **MUST NOT** be treated as project-approved requirements. No real client data.

## Envelope

```yaml
grounding:
  facts:
    - id: F-001
      claim_id: CLM-001
      statement: Agents shall log customer complaints as Cases linked to Account
  evidence:
    - id: E-001
      source_type: artifact
      source_ref: examples/sample-brd/README.md
      claim: Fictional BR-010 states Case logging for complaints
      confidence: medium
  assumptions:
    - id: A-001
      statement: Average handle time target is 4 minutes
      rationale: Needed for capacity narrative in workshop draft
      validation_needed: true
      impact: SLA and staffing recommendations remain provisional
  unknowns:
    - id: U-001
      question: Is chat in Phase 1 or deferred to Phase 2?
      impact: Channel scope and Omni-Channel design cannot be finalized
      blocking: true
  conflicts:
    - id: CFG-001
      summary: Workshop notes vs scope deck disagree on chat Phase 1
  recommendations:
    - id: R-001
      statement: Omni-Channel skill-based routing is recommended
      evidence_refs: [E-001]
```

## Claim table (aligned)

| claim_id | claim | classification | notes |
|----------|-------|----------------|-------|
| CLM-001 | Agents shall log complaints as Cases linked to Account | requirement-derived | F-001 |
| CLM-002 | Omni-Channel routing recommended | recommendation | R-001 |
| CLM-003 | AHT target is 4 minutes | assumption | A-001 |
| CLM-004 | Chat channel deferred vs Phase 1 | open-question | U-001 / CFG-001 |
