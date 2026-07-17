---
title: Deliverable Selection Logic
version: 0.7.0
---

# Deliverable Selection Logic

| Situation | Prefer | Avoid |
|-----------|--------|-------|
| New program / major release | Test Strategy + Plan | Jumping to cases only |
| Single story clarification | Requirement Review Report | Full RTM rebuild |
| Need coverage proof | RTM (appropriate view) | Unlinked case dumps |
| Design complete, need execution | Scenario doc → Cases | Cases without objectives |
| Deploy tonight | Smoke + Deployment Validation | Full regression unless risk says so |
| Release decision | Readiness + Go/No-Go + Summary | Dashboard without evidence |
| Production escape | Defect + RCA | Closing without preventive actions |
| Automation ask | Candidate Matrix + Assessment | Scripts without candidates |
| UAT start | UAT + Entry Criteria | Starting without environment readiness |

## Project type tailoring

| Project type | Tailoring |
|--------------|-----------|
| Agile sprint | Lightweight plan; Sprint RTM; daily status |
| SAFe ART | Strategy per PI; Release RTM; dashboards |
| Waterfall / gated | Full strategy/plan; formal entry/exit; approvals |
| Package upgrade | Upgrade-focused regression + smoke; vendor notes |
| Integration-heavy | SIT checklist + integration defect fields |

## Related

- [document-intelligence.md](document-intelligence.md)
- [../templates/README.md](../templates/README.md)
