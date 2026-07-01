#!/usr/bin/env python3
"""
Deprecated shim — use output-engine/convert.py instead.

This module delegates to the Enterprise Output Engine orchestrator.
"""

from __future__ import annotations

import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ENGINE_DIR))

from convert import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
