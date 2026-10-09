---
title: Orchestration
version: 0.3.0
tags: [framework-core, orchestration]
---

# Orchestration

## Purpose

Cross-module request routing, context assembly, workflow execution, and reasoning pipeline contracts.

## Scope

Contracts only. Module routers (e.g. QE `enterprise-orchestrator/`, BA `.cursor/rules/routing.mdc`) **implement** these contracts.

## Documents

| Document | Focus | Load |
|----------|-------|------|
| [request-router.md](request-router.md) | Intent → module → capability | Tier-0 always |
| [context-manager.md](context-manager.md) | What to load; progressive disclosure | Tier-0 always |
| [context-policy.md](context-policy.md) | Context classes A–H; lifecycle MUST/MUST NOT | Tier-0 always |
| [context-engineering-contract.md](context-engineering-contract.md) | Layer→class A–H index; precedence (spec CONTEXT-CONTRACT) | On demand |
| [execution-state-model.md](execution-state-model.md) | Agent states, gates, safe failure | Tier-0 always |
| [execution-states.yaml](execution-states.yaml) | Machine-readable state graph | On demand |
| [workflow-engine.md](workflow-engine.md) | Multi-step composition patterns | On demand |
| [reasoning-pipeline.md](reasoning-pipeline.md) | Shared think → decide → deliver flow | On demand |

## Navigation

- **Up:** [../README.md](../README.md)
