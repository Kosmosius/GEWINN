# GEWINN: Twenty Optimal Classless Builds

## Executive verdict

The current system produces a real Pareto frontier rather than one universal character. The strongest stable characters concentrate on **one primary combat axis and one supporting axis**. Pure physical specialists remain strong because armor, Control, reload protection, and expedition resilience matter after limited magic is spent. INT and FTH hybrids gain breadth, but their weight, source, hand, and stat commitments prevent the full mixed adventurer from becoming the default. The rarest selected clean build is the 4d4 implement artillery user; the most accessible strong procedures are the shielded one-die martial, arbalester, and ordinary spear specialist.

The most dangerous legal edge is not a class combination: it is access to **Unique one-die d10/d12 implements**, which combine a low dice-count gate with Reload 1. Their current 20–24 lb load and Unique status must be enforced. The strongest ordinary anti-magic package is one 1d4 relic of each type, but four slots plus physical armor and expedition gear create real movement and treasure costs.

## Optimization method

The code enumerated 7,191 structured legal candidates, retained 112 formal Pareto-efficient representatives, and selected twenty mechanically distinct campaign builds. It calculated exact attack/wound probabilities against ten defense profiles, evaluated six published scoring profiles, pruned within equivalent clusters, retained Pareto-efficient representatives, and then ran 100,000-trial fixed-seed duels and party tests. The exact general-campaign formula uses the percentages in the prompt without alteration.

## Published scoring formulas

All component metrics are normalized to 0–1 before weighting.

- **General campaign:** `0.15 Survival + 0.13 Serious+ + 0.08 Grave+ + 0.08 Initiative + 0.08 Matchup Breadth + 0.07 Sustained Output + 0.07 Expedition Utility + 0.06 Retreat + 0.05 mean(Control, Morale) + 0.05 Movement + 0.04 Range + 0.04 Slot Efficiency + 0.04 Hand Efficiency + 0.03 Resource-Loss Resilience + 0.03 Legal/Availability Robustness`.
- **Duel lethality:** `0.30 Serious+ + 0.20 Grave+ + 0.15 Initiative + 0.15 Survival + 0.10 Sustained Output + 0.05 Matchup Breadth + 0.05 Range`.
- **Party combat:** `0.15 Serious+ + 0.10 Grave+ + 0.10 Survival + 0.15 Control + 0.10 Range + 0.10 Sustained Output + 0.10 Matchup Breadth + 0.10 mean(Healing, Morale) + 0.05 Hand Efficiency + 0.05 Slot Efficiency`.
- **Expedition:** `0.20 Expedition Utility + 0.15 Survival + 0.10 Movement + 0.10 Retreat + 0.10 Slot Efficiency + 0.10 Resource-Loss Resilience + 0.10 Utility + 0.10 Legal Robustness + 0.05 Sustained Output`.
- **Survivability:** `0.40 Survival + 0.15 Retreat + 0.10 Movement + 0.15 Physical Defense + 0.10 Exotic Defense + 0.10 Resource-Loss Resilience`.
- **Low-resource:** `0.25 Cost Efficiency + 0.15 Legal Robustness + 0.15 Natural Qualification + 0.15 Slot Efficiency + 0.10 Survival + 0.10 Serious+ + 0.05 Sustained Output + 0.05 Resource-Loss Resilience`.

The final ordering uses a campaign-viability selector rather than pretending the general score alone resolves every niche: `General + 0.25 Party + 0.15 Expedition + 0.10 Low-Resource + 0.025 Stability Count − 0.15 Impossible-Natural penalty − 0.07 Extreme-Rarity penalty − 0.08 Unique-item penalty − 0.018 slots above 20`. Stability Count is the number of the six profiles in whose top sensitivity band the candidate appears. This selector chooses among distinct frontier procedures; it does not rebalance item costs.


## Source conflicts and assumptions

- The consolidated update lists seven damage types; the explicit optimization prompt adds **Freezing** as the eighth. Freezing therefore uses the same implement/relic inventory grammar as Burning, Shocking, and Toxic.
- The older integrated simulation modeled separate melee/ranged implements and lower magical-item weights. The current rule is one dual-mode implement, weight **2 × N × S lb**, ranged Reload N, no melee reload.
- The v5 draft's spell/prayer templates are retained as representative named Workings, but its older casting and Growth-eligible-Stress language is superseded by remembered memory, one resolution roll, recharge wounds, and one universal Stress track.
- The current document contains both a movement formula and load-band prose. The optimizer applies the explicit movement formula once and treats load-band pressure qualitatively; it does not double-penalize movement.
- Complete individual weights for rope, light, bandages, water, rations, ammunition, and surgical tools are absent from the consolidated combat tables. Standardized field bundles are declared in the assumptions file and applied equally.

## Top-20 ranking

|   Rank | Build                           | Primary Axis   | Secondary Axis   | Main Role                | Stat Rarity   |   Slots |   Campaign Score | Best Niche                                                        | Main Counter                                                                              |
|-------:|:--------------------------------|:---------------|:-----------------|:-------------------------|:--------------|--------:|-----------------:|:------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
|      1 | Rifle Specialist                | WLL            | STR              | Firearm                  | 100.000%      |      11 |            0.879 | plate not fully proofed                                           | proofed harness and reload pressure; ambushes and close pressure                          |
|      2 | Spell-and-Implement Magician    | INT            | INT              | Spell-implement hybrid   | 4.630%        |      11 |            0.834 | physical armor without the matching relic                         | stacked matching relic DR; ambushes and close pressure; source loss and expended memory   |
|      3 | Four-Type Relic Defender        | WLL            | STR              | Universal relic defender | 100.000%      |      16 |            0.793 | plate not fully proofed; occult volleys                           | proofed harness and reload pressure; physical armor-breakers; ambushes and close pressure |
|      4 | Direct-Damage Magician          | INT            | INT              | Spell specialist         | 4.630%        |       4 |            0.737 | physically armored targets without the matching exotic defense    | matching relic DR; expended memory; source loss                                           |
|      5 | Implement-and-Relic Hybrid      | INT            | STR              | Implement-relic hybrid   | 4.630%        |      18 |            0.702 | physical armor without the matching relic; occult volleys         | stacked matching relic DR; physical armor-breakers; ambushes and close pressure           |
|      6 | Gun-and-Implement Hybrid        | INT            | WLL              | Gun-implement hybrid     | 100.000%      |      15 |            0.689 | physical armor without the matching relic                         | stacked matching relic DR                                                                 |
|      7 | Low-N Implement Duelist         | INT            | STR              | Implement duelist        | 100.000%      |      11 |            0.643 | physical armor without the matching relic                         | stacked matching relic DR                                                                 |
|      8 | Warhammer Armor Breaker         | STR            | —                | Armor breaker            | 100.000%      |       7 |            0.629 | mail and armor reliant on cut resistance                          | coordinated Control, surprise, and asymmetric range                                       |
|      9 | Composite-Bow Specialist        | WLL            | STR              | Archer                   | 4.630%        |       9 |            0.624 | light and medium armor                                            | coordinated Control, surprise, and asymmetric range                                       |
|     10 | High-Stat Implement Artillery   | INT            | STR              | Implement artillery      | 0.463%        |      17 |            0.618 | physical armor without the matching relic                         | stacked matching relic DR; ambushes and close pressure                                    |
|     11 | Spear Brace Specialist          | STR            | —                | Brace                    | 100.000%      |       9 |            0.617 | light and medium armor                                            | coordinated Control, surprise, and asymmetric range                                       |
|     12 | Arbalest Position Fighter       | WLL            | STR              | Crossbow                 | 100.000%      |      11 |            0.616 | light and medium armor                                            | ambushes and close pressure                                                               |
|     13 | Low-Resource Extraction Fighter | STR            | —                | Extraction               | 100.000%      |      16 |            0.579 | light and medium armor                                            | coordinated Control, surprise, and asymmetric range                                       |
|     14 | Retainer Expedition Commander   | STR            | FTH              | Commander                | 4.630%        |      16 |            0.575 | light and medium armor                                            | source loss and expended memory                                                           |
|     15 | Mace-and-Shield Defender        | STR            | —                | Shield                   | 100.000%      |      12 |            0.552 | mail and armor reliant on cut resistance                          | coordinated Control, surprise, and asymmetric range                                       |
|     16 | Relic Morale Minister           | FTH            | FTH              | Miracle-relic worker     | 4.630%        |      20 |            0.552 | light and medium armor; occult volleys                            | physical armor-breakers; source loss and expended memory                                  |
|     17 | Control Magician                | INT            | INT              | Spell specialist         | 4.630%        |       4 |            0.548 | high-AC groups vulnerable to Control and terrain                  | named-target Defense; expended memory; source loss                                        |
|     18 | Relic Field Minister            | FTH            | FTH              | Miracle-relic worker     | 4.630%        |      20 |            0.544 | light and medium armor; occult volleys                            | physical armor-breakers; source loss and expended memory                                  |
|     19 | Sword-and-Shield Defender       | STR            | —                | Shield                   | 100.000%      |      12 |            0.544 | light and medium armor                                            | coordinated Control, surprise, and asymmetric range                                       |
|     20 | Full-Harness Poleaxe Fighter    | STR            | STR              | Armor breaker            | 16.204%       |      25 |            0.507 | mail and armor reliant on cut resistance; ordinary physical mooks | Control and Gap Strike                                                                    |

## 1. Rifle Specialist

### Mechanical identity

Firearm. Its main procedure is **Rifle**; **Rifle** is the primary weapon, Unarmored is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **musketeer / sharpshooter**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 12 (+1) | Fallback offense |
| INT | 3 (+0) | 3 (+0) | Secondary |
| FTH | 3 (+0) | 3 (+0) | Secondary |
| WLL | 3 (+0) | 14 (+2) | Primary |

- Natural 3d6 qualification: **100.000%**.
- Primary advancement: **WLL**.
- Secondary advancement: **STR**.
- Functions at +0/+1: **yes**.

### Core loadout

