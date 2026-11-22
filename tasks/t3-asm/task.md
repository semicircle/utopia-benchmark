# Register machine

Standard input holds a program for a small machine, one instruction per
line, numbered from 0. The machine has 26 registers named `a` to `z`, each
holding an integer and starting at 0. An instruction is a name and its
operands, separated by single spaces. Below, `r` is a register name and `x`
and `y` are each either a register name (meaning its value) or an integer
literal, which may start with `-`.

| Instruction | Effect |
|---|---|
| `set r x` | `r` becomes `x` |
| `add r x` | `r` becomes `r + x` |
| `sub r x` | `r` becomes `r - x` |
| `mul r x` | `r` becomes `r * x` |
| `div r x` | `r` becomes `r / x`, rounded toward zero |
| `mod r x` | `r` becomes `r - x * (r / x)`, with that same division |
| `jnz x y` | if `x` is not 0, jump `y` instructions forward (backward if `y` is negative) |
| `out x` | print `x` on a line of its own |

Execution starts at instruction 0. After each instruction other than a jump
that is taken, it moves on to the next instruction. A jump of `y` from
instruction `i` goes to instruction `i + y`. The program ends as soon as the
next instruction number is outside the program (below 0, or past the last
instruction).

Two things end it early. If `div` or `mod` would divide by zero, print
`error` and stop, leaving the register unchanged. And count every
instruction executed, taken jumps included: when 10000 instructions have
been executed and the program has not ended, print `timeout` and stop
instead of executing another one. All values stay well within 64-bit range.

Write a {{.Lang}} program that runs the program and prints what it prints.

For example, this program prints `3`, `2` and `1`:

```
set a 3
out a
sub a 1
jnz a -2
```
