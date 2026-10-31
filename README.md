<p align="center">
  <img src="assets/logo.png" width="140" alt="run the sim" />
</p>

<h1 align="center">run the sim</h1>

<p align="center">We answer the questions you google at 2 a.m. — by simulating them.<br/>
10,000 lives per question · assumptions on screen · open code</p>

---

This is the simulation behind **episode 01: "At what age is it too late to start over?"**

Every number in the video comes from this file. Nothing else.

## Run it — 3 steps, no experience needed

**1 · Get Python** (skip if you have it): [python.org/downloads](https://www.python.org/downloads/)

**2 · Install the one thing it needs** — open a terminal and run:

```bash
pip install numpy
```

**3 · Download this repo** (green button → Download ZIP, or `git clone`), then:

```bash
python life_sim.py
```

After a few seconds you'll see the table from the video:

```
switch at | catch up (money) | happier they switched
   45     |       50%        |    84%  <- the coin flip
```

## Now change one line

Open `life_sim.py` in any editor. The very first setting is the luggage line:

```python
TRANSFER = 0.4   # how much of your skill travels with you
```

Make it `0.8`. Run again. Watch the coin flip move.

That's the whole idea: don't trust us — rerun the world with your own assumptions.
Every assumption lives in the block at the top of the file.

## What this is — and isn't

- A **simulation**, not a study. No real people were measured.
- Five rules build the world; the code computes what follows.
- Stress-tested across 81 assumption variants: the coin-flip age stayed in the
  mid-forties in about 4 of 5 worlds. The exact number belongs to this model.

**Do I need math?** No. **Do I need to code?** No — you change one number and press enter.

MIT license — do what you want, a link back is appreciated.
