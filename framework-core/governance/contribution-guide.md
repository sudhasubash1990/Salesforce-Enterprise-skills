---
title: Contribution Guide (Framework Core)
version: 0.1.0
tags: [framework-core]
status: draft
last_updated: 2026-07-18
---

# Contribution Guide (Framework Core)

## Purpose

How to extend Framework Core and register new modules.

## Scope

**In:** Cross-module SEACF contracts reusable by BA, QE, SA, Developer, DevOps, and Production Support packs.  
**Out:** Module-specific deep knowledge (lives in each module); inventing client metrics or certifications.

## Business Context

SEACF modules must share one orchestration, governance, and evaluation language so agents and humans do not re-implement routing, standards, or certification differently per skill.


## Adding a new module

1. Create `salesforce-<discipline>/` with `skill.md`, `README.md`, `brain/`.  
2. Implement module router that **conforms** to [../orchestration/request-router.md](../orchestration/request-router.md).  
3. Link shared knowledge via [../shared-knowledge/](../shared-knowledge/README.md)—do not fork glossary.  
4. Add module validation under module `validation/` implementing [../evaluation/](../evaluation/README.md).  
5. Register in Framework Core README module table + root [ROADMAP.md](../../ROADMAP.md).  
6. Add Cursor discovery stub under `.cursor/skills/`.  

## Changing a core contract

1. Update the core markdown.  
2. Bump framework-core version.  
3. Note migration in module CHANGELOGs.  
4. Prefer additive changes.

## Also see

[CONTRIBUTING.md](../../CONTRIBUTING.md) · [docs/repository-guidelines.md](../../docs/repository-guidelines.md)


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

- [versioning.md](versioning.md)
- [../../CONTRIBUTING.md](../../CONTRIBUTING.md)

## Future Enhancements

- Machine-readable route schemas
- Shared CI hooks for all modules
