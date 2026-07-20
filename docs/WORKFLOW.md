# Safe GEWINN workflow

## Before migration work

1. Read `AGENTS.md`, `docs/CANONICAL_SOURCES.md`, the migration changelog, and the YAML manifest completely.
2. Confirm the working source and source hash in `manuscript/source/MANUSCRIPT_STATUS.md`.
3. Create one branch for one migration subsystem. Do not combine the v2.5 baseline, v5 scaffold, experiments, or migration notes into a new manuscript.
4. Record uncertainty in `docs/OPEN_QUESTIONS.md`; do not invent procedures, values, wound tables, spells, or prices.

## For a scoped change

1. Apply only the relevant manifest/changelog instructions to `manuscript/source/` and/or canonical data.
2. Generate Markdown tables with `make generate`; never hand-edit the output.
3. Update tests, schemas, simulations, and `CHANGELOG.md` when the change affects them.
4. Run `make check`. During the unmigrated bootstrap stage, the term scanner reports known v2.5 debt but exits successfully; use `validate_terms.py --strict` only after migration completion.
5. Commit the single subsystem with a concise conventional message.

## Artifact policy

Track sources, small summaries, configuration, and regeneration instructions. Keep large reproducible raw output in ignored `artifacts/raw/`, then record size, SHA-256, provenance, and the exact command in `artifacts/MANIFEST.md`. Do not put routine full simulations in CI.
