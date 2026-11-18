# Research dossier: Solitaire Grand Harvest through a Game Economist's lens

**Research date:** 18 November 2026. **Scope:** public evidence, not internal analytics or hands-on inspection of the exact current account build. Any specific mechanic may be reconfigured by crop, player, market, experiment or game version.

## 1. Genre and business model

- **Officially verified:** a free-to-play casual **TriPeaks Solitaire** card game by Supertreat (a Playtika studio), with a farm-building / decoration meta and optional in-app purchases. The Google Play listing was updated **13 November 2026** [S1]. Calling it purely 'hyper-casual' would misrepresent its progression and monetization depth.
- **Historically interpreted by Naavik, 2023:** a hybrid of level-based puzzle progression and a 'casino-inspired' credits/bet-scaling economy [S4]. This describes economic mechanics; it does **not** mean real-money wagering, and we must not confuse credits with redeemable money.
- **Official game goal:** remove cards of adjacent ranks from the TriPeaks board [S2, S1]. Level performance grants 1–3 stars [S2].

## 2. Map of relevant mechanics (facts vs hypotheses)

| System | Grounded observation | Economic significance (hypothesis / inference) | Evidence / temporal caveat |
|---|---|---|---|
| Core card levels | Complete TriPeaks boards with 1–3 stars | Wins, loss streaks and perceived near-misses shape replay demand | [S2] official; exact failure rates not public |
| Credits | Player earns credits; credits are used to play levels | Credit faucet and sink; balance should be normalized to crop/stage economy | [S2, S3]; historic cost scaling [S4] |
| Farming harvest | Farm harvest and bonuses generate Credits, described by official site | Return motive and replenishment; reduces scarcity over time | [S3] official; exact amounts not public |
| Star-based reward crates | Crates can be upgraded [S1]; named Crop Master crate noted in 2025 official guide [S3] | Intermediate goal / escalating reward expectation | Historical star thresholds and picks are **not** current verified |
| Replaying older levels | Official guide permits replay for a better star rating [S2] | Effort-vs-reward decision; attempt cost and engagement opportunity cost | [S2]; replay reason may be multi-feature |
| Crate upgrade | 2023 Naavik describes 8–48 stars and 1–10 picks (historically) [S4] | Creates threshold / goal-gradient tension and credit-exchange tradeoff | Do not present these as 2026 settings |
| In-level continuation | + Cards, Wilds, boosts appear in official guide [S2] | Boosters can lower frustration but may add sink or undermine challenge | Current exact prices not public |
| Betting / level stake multiplier | Historically Naavik describes x1–x8 bets and scaled credit payouts [S4] | Players at same playtime may have different credit velocity | Historical claim; do not apply 2023 x8 to current model |
| Meta progression | Grand Album, seasonal areas, MyTrail, tournaments and other extras described officially [S2] | Competing motivational loops; changing reward crate could cannibalize other modes | Event availability changes over time |
| In-app offers | Official stores confirm optional virtual item IAP [S1] | Financial KPI monitor; any effect on IAP must be measured separately | **No player-level IAP, ARPDAU, ARPPU data publicly available** |

## 3. The system we chose: star-gated crate tiers

**Why this is a strong candidate:** it links one visible mechanic (the star/reward relationship) to three concrete economic questions: (1) How many players can access the best reward? (2) How much effort / how many Credits are spent to reach it? (3) How large is the payout obligation? A player-psychology lens adds *perceived attainability* and *goal-gradient motivation*.

**Documented historical details:** Liquid & Grit (Dec 2019) describes completing levels to earn stars that upgrade crates and add reward picks [S5]. Naavik (Apr 2023) describes Crop Master crates after a level pack, replays for extra stars, and the historical 8-to-48 star / 1-to-10 pick progression [S4]. Current Google Play says upgrade reward crates for larger prizes [S1]; the official 2025 credit guide identifies the Crop Master crate recurring after 25 levels [S3].

**Important mismatch:** a historical 48-star high-tier from 2023 plus 25-level interval from a 2025 guide is not a verified current star structure. Version, level-pack design, thresholds and event gating may have changed. In the workbook, **'Reference' is an invented comparison scenario**, not a reverse-engineered current live baseline.

## 4. Economics: what we can calculate vs what we cannot

### Model outputs that can be calculated under declared assumptions
- `High-tier attainability`: synthetic probability of reaching the top star requirement among crop-completers.
- `Expected reward picks`: weighted by assumed tier thresholds and reward-pick counts.
- `Reward budget`: expected picks × assumed expected credit-equivalent value per pick.
- `Replay spend`: modeled chance of replay × assumed replay attempts × assumed credit cost per attempt.
- `Net emission proxy`: reward budget − replay spend. **This is a hybrid shadow-value proxy**, not a reconciled in-game Credit ledger; crate picks can include boosters/items that cannot be treated as actual Credits. In live reporting, separate the true currency ledger from item reward cost / shadow values.

