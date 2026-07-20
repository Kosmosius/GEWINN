# GEWINN v2.5 → Current Working Rules
## Codex-Readable Migration Changelog

**Purpose:** update a local GEWINN v2.5 source tree into the current working rules without importing superseded v3–v6 experiments.

**This is a migration specification, not a historical essay.** Every instruction is one of:

- `KEEP`: preserve v2.5 content unless another instruction replaces it.
- `REPLACE`: remove the old rule/table and insert the current rule/table.
- `ADD`: insert new material.
- `DELETE`: remove obsolete text and all dependent references.
- `REGENERATE`: calculate derived values from canonical data files.
- `TODO`: intentionally unresolved; Codex must not invent a solution.

---

# 0. Source authority

Apply sources in this order:

1. This changelog and `GEWINN_v2_5_to_current_CHANGE_MANIFEST.yaml`.
2. The CSV tables shipped beside this changelog.
3. Latest explicit designer decisions represented here.
4. GEWINN v5.0 only for complete procedures not replaced here.
5. GEWINN v2.5 for voice, original identity, front matter, discrete wound flavor, attribution, and untouched material.
6. Ignore intermediate v3–v6 mechanics unless explicitly retained here.

The designer-written v2.5 document remains the voice and identity anchor. The v5 text is a useful full-system scaffold, but it contains obsolete Scale, Arms Training, old slot semantics, old proofing, old magic, old names, and stale equipment values. Do not merge those obsolete elements.

---

# 1. Repository recommendation

**Yes: create a repository before Codex edits anything.**

Minimum safe workflow:

```text
main
  └── exact untouched v2.5 source commit
migration/v2.5-current
  └── Codex applies this migration in subsystem-sized commits
```

Recommended structure:

```text
GEWINN/
├── README.md
├── CHANGELOG.md
├── LICENSE.md
├── rules/
│   ├── 00-front-matter.md
│   ├── 01-core.md
│   ├── 02-characters.md
│   ├── 03-stress-growth.md
│   ├── 04-exploration.md
│   ├── 05-combat.md
│   ├── 06-wounds.md
│   ├── 07-equipment.md
│   ├── 08-magic.md
│   ├── 09-recovery.md
│   ├── 10-retainers-economy.md
│   ├── 11-monsters-conversion.md
│   └── 12-reference.md
├── data/
│   ├── melee_weapons.csv
│   ├── ranged_weapons.csv
│   ├── body_armor.csv
│   ├── helmets.csv
│   ├── arms_armor.csv
│   ├── leg_armor.csv
│   ├── shields.csv
│   ├── proofing.csv
│   ├── common_armor_kits.csv
│   ├── occult_implements.csv
│   └── sacred_relics.csv
├── tools/
│   ├── validate_terms.py
│   ├── validate_kits.py
│   └── generate_tables.py
├── playtest/
│   ├── session-report.md
│   └── issues.md
└── archive/
    ├── GEWINN_v2.5.pdf
    └── superseded-drafts/
```

Do not ask Codex to rewrite the whole book in one commit. Use the implementation order in section 25.

---

# 2. Global terminology and schema migration

## 2.1 DELETE globally

Delete these mechanics and all references, character-sheet fields, examples, glossary entries, probability assumptions, and derived values:

- `Scale`, `Weapon Scale`, `Draw Scale`.
- `Arms Training` and `Mastery`.
- `Breach`.
- `Cut`, `Point`, `Crush` as damage-type names.
- Pistol-proof, musket-proof, and all range-dependent proofing.
- Slots representing awkwardness, length, heat, visibility, noise, legality, or social burden.
- Separate purchases for half-swording, mordhau, or unmounted lance.
- Arcane Circle, Holy Circle, Prepared Load.
- Source Strain, Relic Strain, Push, Power, Disturbance.
- Transcendent Exertion, Force Through, Petition, Greater Petition.
- Reactive per-hit relic DR rolls.
- Non-stacking relic rules.
- Generic mana, spell points, caster level, caster classes, spellcasting proficiency, and weapon training.
- The separate `Growth-eligible Stress` field and any non-growth-eligible Stress category.

## 2.2 REPLACE globally

