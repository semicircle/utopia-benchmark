# Utopia v2

v2 keeps v1's two languages, Reslil (seed 182) and Dushpek (seed 977), and
adds five harder tasks (tier T3): 22 tasks in all. The manuals and hidden
settings here are the same files as in [v1](../v1/README.md).

Why: frontier models score 16–17 of 17 on v1, so a model that gets a little
worse barely shows. The T3 tasks are longer programs (100–200 lines in the
reference) where the languages' false friends bite in many places at once:

| Task | What it asks | Where the false friends bite |
|---|---|---|
| `t3-calc` | an infix calculator with precedence, unary minus and errors | precedence in your own code, division rounding, bounds checks without short-circuit |
| `t3-maze` | shortest path length and number of shortest paths in a grid | neighbor bounds with wrapping indexes and no short-circuit, index base |
| `t3-bigdiv` | quotient and remainder of numbers up to 80 digits | loop bounds, index base, digit arithmetic |
| `t3-justify` | full text justification | spreading spaces with a division that may round up, loop bounds |
| `t3-asm` | an interpreter for a small register machine | division rounding, relative jumps, a step limit |

A solution written by habit, without adapting to the language, fails in
52–83% of generated languages on these tasks
(`UTOPIA_TRAPS=1 go test ./internal/tasks -run HabitTraps -v`).

Each T3 task has 5–9 hidden test files, one per kind of input, so a partly
right program scores partly: run results record the share of tests passed
as well as the tasks passed.

`release.json` lists the tasks and a checksum of their prompts and hidden
tests; `go test ./internal/tasks` fails if any of them changes.

```bash
.venv/bin/python harness/run.py oneshot --release v2 --model MODEL ...
.venv/bin/python harness/checkup.py --model MODEL ...        # checkups use v2
```

The protocol is v1's: up to 64,000 output tokens per request and, in agent
mode, 150 model requests. Results on v1 and v2 are not comparable with each
other.
