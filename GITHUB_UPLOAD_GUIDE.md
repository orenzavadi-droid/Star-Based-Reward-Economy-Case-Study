# Publish this independent case to GitHub

**Suggested neutral repository name:** `Star-Based-Reward-Economy-Case-Study`

**Description:** `Independent Game Economy case study inspired by Solitaire Grand Harvest: Excel reward-tier balancing, player segmentation, sensitivity checks and A/B experiment design. Assumption-driven, not publisher-affiliated.`

## Before publishing

- Read `LEGAL_AND_ATTRIBUTION.md` and `AUDIT_REPORT.md`. Publisher permission / Terms compliance is **not confirmed**, particularly AI/data-use restrictions. The materials are original analysis of short, attributed public facts, not official endorsement or game telemetry. If you want full certainty, seek publisher authorization or qualified legal advice.
- **Do not** include copyrighted game screenshots, logos, original code or private correspondence with employees. No such assets are supplied in this package.
- Confirm all custom content is independently authored and that you are comfortable identifying the game in public. A neutral repository name does not remove any legal uncertainties.

## Upload manually

1. Create a **public** repository on GitHub named `Star-Based-Reward-Economy-Case-Study` (or your preferred neutral name). Leave GitHub's auto-README unchecked.
2. Extract the `GITHUB_READY.zip` artifact provided alongside this guide.
3. On the repository's `Add file > Upload files` page, upload **all files and folders inside the extracted directory**, keeping their paths.
4. Commit, then check `README.md`, `CASE_STUDY_ONE_PAGER.pdf`, `Crop_Master_Economy_Model.xlsx`, `STUDY_GUIDE_HE.html` and both Python tests appear. Open each to verify.
5. Run locally if desired: `python tests/verify_model.py && python tests/sensitivity_analysis.py` (only Python standard library is required for those tests).

## Suggested interview disclosure

> This is an independent, assumption-driven analysis of publicly described mechanics. The specific star thresholds, player segments, payouts and outputs are invented scenarios, not Playtika's current live settings. I'd use real data and a preregistered test before making a rollout decision.

## Link quality

A GitHub link should **not** be added to a CV until the repository's actual files and the artifact previews have been checked. Do not imply any Playtika affiliation or use company imagery without approval.
