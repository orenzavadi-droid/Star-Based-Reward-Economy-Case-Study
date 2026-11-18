# Independent Red Team: claims the interviewer can attack

**Q1. Are those the actual star thresholds in today's game?**
No. Publisher materials confirm upgradable reward crates and star-based performance. Independent reports from 2019/2023 document historical Crop Master logic; the workbook **invented** middle-tier thresholds, segment distributions and economic values. The source dates do not establish 2026 current values.

**Q2. What about the official page that says Crop Master every 25 levels?**
That page is written as a 2025 guide. Naavik's 48-star high-tier comes from 2023. We do not combine the two to claim a consistent 25-stage / 48-star schema. Only the conceptual mechanism is borrowed.

**Q3. Is 'top-tier attainment' really a business KPI?**
It is an intermediate product/economy outcome, not necessarily a business KPI. Studio goals might instead emphasize replay attempts, retention, IAP RPU, economy health, or satisfaction. A good economist would validate alignment before optimizing it.

**Q4. Did you prove the change improves engagement or revenue?**
No. The spreadsheet estimates effects under assumed star distributions and replay probabilities. It has zero real players, zero observed experiments, zero actual revenue and no retention mechanism. Any such claim is unsupported.

**Q5. What is 'credit-equivalent' if prizes can contain boosters?**
An assumed shadow-price / reward-budget equivalence. It is **not** a transaction ledger and could be wrong. A studio would need item-specific expected values and accounting policy. Altering the assumed value in INPUTS changes model budget and recommendation.

**Q6. Why these segment shares and replay rates?**
To demonstrate heterogeneity and behavioral thinking, not because those are actual SGH customer distributions. In a real test, define segments from historical (pre-treatment) product data and sensitivity-test the assumptions.

**Q7. Your replay formula seems simplistic.**
Correct. `Replay participation = willingness × (0.5 + 0.5 × attainability of next goal after replay)`. It does not model time, heterogeneous star outcomes, progressive stopping, earned bonuses, overlapping events, personal loss aversion or 1–8× bet variations described historically. Treat it as a transparent teaching proxy, not a calibrated behavioral model.

**Q8. Can both modeled net emissions and reward budget matter?**
Yes as two heuristic guards: total cost of granting prizes and simplified net value after replay spend. But they omit most currency sources/sinks and non-currency items. They are not substitutes for a whole-economy model. Their 8%/10% limits are **arbitrary example policy thresholds**.

**Q9. Why only 3 configurations?**
Ease of communication and disentangling a focused change from a broad generosity change. In production, price, reward tiers, eligibility and meaningful heterogeneity require an explicit design of experiments, sensitivity analysis, and controlled testing. The workbook is editable and can be extended.

**Q10. Is it okay to publish a named game case study?**
No legal clearance was obtained. We avoid copyrighted art, logos and game files, use the name descriptively and provide clear independence attribution. Publisher terms reserve rights; consult counsel or publisher for publication plans that go beyond original analysis.

## Go / no-go for professional discussion

**Go:** "I reverse-engineered the decision question from public sources and built an assumption-explicit model illustrating the trade-offs."

**No-go:** "I know Playtika's current thresholds; I proved +5.15pp uplift and revenue growth in Solitaire Grand Harvest."

**Q11. Isn't your A/B design biased if you only randomize crop completers?**
Yes, for an end-to-end game-economy claim. We corrected this: the main proposed trial randomizes at **crop entry** and measures the top-tier claim rate over **all randomized entrants**. The workbook instead predicts a conditional, completer-only illustration and cannot be used as an ITT projection. A post-completion test is valid only for the narrower replay/claim question.

**Q12. Which player group actually benefits?**
The toy Focused variant changes high-tier reach from 0% to 0% for Casual, 3.75% to 11.25% for Regular, and 32.33% to 49.17% for Engaged. Thus the headline average increase is not a universal player benefit. This is a major reason to predefine target segments and check fairness/experience guardrails.

**Q13. What if input thresholds are non-monotonic?**
Tier cutoffs must be strictly increasing and prize picks nondecreasing. The audited workbook now has visible input-validation cells and labels invalid variants instead of silently reporting a PASS. Tests still cannot establish the model's external validity.

**Q14. Your net emission subtracts boosters' value from spent Credits. Is that coherent?**
Only as an explicitly defined hybrid *shadow-value budget proxy*. A real game economy analysis needs **two** ledgers: actual Credits source/sink transactions, and item-level expected reward cost. Their conversion/exchange rule must be empirically defined before merging them.

**Q15. Is the named-game GitHub case legally cleared?**
No. Public use of a factual game name with original analysis is generally lower risk than republishing assets, but Playtika's June 2026 Terms include limits on non-commercial entertainment use, on using Services/data for AI purposes, and on developing similar offerings. Whether these clauses apply to this independent work is not established, and no permission was obtained. See `LEGAL_AND_ATTRIBUTION.md`; avoid claiming this portfolio is officially authorized.

**Q16. You are using stars from 1–3 per level, yet a 25-level crop has at least 25 stars. Does your Casual distribution drop below that?**
Yes, if it were a 25-level crop. The audited model is instead explicitly a **fictional 20-level crop** (feasible total 20–60), with all modeled base and post-replay star supports inside that range. It makes no claim about the live crop length, and the 25-level official 2025 marketing description is not combined with 2023 thresholds. Replace the continuous score proxy with real integer per-crop data before applying to live game decisions.