| Old term | Current term |
|---|---|
| FAI | FTH when abbreviated; `Faith` in prose |
| Cut | Slashing |
| Point | Piercing |
| Crush | Bludgeoning |
| Damage | Impact when referring to the retained initiative roll |
| Spell/prayer rank where copied from v5 | Original classic spell level, unless an individually converted Working says otherwise |

## 2.3 ADD global damage taxonomy

The final damage types are:

**Physical:** Slashing, Piercing, Bludgeoning, Shot.

**Nonphysical:** Burning, Shocking, Toxic, Freezing.

Interpret broadly:

- Burning: flame, heat, steam, acid, caustics, searing supernatural light.
- Shocking: lightning, electricity, nerve disruption, violent supernatural thunder; use Bludgeoning instead for a purely concussive blast.
- Toxic: poison, venom, gas, spores, disease, rot, necrosis, bodily corruption.
- Freezing: cold, frost, ice, flash-freezing, immediate hypothermic injury.
- Fear/psychic pressure: Stress, Panic, morale, or Control—not a damage type.
- Force: use the bodily result—usually Bludgeoning or Piercing.
- Energy drain, petrification, disintegration, drowning, curse, charm, sleep, and transformation remain special effects.

---

# 3. Identity and front matter

## KEEP

Preserve from v2.5:

- title and original visual identity;
- original authorial voice and compressed table-facing style;
- “Gewinn is Hael…” opening;
- “War is Hell; Conflict, Gain, and Profit” identity;
- copyright, CC-BY-SA language, OSE fork statement, cavegirlgames/Mothership acknowledgments, art credits, publisher/contact details;
- classless, level-less, no-HP, wound-, armor-, Stress-, gear-, and expedition-focused identity.

## ADD

State explicitly, once rather than repeatedly:

- full armor stacking is intentional;
- equipment is survival technology, property, status, legal risk, and investment;
- fair fights are not balanced encounters;
- morale, reaction, retreat, light, time, retainers, law, and logistics are core procedures;
- magic is material equipment and remembered exception, not a class subsystem.

## DELETE

Remove repetitive AI-era manifesto paragraphs. Preserve the severe thesis but compress it into the v2.5 voice.

---

# 4. Core dice procedures

## REPLACE ability modifier table

```text
Score 3–11: +0
Score 12–13: +1
Score 14–15: +2
Score 16–17: +3
Score 18–19: +4
Score 20: +5
```

Normal human improvement stops at 20 unless the campaign provides supernatural permission.

## REPLACE core resolution

- Ability check: `1d20 <= relevant ability` when risk, cost, pressure, or uncertainty matters.
- Player attack: `1d20 + relevant ability modifier >= enemy AC`.
- Enemy attack: referee rolls retained Impact; player rolls `1d20 <= PC AC`.
- Opposed check: both sides roll `1d20 + relevant modifier`; higher wins; ties favor defender/status quo.
- Advantage/disadvantage: roll twice, keep better/worse for that procedure.
- Impact advantage/disadvantage: roll the whole pool twice, keep higher/lower total.

## REPLACE Attack Bonus

Attack Bonus is the relevant ability modifier plus situation. There is no Arms Training.

- STR: muscle-powered melee and force-thrown attacks.
- WLL: bows, crossbows, firearms, slings, aimed physical ranged attacks.
- INT: occult implements and spell attacks.
- FTH: only miracles that explicitly require an attack.

## KEEP/UPDATE natural results

Player attack:

- Natural 1: miss. It gains Stress only if it is a failed dangerous roll under the general Stress rule.
- Natural 20: hit; reduce matching DR by 2, minimum zero, or choose a supported disarm, shove, shield pin, armor damage, or positional advantage.

PC AC Save:

- Natural 1: Critical Defense; avoid and take one plausible immediate positional benefit.
- Natural 20: attack lands; reduce matching DR by 2, minimum zero, or apply an appropriate defensive disaster.
- AC caps at 20; a natural 20 always fails.

## KEEP declaration before Impact

Declare target, weapon/Working, mode/type, and broad action before rolling Impact. Do not permit target/type selection after seeing initiative/damage.

---

# 5. Character creation and abilities

## REPLACE ability list

Use STR, INT, FTH, WLL. Default generation is 3d6 in order.

### STR

