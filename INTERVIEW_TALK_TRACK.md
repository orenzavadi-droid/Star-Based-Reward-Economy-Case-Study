# Interview / Zoom guide

## 45-second pitch (English)

"I researched Solitaire Grand Harvest's publicly documented star-based reward crates. Instead of modeling the whole game, I focused on one economy question: could a more achievable top-tier crate improve perceived progress without giving away too much reward value? I built an editable Excel model with three illustrative segments, replay incentives, star thresholds and two economy guardrails. Under my explicitly hypothetical assumptions, lowering only the top requirement improved modeled reach from 6.2% to 11.3% while raising net credit-equivalent emission about 5.3%, within my toy limits. A broader change pushed net emission up 19.4% and failed. This doesn't demonstrate real uplift; I'd validate the current mechanic and use actual player data and a controlled A/B before recommending any rollout."

## Two-minute structure

1. **Context (15s):** F2P TriPeaks Solitaire + farm economy; 1–3 star scores and upgradable crate tiers publicly described.
2. **Problem (20s):** a difficult top-tier milestone may suppress motivation; an overly generous threshold may inflate the economy.
3. **Psychology (20s):** Cas/Reg/Eng behavior differs in willingness to replay; perceived attainable goals matter; those are hypotheses requiring data.
4. **Method (35s):** 3 configurations, 3 hypothetical segments, star distribution proxy, replay participation formula, expected picks, expected credit-equivalent payout and replay spend.
5. **Trade-off (20s):** focused version modeled +5.15pp high-tier attainment and +5.3% net emission; broad version +6.26pp and +19.4%, guardrail fail.
6. **Business decision (10s):** pilot candidate, not launch; monitor actual IAP and D7 as downstream metrics.

## Questions to ask the SGH economist

- Which current public feature most closely resembles star-gated crate tiers?
- Would you expect any threshold change to alter replay behavior, or mostly claim distribution?
- What are the relevant reward and economy accounting units; does 'credit-equivalent' make sense here?
- Which player segmentation is practical: crop level, past replay depth or payer status?
- What is one important metric we have neglected before making a live decision?

## Three technical questions to expect

**Why not use data from the actual game?** No access to telemetry, and public writeups are historical. We explicitly demonstrate a *framework* and identify what would be needed to fit it.

**Why would increasing reward accessibility lead to more engagement?** It might not. We hypothesize a goal-gradient effect and need a randomized experiment measuring replay attempts and post-assignment activity.

**Why is the 'focused' scenario preferred?** *Only in this toy setup*, it satisfies **assumed** guardrails while improving top-tier attainment. The point is economy-aware decision-making rather than claiming it is universally optimal.

## CV-friendly honest descriptor

"Independent star-based reward-tier economy case study inspired by Solitaire Grand Harvest: built Excel scenario model for attainment, replay credit spend and reward-budget guardrails; proposed a pre-registered experiment and segment-level KPIs."

## Three red-team refinements to volunteer in the Zoom

1. **Heterogeneity beats the headline:** the model's focused change has no effect on modeled Casual high-tier reach, while Regular/Engaged gain considerably. Ask whether top-tier accessibility is the right target segment KPI at all.
2. **Conditional vs ITT:** 6.2%→11.3% is conditional on crop completion. A true trial should randomize at crop entry and measure high-tier claims per randomized entrant; otherwise a narrower post-completion replay experiment is the honest estimand.
3. **Economy accounting:** the toy `net emission` mixes a shadow estimate of prize value with Credit spend. An actual studio needs a true currency ledger, plus separate item-level expected payout costs.
