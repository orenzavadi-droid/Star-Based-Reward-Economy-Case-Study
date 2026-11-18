"""Original, pure-Python reproduction of the editable Excel teaching model.

This is a deterministic illustrative decision model, not a real SGH simulation.
Run: python tests/verify_model.py
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Segment:
    weight: float
    stars: float
    replay_willingness: float
    replay_gain: float
    replay_attempts: float
    credit_cost_per_attempt: float

SEGMENTS = [
    Segment(.50, 29, .22, 5, 3, 160),
    Segment(.35, 35, .45, 8, 5, 160),
    Segment(.15, 41, .70, 8, 6, 160),
]
SCENARIOS = {"Reference": (8, 24, 36, 48),
             "Focused top-tier": (8, 24, 36, 46),
             "Broad generosity": (8, 24, 34, 45)}
PICKS = (1, 3, 6, 10)
SPREAD = 6  # assumed half-width of approximate uniform distribution
TOY_CROP_LEVELS = 20  # explicitly fictional; possible cumulative stars: 20..60
PICK_EV = 180  # fictional credit-equivalent units, NOT a real prize value

def p_ge(mean, threshold):
    return max(0.0, min(1.0, (mean + SPREAD - threshold) / (2 * SPREAD)))

def evaluate(thresholds):
    results = []
    for s in SEGMENTS:
        next_goal = next((t for t in thresholds if t > s.stars), thresholds[-1])
        attainable_if_replay = p_ge(s.stars+s.replay_gain, next_goal)
        replay = s.replay_willingness * (.5 + .5 * attainable_if_replay)
        tier_reach = [((1-replay)*p_ge(s.stars, t) + replay*p_ge(s.stars+s.replay_gain, t))
                      for t in thresholds]
        expected_picks = (tier_reach[0]*PICKS[0] +
                          sum(tier_reach[i]*(PICKS[i]-PICKS[i-1]) for i in range(1,4)))
        reward_ev = expected_picks*PICK_EV
        replay_spend = replay*s.replay_attempts*s.credit_cost_per_attempt
        results.append(dict(w=s.weight,top=tier_reach[-1],picks=expected_picks,
                            reward=reward_ev,spend=replay_spend,net=reward_ev-replay_spend))
    return {key:sum(r[key]*r['w'] for r in results) for key in ('top','picks','reward','spend','net')}

if __name__ == '__main__':
    assert abs(sum(s.weight for s in SEGMENTS)-1) < 1e-10
    for s in SEGMENTS:
        assert s.stars-SPREAD >= TOY_CROP_LEVELS, 'Initial score lower than 1 star per toy level'
        assert s.stars+s.replay_gain+SPREAD <= 3*TOY_CROP_LEVELS, 'Post-replay exceeds max toy stars'
        assert 0 <= s.replay_willingness <= 1
    output = {name:evaluate(thr) for name,thr in SCENARIOS.items()}
    a=output['Reference']; b=output['Focused top-tier']; c=output['Broad generosity']
    assert abs(a['top']-0.061614583333333334)<1e-10
    assert abs(b['top']-0.113125)<1e-10
    assert abs(c['top']-0.12416666666666668)<1e-10
    assert (b['net']/a['net']-1)<.10 and (b['reward']/a['reward']-1)<.08
    assert (c['net']/a['net']-1)>.10
    assert b['top']>a['top'] and c['top']>b['top']
    for name,r in output.items():
        print(f'{name:20s} | top {r["top"]:.1%} | picks {r["picks"]:.2f} | reward EV {r["reward"]:.1f} | replay spend {r["spend"]:.1f} | net {r["net"]:.1f}')
    print('PASS: deterministic arithmetic and illustrative decision gates')
