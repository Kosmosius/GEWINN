# Project status

| Area | Status | Notes |
| --- | --- | --- |
| Editable manuscript | v2.5 baseline selected | `manuscript/source/GEWINN_v2.5.docx` is byte-preserved from archive. |
| Current migration | Not applied | Bundle is installed at `migration/v2.5-current/`; migrate one subsystem at a time later. |
| Numerical tables | Canonical | CSV data lives under `data/equipment/` and `data/magic/`. |
| Historical evidence | Archived | `archive/` is immutable and non-authoritative. |
| Validation | Operational | `make check` passes with explicitly classified unmigrated-manuscript debt. |
| Simulations | Bootstrap harness only | No imported model or raw result was present. |
| Git LFS | Installed, unused | No LFS paths were configured or migrated. |
| License | Needs rights-holder direction | No `LICENSE.md` was present in the import; none was invented. |

See `docs/OPEN_QUESTIONS.md` for preserved migration TODOs and operational follow-ups. The v5 scaffold was not present in the import and must not be silently substituted for the v2.5 baseline if later supplied.
