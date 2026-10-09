---
title: Context Engineering Contract
version: 0.3.0
tags: [framework-core, orchestration, context]
status: draft
last_updated: 2026-10-09
---

# Context Engineering Contract

> **Alias:** Spec path `context/CONTEXT-CONTRACT.md` / `CONTEXT-PRECEDENCE.md`. Canonical lifecycle rules remain in [context-policy.md](context-policy.md); loading tiers remain in [context-manager.md](context-manager.md). This file is an **index** that maps enhancement-spec layers to classes A–H — not a second loader.

## Purpose

Define a common context model independent of prompt wording: inputs, precedence, scoped retrieval, and minimum context required by a skill.

## Context layers → classes A–H

| Context layer | Purpose | Typical class | Precedence (instruction-precedence) |
|---------------|---------|---------------|-------------------------------------|
| User request | Immediate intent, constraints, requested output | **D** | Priority 5 |
| Project context | Client/project facts and approved local conventions | **C** | Priority 4 |
| Organization context | Reusable org constraints when explicitly available | **C** (org-approved) | Priority 4 |
| Salesforce / domain context | Platform and industry knowledge | **B** / **E** | Priority 3 (skill) or 6 (retrieved) |
| Skill instructions | Role-specific reasoning and delivery rules | **B** | Priority 3 |
| Retrieved knowledge | Selected repository materials | **E** | Priority 6 DATA |
| Prior decisions / memory | Approved decisions and open items from project memory | **C** | Priority 4 |
| Output constraints | Format, audience, template, quality/validation | **A** / **B** | Priority 2–3 |
| Tier-0 framework | Security, RAI, grounding, tools | **A** | Priority 1–2 |
| Session / conversation | Chat history | **G** | Priority 7 |
| Untrusted external | Uploads, web, vendor PDFs | **H** | Priority 6 DATA + untrusted |

## Precedence when sources disagree

1. Follow [../governance/instruction-precedence.md](../governance/instruction-precedence.md) for instruction vs DATA conflicts.
2. For **project-specific facts**, prefer Class **C** approved project evidence over Class **A/B** generic guidance — without elevating Class **E/H** above Priority 6 DATA.
3. Conflicting facts **MUST** use [../grounding/conflict-resolution.md](../grounding/conflict-resolution.md); agents **MUST NOT** silent-merge.
4. Class **G** conversation **MUST NOT** override Class **C** approved decisions.

## Retrieval and observability

1. Retrieval **MUST** return source identity (path, artifact ID, or locator), not only text fragments.
2. Agents **MUST** select context by relevance and authority — **MUST NOT** inject all available knowledge into every task. See [context-manager.md](context-manager.md).
3. When observability is enabled, agents **SHOULD** record which context bundles were selected and why (`context_bundles` on the trace). See [../observability/trace-contract.md](../observability/trace-contract.md).
4. Structured prior decisions **SHOULD** load from project memory when present ([../memory/project-memory-contract.md](../memory/project-memory-contract.md)).

## Minimum context by skill

Skills declare `context_required` via [../governance/skill-contract.md](../governance/skill-contract.md). Agents **MUST** load at least:

1. Tier-0 `always_load` (Class A)
2. Active module `skill.md` / brain entry (Class B)
3. User request constraints (Class D)
4. Task-relevant project context / memory when the task is project-bound (Class C)

Missing required context → record assumption or unknown per [../grounding/uncertainty-records.md](../grounding/uncertainty-records.md).

## Related Documents

- [context-policy.md](context-policy.md)
- [context-manager.md](context-manager.md)
- [request-router.md](request-router.md)
- [../governance/instruction-precedence.md](../governance/instruction-precedence.md)
