Below is the complete reference for Wokluwu, a programming language you have
never seen before, followed by 17 programming tasks.

Write a Wokluwu solution for every task. You cannot run any code, so read the
reference carefully: where Wokluwu differs from languages you know, follow the
reference, not habit. Programs read standard input and write standard
output, and are graded by comparing their output exactly.

Give each solution in exactly this format:

<solution task="TASK-ID">
...Wokluwu source code...
</solution>


# REFERENCE

# The Wokluwu Language Reference

Wokluwu is a small programming language. This reference is complete: it
describes everything the language and its toolchain do. Where Wokluwu
differs from languages you may know, the difference is deliberate, so follow
this document rather than habit.

Every example in this reference was run with the real toolchain, and the
output shown is exactly what it printed.

## 1. Running programs

Wokluwu source files use the extension `.wok`. The toolchain is a
single program named `wokluwu`:

```
wokluwu run program.wok      # check and run a program
wokluwu check program.wok    # only check it for errors, without running it
```

A program reads from standard input and writes to standard output. If an
error occurs, `wokluwu` prints a message to standard error and exits with
status 1. Output printed before the error is kept.

A program may run at most 50,000,000 steps and nest at most 10,000 function
calls. Exceeding either limit is an error.

## 2. Lexical structure

**Layout.** Spaces, tabs, line breaks and indentation have no meaning; use
them freely for readability. A comment starts with `#` and runs to
the end of the line.

**Statement terminator.** Simple statements (declarations, assignments,
calls, printing, jumps, `EFOTU`, `DUTZE`, `DOSHMON`) end with
`;`. Compound statements such as conditionals and loops do not need
one after them, but their syntax is shown in full below.

**Names** of variables, functions and labels are made of letters, digits
and `_`, and must not start with a digit. Names are case-sensitive.

**Keywords** are reserved and cannot be used as names. They are
case-sensitive and must be written exactly as shown:

| Keyword | Meaning |
|---|---|
| `CHEME` | part of: if statement, switch statement |
| `CHU` | part of: switch statement |
| `DEWOTUSH` | part of: if statement |
| `DOSHFETO` | part of: repeat-until loop |
| `DOSHMON` | part of: continue statement |
| `DUDERTE` | part of: repeat-until loop |
| `DUTZE` | part of: break statement |
| `EDEWUT` | part of: function declaration |
| `EFOTU` | part of: return statement |
| `EFUDU` | part of: if statement, switch statement, while loop, counting loop |
| `EPLOWEK` | part of: print statement |
| `FOMOFE` | part of: variable declaration |
| `FUKCHEFE` | part of: while loop |
| `LEKFESH` | part of: if statement, switch statement, while loop, counting loop |
| `LER` | the value none |
| `LERLU` | the boolean value false |
| `LOLO` | part of: while loop, counting loop |
| `MULO` | the boolean value true |
| `MUR` | logical or |
| `PLUWOK` | part of: if statement |
| `TEMO` | logical not |
| `TUTCHEK` | part of: counting loop |
| `WOFE` | part of: write statement |
| `ZEPLO` | part of: counting loop |
| `ZET` | part of: switch statement |
| `ZULUSHTE` | logical and |
| `ZUWOWEN` | part of: counting loop |

The builtin function names (section 9) are also reserved.

**Literals.** Integers are written in decimal (`0`, `42`, `1000`); there are
no fractions. A negative number is written with a minus sign (`-5`). Strings
are written between double quotes, such as `"hello"`. Inside a string, `\n`
is a line break, `\t` a tab, `\"` a double quote and `\\` a backslash.
Booleans are `MULO` and `LERLU`. The value `LER` means "no
value".

## 3. Values

| Type | Examples | Notes |
|---|---|---|
| integer | `0`, `-7`, `123` | 64-bit; overflow wraps around |
| string | `"hi"`, `""` | a sequence of characters; cannot be changed in place |
| boolean | `MULO`, `LERLU` | the only values allowed as conditions |
| list | `[1, 2, 3]`, `[]`, `["a", 1]` | mutable; may mix types |
| none | `LER` | "no value"; returned by functions that return nothing |

Lists are shared, not copied: assigning a list to another variable, or
passing it to a function, gives access to the same list.

```
EDEWUT addOne(xs) {
    WESH(xs, 1);
}

FOMOFE mine := [5];
addOne(mine);
EPLOWEK mine;
```

Output:

```
[5, 1]
```

Printing shows integers in decimal, strings without quotes, booleans and
`LER` as their keywords, and lists in brackets with strings quoted.

## 4. Variables and simple statements

