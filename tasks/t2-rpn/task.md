# RPN calculator

Standard input contains zero or more lines, each holding an expression in
reverse Polish notation: tokens separated by one or more spaces. A token is
either an integer (an optional `-` followed by one or more digits, such as
`42` or `-7`) or one of the operators `+`, `-`, `*`, `/` and `%`.

Evaluate each expression with a stack: an integer is pushed; an operator
pops the top value `b`, then the next value `a`, and pushes the result of
`a op b`. Division `/` rounds toward zero, so `-7 2 /` is `-3`, and the
remainder `a % b` is `a - b * (a / b)` with that division, so `-7 2 %` is
`-1`. All values stay well within 64-bit range.

Write a {{.Lang}} program that prints one line for each expression: its
value, or `error` if the line has no tokens, contains any other token,
applies an operator to fewer than two values, divides or takes a remainder
by zero, or leaves anything other than exactly one value on the stack.

For example, `5 1 2 + 4 * + 3 -` gives `14`.
