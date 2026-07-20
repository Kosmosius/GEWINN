# ADR 0002: CSV data is the numerical source of truth

## Status

Accepted during repository bootstrap.

## Decision

Canonical equipment and magic numerical values live only in the CSV files under `data/equipment/` and `data/magic/`. Markdown tables are generated from them. Derived armor-kit totals are validator outputs, not hand-maintained values.

## Consequences

Numerical changes require schema, slot, and kit validation; generated tables; relevant simulation-baseline review; and a changelog entry.
