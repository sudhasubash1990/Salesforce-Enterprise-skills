---
title: Automation Intelligence — README
module: Salesforce Quality Engineering
version: 0.10.1
tags: [automation-intelligence, sprint-8]
---

# Automation Intelligence & Test Automation Architecture

## Purpose

Enable the AI to act as a **Test Automation Architect**: recommend whether to automate, select frameworks, design architecture, plan CI/CD, estimate ROI, **review existing estates**, and govern maintainable Salesforce automation—**without generating full scripts**.

## Scope (Sprint 8)

**In scope:** Strategy, framework design/comparison, Playwright enterprise guidance, API/mobile/visual/performance advisory, CI/CD, test data, governance, maintenance, metrics, Salesforce automation intelligence, decision engine, **review engine** (brownfield assessment).

**Out of scope:** Full Playwright/Selenium/Cypress script generation; inventing coverage % or ROI numbers without inputs.

## Engine entry

- [automation-intelligence-engine.md](automation-intelligence-engine.md)
- [automation-decision-engine.md](automation-decision-engine.md)
- [review-engine/](review-engine/README.md) — assess existing frameworks

## Folders

| Folder | Focus |
|--------|-------|
| [Automation Strategy](automation-strategy/README.md) | Define when, what, and why to automate across Salesforce delivery. |
| [Framework Design](framework-design/README.md) | Design maintainable, scalable enterprise automation frameworks. |
| [Framework Comparison](framework-comparison/README.md) | Select tools with transparent strengths, weaknesses, and Salesforce fit. |
| [Automation Patterns](automation-patterns/README.md) | Reusable automation design patterns for Salesforce programs. |
| [Playwright Knowledge](playwright/README.md) | Enterprise Playwright guidance for Salesforce (design-level, not full scripts). |
| [Selenium Guidance](selenium/README.md) | Enterprise Selenium considerations when Playwright is not adopted. |
| [Cypress Guidance](cypress/README.md) | When Cypress is appropriate vs Playwright for Salesforce. |
| [Robot Framework Guidance](robot-framework/README.md) | Keyword-driven automation with Robot Framework on Salesforce programs. |
| [API Testing](api-testing/README.md) | API automation strategy for Salesforce and integrations. |
| [Mobile Testing](mobile-testing/README.md) | Mobile automation advisory for Salesforce mobile / Field Service contexts. |
| [Visual Testing](visual-testing/README.md) | Visual regression advisory for Lightning/Experience UIs. |
| [Performance Testing](performance-testing/README.md) | Performance test strategy adjacent to functional automation. |
| [CI/CD](ci-cd/README.md) | Integrate automation into enterprise delivery pipelines. |
| [Test Data Automation](test-data/README.md) | Reliable, compliant test data for automation. |
| [Automation Governance](automation-governance/README.md) | Standards, ownership, and reviews for sustainable automation. |
| [Automation Maintenance](maintenance/README.md) | Keep suites healthy and reduce maintenance drag. |
| [Automation Metrics](metrics/README.md) | Measure automation value and health without inventing KPIs. |
| [salesforce/](salesforce/README.md) | Salesforce-specific automation intelligence |
| [decision-engine/](decision-engine/README.md) | Automate? Framework? ROI? Priority? |
| [**review-engine/**](review-engine/README.md) | **Assess existing Playwright/Selenium/Cypress estates** |

## Supported frameworks (advisory)

Playwright (**default first**), Selenium, Cypress, Robot Framework, WebdriverIO, Appium, REST Assured, Postman, Karate.

## Supported CI/CD platforms

Azure DevOps Pipelines · GitHub Actions · Jenkins

## Navigation

- **Previous:** [../quality-intelligence/README.md](../quality-intelligence/README.md)
- **Next:** [automation-intelligence-engine.md](automation-intelligence-engine.md)
- **See Also:** [../skill.md](../skill.md)

## Related Documents

- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../knowledge/clouds/README.md)
- [Documentation Generator (Sprint 5)](../templates/README.md)
- [ADO Delivery Intelligence (Sprint 6)](../ado/README.md)
- [Defect Intelligence (Sprint 7)](../quality-intelligence/README.md)
- [QI Automation Stability Rules](../quality-intelligence/rules/automation-stability-rules.md)
