# GEWINN numerical data

The CSV files in `data/equipment/` and `data/magic/` are GEWINN's numerical
source of truth. Manuscript tables are generated from those files, never
maintained as a second hand-edited numerical source.

Derived kit totals are calculated from components and must never be edited by
hand. A CSV change requires validation, regenerated manuscript tables, updated
simulation baselines when relevant, and a `CHANGELOG.md` entry.

Schemas in `data/schemas/` describe accepted inputs; `data/derived/` is for
reproducible derived material rather than another canonical copy of a table.