### Cannot be claimed with this model
- Real active player shares; real current reward tiers; actual card/reward distribution.
- Revenue/ARPDAU/ARPPU, retention improvements, payer conversion, price elasticity, customer satisfaction or causal behavior change.
- That 2023 bet multipliers, 2025 25-level cadence, and 2026 crate design coexist unchanged.
- That a single normalized cost holds across crop levels or payment segments.

## 5. Player psychology: hypotheses, not diagnosis

1. **Goal gradient:** a reachable next milestone might increase willingness to replay; our model builds this as an assumed replay propensity response. No effect is *demonstrated* by public data.
2. **Expectancy-value:** replay decisions depend on expected value of next prize vs time and credit cost, not just on stars.
3. **Loss aversion / near-miss:** historical Naavik analysis connects near-completion to willingness to spend on continuation [S4]; do not assume uniform effects across segments.
4. **Segmentation:** a Casual player may prioritize relaxed quick play, whereas an Engaged player may invest more attempts for mastery; the segment shares and propensities in Excel are **examples only**.
5. **Autonomy and fairness:** removing a challenge entirely can devalue achievement; increasing it can frustrate low-resource players. Measure complaints and progress, not only purchase revenue.

## 6. Instrumentation needed for real validation

Prefer randomizing **at crop entry, before the player can see variant-dependent thresholds**, to estimate entrant-level effects without conditioning on treatment-affected completion. A deliberately narrower post-completion A/B is possible if the feature truly only appears after completion, but that estimates effects **among crop completers** rather than overall progression. Log persistent user-level assignment, use an intention-to-treat entrant denominator for the main trial, and distinguish conditional (completer) descriptive metrics. Track stars, reward tiers, completion, replay attempts, credits sources/sinks, item reward EV, IAP RPU, D7 return and complaints. Use pre-treatment segments only. See `EXPERIMENT_DESIGN.md`.

## 7. Open questions for the SGH expert

- Is Crop Master still called that? At what point are players allowed to replay / claim / see thresholds?
- Which currencies and expected-value accounting are used to evaluate rewards including power-ups?
- Are tier cutoffs per crop, per level count, per market or per player segment?
- What are the important economic sinks around crop transitions and credit refresh?
- Does the team optimize a reward-milestone KPI in isolation or tie it to a broader business objective (return / ARPDAU / replay economy)?
- Which current features compete for stars/replays and could confound our test?

## 8. Source ledger with reliability labels

- **[S1] Official publisher app listing, current** — https://play.google.com/store/apps/details?id=net.supertreat.solitaire — verified genre, publisher, Credits/Gems/Boosters, crate upgrades, optional IAP; Google Play states updated 13 Nov 2026.
- **[S2] Official game how-to** — https://www.solitairegrandharvest.com/how-to-play-solitaire-grand-harvest/ — 1–3 stars, replay earlier levels to gain stars, core mechanics, side modes.
- **[S3] Official publisher credit guide, labeled 2025** — https://www.solitairegrandharvest.com/free-credits/ — Crop Master named, 25-level cadence according to that dated guide, credit harvest methods. Not current 2026 tier configuration.
- **[S4] Naavik, independent professional deconstruction, 6 Apr 2023** — https://naavik.co/deep-dives/solitaire-grand-harvest-deconstruction/ — historically detailed economy, sources/sinks, Crop Master 8-to-48 star progression, 1-to-10 reward picks, replay affordances. Historical and editorial, not an official config export.
- **[S5] Liquid & Grit, Dec 2019 report** — https://www.liquidandgrit.com/wp-content/uploads/2019/12/Puzzle-Report-December-2019.pdf — historical Crop Master collection + escalating star reward crate feature. Historical document with third-party copyrighted imagery; no images reused here.
- **[S6] Playtika, current Terms of Service** — https://www.playtika.com/terms-service/ — IP protections and limited game use license. Not a permission grant for public reproduction of assets.

**Research method:** public documentation triangulation; no scraping of player accounts, reverse engineering of game files, exploitation or claim of privileged access. Dated historical reports are not silently merged with 2026 observations.

## 9. Critical heterogeneity and decision robustness

The focused toy variant has **no modeled top-tier improvement for Casual players** (0% → 0%), while Regular rises **3.75% → 11.25%** and Engaged **32.33% → 49.17%**. This reinforces a key behavioral research point: even when cohort-level KPI increases, an intervention may largely help already-engaged players. A studio needs to define its target segment, expected effect and fairness/engagement trade-offs before choosing a threshold. The exact 46-star numerical recommendation is sensitive to the unvalidated score distribution, player replay propensity and shadow reward values. `SENSITIVITY_AND_ROBUSTNESS.md` demonstrates this explicitly.

## 10. Hypothetical star support check

The toy algebra needs a coherent possible star-score range. We explicitly choose a **fictional 20-level crop** purely for this purpose (possible 20–60 cumulative stars at 1–3 stars per level); all model initial and replay score-support intervals lie in this range. This 20-level toy assumption is **not** claimed to match any SGH live build, and must not be confused with the official 2025 reference to 25-level intervals. Discrete integer star outcomes would be required for a full calibrated model.