- muscle-powered melee Attack;
- weapon handling by damage-dice count;
- force, hauling, climbing, swimming, doors, carrying wounded allies;
- Control by force;
- movement/load support.

### INT

- occult-implement Attack and handling;
- spell memory;
- languages, maps, mechanisms, traps, architecture, engineering, accounts, law, medicine, alchemy/chymistry, astrology, natural philosophy, logistics, research;
- spell sources and occult material culture.

### FTH

- relic qualification;
- miracle memory;
- sacred authority, saints, relics, vows, burial, taboo, confession, exorcism, sacred law, legitimacy, turning, spiritual resistance.

### WLL

- bows, crossbows, firearms, slings, aimed physical range;
- base PC AC;
- Shock, Panic, pain, watch, breath, exposure, recovery discipline, retreat composure.

## DELETE OR HOLD

Eureka and Divine Favour are not required by the current combat/magic architecture. Their final status is unresolved. Do not expand or rewrite them automatically. Move them to `TODO` or an optional-rules file until the designer confirms keep/delete.

## KEEP starting packages provisionally

Keep the v5 package structure as a scaffold, but mark all equipment examples `REGENERATE`. Corrected prices make several old examples illegal.

---

# 6. Stress, Relief, Revelry, and advancement

## REPLACE Stress categorization

There is one Stress track. **All Stress that the referee actually awards is eligible to become Growth after Relief.**

Do not track `Growth-eligible Stress` separately.

Prevent farming by withholding Stress:

- no Stress for trivial, safe, staged, repetitive, mock, or consequence-free rolls;
- award Stress only for real danger, wound, loss, horror, pressure, shame, legal consequence, failed retreat, hunger, exposure, betrayal, or similar campaign stakes.

## KEEP core Stress triggers

A failed dangerous player-facing roll under pressure normally gives 1 Stress. Serious consequences may give additional Stress as currently written.

## KEEP Relief/Revelry with wording migration

Replace every phrase `relieved Growth-eligible Stress` with `relieved Stress`.

Safe Relief failure does not increase Stress. Unsafe Relief failure may increase Stress.

## REPLACE advancement

To raise ability score X to X+1:

1. Relieve and convert X Stress through fitting downtime.
2. Spend at least one downtime turn.
3. Provide appropriate fictional support: practice, teacher, study, devotion, recovery, ordeal, office, book, surgeon, armor, field experience, etc.
4. Pay any fictional cost.

No Arms Training progress. No parallel weapon, spell, prayer, reputation, faction, or property point tracks.

Spells, miracles, offices, equipment, property, reputation, and faction assets are obtained through play, source, service, payment, inheritance, law, theft, patronage, vows, or discovery.

---

# 7. Slots, load, movement, and equipment burden

## REPLACE slots

```text
Slots represent weight only.
1 slot is approximately 3 lb.
Use listed rounded values.
```

Do not inflate slots for length, heat, noise, law, visibility, social burden, or awkwardness. Those remain procedures, tags, or fictional consequences.

## KEEP load bands provisionally

Keep the current Light/Laden/Burdened/Heavy/Overloaded thresholds unless a later live test changes them.

## KEEP movement formula provisionally

`40′ + 5′ per STR modifier – 5′ per 5 filled slots`, minimum 5′.

## KEEP pressure outside slots

Heat, mud, water, sleep, stealth, climbing, fitting, maintenance, law, and social reaction remain separate armor-pressure procedures.

---

# 8. Combat sequence

Use this round:

1. Surprise if needed.
2. Declare action, target, mode/type, movement.
3. Roll Impact/initiative.
4. Resolve low to high.
5. Apply wounds, interruption, Stress, Control, morale, reload, smoke, retreat.
6. Tick end-round clocks.

- Attack initiative: retained Impact.
- Non-attack initiative: 1d4.
- Damaging spell/miracle: retained listed Impact.
- Non-damaging spell/miracle: 1d8 per spell level.

Interruption:

- Minor: no automatic interruption.
- Serious: WLL save or lose pending action.
- Grave+: lose pending action.
- Mortal: only Dead Man Walking or explicit effect permits final action.

---

# 9. Damage and wounds

## KEEP calculation

`Wound Value = retained Impact – total matching DR`.

