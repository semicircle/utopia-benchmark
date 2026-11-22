Below is the complete reference for Reslil, a programming language you have
never seen before, followed by 25 programming tasks.

Write a Reslil solution for every task. You cannot run any code, so read the
reference carefully: where Reslil differs from languages you know, follow the
reference, not habit. Programs read standard input and write standard
output, and are graded by comparing their output exactly.

Give each solution in exactly this format:

<solution task="TASK-ID">
...Reslil source code...
</solution>


# REFERENCE

# The Reslil Language Reference

Reslil is a small programming language. This reference is complete: it
describes everything the language and its toolchain do. Where Reslil
differs from languages you may know, the difference is deliberate, so follow
this document rather than habit.

Every example in this reference was run with the real toolchain, and the
output shown is exactly what it printed.

## 1. Running programs

Reslil source files use the extension `.res`. The toolchain is a
single program named `reslil`:

```
reslil run program.res      # check and run a program
reslil check program.res    # only check it for errors, without running it
```

A program reads from standard input and writes to standard output. If an
error occurs, `reslil` prints a message to standard error and exits with
status 1. Output printed before the error is kept.

A program may run at most 50,000,000 steps and nest at most 10,000 function
calls. Exceeding either limit is an error.

## 2. Lexical structure

**Layout.** Spaces, tabs, line breaks and indentation have no meaning; use
them freely for readability. A comment starts with `'` and runs to
the end of the line.

**Statement terminator.** Simple statements (declarations, assignments,
calls, printing, jumps, `cha`, `bou`, `chidrom`) end with
`;`. Compound statements such as conditionals and loops do not need
one after them, but their syntax is shown in full below.

**Names** of variables, functions and labels are made of letters, digits
and `_`, and must not start with a digit. Names are case-sensitive.

**Keywords** are reserved and cannot be used as names. They are
case-sensitive and must be written exactly as shown:

| Keyword | Meaning |
|---|---|
| `amdre` | part of: switch statement |
| `bawoum` | part of: switch statement, function declaration |
| `bou` | part of: break statement |
| `cha` | part of: return statement |
| `chidrom` | part of: continue statement |
| `dilisyo` | logical and |
| `drol` | logical not |
| `drossou` | remainder operator |
| `emsoulve` | logical or |
| `ishe` | the boolean value false |
| `malwe` | the value none |
| `mele` | part of: do-while loop |
| `moumare` | part of: switch statement |
| `oli` | part of: if statement, switch statement |
| `sheye` | part of: variable declaration |
| `shilsa` | the boolean value true |
| `sho` | part of: for loop |
| `tivou` | part of: write statement |
| `tosedo` | part of: function declaration |
| `veshim` | part of: while loop, do-while loop |
| `wami` | part of: print statement |
| `wesosa` | part of: if statement |

The builtin function names (section 9) are also reserved.

**Literals.** Integers are written in decimal (`0`, `42`, `1000`); there are
no fractions. A negative number is written with a minus sign (`-5`). Strings
are written between double quotes, such as `"hello"`. Inside a string, `\n`
is a line break, `\t` a tab, `\"` a double quote and `\\` a backslash.
Booleans are `shilsa` and `ishe`. The value `malwe` means "no
value".

## 3. Values

| Type | Examples | Notes |
|---|---|---|
| integer | `0`, `-7`, `123` | 64-bit; overflow wraps around |
| string | `"hi"`, `""` | a sequence of characters; cannot be changed in place |
| boolean | `shilsa`, `ishe` | the only values allowed as conditions |
| list | `[1, 2, 3]`, `[]`, `["a", 1]` | mutable; may mix types |
| none | `malwe` | "no value"; returned by functions that return nothing |

Lists are shared, not copied: assigning a list to another variable, or
passing it to a function, gives access to the same list.

```
tosedo addOne(xs)
    omse(xs, 1);
bawoum tosedo

sheye mine <- [5];
addOne(mine);
wami mine;
```

Output:

```
[5, 1]
```

Printing shows integers in decimal, strings without quotes, booleans and
`malwe` as their keywords, and lists in brackets with strings quoted.

## 4. Variables and simple statements

A variable must be declared before it is used:

```
sheye <name> <- <expression>;
```

Assignment changes an existing variable. Assigning to a name that was never
declared is an error.

