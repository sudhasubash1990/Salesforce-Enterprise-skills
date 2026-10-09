---
title: Privacy and Data Handling
version: 0.2.0
tags: [framework-core, responsible-ai]
status: draft
last_updated: 2026-10-09
---

# Privacy and Data Handling

## Purpose

Data minimization, purpose limitation, and masking for SEACF agents.

## Normative rules

1. Agents **MUST** practice **data minimization**: load only data needed for the stated user task.
2. Agents **MUST** apply **purpose limitation**: do not reuse customer/production data for unrelated tasks without authorization.
3. Customer / production data **MUST** be masked in generated examples unless the user provides sanitized data.
4. Credentials and secrets **MUST NOT** appear in outputs. See [secrets-and-data-handling.md](../security/secrets-and-data-handling.md).
5. Agents **SHOULD** prefer fictional personas and org names in examples.
6. Regulatory privacy claims **MUST** be marked TBC with Legal/Compliance unless confirmed.

## Related Documents

- [principles.md](principles.md)
- [../../docs/security-guidelines.md](../../docs/security-guidelines.md)