## REPLACE generic-only presentation with discrete tables

Return to v2.5-style damage-type-specific wounds, but **do not restore wound points or HP-like accumulation**.

Required architecture:

1. Wound Value indexes the matching discrete wound table.
2. Every result carries a severity tag: Minor, Serious, Grave, Mortal, or Catastrophic.
3. Shock, Bleeding, interruption, treatment, recovery, mook conversion, and magical healing use the severity tag.
4. Repeated wound fiction follows the current escalation rules; do not add wound points.

### KEEP/ADAPT from v2.5

- Piercing table.
- Slashing table.
- Bludgeoning table.
- Burning table.
- Shocking table.
- Toxic table.

Rename/update terminology and reconcile effects with current abilities and procedures.

### TODO

- Write Shot discrete wounds.
- Write Freezing discrete wounds.
- Assign severity metadata to every result.
- Decide how results above original table ranges map to Catastrophic.

Do not let Codex invent these tables.

## ADD Freezing

Freezing generally produces cold shock, numbness, frostbite, hypothermic confusion, frozen limbs/airways, cardiac collapse, systemic hypothermia, and flash-freezing. It normally does not Bleed.

## KEEP special effects separate

Petrification, energy drain, curses, charm, sleep, drowning, disintegration, and transformation are not damage types.

---

# 10. Physical equipment

## REPLACE all physical weapon and armor tables

Use the CSV files in this bundle as the sole data source:

- `melee_weapons.csv`
- `ranged_weapons.csv`
- `body_armor.csv`
- `helmets.csv`
- `arms_armor.csv`
- `leg_armor.csv`
- `shields.csv`
- `proofing.csv`
- `common_armor_kits.csv`

Do not hand-copy stale v5 values. Generate formatted book tables from CSV.

## REPLACE weapon handling

A character cleanly wields a muscle-powered weapon when its number of damage dice is no greater than `max(1, STR modifier)`.

Above that limit:

- Attack has disadvantage.
- Impact has disadvantage.

Do not add AC Save disadvantage, Stagger checks, stance restrictions, or additional penalties from the obsolete Scale rule.

Crossbows and firearms ignore STR handling.

Bows attack with WLL but use STR for damage-dice handling.

## REPLACE mode rows

Half-swording, mordhau, and unmounted lance are notes/modes under the purchased weapon, not separate inventory rows.

## KEEP physical tables otherwise frozen

The integrated simulations did not justify further changes to corrected mundane weapons, armor, shields, proofing, or firearms.

---

# 11. Armor, shields, and proofing

## KEEP full layer stacking

Wear one body armor, helmet, arms item, legs item, and ready shield. Add all AC and matching DR.

Physical armor normally has 0 Burning, Shocking, Toxic, and Freezing DR.

## REPLACE proofing

```text
Proofed body armor:
+3 Shot DR
+6 lb
+2 slots
+£3
Body armor only
No range clause
Does not stack
```

Delete pistol-proof/musket-proof distinctions and close-range exceptions.

## KEEP shield readiness and sacrifice

- Shield DR applies only when ready/relevant.
- Controlled target loses shield AC/DR and cannot sacrifice.
- Preserve current sacrifice severity reduction, including reduced effect against firearms, lances, siege, huge monsters, and Great weapons.

## REGENERATE common kits

Use `common_armor_kits.csv`. Do not use v5 kit totals.

---

# 12. Firearms

Keep firearms distinct from bows:

- WLL attack.
- Shot damage.
- listed Reload actions.
- noise, smoke, morale, ammunition, wet/fouled conditions, legal pressure.
- cannot reload while Controlled, swimming, climbing, panicking, or otherwise unable to perform the listed actions.
- firearm volley triggers morale as currently written.

Use corrected firearm values from `ranged_weapons.csv`.

Keep +3 proofing. Delete range-dependent proofing.

---

# 13. Control, mobs, Gap Strike, brace, and charge

## KEEP current state engine

Free → Compromised → Controlled.

Control attempt:

- attacker: d20 + STR;
- defender: d20 + STR or WLL;
- tie: defender/status quo;
- first success: Compromised;
- second success: Controlled.

Controlled:

