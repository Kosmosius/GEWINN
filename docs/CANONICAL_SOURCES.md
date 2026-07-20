# Canonical sources

Use this hierarchy when editing GEWINN. A lower-ranked source cannot override a
higher-ranked source. If the material is ambiguous, record the conflict in
`docs/OPEN_QUESTIONS.md` instead of guessing.

1. `migration/v2.5-current/GEWINN_v2_5_to_current_CHANGE_MANIFEST.yaml`
2. `migration/v2.5-current/GEWINN_v2_5_to_current_CODEX_CHANGELOG.md`
3. Canonical CSV files under `data/`
4. Latest explicit designer decisions already encoded in the migration bundle
5. GEWINN v5.0 as a procedural scaffold only
6. GEWINN v2.5 as the voice, identity, attribution, front matter, and
   discrete-wound source
7. All other drafts and experiments as non-authoritative history

The v5 manuscript is never the final canonical rules source. It supplies useful
procedures only when they have not been superseded by the migration bundle.

## Working locations

- Editable manuscript baseline: `manuscript/source/GEWINN_v2.5.docx`
- Immutable original baseline: `archive/v2.5-baseline/GEWINN_v2.5.docx`
- Numerical source of truth: `data/equipment/` and `data/magic/`
- Generated manuscript tables: `manuscript/generated/tables/`
- Historical evidence: `archive/` (never edit)

The current working source is deliberately still the v2.5 baseline. The
migration bundle has been placed and validated as an instruction source, not
applied to rules text.
