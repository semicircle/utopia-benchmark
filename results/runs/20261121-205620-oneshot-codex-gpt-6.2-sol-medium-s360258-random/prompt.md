Below is the complete reference for Atpleim, a programming language you have
never seen before, followed by 17 programming tasks.

Write a Atpleim solution for every task. You cannot run any code, so read the
reference carefully: where Atpleim differs from languages you know, follow the
reference, not habit. Programs read standard input and write standard
output, and are graded by comparing their output exactly.

Give each solution in exactly this format:

<solution task="TASK-ID">
...Atpleim source code...
</solution>


# REFERENCE

# The Atpleim Language Reference

Atpleim is a small programming language. This reference is complete: it
describes everything the language and its toolchain do. Where Atpleim
differs from languages you may know, the difference is deliberate, so follow
this document rather than habit.

Every example in this reference was run with the real toolchain, and the
output shown is exactly what it printed.

## 1. Running programs

Atpleim source files use the extension `.atp`. The toolchain is a
single program named `atpleim`:

```
atpleim run program.atp      # check and run a program
atpleim check program.atp    # only check it for errors, without running it
```

A program reads from standard input and writes to standard output. If an
error occurs, `atpleim` prints a message to standard error and exits with
status 1. Output printed before the error is kept.

A program may run at most 50,000,000 steps and nest at most 10,000 function
calls. Exceeding either limit is an error.

## 2. Lexical structure

**Layout.** Spaces, tabs, line breaks and indentation have no meaning; use
them freely for readability. A comment starts with `//` and runs to
the end of the line.

**Statement terminator.** Simple statements (declarations, assignments,
calls, printing, jumps, `Bushayei`, `Kei`, `Sabatchi`) end with
`.`. Compound statements such as conditionals and loops do not need
one after them, but their syntax is shown in full below.

**Names** of variables, functions and labels are made of letters, digits
and `_`, and must not start with a digit. Names are case-sensitive.

**Keywords** are reserved and cannot be used as names. They are
case-sensitive and must be written exactly as shown:

| Keyword | Meaning |
|---|---|
| `Ashes` | part of: for loop |
| `Atbekis` | part of: variable declaration |
| `Bachet` | part of: write statement |
| `Beiplo` | the boolean value false |
| `Bitreim` | part of: while loop, do-while loop |
| `Bushayei` | part of: return statement |
| `Dradesde` | part of: function declaration |
| `Ebakris` | logical not |
| `Kapluda` | the value none |
| `Kei` | part of: break statement |
| `Kekrako` | part of: switch statement, function declaration |
| `Kro` | part of: switch statement, function declaration |
| `Oyatda` | the boolean value true |
| `Sabatchi` | part of: continue statement |
| `Sabei` | part of: switch statement |
| `Seimyu` | part of: print statement |
| `Seshi` | part of: switch statement |
| `Shei` | logical or |
| `Triboba` | part of: switch statement |
| `Ubok` | remainder operator |
| `Umkeim` | part of: conditional jump |
| `Yebu` | logical and |
| `Yohekyo` | part of: do-while loop |
| `Yudrese` | part of: jump |

The builtin function names (section 9) are also reserved.

**Literals.** Integers are written in decimal (`0`, `42`, `1000`); there are
no fractions. A negative number is written with a minus sign (`-5`). Strings
are written between double quotes, such as `"hello"`. Inside a string, `\n`
is a line break, `\t` a tab, `\"` a double quote and `\\` a backslash.
Booleans are `Oyatda` and `Beiplo`. The value `Kapluda` means "no
value".

## 3. Values

| Type | Examples | Notes |
|---|---|---|
| integer | `0`, `-7`, `123` | 64-bit; overflow wraps around |
| string | `"hi"`, `""` | a sequence of characters; cannot be changed in place |
| boolean | `Oyatda`, `Beiplo` | the only values allowed as conditions |
| list | `[1, 2, 3]`, `[]`, `["a", 1]` | mutable; may mix types |
| none | `Kapluda` | "no value"; returned by functions that return nothing |

Lists are shared, not copied: assigning a list to another variable, or
passing it to a function, gives access to the same list.

