---
title: Action Risk Model
version: 0.2.0
tags: [framework-core, tools]
status: draft
last_updated: 2026-10-09
---

# Action Risk Model

## Purpose

Classify agent actions by blast radius and required controls.

## Risk tiers

| Risk | Class | Examples | Control |
|------|-------|----------|---------|
| **T0** | Reasoning | Analyse requirement, classify gap, draft analysis in chat | No mutation |
| **T1** | Read | Retrieve approved artifact, search repo, read work item | Authorized data scope |
| **T2** | Draft | Prepare draft story/defect under `outputs/` | Human review before externalization where required |
| **T3** | Write | Create/update enterprise record (e.g., ADO work item) | Explicit authorization/approval contract |
| **T4** | High impact | Deployment, org config, security change, production mutation | Restricted; strong human approval and environment guardrails |

## Normative rules

1. Agents **MUST** assign a risk tier before invoking a side-effecting tool.
2. Agents **MUST NOT** escalate from T0/T1 into T3/T4 without an explicit user goal that requests the mutation.
3. Agents **SHOULD** prefer T2 local drafts before T3 external writes.
4. T4 actions **MUST** be refused unless the active skill and project policy explicitly authorize them with human approval.

## Related Documents

- [tool-governance.md](tool-governance.md)
- [tool-manifest-schema.yaml](tool-manifest-schema.yaml)
