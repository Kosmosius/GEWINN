# Contributing to GEWINN

Read `AGENTS.md` and `docs/CANONICAL_SOURCES.md` before work. Use a descriptive local branch name such as `rules/migrate-combat` or `data/equipment-prices` and keep one rules subsystem per branch and commit.

Use concise conventional commit messages: `docs:`, `data:`, `rules:`, `test:`, `sim:`, `playtest:`, `build:`, or `chore:`. Do not mix mechanical migration, table values, prose rewrites, and simulation changes in one commit.

Before every commit, run:

```text
make PYTHON=./.venv/Scripts/python.exe check
```

Never edit generated manuscript tables directly. Rule changes require an appropriate `CHANGELOG.md` entry and regression-test update. Numerical changes also require CSV/schema validation and regenerated tables. Simulation changes require baseline review plus registry metadata for seed, trials, assumptions, rules commit, and output locations.

Do not edit `archive/`, resolve TODOs without an explicit designer decision, or commit large raw generated output unless explicitly approved.
