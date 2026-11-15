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

## 4. Platform substrate: many models on one VM

Can one VM support different concurrency and memory models? Yes, within a
range. The VM is an interpreter, so guest threads and guest memory are never
host threads or host memory. They are data structures inside the VM. A
concurrency model is a scheduler policy, and a memory model is an allocator
plus checking rules. Both sit behind narrow interfaces over a fixed core.

### Concurrency: one scheduler core, swappable policies

Every concurrency model reduces to *tasks*, *wait conditions*, *wake-ups* and
*a choice of what runs next*:

```go
type Scheduler interface {
    PickNext(runnable []TaskID, clock Tick) TaskID // seeded, deterministic
    ShouldPreempt(t TaskID, instrsRun int) bool    // checked between instructions
    OnBlock(t TaskID, why WaitCond)
    OnWake(t TaskID)
}
```

| Model | How it maps onto the substrate |
|---|---|
| Synchronous ticks | Every task runs to the tick boundary; signals latch; the clock advances |
| Households + letters (actors) | Task plus mailbox; receiving blocks on "queue not empty" |
| CSP channels | Send and receive block until both sides meet (rendezvous) |
| Linda tuple space | Shared store; `in()` blocks on "a matching tuple exists" |
| RTOS priorities (hard mode) | `PickNext` = highest priority; preempt when a higher one wakes |

Preemption is free because the interpreter decides between instructions, and
every choice is driven by the seed, so runs stay deterministic. This is the
same approach as deterministic concurrency testers such as `loom` and
`shuttle`: a fixed runtime with a pluggable scheduling strategy.

### Memory: handles, not pointers

Guest code only holds **handles** (an object-table index plus a generation
number). A memory model is then a rule for allocating and invalidating them:

| Model | Rule |
|---|---|
| GC heap | Handles never go stale; unreachable objects are collected |
| Seasons (regions) | Objects are tagged with a season; ending it makes all its handles stale |
| Fixed pools (hard mode) | Allocation fails when the pool is at capacity |
| Move / ownership | Sending a letter invalidates the sender's handle |

A stale handle is a deterministic trap, never undefined behavior. That keeps
runs reproducible and gives errata a clean hook (for example, an off-by-one in
season release under a specific condition).

**Weak memory / reordering** (hard mode) fits the same way: give each task a
store buffer, flushed at explicit barriers or by a seeded policy.

### Where the range ends

The VM is not the hard part. These are:

1. **Not every combination is coherent.** Synchronous ticks with reordering
   shared memory, or capability isolation with a global tuple space, make no
   sense together. So models are not independent knobs. They come as a few
   coherent **platform profiles**, and each seed varies *parameters within*
   a profile: letter latency (1 or 2 ticks), delivery order (FIFO or by
   sender), whether seasons nest, and so on.
2. **Every task must be solvable in every profile.** Hidden tests observe only
   outputs (stdout, the UI grid, letters crossing the boundary), never VM
   internals, and each profile needs its own reference solution to prove a
   task is solvable.
3. **Each model needs its own docs chapter template,** and the whole set still
   has to fit the context budget (§8).

### Plan

- **v0/v1:** ship **one** profile (ticks + households + seasons). Novelty comes
  from the lexicon, false friends and parameters within that profile, which is
  already enough to defeat memorization.
- **From day one,** build the VM on `Scheduler` and `Allocator` interfaces so a
  second profile (for example async actors or CSP) can be added later without a
  rewrite.

## 5. Hard mode and surprises

Painful features live behind knobs, are off by default, and are scored on a
separate tier:

- real priorities, priority inversion, deadlock-prone primitives (RTOS style)
- a reordering optimizer that only respects explicit barriers (DSP style)
- customized fixed-size memory pools exposed to user code

Some knobs can be turned on as hidden **surprises**: not in the docs, but
discoverable by experiment.

## 6. Errata: seeded system bugs

Debugging the platform itself is a core skill under test. Three classes:

1. **Docs silent**: behavior exists but is not documented.
2. **Docs wrong**: the docs say X, and the VM does Y.
3. **VM bug**: an edge case crashes or corrupts state.

Rules:

- Every bug is **deterministic and observable** through a small experiment.
  If finding it needs luck, it's noise.
- Each seed has a hidden **errata ledger**, so scoring can record which bugs
  were found and worked around, not just whether the app passed.

## 7. Tasks

Tiered from small to real:

- **T0**: warm-up programs (the fizzbuzz equivalents of this language)
- **T1**: single-household programs that use the stdlib, seasons and letters
- **T2**: multi-household apps with concurrency
- **T3**: apps with UI on the cell grid
- **T4**: tasks where seeded errata must be found and worked around

Every task has hidden tests and a Python **control** version.

## 8. Constraints

- Docs should fit comfortably in context (roughly 30–50k tokens), so this tests
  in-context learning, not retrieval over a huge manual.
- The VM is deterministic given (seed, inputs).

## 9. Implementation stack

**Toolchain (generator, compiler, VM, headless UI): Go.**
**Harness (running models, sandboxes, scoring): Python.**

Why Go for the toolchain:

- **Opaque, per-seed binaries.** The AI under test must not read the VM source,
  or it could read the errata ledger and semantic knobs straight out of it.
  Each evaluation seed is baked into a single static binary (dialect tables
  embedded with `go:embed`) and only that binary goes into the sandbox. Go
  builds in seconds, so a fresh build per seed is cheap.
- **Single static binary, easy cross-compilation.** It drops into any sandbox
  image with no runtime to install.
- **The VM owns concurrency and memory.** Households, ticks and seasons are
  implemented inside the VM as data structures and a seeded scheduler, so the
  host language's own threading and GC don't leak into the semantics. Go's
  simplicity costs nothing here.
- **Easy to read and contribute to,** for humans and AI coding agents alike.

The trade-off is that Go has no sum types, so AST/IR code uses interfaces and
type switches, which is more verbose than Rust's enums and `match`. Speed is
not a concern at benchmark program sizes.

**Determinism rules:** never iterate a Go map where order can affect output
(sort keys, or use ordered structures). All randomness comes from the seed.
No wall-clock time inside the VM; time is logical ticks.

Why Python for the harness: every model provider ships a Python SDK first, and
existing eval frameworks with sandboxed agent support (for example UK AISI's
Inspect) may save most of the harness work. That needs evaluating before we
build our own.
