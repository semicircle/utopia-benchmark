Below is the complete reference for Tinbousan, a programming language you have
never seen before, followed by 17 programming tasks.

Write a Tinbousan solution for every task. You cannot run any code, so read the
reference carefully: where Tinbousan differs from languages you know, follow the
reference, not habit. Programs read standard input and write standard
output, and are graded by comparing their output exactly.

Give each solution in exactly this format:

<solution task="TASK-ID">
...Tinbousan source code...
</solution>


# REFERENCE

# The Tinbousan Language Reference

Tinbousan is a small programming language. This reference is complete: it
describes everything the language and its toolchain do. Where Tinbousan
differs from languages you may know, the difference is deliberate, so follow
this document rather than habit.

Every example in this reference was run with the real toolchain, and the
output shown is exactly what it printed.

## 1. Running programs

Tinbousan source files use the extension `.tin`. The toolchain is a
single program named `tinbousan`:

```
tinbousan run program.tin      # check and run a program
tinbousan check program.tin    # only check it for errors, without running it
```

A program reads from standard input and writes to standard output. If an
error occurs, `tinbousan` prints a message to standard error and exits with
status 1. Output printed before the error is kept.

A program may run at most 50,000,000 steps and nest at most 10,000 function
calls. Exceeding either limit is an error.

## 2. Lexical structure

**Layout.** Spaces, tabs, line breaks and indentation have no meaning; use
them freely for readability. A comment starts with `//` and runs to
the end of the line.

**Statement terminator.** Simple statements (declarations, assignments,
calls, printing, jumps, `drur`, `basu`, `samu`) end with
`;`. Compound statements such as conditionals and loops do not need
one after them, but their syntax is shown in full below.

**Names** of variables, functions and labels are made of letters, digits
and `_`, and must not start with a digit. Names are case-sensitive.

**Keywords** are reserved and cannot be used as names. They are
case-sensitive and must be written exactly as shown:

| Keyword | Meaning |
|---|---|
| `basu` | part of: break statement |
| `binmi` | part of: print statement |
| `butrouta` | logical or |
| `dra` | logical and |
| `drin` | part of: repeat-until loop |
| `drufirsa` | part of: if statement |
| `drumin` | part of: if statement, function declaration |
| `drur` | part of: return statement |
| `fisu` | part of: if statement |
| `fitru` | part of: switch statement |
| `fufir` | the boolean value false |
| `furfifan` | the value none |
| `moun` | part of: counting loop |
| `samu` | part of: continue statement |
| `sansou` | part of: repeat-until loop |
| `sha` | part of: write statement |
| `shutoun` | logical not |
| `sibitrou` | the boolean value true |
| `sitrartu` | part of: if statement |
| `sou` | part of: counting loop |
| `sourmar` | part of: switch statement |
| `sun` | part of: repeat-until loop |
| `suntru` | part of: counting loop |
| `sutrarsu` | part of: counting loop |
| `tafashou` | part of: while loop |
| `troufu` | part of: variable declaration |
| `tru` | part of: if statement |
| `trushou` | part of: while loop |
| `tumumin` | part of: function declaration |
| `utir` | part of: switch statement |

The builtin function names (section 9) are also reserved.

**Literals.** Integers are written in decimal (`0`, `42`, `1000`); there are
no fractions. A negative number is written with a minus sign (`-5`). Strings
are written between double quotes, such as `"hello"`. Inside a string, `\n`
is a line break, `\t` a tab, `\"` a double quote and `\\` a backslash.
Booleans are `sibitrou` and `fufir`. The value `furfifan` means "no
value".

## 3. Values

| Type | Examples | Notes |
|---|---|---|
| integer | `0`, `-7`, `123` | 64-bit; overflow wraps around |
| string | `"hi"`, `""` | a sequence of characters; cannot be changed in place |
| boolean | `sibitrou`, `fufir` | the only values allowed as conditions |
| list | `[1, 2, 3]`, `[]`, `["a", 1]` | mutable; may mix types |
| none | `furfifan` | "no value"; returned by functions that return nothing |

Lists are shared, not copied: assigning a list to another variable, or
passing it to a function, gives access to the same list.

