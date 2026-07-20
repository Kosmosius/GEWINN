"""Validate canonical GEWINN CSV tables against their checked-in schemas."""

from __future__ import annotations

import csv
import json
from pathlib import Path

try:
    from .common import (
        DAMAGE_TYPES,
        OBSOLETE_DAMAGE_COLUMNS,
        ROOT,
        is_valid_dice,
        is_valid_money,
        split_damage_types,
    )
except ImportError:  # Script execution: python tools/validate_csv_schema.py
    from common import (
        DAMAGE_TYPES,
        OBSOLETE_DAMAGE_COLUMNS,
        ROOT,
        is_valid_dice,
        is_valid_money,
        split_damage_types,
    )

SCHEMA_PATH = ROOT / "data/schemas/table_schemas.json"


def load_schemas(root: Path = ROOT) -> dict:
    return json.loads((root / "data/schemas/table_schemas.json").read_text(encoding="utf-8"))


def validate_table(path: Path, spec: dict) -> list[str]:
    errors: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        rows = list(reader)

    missing = [column for column in spec["required_columns"] if column not in headers]
    if missing:
        return [f"{path.relative_to(ROOT)}: missing required columns: {', '.join(missing)}"]

    obsolete = [
        column for column in headers if column.strip().casefold() in OBSOLETE_DAMAGE_COLUMNS
    ]
    if obsolete:
        errors.append(
            f"{path.relative_to(ROOT)}: obsolete damage-type columns: {', '.join(obsolete)}"
        )

    names: set[str] = set()
    name_column = spec["name_column"]
    for number, row in enumerate(rows, start=2):
        label = row[name_column].strip()
        if not label:
            errors.append(f"{path.relative_to(ROOT)}:{number}: missing {name_column}")
        elif label.casefold() in names:
            errors.append(f"{path.relative_to(ROOT)}:{number}: duplicate {name_column} {label!r}")
        else:
            names.add(label.casefold())

        for column in spec["required_columns"]:
            if not row.get(column, "").strip():
                errors.append(f"{path.relative_to(ROOT)}:{number}: missing mandatory {column}")

        for column in spec.get("dice_columns", []):
            if row.get(column) and not is_valid_dice(row[column]):
                errors.append(
                    f"{path.relative_to(ROOT)}:{number}: invalid dice in {column}: {row[column]!r}"
                )

        for column in spec.get("damage_value_columns", []):
            values = split_damage_types(row.get(column, ""))
            invalid = [value for value in values if value not in DAMAGE_TYPES]
            if not values or invalid:
                errors.append(
                    f"{path.relative_to(ROOT)}:{number}: invalid damage types in {column}: {invalid or row[column]!r}"
                )

        for column in ("Weight_lb", "Slots"):
            if column not in headers:
                continue
            try:
                value = float(row[column])
                if value < 0:
                    raise ValueError
            except ValueError:
                errors.append(
                    f"{path.relative_to(ROOT)}:{number}: {column} must be a non-negative number"
                )

        if "Cost" in headers and not is_valid_money(row["Cost"]):
            errors.append(f"{path.relative_to(ROOT)}:{number}: invalid £/s/d cost {row['Cost']!r}")

        if "Reload" in headers and row["Reload"] != "—":
            try:
                if int(row["Reload"]) < 0:
                    raise ValueError
            except ValueError:
                errors.append(
                    f"{path.relative_to(ROOT)}:{number}: Reload must be a non-negative integer or em dash"
                )

    return errors


def validate_all(root: Path = ROOT) -> list[str]:
    schemas = load_schemas(root)["tables"]
    errors: list[str] = []
    global_items: dict[str, str] = {}
    for relative, spec in schemas.items():
        path = root / relative
        if not path.is_file():
            errors.append(f"missing canonical table: {relative}")
            continue
        errors.extend(validate_table(path, spec))
        if spec["name_column"] == "Rating":
            continue
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                item = row[spec["name_column"]].strip().casefold()
                if item in global_items:
                    errors.append(
                        f"duplicate canonical item {row[spec['name_column']]!r}: {relative} and {global_items[item]}"
                    )
                else:
                    global_items[item] = relative
    return errors


def main() -> int:
    errors = validate_all()
    if errors:
        print("CSV schema validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("CSV schema validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