```
Dradesde addOne(xs) Kro
    Tritriba(xs, 1).
Kekrako

Atbekis mine := [5].
addOne(mine).
Seimyu mine.
```

Output:

```
[5, 1]
```

Printing shows integers in decimal, strings without quotes, booleans and
`Kapluda` as their keywords, and lists in brackets with strings quoted.

## 4. Variables and simple statements

A variable must be declared before it is used:

```
Atbekis <name> := <expression>.
```

Assignment changes an existing variable. Assigning to a name that was never
declared is an error.

```
<name> := <expression>.
```

Each function has one flat set of variables. A variable declared anywhere in
a function, including inside a loop or a branch, is visible from that point
to the end of the function. Declaring an existing variable again simply
assigns to it. The top-level code of a program has its own variables, which
functions cannot see.

`Seimyu` prints a value followed by a line break. `Bachet` prints a
value without a line break.

```
Seimyu <expression>.
```

```
Bachet <expression>.
```

```
Atbekis x := 5.
x := x + 2.
Atbekis name := "Ada".
Seimyu ((name & " has ") & x) & " apples".
Atbekis flag := x > 6.
Seimyu flag.
Seimyu Kapluda.
```

Output:

```
Ada has 7 apples
Oyatda
Kapluda
```

## 5. Expressions

### Operators

| Operator | Meaning |
|---|---|
| `-x` | negation |
| `Ebakris x` | logical not |
| `a * b` | multiplication |
| `a / b` | integer division (see below) |
| `a Ubok b` | remainder (see below) |
| `a + b` | addition |
| `a - b` | subtraction |
| `a & b` | joining text (see below) |
| `a = b` | equal |
| `a != b` | not equal |
| `a < b`, `a <= b`, `a > b`, `a >= b` | ordering |
| `a Yebu b` | logical and |
| `a Shei b` | logical or |

Note the spellings: assignment is `:=` and equality is `=`.

### Grouping and precedence

**All binary operators have the same precedence and group from right to
left.** There is no "multiplication first" rule: `2 * 3 + 4` means
`2 * (3 + 4)`, and `10 - 4 - 3` means `10 - (4 - 3)`. This applies to every
binary operator, including comparisons and `Yebu`/`Shei`, so
`a < b Yebu c < d` means `a < (b Yebu (c < d))`; write
`(a < b) Yebu (c < d)` instead. Negation and `Ebakris` bind tighter than
any binary operator. Parentheses group explicitly.

```
Seimyu 2 + 3 * 4.
Seimyu 10 - 4 - 3.
Seimyu (2 + 3) * 4.
Seimyu 2 + (3 * 4).
```

Output:

```
14
9
20
14
```

### Order of evaluation

The two operands of a binary operator are evaluated left operand first.

```
Dradesde show(x) Kro
    Seimyu "evaluating " & x.
    Bushayei x.
Kekrako

Seimyu show(10) - show(4).
```

Output:

```
evaluating 10
evaluating 4
6
```

Arguments of a function call are evaluated from left to right.

```
Dradesde show(x) Kro
    Seimyu "evaluating " & x.
    Bushayei x.
Kekrako

Dradesde pair(a, b) Kro
    Bushayei a & b.
Kekrako

Seimyu pair(show(1), show(2)).
```

Output:

```
evaluating 1
evaluating 2
12
```

### Integer arithmetic

Division of integers gives an integer. **The exact result is rounded up, toward positive infinity**, so
`7 / 2` is `4` and `-7 / 2` is `-3`. The remainder `a Ubok b` is always `a - b * (a / b)` using that
division, so its sign follows from the rounding rule. Dividing by zero is an
error.

```
Seimyu 7 / 2.
Seimyu -7 / 2.
Seimyu 7 Ubok 2.
Seimyu -7 Ubok 2.
Seimyu 6 / 3.
```

Output:

```
4
-3
-1
-1
2
```

### Text

`&` converts both operands to text (as printing would show them)
and joins them. `+` only adds integers.

```
Seimyu "n = " & 5.
Seimyu "a" & "b" & "c".
```

