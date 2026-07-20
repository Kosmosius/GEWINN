# Import inventory

Captured on 2026-07-20 before repository reorganization, from the clean `main`
checkout at `16bc0a1`.  Every imported project file was Git-tracked and there
were no untracked project files.  SHA-256 values are of the imported bytes.

## Top-level entries

| Entry | Type | Size (bytes) | SHA-256 | Likely role | Duplicate / classification |
| --- | --- | ---: | --- | --- | --- |
| `images/` | directory | 25,182,101 | `673c6be456318706cd09fa43c75dca22d18ceb74e2be18ac8b9ea98e18566b2e` (deterministic tree hash) | historical art/reference assets | Source research / v2.5 layout assets; several `_edit` derivatives, no byte-identical files |
| `arms_armor.csv` | CSV | 580 | `db319e726684c4b77e03caa528112e4bb5f069e76954105522009fd813cda198` | equipment data | canonical data candidate |
| `body_armor.csv` | CSV | 1,310 | `0cad13f43f9e7ef6f852b958449f50f09d914947e23c6ba969e96b86c59654f2` | equipment data | canonical data candidate |
| `common_armor_kits.csv` | CSV | 1,247 | `e22dd7740df2f4eceb7c92399c77da8b92664e0c98e58f4eb985a11aaca66557` | derived kit data | canonical data candidate |
| `GEWINN_top_20_optimal_builds.md` | Markdown | 115,195 | `8b316bf33228953aa56e60f42b392c0112abf8f3300dceb6eaafd5f066eea343` | generated/audit report | archive: imported report |
| `GEWINN_v2.5.docx` | DOCX | 2,525,775 | `3eab84db994de4d246457a4afa55fee5a51eb3f0aa61c2da605b518e7124bc71` | designer-authored editable manuscript | archive baseline and working-source candidate |
| `GEWINN_v2.5.pdf` | PDF | 2,495,478 | `45375b0ce526228fd9d64dbade55c5dea2677b2635a65fb4ab81c9fa95bf9ea9` | rendered source manuscript | archive baseline |
| `GEWINN_v2_5_to_current_CHANGE_MANIFEST.yaml` | YAML | 6,750 | `8f4eb3a888609c5b71ac9e2e086b78d20c725ec72abb62e4358e6571cbad0e6c` | migration specification | migration source |
| `GEWINN_v2_5_to_current_CODEX_CHANGELOG.md` | Markdown | 34,881 | `2b85018af41e45f74acf304f1f53f31578f0708947484da154d7b081cee082be` | migration specification | migration source |
| `GEWINN_v2_5_to_current_consolidated_update.docx` | DOCX | 83,121 | `ec69b8d295de013a08c833b111e4c3631a71086ef63f0ad0ef341879cedc2aea` | prior consolidated update | archive: imported report; non-authoritative |
| `helmets.csv` | CSV | 1,003 | `1f30e1ee803ec86f95edfbe709b42774ee5dc9e69b96094d0427ee1d88818110` | equipment data | canonical data candidate |
| `leg_armor.csv` | CSV | 510 | `6aacf67fa6fd28161492e9f344d0c6d2cf63bc0dea258277840104ae65ed2c54` | equipment data | canonical data candidate |
| `melee_weapons.csv` | CSV | 1,786 | `9a992bdc0e5576743a1aedadc394d1bb94095573c0af928e4fab0ad7459bf615` | equipment data | canonical data candidate |
| `occult_implements.csv` | CSV | 1,203 | `65b8a37943694ebe438ccdb5dc293b11a830a53868e75ee4af2c983b3cc7bbc5` | magic data | canonical data candidate |
| `proofing.csv` | CSV | 139 | `6e26b491270188cbabae8b8aa8ec537a4729662f2c90b3e450c09cf17c743606` | equipment data | canonical data candidate |
| `ranged_weapons.csv` | CSV | 818 | `dea75b89932129cec405a1fd13a785e026ed2ecc5e9a4956eca3c0504fd2a635` | equipment data | canonical data candidate |
| `README.md` | Markdown | 374 | `92a8858d5e46f5eaf607c295acd5c41e49537cfaea2afdf7b524e5307e505452` | migration-bundle README | migration source; renamed on placement |
| `sacred_relics.csv` | CSV | 1,292 | `329db03f33f3e9027bccc8299bb38d6ed1e20c0fc24fa9d1fa6c839a1d03c8bf` | magic data | canonical data candidate |
| `shields.csv` | CSV | 701 | `662f57c4910008fb3cdfc8cf72f3c83f84136c927b53b57a588e5f700caf3e31` | equipment data | canonical data candidate |

The directory hash is calculated from sorted `relative-path<TAB>file-SHA-256`
records. No exact SHA-256 duplicates were found.  `_edit` and contrast/crop
variants are retained as distinct historical art assets rather than deduplicated.

## Size review

No imported file exceeded 10 MB or 50 MB. The `images/` directory is 25.2 MB
in total but consists of individually tracked source/reference assets, not a
reproducible generated artifact.

## Git state before bootstrap

All files below were tracked; no files were untracked.  The import was clean,
so no separate preservation-snapshot commit was required.

```text
GEWINN_top_20_optimal_builds.md
GEWINN_v2.5.docx
GEWINN_v2.5.pdf
GEWINN_v2_5_to_current_CHANGE_MANIFEST.yaml
GEWINN_v2_5_to_current_CODEX_CHANGELOG.md
GEWINN_v2_5_to_current_consolidated_update.docx
README.md
arms_armor.csv
body_armor.csv
common_armor_kits.csv
helmets.csv
images/ (32 image files and images/readme.md)
leg_armor.csv
melee_weapons.csv
occult_implements.csv
proofing.csv
ranged_weapons.csv
sacred_relics.csv
shields.csv
```

The tracked `images/` contents are preserved in full in the baseline archive;
their individual source-file hashes can be reproduced from the original commit
(`16bc0a1`) or from `git ls-tree -r 16bc0a1`.
