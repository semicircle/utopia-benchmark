Below is the complete reference for Wochu, a programming language you have
never seen before, followed by 17 programming tasks.

Write a Wochu solution for every task. You cannot run any code, so read the
reference carefully: where Wochu differs from languages you know, follow the
reference, not habit. Programs read standard input and write standard
output, and are graded by comparing their output exactly.

Give each solution in exactly this format:

<solution task="TASK-ID">
...Wochu source code...
</solution>


# REFERENCE

# The Wochu Language Reference

Wochu is a small programming language. This reference is complete: it
describes everything the language and its toolchain do. Where Wochu
differs from languages you may know, the difference is deliberate, so follow
this document rather than habit.

Every example in this reference was run with the real toolchain, and the
output shown is exactly what it printed.

## 1. Running programs

Wochu source files use the extension `.woc`. The toolchain is a
single program named `wochu`:

```
wochu run program.woc      # check and run a program
wochu check program.woc    # only check it for errors, without running it
```

A program reads from standard input and writes to standard output. If an
error occurs, `wochu` prints a message to standard error and exits with
status 1. Output printed before the error is kept.

A program may run at most 50,000,000 steps and nest at most 10,000 function
calls. Exceeding either limit is an error.

## 2. Lexical structure

**Layout.** Spaces, tabs, line breaks and indentation have no meaning; use
them freely for readability. A comment starts with `--` and runs to
the end of the line.

**Statement terminator.** Simple statements (declarations, assignments,
calls, printing, jumps, `chozulni`, `exzulto`, `weshosho`) end with
`;`. Compound statements such as conditionals and loops do not need
one after them, but their syntax is shown in full below.

**Names** of variables, functions and labels are made of letters, digits
and `_`, and must not start with a digit. Names are case-sensitive.

**Keywords** are reserved and cannot be used as names. They are
case-sensitive and must be written exactly as shown:

| Keyword | Meaning |
|---|---|
| `chozulni` | part of: return statement |
| `dut` | the boolean value true |
| `eikreit` | the boolean value false |
| `eilyot` | part of: function declaration |
| `eixwo` | part of: switch statement |
| `elish` | logical and |
| `exzulto` | part of: break statement |
| `iweil` | part of: function declaration |
| `keit` | part of: for loop |
| `krei` | part of: switch statement |
| `krenul` | part of: while loop, do-while loop |
| `leitchux` | the value none |
| `leshdei` | part of: print statement |
| `nei` | part of: if statement |
| `tilteiyo` | logical not |
| `weltuxle` | part of: variable declaration |
| `weshosho` | part of: continue statement |
| `wogeish` | part of: if statement, switch statement |
| `yeil` | remainder operator |
| `yishzit` | part of: switch statement |
| `yosheil` | logical or |
| `zoltit` | part of: do-while loop |
| `zulkucho` | part of: write statement |
| `zushox` | part of: switch statement |

The builtin function names (section 9) are also reserved.

**Literals.** Integers are written in decimal (`0`, `42`, `1000`); there are
no fractions. A negative number is written with a minus sign (`-5`). Strings
are written between double quotes, such as `"hello"`. Inside a string, `\n`
is a line break, `\t` a tab, `\"` a double quote and `\\` a backslash.
Booleans are `dut` and `eikreit`. The value `leitchux` means "no
value".

## 3. Values

| Type | Examples | Notes |
|---|---|---|
| integer | `0`, `-7`, `123` | 64-bit; overflow wraps around |
| string | `"hi"`, `""` | a sequence of characters; cannot be changed in place |
| boolean | `dut`, `eikreit` | the only values allowed as conditions |
| list | `[1, 2, 3]`, `[]`, `["a", 1]` | mutable; may mix types |
| none | `leitchux` | "no value"; returned by functions that return nothing |

Lists are shared, not copied: assigning a list to another variable, or
passing it to a function, gives access to the same list.

