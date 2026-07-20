"""Check that listed GEWINN slots remain weight-only rounded values."""

from __future__ import annotations

import json
from pathlib import Path

try:
    from .common import ROOT, read_csv
except ImportError:  # Script execution
    from common import ROOT, read_csv

POUNDS_PER_SLOT = 3.0
# Two pounds accepts the imported kit table's largest rounded departure while
# still rejecting values that encode non-weight burdens as slots.
ROUNDING_TOLERANCE_LB = 2.0


def validate_slots(root: Path = ROOT) -> list[str]:
    schemas = json.loads((root / "data/schemas/table_schemas.json").read_text(encoding="utf-8"))[
        "tables"
    ]
    errors: list[str] = []
    for relative in schemas:
        path = root / relative
        if not path.is_file():
            continue
        rows = read_csv(path)
        if not rows or "Weight_lb" not in rows[0] or "Slots" not in rows[0]:
            continue
        for number, row in enumerate(rows, start=2):
            weight = float(row["Weight_lb"])
            slots = float(row["Slots"])
            difference = abs(weight - slots * POUNDS_PER_SLOT)
            if difference > ROUNDING_TOLERANCE_LB + 1e-9:
                errors.append(
                    f"{relative}:{number}: {weight:g} lb and {slots:g} slots differ by {difference:g} lb "
                    f"(tolerance {ROUNDING_TOLERANCE_LB:g} lb)"
                )
    return errors


def main() -> int:
    errors = validate_slots()
    if errors:
        print("Weight-only slot validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(
        f"Slot validation passed ({POUNDS_PER_SLOT:g} lb/slot, ±{ROUNDING_TOLERANCE_LB:g} lb rounding tolerance)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
