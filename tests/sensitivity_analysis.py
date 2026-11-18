"""Independent sensitivity checks for the hypothetical Crop Master model.

This is parameter stress-testing, NOT external validation or a prediction.
Run: python tests/sensitivity_analysis.py
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_model as model

base_thr=(8,24,36,48)
base=model.evaluate(base_thr)
assert abs(base['top']-0.061614583333333334)<1e-12
assert 0 < base['top'] < 1

print('TOP-TIER THRESHOLD STRESS TEST | reward pick value = 180 (invented)')
print('top-stars | modeled reach | modeled net proxy change | passes 10% net guard')
for top in [43,44,45,46,47,48]:
    case=model.evaluate((8,24,36,top))
    rel=case['net']/base['net']-1
    passes=rel<=.10
    print(f'{top:>9d} | {100*case["top"]:>11.2f}% | {100*rel:>23.2f}% | {passes}')
    if top==44: assert not passes
    if top==46: assert passes

print('\nASSUMED PRIZE-VALUE STRESS TEST | focused threshold 46')
for prize_ev in [100,140,180,220,260]:
    model.PICK_EV=prize_ev
    ref=model.evaluate(base_thr)
    case=model.evaluate((8,24,36,46))
    rel=case['net']/ref['net']-1
    assert case['top']>ref['top']
    assert rel<.10
    print(f'EV per pick {prize_ev:3d} hypothetical units: net proxy +{100*rel:.2f}%')
model.PICK_EV=180

print('\nSEGMENT DIFFERENCES IN FOCUSED SCENARIO')
def seg_top(seg, cutoff):
    next_goal=next((t for t in [8,24,36,cutoff] if t>seg.stars), cutoff)
    replay=seg.replay_willingness*(.5+.5*model.p_ge(seg.stars+seg.replay_gain,next_goal))
    return (1-replay)*model.p_ge(seg.stars,cutoff)+replay*model.p_ge(seg.stars+seg.replay_gain,cutoff)
for name,seg in zip(['Casual','Regular','Engaged'],model.SEGMENTS):
    a=seg_top(seg,48);b=seg_top(seg,46)
    print(f'{name:8s}: {100*a:.2f}% -> {100*b:.2f}%')
assert seg_top(model.SEGMENTS[0],48)==seg_top(model.SEGMENTS[0],46)==0
print('\nPASS: Toy model sensitivity checked, with acknowledged incompleteness.')