```
<name> <- <expression>;
```

Each function has one flat set of variables. A variable declared anywhere in
a function, including inside a loop or a branch, is visible from that point
to the end of the function. Declaring an existing variable again simply
assigns to it. The top-level code of a program has its own variables, which
functions cannot see.

`wami` prints a value followed by a line break. `tivou` prints a
value without a line break.

```
wami <expression>;
```

```
tivou <expression>;
```

```
sheye x <- 5;
x <- x + 2;
sheye name <- "Ada";
wami ((name + " has ") + x) + " apples";
sheye flag <- x > 6;
wami flag;
wami malwe;
```

Output:

```
Ada has 7 apples
shilsa
malwe
```

## 5. Expressions

### Operators

| Operator | Meaning |
|---|---|
| `-x` | negation |
| `drol x` | logical not |
| `a * b` | multiplication |
| `a / b` | integer division (see below) |
| `a drossou b` | remainder (see below) |
| `a + b` | addition, or joining text (see below) |
| `a - b` | subtraction |
| `a = b` | equal |
| `a <> b` | not equal |
| `a < b`, `a <= b`, `a > b`, `a >= b` | ordering |
| `a dilisyo b` | logical and |
| `a emsoulve b` | logical or |

Note the spellings: assignment is `<-` and equality is `=`. Because `<-` is one token, write `a < -1` with a space
when comparing with a negative number.

### Grouping and precedence

**All binary operators have the same precedence and group from right to
left.** There is no "multiplication first" rule: `2 * 3 + 4` means
`2 * (3 + 4)`, and `10 - 4 - 3` means `10 - (4 - 3)`. This applies to every
binary operator, including comparisons and `dilisyo`/`emsoulve`, so
`a < b dilisyo c < d` means `a < (b dilisyo (c < d))`; write
`(a < b) dilisyo (c < d)` instead. Negation and `drol` bind tighter than
any binary operator. Parentheses group explicitly.

```
wami 2 + 3 * 4;
wami 10 - 4 - 3;
wami (2 + 3) * 4;
wami 2 + (3 * 4);
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
tosedo show(x)
    wami "evaluating " + x;
    cha x;
bawoum tosedo

wami show(10) - show(4);
```

Output:

```
evaluating 10
evaluating 4
6
```

Arguments of a function call are evaluated from left to right.

```
tosedo show(x)
    wami "evaluating " + x;
    cha x;
bawoum tosedo

tosedo pair(a, b)
    cha ramou(a) + b;
bawoum tosedo

wami pair(show(1), show(2));
```

Output:

```
evaluating 1
evaluating 2
12
```

### Integer arithmetic

Division of integers gives an integer. **The exact result is
rounded down, toward negative infinity**, so `7 / 2` is `3` and `-7 / 2` is `-4`. The remainder `a drossou b` is always `a - b * (a / b)` using that
division, so its sign follows from the rounding rule. Dividing by zero is an
error.

```
wami 7 / 2;
wami -7 / 2;
wami 7 drossou 2;
wami -7 drossou 2;
wami 6 / 3;
```

Output:

```
3
-4
1
1
2
```

### Text

`+` adds two integers. If either operand is a string, both operands are
converted to text (as printing would show them) and joined instead. Note that
`1 + 2 + "x"` is `"3x"` but `"x" + 1 + 2` is `"x12"`, following the grouping
rules above.

```
wami "n = " + 5;
wami "a" + "b" + "c";
```

Output:

```
n = 5
abc
```

Strings can be compared with `<`, `<=`, `>` and `>=`, character by character
(by character code). Comparing values of different types with `=` gives
`ishe`; ordering them is an error.

### Lists and indexing

`x[i]` is element `i` of list `x`, or the one-character string at position
`i` of string `x`. **Indexes start at 0**: the first element
is `x[0]`. List elements can be replaced with `x[i] <- value;`.

```
<name>[<index>] <- <expression>;
```

```
sheye xs <- [10, 20, 30];
wami xs[1];
xs[1] <- 99;
wami xs;
sheye word <- "abc";
wami word[1];
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
sheye a <- [1, 2];
sheye b <- [1, 2];
sheye c <- a;
omse(c, 3);
wami a;
wesosa (a = c) {
    wami "a equals c";
}
wesosa (a = [1, 2, 3]) {
    wami "a equals a new list with the same elements";
} oli {
    wami "a does not equal a new list with the same elements";
}
```

