Below is the complete reference for Yemora, a programming language you have
never seen before, followed by 17 programming tasks.

Write a Yemora solution for every task. You cannot run any code, so read the
reference carefully: where Yemora differs from languages you know, follow the
reference, not habit. Programs read standard input and write standard
output, and are graded by comparing their output exactly.

Give each solution in exactly this format:

<solution task="TASK-ID">
...Yemora source code...
</solution>


# REFERENCE

# The Yemora Language Reference

Yemora is a small programming language. This reference is complete: it
describes everything the language and its toolchain do. Where Yemora
differs from languages you may know, the difference is deliberate, so follow
this document rather than habit.

Every example in this reference was run with the real toolchain, and the
output shown is exactly what it printed.

## 1. Running programs

Yemora source files use the extension `.yem`. The toolchain is a
single program named `yemora`:

```
yemora run program.yem      # check and run a program
yemora check program.yem    # only check it for errors, without running it
```

A program reads from standard input and writes to standard output. If an
error occurs, `yemora` prints a message to standard error and exits with
status 1. Output printed before the error is kept.

A program may run at most 50,000,000 steps and nest at most 10,000 function
calls. Exceeding either limit is an error.

## 2. Lexical structure

**Layout.** Spaces, tabs, line breaks and indentation have no meaning; use
them freely for readability. A comment starts with `'` and runs to
the end of the line.

**Statement terminator.** Simple statements (declarations, assignments,
calls, printing, jumps, `Omel`, `Kiyetrel`, `Tril`) end with
`;`. Compound statements such as conditionals and loops do not need
one after them, but their syntax is shown in full below.

**Names** of variables, functions and labels are made of letters, digits
and `_`, and must not start with a digit. Names are case-sensitive.

**Keywords** are reserved and cannot be used as names. They are
case-sensitive and must be written exactly as shown:

| Keyword | Meaning |
|---|---|
| `Hemorhor` | part of: do-while loop |
| `Hiyikra` | logical or |
| `Hupo` | part of: if statement |
| `Kiyetrel` | part of: break statement |
| `Krupelro` | the value none |
| `Mushu` | part of: if statement |
| `Omel` | part of: return statement |
| `Opa` | part of: function declaration |
| `Pakru` | part of: switch statement |
| `Pethe` | logical and |
| `Pil` | part of: for loop |
| `Rashar` | part of: print statement |
| `Rokomi` | part of: while loop, do-while loop |
| `Rurmopa` | part of: write statement |
| `Ruyoyo` | part of: function declaration |
| `Sher` | part of: switch statement |
| `Shurisho` | logical not |
| `Tho` | part of: if statement, switch statement |
| `Thotri` | part of: if statement, switch statement |
| `Trepiho` | part of: variable declaration |
| `Tril` | part of: continue statement |
| `Yaki` | the boolean value false |
| `Yeshil` | part of: if statement |
| `Yupu` | the boolean value true |

The builtin function names (section 9) are also reserved.

**Literals.** Integers are written in decimal (`0`, `42`, `1000`); there are
no fractions. A negative number is written with a minus sign (`-5`). Strings
are written between double quotes, such as `"hello"`. Inside a string, `\n`
is a line break, `\t` a tab, `\"` a double quote and `\\` a backslash.
Booleans are `Yupu` and `Yaki`. The value `Krupelro` means "no
value".

## 3. Values

| Type | Examples | Notes |
|---|---|---|
| integer | `0`, `-7`, `123` | 64-bit; overflow wraps around |
| string | `"hi"`, `""` | a sequence of characters; cannot be changed in place |
| boolean | `Yupu`, `Yaki` | the only values allowed as conditions |
| list | `[1, 2, 3]`, `[]`, `["a", 1]` | mutable; may mix types |
| none | `Krupelro` | "no value"; returned by functions that return nothing |

Lists are shared, not copied: assigning a list to another variable, or
passing it to a function, gives access to the same list.

