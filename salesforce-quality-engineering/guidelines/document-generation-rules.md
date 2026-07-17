---
title: Document Generation Rules
version: 0.7.0
---

# Document Generation Rules

## Hard rules

1. **Never create unnecessary documents** — use [deliverable-selection.md](deliverable-selection.md).
2. **Lifecycle-based** — generate what the phase requires.
3. **Reuse** — pull from Requirement Analysis and Test Design outputs; do not rewrite from scratch.
4. **No duplicate content** — link related artifacts; summarize deltas only.
5. **Traceability** — preserve IDs across RTM, scenarios, cases, defects.
6. **Consistent formatting** — Markdown tables; consulting tone; no client PII/credentials.
7. **Enterprise governance** — include owner, version, status, approval where required.
8. **Analysis before heavy docs** — Strategy/Plan/RTM/Cases require Sprint 2 (± Sprint 3) unless user explicitly provides ready inputs.
9. **No silent invention** — mark assumptions; do not invent regulatory requirements.
10. **Export awareness** — structure for ADO / Jira / Excel; Sprint 6 deepens ADO publish.

## Tooling notes

| Target | Guidance |
|--------|----------|
| Markdown | Source of truth in repo / `outputs/<project>/` |
| Excel | Tables map 1:1 from template sections |
| Azure DevOps | Cases/defects as work items (Sprint 6) |
| Jira Xray / Zephyr | Preserve step/expected columns |

## Related

- [template-standards.md](template-standards.md)