Output:

```
[1, 2, 3]
a equals c
a does not equal a new list with the same elements
```

### Logic and conditions

Conditions must be booleans: there is no "truthiness", and using an integer,
string, list or `malwe` as a condition is an error. The operands of
`dilisyo`, `emsoulve` and `drol` must also be booleans.

**`dilisyo` and `emsoulve` always evaluate both operands**, even when the
left operand already decides the result.

```
tosedo check(name, result)
    wami "checking " + name;
    cha result;
bawoum tosedo

wesosa (check("left", shilsa) emsoulve check("right", ishe)) {
    wami "yes";
}
wesosa (check("left", ishe) dilisyo check("right", shilsa)) {
    wami "yes";
} oli {
    wami "no";
}
```

Output:

```
checking left
checking right
yes
checking left
checking right
no
```

## 6. Control flow

### Conditionals

```
wesosa (<condition>) {
    <statements>
} oli wesosa (<condition>) {
    <statements>
} oli {
    <statements>
}
```

- The `oli wesosa ...` part may appear any number of times, including not at all.
- The `oli ...` part is optional.

The conditions are tested in order, and the statements of the first true
one run. If none is true, the statements of the final branch without a
condition run, if there is one.

```
sheye n <- 7;
wesosa (n < 5) {
    wami "small";
} oli wesosa (n < 10) {
    wami "medium";
} oli {
    wami "large";
}
```

Output:

```
medium
```

### Choosing by value

```
moumare amdre <expression>
amdre <literal>, ...
    <statements>
amdre oli
    <statements>
bawoum moumare
```

- The `amdre ...` part may appear any number of times, including not at all.
- The `amdre oli ...` part is optional.

The expression is evaluated once and compared with each literal in order,
using `=`. Literals are integers or strings, and must all be
different. Only the statements of the matching case run (or the default part,
if none matches and there is one). `bou` inside it refers to the enclosing loop, not
to this statement.

```
sho (sheye d <- 1; d <= 4; d <- d + 1) {
    moumare amdre d
    amdre 1
        wami "one";
    amdre 2, 3
        wami "two or three";
    amdre oli
        wami "something else";
    bawoum moumare
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
veshim (<condition>) {
    <statements>
}
```

The condition is tested before each pass; the loop ends when it is
`ishe`.

```
sheye n <- 1;
veshim (n < 100) {
    n <- n * 2;
}
wami n;
```

Output:

```
128
```

### Do-while loops

```
mele {
    <statements>
} veshim (<condition>);
```

The statements run once, then again for as long as the condition is
`shilsa`. The condition is tested after each pass.

```
sheye n <- 0;
mele {
    n <- n + 3;
} veshim (n <= 10);
wami n;
```

Output:

```
12
```

### For loops

```
sho (<initializer>; <condition>; <update>) {
    <statements>
}
```

- `<initializer>` and `<update>` are each a declaration or assignment written without the final `;`; either may be left out.

The initializer runs once. Then, while the condition is `shilsa`, the
statements run, followed by the update.

```
sho (sheye i <- 0; i < 3; i <- i + 1) {
    wami i;
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
bou;
```

```
chidrom;
```

`bou` leaves the innermost loop. `chidrom` skips to the next pass of
the innermost loop (for a counting or for loop, the update still happens).

```
tosedo div_(a, b)
    sheye q <- a / b;
    sheye r <- a - b * q;
    wesosa (r <> 0) {
        wesosa ((r < 0) <> a < 0) {
            wesosa ((r < 0) = b < 0) {
                q <- q + 1;
            } oli {
                q <- q - 1;
            }
        }
    }
    cha q;
bawoum tosedo

tosedo mod_(a, b)
    cha a - b * div_(a, b);
bawoum tosedo

sho (sheye i <- 1; i <= 10; i <- i + 1) {
    wesosa (mod_(i, 2) = 0) {
        chidrom;
    }
    wesosa (i > 7) {
        bou;
    }
    tivou i + " ";
}
wami "";
```

Output:

```
1 3 5 7 
```

## 7. Functions

```
tosedo <name>(<parameter>, ...)
    <statements>
bawoum tosedo
```

- The list of parameters may be empty.

