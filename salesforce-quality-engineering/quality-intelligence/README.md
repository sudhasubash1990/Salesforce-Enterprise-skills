---
title: Quality Intelligence — README
module: Salesforce Quality Engineering
version: 0.9.1
tags: [quality-intelligence, sprint-7]
---

# Defect Intelligence & Quality Analytics Engine

## Purpose

Enable the AI to act as a **Quality Advisor**: analyse defects, perform RCA, detect patterns, interpret metrics, apply **decision rules**, predict risk, and recommend prevention across Salesforce delivery.

## Scope (Sprint 7)

**In scope:** Defect management, RCA methods, patterns, metrics, **rules engine (actionable IF/THEN)**, risk/trend/predictive analytics, continuous improvement, Salesforce hotspot intelligence, executive report standards.  

**Out of scope:** Fabricating metrics without data; replacing Sprint 5 templates (reuse them).

## Engine entry

- [defect-intelligence-engine.md](defect-intelligence-engine.md)
- [rules/](rules/README.md) — Quality Intelligence Rules Engine

## Folders

| Folder | Focus |
|--------|-------|
| [defect-management/](defect-management/README.md) | Lifecycle, severity, defect types |
| [root-cause-analysis/](root-cause-analysis/README.md) | 5 Whys, Fishbone, Pareto, FMEA, cause classes |
| [defect-patterns/](defect-patterns/README.md) | Pattern detection & prevention |
| [quality-metrics/](quality-metrics/README.md) | DRE, leakage, coverage, indices |
| [**rules/**](rules/README.md) | **Decision rules → actionable recommendations** |
| [risk-analysis/](risk-analysis/README.md) | Risk types & scoring |
| [trend-analysis/](trend-analysis/README.md) | Sprint/release/prod trends |
| [predictive-quality/](predictive-quality/README.md) | Predictions + confidence + mitigations |
| [continuous-improvement/](continuous-improvement/README.md) | Retro, CAPA, QIP, TPI |
| [quality-gates/](quality-gates/README.md) | Gate decision intelligence |
| [knowledge-base/](knowledge-base/README.md) | SF hotspots + executive reports |

## Navigation

- **Previous:** [../ado/README.md](../ado/README.md)
- **Next:** [defect-intelligence-engine.md](defect-intelligence-engine.md)
- **See Also:** [../skill.md](../skill.md)

## Related Documents

- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../knowledge/clouds/README.md)
- [Documentation Generator (Sprint 5)](../templates/README.md)
- [ADO Delivery Intelligence (Sprint 6)](../ado/README.md)
- [Defect Report Template](../templates/defect-report.md)
- [Defect RCA Template](../templates/defect-rca-report.md)
- [Rules Engine](rules/README.md)
