---
title: Response Guidelines
module: Salesforce Quality Engineering
category: Brain
document_type: Framework
version: 0.2.1
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/skill.md
  - salesforce-quality-engineering/brain/brain.md
  - salesforce-quality-engineering/prompts.md
  - shared/output-standards.md
keywords: [response-guidelines]
tags: [brain, response]
---

# Response Guidelines

**Purpose:** Standard response format for every substantive QE answer.

**Scope:** Structure, clarifications, assumptions, confidence, and formatting. Reasoning content comes from [brain.md](brain.md) / [thinking-model.md](thinking-model.md). Prompting standards also in [prompts.md](../prompts.md).

**Owner:** QE Practice Lead

**Version:** 0.2.1

**Status:** Draft (Sprint 1 — modular Brain)

---

## Default Response Structure

| # | Section | Required |
|---|---------|----------|
| 1 | **Reasoning summary** — Context, completeness, key Salesforce impacts, risks (brief) | Yes |
| 2 | **Assumptions** — Numbered; impact if false | Yes when any inference used |
| 3 | **Open questions / blockers** — Must / Should / Nice to know | Yes when gaps exist; else "None blocking" |
| 4 | **Recommendations** — Testing approach, automation scope, regression scope | Yes for design-or-plan intents |
| 5 | **Body** — Requested deliverable or advisory outline | Yes |
| 6 | **Confidence** — High / Medium / Low + one-line rationale | Yes |
| 7 | **Dependencies** — Upstream/downstream/handoffs | When applicable |

## Clarification Questions

- Group by theme (business, data, security, integration, environments).
- Prioritize blockers first.
- Make questions answerable (closed or bounded open).
- Tie each question to the Thinking Model stage it unblocks.

Example:

```markdown
### Open questions
- **[Must][Stage 22]** Which permission set grants create on Case for the agent persona?
- **[Should][Stage 17]** Is the billing integration synchronous or async on Case close?
```

## Assumptions

```markdown
### Assumptions
- **A1:** Sharing model remains Private for Account. *Impact if wrong:* permission and regression scope expands.
- **A2:** No Apex trigger on Case beyond existing Flow X. *Impact if wrong:* add Apex path verification.
```

Rules:

- Never present assumptions as facts.
- Always state impact if false.
- Prefer asking over assuming when the item is a P0 blocker.

## Recommendation Prioritization

Use P0–P3 from [decision-framework.md](decision-framework.md). Lead with P0/P1. State **purpose** for automation and regression recommendations.

## Requirement Analysis Response (Sprint 2)

When a requirement is pasted for analysis, the **Body** must include the mandatory sections from [knowledge/requirement-analysis.md](../knowledge/requirement-analysis.md). Do **not** include detailed test cases or a full RTM.

## Test Design Response (Sprint 3)

When designing tests, the **Body** must follow [knowledge/test-design-engine.md](../knowledge/test-design-engine.md): techniques, scenario objectives, Quality Coverage Matrix, coverage gaps, regression scope, automation readiness. Recommended testing / regression / automation sections remain **intent only**—no case steps or scripts.

## Tone and Formatting

- Professional, concise, consulting-grade
- Nested bullets for criteria; tables for matrices
- Given/When/Then when expressing testable conditions (aligned with BA AC style)
- Relative links; no duplication of BA content
- Align formal artifacts to [shared/output-standards.md](../../shared/output-standards.md)

## Related Documents

- [brain.md](brain.md)
- [prompts.md](../prompts.md)
- [decision-framework.md](decision-framework.md)
- [thinking-model.md](thinking-model.md)

## Future Enhancements

- Audience variants (executive vs delivery) when communication pack lands

## Navigation

- **Previous:** [decision-framework.md](decision-framework.md)
- **Next:** [cross-module-map.md](cross-module-map.md)
- **See Also:** [prompts.md](../prompts.md)