Functions are declared at the top level of a program, not inside other
statements, and may be called before their declaration. Calling a function
with the wrong number of arguments is an error. Recursion is allowed.

```
cha <expression>;
```

- `<expression>` is optional.

`cha` ends the function and gives back the value, or `malwe`
without one. A function that ends without `cha` returns `malwe`.
A `cha` in top-level code ends the program.

A call can be used as a statement, which discards its result:

```
<function>(<argument>, ...);
```

- The list of arguments may be empty.

```
tosedo square(x)
    cha x * x;
bawoum tosedo

tosedo fact(n)
    wesosa (n <= 1) {
        cha 1;
    }
    cha n * fact(n - 1);
bawoum tosedo

tosedo greet(name)
    wami "Hello, " + name;
bawoum tosedo

wami square(7);
wami fact(10);
greet("Lin");
sheye r <- greet("Max");
wami r;
```

Output:

```
49
3628800
Hello, Lin
Hello, Max
malwe
```

## 8. Errors

Errors found before running, such as syntax errors, unknown names and wrong
argument counts, stop the program before anything runs. Errors found while
running stop it at that point. In both cases, the message names the line.

```
wami "before";
wami 1 / 0;
wami "after";
```

Output:

```
before
error: line 2: division by zero
```

## 9. Builtin functions

| Function | Description |
|---|---|
| `louwo` | `(x)`: the number of elements of list `x`, or the number of characters of string `x`. |
| `omse` | `(xs, v)`: appends `v` to the end of list `xs` (changing it) and returns `malwe`. |
| `ramou` | `(v)`: converts any value to the string that printing it would show. |
| `odresdra` | `(s)`: converts a string of decimal digits (optionally with a leading `-`, surrounding spaces allowed) to an integer. An integer is returned unchanged. Anything else is an error. |
| `diwela` | `()`: reads the next line of standard input and returns it as a string without the line ending, or `malwe` when there is no more input. |

```
sheye xs <- [3, 1];
omse(xs, 4);
wami louwo(xs);
wami louwo("hello");
wami ramou(42) + "!";
wami odresdra("12") + 1;
wami diwela();
wami diwela();
wami diwela();
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
malwe
```

## 10. A complete program

This program reads integers, one per line, until the input ends, and prints
how many there were, their sum and the largest.

