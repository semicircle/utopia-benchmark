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

**v0 in progress.** The dialect generator, compiler, VM, docs generator and
seven T0 tasks work end to end. Households, seasons and the UI are not built
yet.

What a seed varies today:

- **Lexicon**: every keyword and builtin name is a fresh conlang word, from
  a per-seed sound system, in lower, UPPER or Title case.
- **Syntax styles**, chosen separately for functions, conditionals, switches
  and loops: C/Java-like (`{ }`), Pascal-like (`begin`/`end`, `repeat`/`until`,
  `case ... of`), BASIC-like (`END IF`, `WEND`, `FOR ... NEXT i`,
  `SELECT CASE`), and assembly-like (labels, `jumpif cond, label`, dispatch
  tables, no structured loops or ifs).
- **Operator spelling**: assignment `=`/`:=`/`<-`, equality, inequality,
  concatenation, `mod`, the statement terminator and the comment marker.
- **Semantics (false friends)**: argument and operand evaluation order,
  division rounding, index base, out-of-range wrapping, inclusive or
  exclusive counting loops, short-circuit logic, switch fallthrough, list
  equality, and operator precedence (standard, flat left-to-right, or flat
  right-to-left).

The reference manual comes from one fixed English template
([internal/docs/reference.md.tmpl](internal/docs/reference.md.tmpl)). Its
syntax blocks are drawn from the same templates the parser uses, and every
example in it is run to produce the output shown.

### Quick start

```bash
go build -o utopia ./cmd/utopia
./utopia docs -seed 42 | less                     # read a generated language reference
./utopia gen -seed 42 -out workspaces/s42 -bake    # workspace for an AI: docs, tasks, toolchain
./utopia render -seed 42 tasks/t0-fizzbuzz/solution.canon   # reference solution in that dialect
python3 harness/grade.py --bin workspaces/s42/bin/<name> --solutions workspaces/s42/solutions
```

Pass `-semantics standard` to keep conventional behavior and vary only
syntax and vocabulary. That makes a useful ablation arm.

### Running a model

`harness/run.py` drives a model through the `claude` CLI, so either a Claude
subscription login (`claude auth login`) or `ANTHROPIC_API_KEY` works. With
a key, runs use `--bare` (no hooks, plugins or CLAUDE.md), and the key is kept
out of the model's tool environment and redacted from saved results.

```bash
python3 harness/run.py oneshot --model reference --seeds 1-12 --out /tmp/selftest   # pipeline self-test, no model
python3 harness/run.py oneshot --arm python --model claude-opus-5-5                 # control arm
python3 harness/run.py oneshot --seeds 1-8 --semantics standard --model claude-opus-5-5
python3 harness/run.py oneshot --seeds 1-8 --model claude-opus-5-5                  # false friends
python3 harness/run.py agent --seeds 1,2 --model claude-opus-5-5                    # full agent runs
python3 harness/build_site.py                                                       # results site in _site/
```

- **oneshot**: the manual and all tasks in one prompt, no tools. Cheap, and it
  measures pure in-context learning.
- **agent**: a headless Claude Code agent in a fresh workspace outside this
  repo, with the manual, tasks and toolchain. Web tools are disabled and every
  path and command in the transcript is audited.

Each run lands in `results/runs/RUN_ID/` (scores, usage, prompt, response or
transcript, solutions). Pushing to `main` rebuilds the site and publishes it
with GitHub Pages (`.github/workflows/pages.yml`; set Pages' source to
"GitHub Actions" once in the repo settings).

### Layout

- `internal/lang`: AST, and a lexer, parser and printer driven by shape templates
- `internal/gen`: seed to dialect (styles, conlang lexicon, knobs) and the canonical dialect
- `internal/lower`: rewrites canonical programs into any dialect (down to labels and jumps)
- `internal/vm`: bytecode compiler and deterministic VM
- `internal/docs`: the language reference generator
- `tasks/`: tasks, each with a prompt, a canonical reference solution and hidden tests
- `harness/grade.py`: runs solutions against hidden tests
- `harness/run.py`: runs a model (one-shot or agent) and records the result
- `harness/build_site.py`: builds the static results site from `results/`

`go test ./...` checks that every reference solution passes its tests in
600 generated dialects. It also checks that lowered programs round-trip
through the printer and parser, and that the reference renders for every
seed.

See also:

- [docs/design.md](docs/design.md): design notes for v1
- [docs/related-work.md](docs/related-work.md): prior work and how Utopia differs
- [docs/roadmap.md](docs/roadmap.md): from v0 to a public leaderboard

## About

Utopia is an AI-native project: a benchmark designed for AIs, and built
together with AI coding agents.