A variable must be declared before it is used:

```
FOMOFE <name> := <expression>;
```

Assignment changes an existing variable. Assigning to a name that was never
declared is an error.

```
<name> := <expression>;
```

Each function has one flat set of variables. A variable declared anywhere in
a function, including inside a loop or a branch, is visible from that point
to the end of the function. Declaring an existing variable again simply
assigns to it. The top-level code of a program has its own variables, which
functions cannot see.

`EPLOWEK` prints a value followed by a line break. `WOFE` prints a
value without a line break.

```
EPLOWEK <expression>;
```

```
WOFE <expression>;
```

```
FOMOFE x := 5;
x := x + 2;
FOMOFE name := "Ada";
EPLOWEK name & " has " & x & " apples";
FOMOFE flag := x > 6;
EPLOWEK flag;
EPLOWEK LER;
```

Output:

```
Ada has 7 apples
MULO
LER
```

## 5. Expressions

### Operators

| Operator | Meaning |
|---|---|
| `-x` | negation |
| `TEMO x` | logical not |
| `a * b` | multiplication |
| `a / b` | integer division (see below) |
| `a % b` | remainder (see below) |
| `a + b` | addition |
| `a - b` | subtraction |
| `a & b` | joining text (see below) |
| `a = b` | equal |
| `a ~= b` | not equal |
| `a < b`, `a <= b`, `a > b`, `a >= b` | ordering |
| `a ZULUSHTE b` | logical and |
| `a MUR b` | logical or |

Note the spellings: assignment is `:=` and equality is `=`.

### Grouping and precedence

Operators group the usual mathematical way. From tightest to loosest:
negation and `TEMO`; then `*`, `/` and `%`; then `+` and `-` and `&`; then the comparisons; then
`ZULUSHTE`; then `MUR`. Operators of the same level group from left to
right, so `10 - 4 - 3` means `(10 - 4) - 3`. Parentheses group explicitly.

```
EPLOWEK 2 + 3 * 4;
EPLOWEK 10 - 4 - 3;
EPLOWEK (2 + 3) * 4;
EPLOWEK 2 + (3 * 4);
```

Output:

```
14
3
20
14
```

### Order of evaluation

The two operands of a binary operator are evaluated left operand first.

```
EDEWUT show(x) {
    EPLOWEK "evaluating " & x;
    EFOTU x;
}

EPLOWEK show(10) - show(4);
```

Output:

```
evaluating 10
evaluating 4
6
```

Arguments of a function call are evaluated from left to right.

```
EDEWUT show(x) {
    EPLOWEK "evaluating " & x;
    EFOTU x;
}

EDEWUT pair(a, b) {
    EFOTU a & b;
}

EPLOWEK pair(show(1), show(2));
```

Output:

```
evaluating 1
evaluating 2
12
```

### Integer arithmetic

Division of integers gives an integer. The exact result is rounded toward zero,
so `7 / 2` is `3` and `-7 / 2` is `-3`. The remainder `a % b` is always `a - b * (a / b)` using that
division, so its sign follows from the rounding rule. Dividing by zero is an
error.

```
EPLOWEK 7 / 2;
EPLOWEK -7 / 2;
EPLOWEK 7 % 2;
EPLOWEK -7 % 2;
EPLOWEK 6 / 3;
```

Output:

```
3
-3
1
-1
2
```

### Text

`&` converts both operands to text (as printing would show them)
and joins them. `+` only adds integers.

```
EPLOWEK "n = " & 5;
EPLOWEK "a" & "b" & "c";
```

Output:

```
n = 5
abc
```

Strings can be compared with `<`, `<=`, `>` and `>=`, character by character
(by character code). Comparing values of different types with `=` gives
`LERLU`; ordering them is an error.

### Lists and indexing

`x[i]` is element `i` of list `x`, or the one-character string at position
`i` of string `x`. **Indexes start at 0**: the first element
is `x[0]`. List elements can be replaced with `x[i] := value;`.

```
<name>[<index>] := <expression>;
```

```
FOMOFE xs := [10, 20, 30];
EPLOWEK xs[1];
xs[1] := 99;
EPLOWEK xs;
FOMOFE word := "abc";
EPLOWEK word[1];
```

Output:

```
20
[10, 99, 30]
b
```

Using an index outside the list or string is an error.

Two lists are equal (`=`) when they have the same length and equal
elements.