Output:

```
n = 5
abc
```

Strings can be compared with `<`, `<=`, `>` and `>=`, character by character
(by character code). Comparing values of different types with `=` gives
`Beiplo`; ordering them is an error.

### Lists and indexing

`x[i]` is element `i` of list `x`, or the one-character string at position
`i` of string `x`. **Indexes start at 1**: the first element
is `x[1]`. List elements can be replaced with `x[i] := value.`.

```
<name>[<index>] := <expression>.
```

```
Atbekis xs := [10, 20, 30].
Seimyu xs[1].
xs[1] := 99.
Seimyu xs.
Atbekis word := "abc".
Seimyu word[1].
```

Output:

```
10
[99, 20, 30]
a
```

Using an index outside the list or string is an error.

Two lists are equal (`=`) when they have the same length and equal
elements.

```
Atbekis a := [1, 2].
Atbekis b := [1, 2].
Atbekis c := a.
Tritriba(c, 3).
Seimyu a.
Umkeim a != c, endif1.
Seimyu "a equals c".
endif1:
Umkeim a != [1, 2, 3], else3.
Seimyu "a equals a new list with the same elements".
Yudrese endif2.
else3:
Seimyu "a does not equal a new list with the same elements".
endif2:
```

Output:

```
[1, 2, 3]
a equals c
a equals a new list with the same elements
```

### Logic and conditions

Conditions must be booleans: there is no "truthiness", and using an integer,
string, list or `Kapluda` as a condition is an error. The operands of
`Yebu`, `Shei` and `Ebakris` must also be booleans.

`Yebu` and `Shei` evaluate their right operand only when needed: if the
left operand of `Yebu` is `Beiplo`, or the left operand of `Shei`
is `Oyatda`, the right operand is not evaluated.

```
Dradesde check(name, result) Kro
    Seimyu "checking " & name.
    Bushayei result.
Kekrako

Umkeim Ebakris (check("left", Oyatda) Shei check("right", Beiplo)), endif1.
Seimyu "yes".
endif1:
Umkeim Ebakris (check("left", Beiplo) Yebu check("right", Oyatda)), else3.
Seimyu "yes".
Yudrese endif2.
else3:
Seimyu "no".
endif2:
```

Output:

```
checking left
yes
checking left
no
```

## 6. Control flow

### Choosing by value

```
Sabei <expression> Triboba
<literal>, ...: Kro
    <statements>
Kekrako
Seshi Kro
    <statements>
Kekrako Kekrako
```

- The `<literal> ...` part may appear any number of times, including not at all.
- The `Seshi Kro ...` part is optional.

The expression is evaluated once and compared with each literal in order,
using `=`. Literals are integers or strings, and must all be
different. Only the statements of the matching case run (or the default part,
if none matches and there is one). `Kei` inside it refers to the enclosing loop, not
to this statement.

```
Ashes (Atbekis d := 1; d <= 4; d := d + 1) {
    Sabei d Triboba
    1: Kro
        Seimyu "one".
    Kekrako
    2, 3: Kro
        Seimyu "two or three".
    Kekrako
    Seshi Kro
        Seimyu "something else".
    Kekrako Kekrako
}
```

Output:

```
one
two or three
two or three
something else
```

### While loops

```
Bitreim (<condition>) {
    <statements>
}
```

The condition is tested before each pass; the loop ends when it is
`Beiplo`.

```
Atbekis n := 1.
Bitreim (n < 100) {
    n := n * 2.
}
Seimyu n.
```

Output:

```
128
```

### Do-while loops

```
Yohekyo {
    <statements>
} Bitreim (<condition>).
```

The statements run once, then again for as long as the condition is
`Oyatda`. The condition is tested after each pass.

```
Atbekis n := 0.
Yohekyo {
    n := n + 3.
} Bitreim (n <= 10).
Seimyu n.
```

Output:

```
12
```

### For loops

```
Ashes (<initializer>; <condition>; <update>) {
    <statements>
}
```

- `<initializer>` and `<update>` are each a declaration or assignment written without the final `.`; either may be left out.