- no shield AC/DR;
- no Shield Sacrifice;
- cannot brace or reload;
- cannot use two-handed weapon effectively;
- armor remains unless helpless;
- armor DR remains except against Gap Strike or explicit effect.

## KEEP Mob Control

Three or more attackers roll d20 + active mobbers, maximum +6. Extra bodies replace losses, block escape, hold limbs/shields, or support the Gap Strike.

## KEEP Gap Strike

- Controlled target.
- Gap-capable method.
- Attack with advantage.
- 1d6+2 Piercing Impact.
- Ignore armor and shield DR.
- Any wound minimum Serious.

## UPDATE brace wording

Brace acts against the **charge event**, not automatically the rider’s best body armor. A successful braced wound, shield sacrifice, Compromised result, injured mount, broken lane, or disrupted formation stops/reduces the charge.

Keep mounted-lance requirements and 4d6 Piercing charge Impact.

---

# 14. Magic: memory, sources, resolution, and recharge

This section replaces every v2.5/v5/v6 magic engine while preserving compatibility with classic OSR spell lists.

## 14.1 Spell and miracle memory

```text
Spell-level memory capacity = INT modifier.
Miracle-level memory capacity = FTH modifier.
+0 capacity = 0.
```

A level-N Working occupies N memory.

Examples:

- INT +3: three level-1 spells, one level-1 plus one level-2, or one level-3.
- FTH +5: five level-1 miracles, level 2 + level 3, or one level-5.

Duplicate remembered instances are permitted.

High ability grants capacity, not knowledge. Every Working requires an actual source, teacher, office, relic, shrine, pact, diagram, specimen, liturgy, or equivalent permission.

## 14.2 Expenditure and restoration

- A remembered instance is expended when used.
- A spent instance is unavailable until restored.
- Safe access to the required source restores spent instances and permits rearranging memory.
- Ordinary sleep without the source does not restore or rearrange memory.

## 14.3 Resolution

There is no general casting roll.

Each ordinary Working uses exactly one of:

1. INT or FTH attack versus AC;
2. one target Defense;
3. no roll when unopposed.

Do not require both an attack and target Defense for one ordinary effect.

When an NPC uses magic against a PC, use the player’s listed Defense; do not add an NPC casting roll.

Named targets receive a Defense against immediate encounter-ending effects. Bosses require a written vulnerability/setup before control, banishment, transformation, destruction, or defining-power removal can fully work.

## 14.4 Initiative

- Damaging Working: roll listed Impact for initiative and retain it as damage.
- Non-damaging Working: 1d8 per spell level.

## 14.5 Classic spell conversion

- Use original classic spell level as memory cost.
- Remove class and caster-level prerequisites.
- If an effect requires caster-level scaling, use relevant INT/FTH modifier, minimum 1, unless the converted entry supplies fixed values.
- Convert damage to one of the eight types.
- Convert saves to one Defense.
- Convert fear/turning to morale/Panic where appropriate.
- Convert restraint to Compromised/Controlled.
- Convert healing to discrete wound/severity effects.
- Permanent, regional, resurrection, or campaign-scale effects require a rite/project, not ordinary field memory.

## 14.6 Emergency recharge

A character may restore one **spent** remembered instance by taking a full action.

- Combat initiative: 1d4.
- Wound occurs when the action resolves.
- Recharge gives no automatic Stress.

| Spell level | Recharge wound |
|---:|---|
| 1 | Minor |
| 2 | Serious |
| 3 | Grave |
| 4 | Mortal |
| 5 | Catastrophic |

The Working fixes the recharge wound’s damage type. A damaging Working normally uses its own type. A non-damaging Working must list one.

Recharge wound:

- ignores armor and DR;
- follows normal Shock, Bleeding, escalation, treatment, infection, and recovery;
- cannot be reduced, removed, transferred, or downgraded by magic;
- may be stabilized and treated normally;
- repeated recharge of the same Working uses the same wound fiction and therefore normal escalation.

Do not split INT recharge into nonphysical and FTH recharge into physical. Do not require a new damage type each time.

## 14.7 Healing

No HP restoration.

Every healing Working must say exactly which wound/severity it removes, downgrades, stabilizes, or preserves.

Magic cannot reduce recharge wounds.

Returning the dead is never ordinary field magic.

