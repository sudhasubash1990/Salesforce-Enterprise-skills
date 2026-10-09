---
title: Human Review Policy
version: 0.3.0
tags: [framework-core, governance, human-review]
status: draft
last_updated: 2026-10-09
---

# Human Review Policy

> **Alias:** Spec path `governance/HUMAN-REVIEW-POLICY.md`. Complements [../responsible-ai/human-oversight.md](../responsible-ai/human-oversight.md) and tool risk tiers in [../tools/tool-governance.md](../tools/tool-governance.md).

## Purpose

Risk-based human review gates for AI-generated SEACF outputs. Automated validation **MUST NOT** alone mark content as business-approved.

## Risk levels

| Risk | Examples | Expected behavior |
|------|----------|-------------------|
| **Low** | Workshop questions, formatting, summaries | Proceed; identify assumptions normally |
| **Medium** | Requirements, acceptance criteria, test design | Generate with traceability and explicit review points |
| **High** | Security, architecture-impacting design, destructive data actions, production changes | Require explicit human approval before treating recommendation as approved/ready for action |

## Artifact metadata (optional, non-breaking)

Agents **MAY** set these frontmatter fields on generated deliverables (see [../../docs/metadata-schema.md](../../docs/metadata-schema.md)):

```yaml
risk_level: low | medium | high
human_review_status: draft | review_required | approved
```

### Normative rules

1. AI-generated content **MUST NOT** be marked `human_review_status: approved` merely because it passed automated validation or claim checks.
2. `human_review_status: approved` **MUST** reflect an explicit human (or designated stakeholder) approval event.
3. Medium-risk deliverables **SHOULD** set `human_review_status: review_required` until reviewed.
4. High-risk recommendations and T3+ tool actions **MUST** enter `HUMAN_APPROVAL_REQUIRED` per [../orchestration/execution-state-model.md](../orchestration/execution-state-model.md) before `EXECUTING_ACTION`.
5. When observability is enabled, agents **SHOULD** record `human_review_triggers` on the decision trace.

## Mapping to tool risk tiers

| Human-review risk | Typical tool tier |
|-------------------|-------------------|
| Low | T0–T1 |
| Medium | T2–T3 (read/analyze; write with gate) |
| High | T3–T4 (writes, production, destructive) |

## Related Documents

- [../responsible-ai/human-oversight.md](../responsible-ai/human-oversight.md)
- [../tools/action-risk-model.md](../tools/action-risk-model.md)
- [../observability/trace-contract.md](../observability/trace-contract.md)