The initializer runs once. Then, while the condition is `Oyatda`, the
statements run, followed by the update.

```
Ashes (Atbekis i := 0; i < 3; i := i + 1) {
    Seimyu i.
}
```

Output:

```
0
1
2
```

### Leaving loops early

```
Kei.
```

```
Sabatchi.
```

`Kei` leaves the innermost loop. `Sabatchi` skips to the next pass of
the innermost loop (for a counting or for loop, the update still happens).

```
Dradesde div_(a, b) Kro
    Atbekis q := a / b.
    Atbekis r := a - b * q.
    Umkeim r = 0, endif3.
    Umkeim (r < 0) = a < 0, endif4.
    Umkeim (r < 0) != b < 0, else6.
    q := q + 1.
    Yudrese endif5.
else6:
    q := q - 1.
endif5:
endif4:
endif3:
    Bushayei q.
Kekrako

Dradesde mod_(a, b) Kro
    Bushayei a - b * div_(a, b).
Kekrako

Ashes (Atbekis i := 1; i <= 10; i := i + 1) {
    Umkeim mod_(i, 2) != 0, endif1.
    Sabatchi.
endif1:
    Umkeim i <= 7, endif2.
    Kei.
endif2:
    Bachet i & " ".
}
Seimyu "".
```

Output:

```
1 3 5 7 
```

### Labels and jumps
Atpleim has no if statement; decisions are made with conditional jumps.

A label marks a position in a function. It does not end with `.`:

```
<label>:
```

A jump continues execution at a label in the same function:

```
Yudrese <label>.
```

A conditional jump jumps only if the condition is `Oyatda`; otherwise
execution continues with the next statement:

```
Umkeim <condition>, <label>.
```

Each label name may be defined only once in a function. Jumps may go
forward or backward, and into or out of any block in the same function.

```
Atbekis n := 7.
Umkeim n >= 5, else2.
Seimyu "small".
Yudrese endif1.
else2:
Umkeim n >= 10, else3.
Seimyu "medium".
Yudrese endif1.
else3:
Seimyu "large".
endif1:
```

Output:

```
medium
```

## 7. Functions

```
Dradesde <name>(<parameter>, ...) Kro
    <statements>
Kekrako
```

- The list of parameters may be empty.

Functions are declared at the top level of a program, not inside other
statements, and may be called before their declaration. Calling a function
with the wrong number of arguments is an error. Recursion is allowed.

```
Bushayei <expression>.
```

- `<expression>` is optional.

`Bushayei` ends the function and gives back the value, or `Kapluda`
without one. A function that ends without `Bushayei` returns `Kapluda`.
A `Bushayei` in top-level code ends the program.

A call can be used as a statement, which discards its result:

```
<function>(<argument>, ...).
```

- The list of arguments may be empty.

```
Dradesde square(x) Kro
    Bushayei x * x.
Kekrako

Dradesde fact(n) Kro
    Umkeim n > 1, endif1.
    Bushayei 1.
endif1:
    Bushayei n * fact(n - 1).
Kekrako

Dradesde greet(name) Kro
    Seimyu "Hello, " & name.
Kekrako

Seimyu square(7).
Seimyu fact(10).
greet("Lin").
Atbekis r := greet("Max").
Seimyu r.
```

Output:

```
49
3628800
Hello, Lin
Hello, Max
Kapluda
```

## 8. Errors

Errors found before running, such as syntax errors, unknown names and wrong
argument counts, stop the program before anything runs. Errors found while
running stop it at that point. In both cases, the message names the line.

```
Seimyu "before".
Seimyu 1 / 0.
Seimyu "after".
```

Output:

```
before
error: line 2: division by zero
```

## 9. Builtin functions

| Function | Description |
|---|---|
| `Pluchutde` | `(x)`: the number of elements of list `x`, or the number of characters of string `x`. |
| `Tritriba` | `(xs, v)`: appends `v` to the end of list `xs` (changing it) and returns `Kapluda`. |
| `Chidedo` | `(v)`: converts any value to the string that printing it would show. |
| `Yomheis` | `(s)`: converts a string of decimal digits (optionally with a leading `-`, surrounding spaces allowed) to an integer. An integer is returned unchanged. Anything else is an error. |
| `Ucheschu` | `()`: reads the next line of standard input and returns it as a string without the line ending, or `Kapluda` when there is no more input. |

