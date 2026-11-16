# Floor division

Standard input contains zero or more lines, each holding two integers `a`
and `b` separated by one space, with absolute values at most 10^9 and
`b` not 0.

Write a {{.Lang}} program that prints one line for each input line: `q`, a
space, and `r`, where `q` is `a / b` rounded down (toward negative
infinity) and `r = a - b * q`. So `r` is 0 or has the sign of `b`.

For example, `7 2` gives `3 1`, `-7 2` gives `-4 1`, and `7 -2` gives
`-4 -1`.
