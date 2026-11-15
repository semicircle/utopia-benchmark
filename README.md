# Utopia

> *Can your AI code in a language that didn't exist this morning?*

**Utopia** is an AI-native benchmark for coding ability that cannot be memorized.

Every evaluation run generates a brand-new **disposable language**: fresh
keywords, shifted semantics, its own concurrency model, OS interfaces, UI API
and virtual machine, plus a few hidden system bugs. The AI under test gets the
documentation and a working toolchain, and must build real apps in it.

Nothing it wrote during training applies. It has to read, learn, experiment
and debug, inside a single context.

*Utopia* comes from the Greek *ou-topos*, meaning "no place". These languages
come from nowhere, nobody speaks them, and each one disappears after its test.

## Why

Today's coding benchmarks mostly measure recall. Models have seen millions of
Python and JavaScript programs, so "write a todo app" often means remembering
one rather than engineering one. Prior work backs this up: frontier models
that score ~100% on problems in Python drop to 0–11% on the same problems in
esoteric languages ([EsoLang-Bench](https://arxiv.org/abs/2603.09678)).

Utopia measures what is left when recall is taken away:

- **In-context learning**: learning a whole language and platform from its docs.
- **Following the spec over habit**: semantics that *look* familiar but behave
  differently ("false friends").
- **Engineering**: building working, multi-part apps, not toy algorithms.
- **Debugging the platform itself**: finding and working around seeded VM bugs
  and docs that are wrong.

## Core ideas

1. **Generated, not written.** A seed produces the whole dialect, including
   lexicon, semantic knobs, docs, toolchain and seeded bugs. Hidden evaluation
   seeds keep it contamination-resistant by construction, even after
   publication.
2. **Novelty in semantics, not just syntax.** Renamed keywords are learned in
   minutes. Different *behavior* is what breaks memorized code.
3. **Fair, not hostile.** A good human engineer should be able to learn a
   dialect in an afternoon. Painful features (priority inversion, reordering
   compilers, hand-managed memory pools) are optional knobs or hidden
   "surprises", never the default.
4. **Deterministic.** The scheduler is seeded, so every bug reproduces and every
   score is stable.
5. **Underrepresented but coherent models.** For example: synchronous-tick
   concurrency, capability-isolated "households" exchanging "letters" instead
   of processes, region-based memory with lexical lifetimes, and a reactive
   cell-grid UI.

## Two leaderboards

- **Utopia: Native** uses invented conlang keywords. No priors from any human
  language, and uniform tokenization for every model.
- **Utopia: Babel** uses metaphorical keywords drawn from many human languages
  (Japanese, Chinese, Spanish, French, Hindi, ...). It is more interesting,
  but carries tokenizer bias, so it is scored separately.

## Scoring (planned)

- Pass rate on hidden test suites per task.
- **Prior-dependence gap**: the same tasks in Python as a control arm. The
  drop from Python to Utopia is the headline number.
- Process metrics: iterations to green, tokens spent, and seeded bugs found
  and worked around.
- A **human baseline**: an engineer with the same docs and a time budget.

## Status

Idea stage. See:

- [docs/design.md](docs/design.md): design notes for v1
- [docs/related-work.md](docs/related-work.md): prior work and how Utopia differs
- [docs/roadmap.md](docs/roadmap.md): from v0 to a public leaderboard

## About

Utopia is an AI-native project: a benchmark designed for AIs, and built
together with AI coding agents.
