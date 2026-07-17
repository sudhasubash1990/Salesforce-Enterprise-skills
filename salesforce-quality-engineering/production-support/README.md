---
title: Production Support — README
module: Salesforce Quality Engineering
version: 0.11.1
tags: [production-support, sprint-9]
---

# Production Support, Release Operations & Operational Excellence

> **Module identity:** This folder is the **QE Sprint 9 ops pack** inside SEACF Module 2. It is **not** the planned standalone `salesforce-production-support/` module. See [framework-core/MODULE-INTEGRATION.md](../../framework-core/MODULE-INTEGRATION.md).

## Purpose

Enable the AI to act as a **Production Support Lead / Release Manager / Service Delivery Consultant**: assess go-live readiness, run hypercare, manage incidents/problems/changes, operate releases, monitor health, apply **operations intelligence**, and drive operational excellence for Salesforce.

## Scope (Sprint 9)

**In scope:** Go-live, hypercare, ITIL-aligned service practices, release operations, monitoring, environments, knowledge, operational excellence, runbooks, Salesforce production intelligence, operational analytics, executive reporting, **operations intelligence** (health, anomalies, predictions, decisions).

**Out of scope:** Inventing SLA/MTTR/KPI values; replacing Sprint 7 defect RCA engine (reuse it); full Apex fix implementation; acting as a substitute for the future standalone Production Support SEACF module.

## Engine entry

- [production-support-engine.md](production-support-engine.md)
- [operations-intelligence/](operations-intelligence/README.md) — Operations Intelligence Engine

## Folders

| Folder | Focus |
|--------|-------|
| [Go-Live](go-live/README.md) | Prepare and execute Salesforce go-live with evidence-based Go/No-Go decisions. |
| [Hypercare](hypercare/README.md) | Stabilize production immediately after go-live with structured hypercare. |
| [Incident Management](incident-management/README.md) | Restore service quickly with disciplined Salesforce incident management. |
| [Problem Management](problem-management/README.md) | Find and remove root causes; reduce recurring production pain. |
| [Change Management](change-management/README.md) | Control Salesforce production change risk with ITIL-aligned change practice. |
| [Release Operations](release-operations/README.md) | Operate Salesforce releases safely from calendar through monitoring and rollback. |
| [Monitoring](monitoring/README.md) | Detect Salesforce production risk early through layered monitoring. |
| [Service Management](service-management/README.md) | Align Salesforce support with ITIL-oriented service management practices. |
| [Environment Management](environment-management/README.md) | Govern Salesforce environments from Dev through Production. |
| [Knowledge Management](knowledge-management/README.md) | Capture and reuse operational knowledge for faster, safer support. |
| [Operational Excellence](operational-excellence/README.md) | Drive continuous improvement of Salesforce production reliability and support health. |
| [Support Playbooks](support-playbooks/README.md) | Ceremony and workflow playbooks for production support teams. |
| [Operational Analytics](operational-analytics/README.md) | Analyze production and support signals for risk and improvement. |
| [Executive Reporting](executive-reporting/README.md) | Standard operational and executive reports for Salesforce production support. |
| [runbooks/](runbooks/README.md) | Reusable operational runbooks |
| [salesforce/](salesforce/README.md) | Salesforce production troubleshooting intelligence |
| [**operations-intelligence/**](operations-intelligence/README.md) | **Health, anomalies, predictions, ops decisions & recommendations** |

## ITIL coverage

Incidents · Problems · Changes · Service requests · Knowledge · SLA/OLA · Continual improvement (practice-level alignment).

## Runbook library

See [runbooks/](runbooks/README.md) — deployment, major incident, integration/batch/API/Flow failures, rollback, emergency support, and more.

## Monitoring

Layered Salesforce health, jobs, Flow, events, integrations, security, performance — [monitoring/](monitoring/README.md).

## Navigation

- **Previous:** [../automation-intelligence/README.md](../automation-intelligence/README.md)
- **Next:** [production-support-engine.md](production-support-engine.md)
- **See Also:** [../skill.md](../skill.md)

## Related Documents

- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../knowledge/clouds/README.md)
- [Documentation Generator (Sprint 5)](../templates/README.md)
- [ADO Delivery Intelligence (Sprint 6)](../ado/README.md)
- [Defect Intelligence (Sprint 7)](../quality-intelligence/README.md)
- [Automation Intelligence (Sprint 8)](../automation-intelligence/README.md)
- [Sprint 5 Hypercare / Prod Val templates](../templates/README.md)
- [Sprint 7 RCA](../quality-intelligence/root-cause-analysis/README.md)
