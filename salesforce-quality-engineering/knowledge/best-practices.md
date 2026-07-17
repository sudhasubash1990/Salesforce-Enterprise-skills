---
title: Best Practices
module: Salesforce Quality Engineering
category: Root
document_type: Guide
version: 0.14.0
review_status: Approved
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-18
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/knowledge/anti-patterns.md
  - salesforce-quality-engineering/README.md
  - salesforce-quality-engineering/skill.md
keywords: [best-practices]
tags: [best-practices]
---

# Best Practices

**Purpose:** Index of Salesforce Quality Engineering best practices with pointers to canonical sprint packs (no duplicated engines).

**Status:** Active index (Sprint 11 alignment)

---

## Requirement Analysis

- Complete Sprint 2 analysis before detailed test cases — [requirement-analysis.md](requirement-analysis.md)
- Score requirement quality; raise clarifying questions; do not invent AC

## Test Planning & Design

- Use the Test Design Engine — [test-design-engine.md](test-design-engine.md)
- Risk-based coverage; document assumptions when evidence is thin
- Regression planning — [regression-planning.md](regression-planning.md)

## Execution & Documentation

- Select deliverables via [../guidelines/deliverable-selection.md](../guidelines/deliverable-selection.md)
- Follow [../guidelines/document-generation-rules.md](../guidelines/document-generation-rules.md)
- Prefer Sprint 5 templates over ad-hoc formats

## Defect & Quality Intelligence

- Classify and trend via [../quality-intelligence/](../quality-intelligence/README.md)
- Cite Rule IDs from [../quality-intelligence/rules/](../quality-intelligence/rules/README.md)
- Never invent leakage %, escape rates, or confidence scores without data

## Automation

- Strategy and feasibility via [../automation-intelligence/](../automation-intelligence/README.md)
- Playwright-first but framework-agnostic; **no full scripts** unless explicitly requested
- Review existing estates with [../automation-intelligence/review-engine/](../automation-intelligence/review-engine/README.md)

## Production Support (QE Sprint 9)

- Restore-service-first for Sev1 — [../production-support/](../production-support/README.md)
- Reuse Sprint 7 RCA; do not invent SLA/MTTR
- Standalone SEACF PS module is **planned separately** — see [../../framework-core/MODULE-INTEGRATION.md](../../framework-core/MODULE-INTEGRATION.md)

## Advisory & Validation

- Portfolio / CQO decisions → [../enterprise-quality/](../enterprise-quality/README.md)
- Framework certify / benchmark → [../validation/](../validation/README.md)
- Always route via [../enterprise-orchestrator/](../enterprise-orchestrator/README.md)

## Cross-cutting

- Load Tier-0 [framework-core](../../framework-core/README.md) before deep QE work
- Prefer multi-lens pointers over duplicating BA or Core articles
- Anti-patterns: [anti-patterns.md](anti-patterns.md)
