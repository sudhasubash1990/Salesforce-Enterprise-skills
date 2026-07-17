---
title: Quality Philosophy
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
  - salesforce-quality-engineering/brain/consulting-principles.md
  - salesforce-quality-engineering/brain/brain.md
keywords: [philosophy, principles]
tags: [brain, philosophy]
---

# Quality Engineering Philosophy

**Purpose:** Define the quality philosophy and principles that govern every QE recommendation.

**Scope:** Principles only. Reasoning stages live in [thinking-model.md](thinking-model.md); decisions in [decision-framework.md](decision-framework.md).

**Owner:** QE Practice Lead

**Version:** 0.2.1

**Status:** Draft (Sprint 1 — modular Brain)

---

## Philosophy

Quality is a **continuous consulting capability**, not a late-phase test factory.

- Every user story should be testable.
- Every material risk should have a mitigation path.
- Every release decision should be evidence-based.
- Every defect should teach the system.
- AI accelerates analysis and drafting; humans own decisions and evidence.

## Principles

| Principle | Meaning |
|-----------|---------|
| **Business First** | Quality serves business outcomes, not test counts |
| **Quality Built In** | Shift quality into requirements, design, and build—not only execute |
| **Risk-Based Testing** | Depth follows risk and impact, not equal effort everywhere |
| **Shift Left Testing** | Review stories/AC early; find defects before code freezes |
| **Requirement Driven Testing** | Trace tests to requirements/stories/AC; no orphan cases |
| **End-to-End Thinking** | Journey, data, integration, security, and ops—not isolated screens |
| **Reusable Assets** | Prefer reusable scenarios, data patterns, and packs over one-offs |
| **Automation with Purpose** | Automate for speed, confidence, and regression ROI—not vanity |
| **Production Focus** | Release readiness and production validation close the loop |
| **Continuous Improvement** | Defects and escapes feed process and pack improvement |
| **Customer Value** | Protect customer experience and trust |
| **AI Assisted Quality Engineering** | AI accelerates analysis and drafting; humans own decisions and evidence |

## Related Documents

- [skill.md](../skill.md)
- [consulting-principles.md](consulting-principles.md)
- [brain.md](brain.md)

## Future Enhancements

- Link principles to metric categories in [../knowledge/metrics.md](../knowledge/metrics.md) when formulas land

## Navigation

- **Previous:** [skill.md](../skill.md)
- **Next:** [consulting-principles.md](consulting-principles.md)
- **See Also:** [thinking-model.md](thinking-model.md)
