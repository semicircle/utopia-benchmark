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

**v0 in progress.** The dialect generator, compiler, VM, docs generator,
harness, results site and 25 tasks work end to end. Households, seasons and
the UI are not built yet.

Tasks come in tiers:

- **T0** (7 tasks, 1 to 20 lines): hello, counting, FizzBuzz and the like. A
  smoke test: every model tried so far solves all of them.
- **T1** (6 tasks, 20 to 50 lines): digit sums, floor division, rotation,
  palindromes, binary-search rank, weekday of a date.
- **T2** (4 tasks, 50 to 150 lines): an RPN calculator, Game of Life,
  100-digit arithmetic, word frequencies.
- **T3** (5 tasks, 100 to 200 lines): an infix calculator with precedence,
  shortest paths in a maze, 80-digit division, full text justification and
  a register-machine interpreter. Long enough that one slip with a false
  friend anywhere shows; each has 5–9 test files, so a nearly right program
  scores partly.
- **T4** (3 tasks, 300 to 500 lines): small systems. A Lisp interpreter
  with closures, a spreadsheet with ranges and spreading errors, and a
  regular-expression matcher. Their tests form a ladder, one feature per
  test file, so the score falls in steps.

Every program parses its own input character by character (there is no
split), and T1–T2 lean on the false friends: integer division and remainder
with negative numbers, index base, loop bounds, evaluation order and
short-circuiting. Translated by habit, without adapting to the dialect's
semantics, the T1–T4 reference solutions fail in 37–83% of dialects, against
0–52% for T0 (`UTOPIA_TRAPS=1 go test ./internal/tasks -run HabitTraps -v`).

**Release v1** fixes two languages, Reslil (seed 182) and Dushpek (seed 977),
so results are comparable and anyone can reproduce them: run
`harness/run.py --release v1`. A rule that never looks at model results
picked the pair. Between them they flip every false friend.
[releases/v1/](releases/v1/README.md) has the manuals, the rule and how to
verify a result. Fresh seeds remain the contamination-proof check.

**Release v2** keeps v1's two languages and adds the five T3 tasks (22 in
all), because frontier models score 16–17 of 17 on v1 and a small decline
cannot show there. Results also record a partial score: the share of each
task's hidden tests passed, averaged over tasks. Each release pins its tasks
with a checksum. [releases/v2/](releases/v2/README.md) has the details.

**Release v3** adds the three T4 tasks (25 in all), because a frontier
model still scored 22/22 on v2. Checkups use v3.
[releases/v3/](releases/v3/README.md) has the details.

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

Bring an API key and a model name. The harness talks to the Anthropic
Messages API or to any OpenAI-compatible endpoint (OpenAI, OpenRouter,
Together, vLLM, Ollama, ...).

```bash
python3 -m venv .venv && .venv/bin/pip install -r harness/requirements.txt

export ANTHROPIC_API_KEY=...
.venv/bin/python harness/run.py oneshot --arm python                      # control arm
.venv/bin/python harness/run.py oneshot --seeds 1-8 --semantics standard  # new syntax only
.venv/bin/python harness/run.py oneshot --seeds 1-8                       # plus false friends
.venv/bin/python harness/run.py agent --seeds 1,2 --max-cost 10           # full agent runs

# any OpenAI-compatible endpoint
export OPENROUTER_API_KEY=...
.venv/bin/python harness/run.py oneshot --provider openai --base-url https://openrouter.ai/api/v1 \
    --api-key-env OPENROUTER_API_KEY --model some/model --price-in 1 --price-out 4

.venv/bin/python harness/build_site.py                                    # results site in _site/
.venv/bin/python harness/regrade.py results/runs/RUN_ID                  # re-score a saved one-shot answer
```

No API key? Run it through a coding-agent subscription you already have.

**Codex (ChatGPT plan).** If you use Codex in the ChatGPT desktop app, there
is nothing to install or log in to: the harness drives the Codex engine that
ships inside the app, with the app's login. Leave out `--model` to list the
models your plan offers.

```bash
.venv/bin/python harness/run.py oneshot --runner codex --model gpt-6.2-sol --effort high --release v1
.venv/bin/python harness/run.py agent   --runner codex --model gpt-6.2-sol --effort high --release v1
```