```
eilyot addOne(xs)
    koshkil(xs, 1);
iweil

weltuxle mine := [5];
addOne(mine);
leshdei mine;
```

Output:

```
[5, 1]
```

Printing shows integers in decimal, strings without quotes, booleans and
`leitchux` as their keywords, and lists in brackets with strings quoted.

## 4. Variables and simple statements

A variable must be declared before it is used:

```
weltuxle <name> := <expression>;
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

`leshdei` prints a value followed by a line break. `zulkucho` prints a
value without a line break.

```
leshdei <expression>;
```

```
zulkucho <expression>;
```

```
weltuxle x := 5;
x := x + 2;
weltuxle name := "Ada";
leshdei name + " has " + x + " apples";
weltuxle flag := x > 6;
leshdei flag;
leshdei leitchux;
```

Output:

```
Ada has 7 apples
dut
leitchux
```

## 5. Expressions

### Operators

| Operator | Meaning |
|---|---|
| `-x` | negation |
| `tilteiyo x` | logical not |
| `a * b` | multiplication |
| `a / b` | integer division (see below) |
| `a yeil b` | remainder (see below) |
| `a + b` | addition, or joining text (see below) |
| `a - b` | subtraction |
| `a == b` | equal |
| `a <> b` | not equal |
| `a < b`, `a <= b`, `a > b`, `a >= b` | ordering |
| `a elish b` | logical and |
| `a yosheil b` | logical or |

Note the spellings: assignment is `:=` and equality is `==`. Because `--` starts a comment, write `a - -1` with a
space when subtracting a negative number.

### Grouping and precedence

Operators group the usual mathematical way. From tightest to loosest:
negation and `tilteiyo`; then `*`, `/` and `yeil`; then `+` and `-`; then the comparisons; then
`elish`; then `yosheil`. Operators of the same level group from left to
right, so `10 - 4 - 3` means `(10 - 4) - 3`. Parentheses group explicitly.

```
leshdei 2 + 3 * 4;
leshdei 10 - 4 - 3;
leshdei (2 + 3) * 4;
leshdei 2 + (3 * 4);
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
eilyot show(x)
    leshdei "evaluating " + x;
    chozulni x;
iweil

leshdei show(10) - show(4);
```

Output:

```
evaluating 10
evaluating 4
6
```

Arguments of a function call are evaluated from left to right.

```
eilyot show(x)
    leshdei "evaluating " + x;
    chozulni x;
iweil

eilyot pair(a, b)
    chozulni sheiyidi(a) + b;
iweil

leshdei pair(show(1), show(2));
```

Output:

```
evaluating 1
evaluating 2
12
```

### Integer arithmetic

Division of integers gives an integer. The exact result is rounded toward zero,
so `7 / 2` is `3` and `-7 / 2` is `-3`. The remainder `a yeil b` is always `a - b * (a / b)` using that
division, so its sign follows from the rounding rule. Dividing by zero is an
error.

```
leshdei 7 / 2;
leshdei -7 / 2;
leshdei 7 yeil 2;
leshdei -7 yeil 2;
leshdei 6 / 3;
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
leshdei "n = " + 5;
leshdei "a" + "b" + "c";
```

Output:

```
n = 5
abc
```

Strings can be compared with `<`, `<=`, `>` and `>=`, character by character
(by character code). Comparing values of different types with `==` gives
`eikreit`; ordering them is an error.

### Lists and indexing

`x[i]` is element `i` of list `x`, or the one-character string at position
`i` of string `x`. **Indexes start at 0**: the first element
is `x[0]`. List elements can be replaced with `x[i] := value;`.

```
<name>[<index>] := <expression>;
```

```
weltuxle xs := [10, 20, 30];
leshdei xs[1];
xs[1] := 99;
leshdei xs;
weltuxle word := "abc";
leshdei word[1];
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
weltuxle a := [1, 2];
weltuxle b := [1, 2];
weltuxle c := a;
koshkil(c, 3);
leshdei a;
nei (a == c) {
    leshdei "a equals c";
}
nei (a == [1, 2, 3]) {
    leshdei "a equals a new list with the same elements";
} wogeish {
    leshdei "a does not equal a new list with the same elements";
}
```

Output:

```
[1, 2, 3]
a equals c
a equals a new list with the same elements
```

### Logic and conditions

Conditions must be booleans: there is no "truthiness", and using an integer,
string, list or `leitchux` as a condition is an error. The operands of
`elish`, `yosheil` and `tilteiyo` must also be booleans.

`elish` and `yosheil` evaluate their right operand only when needed: if the
left operand of `elish` is `eikreit`, or the left operand of `yosheil`
is `dut`, the right operand is not evaluated.

```
eilyot check(name, result)
    leshdei "checking " + name;
    chozulni result;