```
tumumin addOne(xs)
    marboun(xs, 1);
drumin tumumin

troufu mine = [5];
addOne(mine);
binmi mine;
```

Output:

```
[5, 1]
```

Printing shows integers in decimal, strings without quotes, booleans and
`furfifan` as their keywords, and lists in brackets with strings quoted.

## 4. Variables and simple statements

A variable must be declared before it is used:

```
troufu <name> = <expression>;
```

Assignment changes an existing variable. Assigning to a name that was never
declared is an error.

```
<name> = <expression>;
```

Each function has one flat set of variables. A variable declared anywhere in
a function, including inside a loop or a branch, is visible from that point
to the end of the function. Declaring an existing variable again simply
assigns to it. The top-level code of a program has its own variables, which
functions cannot see.

`binmi` prints a value followed by a line break. `sha` prints a
value without a line break.

```
binmi <expression>;
```

```
sha <expression>;
```

```
troufu x = 5;
x = x + 2;
troufu name = "Ada";
binmi name + " has " + x + " apples";
troufu flag = x > 6;
binmi flag;
binmi furfifan;
```

Output:

```
Ada has 7 apples
sibitrou
furfifan
```

## 5. Expressions

### Operators

| Operator | Meaning |
|---|---|
| `-x` | negation |
| `shutoun x` | logical not |
| `a * b` | multiplication |
| `a / b` | integer division (see below) |
| `a % b` | remainder (see below) |
| `a + b` | addition, or joining text (see below) |
| `a - b` | subtraction |
| `a == b` | equal |
| `a ~= b` | not equal |
| `a < b`, `a <= b`, `a > b`, `a >= b` | ordering |
| `a dra b` | logical and |
| `a butrouta b` | logical or |

Note the spellings: assignment is `=` and equality is `==`.

### Grouping and precedence

Operators group the usual mathematical way. From tightest to loosest:
negation and `shutoun`; then `*`, `/` and `%`; then `+` and `-`; then the comparisons; then
`dra`; then `butrouta`. Operators of the same level group from left to
right, so `10 - 4 - 3` means `(10 - 4) - 3`. Parentheses group explicitly.

```
binmi 2 + 3 * 4;
binmi 10 - 4 - 3;
binmi (2 + 3) * 4;
binmi 2 + (3 * 4);
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
tumumin show(x)
    binmi "evaluating " + x;
    drur x;
drumin tumumin

binmi show(10) - show(4);
```

Output:

```
evaluating 10
evaluating 4
6
```

Arguments of a function call are evaluated from left to right.

```
tumumin show(x)
    binmi "evaluating " + x;
    drur x;
drumin tumumin

tumumin pair(a, b)
    drur moufunsa(a) + b;
drumin tumumin

binmi pair(show(1), show(2));
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
binmi 7 / 2;
binmi -7 / 2;
binmi 7 % 2;
binmi -7 % 2;
binmi 6 / 3;
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

`+` adds two integers. If either operand is a string, both operands are
converted to text (as printing would show them) and joined instead. Note that
`1 + 2 + "x"` is `"3x"` but `"x" + 1 + 2` is `"x12"`, following the grouping
rules above.

```
binmi "n = " + 5;
binmi "a" + "b" + "c";
```

Output:

```
n = 5
abc
```

Strings can be compared with `<`, `<=`, `>` and `>=`, character by character
(by character code). Comparing values of different types with `==` gives
`fufir`; ordering them is an error.

### Lists and indexing

`x[i]` is element `i` of list `x`, or the one-character string at position
`i` of string `x`. **Indexes start at 0**: the first element
is `x[0]`. List elements can be replaced with `x[i] = value;`.

```
<name>[<index>] = <expression>;
```

```
troufu xs = [10, 20, 30];
binmi xs[1];
xs[1] = 99;
binmi xs;
troufu word = "abc";
binmi word[1];
```

Output:

```
20
[10, 99, 30]
b
```

Using an index outside the list or string is an error.

Two lists are equal (`==`) when they have the same length and equal
elements.

```
troufu a = [1, 2];
troufu b = [1, 2];
troufu c = a;
marboun(c, 3);
binmi a;
sitrartu a == c fisu drufirsa
    binmi "a equals c";
