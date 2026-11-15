# Related work

A first survey (November 2026). It is not exhaustive.

| Work | What it does | How Utopia differs |
|---|---|---|
| [EsoLang-Bench](https://arxiv.org/abs/2603.09678) (Sharma & Chopra, 2026) | 80 problems in each of 5 existing esolangs (Brainfuck, Befunge-98, Whitespace, Unlambda, Shakespeare). Frontier models score ~100% in Python and 0–11% in esolangs; few-shot prompting and self-reflection don't close the gap. | The closest prior work. Its languages already exist, so they will be in future training data. Its tasks are stdin/stdout algorithms, and the languages are hostile to humans too. Utopia generates a fair language per run, with apps, a platform and UI. |
| [Patel et al.](https://arxiv.org/abs/2311.09635) (NAACL 2024) | In-context learning of new libraries and even new languages from their descriptions. | Confirms that in-context language learning is possible. Utopia makes it a full engineering benchmark. |
| [In-Context Learning for Esoteric Programming Languages](https://openreview.net/forum?id=jdrXx0ReH3) (OpenReview, ~2025) | Minipy, Pyth, Rhokell and 0815, given docs and sparse examples. "Self-scaffolding" raised Pyth accuracy from ~17% to ~31%. | Same direction; Utopia adds generation, a platform and errata. |
| [MTOB](https://arxiv.org/abs/2309.16575) (Tanzer et al., ICLR 2024) | Translate Kalamang (fewer than 200 speakers) from a single grammar book, with a human baseline. | Not code, but the closest in spirit. Utopia borrows the human-baseline idea. |
| [The Larger They Are, the Harder They Fail](https://preview.aclanthology.org/setup/2023.findings-acl.19) (ACL Findings 2023) | Swap Python built-in names and models keep using the original meaning, sometimes more confidently as they get bigger. | Evidence for Utopia's false-friend semantics. |
| [When Names Disappear](https://arxiv.org/abs/2510.03178) (2025) | Studies how much LLMs rely on names rather than structure in code. | Same evidence. |
| [Spaghetti Architect](https://arxiv.org/pdf/2607.18642) (2026) | A generator for contamination-resistant code datasets; argues freshly generated samples are the only durable defense. | Generates samples, not languages. |
| [LiveCodeBench](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf) (ICLR 2025) | Fights contamination by continuously collecting new problems. | Uses mainstream languages. |

## The gap Utopia fills

No work found combines all of these:

- a generated, parametric language, with a new dialect per evaluation run
- a real VM with its own concurrency, isolation, memory and UI model
- app-building tasks, not algorithm puzzles
- seeded, discoverable system bugs and wrong docs
- separate leaderboards for tokenizer fairness
- a human baseline
