# GEWINN operating rules

Before editing rules, read `docs/CANONICAL_SOURCES.md`. Before migration work,
read both files in `migration/v2.5-current/` completely.

## Source hierarchy

1. `migration/v2.5-current/GEWINN_v2_5_to_current_CHANGE_MANIFEST.yaml`
2. `migration/v2.5-current/GEWINN_v2_5_to_current_CODEX_CHANGELOG.md`
3. Canonical CSV files under `data/`
4. Latest explicit designer decisions already encoded in the migration bundle
5. GEWINN v5.0 as a procedural scaffold only
6. GEWINN v2.5 as the voice, identity, attribution, front matter, and
   discrete-wound source
7. All other drafts and experiments as non-authoritative history

The v5 manuscript is never the final canonical rules source. It is useful for
procedures only where the migration bundle has not superseded it.

## Non-negotiable workflow

- Never edit `archive/`.
- Never edit generated manuscript tables directly; numerical values come from
  `data/`.
- Do not resolve TODOs or design ambiguities without explicit designer
  instruction; log ambiguity in `docs/OPEN_QUESTIONS.md`.
- Preserve v2.5 voice, attribution, front matter, and discrete-wound identity.
- Use v5 only for procedures not superseded by migration decisions.
- Work one subsystem per branch and commit. Run `make check` before every
  commit.
- Update `CHANGELOG.md` for behavioral or numerical changes.
- Simulation changes must record the seed, trial count, assumptions, source
  rules commit, and output paths.
- Do not commit large raw generated outputs unless explicitly approved.
- Never silently restore Scale, Arms Training, Cut/Point/Crush, range-based
  proofing, reactive relic rolls, non-stacking relics, separate
  Growth-eligible Stress, or superseded magic systems.
