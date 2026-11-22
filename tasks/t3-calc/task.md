# Calculator

Standard input contains zero or more lines, each holding an arithmetic
expression. An expression is built from non-negative integer literals (one
or more digits), the binary operators `+`, `-`, `*`, `/` and `%`, unary
minus `-`, and parentheses. Spaces may appear anywhere between tokens.

The usual rules apply, whatever {{.Lang}} itself does:

- `*`, `/` and `%` bind tighter than `+` and `-`; operators of the same
  level group from left to right, so `10-4-3` is `3` and `100/10/3` is `3`.
- Unary minus binds tighter than every binary operator: `-2*3` is `(-2)*3`,
  `3*-2` is `3*(-2)`, and `--4` is `4`. There is no unary plus.
- Division `/` rounds toward zero, so `-7/2` is `-3`, and `a % b` is
  `a - b * (a / b)` with that division, so `-7%2` is `-1`.

Every value along the way stays well within 64-bit range.

Write a {{.Lang}} program that prints one line for each expression: its
value, or `error` if the line is empty or only spaces, contains any other
character, is not a well-formed expression, or divides or takes a remainder
by zero anywhere.

For example, `2 + 3 * (4 - 6) % 5` gives `1`, and `(1 + 2` gives `error`.