```
Atbekis xs := [3, 1].
Tritriba(xs, 4).
Seimyu Pluchutde(xs).
Seimyu Pluchutde("hello").
Seimyu Chidedo(42) & "!".
Seimyu Yomheis("12") + 1.
Seimyu Ucheschu().
Seimyu Ucheschu().
Seimyu Ucheschu().
```

Given this standard input:

```
first line
second line
```

Output:

```
3
5
42!
13
first line
second line
Kapluda
```

## 10. A complete program

This program reads integers, one per line, until the input ends, and prints
how many there were, their sum and the largest.

```
Atbekis total := 0.
Atbekis seen := 0.
Atbekis best := 0.
Atbekis line := Ucheschu().
Bitreim (line != Kapluda) {
    Atbekis n := Yomheis(line).
    Umkeim seen != 0, else2.
    best := n.
    Yudrese endif1.
else2:
    Umkeim n <= best, endif1.
    best := n.
endif1:
    total := total + n.
    seen := seen + 1.
    line := Ucheschu().
}
Seimyu "count " & seen.
Seimyu "sum " & total.
Seimyu "max " & best.
```

Given this standard input:

```
4
-2
17
9
```

Output:

```
count 4
sum 28
max 17
```


# TASKS

## Task ID: t0-count

# Count

Standard input contains one line with an integer `n` (0 ≤ n ≤ 1000).

Write a Atpleim program that prints the integers from 1 to `n`, one per
line. If `n` is 0, print nothing.


## Task ID: t0-day-names

# Day names

Standard input contains zero or more lines, each holding one integer.

Write a Atpleim program that prints one line for each input line: the name
of the day of the week for numbers 1 to 7 (`Monday` for 1, `Tuesday` for 2,
`Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday` for 7), and
`invalid` for any other number.


## Task ID: t0-even-odd

# Even and odd

Standard input contains zero or more lines, each holding one integer
(possibly negative, with absolute value at most 1,000,000).

Write a Atpleim program that counts how many of the integers are even and
how many are odd, and prints exactly two lines:

```
even <number of even integers>
odd <number of odd integers>
```


## Task ID: t0-factorial

# Factorial

Standard input contains one line with an integer `n` (0 ≤ n ≤ 20).

Write a Atpleim program that prints `n!`, the product of the integers from
1 to `n`. By definition, `0!` is 1.


## Task ID: t0-fizzbuzz

# FizzBuzz

Standard input contains one line with an integer `n` (1 ≤ n ≤ 1000).

Write a Atpleim program that prints one line for each integer `i` from 1
to `n`:

- `FizzBuzz` if `i` is divisible by both 3 and 5,
- otherwise `Fizz` if `i` is divisible by 3,
- otherwise `Buzz` if `i` is divisible by 5,
- otherwise the number `i` itself.


## Task ID: t0-hello

# Hello

Write a Atpleim program that prints exactly this line:

```
Hello, Utopia!
```


## Task ID: t0-reverse-lines

# Reverse lines

Standard input contains zero or more lines of text.

Write a Atpleim program that prints the same lines in reverse order: the
last line first and the first line last. Print each line exactly as it was
read.


## Task ID: t1-digits

# Digits

Standard input contains zero or more lines, each holding one integer `n`
with absolute value at most 10^15.

Write a Atpleim program that prints one line for each input line: the sum
of the decimal digits of `n`, a space, and the digits of `n` in reverse order
as an integer. Leading zeros of the reversed number are dropped, and it keeps
the sign of `n` (unless it is 0).

For example, `123` gives `6 321`, `-4500` gives `9 -54`, and `0` gives `0 0`.


## Task ID: t1-floordiv

# Floor division

Standard input contains zero or more lines, each holding two integers `a`
and `b` separated by one space, with absolute values at most 10^9 and
`b` not 0.