- Primary: **Rifle**, 3d12 Shot, 2 hand(s), 10 lb/3 slots, £7, Elite.
- Secondary: **Dagger**.
- Armor: **Clothing**; 0 lb/0 slots, —.
- Relics: **none**.
- Remembered spells: **none**.
- Remembered miracles: **none**.
- Source: **none required**.
- Expedition equipment: **lantern and oil; 50' rope; bandages; water and rations; flint, chalk, sacks**.
- Ammunition: **20 prepared shots in the standardized 2-slot ammunition bundle**.

### Derived statistics

- AC: **2 melee / 2 missile** while the primary is in hand.
- DR: **Slashing 0, Piercing 0, Bludgeoning 0, Shot 0, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **35.0 lb**.
- Total slots: **11**; movement **35'**.
- Hands: primary 2; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+2 WLL; Impact 3d12; handling clean**.
- Range/reload: **range band 2, Reload 4**.
- Spell memory: **0 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 99.9%, Armored mook 98.4%, Arbalester 83.7%, Musketeer 83.4%, Occult striker 94.1%, Harness knight 69.8% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open at range with Rifle; declare damage type/mode before Impact. Reload behind allies or cover; the full reload clock is 4 actions. Use the sidearm if the line collapses. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

plate not fully proofed.

### Hard counters

proofed harness and reload pressure; ambushes and close pressure.

### Resource failure

Without ammunition or dry powder, fall back to the sidearm and the armor/relic package. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise WLL; raise STR; raise INT.

### Campaign requirements

Wealth: professional; access: Elite, Common; legality follows visible arms, firearms, occult restrictions, and faction ownership. Campaign-developed at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: open field, treasure extraction. Weakest: tight dungeon.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Exceptional |
| Sustained power | Low |
| Initiative | Low |
| Survival | Low |
| Mobility | 35' |
| Expedition value | Moderate |
| Party value | Moderate |
| Complexity | Low |
| Robustness | Low |

### Verdict

**powerful but fragile.**

## 2. Spell-and-Implement Magician

### Mechanical identity

Spell-implement hybrid. Its main procedure is **Burning implement 2d4**; **Burning implement 2d4** is the primary weapon, Unarmored is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **gish, but one-stat and gear-bound**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 12 (+1) | Fallback offense |
| INT | 16 (+3) | 16 (+3) | Primary |
| FTH | 3 (+0) | 3 (+0) | Secondary |
| WLL | 3 (+0) | 12 (+1) | Important defense/utility |

- Natural 3d6 qualification: **4.630%**.
- Primary advancement: **INT**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **only in a reduced or over-wielded form**.

### Core loadout

- Primary: **Burning implement 2d4**, 2d4 Burning, 2 hand(s), 16 lb/5 slots, £8, Restricted.
- Secondary: **Dagger**.
- Armor: **Clothing**; 0 lb/0 slots, —.
- Relics: **none**.
- Remembered spells: **Hex of Stumbling L1; Fog / Smoke L1; Sleep Charm L1**.
- Remembered miracles: **none**.
- Source: **Arcane grimoire**.
- Expedition equipment: **lantern and oil; 50' rope; bandages; water and rations; flint, chalk, sacks**.
- Ammunition: **none**.

### Derived statistics

- AC: **1 melee / 1 missile** while the primary is in hand.
- DR: **Slashing 0, Piercing 0, Bludgeoning 0, Shot 0, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **35.0 lb**.
- Total slots: **11**; movement **35'**.
- Hands: primary 2; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+3 INT; Impact 2d4; handling clean**.
- Range/reload: **melee and range band 2, ranged Reload 2**.
- Spell memory: **3 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 85.8%, Armored mook 70.7%, Arbalester 37.7%, Musketeer 34.5%, Occult striker 65.1%, Harness knight 17.0% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open at range with Burning implement 2d4; declare damage type/mode before Impact. Against high AC or a named threat, spend control before trading damage; exploit Compromised/Controlled with allies or a dagger Gap Strike. After a ranged discharge, mark Reload 2; use the same implement in melee rather than standing idle if the enemy closes. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

physical armor without the matching relic.

### Hard counters

stacked matching relic DR; ambushes and close pressure; source loss and expended memory.

### Resource failure

If the implement is lost or confiscated, only the secondary weapon, remembered magic, armor, and relics remain. Spent memory leaves equipment and ordinary actions; source loss prevents safe restoration or rearrangement, not already remembered use. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise INT; raise WLL; raise STR.

### Campaign requirements

Wealth: professional; access: Restricted, Common, Restricted source; legality follows visible arms, firearms, occult restrictions, and faction ownership. Campaign-developed at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: treasure extraction, open field. Weakest: tight dungeon.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Moderate |
| Sustained power | Low |
| Initiative | Exceptional |
| Survival | Low |
| Mobility | 35' |
| Expedition value | High |
| Party value | Moderate |
| Complexity | High |
| Robustness | High |

### Verdict

**niche optimal.**

## 3. Four-Type Relic Defender

### Mechanical identity

Universal relic defender. Its main procedure is **Musket**; **Musket** is the primary weapon, Unarmored is the defensive commitment, and one 1d4 relic of each type is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **paladin or magic-resistant tank, but entirely equipment-based**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 12 (+1) | Fallback offense |
| INT | 3 (+0) | 3 (+0) | Secondary |
| FTH | 3 (+0) | 12 (+1) | Secondary |
| WLL | 3 (+0) | 14 (+2) | Primary |

- Natural 3d6 qualification: **100.000%**.
- Primary advancement: **WLL**.
- Secondary advancement: **STR**.
- Functions at +0/+1: **yes**.

### Core loadout

- Primary: **Musket**, 2d12 Shot, 2 hand(s), 12 lb/4 slots, £4, Military.
- Secondary: **Dagger**.
- Armor: **Clothing**; 0 lb/0 slots, —.
- Relics: **1× 1d4 Burning; 1× 1d4 Shocking; 1× 1d4 Toxic; 1× 1d4 Freezing**.
- Remembered spells: **none**.
- Remembered miracles: **none**.
- Source: **none required**.
- Expedition equipment: **lantern and oil; 50' rope; bandages; water and rations; flint, chalk, sacks**.
- Ammunition: **20 prepared shots in the standardized 2-slot ammunition bundle**.

### Derived statistics

- AC: **2 melee / 2 missile** while the primary is in hand.
- DR: **Slashing 0, Piercing 0, Bludgeoning 0, Shot 0, Burning 4, Shocking 4, Toxic 4, Freezing 4**.
- Total carried weight: **53.0 lb**.
- Total slots: **16**; movement **30'**.
- Hands: primary 2; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+2 WLL; Impact 2d12; handling clean**.
- Range/reload: **range band 2, Reload 3**.
- Spell memory: **0 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 99.6%, Armored mook 96.6%, Arbalester 83.6%, Musketeer 83.5%, Occult striker 100.0%, Harness knight 49.2% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open at range with Musket; declare damage type/mode before Impact. Reload behind allies or cover; the full reload clock is 3 actions. Use the sidearm if the line collapses. Relic DR is passive and stacked; change positioning or damage type rather than spending actions to activate it. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

plate not fully proofed; occult volleys.

### Hard counters

proofed harness and reload pressure; physical armor-breakers; ambushes and close pressure.

### Resource failure

Without ammunition or dry powder, fall back to the sidearm and the armor/relic package. If relics are lost, physical AC/DR remains but exotic protection collapses. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise WLL; raise STR; raise INT.

### Campaign requirements

Wealth: professional; access: Military, Common, Restricted; legality follows visible arms, firearms, occult restrictions, and faction ownership. Campaign-developed at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: magic-rich opposition, open field. Weakest: tight dungeon.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | High |
| Sustained power | Low |
| Initiative | Low |
| Survival | Moderate |
| Mobility | 30' |
| Expedition value | Low |
| Party value | Moderate |
| Complexity | High |
| Robustness | Low |

### Verdict

**powerful but fragile.**

## 4. Direct-Damage Magician

### Mechanical identity

Spell specialist. Its main procedure is **Arcane firebrand reserve**; **Dagger** is the exhausted fallback, Unarmored is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **magic-user / artillery caster**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 3 (+0) | Fallback offense |
| INT | 16 (+3) | 16 (+3) | Primary |
| FTH | 3 (+0) | 3 (+0) | Secondary |
| WLL | 3 (+0) | 12 (+1) | Important defense/utility |

- Natural 3d6 qualification: **4.630%**.
- Primary advancement: **INT**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **only in a reduced or over-wielded form**.

### Core loadout

- Primary: **Dagger**, 1d4 Slashing/Piercing, 1 hand(s), 1 lb/0 slots, 1s, Common.
- Secondary: **none**.
- Armor: **Clothing**; 0 lb/0 slots, —.
- Relics: **none**.
- Remembered spells: **Firebrand L1; Firebrand L1; Firebrand L1**.
- Remembered miracles: **none**.
- Source: **Arcane grimoire**.
- Expedition equipment: **torch or candle; bandages; water and rations; chalk, flint, sacks**.
- Ammunition: **none**.

### Derived statistics

- AC: **1 melee / 1 missile** while the primary is in hand.
- DR: **Slashing 0, Piercing 0, Bludgeoning 0, Shot 0, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **13.0 lb**.
- Total slots: **4**; movement **40'**.
- Hands: primary 1; shield defense is inactive with an incompatible two-handed primary.
- Attack: **Working attack +3 INT; direct Impact 1d8; dagger fallback +0 STR, 1d4**.
- Range/reload: **Working range/effect as listed; dagger melee fallback**.
- Spell memory: **3 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 59.3%, Armored mook 52.4%, Arbalester 41.5%, Musketeer 39.7%, Occult striker 53.6%, Harness knight 25.4% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open with Arcane firebrand reserve; direct Workings are finite, so reserve later uses for armor or clustered danger. Once memory is spent, use light, tools, positioning, and the dagger only as a last resort. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

physically armored targets without the matching exotic defense.

### Hard counters

matching relic DR; expended memory; source loss.

### Resource failure

