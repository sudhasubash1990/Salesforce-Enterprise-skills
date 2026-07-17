---
title: Azure DevOps Test Plans Organization
version: 0.8.0
tags: [ado, sprint-6]
---

# Azure DevOps Test Plans Organization

## When to create Test Plans

| Trigger | Plan intent |
|---------|-------------|
| Sprint start | Sprint execution plan |
| Release train | Release regression + smoke |
| SIT window | Integration suites |
| UAT start | Business validation suites |
| Prod deploy | Production validation / hypercare smoke |

## Suite strategies

| Suite type | Use |
|------------|-----|
| **Static** | Curated Smoke / critical path |
| **Requirement-based** | Coverage vs Stories/Requirements |
| **Query-based** | Dynamic packs by tag/Area/Iteration |
| **Regression** | Risk-based prior scope |
| **Smoke** | Post-deploy confidence |
| **UAT** | Business scenarios |
| **Release** | Full release evidence set |

## Organization tips

- Name: `YYYY.MM - <Release/Sprint> - <Purpose>`  
- Separate Automation vs Manual suites if helpful  
- Keep Smoke small and stable  

## Related

- [test-plans/README.md](test-plans/README.md)
- [test-suites/README.md](test-suites/README.md)
