---
title: Tool and Action Governance
version: 0.2.0
tags: [framework-core, tools]
status: draft
last_updated: 2026-10-09
---

# Tool and Action Governance

## Purpose

Separate reasoning capability from action authority. Reasoning alone does not authorize mutation.

## Documents

| Document | Role | Load |
|----------|------|------|
| [tool-governance.md](tool-governance.md) | Authorization contract | Tier-0 always |
| [action-risk-model.md](action-risk-model.md) | T0–T4 risk tiers | On demand |
| [tool-manifest-schema.yaml](tool-manifest-schema.yaml) | Manifest field contract | On demand / CI |
| [failure-and-retry-policy.md](failure-and-retry-policy.md) | Retry, timeout, audit | On demand |

## Navigation

- **Up:** [../README.md](../README.md)
- **Related:** [../security/untrusted-content-policy.md](../security/untrusted-content-policy.md)