drumin
sitrartu a == [1, 2, 3] fisu drufirsa
    binmi "a equals a new list with the same elements";
drumin tru drufirsa
    binmi "a does not equal a new list with the same elements";
drumin
```

Output:

```
[1, 2, 3]
a equals c
a equals a new list with the same elements
```

### Logic and conditions

Conditions must be booleans: there is no "truthiness", and using an integer,
string, list or `furfifan` as a condition is an error. The operands of
`dra`, `butrouta` and `shutoun` must also be booleans.

`dra` and `butrouta` evaluate their right operand only when needed: if the
left operand of `dra` is `fufir`, or the left operand of `butrouta`
is `sibitrou`, the right operand is not evaluated.

```
tumumin check(name, result)
    binmi "checking " + name;
    drur result;
drumin tumumin

sitrartu check("left", sibitrou) butrouta check("right", fufir) fisu drufirsa
    binmi "yes";
drumin
sitrartu check("left", fufir) dra check("right", sibitrou) fisu drufirsa
    binmi "yes";
drumin tru drufirsa
    binmi "no";
drumin
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
sitrartu <condition> fisu drufirsa
    <statements>
drumin tru sitrartu <condition> fisu drufirsa
    <statements>
drumin tru drufirsa
    <statements>
drumin
```

- The `tru sitrartu ...` part may appear any number of times, including not at all.
- The `tru drufirsa ...` part is optional.

The conditions are tested in order, and the statements of the first true
one run. If none is true, the statements of the final branch without a
condition run, if there is one.

```
troufu n = 7;
sitrartu n < 5 fisu drufirsa
    binmi "small";
drumin tru sitrartu n < 10 fisu drufirsa
    binmi "medium";
drumin tru drufirsa
    binmi "large";
drumin
```

Output:

```
medium
```

### Choosing by value

```
utir (<expression>) {
sourmar <literal>, ...:
    <statements>
fitru:
    <statements>
}
```

- The `sourmar ...` part may appear any number of times, including not at all.
- The `fitru ...` part is optional.

The expression is evaluated once and compared with each literal in order,
using `==`. Literals are integers or strings, and must all be
different. Only the statements of the matching case run (or the default part
if none matches); execution does not continue into the next case. `basu` inside a case leaves the statement early.

```
sutrarsu d = 1 sou 4
    utir (d) {
    sourmar 1:
        binmi "one";
    sourmar 2, 3:
        binmi "two or three";
    fitru:
        binmi "something else";
    }
moun d
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
tafashou <condition>
    <statements>
trushou
```

The condition is tested before each pass; the loop ends when it is
`fufir`.

```
troufu n = 1;
tafashou n < 100
    n = n * 2;
trushou
binmi n;
```

Output:

```
128
```

### Repeat-until loops

```
sansou
    <statements>
drin sun <condition>
```

The statements run once, then again **until** the condition is `sibitrou`.
The condition is tested after each pass.

```
troufu n = 0;
sansou
    n = n + 3;
drin sun n > 10
binmi n;
```

Output:

```
12
```

### Counting loops

```
sutrarsu <name> = <start> sou <limit> suntru <step>
    <statements>
moun <name>
```

- The `suntru ...` part is optional.
- The name after `moun` must be the loop variable.

The start, limit and step are evaluated once, before the loop begins; the
step defaults to `1` and must not be `0`. The variable starts at the start
value and changes by the step after each pass. The loop runs while the variable has not passed the
limit; **the limit itself is included**.

```
sutrarsu i = 1 sou 5
    sha i + " ";
moun i
binmi "";
sutrarsu i = 10 sou 1 suntru -3
    sha i + " ";
moun i
binmi "";
```

Output:

```
1 2 3 4 5 
10 7 4 1 
```

### Leaving loops early

```
basu;
```

```
samu;
```

`basu` leaves the innermost loop. `samu` skips to the next pass of
the innermost loop (for a counting or for loop, the update still happens).

```
sutrarsu i = 1 sou 10
    sitrartu i % 2 == 0 fisu drufirsa
        samu;
    drumin
    sitrartu i > 7 fisu drufirsa
        basu;
    drumin
    sha i + " ";
