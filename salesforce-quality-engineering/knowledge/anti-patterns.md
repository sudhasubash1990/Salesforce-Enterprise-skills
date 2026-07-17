---
title: Anti-Patterns
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
  - salesforce-quality-engineering/knowledge/best-practices.md
  - salesforce-quality-engineering/README.md
  - salesforce-quality-engineering/brain/anti-hallucination.md
keywords: [anti-patterns]
tags: [anti-patterns]
---

# Anti-Patterns

**Purpose:** Anti-patterns to avoid in Salesforce Quality Engineering engagements.

**Status:** Active index (Sprint 11 alignment)

---

## Incomplete Requirement Analysis

Jumping to detailed test cases or automation without Sprint 2 analysis, gaps, and quality score. Fix: load [requirement-analysis.md](requirement-analysis.md) first.

## Poor Test Coverage / Weak Test Design

Equivalence and risk ignored; only happy-path cases. Fix: [test-design-engine.md](test-design-engine.md) + coverage matrix.

## Duplicate Test Cases / Knowledge Forks

Copying BA stories or Core glossary into QE articles. Fix: multi-lens pointers; canonical content in BA/`shared`/`framework-core`.

## Skipping the Enterprise Orchestrator

Loading an unrelated sprint pack because the prompt mentioned a keyword. Fix: [../enterprise-orchestrator/enterprise-orchestrator.md](../enterprise-orchestrator/enterprise-orchestrator.md).

## Invented Metrics

Maturity scores, SLA/MTTR, ROI %, certification levels, or compliance attestations without evidence. Fix: [../brain/anti-hallucination.md](../brain/anti-hallucination.md).

## Full Automation Scripts by Default

Generating Playwright/Selenium suites when the ask was strategy or feasibility. Fix: Sprint 8 advisory only unless scripts are explicitly requested.

## Sev1 Diverted to Advisory

Portfolio health or maturity scoring while production is down. Fix: Sprint 9 restore-service-first.

## Conflating QE Production Support with Standalone PS Module

Treating `production-support/` (QE Sprint 9) as the future `salesforce-production-support/` module. Fix: [../../framework-core/MODULE-INTEGRATION.md](../../framework-core/MODULE-INTEGRATION.md).

## Related

- [best-practices.md](best-practices.md)
- [../skill.md](../skill.md)