```
sheye total <- 0;
sheye seen <- 0;
sheye best <- 0;
sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    wesosa (seen = 0) {
        best <- n;
    } oli wesosa (n > best) {
        best <- n;
    }
    total <- total + n;
    seen <- seen + 1;
    line <- diwela();
}
wami "count " + seen;
wami "sum " + total;
wami "max " + best;
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

Write a Reslil program that prints the integers from 1 to `n`, one per
line. If `n` is 0, print nothing.


## Task ID: t0-day-names

# Day names

Standard input contains zero or more lines, each holding one integer.

Write a Reslil program that prints one line for each input line: the name
of the day of the week for numbers 1 to 7 (`Monday` for 1, `Tuesday` for 2,
`Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday` for 7), and
`invalid` for any other number.


## Task ID: t0-even-odd

# Even and odd

Standard input contains zero or more lines, each holding one integer
(possibly negative, with absolute value at most 1,000,000).

Write a Reslil program that counts how many of the integers are even and
how many are odd, and prints exactly two lines:

```
even <number of even integers>
odd <number of odd integers>
```


## Task ID: t0-factorial

# Factorial

Standard input contains one line with an integer `n` (0 ≤ n ≤ 20).

Write a Reslil program that prints `n!`, the product of the integers from
1 to `n`. By definition, `0!` is 1.


## Task ID: t0-fizzbuzz

# FizzBuzz

Standard input contains one line with an integer `n` (1 ≤ n ≤ 1000).

Write a Reslil program that prints one line for each integer `i` from 1
to `n`:

- `FizzBuzz` if `i` is divisible by both 3 and 5,
- otherwise `Fizz` if `i` is divisible by 3,
- otherwise `Buzz` if `i` is divisible by 5,
- otherwise the number `i` itself.


## Task ID: t0-hello

# Hello

Write a Reslil program that prints exactly this line:

```
Hello, Utopia!
```


## Task ID: t0-reverse-lines

# Reverse lines

Standard input contains zero or more lines of text.

Write a Reslil program that prints the same lines in reverse order: the
last line first and the first line last. Print each line exactly as it was
read.


## Task ID: t1-digits

# Digits

Standard input contains zero or more lines, each holding one integer `n`
with absolute value at most 10^15.

Write a Reslil program that prints one line for each input line: the sum
of the decimal digits of `n`, a space, and the digits of `n` in reverse order
as an integer. Leading zeros of the reversed number are dropped, and it keeps
the sign of `n` (unless it is 0).

For example, `123` gives `6 321`, `-4500` gives `9 -54`, and `0` gives `0 0`.


## Task ID: t1-floordiv

# Floor division

Standard input contains zero or more lines, each holding two integers `a`
and `b` separated by one space, with absolute values at most 10^9 and
`b` not 0.

Write a Reslil program that prints one line for each input line: `q`, a
space, and `r`, where `q` is `a / b` rounded down (toward negative
infinity) and `r = a - b * q`. So `r` is 0 or has the sign of `b`.

For example, `7 2` gives `3 1`, `-7 2` gives `-4 1`, and `7 -2` gives
`-4 -1`.


## Task ID: t1-palindromes

# Palindromes

Standard input contains zero or more lines of text (printable ASCII
characters).

Write a Reslil program that prints one line for each input line: `yes`
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

Write a Reslil program that prints one line for each query: the number
of integers in the first line that are smaller than the query, a space, and
`found` if the query occurs in the first line or `missing` if it does not.

For example, with the first line `1 3 5 7`, the query `5` gives `2 found`
and the query `4` gives `2 missing`.


## Task ID: t1-rotate

# Rotate

The first line of standard input holds an integer `k` (absolute value at
most 10^9). It is followed by zero or more lines of text, the items.

Write a Reslil program that prints the items rotated right by `k`
places, one per line. Rotating right by one place moves the last item to
the front. A negative `k` rotates left. Print each item exactly as it was
read. If there are no items, print nothing.


## Task ID: t1-weekday

# Weekday

Standard input contains zero or more lines, each holding a date written
`YYYY-MM-DD` (always four digits for the year and two for the month and
day), between `0001-01-01` and `9999-12-31`. Dates follow the Gregorian
calendar, extended backwards to year 1.

Write a Reslil program that prints the day of the week of each date, one
per line: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`,
`Saturday` or `Sunday`.

For example, `2000-01-01` gives `Saturday`.


## Task ID: t2-bignum

# Big numbers

Standard input contains zero or more lines, each holding two non-negative
integers `a` and `b` separated by one space. Each has at most 100 digits and
no leading zeros (except the number 0 itself), so they can be far too large
for the language's integers.

Write a Reslil program that prints one line for each input line: the sum
`a + b`, a space, and the product `a * b`, both written in decimal without
leading zeros.

For example, `999 1` gives `1000 999`.


## Task ID: t2-life

# Life

The first line of standard input holds an integer `g` (0 ≤ g ≤ 30). It is
followed by one or more lines of equal length (at most 20 lines of at most
20 characters), a grid of cells: `#` is a live cell and `.` a dead one.

Write a Reslil program that runs `g` generations of Conway's Game of Life
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

Write a Reslil program that prints one line for each expression: its
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

Write a Reslil program that counts how often each word occurs and prints
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


## Task ID: t3-asm

# Register machine

Standard input holds a program for a small machine, one instruction per
line, numbered from 0. The machine has 26 registers named `a` to `z`, each
holding an integer and starting at 0. An instruction is a name and its
operands, separated by single spaces. Below, `r` is a register name and `x`
and `y` are each either a register name (meaning its value) or an integer
literal, which may start with `-`.

| Instruction | Effect |
|---|---|
| `set r x` | `r` becomes `x` |
| `add r x` | `r` becomes `r + x` |
| `sub r x` | `r` becomes `r - x` |
| `mul r x` | `r` becomes `r * x` |
| `div r x` | `r` becomes `r / x`, rounded toward zero |
| `mod r x` | `r` becomes `r - x * (r / x)`, with that same division |
| `jnz x y` | if `x` is not 0, jump `y` instructions forward (backward if `y` is negative) |
| `out x` | print `x` on a line of its own |

Execution starts at instruction 0. After each instruction other than a jump
that is taken, it moves on to the next instruction. A jump of `y` from
instruction `i` goes to instruction `i + y`. The program ends as soon as the
next instruction number is outside the program (below 0, or past the last
instruction).