Spent memory leaves equipment and ordinary actions; source loss prevents safe restoration or rearrangement, not already remembered use. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise INT; raise WLL; raise STR.

### Campaign requirements

Wealth: low; access: Common, Restricted source; legality follows visible arms, firearms, occult restrictions, and faction ownership. Plausible at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: treasure extraction, open field. Weakest: tight dungeon.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Moderate |
| Sustained power | Moderate |
| Initiative | Exceptional |
| Survival | Low |
| Mobility | 40' |
| Expedition value | High |
| Party value | Moderate |
| Complexity | Low |
| Robustness | Moderate |

### Verdict

**niche optimal.**

## 5. Implement-and-Relic Hybrid

### Mechanical identity

Implement-relic hybrid. Its main procedure is **Burning implement 3d4**; **Burning implement 3d4** is the primary weapon, Unarmored is the defensive commitment, and burning and freezing relics 1d6 is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **occult-sacred hybrid**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 12 (+1) | Fallback offense |
| INT | 16 (+3) | 16 (+3) | Primary |
| FTH | 3 (+0) | 12 (+1) | Secondary |
| WLL | 3 (+0) | 12 (+1) | Important defense/utility |

- Natural 3d6 qualification: **4.630%**.
- Primary advancement: **INT**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **only in a reduced or over-wielded form**.

### Core loadout

- Primary: **Burning implement 3d4**, 3d4 Burning, 2 hand(s), 24 lb/8 slots, £12, Elite/Restricted.
- Secondary: **Dagger**.
- Armor: **Clothing**; 0 lb/0 slots, —.
- Relics: **1× 1d6 Burning; 1× 1d6 Freezing**.
- Remembered spells: **none**.
- Remembered miracles: **none**.
- Source: **none required**.
- Expedition equipment: **lantern and oil; 50' rope; bandages; water and rations; flint, chalk, sacks**.
- Ammunition: **none**.

### Derived statistics

- AC: **1 melee / 1 missile** while the primary is in hand.
- DR: **Slashing 0, Piercing 0, Bludgeoning 0, Shot 0, Burning 6, Shocking 0, Toxic 0, Freezing 6**.
- Total carried weight: **55.0 lb**.
- Total slots: **18**; movement **30'**.
- Hands: primary 2; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+3 INT; Impact 3d4; handling clean**.
- Range/reload: **melee and range band 2, ranged Reload 3**.
- Spell memory: **0 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 98.1%, Armored mook 93.9%, Arbalester 74.5%, Musketeer 74.8%, Occult striker 100.0%, Harness knight 56.5% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open at range with Burning implement 3d4; declare damage type/mode before Impact. After a ranged discharge, mark Reload 3; use the same implement in melee rather than standing idle if the enemy closes. Relic DR is passive and stacked; change positioning or damage type rather than spending actions to activate it. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

physical armor without the matching relic; occult volleys.

### Hard counters

stacked matching relic DR; physical armor-breakers; ambushes and close pressure.

### Resource failure

If the implement is lost or confiscated, only the secondary weapon, remembered magic, armor, and relics remain. If relics are lost, physical AC/DR remains but exotic protection collapses. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise INT; raise WLL; raise STR.

### Campaign requirements

Wealth: privileged/elite; access: Elite/Restricted, Common, Restricted; legality follows visible arms, firearms, occult restrictions, and faction ownership. Campaign-developed at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: magic-rich opposition, open field. Weakest: tight dungeon.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | High |
| Sustained power | Low |
| Initiative | Moderate |
| Survival | Moderate |
| Mobility | 30' |
| Expedition value | Low |
| Party value | Moderate |
| Complexity | High |
| Robustness | High |

### Verdict

**niche optimal.**

## 6. Gun-and-Implement Hybrid

### Mechanical identity

Gun-implement hybrid. Its main procedure is **Burning implement 1d4**; **Burning implement 1d4** is the primary weapon, Unarmored is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **gun-mage**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 3 (+0) | Secondary |
| INT | 3 (+0) | 14 (+2) | Primary |
| FTH | 3 (+0) | 3 (+0) | Secondary |
| WLL | 3 (+0) | 14 (+2) | Important defense/utility |

- Natural 3d6 qualification: **100.000%**.
- Primary advancement: **INT**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **yes**.

### Core loadout

- Primary: **Burning implement 1d4**, 1d4 Burning, 2 hand(s), 8 lb/3 slots, £4, Restricted.
- Secondary: **Musket**.
- Armor: **Clothing**; 0 lb/0 slots, —.
- Relics: **none**.
- Remembered spells: **none**.
- Remembered miracles: **none**.
- Source: **none required**.
- Expedition equipment: **lantern and oil; 50' rope; bandages; water and rations; flint, chalk, sacks**.
- Ammunition: **none**.

### Derived statistics

- AC: **2 melee / 2 missile** while the primary is in hand.
- DR: **Slashing 0, Piercing 0, Bludgeoning 0, Shot 0, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **44.0 lb**.
- Total slots: **15**; movement **25'**.
- Hands: primary 2; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+2 INT; Impact 1d4; handling clean**.
- Range/reload: **melee and range band 2, ranged Reload 1**.
- Spell memory: **0 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 99.6%, Armored mook 96.6%, Arbalester 83.6%, Musketeer 83.3%, Occult striker 93.7%, Harness knight 49.1% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open at range with Burning implement 1d4; declare damage type/mode before Impact. After a ranged discharge, mark Reload 1; use the same implement in melee rather than standing idle if the enemy closes. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

physical armor without the matching relic.

### Hard counters

stacked matching relic DR.

### Resource failure

Without ammunition or dry powder, fall back to the sidearm and the armor/relic package. If the implement is lost or confiscated, only the secondary weapon, remembered magic, armor, and relics remain. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise INT; raise WLL; raise STR.

### Campaign requirements

Wealth: professional; access: Restricted, Common; legality follows visible arms, firearms, occult restrictions, and faction ownership. Campaign-developed at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: open field, lone play. Weakest: tight dungeon.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | High |
| Sustained power | Low |
| Initiative | Low |
| Survival | Low |
| Mobility | 25' |
| Expedition value | Moderate |
| Party value | Moderate |
| Complexity | Low |
| Robustness | High |

### Verdict

**niche optimal.**

## 7. Low-N Implement Duelist

### Mechanical identity

Implement duelist. Its main procedure is **Burning implement 1d8**; **Burning implement 1d8** is the primary weapon, Unarmored is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **magic-user / warlock, but weaponized and repeatable**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 12 (+1) | Fallback offense |
| INT | 3 (+0) | 14 (+2) | Primary |
| FTH | 3 (+0) | 3 (+0) | Secondary |
| WLL | 3 (+0) | 12 (+1) | Important defense/utility |

- Natural 3d6 qualification: **100.000%**.
- Primary advancement: **INT**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **yes**.

### Core loadout

- Primary: **Burning implement 1d8**, 1d8 Burning, 2 hand(s), 16 lb/5 slots, £16, Elite/Restricted.
- Secondary: **Dagger**.
- Armor: **Clothing**; 0 lb/0 slots, —.
- Relics: **none**.
- Remembered spells: **none**.
- Remembered miracles: **none**.
- Source: **none required**.
- Expedition equipment: **lantern and oil; 50' rope; bandages; water and rations; flint, chalk, sacks**.
- Ammunition: **none**.

### Derived statistics

- AC: **1 melee / 1 missile** while the primary is in hand.
- DR: **Slashing 0, Piercing 0, Bludgeoning 0, Shot 0, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **35.0 lb**.
- Total slots: **11**; movement **35'**.
- Hands: primary 2; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+2 INT; Impact 1d8; handling clean**.
- Range/reload: **melee and range band 2, ranged Reload 1**.
- Spell memory: **0 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 87.6%, Armored mook 71.9%, Arbalester 42.0%, Musketeer 39.3%, Occult striker 66.6%, Harness knight 27.3% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open at range with Burning implement 1d8; declare damage type/mode before Impact. After a ranged discharge, mark Reload 1; use the same implement in melee rather than standing idle if the enemy closes. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

physical armor without the matching relic.

### Hard counters

stacked matching relic DR.

### Resource failure

If the implement is lost or confiscated, only the secondary weapon, remembered magic, armor, and relics remain. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise INT; raise WLL; raise STR.

### Campaign requirements

Wealth: privileged/elite; access: Elite/Restricted, Common; legality follows visible arms, firearms, occult restrictions, and faction ownership. Campaign-developed at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: treasure extraction, open field. Weakest: tight dungeon.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Low |
| Sustained power | Low |
| Initiative | Exceptional |
| Survival | Low |
| Mobility | 35' |
| Expedition value | Moderate |
| Party value | Low |
| Complexity | Low |
| Robustness | High |

### Verdict

**niche optimal.**

## 8. Warhammer Armor Breaker

### Mechanical identity

Armor breaker. Its main procedure is **Warhammer**; **Warhammer** is the primary weapon, Unarmored is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **man-at-arms / anti-armor specialist**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 14 (+2) | Primary |
| INT | 3 (+0) | 3 (+0) | Secondary |
| FTH | 3 (+0) | 3 (+0) | Secondary |
| WLL | 3 (+0) | 12 (+1) | Important defense/utility |

- Natural 3d6 qualification: **100.000%**.
- Primary advancement: **STR**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **yes**.

### Core loadout

- Primary: **Warhammer**, 1d10 Bludgeoning/Piercing, 1 hand(s), 3.5 lb/1 slots, 18s, Military.
- Secondary: **none**.
- Armor: **Clothing**; 0 lb/0 slots, —.
- Relics: **none**.
- Remembered spells: **none**.
- Remembered miracles: **none**.
- Source: **none required**.
- Expedition equipment: **lantern and oil; 50' rope; bandages; water and rations; flint, chalk, sacks**.
- Ammunition: **none**.

### Derived statistics

