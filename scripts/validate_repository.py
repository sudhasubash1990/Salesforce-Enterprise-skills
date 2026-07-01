"""Sprint 8 — full repository validation (structure + metadata)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BA = REPO / "salesforce-business-analyst"

REQUIRED_BA_DIRS = [
    "brain",
    "knowledge",
    "templates",
    "playbooks",
    "scenarios",
    "interview-guide",
    "validation",
]

REQUIRED_BA_FILES = [
    "skill.md",
    "checklists.md",
    "brain/validation-framework.md",
    "validation/README.md",
    "validation/enterprise-validation-framework.md",
]


def check_structure() -> list[str]:
    errors: list[str] = []
    if not BA.is_dir():
        errors.append(f"Missing skill root: {BA}")
        return errors
    for name in REQUIRED_BA_DIRS:
        path = BA / name
        if not path.is_dir():
            errors.append(f"Missing required directory: salesforce-business-analyst/{name}/")
    for rel in REQUIRED_BA_FILES:
        path = BA / rel
        if not path.is_file():
            errors.append(f"Missing required file: salesforce-business-analyst/{rel}")
    return errors


def run_metadata_validation() -> tuple[int, str]:
    script = REPO / "scripts" / "validate_metadata.py"
    result = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
        text=True,
        cwd=str(REPO),
    )
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode, output


def main() -> int:
    print("Sprint 8 Enterprise Repository Validation")
    print("=" * 40)

    struct_errors = check_structure()
    if struct_errors:
        print(f"STRUCTURE: FAIL ({len(struct_errors)} issues)")
        for e in struct_errors:
            print(f"  - {e}")
    else:
        print("STRUCTURE: PASS")

    print()
    print("Running metadata validation...")
    meta_code, meta_out = run_metadata_validation()
    print(meta_out.rstrip())
    meta_ok = meta_code == 0

    print()
    print("=" * 40)
    if struct_errors or not meta_ok:
        print("OVERALL: FAIL — repository not enterprise-ready")
        return 1
    print("OVERALL: PASS — repository enterprise-ready")
    return 0


if __name__ == "__main__":
    sys.exit(main())