**Cursor.** With [Cursor's CLI](https://cursor.com/cli) logged in, any model
your Cursor account offers works, Grok included:

```bash
cursor-agent login                     # once
cursor-agent models                    # pick a name from this list
.venv/bin/python harness/run.py agent --runner cursor --model MODEL --release v1
```

**Claude Code (Claude plan).** Sign the CLI in once with `claude auth login`
(the Claude desktop app's sign-in does not carry over to the CLI).

```bash
.venv/bin/python harness/run.py oneshot --runner claude-code --model claude-opus-5-5 --effort high --release v1
```

**Kimi Code (Kimi plan).** With `kimi login` done, leave out `--model` to use
your default model:

```bash
.venv/bin/python harness/run.py oneshot --runner kimi --effort high --release v1
```

**Gemini CLI (Google subscription).** Install it once
(`npm install -g @google/gemini-cli`), run `gemini` and choose *Sign in with
Google*. `gemini --list-models` shows the models your account offers.

```bash
.venv/bin/python harness/run.py oneshot --runner gemini --model MODEL --release v1
```

**Antigravity CLI (Google subscription).** Google's own agent CLI for the
Gemini models (`agy`). It is not on PATH by default: T3 Code ships a copy,
which the runner finds itself (or set `ANTIGRAVITY_BIN`). Run it once with
no arguments to sign in; `agy models` shows the models your account offers.
Its model names carry the effort (`gemini-4-argon-high`), as Cursor's do.

```bash
.venv/bin/python harness/run.py oneshot --runner antigravity --model gemini-4-neon-high --release v1
```

**OpenCode (Kimi plan, free models).** Models are `provider/model`, as
`opencode models` lists them: a provider you logged in to with
`opencode auth login` (the Kimi plan is `kimi-code-plan-global/...`) or
OpenCode's own free models (`opencode/...`, which have a small free usage
limit). The effort is OpenCode's variant.

```bash
.venv/bin/python harness/run.py oneshot --runner opencode --model kimi-code-plan-global/kimi-for-coding --effort high --release v1
.venv/bin/python harness/run.py oneshot --runner opencode --model opencode/deepseek-v4.1-flash-free --effort high --release v1
```

Every runner does both modes, agent and one-shot. In one-shot mode each tool
gets the same single prompt with its code-running tools off or denied, so a
model that tries to run something fails closed.

### Has my model got worse?

Models behind a subscription can change without notice. `checkup.py` runs a
model on release v3's fixed languages, compares the result with your own
earlier runs of the same setup, and says whether a drop is more than
run-to-run noise (a permutation test on per-run partial scores). The first checkup
is the baseline. It also runs one brand-new language, so a model that has
learned the release itself shows up too.

```bash
.venv/bin/python harness/checkup.py --runner codex --model gpt-6.2-sol --effort high
.venv/bin/python harness/checkup.py --runner codex --model gpt-6.2-sol --effort high --no-run   # report only
```

It runs one-shot by default (one request per language, cheap enough to run
daily); `--mode agent` is slower and closer to everyday use. Runs go one at a
time to stay inside the plan's rate limits. Runs that end in an error (logged
out, quota, rate limit) are left out of the comparison, and the checkup stops
after the first one. The site's "Over time" chart plots the same series by
day.

### Weekly checkup of every subscription

`harness/weekly.py` runs a checkup for every model in
[harness/roster.toml](harness/roster.toml) (one line each: tool, model,
effort, mode, enabled), one at a time, and ends with a status board: this
week's score against the model's own history, the change, the verdict
(worse / within noise / no drop / baseline), the model the tool reported, and
anything skipped. A tool that is logged out or out of quota is marked
*skipped*, not failed, and its error runs never enter the history.

```bash
.venv/bin/python harness/weekly.py --dry-run    # who is logged in, what would run
.venv/bin/python harness/weekly.py              # run it (about 3 requests per model)
.venv/bin/python harness/weekly.py --no-run     # rebuild the board from saved runs
```

Results stay private: runs, logs and the board (`status/latest.html`, `.md`,
`.json`) go to `results/private/` (git-ignored; `--out` or
`UTOPIA_PRIVATE_RESULTS` to move it), never to `results/runs`, which the
public site is built from. Runs already in `results/runs` count as history
but are never written to (`--no-history` to ignore them).

Never read the board across rows. Each tool adds its own system prompt and
tools, so a model is only ever compared with its own earlier runs through the
same tool, effort and mode.

To run it every Sunday at 22:00 (launchd catches up after sleep; `--notify`
shows a macOS notification when a model looks worse):

```bash
.venv/bin/python harness/weekly.py --print-launchd > ~/Library/LaunchAgents/com.utopia.weekly-checkup.plist
launchctl load ~/Library/LaunchAgents/com.utopia.weekly-checkup.plist
```

Gemini is tested through the Antigravity CLI (`agy -p`), or Gemini CLI.
The Antigravity *app*'s headless entry point
(`~/.gemini/antigravity/bin/agentapi`) starts conversations in the running
app with your own settings and permissions and cannot switch its tools off,
so it is not used.

Release v1 is close to the ceiling for frontier models (16–17 of 17), so a
small decline cannot show on it; checkups use v3, which adds the harder T3
and T4 tasks. `weekly.py` takes the release from each entry in `roster.toml`.

Offline self-tests, no key needed:

```bash
python3 harness/run.py oneshot --provider reference --seeds 1-12 --out /tmp/selftest
python3 harness/run.py agent --provider scripted --seeds 1-4 --out /tmp/selftest
```

- **oneshot**: the manual and all tasks in one prompt, no tools. Cheap, and it
  measures pure in-context learning.
- **agent**: the model works in a fresh workspace outside this repo with three
  tools (`run_shell`, `read_file`, `write_file`), the same for every provider.
  File tools are confined to the workspace; shell commands are audited and
  flagged if they reach outside it. Grading rebuilds the toolchain after the
  run, so nothing the agent touched is trusted. Shell commands do run on the
  host, so use a container or VM for models you do not trust.
- `--runner claude-code` runs it as headless Claude Code (`claude -p`), with
  an API key or with the CLI's own login. Your own setup is kept out in both
  cases: `--safe-mode` (no CLAUDE.md, auto-memory, skills, installed plugins,
  hooks, MCP servers or custom agents), no settings files, no slash commands,
  and a cleaned environment, so a `claude` started from inside another Claude
  session does not inherit its variables (`ANTHROPIC_BASE_URL` among them).
  Each run records the tools, skills, plugins, MCP servers and memory Claude
  Code reports and warns about anything unexpected. Agent mode skips
  permission prompts, so the CLI runs in a macOS Seatbelt sandbox
  (`harness/sandbox.py`): writes only in the workspace, Claude Code's own state
  and temp folders, and this repository unreadable. Network is not blocked.
  One-shot mode offers no tools at all and refuses anything that would ask.
- `--runner kimi` runs it as Kimi Code (`kimi -p`), billed to your Kimi plan.
  Each run gets a throwaway HOME and Kimi home with only the login (linked,
  so token refreshes reach your real one), the model, its provider and the
  effort: no permission rules, plugins, MCP servers, AGENTS.md, skills
  (`~/.agents` included) or search and fetch services. Agent mode drops the
  tools that reach outside the workspace and runs in the same Seatbelt
  sandbox; one-shot mode offers no tools. Each run records the model Kimi
  requested, the effort, the tools offered and the model's display name in
  your Kimi catalog (an alias like `kimi-for-coding` can be repointed), and
  Kimi's session log is copied in as `kimi_session.jsonl`.
