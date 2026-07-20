# GEWINN

GEWINN is a classless, level-less, no-HP tabletop role-playing game about wounds, armor, Stress, equipment, and expeditions: war, conflict, gain, and profit. This repository preserves its designer-authored v2.5 identity while providing a safe workspace for a future current-rules migration.

## Status

The current editable manuscript is an untouched v2.5 DOCX baseline. The v2.5-to-current migration bundle and numerical data have been installed, but **the rules migration has not been applied**. See `docs/PROJECT_STATUS.md` and `manuscript/source/MANUSCRIPT_STATUS.md`.

## Repository map

| Location | Purpose |
| --- | --- |
| `manuscript/source/` | Editable canonical manuscript baseline. |
| `manuscript/generated/` | Generated Markdown tables; never edit directly. |
| `migration/v2.5-current/` | Current migration manifest, changelog, and bundle README. |
| `data/equipment/`, `data/magic/` | Numerical source of truth. |
| `tools/`, `tests/` | Validators, generators, and regression tests. |
| `simulations/` | Reproducible simulation registry and smoke harness. |
| `playtest/` | Versioned report and issue templates. |
| `archive/` | Immutable historical evidence; never edit it. |
| `artifacts/raw/` | Ignored large reproducible raw output, listed in `artifacts/MANIFEST.md`. |

## Canonical-source hierarchy

1. `migration/v2.5-current/GEWINN_v2_5_to_current_CHANGE_MANIFEST.yaml`
2. `migration/v2.5-current/GEWINN_v2_5_to_current_CODEX_CHANGELOG.md`
3. Canonical CSV files under `data/`
4. Latest explicit designer decisions already encoded in the migration bundle
5. GEWINN v5.0 as a procedural scaffold only
6. GEWINN v2.5 as the voice, identity, attribution, front matter, and discrete-wound source
7. All other drafts and experiments as non-authoritative history

Read `docs/CANONICAL_SOURCES.md` and `AGENTS.md` before editing rules. The v5 manuscript is never a final canonical rules source.

## Quick start

Use Python 3.11 or newer. On Windows, after selecting a suitable interpreter:

```text
make PYTHON=C:/path/to/python.exe bootstrap
make PYTHON=./.venv/Scripts/python.exe check
make PYTHON=./.venv/Scripts/python.exe status
```

Direct Python equivalents (for systems without `make`) are:

```text
python -m venv .venv
.venv/Scripts/python.exe -m pip install -e ".[dev]"
.venv/Scripts/python.exe -m ruff check .
.venv/Scripts/python.exe -m pytest -p no:cacheprovider
.venv/Scripts/python.exe tools/generate_tables.py
.venv/Scripts/python.exe tools/validate_manifest.py
.venv/Scripts/python.exe tools/validate_csv_schema.py
.venv/Scripts/python.exe tools/validate_slots.py
.venv/Scripts/python.exe tools/validate_kits.py
.venv/Scripts/python.exe tools/validate_terms.py
.venv/Scripts/python.exe simulations/src/smoke.py --config simulations/configs/smoke.json
```

`uv` was not available during bootstrap, so no lockfile is committed. The documented virtual-environment workflow is the supported local setup.

## Workflows

- **Manuscript:** edit only `manuscript/source/` in an explicitly scoped migration commit. Generate tables rather than editing `manuscript/generated/`.
- **Data:** edit a canonical CSV only with validation, regenerated tables, relevant simulation-baseline review, and a `CHANGELOG.md` entry.
- **Simulation:** record seed, trials, assumptions, source-rules commit, and output paths in `simulations/registry.yaml`. Run `make sim-smoke`; do not put full simulations in routine checks.
- **Playtest:** record the rules commit and manuscript version in a session report, then file reproducible issues or balance observations separately.
- **Archive:** treat every archived file as immutable evidence, not a rules source. Create a working copy outside `archive/` when needed.

No license file was present in the imported repository. Do not infer or add one without the rights holder’s instruction; preserved attribution and source material remain in the v2.5 archive.