## 14.8 Memory-expanding items

The designer has established that expensive items may raise memory capacity, but no standard ladder is finalized.

`TODO`: preserve a hook for specific books, reliquaries, offices, or instruments to hold additional spell levels. Do not invent generic `+1 memory` shop items or values.

---

# 15. Occult implements

Use `occult_implements.csv` as the sole standard purchasable inventory.

## Rules

- Each implement has one fixed type: Burning, Shocking, Toxic, or Freezing.
- Attack with INT.
- NdS is initiative and retained Impact.
- It may attack in melee or at listed range.
- Melee attack causes no reload.
- After ranged use, Reload N.
- While ranged mode is unloaded, melee remains available.
- Clean if N <= max(1, INT modifier); otherwise Attack and Impact have disadvantage.
- 1-die implement is one-handed; 2+ dice is two-handed.
- Standard range is 30′ × N.
- Standard implement weight is 2 × N × S lb.
- Standard cost is N × S² ÷ 4 pounds, rounded as tabled.
- No ammunition, charges, mana, activation roll, or Drain roll.

## Standard purchasable ratings

- 1d4
- 1d6
- 2d4
- 1d8
- 2d6
- 3d4

Anything d10, d12, 2d8, 3d6, 4d4, 5d4, or stronger is Unique/institutional/campaign treasure, not standard merchandise.

## Naming/editorial rule

Do not name player-facing inventory entries `1d6 implement`. Give each object a historically grounded form and provenance; keep rating/type in columns or parentheses.

Examples of forms: virge, rod, sceptre, mirror, bell, censer, staff, crozier, processional standard, portable shrine apparatus.

---

# 16. Sacred relics

Use `sacred_relics.csv` as the sole standard purchasable inventory.

## Rules

- Each relic protects one fixed type: Burning, Shocking, Toxic, or Freezing.
- Qualified if N <= max(1, FTH modifier).
- An unqualified bearer receives no worn benefit and cannot bestow it.
- While worn, flat matching DR = S.
- Relic DR stacks normally with all matching worn/bestowed DR.
- No activation or reactive per-hit roll.
- As an action, a qualified bearer may bestow protection on another creature.
- Roll NdS once at bestowal; record result as flat matching DR until recipient next reaches safe rest.
- While bestowed, relic does not protect wearer.
- Weight = N × S lb.
- Cost = N × S² ÷ 8 pounds, rounded as tabled.

## Standard purchasable ratings

- 1d4
- 1d6
- 2d4
- 1d8
- 2d6
- 3d4

Stronger relics are Unique/institutional/campaign treasure.

## Naming/editorial rule

Do not present `1d6 relic` as an in-world name. Use historical forms such as badge, pectoral, reliquary cross, amulet case, girdle, scapular set, vestment, talismanic shirt, arm reliquary, portable shrine. Keep rating/type in a mechanical column.

---

# 17. Exploration procedures

ADD/KEEP the v5 full procedures, rewritten into v2.5 density:

- 10-minute dungeon turn;
- wandering check 1-in-6 every 2 turns by default;
- immediate checks after gunfire, screaming, heavy breaking, major magic, or foolish noise;
- light durations and visible position;
- required rest after 6 turns;
- doors, listening, searching, traps, surprise;
- reaction and morale;
- pursuit/evasion;
- wilderness watches, travel, food/water, weather;
- one-week downtime turn.

Do not let utility magic erase these procedures without spending remembered magic, time, source access, or creating consequences.

---

# 18. Recovery, surgery, disease, and troupe play

Keep the v5 procedural additions, adapted to discrete wounds:

- Serious+ Shock tests;
- Bleeding and Bleeding Out by damage/wound result;
- Dead Man Walking;
- treatment times;
- surgery with INT/WLL/FTH support where appropriate;
- infection checks;
- recovery times by severity;
- permanent injuries only for Catastrophic survival, failed surgery, accepted maiming, curse, or explicit effect;
- troupe/replacement play while PCs recover.

Delete any healing rule that treats wounds as HP or disease points.

Recharge wounds obey ordinary recovery but cannot be magically reduced.

---

# 19. Mooks, morale, retainers, and retreat

## KEEP mook states

