# Simulation reproducibility rules

Do not change imported simulation mathematics during bootstrap. Every maintained
or changed simulation must record its seed, trial count, assumptions, source
rules commit, input data, output paths, and regeneration command in
`simulations/registry.yaml`.

Use repository-relative paths. Put small summaries in `simulations/results/`;
put large reproducible raw output under ignored `artifacts/raw/` and record its
hash and provenance in `artifacts/MANIFEST.md`. Keep full 100,000+ trial runs
out of normal checks and provide deterministic smoke configurations.
