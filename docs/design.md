# Design notes (v1)

Working notes, not a final spec. Everything here is open to change.

## 1. The dialect generator

The heart of Utopia. A single seed produces a complete, self-consistent dialect:

| Output | Examples |
|---|---|
| **Lexicon** | Which word maps to which construct (conlang for *Native*, metaphorical multilingual words for *Babel*) |
| **Semantic knobs** | Evaluation order, integer rounding, index base and wrapping, scoping rules, equality rules, ... |
| **Platform knobs** | Scheduling policy, memory model options, UI layout rules |
| **Errata set** | Which seeded bugs exist in this build of the VM and docs |
| **Docs** | Language reference, platform/OS reference, UI reference, examples |
| **Toolchain** | Compiler and VM configured for the dialect |

Public **practice seeds** let anyone try it. Private **evaluation seeds** are
used for the leaderboard and never published.

### Keyword metaphors (Babel lexicon)

Keywords should be *metaphors* in their source language, not literal
translations, because literal ones collapse to the English concept inside an
LLM. Examples of the idea (not final):

- 縁 (*en*, Japanese: fate, bond) for a channel between households
- *cosecha* (Spanish: harvest) for returning a value
- *saison* (French: season) for a memory region's lifetime

## 2. False friends

Cheap to build and very effective. They look familiar but behave differently,
so following the docs works and pasting from memory fails:

- arguments evaluated right to left
- integer division rounds toward +∞
- indices start at 1 and wrap modulo length
- dynamic scope for one binding form, lexical for another
- identity equality for records, structural equality for lists

Each is a generator knob, so dialects differ in which false friends they have.

## 3. Platform model (candidate)

The platform deliberately avoids mainstream models that models have memorized.

- **Concurrency: synchronous ticks** (Esterel/Lustre style). Logic advances
  in discrete logical instants, so behavior is deterministic. Tuple spaces
  (Linda) are an alternative candidate.
- **Isolation: "households"** instead of processes. They are capability-based
  with no ambient authority, so a household can only touch what it was handed,
  and they talk by sending **"letters"** through the **"post"**.
- **Memory: "seasons"**, which are regions/arenas with lexical lifetimes,
  freed in bulk. Hand-managed pools are an optional hard-mode knob.
- **UI: reactive cell grid**, spreadsheet-like. It is not a widget tree and not
  immediate mode. Rendering is headless (character grid or framebuffer) and
  driven by scripted events, so UI tasks are testable automatically.

## 4. Hard mode and surprises

Painful features live behind knobs, are off by default, and are scored on a
separate tier:

- real priorities, priority inversion, deadlock-prone primitives (RTOS style)
- a reordering optimizer that only respects explicit barriers (DSP style)
- customized fixed-size memory pools exposed to user code

Some knobs can be turned on as hidden **surprises**: not in the docs, but
discoverable by experiment.

## 5. Errata: seeded system bugs

Debugging the platform itself is a core skill under test. Three classes:

1. **Docs silent**: behavior exists but is not documented.
2. **Docs wrong**: the docs say X, and the VM does Y.
3. **VM bug**: an edge case crashes or corrupts state.

Rules:

- Every bug is **deterministic and observable** through a small experiment.
  If finding it needs luck, it's noise.
- Each seed has a hidden **errata ledger**, so scoring can record which bugs
  were found and worked around, not just whether the app passed.

## 6. Tasks

Tiered from small to real:

- **T0**: warm-up programs (the fizzbuzz equivalents of this language)
- **T1**: single-household programs that use the stdlib, seasons and letters
- **T2**: multi-household apps with concurrency
- **T3**: apps with UI on the cell grid
- **T4**: tasks where seeded errata must be found and worked around

Every task has hidden tests and a Python **control** version.

## 7. Constraints

- Docs should fit comfortably in context (roughly 30–50k tokens), so this tests
  in-context learning, not retrieval over a huge manual.
- The VM is deterministic given (seed, inputs).
- Implementation language for the VM and compiler: to be decided (Rust or Go
  are the candidates).