- <=0 Fine
- 1–3 Shaken
- 4–7 Out
- 8+ Dead

Use actual equipment AC/DR. Mooks do not track Stress.

## KEEP mandatory morale

Trigger on first Out, leader fall, visible Grave+, firearm volley hit, overwhelming magic/monster force, broken formation, closed escape, or obvious suicidal order.

## ADD/KEEP retainers

Retainers carry light, ammunition, bodies, treasure; screen reloaders; support Control; become replacement PCs. Keep wage/hiring/loyalty procedures, but add the missing exact Loyalty roll before publication.

## KEEP retreat

Declare retreat, determine pursuit, compare movement/load/route/terrain/wounds, permit dropping gear/treasure, resolve consequences. Heavy armor and carrying wounded allies must matter through this procedure, not reduced DR.

---

# 20. Economy, law, property, and factions

KEEP v2.5 £/s/d economy and ordinary goods not replaced by CSVs.

ADD/KEEP:

- corrected gear prices;
- wages and services;
- maintenance;
- legal carry/firearm/armor pressure;
- bribes, licenses, fines, taxes, ransom;
- property and upkeep;
- faction turns;
- rich-PC event pressure;
- treasure conversion default of 1 old-module gp = 1s, subject to campaign adjustment;
- books, relics, grimoires, offices, and magical implements as property and legal/faction claims.

Do not turn rarity into a numerical bonus. Availability controls access, not combat math.

---

# 21. Monsters and module conversion

KEEP/UPDATE:

- OSE AAC → GEWINN enemy AC = AAC – 10.
- Descending AC → 9 – DAC.
- Humanoids use actual gear when available.
- Referee rolls monster Impact; PCs make AC Saves.
- HD determines mook/named/boss role, not HP.
- Large/huge monsters may reduce Wound Value by 2/4 where currently specified.
- Named targets receive one Defense against encounter-ending magic.
- Bosses require vulnerabilities/objectives/setups.
- Mook fear/turning uses morale.
- Assign natural armor across all eight damage types only where the monster fiction supports it.

Update all old Cut/Point/Crush references and add Freezing where relevant.

---

# 22. Character sheet and referee screen migration

## DELETE fields

- Scale.
- Arms Training/Mastery.
- Growth-eligible Stress separate field.
- Cut/Point/Crush.
- old proofing categories.
- casting-roll/backfire/Disturbance/Strain fields.

## ADD fields

- Slashing, Piercing, Bludgeoning, Shot, Burning, Shocking, Toxic, Freezing DR.
- Implement: rating, type, range, ranged Reload, loaded/unloaded state.
- Relic: rating, type, worn DR, bestowed target/result/duration.
- Spell memory total and used levels.
- Miracle memory total and used levels.
- source for each Working.
- recharge wound and its type.
- current exact discrete wound result plus severity.
- proofed body armor.

## Referee screen must include

- modifier table;
- attack/AC Save/natural results;
- Impact initiative;
- eight damage types;
- discrete wound lookup references;
- Control/Mob/Gap;
- shield readiness/sacrifice;
- proofing;
- implement and relic formulas;
- spell memory/recharge;
- mook states/morale;
- light/dungeon turns;
- firearms/reload/smoke;
- pursuit/evasion;
- monster conversion.

---

# 23. Superseded experiments: never merge

The following appeared in intermediate drafts but are not current:

- generic v5 Rank 1–3 casting subsystem;
- 2 × modifier spell/prayer preparation;
- success remains prepared until failure;
- always-roll casting;
- casting failure that produces the effect;
- margin-of-failure Stress forcing;
- Circle/Load/Power/Push;
- source/relic Strain tracks;
- one-use reactive relic dice;
- non-stacking relics;
- mundane armor receiving generic exotic DR;
- Nd4-only implements as a permanent restriction;
- separate melee and ranged implement inventories;
- ranged implements unable to melee while unloaded;
- automatic recharge Stress;
- non-Growth-eligible Stress;
- INT recharge always nonphysical / FTH recharge always physical;
- recharge wound forced to use a new damage type;
- arbitrary attunement, relic slots, mana, charges, or proficiency bonuses.

---

# 24. Open decisions: Codex must stop and leave TODO

