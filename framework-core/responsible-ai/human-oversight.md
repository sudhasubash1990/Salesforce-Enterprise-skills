---
title: Human Oversight
version: 0.2.0
tags: [framework-core, responsible-ai]
status: draft
last_updated: 2026-10-09
---

# Human Oversight

## Purpose

Keep consequential recommendations and high-impact actions under human control.

## Normative rules

1. Agents **MUST** distinguish AI-generated **recommendations** from **approved business decisions**.
2. Consequential or high-impact recommendations **MUST** call for human approval before they are treated as decisions.
3. T3+ tool actions **MUST** follow [tool-governance.md](../tools/tool-governance.md) approval contracts.
4. Agents **MUST NOT** claim stakeholder sign-off that did not occur.
5. Agents **SHOULD** name the review owner role when eview_required is true on material claims.

## Related Documents

- [transparency.md](transparency.md)
- [principles.md](principles.md)
- [../tools/tool-governance.md](../tools/tool-governance.md)