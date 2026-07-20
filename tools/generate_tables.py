"""Deterministically generate Markdown tables from canonical GEWINN CSV data."""

from __future__ import annotations

import csv
from pathlib import Path

try:
    from .common import ROOT
except ImportError:  # Script execution
    from common import ROOT

DATA_DIRECTORIES = ("data/equipment", "data/magic")


def escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render_table(relative_source: str, headers: list[str], rows: list[dict[str, str]]) -> str:
    lines = [
        "<!-- GENERATED FILE — DO NOT EDIT DIRECTLY.",
        f"     Source: {relative_source}",
        "     Regenerate: python tools/generate_tables.py -->",
        "",
        "| " + " | ".join(escape_cell(header) for header in headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    lines.extend(
        "| " + " | ".join(escape_cell(row[header]) for header in headers) + " |" for row in rows
    )
    return "\n".join(lines) + "\n"


def generate_tables(root: Path = ROOT, output_dir: Path | None = None) -> list[Path]:
    output = output_dir or root / "manuscript/generated/tables"
    output.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []
    for directory in DATA_DIRECTORIES:
        for source in sorted((root / directory).glob("*.csv")):
            with source.open("r", encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle)
                headers = reader.fieldnames or []
                rows = list(reader)
            destination = output / f"{source.stem}.md"
            content = render_table(source.relative_to(root).as_posix(), headers, rows)
            if not destination.exists() or destination.read_text(encoding="utf-8") != content:
                destination.write_text(content, encoding="utf-8", newline="\n")
            created.append(destination)
    return created


def main() -> int:
    created = generate_tables()
    print(f"Generated {len(created)} Markdown tables in manuscript/generated/tables/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