moun i
binmi "";
```

Output:

```
1 3 5 7 
```

## 7. Functions

```
tumumin <name>(<parameter>, ...)
    <statements>
drumin tumumin
```

- The list of parameters may be empty.

Functions are declared at the top level of a program, not inside other
statements, and may be called before their declaration. Calling a function
with the wrong number of arguments is an error. Recursion is allowed.

```
drur <expression>;
```

- `<expression>` is optional.

`drur` ends the function and gives back the value, or `furfifan`
without one. A function that ends without `drur` returns `furfifan`.
A `drur` in top-level code ends the program.

A call can be used as a statement, which discards its result:

```
<function>(<argument>, ...);
```

- The list of arguments may be empty.

```
tumumin square(x)
    drur x * x;
drumin tumumin

tumumin fact(n)
    sitrartu n <= 1 fisu drufirsa
        drur 1;
    drumin
    drur n * fact(n - 1);
drumin tumumin

tumumin greet(name)
    binmi "Hello, " + name;
drumin tumumin

binmi square(7);
binmi fact(10);
greet("Lin");
troufu r = greet("Max");
binmi r;
```

Output:

```
49
3628800
Hello, Lin
Hello, Max
furfifan
```

## 8. Errors

Errors found before running, such as syntax errors, unknown names and wrong
argument counts, stop the program before anything runs. Errors found while
running stop it at that point. In both cases, the message names the line.

```
binmi "before";
binmi 1 / 0;
binmi "after";
```

Output:

```
before
error: line 2: division by zero
```

## 9. Builtin functions

| Function | Description |
|---|---|
| `utoufa` | `(x)`: the number of elements of list `x`, or the number of characters of string `x`. |
| `marboun` | `(xs, v)`: appends `v` to the end of list `xs` (changing it) and returns `furfifan`. |
| `moufunsa` | `(v)`: converts any value to the string that printing it would show. |
| `shufa` | `(s)`: converts a string of decimal digits (optionally with a leading `-`, surrounding spaces allowed) to an integer. An integer is returned unchanged. Anything else is an error. |
| `bounfou` | `()`: reads the next line of standard input and returns it as a string without the line ending, or `furfifan` when there is no more input. |

```
troufu xs = [3, 1];
marboun(xs, 4);
binmi utoufa(xs);
binmi utoufa("hello");
binmi moufunsa(42) + "!";
binmi shufa("12") + 1;
binmi bounfou();
binmi bounfou();
binmi bounfou();
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
furfifan
```

## 10. A complete program

This program reads integers, one per line, until the input ends, and prints
how many there were, their sum and the largest.

```
troufu total = 0;
troufu seen = 0;
troufu best = 0;
troufu line = bounfou();
tafashou line ~= furfifan
    troufu n = shufa(line);
    sitrartu seen == 0 fisu drufirsa
        best = n;
    drumin tru sitrartu n > best fisu drufirsa
        best = n;
    drumin
    total = total + n;
    seen = seen + 1;
    line = bounfou();
trushou
binmi "count " + seen;
binmi "sum " + total;
binmi "max " + best;
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

Write a Tinbousan program that prints the integers from 1 to `n`, one per
line. If `n` is 0, print nothing.


## Task ID: t0-day-names

# Day names

Standard input contains zero or more lines, each holding one integer.

Write a Tinbousan program that prints one line for each input line: the name
of the day of the week for numbers 1 to 7 (`Monday` for 1, `Tuesday` for 2,
`Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday` for 7), and
`invalid` for any other number.


## Task ID: t0-even-odd

# Even and odd

Standard input contains zero or more lines, each holding one integer
(possibly negative, with absolute value at most 1,000,000).

Write a Tinbousan program that counts how many of the integers are even and
how many are odd, and prints exactly two lines:

```
even <number of even integers>
odd <number of odd integers>
```


## Task ID: t0-factorial

# Factorial

Standard input contains one line with an integer `n` (0 ≤ n ≤ 20).