```
FOMOFE a := [1, 2];
FOMOFE b := [1, 2];
FOMOFE c := a;
WESH(c, 3);
EPLOWEK a;
PLUWOK a = c DEWOTUSH LEKFESH
    EPLOWEK "a equals c";
EFUDU
PLUWOK a = [1, 2, 3] DEWOTUSH LEKFESH
    EPLOWEK "a equals a new list with the same elements";
EFUDU CHEME LEKFESH
    EPLOWEK "a does not equal a new list with the same elements";
EFUDU
```

Output:

```
[1, 2, 3]
a equals c
a equals a new list with the same elements
```

### Logic and conditions

Conditions must be booleans: there is no "truthiness", and using an integer,
string, list or `LER` as a condition is an error. The operands of
`ZULUSHTE`, `MUR` and `TEMO` must also be booleans.

`ZULUSHTE` and `MUR` evaluate their right operand only when needed: if the
left operand of `ZULUSHTE` is `LERLU`, or the left operand of `MUR`
is `MULO`, the right operand is not evaluated.

```
EDEWUT check(name, result) {
    EPLOWEK "checking " & name;
    EFOTU result;
}

PLUWOK check("left", MULO) MUR check("right", LERLU) DEWOTUSH LEKFESH
    EPLOWEK "yes";
EFUDU
PLUWOK check("left", LERLU) ZULUSHTE check("right", MULO) DEWOTUSH LEKFESH
    EPLOWEK "yes";
EFUDU CHEME LEKFESH
    EPLOWEK "no";
EFUDU
```

Output:

```
checking left
yes
checking left
no
```

## 6. Control flow

### Conditionals

```
PLUWOK <condition> DEWOTUSH LEKFESH
    <statements>
EFUDU CHEME PLUWOK <condition> DEWOTUSH LEKFESH
    <statements>
EFUDU CHEME LEKFESH
    <statements>
EFUDU
```

- The `CHEME PLUWOK ...` part may appear any number of times, including not at all.
- The `CHEME LEKFESH ...` part is optional.

The conditions are tested in order, and the statements of the first true
one run. If none is true, the statements of the final branch without a
condition run, if there is one.

```
FOMOFE n := 7;
PLUWOK n < 5 DEWOTUSH LEKFESH
    EPLOWEK "small";
EFUDU CHEME PLUWOK n < 10 DEWOTUSH LEKFESH
    EPLOWEK "medium";
EFUDU CHEME LEKFESH
    EPLOWEK "large";
EFUDU
```

Output:

```
medium
```

### Choosing by value

```
ZET <expression> CHU
<literal>, ...: LEKFESH
    <statements>
EFUDU
CHEME LEKFESH
    <statements>
EFUDU EFUDU
```

- The `<literal> ...` part may appear any number of times, including not at all.
- The `CHEME LEKFESH ...` part is optional.

The expression is evaluated once and compared with each literal in order,
using `=`. Literals are integers or strings, and must all be
different. Only the statements of the matching case run (or the default part,
if none matches and there is one). `DUTZE` inside it refers to the enclosing loop, not
to this statement.

```
TUTCHEK d := 1 ZUWOWEN 4 LOLO LEKFESH
    ZET d CHU
    1: LEKFESH
        EPLOWEK "one";
    EFUDU
    2, 3: LEKFESH
        EPLOWEK "two or three";
    EFUDU
    CHEME LEKFESH
        EPLOWEK "something else";
    EFUDU EFUDU
EFUDU
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
FUKCHEFE <condition> LOLO LEKFESH
    <statements>
EFUDU
```

The condition is tested before each pass; the loop ends when it is
`LERLU`.

```
FOMOFE n := 1;
FUKCHEFE n < 100 LOLO LEKFESH
    n := n * 2;
EFUDU
EPLOWEK n;
```

Output:

```
128
```

### Repeat-until loops

```
DUDERTE
    <statements>
DOSHFETO <condition>;
```

The statements run once, then again **until** the condition is `MULO`.
The condition is tested after each pass.

```
FOMOFE n := 0;
DUDERTE
    n := n + 3;
DOSHFETO n > 10;
EPLOWEK n;
```

Output:

```
12
```

### Counting loops

```
TUTCHEK <name> := <start> ZUWOWEN <limit> ZEPLO <step> LOLO LEKFESH
    <statements>
EFUDU
```

- The `ZEPLO ...` part is optional.

The start, limit and step are evaluated once, before the loop begins; the
step defaults to `1` and must not be `0`. The variable starts at the start
value and changes by the step after each pass. The loop runs while the variable has not passed the
limit; **the limit itself is included**.

```
TUTCHEK i := 1 ZUWOWEN 5 LOLO LEKFESH
    WOFE i & " ";
EFUDU
EPLOWEK "";
TUTCHEK i := 10 ZUWOWEN 1 ZEPLO -3 LOLO LEKFESH
    WOFE i & " ";
EFUDU
EPLOWEK "";
```

