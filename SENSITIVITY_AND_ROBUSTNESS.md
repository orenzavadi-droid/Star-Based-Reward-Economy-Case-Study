# Sensitivity & decision robustness — independent teaching model

**Purpose:** expose where a plausible, transparent calculation could produce a misleadingly confident portfolio recommendation. Every number below is a **hypothetical model output**, not observed behavior in Solitaire Grand Harvest.

## Threshold stress test (all other assumptions fixed)

The published 2023 analysis describes a historical **48-star** high-tier endpoint; the model uses it only as an *illustrative reference*, not a current Playtika baseline. Tier 1/2/3 cutoffs and all score distributions are invented.

| Assumed top-tier stars | Model high-tier reach among crop-completers | Change in model net shadow-value proxy vs 48 | Toy +10% cap |
|---:|---:|---:|---|
| 48 | 6.16% | 0.00% | Reference |
| 47 | 8.46% | +2.28% | Pass |
| 46 | 11.31% | +5.29% | Pass |
| 45 | 14.17% | +8.29% | Pass |
| 44 | 17.02% | +11.30% | **Fail** |
| 43 | 19.88% | +14.31% | **Fail** |

These cutoffs are *not* empirically chosen. They only show the mechanism by which a tighter economic guardrail can reject a superficially more generous improvement.

## Shadow-prize value stress test

Vary the invented value per crate prize pick (reference 180 credit-equivalent teaching units). For the **46-star focused variant**, the modeled net proxy uplift remains below the 10% *illustrative* limit in this narrow range:

| Assumed value per pick | Model net shadow-proxy uplift |
|---:|---:|
| 100 | +6.26% |
| 140 | +5.54% |
| 180 | +5.29% |
| 220 | +5.15% |
| 260 | +5.07% |

**This is NOT comprehensive robustness.** Altering the star distributions, replay response, group shares, attempt costs, award menus or cohort-completion dynamics can change results drastically. The conversion of physical boosters/items into 'credit-equivalents' is hypothetical, not a real currency-equivalence rule. Actual Credits issuance and item reward economics must be tracked separately.

## Segments: the headline average conceals unequal benefit

| Synthetic segment | Reference high-tier reach | Focused high-tier reach | Interpretation |
|---|---:|---:|---|
| Casual | 0.00% | 0.00% | No modeled benefit |
| Regular | 3.75% | 11.25% | Material gain |
| Engaged | 32.33% | 49.17% | Largest gain |

**Economic question for the interviewer:** If the studio's real objective is to help *early-game* or *low-engagement* players, is a top-tier threshold reduction even the right tool? We should not optimize a cohort average while leaving the intended segment behind.

## The biggest inference boundary

- The workbook **conditions on a hypothetical crop completer**. It makes no prediction about the crop-completion probability or how many **crop entrants** would claim high tier. A real randomized trial should assign variants at **crop entry**, use an intention-to-treat entrant denominator and monitor completion. A narrower post-completion trial is possible but answers a different question.
- The 'net issuance' column is **prize shadow EV minus Credit replay expenditure**; these are not automatically comparable accounting units. Treat it as a toy cost proxy until a studio defines a sound valuation and a separate, reconciled true-Credits ledger.
- A real product rollout requires validated current feature mechanics, actual player telemetry, a preregistered success criterion, robust uncertainty quantification and explicit guardrails.

Reproduce this table with `python tests/sensitivity_analysis.py`. Python and workbook default reference results are independently checked in `tests/verify_model.py`.

## Logical score feasibility (additional audit)

For illustration only, choose a **fictional 20-level crop** (20–60 possible cumulative stars at 1–3 per stage). The synthetic initial and post-replay scores with their assumed ±6 uniform half-width remain within those bounds. This is deliberately **not** the officially described 25-level interval from a 2025 marketing guide. Never assert the toy crop length is the current in-game design. A future calibrated model should operate on empirical integer star totals, not uniform continuous scores.
