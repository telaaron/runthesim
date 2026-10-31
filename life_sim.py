"""run the sim — episode 01: At what age is it too late to start over?

10,000 simulated working lives. Change the assumptions below, run it,
and watch your own world. Requires: numpy (pip install numpy).

This is a simulation, not a study: no real people were measured.
We built a world from five rules and computed what follows.
"""
import numpy as np

# ----------------------------- the assumptions -----------------------------
TRANSFER = 0.4      # the luggage line: how much of your skill travels with you
LEARNING_RATE = 0.16   # how fast skill grows (scaled by fit)
PERF_SLOPE = 0.6    # promotion penalty/bonus from fit (rule 4)
FAIL_RATE = 0.15    # share of restarts that land in a worse-fitting job (rule 5)
N = 10_000          # lives per world ("one story is an anecdote")
SEED = 42           # change me for a different world
# ---------------------------------------------------------------------------

AGE0, RETIRE, AGE_END = 18, 67, 85
YEARS = AGE_END - AGE0
BASE = 50_000.0

def age_learning_factor(age):
    return np.clip(1.0 - 0.006 * np.maximum(age - 20, 0), 0.6, 1.0)

def seniority(tenure):
    return 0.75 + 0.25 * (1 - np.exp(-tenure / 12.0))

def simulate(fit0, switch_age=None, transfer=TRANSFER, twin_seed=1000):
    """One world. Twins share randomness: everyone competes only against themselves."""
    n = len(fit0)
    local = np.random.default_rng(twin_seed)
    uplift_raw = local.beta(2, 2, n)
    fails = local.random(n) < FAIL_RATE
    fit = fit0.copy()
    skill = np.full(n, 0.05)
    tenure = np.zeros(n)
    income = np.zeros((n, YEARS))
    satisf = np.zeros((n, YEARS))
    for t in range(YEARS):
        age = AGE0 + t
        if switch_age is not None and age == switch_age:
            uplift = np.where(fails, -0.08, uplift_raw * np.maximum(0.9 - fit, 0))
            fit = np.clip(fit + uplift, 0.02, 0.98)
            skill = transfer * skill          # <- your luggage
            tenure[:] = 0
        if age < RETIRE:
            lr = LEARNING_RATE * fit * age_learning_factor(age)
            skill = np.clip(skill + lr * (1 - skill) - 0.004 * (1 - fit), 0, 1)
            tenure += 1
            perf = (1 - PERF_SLOPE / 2) + PERF_SLOPE * fit
            pay = BASE * (0.35 + 0.65 * skill) * seniority(tenure) * perf
            if switch_age is not None and age == switch_age:
                pay *= 0.55                   # retraining year
        else:
            pay = np.full(n, 0.45 * BASE)
        income[:, t] = pay
        satisf[:, t] = 0.55 * fit + 0.45 * np.sqrt(np.clip(pay / (1.9 * BASE), 0, 1))
    return income, satisf

def main():
    rng = np.random.default_rng(SEED)
    fit0 = rng.beta(2.2, 2.8, N)              # career choice at 18 ≈ a dice roll
    misfits = fit0 < 0.4
    print(f"world seed {SEED} · n={N} · misfits: {misfits.mean()*100:.0f}%\n")
    inc_stay, sat_stay = simulate(fit0)
    life_stay = inc_stay.sum(axis=1)
    sat_stay_total = sat_stay.sum(axis=1)

    print("switch at | catch up (money) | happier they switched")
    for age in (25, 30, 35, 40, 45, 50, 55, 60):
        inc_sw, sat_sw = simulate(fit0, switch_age=age)
        t0 = age - AGE0
        cum = np.cumsum(inc_sw[:, t0:] - inc_stay[:, t0:], axis=1)
        ever = (cum > 0).any(axis=1)[misfits].mean() * 100
        happier = ((sat_sw.sum(axis=1) - sat_stay_total) > 0)[misfits].mean() * 100
        marker = "  <- the coin flip" if 48 <= ever <= 53 else ""
        print(f"   {age:2d}     |      {ever:3.0f}%        |   {happier:3.0f}%{marker}")

if __name__ == "__main__":
    main()
