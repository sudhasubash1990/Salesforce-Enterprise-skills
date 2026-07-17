---
title: Enterprise Orchestrator — Routing Coordinator
version: 0.12.1
tags: [enterprise-orchestrator, coordinator, routing]
---

# Enterprise Orchestrator

## Purpose

Act as the **single routing coordinator** for SEACF Module 2 (Salesforce Quality Engineering). Classify intent, select sprint capabilities, compose multi-capability work, and escalate synthesis to the Sprint 10 Advisory Engine when executive recommendations are needed.

## Business Context

After Sprints 1–10, the module contains many specialist engines. Without an orchestrator, agents may load the wrong pack, skip upstream gates, or re-implement knowledge. The orchestrator ensures every request follows:

**Brain → Route → Capability engine(s) → (optional) Sprint 10 advisory → Response**

## Assessment Criteria (routing quality)

| Criterion | Pass |
|-----------|------|
| Intent classified | Primary intent + secondary intents named |
| Capability selected | At least one sprint entry point with path |
| Upstream gates | Requirement Analysis / Test Design invoked when required |
| No knowledge duplication | Depth loaded from sprint packs, not reinvented here |
| Executive layer | Sprint 10 used when audience is CIO/CTO/CQO/Steering or decision is Proceed/Hold/Escalate |
| Anti-hallucination | No invented metrics, maturity, SLA, or compliance attestations |

## Inputs

| Input | Required |
|-------|----------|
| User request text | Yes |
| Deliverable type (if stated) | Preferred |
| Audience (team / exec) | Preferred for Sprint 10 |
| Evidence pack | When scoring or decisions requested |
| Explicit exclusions (e.g. “no scripts”) | When stated |

## Outputs

1. **Route plan** (shown briefly before deep work on complex requests)
2. Capability-specific analysis / artifacts
3. Optional **Executive Recommendations** via Sprint 10 decision + recommendation engines
4. Confidence + residual risk + open questions

## Evaluation Method — Routing Process

```
1. Load brain (philosophy → consulting → brain → thinking-model)
2. Classify intent (see Intent Catalog)
3. Resolve primary capability via capability-routing-table.md
4. Resolve supporting capabilities (composition-patterns.md)
5. Enforce Pre-Execution Gate from skill.md for selected path(s)
6. Execute primary engine; call support engines for evidence only
7. If executive / portfolio / maturity / release decision / audit / roadmap
      → Sprint 10 Enterprise Quality Advisory Engine
8. Compose unified response (facts vs assumptions; no invented scores)
```

### Architecture

```
User Request
      │
      ▼
Enterprise Orchestrator
      │
 ┌────┼───────────────────────────┐
 │    │    │    │    │    │       │
 ▼    ▼    ▼    ▼    ▼    ▼       ▼
Sprint 2  Sprint 3  Sprint 5  Sprint 6  Sprint 7  Sprint 8  Sprint 9
Requirements → Test Design → Documents → ADO → Defects → Automation → Production
      │
      ▼
Sprint 10 Advisory Engine
      │
      ▼
Executive Recommendations
```

## Decision Framework

### Intent Catalog (primary)

| Intent | Primary sprint | Entry |
|--------|----------------|-------|
| Requirement / AC / story / BRD / FRD review | **2** | [requirement-analysis.md](../knowledge/requirement-analysis.md) |
| Scenarios / coverage / regression scope / technique selection | **3** | [test-design-engine.md](../knowledge/test-design-engine.md) |
| Platform / metadata / security / data explain | **4A** | [knowledge/platform/](../knowledge/platform/README.md) |
| Cloud / package / integration / industry explain | **4B** | [knowledge/clouds/](../knowledge/clouds/README.md) |
| QA document / template / checklist / RTM pack | **5** | [document-generation/](../document-generation/README.md) |
| ADO work items / Test Plans / bugs / queries / dashboards | **6** | [ado/](../ado/README.md) |
| Defects / RCA / trends / QI rules / leakage | **7** | [defect-intelligence-engine.md](../quality-intelligence/defect-intelligence-engine.md) |
| Automation strategy / framework / CI/CD / review | **8** | [automation-intelligence-engine.md](../automation-intelligence/automation-intelligence-engine.md) |
| Go-live / incident / change / runbooks / ops intelligence | **9** | [production-support-engine.md](../production-support/production-support-engine.md) |
| Project/portfolio health, maturity, audits, exec dashboards, roadmaps, Proceed/Hold | **10** | [enterprise-quality-advisory-engine.md](../enterprise-quality/enterprise-quality-advisory-engine.md) |

