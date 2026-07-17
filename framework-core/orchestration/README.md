---
title: Orchestration
version: 0.1.0
tags: [framework-core, orchestration]
---

# Orchestration

## Purpose

Cross-module request routing, context assembly, workflow execution, and reasoning pipeline contracts.

## Scope

Contracts only. Module routers (e.g. QE `enterprise-orchestrator/`, BA `.cursor/rules/routing.mdc`) **implement** these contracts.

## Documents

| Document | Focus |
|----------|-------|
| [request-router.md](request-router.md) | Intent → module → capability |
| [context-manager.md](context-manager.md) | What to load; progressive disclosure |
| [workflow-engine.md](workflow-engine.md) | Multi-step composition patterns |
| [reasoning-pipeline.md](reasoning-pipeline.md) | Shared think → decide → deliver flow |

## Navigation

- **Up:** [../README.md](../README.md)
