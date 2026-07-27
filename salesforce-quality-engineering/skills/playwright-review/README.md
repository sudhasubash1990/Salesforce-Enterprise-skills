---
title: Playwright Review — README
module: Salesforce Quality Engineering
category: QE Specialized Skill
document_type: Guide
version: 0.21.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [playwright-review]
---

# Playwright Review (PWR)

## Purpose

Enterprise **Playwright automation review** capability for Salesforce QE. Evaluates framework architecture, code quality, locators, Salesforce UI sync, flaky tests, performance, security, and CI/CD readiness — not a syntax-only checker.

Canonical encyclopedia remains in:

- [`../../automation-intelligence/review-engine/`](../../automation-intelligence/review-engine/README.md)
- [`../../automation-intelligence/playwright/`](../../automation-intelligence/playwright/README.md)

This pack holds **Playwright review reasoning models** and the **18-section** deliverable.

## Capabilities

- Framework and architecture assessment  
- Locator, assertion, and synchronization review  
- Salesforce Lightning / Experience / Agentforce UI compatibility  
- Maintainability and performance analysis  
- Flaky test investigation  
- CI/CD readiness (Azure DevOps, GitHub Actions)  
- Security (secrets, storageState)  
- 1–5 overall quality score with evidence  

## Supported Playwright Features

Config · Projects · Fixtures · Hooks · POM · Locators · Assertions · Auto-wait · Retries · Parallel · Trace · Reporting · API request · Auth/storageState · Network mock · Accessibility · Mobile emulation · Cross-browser

## Folder Structure

```
skills/playwright-review/
├── SKILL.md
├── README.md
├── skill-config.yaml
├── knowledge/       ← 22 reasoning articles
├── playbooks/       ← 8 playbooks
├── templates/       ← 8 templates
├── prompts/         ← 10 prompts
├── examples/        ← 10 examples
└── tests/           ← 12 scenarios
```

## Inputs

| Input | Required |
|-------|----------|
| Framework context (tree/config) | Yes |
| Review scope (framework / scripts / CI) | Yes |
| Sample page objects / tests (sanitized) | Recommended |
| CI pipeline description | Recommended |
| Flake/failure signals | Recommended |
| Salesforce UI surfaces in scope | When UI automation |

## Outputs

18-section Playwright Review report — see [SKILL.md](SKILL.md). Primary template: [templates/automation-code-review-report.md](templates/automation-code-review-report.md).

## Sample Prompt

```
Load skills/playwright-review/SKILL.md.
Framework: Playwright TS, POM under pages/, fixtures for sales/service personas.
Scope: Login + Account create; CI on Azure DevOps.
Produce all 18 sections with 1–5 scores and refactor snippets.
Do not invent flake %; label assumptions.
```

See [prompts/README.md](prompts/README.md).

## Example Reviews

See [examples/README.md](examples/README.md).

## Best Practices

- Framework context before script critique  
- Prefer getByRole / label / test-id  
- Auto-wait over hard sleeps for Lightning  
- storageState per persona; never commit secrets  
- Score with Sprint 8 1–5 model; N/A if no evidence  
- Chain MIA/SOVA/PTA/AFT/TDG when applicable  

## Common Anti-Patterns

- XPath soup and absolute CSS for Lightning  
- Shared mutable page across workers  
- Disabling isolation to “make tests pass”  
- Invented coverage/stability metrics  
- Full suite rewrite without request  

## Limitations

- No live execution  
- Selenium/Cypress → Sprint 8 review-engine  
- Planned siblings (Risk-Based Regression, Production RCA) — cross-link only  

## Future Enhancements

- Deeper OmniStudio component automation review when OmniStudio QA exists  
- Regression pack impact matrix when Risk-Based Regression exists  

## Related Documents

- [SKILL.md](SKILL.md)  
- [skill-config.yaml](skill-config.yaml)  
- [Parent skill.md](../../skill.md)  
- [Sprint 8 Review Engine](../../automation-intelligence/review-engine/README.md)  
- [Sprint 8 Playwright Knowledge](../../automation-intelligence/playwright/README.md)  

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial Playwright Review capability |
