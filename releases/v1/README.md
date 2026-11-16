# Utopia v1

Utopia's normal mode generates a fresh language for every run, so nothing can
have been memorized. A release does the opposite: it fixes a small set of
languages so that every result on it is comparable and anyone can check it.
v1 has two languages and the 17 tasks in `tasks/` (tiers T0 to T2).

| Language | Seed | Manual | Hidden settings | Styles (func / if / switch / loop) |
|---|---|---|---|---|
| Reslil (`.res`) | 182 | [reference.md](reslil/reference.md) | [settings.json](reslil/settings.json) | basic / c / basic / c |
| Dushpek (`.dus`) | 977 | [reference.md](dushpek/reference.md) | [settings.json](dushpek/settings.json) | c / asm / pascal / pascal |

Both have false friends on (`-semantics random`). Between them, every
setting differs from the conventional one in at least one language:

- **Reslil:** loops that stop before their end value, division rounding toward
  negative infinity, lists compared by identity, flat right-to-left operator
  grouping, no short-circuit evaluation, switch cases that fall through.
- **Dushpek:** arguments and operands evaluated right to left, division
  rounding toward positive infinity, indexes from 1, out-of-range indexes that
  wrap around, flat left-to-right operator grouping. Its `if` is written with
  labels and jumps.

The model under test sees only the manual and the task prompts. `settings.json`
is published so results can be audited; it reveals nothing the manual does not
already state.

## How the two were chosen

By a fixed rule that looks only at the generated languages, never at any
model's results. `scripts/pick_languages.py` states and applies it:
seeds 100-999, each language with 4 to 6 false friends, together covering
all of them (one floor and one ceiling division, one left and one right flat
grouping), different styles in every slot, first such pair in seed order.

## Running and verifying

```bash
.venv/bin/python harness/run.py oneshot --release v1 --model MODEL ...
.venv/bin/python harness/run.py agent   --release v1 --model MODEL ...
```

`--release v1` is the same as `--seeds 182,977 --semantics random`, plus the
release's protocol, which is the same for every model: up to 64,000 output
tokens per request (thinking included) and, in agent mode, 150 model
requests. The run's `meta.json` records `"release": "v1"` and both limits.
An answer cut off at the token limit is graded as it stands. To check a published result,
re-grade its saved answer (`harness/regrade.py results/runs/RUN_ID`) or run
the model again. `go test ./internal/docs` fails if any change to the
generator would alter these two languages; such a change needs a new release.

Fixed languages can leak into training data once published, and fresh seeds
cannot. Treat v1 as the reproducible benchmark and fresh seeds as the
contamination-proof check.