iweil

nei (check("left", dut) yosheil check("right", eikreit)) {
    leshdei "yes";
}
nei (check("left", eikreit) elish check("right", dut)) {
    leshdei "yes";
} wogeish {
    leshdei "no";
}
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
nei (<condition>) {
    <statements>
} wogeish nei (<condition>) {
    <statements>
} wogeish {
    <statements>
}
```

- The `wogeish nei ...` part may appear any number of times, including not at all.
- The `wogeish ...` part is optional.

The conditions are tested in order, and the statements of the first true
one run. If none is true, the statements of the final branch without a
condition run, if there is one.

```
weltuxle n := 7;
nei (n < 5) {
    leshdei "small";
} wogeish nei (n < 10) {
    leshdei "medium";
} wogeish {
    leshdei "large";
}
```

Output:

```
medium
```

### Choosing by value

```
yishzit <expression> eixwo
<literal>, ...: krei
    <statements>
zushox
wogeish krei
    <statements>
zushox zushox
```

- The `<literal> ...` part may appear any number of times, including not at all.
- The `wogeish krei ...` part is optional.

The expression is evaluated once and compared with each literal in order,
using `==`. Literals are integers or strings, and must all be
different. Only the statements of the matching case run (or the default part,
if none matches and there is one). `exzulto` inside it refers to the enclosing loop, not
to this statement.

```
keit (weltuxle d := 1; d <= 4; d := d + 1) {
    yishzit d eixwo
    1: krei
        leshdei "one";
    zushox
    2, 3: krei
        leshdei "two or three";
    zushox
    wogeish krei
        leshdei "something else";
    zushox zushox
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
krenul (<condition>) {
    <statements>
}
```

The condition is tested before each pass; the loop ends when it is
`eikreit`.

```
weltuxle n := 1;
krenul (n < 100) {
    n := n * 2;
}
leshdei n;
```

Output:

```
128
```

### Do-while loops

```
zoltit {
    <statements>
} krenul (<condition>);
```

The statements run once, then again for as long as the condition is
`dut`. The condition is tested after each pass.

```
weltuxle n := 0;
zoltit {
    n := n + 3;
} krenul (n <= 10);
leshdei n;
```

Output:

```
12
```

### For loops

```
keit (<initializer>; <condition>; <update>) {
    <statements>
}
```

- `<initializer>` and `<update>` are each a declaration or assignment written without the final `;`; either may be left out.

The initializer runs once. Then, while the condition is `dut`, the
statements run, followed by the update.

```
keit (weltuxle i := 0; i < 3; i := i + 1) {
    leshdei i;
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
exzulto;
```

```
weshosho;
```

`exzulto` leaves the innermost loop. `weshosho` skips to the next pass of
the innermost loop (for a counting or for loop, the update still happens).

```
keit (weltuxle i := 1; i <= 10; i := i + 1) {
    nei (i yeil 2 == 0) {
        weshosho;
    }
    nei (i > 7) {
        exzulto;
    }
    zulkucho i + " ";
}
leshdei "";
```

Output:

```
1 3 5 7 
```

## 7. Functions

```
eilyot <name>(<parameter>, ...)
    <statements>
iweil
```

- The list of parameters may be empty.

Functions are declared at the top level of a program, not inside other
statements, and may be called before their declaration. Calling a function
with the wrong number of arguments is an error. Recursion is allowed.

```
chozulni <expression>;
```

- `<expression>` is optional.

`chozulni` ends the function and gives back the value, or `leitchux`
without one. A function that ends without `chozulni` returns `leitchux`.
A `chozulni` in top-level code ends the program.

A call can be used as a statement, which discards its result:

```
<function>(<argument>, ...);
```

- The list of arguments may be empty.

```
eilyot square(x)
    chozulni x * x;
iweil

eilyot fact(n)
    nei (n <= 1) {
        chozulni 1;
    }
    chozulni n * fact(n - 1);
iweil

eilyot greet(name)
    leshdei "Hello, " + name;
iweil

leshdei square(7);
leshdei fact(10);
greet("Lin");
weltuxle r := greet("Max");
leshdei r;
```

Output:

```
49
3628800
Hello, Lin
Hello, Max
leitchux
```

## 8. Errors

Errors found before running, such as syntax errors, unknown names and wrong
argument counts, stop the program before anything runs. Errors found while
running stop it at that point. In both cases, the message names the line.

```
leshdei "before";
leshdei 1 / 0;
leshdei "after";
```

Output:

```
before
error: line 2: division by zero
```

## 9. Builtin functions

| Function | Description |
|---|---|
| `dushzosh` | `(x)`: the number of elements of list `x`, or the number of characters of string `x`. |
| `koshkil` | `(xs, v)`: appends `v` to the end of list `xs` (changing it) and returns `leitchux`. |
| `sheiyidi` | `(v)`: converts any value to the string that printing it would show. |
| `leidush` | `(s)`: converts a string of decimal digits (optionally with a leading `-`, surrounding spaces allowed) to an integer. An integer is returned unchanged. Anything else is an error. |
| `lono` | `()`: reads the next line of standard input and returns it as a string without the line ending, or `leitchux` when there is no more input. |

```
weltuxle xs := [3, 1];
koshkil(xs, 4);
leshdei dushzosh(xs);
leshdei dushzosh("hello");
leshdei sheiyidi(42) + "!";
leshdei leidush("12") + 1;
leshdei lono();
leshdei lono();
leshdei lono();
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
leitchux
```

## 10. A complete program

This program reads integers, one per line, until the input ends, and prints
how many there were, their sum and the largest.

```
weltuxle total := 0;
weltuxle seen := 0;
weltuxle best := 0;
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle n := leidush(line);
    nei (seen == 0) {
        best := n;
    } wogeish nei (n > best) {
        best := n;
    }
    total := total + n;
    seen := seen + 1;
    line := lono();
}
leshdei "count " + seen;
leshdei "sum " + total;
leshdei "max " + best;
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

Write a Wochu program that prints the integers from 1 to `n`, one per
line. If `n` is 0, print nothing.


## Task ID: t0-day-names

# Day names

Standard input contains zero or more lines, each holding one integer.

Write a Wochu program that prints one line for each input line: the name
of the day of the week for numbers 1 to 7 (`Monday` for 1, `Tuesday` for 2,
`Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday` for 7), and
`invalid` for any other number.


## Task ID: t0-even-odd

# Even and odd

Standard input contains zero or more lines, each holding one integer
(possibly negative, with absolute value at most 1,000,000).

Write a Wochu program that counts how many of the integers are even and
how many are odd, and prints exactly two lines:

```
even <number of even integers>
odd <number of odd integers>
```


## Task ID: t0-factorial

# Factorial

Standard input contains one line with an integer `n` (0 ≤ n ≤ 20).

Write a Wochu program that prints `n!`, the product of the integers from
1 to `n`. By definition, `0!` is 1.


## Task ID: t0-fizzbuzz

# FizzBuzz

Standard input contains one line with an integer `n` (1 ≤ n ≤ 1000).

Write a Wochu program that prints one line for each integer `i` from 1
to `n`:

- `FizzBuzz` if `i` is divisible by both 3 and 5,
- otherwise `Fizz` if `i` is divisible by 3,
- otherwise `Buzz` if `i` is divisible by 5,
- otherwise the number `i` itself.


## Task ID: t0-hello

# Hello

Write a Wochu program that prints exactly this line:

```
Hello, Utopia!
```


## Task ID: t0-reverse-lines

# Reverse lines

Standard input contains zero or more lines of text.

Write a Wochu program that prints the same lines in reverse order: the
last line first and the first line last. Print each line exactly as it was
read.


## Task ID: t1-digits

# Digits

Standard input contains zero or more lines, each holding one integer `n`
with absolute value at most 10^15.

Write a Wochu program that prints one line for each input line: the sum
of the decimal digits of `n`, a space, and the digits of `n` in reverse order
as an integer. Leading zeros of the reversed number are dropped, and it keeps
the sign of `n` (unless it is 0).

For example, `123` gives `6 321`, `-4500` gives `9 -54`, and `0` gives `0 0`.


## Task ID: t1-floordiv

# Floor division

Standard input contains zero or more lines, each holding two integers `a`
and `b` separated by one space, with absolute values at most 10^9 and
`b` not 0.

Write a Wochu program that prints one line for each input line: `q`, a
space, and `r`, where `q` is `a / b` rounded down (toward negative
infinity) and `r = a - b * q`. So `r` is 0 or has the sign of `b`.

For example, `7 2` gives `3 1`, `-7 2` gives `-4 1`, and `7 -2` gives
`-4 -1`.


## Task ID: t1-palindromes

# Palindromes

Standard input contains zero or more lines of text (printable ASCII
characters).

Write a Wochu program that prints one line for each input line: `yes`
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

Write a Wochu program that prints one line for each query: the number
of integers in the first line that are smaller than the query, a space, and
`found` if the query occurs in the first line or `missing` if it does not.

For example, with the first line `1 3 5 7`, the query `5` gives `2 found`
and the query `4` gives `2 missing`.


## Task ID: t1-rotate

# Rotate

The first line of standard input holds an integer `k` (absolute value at
most 10^9). It is followed by zero or more lines of text, the items.

Write a Wochu program that prints the items rotated right by `k`
places, one per line. Rotating right by one place moves the last item to
the front. A negative `k` rotates left. Print each item exactly as it was
read. If there are no items, print nothing.


## Task ID: t1-weekday

# Weekday

Standard input contains zero or more lines, each holding a date written
`YYYY-MM-DD` (always four digits for the year and two for the month and
day), between `0001-01-01` and `9999-12-31`. Dates follow the Gregorian
calendar, extended backwards to year 1.

Write a Wochu program that prints the day of the week of each date, one
per line: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`,
`Saturday` or `Sunday`.

For example, `2000-01-01` gives `Saturday`.


## Task ID: t2-bignum

# Big numbers

Standard input contains zero or more lines, each holding two non-negative
integers `a` and `b` separated by one space. Each has at most 100 digits and
no leading zeros (except the number 0 itself), so they can be far too large
for the language's integers.

Write a Wochu program that prints one line for each input line: the sum
`a + b`, a space, and the product `a * b`, both written in decimal without
leading zeros.

For example, `999 1` gives `1000 999`.


## Task ID: t2-life

# Life

The first line of standard input holds an integer `g` (0 ≤ g ≤ 30). It is
followed by one or more lines of equal length (at most 20 lines of at most
20 characters), a grid of cells: `#` is a live cell and `.` a dead one.

Write a Wochu program that runs `g` generations of Conway's Game of Life
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

Write a Wochu program that prints one line for each expression: its
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

Write a Wochu program that counts how often each word occurs and prints
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