```
Ruyoyo addOne(xs)
    Theki(xs, 1);
Opa

Trepiho mine := [5];
addOne(mine);
Rashar mine;
```

Output:

```
[5, 1]
```

Printing shows integers in decimal, strings without quotes, booleans and
`Krupelro` as their keywords, and lists in brackets with strings quoted.

## 4. Variables and simple statements

A variable must be declared before it is used:

```
Trepiho <name> := <expression>;
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

`Rashar` prints a value followed by a line break. `Rurmopa` prints a
value without a line break.

```
Rashar <expression>;
```

```
Rurmopa <expression>;
```

```
Trepiho x := 5;
x := x + 2;
Trepiho name := "Ada";
Rashar name + " has " + x + " apples";
Trepiho flag := x > 6;
Rashar flag;
Rashar Krupelro;
```

Output:

```
Ada has 7 apples
Yupu
Krupelro
```

## 5. Expressions

### Operators

| Operator | Meaning |
|---|---|
| `-x` | negation |
| `Shurisho x` | logical not |
| `a * b` | multiplication |
| `a / b` | integer division (see below) |
| `a % b` | remainder (see below) |
| `a + b` | addition, or joining text (see below) |
| `a - b` | subtraction |
| `a = b` | equal |
| `a ~= b` | not equal |
| `a < b`, `a <= b`, `a > b`, `a >= b` | ordering |
| `a Pethe b` | logical and |
| `a Hiyikra b` | logical or |

Note the spellings: assignment is `:=` and equality is `=`.

### Grouping and precedence

Operators group the usual mathematical way. From tightest to loosest:
negation and `Shurisho`; then `*`, `/` and `%`; then `+` and `-`; then the comparisons; then
`Pethe`; then `Hiyikra`. Operators of the same level group from left to
right, so `10 - 4 - 3` means `(10 - 4) - 3`. Parentheses group explicitly.

```
Rashar 2 + 3 * 4;
Rashar 10 - 4 - 3;
Rashar (2 + 3) * 4;
Rashar 2 + (3 * 4);
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
Ruyoyo show(x)
    Rashar "evaluating " + x;
    Omel x;
Opa

Rashar show(10) - show(4);
```

Output:

```
evaluating 10
evaluating 4
6
```

Arguments of a function call are evaluated from left to right.

```
Ruyoyo show(x)
    Rashar "evaluating " + x;
    Omel x;
Opa

Ruyoyo pair(a, b)
    Omel Mitrer(a) + b;
Opa

Rashar pair(show(1), show(2));
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
Rashar 7 / 2;
Rashar -7 / 2;
Rashar 7 % 2;
Rashar -7 % 2;
Rashar 6 / 3;
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
Rashar "n = " + 5;
Rashar "a" + "b" + "c";
```

Output:

```
n = 5
abc
```

Strings can be compared with `<`, `<=`, `>` and `>=`, character by character
(by character code). Comparing values of different types with `=` gives
`Yaki`; ordering them is an error.

### Lists and indexing

`x[i]` is element `i` of list `x`, or the one-character string at position
`i` of string `x`. **Indexes start at 0**: the first element
is `x[0]`. List elements can be replaced with `x[i] := value;`.

```
<name>[<index>] := <expression>;
```

```
Trepiho xs := [10, 20, 30];
Rashar xs[1];
xs[1] := 99;
Rashar xs;
Trepiho word := "abc";
Rashar word[1];
```

Output:

```
20
[10, 99, 30]
b
```

Using an index outside the list or string is an error.

**Two lists are equal (`=`) only if they are the very same list.** Two
different lists with the same elements are not equal.

```
Trepiho a := [1, 2];
Trepiho b := [1, 2];
Trepiho c := a;
Theki(c, 3);
Rashar a;
Mushu a = c Yeshil Hupo
    Rashar "a equals c";
Tho
Mushu a = [1, 2, 3] Yeshil Hupo
    Rashar "a equals a new list with the same elements";
Tho Thotri Hupo
    Rashar "a does not equal a new list with the same elements";
