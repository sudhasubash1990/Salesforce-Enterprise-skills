---
title: Citation Policy
version: 0.2.0
tags: [framework-core, grounding]
status: draft
last_updated: 2026-10-09
---

# Citation Policy

## Purpose

Define when material claims require locators and how citations **SHOULD** be formatted.

## When citations are required

Agents **MUST** provide a citation or locator when:

1. Classification is `verified` or `requirement-derived`.
2. The claim is quantitative (SLA, volume, %, coverage, maturity score).
3. The claim is compliance- or regulatory-related.
4. The claim asserts a Salesforce product capability as available in a named edition/release without marking TBC.

Agents **SHOULD** cite when classifying `repository-guidance` with a SEACF path.

Agents **MAY** omit formal locators for clearly labelled `assumption`, `recommendation`, or `open-question` statements, provided the classification is explicit.

## Locator format

Prefer:

- Repository path + heading or requirement ID: `path/to/file.md#Section` or `BR-012`
- Document ID + page/section when external
- Short excerpt (≤25 words) only when necessary for dispute resolution

Agents **MUST NOT** fabricate citations, URLs, or requirement IDs.

## Related Documents

- [evidence-schema.md](evidence-schema.md)
- [grounding-policy.md](grounding-policy.md)