- AC: **1 melee / 1 missile** while the primary is in hand.
- DR: **Slashing 0, Piercing 0, Bludgeoning 0, Shot 0, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **21.5 lb**.
- Total slots: **7**; movement **45'**.
- Hands: primary 1; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+2 STR; Impact 1d10; handling clean**.
- Range/reload: **range band 0, Reload 0**.
- Spell memory: **0 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 88.6%, Armored mook 46.2%, Arbalester 26.2%, Musketeer 12.4%, Occult striker 67.0%, Harness knight 0.0% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open with Warhammer, using its retained Impact as initiative and damage. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

mail and armor reliant on cut resistance.

### Hard counters

coordinated Control, surprise, and asymmetric range.

### Resource failure

The build remains an ordinary armed and armored adventurer after consumables are lost. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise STR; raise WLL; raise INT.

### Campaign requirements

Wealth: low; access: Military, Common; legality follows visible arms, firearms, occult restrictions, and faction ownership. Plausible at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: treasure extraction, long expedition. Weakest: open field.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Low |
| Sustained power | Low |
| Initiative | Exceptional |
| Survival | Low |
| Mobility | 45' |
| Expedition value | High |
| Party value | Low |
| Complexity | Low |
| Robustness | Moderate |

### Verdict

**low-resource optimal.**

## 9. Composite-Bow Specialist

### Mechanical identity

Archer. Its main procedure is **Composite bow**; **Composite bow** is the primary weapon, Unarmored is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **ranger or longbowman**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 16 (+3) | 16 (+3) | Primary |
| INT | 3 (+0) | 3 (+0) | Secondary |
| FTH | 3 (+0) | 3 (+0) | Secondary |
| WLL | 3 (+0) | 14 (+2) | Primary |

- Natural 3d6 qualification: **4.630%**.
- Primary advancement: **WLL**.
- Secondary advancement: **STR**.
- Functions at +0/+1: **only in a reduced or over-wielded form**.

### Core loadout

- Primary: **Composite bow**, 3d4 Piercing, 2 hand(s), 2 lb/1 slots, 12s, Elite.
- Secondary: **Dagger**.
- Armor: **Clothing**; 0 lb/0 slots, —.
- Relics: **none**.
- Remembered spells: **none**.
- Remembered miracles: **none**.
- Source: **none required**.
- Expedition equipment: **lantern and oil; 50' rope; bandages; water and rations; flint, chalk, sacks**.
- Ammunition: **30 arrows/bolts in the standardized 2-slot bundle**.

### Derived statistics

- AC: **2 melee / 2 missile** while the primary is in hand.
- DR: **Slashing 0, Piercing 0, Bludgeoning 0, Shot 0, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **27.0 lb**.
- Total slots: **9**; movement **50'**.
- Hands: primary 2; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+2 WLL; Impact 3d4; handling clean**.
- Range/reload: **range band 2, Reload 0**.
- Spell memory: **0 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 98.0%, Armored mook 76.8%, Arbalester 72.2%, Musketeer 54.9%, Occult striker 93.7%, Harness knight 0.0% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open at range with Composite bow; declare damage type/mode before Impact. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

light and medium armor.

### Hard counters

coordinated Control, surprise, and asymmetric range.

### Resource failure

The build remains an ordinary armed and armored adventurer after consumables are lost. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise WLL; raise STR; raise INT.

### Campaign requirements

Wealth: low; access: Elite, Common; legality follows visible arms, firearms, occult restrictions, and faction ownership. Plausible at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: treasure extraction, open field. Weakest: tight dungeon.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Low |
| Sustained power | Low |
| Initiative | Moderate |
| Survival | Low |
| Mobility | 50' |
| Expedition value | High |
| Party value | Low |
| Complexity | Low |
| Robustness | Moderate |

### Verdict

**niche optimal.**

## 10. High-Stat Implement Artillery

### Mechanical identity

Implement artillery. Its main procedure is **Burning implement 4d4**; **Burning implement 4d4** is the primary weapon, Unarmored is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **artillery mage / glass cannon**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 12 (+1) | Fallback offense |
| INT | 18 (+4) | 18 (+4) | Primary |
| FTH | 3 (+0) | 3 (+0) | Secondary |
| WLL | 3 (+0) | 12 (+1) | Important defense/utility |

- Natural 3d6 qualification: **0.463%**.
- Primary advancement: **INT**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **only in a reduced or over-wielded form**.

### Core loadout

- Primary: **Burning implement 4d4**, 4d4 Burning, 2 hand(s), 32 lb/11 slots, £16, Unique.
- Secondary: **Dagger**.
- Armor: **Clothing**; 0 lb/0 slots, —.
- Relics: **none**.
- Remembered spells: **none**.
- Remembered miracles: **none**.
- Source: **none required**.
- Expedition equipment: **lantern and oil; 50' rope; bandages; water and rations; flint, chalk, sacks**.
- Ammunition: **none**.

### Derived statistics

- AC: **1 melee / 1 missile** while the primary is in hand.
- DR: **Slashing 0, Piercing 0, Bludgeoning 0, Shot 0, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **51.0 lb**.
- Total slots: **17**; movement **30'**.
- Hands: primary 2; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+4 INT; Impact 4d4; handling clean**.
- Range/reload: **melee and range band 2, ranged Reload 4**.
- Spell memory: **0 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 99.5%, Armored mook 98.2%, Arbalester 81.0%, Musketeer 86.2%, Occult striker 89.2%, Harness knight 67.5% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open at range with Burning implement 4d4; declare damage type/mode before Impact. After a ranged discharge, mark Reload 4; use the same implement in melee rather than standing idle if the enemy closes. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

physical armor without the matching relic.

### Hard counters

stacked matching relic DR; ambushes and close pressure.

### Resource failure

If the implement is lost or confiscated, only the secondary weapon, remembered magic, armor, and relics remain. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise INT; raise WLL; raise STR.

### Campaign requirements

Wealth: privileged/elite; access: Unique, Common; legality follows visible arms, firearms, occult restrictions, and faction ownership. Campaign-developed at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: open field, lone play. Weakest: tight dungeon.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Exceptional |
| Sustained power | Low |
| Initiative | Moderate |
| Survival | Low |
| Mobility | 30' |
| Expedition value | Low |
| Party value | Moderate |
| Complexity | Low |
| Robustness | High |

### Verdict

**powerful but rare.**

## 11. Spear Brace Specialist

### Mechanical identity

Brace. Its main procedure is **Spear**; **Spear** is the primary weapon, Unarmored is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **spearman / hoplite**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 14 (+2) | Primary |
| INT | 3 (+0) | 3 (+0) | Secondary |
| FTH | 3 (+0) | 3 (+0) | Secondary |
| WLL | 3 (+0) | 12 (+1) | Important defense/utility |

- Natural 3d6 qualification: **100.000%**.
- Primary advancement: **STR**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **yes**.

### Core loadout

- Primary: **Spear**, 1d8 Piercing, 1 hand(s), 4 lb/1 slots, 1s, Common.
- Secondary: **none**.
- Armor: **Clothing**; 0 lb/0 slots, —.
- Relics: **none**.
- Remembered spells: **none**.
- Remembered miracles: **none**.
- Source: **none required**.
- Expedition equipment: **lantern and oil; 50' rope; bandages; water and rations; flint, chalk, sacks**.
- Ammunition: **30 arrows/bolts in the standardized 2-slot bundle**.

### Derived statistics

- AC: **1 melee / 1 missile** while the primary is in hand.
- DR: **Slashing 0, Piercing 0, Bludgeoning 0, Shot 0, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **28.0 lb**.
- Total slots: **9**; movement **45'**.
- Hands: primary 1; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+2 STR; Impact 1d8; handling clean**.
- Range/reload: **range band 1, Reload 0**.
- Spell memory: **0 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 74.7%, Armored mook 5.2%, Arbalester 18.4%, Musketeer 1.8%, Occult striker 72.5%, Harness knight 0.0% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open at range with Spear; declare damage type/mode before Impact. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

light and medium armor.

### Hard counters

coordinated Control, surprise, and asymmetric range.

### Resource failure

The build remains an ordinary armed and armored adventurer after consumables are lost. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise STR; raise WLL; raise INT.

### Campaign requirements

Wealth: low; access: Common; legality follows visible arms, firearms, occult restrictions, and faction ownership. Plausible at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: treasure extraction, long expedition. Weakest: lone play.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Low |
| Sustained power | Low |
| Initiative | Exceptional |
| Survival | Low |
| Mobility | 45' |
| Expedition value | High |
| Party value | Low |
| Complexity | Low |
| Robustness | Low |

### Verdict

**low-resource optimal.**

## 12. Arbalest Position Fighter

### Mechanical identity

Crossbow. Its main procedure is **Arbalest**; **Arbalest** is the primary weapon, Unarmored is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **crossbowman**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 12 (+1) | Fallback offense |
| INT | 3 (+0) | 3 (+0) | Secondary |
| FTH | 3 (+0) | 3 (+0) | Secondary |
| WLL | 3 (+0) | 14 (+2) | Primary |

- Natural 3d6 qualification: **100.000%**.
- Primary advancement: **WLL**.
- Secondary advancement: **STR**.
- Functions at +0/+1: **yes**.

### Core loadout

- Primary: **Arbalest**, 2d8 Piercing, 2 hand(s), 10 lb/3 slots, £2 10s, Military.
- Secondary: **Dagger**.
- Armor: **Clothing**; 0 lb/0 slots, —.
- Relics: **none**.
- Remembered spells: **none**.
- Remembered miracles: **none**.
- Source: **none required**.
- Expedition equipment: **lantern and oil; 50' rope; bandages; water and rations; flint, chalk, sacks**.
- Ammunition: **30 arrows/bolts in the standardized 2-slot bundle**.

### Derived statistics

- AC: **2 melee / 2 missile** while the primary is in hand.
- DR: **Slashing 0, Piercing 0, Bludgeoning 0, Shot 0, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **35.0 lb**.
- Total slots: **11**; movement **35'**.
- Hands: primary 2; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+2 WLL; Impact 2d8; handling clean**.
- Range/reload: **range band 2, Reload 2**.
- Spell memory: **0 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 98.9%, Armored mook 91.2%, Arbalester 78.6%, Musketeer 73.1%, Occult striker 92.7%, Harness knight 6.0% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open at range with Arbalest; declare damage type/mode before Impact. Reload behind allies or cover; the full reload clock is 2 actions. Use the sidearm if the line collapses. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