Two things end it early. If `div` or `mod` would divide by zero, print
`error` and stop, leaving the register unchanged. And count every
instruction executed, taken jumps included: when 10000 instructions have
been executed and the program has not ended, print `timeout` and stop
instead of executing another one. All values stay well within 64-bit range.

Write a Reslil program that runs the program and prints what it prints.

For example, this program prints `3`, `2` and `1`:

```
set a 3
out a
sub a 1
jnz a -2
```


## Task ID: t3-bigdiv

# Big division

Standard input contains zero or more lines, each holding two integers `a`
and `b` separated by one space, with `a >= 0` and `b >= 1`. They have at
most 80 and 40 digits, and no leading zeros (except the number 0 itself),
so they can be far too large for the language's integers.

Write a Reslil program that prints one line for each input line: the
quotient `a / b` rounded down, a space, and the remainder `a - b * (a / b)`,
both written in decimal without leading zeros.

For example, `100 7` gives `14 2`.


## Task ID: t3-calc

# Calculator

Standard input contains zero or more lines, each holding an arithmetic
expression. An expression is built from non-negative integer literals (one
or more digits), the binary operators `+`, `-`, `*`, `/` and `%`, unary
minus `-`, and parentheses. Spaces may appear anywhere between tokens.

The usual rules apply, whatever Reslil itself does:

- `*`, `/` and `%` bind tighter than `+` and `-`; operators of the same
  level group from left to right, so `10-4-3` is `3` and `100/10/3` is `3`.
- Unary minus binds tighter than every binary operator: `-2*3` is `(-2)*3`,
  `3*-2` is `3*(-2)`, and `--4` is `4`. There is no unary plus.
- Division `/` rounds toward zero, so `-7/2` is `-3`, and `a % b` is
  `a - b * (a / b)` with that division, so `-7%2` is `-1`.

Every value along the way stays well within 64-bit range.

Write a Reslil program that prints one line for each expression: its
value, or `error` if the line is empty or only spaces, contains any other
character, is not a well-formed expression, or divides or takes a remainder
by zero anywhere.

For example, `2 + 3 * (4 - 6) % 5` gives `1`, and `(1 + 2` gives `error`.


## Task ID: t3-justify

# Justified text

The first line of standard input holds the line width `W` (between 10 and
60). The rest of the input is text: its words are the runs of characters
other than spaces, read across all the remaining lines in order. No word is
longer than `W`.

Fill output lines greedily: each line takes as many of the next words as fit
in `W` characters with one space between neighboring words. Then print every
line:

- The last line: its words with one space between them, and nothing after
  the last word.
- Any other line with one word: that word alone.
- Any other line: exactly `W` characters, starting with its first word and
  ending with its last word. The spaces between words are spread as evenly as
  possible; when they do not divide evenly, the gaps further left get one
  more space than the gaps further right.

If there are no words, print nothing.

Write a Reslil program that does this. For example, with width 16 the
text `This is an example of text justification.` gives:

```
This    is    an
example  of text
justification.
```


## Task ID: t3-maze

# Maze paths

The first line of standard input holds two integers, the height `H` and the
width `W` of a grid (each between 1 and 25), separated by one space. The
next `H` lines each hold `W` characters: `.` is an open cell, `#` is a wall,
`S` is the start and `E` is the end. There is exactly one `S` and exactly
one `E`, and both are open cells.

A step moves from an open cell to one of its four neighbors (up, down, left
or right) that is open and inside the grid. There is no wrapping around the
edges.

Write a Reslil program that prints one line: the smallest number of steps
from `S` to `E`, a space, and the number of different step sequences of that
smallest length. If `E` cannot be reached, print `-1 0`.

For example, for

```
2 3
S..
..E
```

the answer is `3 3`.


## Task ID: t4-lisp

# Lisp interpreter

Standard input holds a program in a small Lisp. Write a Reslil program
that runs it.

**Reading.** The program is a sequence of forms. Tokens are `(`, `)` and
atoms: an atom is a run of characters other than spaces, line breaks and
parentheses. A form is an atom or a parenthesized list of forms; lists may
span lines. The parentheses are always balanced.