Output:

```
1 2 3 4 5 
10 7 4 1 
```

### Leaving loops early

```
DUTZE;
```

```
DOSHMON;
```

`DUTZE` leaves the innermost loop. `DOSHMON` skips to the next pass of
the innermost loop (for a counting or for loop, the update still happens).

```
TUTCHEK i := 1 ZUWOWEN 10 LOLO LEKFESH
    PLUWOK i % 2 = 0 DEWOTUSH LEKFESH
        DOSHMON;
    EFUDU
    PLUWOK i > 7 DEWOTUSH LEKFESH
        DUTZE;
    EFUDU
    WOFE i & " ";
EFUDU
EPLOWEK "";
```

Output:

```
1 3 5 7 
```

## 7. Functions

```
EDEWUT <name>(<parameter>, ...) {
    <statements>
}
```

- The list of parameters may be empty.

Functions are declared at the top level of a program, not inside other
statements, and may be called before their declaration. Calling a function
with the wrong number of arguments is an error. Recursion is allowed.

```
EFOTU <expression>;
```

- `<expression>` is optional.

`EFOTU` ends the function and gives back the value, or `LER`
without one. A function that ends without `EFOTU` returns `LER`.
A `EFOTU` in top-level code ends the program.

A call can be used as a statement, which discards its result:

```
<function>(<argument>, ...);
```

- The list of arguments may be empty.

```
EDEWUT square(x) {
    EFOTU x * x;
}

EDEWUT fact(n) {
    PLUWOK n <= 1 DEWOTUSH LEKFESH
        EFOTU 1;
    EFUDU
    EFOTU n * fact(n - 1);
}

EDEWUT greet(name) {
    EPLOWEK "Hello, " & name;
}

EPLOWEK square(7);
EPLOWEK fact(10);
greet("Lin");
FOMOFE r := greet("Max");
EPLOWEK r;
```

Output:

```
49
3628800
Hello, Lin
Hello, Max
LER
```

## 8. Errors

Errors found before running, such as syntax errors, unknown names and wrong
argument counts, stop the program before anything runs. Errors found while
running stop it at that point. In both cases, the message names the line.

```
EPLOWEK "before";
EPLOWEK 1 / 0;
EPLOWEK "after";
```

Output:

```
before
error: line 2: division by zero
```

## 9. Builtin functions

| Function | Description |
|---|---|
| `FORMOWE` | `(x)`: the number of elements of list `x`, or the number of characters of string `x`. |
| `WESH` | `(xs, v)`: appends `v` to the end of list `xs` (changing it) and returns `LER`. |
| `ECHEK` | `(v)`: converts any value to the string that printing it would show. |
| `ZENZUMUR` | `(s)`: converts a string of decimal digits (optionally with a leading `-`, surrounding spaces allowed) to an integer. An integer is returned unchanged. Anything else is an error. |
| `TODETET` | `()`: reads the next line of standard input and returns it as a string without the line ending, or `LER` when there is no more input. |

```
FOMOFE xs := [3, 1];
WESH(xs, 4);
EPLOWEK FORMOWE(xs);
EPLOWEK FORMOWE("hello");
EPLOWEK ECHEK(42) & "!";
EPLOWEK ZENZUMUR("12") + 1;
EPLOWEK TODETET();
EPLOWEK TODETET();
EPLOWEK TODETET();
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
LER
```

## 10. A complete program

This program reads integers, one per line, until the input ends, and prints
how many there were, their sum and the largest.

