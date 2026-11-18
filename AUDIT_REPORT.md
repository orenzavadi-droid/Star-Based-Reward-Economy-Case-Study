# Red Team audit — Star-Based Reward Tier Balancing

**Review date: 18 November 2026. Status: prepared for professional feedback and GitHub publication with caveats; NOT a production-game recommendation or publisher-approved use.**

## Sources and ground-truth tiers

| Claim | Evidence | Audit judgment |
|---|---|---|
| Game is free-to-play TriPeaks Solitaire with farm progression and optional IAP | Official Google Play listing, last updated 13 Nov 2026 | **Supported as current store description** |
| 1–3 stars awarded for completed levels; replay can improve star grade | Official *How to Play* site | **Supported as published mechanic**, not a guarantee of feature availability for every current account |
| Reward crates are upgradeable | Official Google Play listing | **Supported** |
| Crop Master named in recurring rewards / 25-level interval | Official *Free Credits* guide labeled 2025 | **Supported as dated publisher description**, not proven 2026 config |
| 8→48 star tiers, 1→10 choices / extra replay | Naavik deconstruction dated April 2023 | **Supported historically only**; do not blend 2023 values with 2025 cadence |
| 2019 Crop Master mechanic | Liquid & Grit Puzzle Report Dec 2019, indexed feature table | **Corroborating historical source**; full PDF screenshot endpoint returned HTTP 403 in this audit, but indexed excerpt contains the mechanic; secondary to Naavik and official sources |
| Real 2026 thresholds, odds, segment makeup, user behavior and currency values | No internal access | **Unknown — no claim made** |

Primary URLs: [official store](https://play.google.com/store/apps/details?id=net.supertreat.solitaire); [official instructions](https://www.solitairegrandharvest.com/how-to-play-solitaire-grand-harvest/); [official 2025 credits guide](https://www.solitairegrandharvest.com/free-credits/); [2023 independent deconstruction](https://naavik.co/deep-dives/solitaire-grand-harvest-deconstruction/); [2019 industry report](https://www.liquidandgrit.com/wp-content/uploads/2019/12/Puzzle-Report-December-2019.pdf); [publisher terms](https://www.playtika.com/terms-service/).

## 5 substantive audit corrections

1. **Invalid experimental denominator fixed:** workbook models only crop completers, but an end-to-end A/B must randomize at **crop entry** and report ITT outcomes per randomized entrant. A post-completion A/B may be chosen for a narrower replay/claim question. Updated `EXPERIMENT_DESIGN.md`, `RESEARCH_AND_EVIDENCE.md`, `TELEMETRY` worksheet, HTML guide and pitch material.
2. **Averages mask segments:** Focused model effect is 0pp Casual, +7.5pp Regular, +16.84pp Engaged. Highlighted this so a presenter asks whose experience is actually being improved.
3. **Shadow-value caveat sharpened:** prize EV per pick is not automatically fungible with in-game Credits. The hybrid 'net' column is explicitly a **shadow proxy**, not a reconciled currency ledger. True sources/sinks and item-level grant costs require separate operational accounting.
4. **Input integrity:** Workbook now flags invalid tier ordering, prize-pick ordering, segment weights and invalid key values; `DECISION` no longer silently approves invalid cases. Threshold edit 46→47 recomputes; invalid 35 displays `INVALID INPUTS`.
5. **Star-score feasibility clarified:** 1–3 stars × **fictional 20-level crop** yields 20–60 possible stars. All toy distributions, including post-replay, lie within those bounds. This assumption is NOT the official 2025 25-level description and is not a statement about today's actual crop length.

## Tests performed

- `python tests/verify_model.py`: passes independent deterministic reconciliation of the three scenario summary numbers.
- `python tests/sensitivity_analysis.py`: passes stress tests at top-tier thresholds 43–48 and hypothetical prize values 100–260. At 44 toy stars, the proxy increases +11.3% and breaches the invented +10% cap; 46 passes with +5.29%.
- Excel formula recomputation on an imported workbook: threshold 46→47 adjusts high-tier probability to 8.46%; invalid 35 produces `INVALID INPUTS`. Export/re-import values and validation verified.
- Spreadsheet formula-error scan: no `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?` or `#N/A` in default configuration.
- HTML: six tabs, answer selection, flip-card mechanics and page errors checked with Chromium/Playwright. Offline, no CDN required.
- PDF one-pager: rendered and visually inspected on a single A4 page, re-rendered after the corrections.
- ZIP: entries tested for corruption after packaging.

## Limitations that remain by design

- No live in-game account walkthrough/current game build check by the author yet; **current Crop Master flow must be verified** during gameplay and with the invited expert.
- The current reward crate price table, frequency, item probabilities, player-segment shares, per-player outcomes and real-monetary monetization effects are unavailable. The numerical 'reference' is not a real current baseline.
- Continuous uniform star proxy, causal replay-response formula and fixed 20-level toy length are teaching assumptions, not empirical calibration. Tier rewards have assumed picks and costs.
- Model does **not** simulate crop completion or downstream retention/revenue. It cannot predict an entrant-level live experiment result; a passing toy guardrail does not warrant rollout.
- Named-game use: no written permission / legal clearance; game service terms (June 2026) include personal-use, IP and AI/data-use restrictions. Public commentary with independently authored content may be a lower-risk approach, but it **does not establish legal permission or Terms compliance**. No original game art, sound, code or screenshots are packaged. See `LEGAL_AND_ATTRIBUTION.md`.

## Reviewer verdict

**Suitable for expert discussion and interview as an independent, well-bounded analytical case, with the caveats above prominently disclosed.** It would be inappropriate to pitch it as an operational improvement to Playtika's actual current game or as a measured uplift. '100% perfection' cannot be certified without current gameplay and internal data, and legal clearance cannot be certified without authorization or qualified legal assessment.
