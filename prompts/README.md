---
title: Root Prompts Library
module: Salesforce Enterprise Skills
category: Root
document_type: Guide
version: 1.0.0
review_status: Draft
owner: SEACF Practice Lead
created_date: 2026-08-10
last_updated: 2026-08-10
review_cycle: quarterly
related_documents:
  - GETTING_STARTED.md
  - README.md
  - salesforce-business-analyst/prompts.md
  - salesforce-quality-engineering/prompts.md
keywords: [prompts, copy-paste, seacf, ba, qe]
tags: [prompts, SEACF]
---

# Salesforce Enterprise Skills — Prompt Library

Copy-paste prompts that only make sense **after you clone this repository**. Each prompt tells the AI to load SEACF skills, templates, playbooks, and validation gates—not invent a generic consulting answer.

## How to use

1. Open this repo as your Cursor workspace root (see [GETTING_STARTED.md](../GETTING_STARTED.md)).
2. Pick a prompt from the catalogs below.
3. Replace bracketed placeholders (`[industry]`, `[clouds]`, paste blocks).
4. Run in **Agent** mode (or Claude with this repo in context).
5. Expect outputs under `outputs/<project>/` when the prompt asks to save artifacts.

## Catalogs

| Catalog | Focus | Count |
|---------|-------|------:|
| [salesforce-ba-prompts.md](salesforce-ba-prompts.md) | Discovery, BRD/FRD, stories, fit-gap, KPI, OCM, RAID, RTM, ADO | 28 |
| [salesforce-qa-prompts.md](salesforce-qa-prompts.md) | Test strategy, scenarios, migration, API, automation, defects, production quality | 28 |
| **Total** | | **56** |

## Why these are not generic ChatGPT prompts

| Generic prompt | SEACF prompt |
|----------------|--------------|
| "Write a BRD" | Loads [`brd-template.md`](../salesforce-business-analyst/templates/brd-template.md), requirement IDs, assumptions, anti-hallucination |
| "Make test cases" | Routes via [Enterprise Orchestrator](../salesforce-quality-engineering/enterprise-orchestrator/enterprise-orchestrator.md); forbids invented coverage % / SLA metrics |
| "Is Salesforce a fit?" | Uses Standard / Config / Extend / Gap / Defer from [`decision-framework.md`](../salesforce-business-analyst/brain/decision-framework.md) |

## Related module prompt indexes

Canonical deep catalogs (Sprint / skill-specific) remain in the modules:

- [BA prompts](../salesforce-business-analyst/prompts.md)
- [QE prompts](../salesforce-quality-engineering/prompts.md)
- [QE prompts index](../salesforce-quality-engineering/prompts/README.md)

This `prompts/` folder is the **showcase library** for first-time users and demos.

## Quick start trio

1. BA — [Service Cloud complaint BRD](salesforce-ba-prompts.md#ba-03--service-cloud-complaint-management-brd)
2. BA — [Fit-gap with Standard/Config/Extend](salesforce-ba-prompts.md#ba-09--fit-gap-standard--config--extend--gap--defer)
3. QE — [Release test strategy](salesforce-qa-prompts.md#qe-01--service-cloud-release-test-strategy)
