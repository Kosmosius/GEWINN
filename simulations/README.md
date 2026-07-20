# Simulations

The imported repository contained no simulation source code, configurations,
ZIPs, raw result tables, or audit summaries. The only maintained entry at
bootstrap is a deterministic infrastructure smoke test; it is explicitly not a
balance model and does not change or imply GEWINN mathematics.

Every real simulation must be entered in `registry.yaml` with its status,
source script, assumptions, seed, trial count, source-rules commit, input data,
summary outputs, raw-artifact paths, and exact regeneration command.

## Commands

With the local environment active:

```text
python simulations/src/smoke.py --config simulations/configs/smoke.json
make sim-smoke
make sim-full
```

`make sim-full` deliberately prints a notice until a maintained full simulation
is registered. A future full run must name its fixed seed and trial count,
write small summary outputs to `simulations/results/<simulation-id>/`, and put
large reproducible raw output under ignored `artifacts/raw/<simulation-id>/`
with a hash and provenance in `artifacts/MANIFEST.md`. Full 100,000- and
1,000,000-trial jobs must not run in routine checks or CI.
