# Roadmap

There's no paper planned. The goal is an open benchmark people can run and
trust: a GitHub repo, a website and a leaderboard.

## v0: first result

The goal is one striking chart, as early as possible.

- [ ] Minimal VM and compiler for one dialect family
- [ ] Generator with a handful of lexicon and semantic knobs
- [ ] ~5 tasks (T0–T2) with hidden tests and Python control versions
- [ ] Harness: give the docs and toolchain to an agent, run it, score it
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
- [ ] Optional: turn the methodology page into an arXiv technical report

## Principles

- Make it reproducible, with open code and public practice seeds. Keep the
  evaluation seeds private.
- Make modest claims. It measures learning an unseen language from docs, not
  "true intelligence".
- Lead with stories: transcripts of false friends and bug hunts.
- Watch API costs: start with few models and short tasks.