### Routing rules (priority)

1. **Explicit user target wins** — If the user names a sprint/engine, route there (still enforce upstream gates).
2. **Lifecycle order** — Requirements before Test Design before detailed cases/docs that depend on design.
3. **Acute production first** — Sev1 / active incident → Sprint 9 before advisory narrative.
4. **Executive sink** — CIO/CTO/CQO/Steering, portfolio, maturity index, audit scorecard, transformation roadmap, or release Proceed/Hold → include Sprint 10 after operational engines.
5. **Thin orchestration** — Load only folders needed; do not preload all of `enterprise-quality/` for a single story review.
6. **Never invent** — If evidence missing for scores/decisions, return RAG **Unknown** / assumptions / questions—not fabricated KPIs.

### Multi-capability composition

| Pattern | Order |
|---------|-------|
| Story → scenarios | 2 → 3 → (5 if document) |
| Scenarios → ADO Test Plan | 3 → 5 → 6 |
| Defect surge → prevention | 7 (+ rules) → 8 if automation gap → 10 if exec ask |
| Release go/no-go | 9 (+ ops intel) → 7/8 evidence → **10 decision engine** |
| Maturity / portfolio | 10 primary; pull 7–9 for evidence only |
| Brownfield automation estate | 8 review-engine → 10 if roadmap/exec |

Full patterns: [composition-patterns.md](composition-patterns.md).

## Examples

### Example A — Single capability

**Request:** “Review this user story for testability.”  
**Route:** Sprint 2 Requirement Analysis.  
**Not loaded:** Sprint 10 advisory (unless user asks for executive summary).

### Example B — Composed lifecycle

**Request:** “From this story, design scenarios and draft an ADO Test Suite structure.”  
**Route:** 2 (if not already analyzed) → 3 → 5/6.  
**Advisory:** Skip unless release risk asks for Hold/Proceed.

### Example C — Executive decision

**Request:** “Should we proceed with Friday’s release? Here is defect + automation + hypercare data.”  
**Route:** 7 + 8 + 9 (evidence) → **10 decision + recommendation engines** → Executive Recommendations.

## Best Practices

- State a one-line **Route:** `Primary: Sprint N · Support: … · Advisory: Yes/No` on complex or multi-intent requests.
- Prefer reuse of existing engines over new prose frameworks.
- Keep Sprint 10 as **synthesis**, not a second copy of defect/automation/ops knowledge.
- Preserve persona: team QE consultant by default; CQO posture when Sprint 10 is engaged.

## Common Anti-Patterns

| Anti-pattern | Instead |
|--------------|---------|
| Jump to test cases | Route 2 → 3 first |
| Load all of enterprise-quality for AC review | Stay on Sprint 2 |
| Invent maturity % for “health score” | Evidence-based RAG or Unknown |
| Generate full Playwright scripts via “automation” route | Sprint 8 design/review only |
| Write a new knowledge article inside the orchestrator | Link the sprint pack |
| Skip Sprint 9 on Sev1 to write a portfolio deck | Restore service first |

## Interview Questions (for humans validating the orchestrator)

1. How do you decide between Sprint 7 and Sprint 10 for a defect trend question?
2. When must Requirement Analysis run before Test Design?
3. What triggers the Sprint 10 executive recommendation layer?
4. How should the orchestrator behave when metrics are missing?

## Related Documents

- [README.md](README.md)
- [capability-routing-table.md](capability-routing-table.md)
- [composition-patterns.md](composition-patterns.md)
- [skill.md](../skill.md) — Pre-Execution Gate
- [brain/brain.md](../brain/brain.md)
- [enterprise-quality-advisory-engine.md](../enterprise-quality/enterprise-quality-advisory-engine.md)

## Navigation

- **Previous:** [brain/brain.md](../brain/brain.md)
- **Next:** Selected sprint engine per route plan
- **See also:** [prompts.md](../prompts.md) — Orchestrate QE Request

## Future Enhancements

- Optional machine-readable route plan JSON
- Hook to `scripts/retrieve_context.py` for QE (if added)
- Regression Intelligence route when that pack lands
