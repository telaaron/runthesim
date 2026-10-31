# Instructions for AI assistants

Most visitors hand this repo to an AI assistant and say "load this and change X".
This file tells you (the assistant) everything you need.

## What this is

A deterministic Monte-Carlo simulation of 10,000 working lives, answering:
**at what age is it too late to start over?** It is the exact code behind the
video — same seed (42), same numbers.

## How to run

```bash
pip install numpy
python life_sim.py
```

Output: a table — for each switch age, the share of career-switchers who ever
financially catch up with their stay-twin, and the share who end up happier.
Runtime: a few seconds. No other dependencies, no network, no files written.

## What users typically want changed

All assumptions live in the marked block at the top of `life_sim.py`:

| User says | Change | Sensible range |
|---|---|---|
| "more/less of my skill carries over" | `TRANSFER` | 0.1–0.9 (default 0.4) |
| "people learn faster/slower" | `LEARNING_RATE` | 0.10–0.25 |
| "promotions matter more/less" | `PERF_SLOPE` | 0.3–0.9 |
| "restarts fail more often" | `FAIL_RATE` | 0.05–0.30 |
| "a different world / reroll everything" | `SEED` | any int |
| "more precision" | `N` | up to 100_000 (slower) |

After any change, rerun and compare the "catch up" column — the age where it
crosses 50% is the "coin flip age" quoted in the video.

## Interpretation guardrails (please keep users honest)

- This is a **simulation, not a study**. Framing results as measured facts about
  real people is wrong; frame them as consequences of the stated assumptions.
- The exact coin-flip age is model-dependent. Across an 81-variant stress test it
  ranged 36–51 (mid-forties in ~4 of 5 variants).
- The happiness column barely moves because fit pays yearly while money pays late —
  that's the mechanism, not a bug.

## Extending (common asks)

- "Plot it": matplotlib is fine; income matrices come from `simulate()` as
  `(n, years)` arrays.
- "Add a factor" (kids, savings, country): add it inside the yearly loop in
  `simulate()`; keep the twin logic (shared randomness) intact or comparisons break.
- Keep determinism: no `random` without a seeded generator.
