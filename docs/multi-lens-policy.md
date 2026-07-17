---
title: Multi-Lens Documentation Policy
version: 1.0.0
last_updated: 2026-07-18
---

# Multi-Lens Documentation Policy

## Purpose

Prevent duplicate full articles across QE packs (knowledge, ADO, automation-intelligence, production-support, enterprise-quality) while preserving lens-specific advice.

## Rule

1. **One canonical** article owns the full body (usually under `salesforce-quality-engineering/knowledge/`).
2. Other locations keep a **thin pointer** (frontmatter `type: pointer`) plus optional 5–15 line lens delta if truly unique.
3. Agents load the canonical path; they may add lens context in the *response*, not by inventing a second full KB article.

## Canonical map (priority topics)

| Topic | Canonical |
|-------|-----------|
| Quality gates | `salesforce-quality-engineering/knowledge/quality-gates.md` |
| Release readiness | `salesforce-quality-engineering/knowledge/release/release-readiness.md` (fallback: playbooks if release article absent) |
| Cloud products | `salesforce-quality-engineering/knowledge/clouds/<cloud>.md` |
| Platform Events | `salesforce-quality-engineering/knowledge/integration/platform-events.md` |
| Smoke / sanity / regression planning | `salesforce-quality-engineering/knowledge/release/` |
| Consulting principles (enterprise) | `shared/consulting-principles.md` |

## Anti-patterns

- Copy-pasting a full cloud article into automation-intelligence, production-support, and enterprise-quality
- Maintaining divergent versions of the same gate definitions
