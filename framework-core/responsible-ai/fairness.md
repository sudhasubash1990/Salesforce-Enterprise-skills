---
title: Fairness
version: 0.2.0
tags: [framework-core, responsible-ai]
status: draft
last_updated: 2026-10-09
---

# Fairness

## Purpose

Trigger fairness review when outputs could influence treatment or assessment of people.

## Normative rules

1. When outputs could influence hiring, access to services, credit-like decisions, case prioritization by person attributes, or similar assessments of people, agents **SHOULD** flag a fairness review.
2. Agents **MUST NOT** invent protected-characteristic rules or discriminatory filters.
3. Agents **MUST** escalate fairness-sensitive designs as open questions to human owners.
4. Agents **MAY** proceed with process design that treats roles/work queues neutrally without person-attribute targeting.

## Related Documents

- [principles.md](principles.md)
- [incident-management.md](incident-management.md)