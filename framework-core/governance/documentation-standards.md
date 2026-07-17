---
title: Documentation Standards
version: 0.1.0
tags: [framework-core]
status: draft
last_updated: 2026-07-18
---

# Documentation Standards

## Purpose

Unify documentation expectations across SEACF modules.

## Scope

**In:** Cross-module SEACF contracts reusable by BA, QE, SA, Developer, DevOps, and Production Support packs.  
**Out:** Module-specific deep knowledge (lives in each module); inventing client metrics or certifications.

## Business Context

SEACF modules must share one orchestration, governance, and evaluation language so agents and humans do not re-implement routing, standards, or certification differently per skill.


## Required sections (module articles)

Purpose · Scope · Inputs · Outputs · Navigation · Related Documents  

Deliverables additionally follow [shared/output-standards.md](../../shared/output-standards.md) and module templates.

## Canonical repo standards

| Topic | Path |
|-------|------|
| Markdown | [docs/markdown-standards.md](../../docs/markdown-standards.md) |
| Naming | [docs/naming-conventions.md](../../docs/naming-conventions.md) |
| Metadata | [docs/metadata-schema.md](../../docs/metadata-schema.md) |
| Cross-linking | [docs/cross-linking-framework.md](../../docs/cross-linking-framework.md) |
| Multi-lens | [docs/multi-lens-policy.md](../../docs/multi-lens-policy.md) |
| Output engine | [output-engine/README.md](../../output-engine/README.md) |

## Rule

Framework Core does not replace `docs/`—it **binds modules** to those standards.


## Inputs

- User request / module intent
- Module `skill.md` and brain (when loaded)
- Optional evidence pack

## Outputs

- Route / context / workflow decisions
- References into module engines
- Governance-compliant artifacts

## Navigation

- **Up:** [README.md](../README.md) or parent folder README
- **Core root:** [../../README.md](../../README.md) (adjust depth as needed)

## Related Documents

- [quality-standards.md](quality-standards.md)
- [../../docs/README.md](../../docs/README.md)

## Future Enhancements

- Machine-readable route schemas
- Shared CI hooks for all modules