- `--runner gemini` runs it as Gemini CLI (`gemini -p`), billed to your
  Google subscription through its Google sign-in. Each run gets a throwaway
  HOME whose `~/.gemini` has only the login and a settings file written for
  the run: no GEMINI.md, extensions, MCP servers, hooks, skills (built-in ones
  included), subagents or checkpoints, and Google Cloud variables are removed
  so the personal login is always used. Nothing from the real `~/.gemini`
  (Antigravity's files included) is read. Gemini CLI can switch to another
  model when the requested one is out of quota: each run records the models
  that answered, and a run the requested model did not answer counts as an
  error. Agent mode drops web, ask-user, plan-mode and MCP tools, approves
  everything else, and runs in the Seatbelt sandbox (the CLI's own sandbox is
  off); one-shot mode excludes every tool.
- `--runner antigravity` runs it as the Antigravity CLI (`agy -p`), billed to
  your Google subscription through its own sign-in. Each run gets a throwaway
  HOME, so nothing in `~/.gemini` is read (GEMINI.md, settings, plugins,
  skills, workflows, MCP servers, hooks, memories, the app's settings); only
  the login comes along: the CLI finds your login keychain through
  `$HOME/Library/Keychains`, so that folder is linked (the keychain still
  guards each item). Session settings go in `--settings` and are never saved. Agent mode
  disables web, browser, subagent, image, question and schedule tools, skips
  approvals, and runs in the Seatbelt sandbox (the CLI's own terminal sandbox
  is off); one-shot mode disables every tool. Each run records the models
  that answered; a run the requested model did not answer counts as an
  error. The stream-json events are read defensively: check the first runs'
  transcripts after a CLI update.
- `--runner opencode` runs it as OpenCode (`opencode run`), with the logins
  of your OpenCode setup. Each run gets a throwaway HOME and XDG folders (its
  own config, database and caches) and a private server (`--standalone`)
  instead of your background service. Only the model's provider login is
  copied in (`auth export` piped into `auth import`, in memory). Nothing else
  comes along: no global or project config, AGENTS.md, `~/.claude`
  CLAUDE.md or skills, plugins, MCP servers or saved permissions. Agent mode
  is OpenCode's build agent with web fetch and search, subagents, skills,
  questions and the browser denied, everything else auto-approved (`--auto`),
  in the Seatbelt sandbox; one-shot mode uses an agent whose every
  permission is denied.
- `--runner codex` runs it as Codex (`codex exec`), billed to your ChatGPT
  plan, in agent or one-shot mode. Your own Codex setup is kept out so runs
  stay comparable: config.toml, rules, hooks, memories, plugins, ChatGPT
  apps, skills, browser and computer use, image generation and web search are
  off, and model and effort are always passed explicitly. Each run records
  the model and effort Codex reports, and the tools and instruction blocks the
  model was offered. Agent shell commands run in Codex's workspace-write
  sandbox (no network, writes only in the workspace); one-shot runs in an
  empty read-only folder with the code tool disabled. Codex's session log is
  copied into the run as `codex_session.jsonl` and archived in Codex.
  `CODEX_BIN` points at another copy of Codex (default: the one in the
  ChatGPT app, else `codex` on PATH). Only `--max-seconds` applies, and there
  is no cost estimate unless you pass `--price-in`/`--price-out`.
- `--runner cursor` runs it as Cursor's agent (`cursor-agent -p`), billed to
  your Cursor plan. Shell commands run in Cursor's sandbox: no network, no
  writes outside the workspace and temp folders (reads are not restricted),
  and requests to leave it are rejected and flagged.
  `--cursor-sandbox disabled` turns it off. One-shot runs in an empty folder
  in ask mode, with a permission file that denies shell, reads, writes, web
  fetches and MCP tools; web search needs an approval no one can give.
  Cursor reports tokens but not cost: pass `--price-in`/`--price-out` for an
  estimate. `--max-cost` and `--max-steps` do not apply, only `--max-seconds`.
  Results are labeled "via Cursor", "via Codex" (with the effort) or "via
  Claude Code" on the site, apart from runs of the same model through the
  harness's own loop.
- Limits: `--max-steps`, `--max-cost` (USD, estimated from token usage) and
  `--max-seconds` per run. Effort defaults to `high`; refusal fallbacks are
  off so every answer comes from the model under test.

Keys are read from the environment only. They are stripped from the agent's
shell environment and redacted from everything saved. Each run lands in
`results/runs/RUN_ID/` (scores, usage, cost, prompt, response or transcript,
solutions). Pushing to `main` rebuilds the site and publishes it with Vercel
at https://utopia-benchmark.vercel.app (`vercel.json` runs
`scripts/vercel_build.sh`).

### Layout

- `internal/lang`: AST, and a lexer, parser and printer driven by shape templates
- `internal/gen`: seed to dialect (styles, conlang lexicon, knobs) and the canonical dialect
- `internal/lower`: rewrites canonical programs into any dialect (down to labels and jumps)
- `internal/vm`: bytecode compiler and deterministic VM
- `internal/docs`: the language reference generator
- `tasks/`: tasks, each with a prompt, a canonical reference solution and hidden tests
- `harness/grade.py`: runs solutions against hidden tests
- `harness/run.py`: runs a model (one-shot or agent) and records the result
- `harness/llm.py`: Anthropic and OpenAI-compatible clients, the agent loop and its tools
- `harness/claude_code.py`: optional Claude Code runner
- `harness/cursor_agent.py`: optional Cursor agent runner
- `harness/codex_agent.py`: optional Codex runner (agent and one-shot)
- `harness/kimi_agent.py`: optional Kimi Code runner (agent and one-shot)
- `harness/gemini_agent.py`: optional Gemini CLI runner (agent and one-shot)
- `harness/antigravity_agent.py`: optional Antigravity CLI runner (agent and one-shot)
- `harness/opencode_agent.py`: optional OpenCode runner (agent and one-shot)
- `harness/sandbox.py`: macOS Seatbelt sandbox for the runners without their own
- `harness/checkup.py`: compares a model's new runs with its earlier ones, to catch a model getting worse
- `harness/weekly.py`, `harness/roster.toml`: the weekly checkup of every subscription, and its status board
- `harness/regrade.py`: re-scores saved one-shot answers after a grading fix, without calling a model
- `harness/build_site.py`: builds the static results site from `results/`
- `scripts/make_tests.py`: independent Python references that generate the T1–T2 hidden tests
- `scripts/pick_languages.py`: the rule that picks a release's fixed languages
- `releases/`: published releases (fixed languages and their manuals); `go test` keeps them frozen

`go test ./...` checks that every reference solution passes its tests in
600 generated dialects (the canonical solutions are written once, with
conventional semantics; lowering compensates for index base, loop bounds,
switch fallthrough and division rounding). It also checks that lowered programs round-trip
through the printer and parser, and that the reference renders for every
seed.

See also:

- [docs/design.md](docs/design.md): design notes for v1
- [docs/related-work.md](docs/related-work.md): prior work and how Utopia differs
- [docs/roadmap.md](docs/roadmap.md): from v0 to a public leaderboard

## About

Utopia is an AI-native project: a benchmark designed for AIs, and built
together with AI coding agents.
