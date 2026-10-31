# run the sim

We answer the questions you google at 2 a.m. by simulating them.
Ten thousand lives per question · assumptions on screen · open code.

This repo holds the simulation behind **episode 01 — "At what age is it too late to start over?"**

## Run your own world

```bash
pip install numpy
python life_sim.py
```

Takes a few seconds. You'll get the full table from the video: for every switch age,
the share of switchers who ever financially catch up with the twin who stayed — and the
share who end up gladder to be alive.

## The luggage line

Open `life_sim.py`. The assumptions sit at the top:

```python
TRANSFER = 0.4   # the luggage line: how much of your skill travels with you
```

Change `0.4` to `0.8`, run again, and watch the coin-flip age move. That's the whole
point: don't trust us — rerun the world with your own assumptions.

## What this is (and isn't)

It is a **simulation, not a study**. No real people were measured; we built a world
from five rules (practice curves, fit as the learning throttle, a promotion gap for
misfits, a 15% restart failure rate) and computed what follows.

We stress-tested the result by rebuilding the world 81 times with different
assumptions: the coin-flip age moved between 36 and 51, and landed in the mid-forties
in about four out of five worlds. The exact number belongs to this model. The pattern
is sturdy.

Deterministic by design: same seed, same world (`SEED = 42`).

## License

MIT — do whatever you want, a link back is appreciated.