light and medium armor.

### Hard counters

ambushes and close pressure.

### Resource failure

The build remains an ordinary armed and armored adventurer after consumables are lost. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise WLL; raise STR; raise INT.

### Campaign requirements

Wealth: ordinary; access: Military, Common; legality follows visible arms, firearms, occult restrictions, and faction ownership. Plausible at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: treasure extraction, open field. Weakest: tight dungeon.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Low |
| Sustained power | Low |
| Initiative | Moderate |
| Survival | Low |
| Mobility | 35' |
| Expedition value | Moderate |
| Party value | Low |
| Complexity | Low |
| Robustness | Low |

### Verdict

**low-resource optimal.**

## 13. Low-Resource Extraction Fighter

### Mechanical identity

Extraction. Its main procedure is **Spear**; **Spear** is the primary weapon, Padded traveler kit is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **fighter-thief expedition generalist**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 14 (+2) | Primary |
| INT | 3 (+0) | 3 (+0) | Secondary |
| FTH | 3 (+0) | 3 (+0) | Secondary |
| WLL | 3 (+0) | 14 (+2) | Important defense/utility |

- Natural 3d6 qualification: **100.000%**.
- Primary advancement: **STR**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **yes**.

### Core loadout

- Primary: **Spear**, 1d8 Piercing, 1 hand(s), 4 lb/1 slots, 1s, Common.
- Secondary: **none**.
- Armor: **Padded jack, kettle hat, buckler**; 16.5 lb/5 slots, £1 16s.
- Relics: **none**.
- Remembered spells: **none**.
- Remembered miracles: **none**.
- Source: **none required**.
- Expedition equipment: **lantern and oil; 50' rope; maps and signals; bandages; water and rations**.
- Ammunition: **30 arrows/bolts in the standardized 2-slot bundle**.

### Derived statistics

- AC: **6 melee / 4 missile** while the primary is in hand.
- DR: **Slashing 5, Piercing 3, Bludgeoning 4, Shot 0, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **50.5 lb**.
- Total slots: **16**; movement **35'**.
- Hands: primary 1; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+2 STR; Impact 1d8; handling clean**.
- Range/reload: **range band 1, Reload 0**.
- Spell memory: **0 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 91.1%, Armored mook 10.5%, Arbalester 49.7%, Musketeer 4.9%, Occult striker 89.8%, Harness knight 0.0% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open at range with Spear; declare damage type/mode before Impact. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

light and medium armor.

### Hard counters

coordinated Control, surprise, and asymmetric range.

### Resource failure

The build remains an ordinary armed and armored adventurer after consumables are lost. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise STR; raise WLL; raise INT.

### Campaign requirements

Wealth: ordinary; access: Common; legality follows visible arms, firearms, occult restrictions, and faction ownership. Plausible at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: treasure extraction, long expedition. Weakest: lone play.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Low |
| Sustained power | Low |
| Initiative | Exceptional |
| Survival | Moderate |
| Mobility | 35' |
| Expedition value | Low |
| Party value | Low |
| Complexity | Low |
| Robustness | Low |

### Verdict

**low-resource optimal.**

## 14. Retainer Expedition Commander

### Mechanical identity

Commander. Its main procedure is **Spear**; **Spear** is the primary weapon, Padded traveler kit is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **warlord / expedition leader without class powers**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 14 (+2) | Primary |
| INT | 3 (+0) | 3 (+0) | Secondary |
| FTH | 16 (+3) | 16 (+3) | Primary |
| WLL | 3 (+0) | 14 (+2) | Important defense/utility |

- Natural 3d6 qualification: **4.630%**.
- Primary advancement: **STR**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **only in a reduced or over-wielded form**.

### Core loadout

- Primary: **Spear**, 1d8 Piercing, 1 hand(s), 4 lb/1 slots, 1s, Common.
- Secondary: **none**.
- Armor: **Padded jack, kettle hat, buckler**; 16.5 lb/5 slots, £1 16s.
- Relics: **none**.
- Remembered spells: **none**.
- Remembered miracles: **Staunch Blood L1; Blessing of Nerve L1; Rebuke the Dead L1**.
- Source: **Holy office or prayer book**.
- Expedition equipment: **lantern and oil; 50' rope; maps and signals; bandages; water and rations**.
- Ammunition: **30 arrows/bolts in the standardized 2-slot bundle**.

### Derived statistics

- AC: **6 melee / 4 missile** while the primary is in hand.
- DR: **Slashing 5, Piercing 3, Bludgeoning 4, Shot 0, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **50.5 lb**.
- Total slots: **16**; movement **35'**.
- Hands: primary 1; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+2 STR; Impact 1d8; handling clean**.
- Range/reload: **range band 1, Reload 0**.
- Spell memory: **0 levels**; miracle memory: **3 levels**.
- Monte Carlo wins: Light mook 91.1%, Armored mook 10.8%, Arbalester 49.7%, Musketeer 4.8%, Occult striker 89.8%, Harness knight 0.0% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open at range with Spear; declare damage type/mode before Impact. Against high AC or a named threat, spend control before trading damage; exploit Compromised/Controlled with allies or a dagger Gap Strike. Stabilize Bleeding/Grave allies before chasing damage. Recharge only after a remembered use is spent and retreat is otherwise worse. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

light and medium armor.

### Hard counters

source loss and expended memory.

### Resource failure

Spent memory leaves equipment and ordinary actions; source loss prevents safe restoration or rearrangement, not already remembered use. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise STR; raise WLL; raise INT.

### Campaign requirements

Wealth: ordinary; access: Common, Restricted source; legality follows visible arms, firearms, occult restrictions, and faction ownership. Plausible at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: treasure extraction, tight dungeon. Weakest: open field.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Low |
| Sustained power | Low |
| Initiative | Exceptional |
| Survival | Moderate |
| Mobility | 35' |
| Expedition value | Moderate |
| Party value | Low |
| Complexity | Low |
| Robustness | Low |

### Verdict

**party specialist.**

## 15. Mace-and-Shield Defender

### Mechanical identity

Shield. Its main procedure is **Mace**; **Mace** is the primary weapon, Padded traveler kit is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **fighting-man / defender**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 14 (+2) | Primary |
| INT | 3 (+0) | 3 (+0) | Secondary |
| FTH | 3 (+0) | 3 (+0) | Secondary |
| WLL | 3 (+0) | 12 (+1) | Important defense/utility |

- Natural 3d6 qualification: **100.000%**.
- Primary advancement: **STR**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **yes**.

### Core loadout

- Primary: **Mace**, 1d8 Bludgeoning, 1 hand(s), 2.75 lb/1 slots, 3s, Common.
- Secondary: **none**.
- Armor: **Padded jack, kettle hat, buckler**; 16.5 lb/5 slots, £1 16s.
- Relics: **none**.
- Remembered spells: **none**.
- Remembered miracles: **none**.
- Source: **none required**.
- Expedition equipment: **lantern and oil; 50' rope; bandages; water and rations; flint, chalk, sacks**.
- Ammunition: **none**.

### Derived statistics

- AC: **5 melee / 3 missile** while the primary is in hand.
- DR: **Slashing 5, Piercing 3, Bludgeoning 4, Shot 0, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **37.2 lb**.
- Total slots: **12**; movement **40'**.
- Hands: primary 1; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+2 STR; Impact 1d8; handling clean**.
- Range/reload: **range band 0, Reload 0**.
- Spell memory: **0 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 90.3%, Armored mook 10.3%, Arbalester 28.7%, Musketeer 1.4%, Occult striker 67.0%, Harness knight 0.0% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open with Mace, using its retained Impact as initiative and damage. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

mail and armor reliant on cut resistance.

### Hard counters

coordinated Control, surprise, and asymmetric range.

### Resource failure

The build remains an ordinary armed and armored adventurer after consumables are lost. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise STR; raise WLL; raise INT.

### Campaign requirements

Wealth: ordinary; access: Common; legality follows visible arms, firearms, occult restrictions, and faction ownership. Plausible at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: treasure extraction, long expedition. Weakest: open field.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Low |
| Sustained power | Low |
| Initiative | Exceptional |
| Survival | Moderate |
| Mobility | 40' |
| Expedition value | Moderate |
| Party value | Low |
| Complexity | Low |
| Robustness | Low |

### Verdict

**low-resource optimal.**

## 16. Relic Morale Minister

### Mechanical identity

Miracle-relic worker. Its main procedure is **Spear**; **Spear** is the primary weapon, Padded traveler kit is the defensive commitment, and burning and freezing relics 1d6 is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **cleric / turner and morale support**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 14 (+2) | Fallback offense |
| INT | 3 (+0) | 3 (+0) | Secondary |
| FTH | 16 (+3) | 16 (+3) | Primary |
| WLL | 3 (+0) | 12 (+1) | Important defense/utility |

- Natural 3d6 qualification: **4.630%**.
- Primary advancement: **FTH**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **only in a reduced or over-wielded form**.

### Core loadout

- Primary: **Spear**, 1d8 Piercing, 1 hand(s), 4 lb/1 slots, 1s, Common.
- Secondary: **none**.
- Armor: **Padded jack, kettle hat, buckler**; 16.5 lb/5 slots, £1 16s.
- Relics: **1× 1d6 Burning; 1× 1d6 Freezing**.
- Remembered spells: **none**.
- Remembered miracles: **Blessing of Nerve L1; Rebuke the Dead L1; Omen L1**.
- Source: **Holy office or prayer book**.
- Expedition equipment: **lantern and oil; 50' rope; maps and signals; bandages; water and rations**.
- Ammunition: **30 arrows/bolts in the standardized 2-slot bundle**.

### Derived statistics

