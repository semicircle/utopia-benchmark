# Roadmap

There's no paper planned. The goal is an open benchmark people can run and
trust: a GitHub repo, a website and a leaderboard.

## v0: first result

The goal is one striking chart, as early as possible.

- [x] Minimal VM and compiler (four syntax styles, ten semantic knobs)
- [x] Generator with conlang lexicon, syntax styles and semantic knobs
- [x] Docs generated from a fixed English template, with executed examples
- [x] 7 T0 tasks with hidden tests and canonical reference solutions
- [x] T1–T2 tasks (10), with hidden tests from independent Python references
- [x] Python control versions of every task
- [x] Grader (`harness/grade.py`)
- [x] Harness: give the docs and toolchain to an agent, run it, score it (`harness/run.py`)
- [x] One-shot mode (docs + tasks in one prompt, no tools) and a Python control arm
- [x] Results site (`harness/build_site.py`, deployed by GitHub Pages)
- [ ] Babel lexicon (metaphorical keywords from human languages)
- [ ] Run about 4 models and record full transcripts

## v1: public launch

- [ ] Households, letters, seasons and a headless cell-grid UI
- [ ] Errata ledger with ~8 seeded bugs
- [ ] ~15 tasks across T0–T4
- [ ] Native and Babel leaderboards
- [ ] Human baseline (at least one engineer, same docs, time budget)
- [ ] Website: leaderboard, methodology page and transcript highlights
- [ ] Launch: write-up, Show HN, r/LocalLLaMA, X/Twitter

## Later

- [ ] Hard-mode tier (priorities, reordering optimizer, memory pools)
- [ ] Hidden "surprise" knobs
- [ ] A second platform profile (for example async actors or CSP), on the same
  `Scheduler`/`Allocator` substrate
- [ ] Optional: turn the methodology page into an arXiv technical report

## Principles

- Make it reproducible, with open code and public practice seeds. Keep the
  evaluation seeds private.
- Make modest claims. It measures learning an unseen language from docs, not
  "true intelligence".
- Lead with stories: transcripts of false friends and bug hunts.
- Watch API costs: start with few models and short tasks.