Tho
```

Output:

```
[1, 2, 3]
a equals c
a does not equal a new list with the same elements
```

### Logic and conditions

Conditions must be booleans: there is no "truthiness", and using an integer,
string, list or `Krupelro` as a condition is an error. The operands of
`Pethe`, `Hiyikra` and `Shurisho` must also be booleans.

`Pethe` and `Hiyikra` evaluate their right operand only when needed: if the
left operand of `Pethe` is `Yaki`, or the left operand of `Hiyikra`
is `Yupu`, the right operand is not evaluated.

```
Ruyoyo check(name, result)
    Rashar "checking " + name;
    Omel result;
Opa

Mushu check("left", Yupu) Hiyikra check("right", Yaki) Yeshil Hupo
    Rashar "yes";
Tho
Mushu check("left", Yaki) Pethe check("right", Yupu) Yeshil Hupo
    Rashar "yes";
Tho Thotri Hupo
    Rashar "no";
Tho
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
Mushu <condition> Yeshil Hupo
    <statements>
Tho Thotri Mushu <condition> Yeshil Hupo
    <statements>
Tho Thotri Hupo
    <statements>
Tho
```

- The `Thotri Mushu ...` part may appear any number of times, including not at all.
- The `Thotri Hupo ...` part is optional.

The conditions are tested in order, and the statements of the first true
one run. If none is true, the statements of the final branch without a
condition run, if there is one.

```
Trepiho n := 7;
Mushu n < 5 Yeshil Hupo
    Rashar "small";
Tho Thotri Mushu n < 10 Yeshil Hupo
    Rashar "medium";
Tho Thotri Hupo
    Rashar "large";
Tho
```

Output:

```
medium
```

### Choosing by value

```
Pakru Sher <expression>
Sher <literal>, ...
    <statements>
Sher Thotri
    <statements>