1. Final Shot wound table.
2. Final Freezing wound table.
3. Severity tags and exact migration for the six v2.5 wound tables.
4. Final curated spell/miracle catalogue and individual conversions.
5. Exact memory-expanding items.
6. Eureka and Divine Favour final keep/delete decision.
7. Exact Loyalty roll.
8. Recalculated starting loadouts and whether all v5 packages remain.
9. Final character sheet and referee-screen layout.
10. Whether the optional expert stances survive; they are not part of the settled core.

Codex must not invent answers to these.

---

# 25. Implementation order and commits

Use one commit per line:

1. `chore: import untouched v2.5 baseline and archive later drafts`
2. `refactor: split rules into source modules without changing text`
3. `rules: migrate terminology and remove Scale Arms Training and old proofing`
4. `data: install corrected physical equipment tables`
5. `rules: install current attacks AC saves initiative and handling`
6. `rules: install Control mob Gap brace and charge`
7. `rules: collapse Stress to one Growth-capable track`
8. `rules: install eight damage types and discrete-wound scaffold`
9. `rules: install spell memory sources expenditure and recharge`
10. `data: install occult implement and sacred relic inventories`
11. `rules: install exploration morale retainers retreat and recovery procedures`
12. `rules: update monsters and classic-module conversion`
13. `docs: regenerate examples kits references glossary sheet and screen`
14. `test: add terminology and table validation`

Do not combine these into a single unreviewable rewrite.

---

# 26. Acceptance checks

## Must return zero unintended matches

```bash
rg -n "Arms Training|Mastery:|Weapon Scale|Draw Scale|Cut DR|Point DR|Crush DR|Pistol-proof|Musket-proof|Growth-eligible Stress|Arcane Circle|Holy Circle|Prepared Load|Source Strain|Relic Strain|Transcendent Exertion|Force Through|Greater Petition" rules data
```

Allowed matches are only in archive/changelog text.

## Must find current terms

```bash
rg -n "Slashing|Piercing|Bludgeoning|Shot|Burning|Shocking|Toxic|Freezing" rules data
rg -n "Reload N|recharge wound|Proofed|weight only" rules
```

## Validate table relationships

- all armor rows have eight DR columns;
- physical armor exotic DR defaults to zero;
- all implements exist in four types;
- all relics exist in four types;
- implement Reload equals N;
- standard implement range equals 30′ × N;
- implement weight equals 2 × N × S lb;
- relic weight equals N × S lb;
- worn relic DR equals S;
- common-kit totals equal component sums;
- proofing changes only Shot DR, weight, slots, and cost;
- no mode row is separately purchasable;
- no character-sheet field references deleted mechanics.

---

# 27. Suggested Codex instruction

```text
Work in branch migration/v2.5-current.
Read GEWINN_v2_5_to_current_CODEX_CHANGELOG.md and
GEWINN_v2_5_to_current_CHANGE_MANIFEST.yaml completely before editing.

Treat data/*.csv as canonical values. Generate tables from them; do not hand-copy values.
Preserve v2.5 voice, front matter, attribution, and all unaffected content.
Use v5 only as a procedural scaffold.
Delete all mechanics listed under Superseded Experiments.
Do not resolve any TODO without asking.
Make one subsystem-sized commit at a time in the prescribed order.
After every commit, run the acceptance grep and table validators.
Do not edit archive/.
```

---

# 28. Final migration summary

The current game preserves v2.5’s identity—classless, level-less, no HP, damage-as-initiative, detailed wounds, Stress, gear, money, and severe OSR play—while replacing its weakest or incomplete systems with:

- player attacks plus player-facing defense;
- eight typed damage families;
- weight-only slots;
- corrected historical arms and armor;
- full armor stacking with external pressure;
- formal Control/Mob/Gap anti-armor play;
- complete firearms, proofing, morale, retreat, and recovery procedures;
- INT occult implements that behave as weapons;
- FTH relics that behave as supernatural armor;
- remembered classic spells/miracles paid for by limited memory and desperate recharge wounds;
- full dungeon, wilderness, retainer, property, faction, and module-conversion support.

The migration is mechanically substantial but conceptually narrow: **everything supernatural now uses the same equipment, initiative, DR, wound, source, weight, and campaign-pressure language as the rest of GEWINN.**
