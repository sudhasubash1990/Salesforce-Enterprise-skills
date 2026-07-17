---
title: Versioning
version: 0.1.0
tags: [framework-core]
status: draft
last_updated: 2026-07-18
---

# Versioning

## Purpose

Version discipline for framework-core and consuming modules.

## Scope

**In:** Cross-module SEACF contracts reusable by BA, QE, SA, Developer, DevOps, and Production Support packs.  
**Out:** Module-specific deep knowledge (lives in each module); inventing client metrics or certifications.

## Business Context

SEACF modules must share one orchestration, governance, and evaluation language so agents and humans do not re-implement routing, standards, or certification differently per skill.


## Canonical

[docs/versioning.md](../../docs/versioning.md) · [docs/release-process.md](../../docs/release-process.md)

## Framework Core

- Semver for `framework-core` (`version` in frontmatter / README)  
- Breaking contract changes → major; new contracts → minor; typos → patch  

## Modules

- Each module keeps its own CHANGELOG / skill version  
- When adopting a new core contract, note core version in module CHANGELOG  

## Rule

Do not case-collide filenames on Windows (`CHANGELOG.md` vs `changelog.md`).


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

- [contribution-guide.md](contribution-guide.md)
- [../../docs/versioning.md](../../docs/versioning.md)

## Future Enhancements

- Machine-readable route schemas
- Shared CI hooks for all modules
