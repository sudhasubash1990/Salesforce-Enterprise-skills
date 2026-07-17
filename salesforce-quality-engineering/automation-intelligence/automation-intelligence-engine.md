---
title: Automation Intelligence Engine
version: 0.10.1
tags: [automation-intelligence, sprint-8]
---

# Automation Intelligence Engine

## Purpose

Orchestrate automation strategy → feasibility → framework selection → architecture → CI/CD → governance → metrics → **existing-framework review** for Salesforce QE.

## Process

```
Requirement / scenario / candidate input
    ↓
Feasibility & prioritization (strategy)
    ↓
Automate vs manual decision (decision engine)
    ↓
Framework selection (comparison + Playwright-first default)
    ↓
Architecture & patterns (framework-design)
    ↓
Test data + CI/CD design
    ↓
Governance & maintenance model
    ↓
Metrics & health (no invented %)
    ↓
If existing estate provided → Automation Review Engine (scorecard + improvements)
```

## Review path (brownfield)

When the user provides an existing Playwright/Selenium/Cypress (or hybrid) framework:

1. Load [review-engine/](review-engine/README.md).  
2. Score nine dimensions; compute maintainability score.  
3. Prioritize P0–P3 improvements (secrets/flake before rewrites).  
4. Produce [review-report-template.md](review-engine/review-report-template.md).  

## Hard rules

1. **No full script generation** in Sprint 8—design, decisions, and reviews only.  
2. Playwright-first, framework-agnostic (respect brownfield estates).  
3. Never invent ROI, coverage %, flake %, or execution times without data/assumptions.  
4. Reuse Sprint 3 automation candidates; Sprint 7 flake/stability rules; Sprint 6 ADO CI concepts.  
5. Prefer API/service automation under thin UI smoke (pyramid).  
6. Security ≤ 2 or chronic flake → **At Risk**; do not greenwash with architecture praise alone.  

## Related

- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../knowledge/clouds/README.md)
- [Documentation Generator (Sprint 5)](../templates/README.md)
- [ADO Delivery Intelligence (Sprint 6)](../ado/README.md)
- [Defect Intelligence (Sprint 7)](../quality-intelligence/README.md)
- [QI Automation Stability Rules](../quality-intelligence/rules/automation-stability-rules.md)
- [automation-decision-engine.md](automation-decision-engine.md)
- [review-engine/README.md](review-engine/README.md)
