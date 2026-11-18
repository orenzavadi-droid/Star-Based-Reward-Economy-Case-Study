# Star-Based Reward Tier Balancing
## Independent Game Economy Case Study: *Solitaire Grand Harvest*

**Genre:** Casual free-to-play (F2P), **TriPeaks Solitaire**; level-based puzzle/saga progression, farm-building meta, and casino-inspired credit economy.

> **INDEPENDENT RESEARCH — NOT A PLAYTIKA / SUPERTREAT PROJECT.** No proprietary game data, current internal configuration, source code, brand assets, or real-player telemetry was accessed. All numeric model inputs and outputs are illustrative. The *historical* published details described below are not asserted to be the game's current 2026 settings.

### The business question (one sentence)

**Can we make a high-tier star-based reward crate feel more attainable, without releasing too much reward value into the game economy?**

Why this matters: a target that feels impossible may discourage extra play; a target that is too easy can inflate the reward economy. The right balance depends on player segment, progression stage, and the *relative* reward value compared with the replay cost. This is a business **hypothesis**, not a proven claim about SGH.

### Verified public anchor

- The publisher's current listing calls the game **TriPeaks Solitaire**, confirms Credits/Gems/Boosters, optional IAP, and explicitly advertises **upgradable reward crates** [S1].
- The game's official guide says completed levels award **1–3 stars** and replays can improve a prior non-perfect result [S2].
- The publisher's 2025 guide names **Crop Master** as a recurring crate and describes **25-level** intervals [S3].
- Naavik's **April 6, 2023** independent deconstruction details the *historical* star-gated Crop Master crate, replaying levels to improve stars, historical **8→48 star** thresholds and **1→10** prize selections [S4]. Liquid & Grit also documented the historical mechanic in **December 2019** [S5].

**Crucial reconciliation:** 2025's reference to 25 levels and 2023's 48-star reference come from different dates. They do **not** jointly establish one current configuration. There is no publicly verified 2026 tier table, reward probability table, player-data distribution, IAP uplift or cost scaling for this crate. The model is expressly an **independent counterfactual exercise**.

### What's included

| File | Why it matters |
|---|---|
| `Crop_Master_Economy_Model.xlsx` | Main deliverable: editable hypothetical thresholds, segments, formula-driven economics, KPI/guardrail comparison, event spec and sources |
| `CASE_STUDY_ONE_PAGER.pdf` | Designed to be shared / presented during a 30-minute professional feedback call |
| `STUDY_GUIDE_HE.html` | Attractive offline study guide in Hebrew: pitch, mechanics, economy math, quiz, decision logic |
| `RESEARCH_AND_EVIDENCE.md` | Deep research on genre, gameplay loops, sources & sinks, progression, monetization, and fact-vs-hypothesis ledger |
| `EXPERIMENT_DESIGN.md` | Practical controlled test design, telemetry, segment rules, metrics and invalidation conditions |
| `LEGAL_AND_ATTRIBUTION.md` | IP analysis and use boundaries; not legal advice |
| `RED_TEAM_AND_LIMITATIONS.md` | Honest challenges to assumptions, validity and interpretability |
| `INTERVIEW_TALK_TRACK.md` | 45-second / 2-minute pitch and tough interviewer Q&A |
| `FIELD_NOTES.md` | Tonight's observation guide; no screenshots or spending required |
| `tests/verify_model.py` | Offline independent arithmetic checks for model scenario outputs |
| `tests/sensitivity_analysis.py` | Stress-tests tier cutoffs, shadow prize valuation and effects across segments |
| `SENSITIVITY_AND_ROBUSTNESS.md` | Explains why the observed toy recommendation is assumption-dependent |
| `AUDIT_REPORT.md` | Independent red-team audit and remaining limitations |

### Illustrated result — **NOT actual SGH performance**

The workbook's self-declared, invented reference and variants yield:

| Model output | Illustrative reference | Focused top-tier adjustment | Broad generosity |
|---|---:|---:|---:|
| Estimated high-tier crate reach | **6.2%** | **11.3%** | **12.4%** |
| Modeled reward budget (credit-equivalent units / completed crop) | 791.1 | 828.6 | 872.8 |
| Modeled replay credit spend / completed crop | 241.0 | 249.4 | 216.0 |
| Modeled net credit-equivalent emission / completed crop | 550.1 | 579.2 | 656.8 |
| Modeled change in net issuance | — | **+5.3%** | **+19.4%** |
| Heuristic guardrails (net +10% max; reward budget +8% max) | Reference | **Pass** | **Fail** |

