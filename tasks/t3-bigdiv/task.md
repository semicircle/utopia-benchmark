# Big division

Standard input contains zero or more lines, each holding two integers `a`
and `b` separated by one space, with `a >= 0` and `b >= 1`. They have at
most 80 and 40 digits, and no leading zeros (except the number 0 itself),
so they can be far too large for the language's integers.

Write a {{.Lang}} program that prints one line for each input line: the
quotient `a / b` rounded down, a space, and the remainder `a - b * (a / b)`,
both written in decimal without leading zeros.

For example, `100 7` gives `14 2`.
