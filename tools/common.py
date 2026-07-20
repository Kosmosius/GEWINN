"""Shared parsers and paths for GEWINN tooling."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAMAGE_TYPES = {
    "Slashing",
    "Piercing",
    "Bludgeoning",
    "Shot",
    "Burning",
    "Shocking",
    "Toxic",
    "Freezing",
}
OBSOLETE_DAMAGE_COLUMNS = {"cut", "point", "crush", "cut dr", "point dr", "crush dr"}
_DICE = re.compile(r"^(?:(?P<count>[1-9]\d*)d(?P<sides>[1-9]\d*))$")
_MONEY_PART = re.compile(r"(?:(?P<pounds>£\d+)|(?P<shillings>\d+s)|(?P<pence>\d+d))")


def parse_dice(value: str) -> tuple[int, int]:
    """Parse a positive NdN dice expression."""
    match = _DICE.fullmatch(value.strip())
    if not match:
        raise ValueError(f"invalid dice notation: {value!r}")
    return int(match.group("count")), int(match.group("sides"))


def is_valid_dice(value: str, *, allow_alternatives: bool = True) -> bool:
    """Accept NdN, optionally allowing slash-separated weapon alternatives."""
    values = value.split("/") if allow_alternatives else [value]
    try:
        for part in values:
            parse_dice(part)
    except ValueError:
        return False
    return bool(values)


def split_damage_types(value: str) -> list[str]:
    return [part.strip() for part in re.split(r"[;/]", value) if part.strip()]


def is_valid_money(value: str) -> bool:
    """Validate £/s/d strings, an en-dash range, or an em dash for no price."""
    value = value.strip()
    if value == "—":
        return True
    if "–" in value:
        start, end = value.split("–", 1)
        return is_valid_money(start) and is_valid_money(end)
    parts = _MONEY_PART.findall(value)
    if not parts:
        return False
    matched = " ".join(match.group(0) for match in _MONEY_PART.finditer(value))
    return matched == value and len(parts) == len(set(parts))


def money_to_pence(value: str) -> int:
    """Convert a fixed £/s/d value to pence. Ranges and em dashes are not sums."""
    if not is_valid_money(value) or value.strip() == "—" or "–" in value:
        raise ValueError(f"not a fixed money value: {value!r}")
    total = 0
    for match in _MONEY_PART.finditer(value):
        token = match.group(0)
        if token.startswith("£"):
            total += int(token[1:]) * 240
        elif token.endswith("s"):
            total += int(token[:-1]) * 12
        else:
            total += int(token[:-1])
    return total


def format_money(pence: int) -> str:
    """Format a non-negative pence total using the canonical £/s/d notation."""
    if pence < 0:
        raise ValueError("money cannot be negative")
    pounds, remainder = divmod(pence, 240)
    shillings, pennies = divmod(remainder, 12)
    parts: list[str] = []
    if pounds:
        parts.append(f"£{pounds}")
    if shillings:
        parts.append(f"{shillings}s")
    if pennies or not parts:
        parts.append(f"{pennies}d")
    return " ".join(parts)


def read_csv(path: Path):
    import csv

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))