Write a Tinbousan program that prints `n!`, the product of the integers from
1 to `n`. By definition, `0!` is 1.


## Task ID: t0-fizzbuzz

# FizzBuzz

Standard input contains one line with an integer `n` (1 ≤ n ≤ 1000).

Write a Tinbousan program that prints one line for each integer `i` from 1
to `n`:

- `FizzBuzz` if `i` is divisible by both 3 and 5,
- otherwise `Fizz` if `i` is divisible by 3,
- otherwise `Buzz` if `i` is divisible by 5,
- otherwise the number `i` itself.


## Task ID: t0-hello

# Hello

Write a Tinbousan program that prints exactly this line:

```
Hello, Utopia!
```


## Task ID: t0-reverse-lines

# Reverse lines

Standard input contains zero or more lines of text.

Write a Tinbousan program that prints the same lines in reverse order: the
last line first and the first line last. Print each line exactly as it was
read.


## Task ID: t1-digits

# Digits

Standard input contains zero or more lines, each holding one integer `n`
with absolute value at most 10^15.

Write a Tinbousan program that prints one line for each input line: the sum
of the decimal digits of `n`, a space, and the digits of `n` in reverse order
as an integer. Leading zeros of the reversed number are dropped, and it keeps
the sign of `n` (unless it is 0).

For example, `123` gives `6 321`, `-4500` gives `9 -54`, and `0` gives `0 0`.


## Task ID: t1-floordiv

# Floor division

Standard input contains zero or more lines, each holding two integers `a`
and `b` separated by one space, with absolute values at most 10^9 and
`b` not 0.

Write a Tinbousan program that prints one line for each input line: `q`, a
space, and `r`, where `q` is `a / b` rounded down (toward negative
infinity) and `r = a - b * q`. So `r` is 0 or has the sign of `b`.

For example, `7 2` gives `3 1`, `-7 2` gives `-4 1`, and `7 -2` gives
`-4 -1`.


## Task ID: t1-palindromes

# Palindromes

Standard input contains zero or more lines of text (printable ASCII
characters).

Write a Tinbousan program that prints one line for each input line: `yes`
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

Write a Tinbousan program that prints one line for each query: the number
of integers in the first line that are smaller than the query, a space, and
`found` if the query occurs in the first line or `missing` if it does not.

For example, with the first line `1 3 5 7`, the query `5` gives `2 found`
and the query `4` gives `2 missing`.


## Task ID: t1-rotate

# Rotate

The first line of standard input holds an integer `k` (absolute value at
most 10^9). It is followed by zero or more lines of text, the items.

Write a Tinbousan program that prints the items rotated right by `k`
places, one per line. Rotating right by one place moves the last item to
the front. A negative `k` rotates left. Print each item exactly as it was
read. If there are no items, print nothing.


## Task ID: t1-weekday

# Weekday

Standard input contains zero or more lines, each holding a date written
`YYYY-MM-DD` (always four digits for the year and two for the month and
day), between `0001-01-01` and `9999-12-31`. Dates follow the Gregorian
calendar, extended backwards to year 1.

Write a Tinbousan program that prints the day of the week of each date, one
per line: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`,
`Saturday` or `Sunday`.

For example, `2000-01-01` gives `Saturday`.


## Task ID: t2-bignum

# Big numbers

Standard input contains zero or more lines, each holding two non-negative
integers `a` and `b` separated by one space. Each has at most 100 digits and
no leading zeros (except the number 0 itself), so they can be far too large
for the language's integers.

Write a Tinbousan program that prints one line for each input line: the sum
`a + b`, a space, and the product `a * b`, both written in decimal without
leading zeros.

For example, `999 1` gives `1000 999`.


## Task ID: t2-life

# Life

The first line of standard input holds an integer `g` (0 ≤ g ≤ 30). It is
followed by one or more lines of equal length (at most 20 lines of at most
20 characters), a grid of cells: `#` is a live cell and `.` a dead one.

Write a Tinbousan program that runs `g` generations of Conway's Game of Life
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

Write a Tinbousan program that prints one line for each expression: its
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

Write a Tinbousan program that counts how often each word occurs and prints
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