- AC: **5 melee / 3 missile** while the primary is in hand.
- DR: **Slashing 5, Piercing 3, Bludgeoning 4, Shot 0, Burning 6, Shocking 0, Toxic 0, Freezing 6**.
- Total carried weight: **62.5 lb**.
- Total slots: **20**; movement **30'**.
- Hands: primary 1; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+2 STR; Impact 1d8; handling clean**.
- Range/reload: **range band 1, Reload 0**.
- Spell memory: **0 levels**; miracle memory: **3 levels**.
- Monte Carlo wins: Light mook 91.0%, Armored mook 10.7%, Arbalester 36.4%, Musketeer 2.5%, Occult striker 98.4%, Harness knight 0.0% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open at range with Spear; declare damage type/mode before Impact. Against high AC or a named threat, spend control before trading damage; exploit Compromised/Controlled with allies or a dagger Gap Strike. Relic DR is passive and stacked; change positioning or damage type rather than spending actions to activate it. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

light and medium armor; occult volleys.

### Hard counters

physical armor-breakers; source loss and expended memory.

### Resource failure

If relics are lost, physical AC/DR remains but exotic protection collapses. Spent memory leaves equipment and ordinary actions; source loss prevents safe restoration or rearrangement, not already remembered use. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise FTH; raise WLL; raise STR.

### Campaign requirements

Wealth: professional; access: Common, Restricted, Restricted source; legality follows visible arms, firearms, occult restrictions, and faction ownership. Campaign-developed at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: magic-rich opposition, tight dungeon. Weakest: open field.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Low |
| Sustained power | Low |
| Initiative | Exceptional |
| Survival | High |
| Mobility | 30' |
| Expedition value | Low |
| Party value | Low |
| Complexity | High |
| Robustness | Low |

### Verdict

**party specialist.**

## 17. Control Magician

### Mechanical identity

Spell specialist. Its main procedure is **Arcane control triad**; **Dagger** is the exhausted fallback, Unarmored is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **magic-user / battlefield controller**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 3 (+0) | Fallback offense |
| INT | 16 (+3) | 16 (+3) | Primary |
| FTH | 3 (+0) | 3 (+0) | Secondary |
| WLL | 3 (+0) | 12 (+1) | Important defense/utility |

- Natural 3d6 qualification: **4.630%**.
- Primary advancement: **INT**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **only in a reduced or over-wielded form**.

### Core loadout

- Primary: **Dagger**, 1d4 Slashing/Piercing, 1 hand(s), 1 lb/0 slots, 1s, Common.
- Secondary: **none**.
- Armor: **Clothing**; 0 lb/0 slots, —.
- Relics: **none**.
- Remembered spells: **Hex of Stumbling L1; Fog / Smoke L1; Sleep Charm L1**.
- Remembered miracles: **none**.
- Source: **Arcane grimoire**.
- Expedition equipment: **torch or candle; bandages; water and rations; chalk, flint, sacks**.
- Ammunition: **none**.

### Derived statistics

- AC: **1 melee / 1 missile** while the primary is in hand.
- DR: **Slashing 0, Piercing 0, Bludgeoning 0, Shot 0, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **13.0 lb**.
- Total slots: **4**; movement **40'**.
- Hands: primary 1; shield defense is inactive with an incompatible two-handed primary.
- Attack: **Working attack +3 INT; direct Impact effect-based; dagger fallback +0 STR, 1d4**.
- Range/reload: **Working range/effect as listed; dagger melee fallback**.
- Spell memory: **3 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 33.6%, Armored mook 32.0%, Arbalester 15.1%, Musketeer 14.7%, Occult striker 30.4%, Harness knight 6.6% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open with Arcane control triad; change the fight with Control, smoke, sleep, or escape before drawing the dagger. Against high AC or a named threat, spend control before trading damage; exploit Compromised/Controlled with allies or a dagger Gap Strike. Once memory is spent, use light, tools, positioning, and the dagger only as a last resort. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

high-AC groups vulnerable to Control and terrain.

### Hard counters

named-target Defense; expended memory; source loss.

### Resource failure

Spent memory leaves equipment and ordinary actions; source loss prevents safe restoration or rearrangement, not already remembered use. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise INT; raise WLL; raise STR.

### Campaign requirements

Wealth: low; access: Common, Restricted source; legality follows visible arms, firearms, occult restrictions, and faction ownership. Plausible at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: treasure extraction, long expedition. Weakest: open field.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Low |
| Sustained power | Low |
| Initiative | Exceptional |
| Survival | Low |
| Mobility | 40' |
| Expedition value | High |
| Party value | Low |
| Complexity | Low |
| Robustness | Moderate |

### Verdict

**niche optimal.**

## 18. Relic Field Minister

### Mechanical identity

Miracle-relic worker. Its main procedure is **Spear**; **Spear** is the primary weapon, Padded traveler kit is the defensive commitment, and burning and freezing relics 1d6 is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **battle cleric / field medic**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 14 (+2) | Fallback offense |
| INT | 3 (+0) | 3 (+0) | Secondary |
| FTH | 16 (+3) | 16 (+3) | Primary |
| WLL | 3 (+0) | 12 (+1) | Important defense/utility |

- Natural 3d6 qualification: **4.630%**.
- Primary advancement: **FTH**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **only in a reduced or over-wielded form**.

### Core loadout

- Primary: **Spear**, 1d8 Piercing, 1 hand(s), 4 lb/1 slots, 1s, Common.
- Secondary: **none**.
- Armor: **Padded jack, kettle hat, buckler**; 16.5 lb/5 slots, £1 16s.
- Relics: **1× 1d6 Burning; 1× 1d6 Freezing**.
- Remembered spells: **none**.
- Remembered miracles: **Staunch Blood L1; Blessing of Nerve L1; Rebuke the Dead L1**.
- Source: **Holy office or prayer book**.
- Expedition equipment: **lantern and oil; 50' rope; medical and surgical tools; bandages; water and rations**.
- Ammunition: **30 arrows/bolts in the standardized 2-slot bundle**.

### Derived statistics

- AC: **5 melee / 3 missile** while the primary is in hand.
- DR: **Slashing 5, Piercing 3, Bludgeoning 4, Shot 0, Burning 6, Shocking 0, Toxic 0, Freezing 6**.
- Total carried weight: **62.5 lb**.
- Total slots: **20**; movement **30'**.
- Hands: primary 1; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+2 STR; Impact 1d8; handling clean**.
- Range/reload: **range band 1, Reload 0**.
- Spell memory: **0 levels**; miracle memory: **3 levels**.
- Monte Carlo wins: Light mook 91.1%, Armored mook 10.6%, Arbalester 36.9%, Musketeer 2.5%, Occult striker 98.3%, Harness knight 0.0% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open at range with Spear; declare damage type/mode before Impact. Against high AC or a named threat, spend control before trading damage; exploit Compromised/Controlled with allies or a dagger Gap Strike. Relic DR is passive and stacked; change positioning or damage type rather than spending actions to activate it. Stabilize Bleeding/Grave allies before chasing damage. Recharge only after a remembered use is spent and retreat is otherwise worse. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

light and medium armor; occult volleys.

### Hard counters

physical armor-breakers; source loss and expended memory.

### Resource failure

If relics are lost, physical AC/DR remains but exotic protection collapses. Spent memory leaves equipment and ordinary actions; source loss prevents safe restoration or rearrangement, not already remembered use. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise FTH; raise WLL; raise STR.

### Campaign requirements

Wealth: professional; access: Common, Restricted, Restricted source; legality follows visible arms, firearms, occult restrictions, and faction ownership. Campaign-developed at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: magic-rich opposition, tight dungeon. Weakest: open field.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Low |
| Sustained power | Low |
| Initiative | Exceptional |
| Survival | High |
| Mobility | 30' |
| Expedition value | Low |
| Party value | Low |
| Complexity | High |
| Robustness | Low |

### Verdict

**party specialist.**

## 19. Sword-and-Shield Defender

### Mechanical identity

Shield. Its main procedure is **Short sword**; **Short sword** is the primary weapon, Padded traveler kit is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **fighting-man / defender**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 3 (+0) | 14 (+2) | Primary |
| INT | 3 (+0) | 3 (+0) | Secondary |
| FTH | 3 (+0) | 3 (+0) | Secondary |
| WLL | 3 (+0) | 12 (+1) | Important defense/utility |

- Natural 3d6 qualification: **100.000%**.
- Primary advancement: **STR**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **yes**.

### Core loadout

- Primary: **Short sword**, 1d6 Slashing/Piercing, 1 hand(s), 2 lb/1 slots, 2s, Common.
- Secondary: **none**.
- Armor: **Padded jack, kettle hat, buckler**; 16.5 lb/5 slots, £1 16s.
- Relics: **none**.
- Remembered spells: **none**.
- Remembered miracles: **none**.
- Source: **none required**.
- Expedition equipment: **lantern and oil; 50' rope; bandages; water and rations; flint, chalk, sacks**.
- Ammunition: **none**.

### Derived statistics

- AC: **5 melee / 3 missile** while the primary is in hand.
- DR: **Slashing 5, Piercing 3, Bludgeoning 4, Shot 0, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **36.5 lb**.
- Total slots: **12**; movement **40'**.
- Hands: primary 1; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+2 STR; Impact 1d6; handling clean**.
- Range/reload: **range band 0, Reload 0**.
- Spell memory: **0 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 6.9%, Armored mook 0.0%, Arbalester 2.3%, Musketeer 0.0%, Occult striker 40.4%, Harness knight 0.0% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open with Short sword, using its retained Impact as initiative and damage. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

light and medium armor.

### Hard counters

coordinated Control, surprise, and asymmetric range.

### Resource failure

The build remains an ordinary armed and armored adventurer after consumables are lost. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise STR; raise WLL; raise INT.

### Campaign requirements

Wealth: ordinary; access: Common; legality follows visible arms, firearms, occult restrictions, and faction ownership. Plausible at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: treasure extraction, long expedition. Weakest: open field.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Low |
| Sustained power | Low |
| Initiative | Exceptional |
| Survival | Moderate |
| Mobility | 40' |
| Expedition value | Moderate |
| Party value | Low |
| Complexity | Low |
| Robustness | Moderate |

### Verdict

**low-resource optimal.**

