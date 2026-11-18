# Controlled test proposal (NOT conducted)

## Hypothesis
A *focused* reduction in the top-tier star requirement (holding all reward contents and other thresholds constant) may make the reward feel attainable and increase the **share of eligible crop entrants claiming the highest reward tier within a fixed window**. The crop-conditional model is only an illustrative intermediate calculation; it cannot predict the entrant-level A/B result. The game-economy cost must remain within defined guardrails; actual completion, retention and IAP effects are unknown.

## Variants
- **A — Current live control**: the game's **actual** current star tiers, retrieved from internal configuration only; **unknown to this project**.
- **B — Focused adjustment**: lower only the top-tier cutoff by an amount chosen after inspecting actual distributions and expected-value budgets.
- **C — Optional exploratory**: consider a broader generosity version **only if** pre-test economy simulations allow it. Do not treat exploratory C as confirmatory without adjusting tests.

**Important:** the workbook's 'Reference' 8/24/36/48 and 'Focused' 8/24/36/46 are **toy settings**. They are not the actual A/B test values and should never be uploaded into production configuration.

## Eligibility & randomization
- **Eligibility:** players entering a selected crop **before any variant-dependent star-threshold exposure, completion, replay or reward claim**. Verify the current in-game flow first; if thresholds are visible earlier, the assignment must precede that exposure. Exclude only pre-registered, pre-assignment ineligible players.
- **Assignment:** randomize at crop entry, 50/50 A/B, at the player level; persist the same arm across that crop and preferably across repeat exposures. Stratify by pre-treatment crop level / historical engagement where useful.
- **Primary analysis:** intention-to-treat (ITT) among **all randomized crop entrants**, including those who do not finish the crop, open a crate, or replay. Use a fixed outcome window long enough to observe crop completion; choose the window from actual observed cycle duration, not from the toy workbook.
- Do not randomize on `crop_completed` and then report per-entrant uplift. Completion is potentially affected by treatment; conditioning on it can induce selection bias.
- If studio exposure is unavoidably only after crop completion, an **alternative post-completion experiment** is valid but answers a narrower question about replay/claim decisions *among completers*. Do not generalize that result to overall progression or full-player retention.

## Pre-register metrics

**Primary (experiment proposal) — high-tier crate claim rate per crop entrant:** # randomized entrants claiming the high-tier crate by a pre-registered common observation cutoff / **all randomized crop entrants**. Select the time window based on actual time-to-crop-completion distribution; seven days is merely a placeholder to evaluate. This is an *intermediate* product outcome, not necessarily studio revenue.

**Secondary:** crop-completion rate per entrant; high-tier claim rate **among completers** (descriptive/conditional; not the main ITT); replay attempt rate per randomized entrant; attempts, star gains and cost per user; time to crop completion and crate claim; reward tier distribution; subsequent play sessions and time spent per crop.

**Economy guardrails:** real Credits credited/debited per randomized entrant from **all** relevant sources and sinks (including harvest, level winnings, boosters, continuation), plus a **separate** item-level reward-cost/EV budget. Do not silently subtract a booster shadow value from actual Credits and call the result a reconciled ledger. Track replay spend, normalized wallet distributions, credit depletion, extra cards/boosters and crop-level scale.

**Player & monetization guardrails:** D7 post-assignment return, payer conversion, IAP revenue per randomized entrant over the pre-registered window (IAP RPU, not ARPDAU), purchases/refunds where applicable, perceived frustration / complaints. Do not assume direction. Analyze segment heterogeneity: the toy model's focused change offers **zero** high-tier gain for Casual, but material gains for Regular and Engaged; do not optimize averages while ignoring segment fairness.

## Segmentation plan
- **Pre-treatment**: game tenure, past 14-day replay activity, crop/progression stage, previous purchases or spend *before assignment*, and resource balance if reliably recorded before treatment.
- Avoid post-treatment segmentation that conditions on replay, crate claiming or payer conversion, which creates selection bias.
- Compare outcomes by segment; if sparse, use descriptive intervals and treat subgroup findings as exploratory.

## Decision gates
1. Integrity checks: exposure, assignment counts, carryover, event logging and duplicate events pass.
2. Primary metric shows practically meaningful improvement and estimated confidence interval meets the pre-stated decision threshold.
3. Economy budget, true Credits source/sink reconciliation and monetization guardrails show no unacceptable harm, with uncertainty accounted for.
4. Behavior guardrails do not reveal material frustration/retention harms in any important segment.
5. If primary improves but guardrails fail: **HOLD**, diagnose, reconfigure, rerun. A modeled positive result is **not** sufficient.

## Statistics and caveats
- Sample size and MDE must be derived from actual baseline top-tier claim rate, randomization unit, expected detectable effect and guardrail variance; this public case does not invent a 'required N'.
- Pre-register tests, two-sided confidence intervals / sequential monitoring, planned duration; control the number of primary hypotheses, avoid peeking.
- Non-normal credit and revenue distributions may need player-level bootstrap or robust interval methods.
- Seasonality, event calendar, crop-level scaling, changing player mix and experiment interference are confounders to monitor.
- **No actual A/B was run.** The Excel is a deterministic assumed-value proxy and demonstrates decision structure only.

### Model vs experiment: denominator reconciliation

The Excel model is explicitly **conditioned on crop completion** and holds the share of completers fixed. Its 6.2%/11.3%/12.4% outputs **cannot be read as the experiment's entrant-level claim rate**. The recommended real-world experiment randomizes **before crop completion**, uses the entrant denominator, and measures completion separately. Only after estimating the actual entrant-to-claim pipeline could an end-to-end business impact be claimed. If this game currently hides the threshold until after completion, an alternative narrower post-completion A/B may be operationally cleaner; that design answers a different estimand and needs its own hypotheses.
