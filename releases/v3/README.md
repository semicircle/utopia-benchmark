# Utopia v3

v3 keeps v1's two languages, Reslil (seed 182) and Dushpek (seed 977), and
has 25 tasks: v2's 22 plus three small systems (tier T4). The manuals and
hidden settings here are the same files as in [v1](../v1/README.md).

Why: a frontier model scored 22/22 on v2 in one shot, so v2 still could not
show a decline. The T4 tasks are 300–500 line programs, each a small system
with many rules:

| Task | What it asks |
|---|---|
| `t4-lisp` | an interpreter for a small Lisp: `define`, `lambda` with closures, `let`, `if`, `begin`, lists, and recovery from errors |
| `t4-sheet` | a spreadsheet: formulas with precedence, cell references, ranges, `SUM`/`MIN`/`MAX`, and three kinds of error that spread by severity (cycles, syntax, division by zero) |
| `t4-regex` | a regular-expression matcher: alternation, groups, `*` `+` `?`, classes with ranges and negation, and malformed patterns |

Each T4 task's hidden tests form a ladder: every test file adds one feature
to the ones before (for the Lisp: arithmetic, then definitions, conditions
and recursion, closures, lists, errors, input over several lines). A model
that gets the core right but slips on a later feature still scores partly,
so the partial score falls in steps rather than all at once.

`release.json` lists the tasks and a checksum of their prompts and hidden
tests; `go test ./internal/tasks` fails if any of them changes.

```bash
.venv/bin/python harness/run.py oneshot --release v3 --model MODEL ...
.venv/bin/python harness/checkup.py --model MODEL ...        # checkups use v3
```

The protocol is v1's: up to 64,000 output tokens per request and, in agent
mode, 150 model requests. A one-shot answer to v3 is long (all 25 solutions
in one reply), so a model with a smaller output limit may run out. Results
on v1, v2 and v3 are not comparable with each other.