## 20. Full-Harness Poleaxe Fighter

### Mechanical identity

Armor breaker. Its main procedure is **Poleaxe**; **Poleaxe** is the primary weapon, Full harness knight kit is the defensive commitment, and no relic is its exotic-defense choice. It was selected as the strongest practical representative of a distinct action economy, defense, range profile, or expedition role.

### Historical analogue

Closest analogue: **man-at-arms / anti-armor specialist**. The analogue is incomplete because GEWINN grants no class package: the role comes from the exact weapon, armor, relic, remembered Workings, load, and retreat procedure.

### Stat profile

| Ability | Minimum | Preferred | Importance |
|---|---:|---:|---|
| STR | 14 (+2) | 14 (+2) | Primary |
| INT | 3 (+0) | 3 (+0) | Secondary |
| FTH | 3 (+0) | 3 (+0) | Secondary |
| WLL | 3 (+0) | 12 (+1) | Important defense/utility |

- Natural 3d6 qualification: **16.204%**.
- Primary advancement: **STR**.
- Secondary advancement: **WLL**.
- Functions at +0/+1: **only in a reduced or over-wielded form**.

### Core loadout

- Primary: **Poleaxe**, 2d6 Bludgeoning/Piercing, 2 hand(s), 6.5 lb/2 slots, £1 5s, Elite.
- Secondary: **Dagger**.
- Armor: **Full harness, close helm, plate arms, full plate legs**; 50 lb/16 slots, £29 10s.
- Relics: **none**.
- Remembered spells: **none**.
- Remembered miracles: **none**.
- Source: **none required**.
- Expedition equipment: **torch; rope; bandages; water and rations**.
- Ammunition: **30 arrows/bolts in the standardized 2-slot bundle**.

### Derived statistics

- AC: **12 melee / 12 missile** while the primary is in hand.
- DR: **Slashing 18, Piercing 12, Bludgeoning 9, Shot 8, Burning 0, Shocking 0, Toxic 0, Freezing 0**.
- Total carried weight: **78.5 lb**.
- Total slots: **25**; movement **25'**.
- Hands: primary 2; shield defense is inactive with an incompatible two-handed primary.
- Attack: **+2 STR; Impact 2d6; handling clean**.
- Range/reload: **range band 1, Reload 0**.
- Spell memory: **0 levels**; miracle memory: **0 levels**.
- Monte Carlo wins: Light mook 100.0%, Armored mook 93.6%, Arbalester 98.5%, Musketeer 86.6%, Occult striker 98.0%, Harness knight 0.0% (100,000 trials per matchup; see CSV for confidence intervals).

### Core procedure

Open at range with Poleaxe; declare damage type/mode before Impact. If Controlled, abandon the pending attack and escape with STR or WLL. Retreat after the first Grave wound unless the objective makes that loss acceptable.

### Best matchups

mail and armor reliant on cut resistance; ordinary physical mooks.

### Hard counters

Control and Gap Strike.

### Resource failure

The build remains an ordinary armed and armored adventurer after consumables are lost. A Grave wound changes the objective to extraction; drop treasure before dropping armor unless pursuit, water, or climbing makes armor the greater danger.

### Advancement

raise STR; raise WLL; raise INT.

### Campaign requirements

Wealth: privileged/elite; access: Elite, Common; legality follows visible arms, firearms, occult restrictions, and faction ownership. Campaign-developed at character creation under ordinary 2d4£ only when the listed restricted equipment is actually available.

Campaign environments: Strongest: magic-rich opposition, lone play. Weakest: treasure extraction.

### Performance summary

| Metric | Value or Tier |
|---|---|
| Opening power | Low |
| Sustained power | Low |
| Initiative | High |
| Survival | Exceptional |
| Mobility | 25' |
| Expedition value | Low |
| Party value | Low |
| Complexity | Low |
| Robustness | High |

### Verdict

**niche optimal.**

# Best four-character parties

| Party                  | Members                                                                                                      |   Combined Slots | Damage Coverage                   | Defense Coverage                     | Reload Pattern                                                                                                    | Spell/Miracle Coverage                                                                                          | Retreat Plan                                                             | Primary Weakness                               |
|:-----------------------|:-------------------------------------------------------------------------------------------------------------|-----------------:|:----------------------------------|:-------------------------------------|:------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------|:-----------------------------------------------|
| General dungeon        | Rifle Specialist; Spell-and-Implement Magician; Direct-Damage Magician; Implement-and-Relic Hybrid           |               44 | Burning; Piercing; Shot; Slashing | physical mean 0.23; exotic mean 0.53 | Rifle Specialist: 4; Spell-and-Implement Magician: 2; Implement-and-Relic Hybrid: 3                               | Hex of Stumbling L1; Fog / Smoke L1; Sleep Charm L1; Firebrand L1; Firebrand L1; Firebrand L1                   | drop treasure; control rear guard; carry wounded with highest STR member | shared source/slot/range pressure if clustered |
| Armored-enemy hunters  | Rifle Specialist; Four-Type Relic Defender; Implement-and-Relic Hybrid; High-Stat Implement Artillery        |               62 | Burning; Shot                     | physical mean 0.23; exotic mean 0.68 | Rifle Specialist: 4; Four-Type Relic Defender: 3; Implement-and-Relic Hybrid: 3; High-Stat Implement Artillery: 4 | none                                                                                                            | drop treasure; control rear guard; carry wounded with highest STR member | shared source/slot/range pressure if clustered |
| Magic-heavy opposition | Implement-and-Relic Hybrid; Relic Morale Minister; Relic Field Minister; Full-Harness Poleaxe Fighter        |               83 | Bludgeoning; Burning; Piercing    | physical mean 0.51; exotic mean 0.91 | Implement-and-Relic Hybrid: 3                                                                                     | Blessing of Nerve L1; Rebuke the Dead L1; Omen L1; Staunch Blood L1; Blessing of Nerve L1; Rebuke the Dead L1   | drop treasure; control rear guard; carry wounded with highest STR member | shared source/slot/range pressure if clustered |
| Low-wealth             | Warhammer Armor Breaker; Spear Brace Specialist; Low-Resource Extraction Fighter; Sword-and-Shield Defender  |               44 | Bludgeoning; Piercing; Slashing   | physical mean 0.34; exotic mean 0.38 |                                                                                                                   | none                                                                                                            | drop treasure; control rear guard; carry wounded with highest STR member | shared source/slot/range pressure if clustered |
| Open-field military    | Rifle Specialist; Spell-and-Implement Magician; High-Stat Implement Artillery; Retainer Expedition Commander |               55 | Burning; Piercing; Shot           | physical mean 0.29; exotic mean 0.38 | Rifle Specialist: 4; Spell-and-Implement Magician: 2; High-Stat Implement Artillery: 4                            | Hex of Stumbling L1; Fog / Smoke L1; Sleep Charm L1; Staunch Blood L1; Blessing of Nerve L1; Rebuke the Dead L1 | drop treasure; control rear guard; carry wounded with highest STR member | shared source/slot/range pressure if clustered |

The party Monte Carlo results, confidence intervals, reload counts, and casualties are stored in the combined CSV.

# Exact selected-build matchups

The complete 200-row exact matchup matrix is in the CSV. It includes hit, miss/Stopped, all wound bands, initiative, cycle length, and sustained Serious+ against ten representative defenses. A separate exact table gives failed-Defense and two-success Control probabilities against all six simulated threat bands.

# Campaign-environment analysis

Every final build is scored in all twenty required campaign environments; the full 400-row matrix is in the CSV. Build cards list strongest and weakest environments.

# Ability-value analysis

| Ability   |   Builds Using It |   Offensive Value |   Defensive Value |   Utility Value | Dominance Risk   |
|:----------|------------------:|------------------:|------------------:|----------------:|:-----------------|
| STR       |                17 |             0.340 |             0.413 |           0.166 | High             |
| INT       |                 7 |             0.512 |             0.311 |           0.337 | Low              |
| FTH       |                 5 |             0.341 |             0.532 |           0.300 | Low              |
| WLL       |                20 |             0.345 |             0.393 |           0.191 | High             |

WLL remains the broadest defensive ability because it contributes AC, Shock/Panic resilience, aimed attacks, and retreat discipline. It is not sufficient by itself: STR governs load, Control and clean multi-die muscle weapons; INT governs repeatable exotic offense and spells; FTH governs persistent exotic DR, miracles, and Divine Favour.

# Pure versus hybrid

| Build Type   |   Mean Score |   Mean Slots |   Mean Stat Requirement |   Mean Survival |   Mean Party Value |
|:-------------|-------------:|-------------:|------------------------:|----------------:|-------------------:|
| Pure         |        0.407 |       13.000 |                   0.750 |           0.379 |              0.334 |
| Hybrid       |        0.421 |       13.500 |                   2.625 |           0.414 |              0.423 |

Hybrids generally win matchup breadth but lose slot efficiency, natural qualification, hand simplicity, and resilience after item/source loss. The best parties therefore combine specialists rather than duplicating four full mixed adventurers.

# Equipment concentration

| Item                            |   Top-20 Uses | Why                                           | Mandatory or Optional?     |
|:--------------------------------|--------------:|:----------------------------------------------|:---------------------------|
| Unarmored                       |            13 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Dagger                          |            11 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Padded traveler kit             |             6 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Spear                           |             5 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Burning and Freezing relics 1d6 |             3 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Musket                          |             2 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Rifle                           |             1 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Burning implement 2d4           |             1 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| One 1d4 relic of each type      |             1 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Burning implement 3d4           |             1 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Burning implement 1d4           |             1 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Burning implement 1d8           |             1 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Warhammer                       |             1 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Composite bow                   |             1 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Burning implement 4d4           |             1 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Arbalest                        |             1 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Mace                            |             1 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Short sword                     |             1 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Poleaxe                         |             1 | Primary offense/defense or resilient fallback | Mandatory for listed build |
| Full harness knight kit         |             1 | Primary offense/defense or resilient fallback | Mandatory for listed build |

# Damage-type coverage

