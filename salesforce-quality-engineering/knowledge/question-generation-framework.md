---
title: Question Generation Framework
module: Salesforce Quality Engineering
category: Knowledge
document_type: Knowledge Article
version: 0.3.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/knowledge/requirement-analysis.md
  - salesforce-quality-engineering/brain/response-guidelines.md
keywords: [clarification, questions]
tags: [knowledge, sprint-2]
---

# Question Generation Framework

**Purpose:** Clarification Question Engine—intelligent, categorized, prioritized questions that unblock testability.

**Scope:** Question design rules and categories. Response formatting in [response-guidelines.md](../brain/response-guidelines.md).

**Owner:** QE Practice Lead

**Version:** 0.3.0

**Status:** Draft (Sprint 2)

---

## Rules

1. Map each question to an analysis step or Thinking Model stage.
2. Prefer answerable questions (options, yes/no, bounded lists).
3. Do not ask what is already explicit in the artifact.
4. One concern per question.
5. Prioritize: **Critical → High → Medium → Low**.

## Priority Definitions

| Priority | Meaning |
|----------|---------|
| **Critical** | Blocks analysis confidence or safe design; P0 |
| **High** | Materially affects scope, security, or integration |
| **Medium** | Improves coverage depth; can assume with impact |
| **Low** | Nice-to-know / polish |

## Question Categories

| Category | Example prompts |
|----------|-----------------|
| **Business** | What business outcome fails if this does not work? Who is the decision owner? |
| **Functional** | What happens on cancel / reject / timeout? Which statuses are valid transitions? |
| **Technical** | Declarative only or Apex involved? Any governor-sensitive volume? |
| **Data** | Required seed data? Historical migration? Soft-delete vs hard-delete? |
| **Security** | Which personas? CRUD/FLS? Sharing model? Guest/Experience users? |
| **Integration** | Sync vs async? Idempotency? Failure retry? Source of truth? |
| **Reporting** | Which reports/dashboards must reflect the change? |
| **Automation** | Which Flows/Approvals fire? Order of execution assumptions? |
| **Testing** | Which environments? What evidence defines done for UAT? |
| **Deployment** | Feature flag? Activation order? Data fix needed? |
| **Production Support** | Known errors? Monitoring alerts? Rollback expectation? |

## Output Shape

```markdown
### Open Questions
- **[Critical][Business]** What KPI proves this story delivered value?
- **[High][Security]** Which permission set grants Case create for the agent?
- **[Medium][Integration]** Is billing update sync or async on Case close?
```

## Related Documents

- [requirement-analysis.md](requirement-analysis.md)
- [requirement-review-framework.md](requirement-review-framework.md)
- [../brain/response-guidelines.md](../brain/response-guidelines.md)

## Future Enhancements

- Library of cloud-specific question packs (Sprint 4)

## Navigation

- **Previous:** [requirement-review-framework.md](requirement-review-framework.md)
- **Next:** [requirement-risk-analysis.md](requirement-risk-analysis.md)
- **See Also:** [scope-analysis.md](scope-analysis.md)
