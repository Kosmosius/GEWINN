"""Validate migration-bundle paths, TODO preservation, and source documentation."""

from __future__ import annotations

from pathlib import Path

import yaml

try:
    from .common import ROOT
except ImportError:  # Script execution
    from common import ROOT

MANIFEST = Path("migration/v2.5-current/GEWINN_v2_5_to_current_CHANGE_MANIFEST.yaml")


def load_manifest(root: Path = ROOT) -> dict:
    return yaml.safe_load((root / MANIFEST).read_text(encoding="utf-8-sig"))


def validate_manifest(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    manifest = load_manifest(root)
    for relative in manifest.get("data_files", []):
        candidate = Path(relative)
        if candidate.is_absolute() or ".." in candidate.parts:
            errors.append(f"manifest path must be repository-relative: {relative}")
        elif not (root / candidate).is_file():
            errors.append(f"manifest names missing data file: {relative}")

    questions = (root / "docs/OPEN_QUESTIONS.md").read_text(encoding="utf-8")
    for todo in manifest.get("open_todos", []):
        if todo not in questions:
            errors.append(f"manifest TODO is absent from docs/OPEN_QUESTIONS.md: {todo}")

    documented = (root / "docs/CANONICAL_SOURCES.md").read_text(encoding="utf-8")
    operating = (root / "AGENTS.md").read_text(encoding="utf-8")
    required_hierarchy = (
        "GEWINN_v2_5_to_current_CHANGE_MANIFEST.yaml",
        "GEWINN_v2_5_to_current_CODEX_CHANGELOG.md",
        "Canonical CSV files under `data/`",
        "Latest explicit designer decisions already encoded in the migration bundle",
        "GEWINN v5.0 as a procedural scaffold only",
        "GEWINN v2.5 as the voice, identity, attribution, front matter, and",
        "All other drafts and experiments as non-authoritative history",
    )
    for entry in required_hierarchy:
        if entry not in documented or entry not in operating:
            errors.append(f"source priority is not documented consistently: {entry}")
    return errors


def main() -> int:
    try:
        errors = validate_manifest()
    except (OSError, yaml.YAMLError) as error:
        print(f"Manifest validation infrastructure failure: {error}")
        return 2
    if errors:
        print("Manifest validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("Migration manifest validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
