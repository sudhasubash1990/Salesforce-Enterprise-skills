---
title: SEACF AI Architecture
version: 0.3.0
tags: [docs, seacf, architecture, ai]
status: draft
last_updated: 2026-10-09
---

# SEACF AI Architecture

Target agent architecture for the Salesforce Enterprise AI Consulting Framework. Normative contracts live in [`framework-core/`](../framework-core/README.md); this document is a navigation summary.

## Flow

```text
User Request
    |
    v
Orchestration / Routing
    |
    v
Context Engine
  - request context
  - project context / structured memory
  - retrieved knowledge
  - prior decisions
  - evidence + uncertainty
    |
    v
SEACF Framework Core (Tier-0)
    |
    +--> Business Analyst Module --> skills
    +--> Quality Engineering Module --> skills
    +--> future modules
    |
    v
Output Engine
    |
    v
Evaluation + Human Review
```

## Design principle

| Concern | Owner |
|---------|-------|
| How to work | Skills (`skill.md`, playbooks) |
| What the model may rely on | Context engine (classes A–H) |
| What may be asserted | Grounding / claim validation |
| Why a claim is trusted | Evidence / provenance |
| Whether the result satisfies the contract | Evaluation regression + human review |

## Canonical packs

| Topic | Path |
|-------|------|
| Context | [context-policy.md](../framework-core/orchestration/context-policy.md), [context-engineering-contract.md](../framework-core/orchestration/context-engineering-contract.md) |
| Grounding | [grounding-policy.md](../framework-core/grounding/grounding-policy.md) |
| Handoff BA→QE | [ba-qe-handoff.md](../framework-core/handoffs/ba-qe-handoff.md) |
| Project memory | [project-memory-contract.md](../framework-core/memory/project-memory-contract.md) |
| Human review | [human-review-policy.md](../framework-core/governance/human-review-policy.md) |
| Observability | [trace-contract.md](../framework-core/observability/trace-contract.md) |
| Evaluation | [evaluation/README.md](../framework-core/evaluation/README.md) |
| Safety spine | [ai-safety-and-grounding.md](ai-safety-and-grounding.md) |

## Related

- [architecture.md](architecture.md) — repository layer diagram
- [PROJECT_CONTEXT.md](../PROJECT_CONTEXT.md)