Write a Atpleim program that prints one line for each input line: `q`, a
space, and `r`, where `q` is `a / b` rounded down (toward negative
infinity) and `r = a - b * q`. So `r` is 0 or has the sign of `b`.

For example, `7 2` gives `3 1`, `-7 2` gives `-4 1`, and `7 -2` gives
`-4 -1`.


## Task ID: t1-palindromes

# Palindromes

Standard input contains zero or more lines of text (printable ASCII
characters).

Write a Atpleim program that prints one line for each input line: `yes`
if the line reads the same forwards and backwards when you keep only its
letters and digits and ignore the difference between upper and lower case
letters, and `no` otherwise. A line with no letters or digits counts as a
palindrome.

For example, `A man, a plan, a canal: Panama!` gives `yes`.


## Task ID: t1-rank

# Rank

The first line of standard input holds zero or more integers in
non-decreasing order, separated by single spaces (at most 1000 of them,
each with absolute value at most 10^6). Each following line holds one
integer, a query.

Write a Atpleim program that prints one line for each query: the number
of integers in the first line that are smaller than the query, a space, and
`found` if the query occurs in the first line or `missing` if it does not.

For example, with the first line `1 3 5 7`, the query `5` gives `2 found`
and the query `4` gives `2 missing`.


## Task ID: t1-rotate

# Rotate

The first line of standard input holds an integer `k` (absolute value at
most 10^9). It is followed by zero or more lines of text, the items.

Write a Atpleim program that prints the items rotated right by `k`
places, one per line. Rotating right by one place moves the last item to
the front. A negative `k` rotates left. Print each item exactly as it was
read. If there are no items, print nothing.


## Task ID: t1-weekday

# Weekday

Standard input contains zero or more lines, each holding a date written
`YYYY-MM-DD` (always four digits for the year and two for the month and
day), between `0001-01-01` and `9999-12-31`. Dates follow the Gregorian
calendar, extended backwards to year 1.

Write a Atpleim program that prints the day of the week of each date, one
per line: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`,
`Saturday` or `Sunday`.

For example, `2000-01-01` gives `Saturday`.


## Task ID: t2-bignum

# Big numbers

Standard input contains zero or more lines, each holding two non-negative
integers `a` and `b` separated by one space. Each has at most 100 digits and
no leading zeros (except the number 0 itself), so they can be far too large
for the language's integers.

Write a Atpleim program that prints one line for each input line: the sum
`a + b`, a space, and the product `a * b`, both written in decimal without
leading zeros.

For example, `999 1` gives `1000 999`.


## Task ID: t2-life

# Life

The first line of standard input holds an integer `g` (0 ≤ g ≤ 30). It is
followed by one or more lines of equal length (at most 20 lines of at most
20 characters), a grid of cells: `#` is a live cell and `.` a dead one.

Write a Atpleim program that runs `g` generations of Conway's Game of Life
on the grid and prints the final grid in the same format. In each
generation, every cell looks at its up to eight neighbours (horizontally,
vertically and diagonally adjacent cells): a live cell with two or three
live neighbours stays alive, a dead cell with exactly three live neighbours
becomes alive, and every other cell is dead in the next generation. All
cells change at the same time. Cells outside the grid are always dead: the
grid does not wrap around.


## Task ID: t2-rpn

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

Write a Atpleim program that prints one line for each expression: its
value, or `error` if the line has no tokens, contains any other token,
applies an operator to fewer than two values, divides or takes a remainder
by zero, or leaves anything other than exactly one value on the stack.

For example, `5 1 2 + 4 * + 3 -` gives `14`.


## Task ID: t2-wordfreq

# Word frequencies

Standard input contains zero or more lines of text (printable ASCII
characters). A word is a maximal run of letters `A`–`Z` and `a`–`z`; every
other character separates words. Upper and lower case count as the same
letter.

Write a Atpleim program that counts how often each word occurs and prints
the ten most frequent words, one per line, as the word in lower case, a
space, and its count. Order them by count, highest first, and words with the
same count alphabetically. If there are fewer than ten distinct words, print
them all.

For example, the input `The cat and THE hat.` gives:

```
the 2
and 1
cat 1
hat 1
```

