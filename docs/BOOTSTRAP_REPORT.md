# GEWINN bootstrap report

## 1. Branch

`chore/repo-bootstrap`, created locally from `main` at `16bc0a1`.

## 2. Commits created

1. `a779df3` `chore: establish GEWINN repository structure`
2. `e29e1a9` `data: install canonical GEWINN rules tables`
3. `a0ab3fc` `chore: archive historical manuscripts reports and simulations`
4. `9f89c3c` `docs: establish canonical manuscript workspace`
5. `ea30ddd` `docs: add Codex and contributor operating rules`
6. `f2102ae` `build: add reproducible GEWINN tooling environment`
7. `fdff45e` `test: add GEWINN manuscript data and regression validation`
8. `efdd500` `sim: normalize GEWINN simulation registry and reproducibility`
9. `92ac107` `playtest: add versioned session and rules issue workflow`
10. `adaea09` `chore: tidy playtest issue template whitespace`
11. `ea97724` `docs: document GEWINN project workflow and architecture`
12. `chore: complete GEWINN repository bootstrap` (this report and final verification)

## 3. Final repository tree

```text
GEWINN/
├── AGENTS.md  CONTRIBUTING.md  CHANGELOG.md  README.md  Makefile  pyproject.toml
├── docs/                 project status, workflow, canonical sources, ADRs, reports
├── manuscript/           source baseline, ignored generated tables, working references
├── migration/v2.5-current/  migration README, changelog, manifest
├── data/                 canonical equipment/magic CSVs, schemas, derived area
├── tools/  tests/        validation, table generation, regression coverage
├── simulations/          registry, deterministic smoke harness, configs, results policy
├── playtest/             session and issue templates
├── archive/              immutable v2.5 evidence and imported reports
└── artifacts/            raw-output manifest; ignored raw and temporary directories
```

`LICENSE.md` is intentionally absent: no source license file was imported and
none was invented.

## 4. Canonical manuscript source

The one selected editable baseline is
`manuscript/source/GEWINN_v2.5.docx`, SHA-256
`3eab84db994de4d246457a4afa55fee5a51eb3f0aa61c2da605b518e7124bc71`.
It is a byte-preserved copy of the immutable original at
`archive/v2.5-baseline/GEWINN_v2.5.docx`. The migration is not applied.

## 5. Authoritative data paths

- `data/equipment/melee_weapons.csv`
- `data/equipment/ranged_weapons.csv`
- `data/equipment/body_armor.csv`
- `data/equipment/helmets.csv`
- `data/equipment/arms_armor.csv`
- `data/equipment/leg_armor.csv`
- `data/equipment/shields.csv`
- `data/equipment/proofing.csv`
- `data/equipment/common_armor_kits.csv`
- `data/magic/occult_implements.csv`
- `data/magic/sacred_relics.csv`

## 6. Archived sources

- v2.5 DOCX, PDF, and historical art: `archive/v2.5-baseline/`
- Prior report and consolidated update: `archive/imported-reports/`
- No v5 scaffold, superseded drafts, simulation source, ZIP, or raw simulation
  table was present in the import. The corresponding archive locations are
  retained empty for a future evidence-preserving import.

## 7. Simulation registry

`simulations/registry.yaml` has one entry:
`bootstrap-reproducibility-smoke`. It uses seed `25072026` and 24 trials to
verify deterministic execution and canonical-data access. It is not a GEWINN
combat or balance model; no imported simulation mathematics existed to retain.

## 8. Environment and setup

Use Python 3.11 or newer. `uv` was not locally available, so this repository
uses a documented virtual-environment setup rather than a lockfile:

```text
make PYTHON=C:/path/to/python.exe bootstrap
make PYTHON=./.venv/Scripts/python.exe check
```

For systems without `make`, see the direct Python commands in `README.md`.

## 9. Validation results

Final fast checks passed with Python 3.12.13:

- Ruff: passed.
- Pytest: 10 passed.
- CSV schema, slot, kit, and migration-manifest validation: passed.
- Deterministic simulation smoke: passed, with sample total 84.
- Generated 11 Markdown tables under ignored `manuscript/generated/tables/`.
- No tracked file exceeds 50 MB; no cache, virtual environment, generated table,
  or raw artifact is tracked; every canonical CSV filename appears once.

The term validator reported only expected unmigrated-manuscript debt:

- `Weapon Scale` once and `Transcendent Exertion` three times in the v2.5 DOCX.
- Required post-migration terms absent from the v2.5 baseline: `weight only`,
  `Reload N`, and `recharge wound`.

These are non-strict expected migration debt, not infrastructure or
current-data failures. `tools/validate_terms.py --strict` correctly fails until
the migration is complete.

## 10. Intentionally untracked local material

There were no valuable untracked imported project files. Ignored local output
is limited to `.venv/`, Python/test/lint caches, editable-install metadata,
generated tables, `artifacts/raw/`, and `artifacts/tmp/`. Large reproducible
raw output must be documented with size, SHA-256, provenance, and regeneration
instructions in `artifacts/MANIFEST.md` rather than committed by default.

## 11. Git LFS status

Git LFS 3.3.0 is installed. No file is tracked by LFS, no LFS migration was
run, and no imported file exceeds 10 MB individually. No prospective LFS
decision is currently required.

## 12. Unresolved blockers and questions

- The migration manifest's nine open rules TODOs remain verbatim in
  `docs/OPEN_QUESTIONS.md`.
- The v5 scaffold was not in the import; do not substitute a different v5 copy
  without preserving it as evidence and applying the source hierarchy.
- No repository license file was imported; obtain rights-holder direction
  before adding one.
- The current manuscript intentionally remains v2.5 until a scoped migration
  begins.

## 13. Recommended next Codex prompt

```text
Work locally in a new branch for one GEWINN v2.5-to-current subsystem only.
First read AGENTS.md, docs/CANONICAL_SOURCES.md,
migration/v2.5-current/GEWINN_v2_5_to_current_CODEX_CHANGELOG.md, and
migration/v2.5-current/GEWINN_v2_5_to_current_CHANGE_MANIFEST.yaml completely.
Use manuscript/source/GEWINN_v2.5.docx as the baseline; do not edit archive/ or
resolve any TODO. Apply only the selected subsystem's manifest instructions,
use data/equipment and data/magic as numerical truth, regenerate tables, update
tests and CHANGELOG.md as needed, run make check, and commit that one subsystem.
```

No remote was fetched, pulled, pushed, rebased, or otherwise changed. Archived
source content remained byte-preserved throughout bootstrap.
