from pathlib import Path

from tools.generate_tables import generate_tables
from tools.validate_csv_schema import validate_all
from tools.validate_kits import validate_kits
from tools.validate_manifest import validate_manifest
from tools.validate_slots import validate_slots
from tools.validate_terms import validate_terms

ROOT = Path(__file__).resolve().parents[1]


def test_canonical_csv_schema_and_damage_types() -> None:
    assert validate_all(ROOT) == []


def test_weight_only_slots() -> None:
    assert validate_slots(ROOT) == []


def test_kit_totals() -> None:
    assert validate_kits(ROOT) == []


def test_manifest_paths_and_open_todos() -> None:
    assert validate_manifest(ROOT) == []


def test_term_scanner_allowlist(tmp_path: Path) -> None:
    for directory in ("manuscript/source", "data", "manuscript/generated", "manuscript/reference"):
        (tmp_path / directory).mkdir(parents=True, exist_ok=True)
    note = tmp_path / "manuscript/reference/historical-note.md"
    note.write_text("Arms Training is historical discussion.", encoding="utf-8")
    allowlist = tmp_path / "allowlist.tsv"
    allowlist.write_text(
        "manuscript/reference/historical-note.md\tArms Training\thistorical discussion\n",
        encoding="utf-8",
    )
    expected, current, _ = validate_terms(tmp_path, allowlist_path=allowlist)
    assert expected == []
    assert current == []


def test_table_generation_is_deterministic(tmp_path: Path) -> None:
    output = tmp_path / "tables"
    first = generate_tables(ROOT, output)
    first_contents = {path.name: path.read_bytes() for path in first}
    second = generate_tables(ROOT, output)
    assert [path.name for path in first] == [path.name for path in second]
    assert first_contents == {path.name: path.read_bytes() for path in second}
