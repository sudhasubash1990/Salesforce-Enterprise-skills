---
title: ADO Artifact Generation
version: 0.8.0
tags: [ado, sprint-6]
---

# Artifact Generation

## Purpose

Teach the AI to generate **ADO-ready content** (titles, descriptions, AC, steps)—not API calls.

## Artifacts

| Artifact | Guidance folder / doc |
|----------|------------------------|
| Epic | [epics/epic.md](epics/epic.md) |
| Feature | [features/feature.md](features/feature.md) |
| User Story | [user-stories/user-story.md](user-stories/user-story.md) |
| Task | [tasks/task.md](tasks/task.md) |
| Bug | [bugs/bug.md](bugs/bug.md) |
| Risk / Issue | [work-items/](work-items/README.md) |
| Test Plan / Suite / Case / Shared Steps | [test-plans/](test-plans/README.md) · [test-suites/](test-suites/README.md) · [test-cases/](test-cases/README.md) |
| Acceptance Criteria | Nested Given/When/Then; align userstory-generation rules |
| Definition of Ready / Done | [governance/](governance/README.md) |
| Release Notes | Summarize Stories Done + known limitations + test evidence themes |
| Deployment Validation | Link [../templates/deployment-validation-checklist.md](../templates/deployment-validation-checklist.md) |

## Rules

- Reuse Sprint 2/3/5 outputs; do not rewrite BA stories unless asked.  
- Follow INVEST for stories; nested AC bullets.  
- Leave Story Points empty unless user asks for indicative value.  
- Structure HTML-friendly headings/lists for ADO Description fields.  

## Related

- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../knowledge/clouds/README.md)
- [Documentation Generator (Sprint 5)](../templates/README.md)
- [BA ADO Backlog Integration](../../salesforce-business-analyst/knowledge/ado-backlog-integration.md) (sibling—do not duplicate)
