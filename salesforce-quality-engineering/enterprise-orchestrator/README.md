---
title: Enterprise Orchestrator
version: 0.12.1
tags: [enterprise-orchestrator, coordinator, sprint-10-enhancement]
---

# Enterprise Orchestrator

**Purpose:** Coordinate QE requests across Sprints 2–10. Route to the right engine(s); do **not** duplicate domain knowledge.

**Scope:** Intent classification, capability routing, multi-sprint composition, handoff to Sprint 10 advisory when executive recommendations are required.

**SEACF Framework Core:** Implements the cross-module contracts in [`framework-core/orchestration/`](../../framework-core/orchestration/README.md). Other disciplines (BA, SA, Dev, DevOps, PS) use the same core contracts with their own routers.

**What this is not:** A knowledge module, maturity model, or replacement for `skill.md` / `brain/`. Domain depth remains in each sprint pack.

## Folder contents

| File | Role |
|------|------|
| [enterprise-orchestrator.md](enterprise-orchestrator.md) | Routing process, composition rules, hard gates |
| [capability-routing-table.md](capability-routing-table.md) | Keyword → sprint capability map |
| [composition-patterns.md](composition-patterns.md) | Multi-capability request patterns |

## Flow

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

## Inputs

- User request (intent, deliverable, audience)
- Optional evidence pack (stories, defects, metrics, architecture notes)
- Explicit constraints (no scripts, advisory-only, release decision, etc.)

## Outputs

- **Route plan** (primary + supporting capabilities)
- Loaded engine entry points
- Composed response (or clarification pause)
- Optional Sprint 10 executive recommendation layer

## Navigation

- **Up:** [skill.md](../skill.md) · [README.md](../README.md)
- **Brain:** [brain/brain.md](../brain/brain.md)
- **Advisory sink:** [enterprise-quality-advisory-engine.md](../enterprise-quality/enterprise-quality-advisory-engine.md)

## Related Documents

- [capability-routing-table.md](capability-routing-table.md)
- [composition-patterns.md](composition-patterns.md)
- Sprint engines: Requirement Analysis · Test Design · Document Generation · ADO · Defect Intelligence · Automation Intelligence · Production Support · Enterprise Quality Advisory
