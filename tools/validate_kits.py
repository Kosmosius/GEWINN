"""Recalculate common armor-kit totals from canonical component tables."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

try:
    from .common import ROOT, money_to_pence, read_csv
except ImportError:  # Script execution
    from common import ROOT, money_to_pence, read_csv

PHYSICAL_TABLES = (
    "data/equipment/body_armor.csv",
    "data/equipment/helmets.csv",
    "data/equipment/arms_armor.csv",
    "data/equipment/leg_armor.csv",
    "data/equipment/shields.csv",
)
DAMAGE_COLUMNS = ("Slashing", "Piercing", "Bludgeoning", "Shot")


@dataclass(frozen=True)
class Totals:
    cost: int = 0
    weight: float = 0.0
    slots: float = 0.0
    ac_melee: int = 0
    ac_missile: int = 0
    slashing: int = 0
    piercing: int = 0
    bludgeoning: int = 0
    shot: int = 0

    def add(self, other: Totals) -> Totals:
        return Totals(
            cost=self.cost + other.cost,
            weight=self.weight + other.weight,
            slots=self.slots + other.slots,
            ac_melee=self.ac_melee + other.ac_melee,
            ac_missile=self.ac_missile + other.ac_missile,
            slashing=self.slashing + other.slashing,
            piercing=self.piercing + other.piercing,
            bludgeoning=self.bludgeoning + other.bludgeoning,
            shot=self.shot + other.shot,
        )


def parse_ac(value: str) -> tuple[int, int]:
    value = value.strip()
    if value == "cover":
        return 0, 0
    if value.lstrip("+").isdigit():
        amount = int(value.lstrip("+"))
        return amount, amount
    melee = missile = 0
    for segment in value.split("/"):
        amount_text, target = segment.strip().split(maxsplit=1)
        amount = int(amount_text.lstrip("+"))
        if target == "melee":
            melee = amount
        elif target == "missile":
            missile = amount
        else:
            raise ValueError(f"unsupported AC target {target!r}")
    return melee, missile


def item_totals(row: dict[str, str]) -> Totals:
    melee, missile = parse_ac(row["AC"])
    cost = 0 if row["Cost"] == "—" else money_to_pence(row["Cost"])
    return Totals(
        cost=cost,
        weight=float(row["Weight_lb"]),
        slots=float(row["Slots"]),
        ac_melee=melee,
        ac_missile=missile,
        slashing=int(row["Slashing"]),
        piercing=int(row["Piercing"]),
        bludgeoning=int(row["Bludgeoning"]),
        shot=int(row["Shot"]),
    )


def expected_kit_totals(root: Path = ROOT) -> dict[str, Totals]:
    schema = json.loads((root / "data/schemas/table_schemas.json").read_text(encoding="utf-8"))
    aliases = schema["component_aliases"]
    components: dict[str, dict[str, str]] = {}
    for relative in PHYSICAL_TABLES:
        for row in read_csv(root / relative):
            name = next(
                key
                for key in row
                if key
                not in {
                    "AC",
                    *DAMAGE_COLUMNS,
                    "Burning",
                    "Shocking",
                    "Toxic",
                    "Freezing",
                    "Weight_lb",
                    "Slots",
                    "Cost",
                    "Notes",
                }
            )
            components[row[name]] = row

    kit_rows = read_csv(root / "data/equipment/common_armor_kits.csv")
    by_name = {row["Kit"]: row for row in kit_rows}
    resolved: dict[str, Totals] = {}
    resolving: set[str] = set()

    def resolve(name: str) -> Totals:
        name = aliases.get(name, name)
        if name in components:
            return item_totals(components[name])
        if name in resolved:
            return resolved[name]
        if name not in by_name:
            raise KeyError(f"unknown kit component {name!r}")
        if name in resolving:
            raise ValueError(f"cyclic kit reference at {name!r}")
        resolving.add(name)
        total = Totals()
        for piece in by_name[name]["Pieces"].split(";"):
            total = total.add(resolve(piece.strip()))
        resolving.remove(name)
        resolved[name] = total
        return total

    return {name: resolve(name) for name in by_name}


def validate_kits(root: Path = ROOT) -> list[str]:
    try:
        expected = expected_kit_totals(root)
    except (KeyError, ValueError) as error:
        return [str(error)]
    errors: list[str] = []
    for number, row in enumerate(read_csv(root / "data/equipment/common_armor_kits.csv"), start=2):
        actual = Totals(
            cost=money_to_pence(row["Cost"]),
            weight=float(row["Weight_lb"]),
            slots=float(row["Slots"]),
            ac_melee=int(row["AC_melee"]),
            ac_missile=int(row["AC_missile"]),
            slashing=int(row["Slashing"]),
            piercing=int(row["Piercing"]),
            bludgeoning=int(row["Bludgeoning"]),
            shot=int(row["Shot"]),
        )
        calculated = expected[row["Kit"]]
        if actual != calculated:
            errors.append(
                f"data/equipment/common_armor_kits.csv:{number}: {row['Kit']!r} totals do not match components "
                f"(listed {actual}; calculated {calculated})"
            )
    return errors


def main() -> int:
    errors = validate_kits()
    if errors:
        print("Armor-kit validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("Armor-kit totals match canonical components.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