**Model decision:** The focused adjustment is a **candidate to evaluate** in a controlled A/B under the *invented* assumptions, not a live rollout. The broader change fails the modeled economy-issuance guardrail. **No impact on retention, payer conversion, revenue, crop-completion or actual player satisfaction was modeled or established.** All modeled rates and budget figures are *conditional on a crop-completer*, not per entrant, install or DAU. A real experiment must randomize **before** crop completion and report an entrant-level intention-to-treat (ITT) result, or deliberately run a narrower post-completion replay test.

### How to use it in 5 minutes

1. Open `CASE_STUDY_ONE_PAGER.pdf` for the argument.
2. Open the Excel workbook → `START`, then `INPUTS`. Blue fields are hypothetical and editable.
3. Inspect `DECISION`: compare high-tier attainment and modeled credit-equivalent net issuance across three configurations.
4. Change `INPUTS!E20` (focused top-tier threshold) from `46` to `47` or `44`. Examine whether the recommendation is sensitive to one guessed number.
5. Read `EVIDENCE` and `RESEARCH_AND_EVIDENCE.md` before claiming anything about the game.

### What I would ask the SGH economist in the Zoom

- Is a **star-gated reward-crate upgrade** still live, and what is the actual event/claim timing and player choice flow?
- How do you evaluate reward **attractiveness vs credit-equivalent expected payout** for crate options, including non-currency items?
- Which pre-treatment segments matter most in practice: crop level, historical replay depth, purchase behavior, or another cut?
- What is the biggest omitted cost/risk in this toy proxy (passive farm income, stake scaling, opportunity cost, or instrumentation)?
- Is the primary goal top-tier attainment, *incremental sessions*, long-term retention, or monetization? Does it make sense to randomize at crop entry rather than completion? What would make this a bad intervention?

### Links and provenance (accessed 18 Nov 2026)

- [S1] Google Play, Supertreat / Playtika official listing: https://play.google.com/store/apps/details?id=net.supertreat.solitaire
- [S2] Official how-to: https://www.solitairegrandharvest.com/how-to-play-solitaire-grand-harvest/
- [S3] Official 2025 Credits guide: https://www.solitairegrandharvest.com/free-credits/
- [S4] Naavik, Apr 2023: https://naavik.co/deep-dives/solitaire-grand-harvest-deconstruction/
- [S5] Liquid & Grit, Dec 2019: https://www.liquidandgrit.com/wp-content/uploads/2019/12/Puzzle-Report-December-2019.pdf
- [S6] Playtika Terms of Service (IP): https://www.playtika.com/terms-service/

**Attribution:** Solitaire Grand Harvest is a game of Supertreat, a Playtika studio. All marks belong to their owners. The workbook, prose and analytical figures are independently authored. No affiliation, endorsement or access to internal studio data is implied.

### What an interviewer should challenge

- **Segment heterogeneity:** In the illustrative focused variant, top-tier reach stays **0% for Casual**, increases **3.75% → 11.25% for Regular**, and **32.33% → 49.17% for Engaged**. An average KPI can hide that most benefit accrues to stronger players; a different goal may call for a different intervention.
- **Timing/denominator:** the workbook is conditional on *completers*. The proposed ITT A/B must start at *crop entry*. These outcomes are not interchangeable.
- **Accounting:** `reward EV − replay spend` is a **hybrid shadow-value proxy**, not actual coin issuance. Item-level reward budgets and a complete virtual-currency ledger must be evaluated separately on live data.
- **Model sensitivity:** see `SENSITIVITY_AND_ROBUSTNESS.md` and `tests/sensitivity_analysis.py`. A more aggressive 44-star high tier fails the toy 10% net-emission guardrail, though 46 stars passes. The specific threshold recommendation is sensitive to assumptions; never present it as an optimal live setting.

### Feasibility of the illustrative star-score range

To avoid impossible star totals, the score proxy assumes a purely **fictional 20-level crop**: with 1–3 stars per level, its feasible total is 20–60. The illustrative Casual/Regular/Engaged initial scores and post-replay score ranges all fit within these bounds. **20 levels is NOT claimed to be an actual current SGH crop length**; the separately cited official 2025 page refers to 25 levels, and we do not merge that with historical 2023 tier settings. A real analysis must replace this with the specific live crop length and empirical discrete star distribution. The model's uniform approximations are continuous for algebraic simplicity, not literal star outcomes.

### Red-Team report and replication

See [`AUDIT_REPORT.md`](AUDIT_REPORT.md) and [`SENSITIVITY_AND_ROBUSTNESS.md`](SENSITIVITY_AND_ROBUSTNESS.md). Run `python tests/verify_model.py` and `python tests/sensitivity_analysis.py` to verify assumptions, arithmetic and threshold/valuation sensitivity. An Excel input validation column flags unordered thresholds, reward picks, invalid segment shares and non-positive costs. These tests cannot make the invented premises empirically true.