| Damage Type   |   Builds Using It | Common Defenses        | Strategic Value                    | Redundant?   |
|:--------------|------------------:|:-----------------------|:-----------------------------------|:-------------|
| Slashing      |                12 | physical armor/shields | High                               | No           |
| Piercing      |                18 | physical armor/shields | High                               | No           |
| Bludgeoning   |                 3 | physical armor/shields | High                               | No           |
| Shot          |                 3 | physical armor/shields | High                               | No           |
| Burning       |                 5 | Burning relic DR       | High                               | No           |
| Shocking      |                 0 | Shocking relic DR      | Unrepresented in final primary set | No           |
| Toxic         |                 0 | Toxic relic DR         | Unrepresented in final primary set | No           |
| Freezing      |                 0 | Freezing relic DR      | Unrepresented in final primary set | No           |

# Historical archetype comparison

| GEWINN Build                    | Historical Analogue                                           | Similarity                    | Critical Difference                                                                   |
|:--------------------------------|:--------------------------------------------------------------|:------------------------------|:--------------------------------------------------------------------------------------|
| Rifle Specialist                | musketeer / sharpshooter                                      | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Spell-and-Implement Magician    | gish, but one-stat and gear-bound                             | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Four-Type Relic Defender        | paladin or magic-resistant tank, but entirely equipment-based | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Direct-Damage Magician          | magic-user / artillery caster                                 | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Implement-and-Relic Hybrid      | occult-sacred hybrid                                          | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Gun-and-Implement Hybrid        | gun-mage                                                      | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Low-N Implement Duelist         | magic-user / warlock, but weaponized and repeatable           | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Warhammer Armor Breaker         | man-at-arms / anti-armor specialist                           | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Composite-Bow Specialist        | ranger or longbowman                                          | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| High-Stat Implement Artillery   | artillery mage / glass cannon                                 | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Spear Brace Specialist          | spearman / hoplite                                            | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Arbalest Position Fighter       | crossbowman                                                   | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Low-Resource Extraction Fighter | fighter-thief expedition generalist                           | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Retainer Expedition Commander   | warlord / expedition leader without class powers              | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Mace-and-Shield Defender        | fighting-man / defender                                       | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Relic Morale Minister           | cleric / turner and morale support                            | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Control Magician                | magic-user / battlefield controller                           | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Relic Field Minister            | battle cleric / field medic                                   | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Sword-and-Shield Defender       | fighting-man / defender                                       | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |
| Full-Harness Poleaxe Fighter    | man-at-arms / anti-armor specialist                           | role and equipment silhouette | no class features; material loadout, wounds, memory, and source rules create the role |

# Failed and dominated archetypes

| Expected Archetype              | Why It Failed                                                                                       | Dominated By                                          | Could It Still Be Fun?              |
|:--------------------------------|:----------------------------------------------------------------------------------------------------|:------------------------------------------------------|:------------------------------------|
| Unarmored melee duelist         | Armor and one-hit wound risk overwhelm its initiative/slot advantage                                | Padded shield or implement duelist                    | Yes, as a desperate or social build |
| Pure healer with no weapon      | After limited miracles, it contributes no proactive pressure                                        | Miracle-relic worker with mace, spear, or crossbow    | Yes, in retainer-heavy play         |
| Recharge caster                 | Recharge wounds become Serious/Grave faster than repeat output repays the risk                      | Spell-implement hybrid or ordinary sidearm            | Yes, as an emergency tactic         |
| Universal full mixed adventurer | Stat rarity, slots, hands, and source dependence reduce expedition value                            | Two-axis hybrids and a coordinated party              | Yes, at high advancement            |
| One-die d12 implement regular   | Combat value is extreme but the item is Unique, 24 lb/8 slots, and not a normal starting assumption | 1d8 or 2d4 restricted implement in ordinary campaigns | Yes, as a campaign treasure         |
| Three matching relic stacker    | Hard-locks one type but spends slots on a defense an opponent can bypass                            | One relic per type or armor plus one targeted relic   | Yes, in a known elemental war       |
| Longbow build at ordinary STR   | 4-die handling requires STR +4 for clean use                                                        | Crossbow/arbalest at ordinary stats                   | Yes, as a rare heroic specialist    |

# Exploit log

| ID   | Severity       | Build                             | Reproduction                                                                           | Evidence                                                                                   | Campaign Effect                                                                           | Rules-Legal?   | Minimal Correction                                                       |
|:-----|:---------------|:----------------------------------|:---------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|:---------------|:-------------------------------------------------------------------------|
| B-01 | Major          | Low-N high-S implement            | Use a Unique 1d10/1d12 implement at INT +0/+1; N=1 gives clean handling and Reload 1   | Exact high opening damage; excluded from normal-stock winners by availability and load     | Unique treasure can temporarily dominate ordinary ranged gear                             | Yes            | None in optimizer; enforce current weight, cost, and Unique availability |
| B-02 | Major          | Four-type implement carrier       | Carry several implements and choose an unprotected type before Impact                  | Broad matchup score rises, but 12+ implement slots destroy expedition load                 | Rich supported parties can bypass narrow relics                                           | Yes            | None; enforce slots, hands, declaration, loss/confiscation               |
| B-03 | Moderate       | Full armor plus four 1d4 relics   | Add 4 slots and DR4 in each exotic type to serious armor                               | High survival, low movement/treasure capacity                                              | Strong prepared tank; Control, water, retreat and physical armor-breakers remain counters | Yes            | None                                                                     |
| B-04 | Watchlist      | Melee use during implement reload | Discharge at range, then use same NdS implement in melee while ranged mode reloads     | Improves resilience but requires enemy closure and gives up another ranged discharge       | Prevents dead rounds; does not erase reload at range                                      | Yes            | None                                                                     |
| B-05 | Confirmed safe | Recharge/healing loop             | Recharge remembered healing, then attempt magical healing of recharge wound            | Canonical anti-healing rule blocks the loop                                                | Recharge remains desperate                                                                | No loop        | None                                                                     |
| B-06 | Moderate       | Control into Gap Strike           | Two successes Control a target; dagger Gap Strike ignores armor and is minimum Serious | Strong party payoff but requires actions, proximity, opposed checks and maintained Control | Correct counter to walking fortresses                                                     | Yes            | None                                                                     |

# Population analysis

|   Rank | Build                           |   Qualifying Characters |   Frequency |   Analytic Frequency |   Minimum STR |   Minimum INT |   Minimum FTH |   Minimum WLL |
|-------:|:--------------------------------|------------------------:|------------:|---------------------:|--------------:|--------------:|--------------:|--------------:|
|      1 | Rifle Specialist                |                 1000000 |     1.00000 |              1.00000 |             0 |             0 |             0 |             0 |
|      2 | Spell-and-Implement Magician    |                   46545 |     0.04655 |              0.04630 |             0 |             3 |             0 |             0 |
|      3 | Four-Type Relic Defender        |                 1000000 |     1.00000 |              1.00000 |             0 |             0 |             0 |             0 |
|      4 | Direct-Damage Magician          |                   46545 |     0.04655 |              0.04630 |             0 |             3 |             0 |             0 |
|      5 | Implement-and-Relic Hybrid      |                   46545 |     0.04655 |              0.04630 |             0 |             3 |             0 |             0 |
|      6 | Gun-and-Implement Hybrid        |                 1000000 |     1.00000 |              1.00000 |             0 |             0 |             0 |             0 |
|      7 | Low-N Implement Duelist         |                 1000000 |     1.00000 |              1.00000 |             0 |             0 |             0 |             0 |
|      8 | Warhammer Armor Breaker         |                 1000000 |     1.00000 |              1.00000 |             0 |             0 |             0 |             0 |
|      9 | Composite-Bow Specialist        |                   46044 |     0.04604 |              0.04630 |             3 |             0 |             0 |             0 |
|     10 | High-Stat Implement Artillery   |                    4595 |     0.00460 |              0.00463 |             0 |             4 |             0 |             0 |
|     11 | Spear Brace Specialist          |                 1000000 |     1.00000 |              1.00000 |             0 |             0 |             0 |             0 |
|     12 | Arbalest Position Fighter       |                 1000000 |     1.00000 |              1.00000 |             0 |             0 |             0 |             0 |
|     13 | Low-Resource Extraction Fighter |                 1000000 |     1.00000 |              1.00000 |             0 |             0 |             0 |             0 |
|     14 | Retainer Expedition Commander   |                   46269 |     0.04627 |              0.04630 |             0 |             0 |             3 |             0 |
|     15 | Mace-and-Shield Defender        |                 1000000 |     1.00000 |              1.00000 |             0 |             0 |             0 |             0 |
|     16 | Relic Morale Minister           |                   46269 |     0.04627 |              0.04630 |             0 |             0 |             3 |             0 |
|     17 | Control Magician                |                   46545 |     0.04655 |              0.04630 |             0 |             3 |             0 |             0 |
|     18 | Relic Field Minister            |                   46269 |     0.04627 |              0.04630 |             0 |             0 |             3 |             0 |
|     19 | Sword-and-Shield Defender       |                 1000000 |     1.00000 |              1.00000 |             0 |             0 |             0 |             0 |
|     20 | Full-Harness Poleaxe Fighter    |                  161843 |     0.16184 |              0.16204 |             2 |             0 |             0 |             0 |

# Final observations

1. The strongest ordinary build pattern is **specialist offense + enough armor to survive its reload or initiative weakness + one expedition fallback**.
2. Shields remain excellent for one-die physical weapons but disappear from active defense when the character commits to an incompatible two-handed weapon or implement.
3. Self-powered crossbows are the premier low-stat ranged build; longbows are a rare clean-STR build rather than a default archer.
4. Implements are strongest as one-stat repeatable weapons, but matching relics and their enormous weight at high ratings keep ordinary d4/d6/d8 branches matchup-dependent.
5. Miracles are most efficient when attached to an armed relic bearer; a weaponless healer is a dead choice after memory is spent.
6. Recharge is not a build engine. It is an emergency exchange of future survival for one restored Working.
7. The optimizer found no reason to alter the corrected physical weapon or armor values.