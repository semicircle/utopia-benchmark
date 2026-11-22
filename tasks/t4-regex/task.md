# Regular expressions

Standard input contains zero or more lines, each holding a pattern, one
space, and a text (which may be empty, in which case the line ends right
after the space). Neither contains spaces.

**Patterns** follow this grammar:

- A pattern is one or more alternatives separated by `|`. An alternative may
  be empty.
- An alternative is a sequence of zero or more pieces.
- A piece is an atom, optionally followed by one quantifier: `*` (zero or
  more), `+` (one or more) or `?` (zero or one).
- An atom is a letter or digit (matching itself), `.` (matching any one
  character), a group `( pattern )`, or a class.
- A class is `[`, an optional `^`, one or more items, and `]`. An item is a
  letter or digit, or a range `x-y` of two letters or digits with `x` not
  after `y` in character order. A class matches one character: one that
  matches any of its items, or with `^`, one that matches none of them.

Anything else is malformed, for example `a**`, `*a`, `(ab`, `[]`, `[z-a]`,
`a{2}` or `a-b`.

Write a {{.Lang}} program that prints one line for each input line: `yes` if
the pattern matches the whole text, `no` if it does not, or `error` if the
pattern is malformed.

For example, `(ab|c)*d` matches `ababcd` and `d` but not `acd`, and
`[a-c]+x?` matches `cabx` but not `cad`.
