"""Safe file output helpers for locked or synced paths."""

from __future__ import annotations

import os
import tempfile
import time
from collections.abc import Callable
from pathlib import Path


def write_via_temp(output_path: Path, write_fn: Callable[[Path], None], retries: int = 5) -> None:
    """Write to a temp file, then replace the target (handles OneDrive locks)."""
    fd, temp_name = tempfile.mkstemp(suffix=output_path.suffix, dir=output_path.parent)
    os.close(fd)
    temp_path = Path(temp_name)
    try:
        write_fn(temp_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        last_err: OSError | None = None
        for _ in range(retries):
            try:
                temp_path.replace(output_path)
                return
            except OSError as exc:
                last_err = exc
                time.sleep(1)
        if last_err:
            raise last_err
    finally:
        if temp_path.exists():
            try:
                temp_path.unlink()
            except OSError:
                pass