**Values** are integers, the booleans `#t` and `#f`, the empty list, pairs
and procedures.

**Evaluating a form:**

- An atom that is an integer (an optional `-` followed by one or more digits)
  is that integer. `#t` and `#f` are the booleans. Any other atom is a name:
  its value is looked up in the current environment, then in the enclosing
  ones, out to the global one. A name that is not bound is an error.
- `(if c a b)`: evaluate `c`; if it is anything other than `#f`, the result
  is the value of `a`, else of `b`. Only one of `a` and `b` is evaluated.
  Any other number of parts is an error.
- `(lambda (p1 p2 ...) body1 body2 ...)`: a procedure with those parameter
  names (zero or more, each a name, not an integer) and one or more body forms.
  It remembers the environment it was created in.
- `(let ((n1 e1) (n2 e2) ...) body1 body2 ...)`: evaluate every `ei` in the
  current environment, then evaluate the body forms in a new environment,
  enclosed by the current one, where each `ni` is bound to its value. The
  result is the value of the last body form. Zero bindings are allowed; at
  least one body form is required.
- `(begin f1 f2 ...)`: evaluate one or more forms in order; the result is the
  value of the last.
- `()` is an error, and so is any list starting with `define` or `quote`
  when it is not at the top level (see below).
- Any other list `(f a1 a2 ...)` is a call: evaluate `f` and then each
  argument, left to right. If `f` is a procedure made by `lambda`, the
  number of arguments must equal its number of parameters; evaluate its body
  forms in a new environment, enclosed by the procedure's remembered one,
  that binds each parameter to its argument. The result is the value of the
  last body form. If `f` is a builtin, apply it. Anything else is an error.

**Builtins**, bound in the global environment:

| Name | Takes | Result |
|---|---|---|
| `+`, `*` | any number of integers | their sum or product (`0` or `1` for none) |
| `-` | one or two integers | the negation, or the difference |
| `/` | two integers | the quotient, rounded toward zero |
| `remainder` | two integers | `a - b * (a / b)` with that quotient |
| `=`, `<`, `>` | two integers | `#t` or `#f` |
| `not` | one value | `#t` if it is `#f`, else `#f` |
| `cons` | two values | a new pair |
| `car`, `cdr` | one pair | its first or its second part |
| `list` | any number of values | a list of them (`(list)` is the empty list) |
| `null?` | one value | `#t` if it is the empty list, else `#f` |

Calling a builtin with the wrong number of arguments, a non-integer where an
integer is needed (booleans are not integers), `car` or `cdr` of something
other than a pair, or `/` or `remainder` by zero is an error.

**The top level.** Run the forms in order. A top-level form `(define name e)`
binds `name` in the global environment to the value of `e` (replacing any
earlier binding) and prints nothing. `(define (name p1 p2 ...) body)`, with
exactly one body form, binds `name` to the procedure
`(lambda (p1 p2 ...) body)` and prints nothing. A `define` of any other
shape is an error. Every other top-level form prints its value on a line of
its own. If evaluating a top-level form causes an error, print `error`
instead, leave the global environment as it was before that form, and go on
with the next form.

**Printing:** integers in decimal; `#t` and `#f`; any procedure, builtin or
not, as `#<procedure>`; the empty list as `()`. A pair prints as `(`, then
its first part, then for as long as the second part is a pair a space and
that pair's first part, and then `)`, with ` . ` and the final second part
before the `)` if that is not the empty list: `(1 2 3)`, `(1 . 2)`,
`((1) 2 . 3)`.

All integers stay well within 64-bit range.

For example, this program prints `120` and then `(2 3 4)`:

```
(define (fact n) (if (< n 2) 1 (* n (fact (- n 1)))))
(fact 5)
(define (map f xs) (if (null? xs) (list) (cons (f (car xs)) (map f (cdr xs)))))
(map (lambda (x) (+ x 1)) (list 1 2 3))
```


## Task ID: t4-regex

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

Write a Reslil program that prints one line for each input line: `yes` if
the pattern matches the whole text, `no` if it does not, or `error` if the
pattern is malformed.

For example, `(ab|c)*d` matches `ababcd` and `d` but not `acd`, and
`[a-c]+x?` matches `cabx` but not `cad`.


## Task ID: t4-sheet

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

Write a Reslil program that prints every given cell as `NAME = VALUE`,
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

