# Spreadsheet

Standard input holds the cells of a spreadsheet, one per line:
`NAME = FORMULA`, the name and the formula separated by ` = `. A cell name
is a capital letter (the column, `A` to `Z`) followed by a row number from
1 to 99 without leading zeros, such as `B7` or `Z99`. If a name appears more
than once, the last line wins.

**Formulas** are built from integers (one or more digits; leading zeros are
allowed and ignored), cell names, the binary operators `+`, `-`, `*`, `/`
and `%`, unary minus, parentheses and function calls. Spaces may appear
anywhere between tokens. The usual rules apply: `*`, `/` and `%` bind
tighter than `+` and `-`, operators of the same level group from left to
right, and unary minus binds tighter than any binary operator. `/` rounds
toward zero and `a % b` is `a - b * (a / b)`.

The functions are `SUM`, `MIN` and `MAX`, written in capitals, with one or
more arguments separated by commas: `MAX(A1, 3, B2 * 2)`. An argument may
also be a range `X:Y` of two cell names, meaning every cell of the rectangle
with those two corners (in either order), such as `SUM(A1:B3)` or
`MIN(C4:A2)`. Ranges may appear only as function arguments.

A cell that is not given has the value 0. All values stay well within 64-bit
range.

**Values.** A cell's value is an integer or one of three errors:

- `#ERR` if its formula does not follow the rules above (any other character
  or word, a malformed expression, a bad cell name, a misplaced range).
- `#CYCLE` if the cell refers to itself, directly or through other cells.
  A cell refers to every cell named in its formula, including every cell in
  its ranges.
- `#DIV0` if computing its formula divides or takes a remainder by zero.

Errors spread: a cell's value is the most serious of its own error (if any)
and the values of all the cells it refers to, where `#CYCLE` is more serious
than `#ERR`, which is more serious than `#DIV0`. Only a cell with no error
of its own whose referred cells are all integers is computed.

Write a {{.Lang}} program that prints every given cell as `NAME = VALUE`,
one per line, ordered by row number and then by column letter.

For example:

```
A1 = 5
B1 = A1 * 2 + 1
A2 = SUM(A1:B1) / 0
B2 = B2 + 1
```

gives

```
A1 = 5
B1 = 11
A2 = #DIV0
B2 = #CYCLE
```
