---
title: Document Intelligence
version: 0.7.0
tags: [guidelines, sprint-5]
---

# Document Intelligence

Teach the AI **when** and **why** to create each QA document—not only the blank form.

## Core questions (every artifact)

| Question | Guidance |
|----------|----------|
| When? | Lifecycle phase + trigger event (see template Document Intelligence table) |
| Who owns? | Named role in template |
| Who reviews / approves? | Reviewers and approvers in template |
| Inputs? | Prefer reuse from Sprint 2/3 outputs and prior artifacts |
| Outputs? | Downstream consumers (RTM, summary, Go/No-Go) |
| Links? | See [artifact-relationships.md](artifact-relationships.md) |
| Phase? | Discover → Plan → Design → Execute → Release → Hypercare → Close |

## Lifecycle map (summary)

| Phase | Typical artifacts |
|-------|-------------------|
| Discover / Refine | Requirement Review, Gap Analysis, Quality Assessment, Risk |
| Plan | Test Strategy, Test Plan, Estimation, Data Strategy, Entry Criteria |
| Design | Scenarios, Cases, RTM, Automation Candidate Matrix, Design Review |
| Execute | Daily/Weekly status, Defects, Smoke/Sanity/Regression checklists, SIT/UAT |
| Release | Release Readiness, Go/No-Go, Test Summary, Dashboards |
| Hypercare / Close | Production Validation, Hypercare, Lessons Learned, KT |

## Rules

- Never create unnecessary documents ([document-generation-rules.md](document-generation-rules.md)).
- Small change → prefer checklist + sanity over full strategy rewrite.
- Always maintain traceability IDs.

## Related

- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../knowledge/clouds/README.md)
