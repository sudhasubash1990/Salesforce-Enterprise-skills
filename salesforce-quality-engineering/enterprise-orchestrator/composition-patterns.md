---
title: Multi-Capability Composition Patterns
version: 0.12.1
tags: [enterprise-orchestrator, composition]
---

# Multi-Capability Composition Patterns

## Purpose

Define **ordered** multi-sprint executions so the orchestrator composes engines without duplicating knowledge.

## Business Context

Real requests rarely map to one sprint. Composition patterns encode proven handoffs from the Module 2 roadmap (Requirements → … → Production → Advisory).

## Assessment Criteria

- Order respects upstream gates (analysis before design before cases).  
- Each hop has a clear artifact or evidence handoff.  
- Sprint 10 appears as **sink** for executive synthesis, not as a replacement for deep engines.

## Inputs / Outputs

| Pattern ID | Typical inputs | Outputs |
|------------|----------------|---------|
| COMP-01 | Story + AC | Analysis + scenarios |
| COMP-02 | Scenarios + epic | Docs + ADO structure |
| COMP-03 | Defect dump | QI + prevention + optional exec |
| COMP-04 | Release evidence pack | Ops + decision |
| COMP-05 | Portfolio / maturity ask | Advisory (+ evidence pulls) |
| COMP-06 | Automation estate | Review + roadmap |

## Evaluation Method

Select the nearest pattern; customize supporting hops; state Route line.

## Decision Framework — Patterns

### COMP-01 — Requirement to design

```
Sprint 2 Requirement Analysis
    → Sprint 3 Test Design Engine
    → (optional) Sprint 4A/4B knowledge for SF impact
```

**Stop before:** Detailed test cases until design objectives exist.

### COMP-02 — Design to documentation / ADO

```
Sprint 3 (or reuse ready design)
    → Sprint 5 document-generation / templates
    → Sprint 6 ado/ artifact guidance
```

**Hard rule:** Do not invent ADO API publish unless user explicitly requests it.

### COMP-03 — Defect intelligence loop

```
Sprint 7 defect-intelligence-engine (+ rules/)
    → Sprint 8 if automation gap / flake / coverage intent
    → Sprint 5 RCA/defect templates as needed
    → Sprint 10 if executive trend / investment ask
```

### COMP-04 — Release decision

```
Sprint 9 production-support (+ operations-intelligence)
    → Sprint 7 defect health evidence
    → Sprint 8 automation/regression readiness evidence
    → Sprint 10 decision-engine + recommendation-engine
    → Executive Recommendations (Proceed / Hold / Escalate / …)
```

### COMP-05 — Enterprise advisory primary

```
Sprint 10 advisory engine (primary)
    → Pull Sprint 7/8/9 folders for evidence only
    → Do not re-author QI/automation/ops frameworks
```

### COMP-06 — Automation transformation

```
Sprint 8 automation-intelligence (+ review-engine if brownfield)
    → Sprint 10 roadmaps / capability-model / exec dashboard if asked
```

### COMP-07 — Acute production

```
Sprint 9 FIRST (restore / triage)
    → Sprint 7 RCA after stability
    → Sprint 10 only for post-incident exec briefing
```

## Examples

**“Write scenarios and a Test Plan, then map to ADO.”** → COMP-01 then COMP-02.  
**“Friday release: go or no-go for steering?”** → COMP-04.  
**“Assess TMMi-style maturity across the CoE.”** → COMP-05.

## Best Practices

- Name the pattern ID in the Route line when multi-hop.  
- Pass IDs forward (REQ → SCN → DEF) for traceability.  
- Keep each engine’s hard rules (no scripts, no invented SLA, etc.).

## Common Anti-Patterns

| Anti-pattern | Fix |
|--------------|-----|
| Sprint 10 before Sev1 restore | COMP-07 |
| Sprint 5 detailed cases before Sprint 3 | COMP-01 |
| Duplicating defect taxonomy inside Sprint 10 | Evidence pull from Sprint 7 |

## Interview Questions

1. Why is Sprint 10 a sink in COMP-04?  
2. When is COMP-05 preferred over COMP-03?

## Related Documents

- [enterprise-orchestrator.md](enterprise-orchestrator.md)
- [capability-routing-table.md](capability-routing-table.md)

## Navigation

- **Up:** [README.md](README.md)

## Future Enhancements

- Pattern catalog expansion for Regression Intelligence
