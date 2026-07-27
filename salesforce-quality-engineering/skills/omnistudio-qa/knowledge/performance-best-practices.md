---
title: Performance Best Practices
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.22.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [omnistudio-qa, knowledge]
---

# Performance Best Practices

## Purpose

Assess OmniStudio performance risks without inventing timings.

## Reasoning Model

1. Flag chatty DR/IP patterns and oversized JSON.
2. Note FlexCard nesting and refresh frequency risks.
3. Require measured evidence or labeled assumptions for latency claims.
4. Recommend sampling strategy — not invented SLA %.

## Decision Rules

- Invented p95/p99 numbers → Anti-pattern.
- No Performance Assessment when remotes in scope → Incomplete.

## Cross-Links (Canonical Depth)

- [OmniStudio Cloud Knowledge](../../knowledge/clouds/omnistudio.md)
- [Enterprise Quality Advisory](../../enterprise-quality/salesforce/omnistudio.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.22.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