```
FOMOFE total := 0;
FOMOFE seen := 0;
FOMOFE best := 0;
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE n := ZENZUMUR(line);
    PLUWOK seen = 0 DEWOTUSH LEKFESH
        best := n;
    EFUDU CHEME PLUWOK n > best DEWOTUSH LEKFESH
        best := n;
    EFUDU
    total := total + n;
    seen := seen + 1;
    line := TODETET();
EFUDU
EPLOWEK "count " & seen;
EPLOWEK "sum " & total;
EPLOWEK "max " & best;
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

Write a Wokluwu program that prints the integers from 1 to `n`, one per
line. If `n` is 0, print nothing.


## Task ID: t0-day-names

# Day names

Standard input contains zero or more lines, each holding one integer.

Write a Wokluwu program that prints one line for each input line: the name
of the day of the week for numbers 1 to 7 (`Monday` for 1, `Tuesday` for 2,
`Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday` for 7), and
`invalid` for any other number.


## Task ID: t0-even-odd

# Even and odd

Standard input contains zero or more lines, each holding one integer
(possibly negative, with absolute value at most 1,000,000).

Write a Wokluwu program that counts how many of the integers are even and
how many are odd, and prints exactly two lines:

```
even <number of even integers>
odd <number of odd integers>
```


## Task ID: t0-factorial

# Factorial

Standard input contains one line with an integer `n` (0 ≤ n ≤ 20).

Write a Wokluwu program that prints `n!`, the product of the integers from
1 to `n`. By definition, `0!` is 1.


## Task ID: t0-fizzbuzz

# FizzBuzz

Standard input contains one line with an integer `n` (1 ≤ n ≤ 1000).

Write a Wokluwu program that prints one line for each integer `i` from 1
to `n`:

- `FizzBuzz` if `i` is divisible by both 3 and 5,
- otherwise `Fizz` if `i` is divisible by 3,
- otherwise `Buzz` if `i` is divisible by 5,
- otherwise the number `i` itself.


## Task ID: t0-hello

# Hello

Write a Wokluwu program that prints exactly this line:

```
Hello, Utopia!
```


## Task ID: t0-reverse-lines

# Reverse lines

Standard input contains zero or more lines of text.

Write a Wokluwu program that prints the same lines in reverse order: the
last line first and the first line last. Print each line exactly as it was
read.


## Task ID: t1-digits

# Digits

Standard input contains zero or more lines, each holding one integer `n`
with absolute value at most 10^15.

Write a Wokluwu program that prints one line for each input line: the sum
of the decimal digits of `n`, a space, and the digits of `n` in reverse order
as an integer. Leading zeros of the reversed number are dropped, and it keeps
the sign of `n` (unless it is 0).

For example, `123` gives `6 321`, `-4500` gives `9 -54`, and `0` gives `0 0`.


## Task ID: t1-floordiv

# Floor division

Standard input contains zero or more lines, each holding two integers `a`
and `b` separated by one space, with absolute values at most 10^9 and
`b` not 0.

Write a Wokluwu program that prints one line for each input line: `q`, a
space, and `r`, where `q` is `a / b` rounded down (toward negative
infinity) and `r = a - b * q`. So `r` is 0 or has the sign of `b`.

For example, `7 2` gives `3 1`, `-7 2` gives `-4 1`, and `7 -2` gives
`-4 -1`.


## Task ID: t1-palindromes

# Palindromes

Standard input contains zero or more lines of text (printable ASCII
characters).

Write a Wokluwu program that prints one line for each input line: `yes`
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

Write a Wokluwu program that prints one line for each query: the number
of integers in the first line that are smaller than the query, a space, and
`found` if the query occurs in the first line or `missing` if it does not.

For example, with the first line `1 3 5 7`, the query `5` gives `2 found`
and the query `4` gives `2 missing`.


## Task ID: t1-rotate

# Rotate

The first line of standard input holds an integer `k` (absolute value at
most 10^9). It is followed by zero or more lines of text, the items.

Write a Wokluwu program that prints the items rotated right by `k`
places, one per line. Rotating right by one place moves the last item to
the front. A negative `k` rotates left. Print each item exactly as it was
read. If there are no items, print nothing.


## Task ID: t1-weekday

# Weekday

Standard input contains zero or more lines, each holding a date written
`YYYY-MM-DD` (always four digits for the year and two for the month and
day), between `0001-01-01` and `9999-12-31`. Dates follow the Gregorian
calendar, extended backwards to year 1.

Write a Wokluwu program that prints the day of the week of each date, one
per line: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`,
`Saturday` or `Sunday`.

For example, `2000-01-01` gives `Saturday`.


## Task ID: t2-bignum

# Big numbers

Standard input contains zero or more lines, each holding two non-negative
integers `a` and `b` separated by one space. Each has at most 100 digits and
no leading zeros (except the number 0 itself), so they can be far too large
for the language's integers.

Write a Wokluwu program that prints one line for each input line: the sum
`a + b`, a space, and the product `a * b`, both written in decimal without
leading zeros.

For example, `999 1` gives `1000 999`.


## Task ID: t2-life

# Life

The first line of standard input holds an integer `g` (0 ≤ g ≤ 30). It is
followed by one or more lines of equal length (at most 20 lines of at most
20 characters), a grid of cells: `#` is a live cell and `.` a dead one.

Write a Wokluwu program that runs `g` generations of Conway's Game of Life
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

Write a Wokluwu program that prints one line for each expression: its
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

Write a Wokluwu program that counts how often each word occurs and prints
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