Tho Pakru
```

- The `Sher ...` part may appear any number of times, including not at all.
- The `Sher Thotri ...` part is optional.

The expression is evaluated once and compared with each literal in order,
using `=`. Literals are integers or strings, and must all be
different. Only the statements of the matching case run (or the default part,
if none matches and there is one). `Kiyetrel` inside it refers to the enclosing loop, not
to this statement.

```
Pil (Trepiho d := 1; d <= 4; d := d + 1) {
    Pakru Sher d
    Sher 1
        Rashar "one";
    Sher 2, 3
        Rashar "two or three";
    Sher Thotri
        Rashar "something else";
    Tho Pakru
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
Rokomi (<condition>) {
    <statements>
}
```

The condition is tested before each pass; the loop ends when it is
`Yaki`.

```
Trepiho n := 1;
Rokomi (n < 100) {
    n := n * 2;
}
Rashar n;
```

Output:

```
128
```

### Do-while loops

```
Hemorhor {
    <statements>
} Rokomi (<condition>);
```

The statements run once, then again for as long as the condition is
`Yupu`. The condition is tested after each pass.

```
Trepiho n := 0;
Hemorhor {
    n := n + 3;
} Rokomi (n <= 10);
Rashar n;
```

Output:

```
12
```

### For loops

```
Pil (<initializer>; <condition>; <update>) {
    <statements>
}
```

- `<initializer>` and `<update>` are each a declaration or assignment written without the final `;`; either may be left out.

The initializer runs once. Then, while the condition is `Yupu`, the
statements run, followed by the update.

```
Pil (Trepiho i := 0; i < 3; i := i + 1) {
    Rashar i;
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
Kiyetrel;
```

```
Tril;
```

`Kiyetrel` leaves the innermost loop. `Tril` skips to the next pass of
the innermost loop (for a counting or for loop, the update still happens).

```
Pil (Trepiho i := 1; i <= 10; i := i + 1) {
    Mushu i % 2 = 0 Yeshil Hupo
        Tril;
    Tho
    Mushu i > 7 Yeshil Hupo
        Kiyetrel;
    Tho
    Rurmopa i + " ";
}
Rashar "";
```

Output:

```
1 3 5 7 
```

## 7. Functions

```
Ruyoyo <name>(<parameter>, ...)
    <statements>
Opa
```

- The list of parameters may be empty.

Functions are declared at the top level of a program, not inside other
statements, and may be called before their declaration. Calling a function
with the wrong number of arguments is an error. Recursion is allowed.

```
Omel <expression>;
```

- `<expression>` is optional.

`Omel` ends the function and gives back the value, or `Krupelro`
without one. A function that ends without `Omel` returns `Krupelro`.
A `Omel` in top-level code ends the program.

A call can be used as a statement, which discards its result:

```
<function>(<argument>, ...);
```

- The list of arguments may be empty.

```
Ruyoyo square(x)
    Omel x * x;
Opa

Ruyoyo fact(n)
    Mushu n <= 1 Yeshil Hupo
        Omel 1;
    Tho
    Omel n * fact(n - 1);
Opa

Ruyoyo greet(name)
    Rashar "Hello, " + name;
Opa

Rashar square(7);
Rashar fact(10);
greet("Lin");
Trepiho r := greet("Max");
Rashar r;
```

Output:

```
49
3628800
Hello, Lin
Hello, Max
Krupelro
```

## 8. Errors

Errors found before running, such as syntax errors, unknown names and wrong
argument counts, stop the program before anything runs. Errors found while
running stop it at that point. In both cases, the message names the line.

```
Rashar "before";
Rashar 1 / 0;
Rashar "after";
```

Output:

```
before
error: line 2: division by zero
```

## 9. Builtin functions

| Function | Description |
|---|---|
| `Purmo` | `(x)`: the number of elements of list `x`, or the number of characters of string `x`. |
| `Theki` | `(xs, v)`: appends `v` to the end of list `xs` (changing it) and returns `Krupelro`. |
| `Mitrer` | `(v)`: converts any value to the string that printing it would show. |
| `Eshiyer` | `(s)`: converts a string of decimal digits (optionally with a leading `-`, surrounding spaces allowed) to an integer. An integer is returned unchanged. Anything else is an error. |
| `Thoke` | `()`: reads the next line of standard input and returns it as a string without the line ending, or `Krupelro` when there is no more input. |

```
Trepiho xs := [3, 1];
Theki(xs, 4);
Rashar Purmo(xs);
Rashar Purmo("hello");
Rashar Mitrer(42) + "!";
Rashar Eshiyer("12") + 1;
Rashar Thoke();
Rashar Thoke();
Rashar Thoke();
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
Krupelro
```

## 10. A complete program

This program reads integers, one per line, until the input ends, and prints
how many there were, their sum and the largest.

```
Trepiho total := 0;
Trepiho seen := 0;
Trepiho best := 0;
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho n := Eshiyer(line);
    Mushu seen = 0 Yeshil Hupo
        best := n;
    Tho Thotri Mushu n > best Yeshil Hupo
        best := n;
    Tho
    total := total + n;
    seen := seen + 1;
    line := Thoke();
}
Rashar "count " + seen;
Rashar "sum " + total;
Rashar "max " + best;
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

Write a Yemora program that prints the integers from 1 to `n`, one per
line. If `n` is 0, print nothing.


## Task ID: t0-day-names

# Day names

Standard input contains zero or more lines, each holding one integer.

Write a Yemora program that prints one line for each input line: the name
of the day of the week for numbers 1 to 7 (`Monday` for 1, `Tuesday` for 2,
`Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday` for 7), and
`invalid` for any other number.


## Task ID: t0-even-odd

# Even and odd

Standard input contains zero or more lines, each holding one integer
(possibly negative, with absolute value at most 1,000,000).

Write a Yemora program that counts how many of the integers are even and
how many are odd, and prints exactly two lines:

```
even <number of even integers>
odd <number of odd integers>
```


## Task ID: t0-factorial

# Factorial

Standard input contains one line with an integer `n` (0 ≤ n ≤ 20).

Write a Yemora program that prints `n!`, the product of the integers from
1 to `n`. By definition, `0!` is 1.


## Task ID: t0-fizzbuzz

# FizzBuzz

Standard input contains one line with an integer `n` (1 ≤ n ≤ 1000).

Write a Yemora program that prints one line for each integer `i` from 1
to `n`:

- `FizzBuzz` if `i` is divisible by both 3 and 5,
- otherwise `Fizz` if `i` is divisible by 3,
- otherwise `Buzz` if `i` is divisible by 5,
- otherwise the number `i` itself.


## Task ID: t0-hello

# Hello

Write a Yemora program that prints exactly this line:

```
Hello, Utopia!
```


## Task ID: t0-reverse-lines

# Reverse lines

Standard input contains zero or more lines of text.

Write a Yemora program that prints the same lines in reverse order: the
last line first and the first line last. Print each line exactly as it was
read.


## Task ID: t1-digits

# Digits

Standard input contains zero or more lines, each holding one integer `n`
with absolute value at most 10^15.

Write a Yemora program that prints one line for each input line: the sum
of the decimal digits of `n`, a space, and the digits of `n` in reverse order
as an integer. Leading zeros of the reversed number are dropped, and it keeps
the sign of `n` (unless it is 0).

For example, `123` gives `6 321`, `-4500` gives `9 -54`, and `0` gives `0 0`.


## Task ID: t1-floordiv

# Floor division

Standard input contains zero or more lines, each holding two integers `a`
and `b` separated by one space, with absolute values at most 10^9 and
`b` not 0.

Write a Yemora program that prints one line for each input line: `q`, a
space, and `r`, where `q` is `a / b` rounded down (toward negative
infinity) and `r = a - b * q`. So `r` is 0 or has the sign of `b`.

For example, `7 2` gives `3 1`, `-7 2` gives `-4 1`, and `7 -2` gives
`-4 -1`.


## Task ID: t1-palindromes

# Palindromes

Standard input contains zero or more lines of text (printable ASCII
characters).

Write a Yemora program that prints one line for each input line: `yes`
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

Write a Yemora program that prints one line for each query: the number
of integers in the first line that are smaller than the query, a space, and
`found` if the query occurs in the first line or `missing` if it does not.

For example, with the first line `1 3 5 7`, the query `5` gives `2 found`
and the query `4` gives `2 missing`.


## Task ID: t1-rotate

# Rotate

The first line of standard input holds an integer `k` (absolute value at
most 10^9). It is followed by zero or more lines of text, the items.

Write a Yemora program that prints the items rotated right by `k`
places, one per line. Rotating right by one place moves the last item to
the front. A negative `k` rotates left. Print each item exactly as it was
read. If there are no items, print nothing.


## Task ID: t1-weekday

# Weekday

Standard input contains zero or more lines, each holding a date written
`YYYY-MM-DD` (always four digits for the year and two for the month and
day), between `0001-01-01` and `9999-12-31`. Dates follow the Gregorian
calendar, extended backwards to year 1.

Write a Yemora program that prints the day of the week of each date, one
per line: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`,
`Saturday` or `Sunday`.

For example, `2000-01-01` gives `Saturday`.


## Task ID: t2-bignum

# Big numbers

Standard input contains zero or more lines, each holding two non-negative
integers `a` and `b` separated by one space. Each has at most 100 digits and
no leading zeros (except the number 0 itself), so they can be far too large
for the language's integers.

Write a Yemora program that prints one line for each input line: the sum
`a + b`, a space, and the product `a * b`, both written in decimal without
leading zeros.

For example, `999 1` gives `1000 999`.


## Task ID: t2-life

# Life

The first line of standard input holds an integer `g` (0 ≤ g ≤ 30). It is
followed by one or more lines of equal length (at most 20 lines of at most
20 characters), a grid of cells: `#` is a live cell and `.` a dead one.

Write a Yemora program that runs `g` generations of Conway's Game of Life
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

Write a Yemora program that prints one line for each expression: its
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

Write a Yemora program that counts how often each word occurs and prints
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

