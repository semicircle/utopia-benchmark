Below is the complete reference for Ailullai, a programming language you have
never seen before, followed by 7 programming tasks.

Write a Ailullai solution for every task. You cannot run any code, so read the
reference carefully: where Ailullai differs from languages you know, follow the
reference, not habit. Programs read standard input and write standard
output, and are graded by comparing their output exactly.

Give each solution in exactly this format:

<solution task="TASK-ID">
...Ailullai source code...
</solution>


# REFERENCE

# The Ailullai Language Reference

Ailullai is a small programming language. This reference is complete: it
describes everything the language and its toolchain do. Where Ailullai
differs from languages you may know, the difference is deliberate, so follow
this document rather than habit.

Every example in this reference was run with the real toolchain, and the
output shown is exactly what it printed.

## 1. Running programs

Ailullai source files use the extension `.ail`. The toolchain is a
single program named `ailullai`:

```
ailullai run program.ail      # check and run a program
ailullai check program.ail    # only check it for errors, without running it
```

A program reads from standard input and writes to standard output. If an
error occurs, `ailullai` prints a message to standard error and exits with
status 1. Output printed before the error is kept.

A program may run at most 50,000,000 steps and nest at most 10,000 function
calls. Exceeding either limit is an error.

## 2. Lexical structure

**Layout.** Spaces, tabs, line breaks and indentation have no meaning; use
them freely for readability. A comment starts with `#` and runs to
the end of the line.

**Statement terminator.** Simple statements (declarations, assignments,
calls, printing, jumps, `druna`, `sonaidel`, `deye`) end with
`;`. Compound statements such as conditionals and loops do not need
one after them, but their syntax is shown in full below.

**Names** of variables, functions and labels are made of letters, digits
and `_`, and must not start with a digit. Names are case-sensitive.

**Keywords** are reserved and cannot be used as names. They are
case-sensitive and must be written exactly as shown:

| Keyword | Meaning |
|---|---|
| `aiplai` | the value none |
| `aitudre` | part of: while loop |
| `atdoyal` | part of: if statement |
| `beldra` | part of: repeat-until loop |
| `bulbayo` | part of: if statement |
| `busale` | part of: counting loop |
| `dai` | part of: switch statement |
| `deye` | part of: continue statement |
| `druna` | part of: return statement |
| `ede` | part of: counting loop |
| `edrushe` | part of: while loop |
| `efu` | part of: switch statement |
| `enala` | part of: repeat-until loop |
| `eretde` | the boolean value true |
| `nonotru` | the boolean value false |
| `nudro` | part of: function declaration |
| `otai` | part of: switch statement |
| `pla` | part of: counting loop |
| `plulai` | part of: variable declaration |
| `rulsai` | logical and |
| `shaibe` | part of: print statement |
| `shoyo` | part of: counting loop |
| `sonaidel` | part of: break statement |
| `tobe` | logical or |
| `tul` | logical not |
| `yaiyoyai` | part of: write statement |
| `yelrol` | part of: repeat-until loop |

The builtin function names (section 9) are also reserved.

**Literals.** Integers are written in decimal (`0`, `42`, `1000`); there are
no fractions. A negative number is written with a minus sign (`-5`). Strings
are written between double quotes, such as `"hello"`. Inside a string, `\n`
is a line break, `\t` a tab, `\"` a double quote and `\\` a backslash.
Booleans are `eretde` and `nonotru`. The value `aiplai` means "no
value".

## 3. Values

| Type | Examples | Notes |
|---|---|---|
| integer | `0`, `-7`, `123` | 64-bit; overflow wraps around |
| string | `"hi"`, `""` | a sequence of characters; cannot be changed in place |
| boolean | `eretde`, `nonotru` | the only values allowed as conditions |
| list | `[1, 2, 3]`, `[]`, `["a", 1]` | mutable; may mix types |
| none | `aiplai` | "no value"; returned by functions that return nothing |

Lists are shared, not copied: assigning a list to another variable, or
passing it to a function, gives access to the same list.

```
nudro addOne(xs) {
    sutse(xs, 1);
}

plulai mine := [5];
addOne(mine);
shaibe mine;
```

Output:

```
[5, 1]
```

Printing shows integers in decimal, strings without quotes, booleans and
`aiplai` as their keywords, and lists in brackets with strings quoted.

## 4. Variables and simple statements

A variable must be declared before it is used:

```
plulai <name> := <expression>;
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

`shaibe` prints a value followed by a line break. `yaiyoyai` prints a
value without a line break.

```
shaibe <expression>;
```

```
yaiyoyai <expression>;
```

```
plulai x := 5;
x := x + 2;
plulai name := "Ada";
shaibe name + " has " + x + " apples";
plulai flag := x > 6;
shaibe flag;
shaibe aiplai;
```

Output:

```
Ada has 7 apples
eretde
aiplai
```

## 5. Expressions

### Operators

| Operator | Meaning |
|---|---|
| `-x` | negation |
| `tul x` | logical not |
| `a * b` | multiplication |
| `a / b` | integer division (see below) |
| `a % b` | remainder (see below) |
| `a + b` | addition, or joining text (see below) |
| `a - b` | subtraction |
| `a == b` | equal |
| `a <> b` | not equal |
| `a < b`, `a <= b`, `a > b`, `a >= b` | ordering |
| `a rulsai b` | logical and |
| `a tobe b` | logical or |

Note the spellings: assignment is `:=` and equality is `==`.

### Grouping and precedence

Operators group the usual mathematical way. From tightest to loosest:
negation and `tul`; then `*`, `/` and `%`; then `+` and `-`; then the comparisons; then
`rulsai`; then `tobe`. Operators of the same level group from left to
right, so `10 - 4 - 3` means `(10 - 4) - 3`. Parentheses group explicitly.

```
shaibe 2 + 3 * 4;
shaibe 10 - 4 - 3;
shaibe (2 + 3) * 4;
shaibe 2 + (3 * 4);
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
nudro show(x) {
    shaibe "evaluating " + x;
    druna x;
}

shaibe show(10) - show(4);
```

Output:

```
evaluating 10
evaluating 4
6
```

Arguments of a function call are evaluated from left to right.

```
nudro show(x) {
    shaibe "evaluating " + x;
    druna x;
}

nudro pair(a, b) {
    druna sutlarai(a) + b;
}

shaibe pair(show(1), show(2));
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
shaibe 7 / 2;
shaibe -7 / 2;
shaibe 7 % 2;
shaibe -7 % 2;
shaibe 6 / 3;
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
shaibe "n = " + 5;
shaibe "a" + "b" + "c";
```

Output:

```
n = 5
abc
```

Strings can be compared with `<`, `<=`, `>` and `>=`, character by character
(by character code). Comparing values of different types with `==` gives
`nonotru`; ordering them is an error.

### Lists and indexing

`x[i]` is element `i` of list `x`, or the one-character string at position
`i` of string `x`. **Indexes start at 1**: the first element
is `x[1]`. List elements can be replaced with `x[i] := value;`.

```
<name>[<index>] := <expression>;
```

```
plulai xs := [10, 20, 30];
shaibe xs[1];
xs[1] := 99;
shaibe xs;
plulai word := "abc";
shaibe word[1];
```

Output:

```
10
[99, 20, 30]
a
```

**An index outside the list wraps around**: it is taken modulo the length,
so one past the last element is the first element again, and negative
indexes count back from the end. Indexing an empty list or string is an
error.

```
plulai xs := [10, 20, 30];
shaibe xs[3];
shaibe xs[4];
shaibe xs[-1];
```

Output:

```
30
10
20
```

Two lists are equal (`==`) when they have the same length and equal
elements.

```
plulai a := [1, 2];
plulai b := [1, 2];
plulai c := a;
sutse(c, 3);
shaibe a;
atdoyal (a == c) {
    shaibe "a equals c";
}
atdoyal (a == [1, 2, 3]) {
    shaibe "a equals a new list with the same elements";
} bulbayo {
    shaibe "a does not equal a new list with the same elements";
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
string, list or `aiplai` as a condition is an error. The operands of
`rulsai`, `tobe` and `tul` must also be booleans.

`rulsai` and `tobe` evaluate their right operand only when needed: if the
left operand of `rulsai` is `nonotru`, or the left operand of `tobe`
is `eretde`, the right operand is not evaluated.

```
nudro check(name, result) {
    shaibe "checking " + name;
    druna result;
}

atdoyal (check("left", eretde) tobe check("right", nonotru)) {
    shaibe "yes";
}
atdoyal (check("left", nonotru) rulsai check("right", eretde)) {
    shaibe "yes";
} bulbayo {
    shaibe "no";
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
atdoyal (<condition>) {
    <statements>
} bulbayo atdoyal (<condition>) {
    <statements>
} bulbayo {
    <statements>
}
```

- The `bulbayo atdoyal ...` part may appear any number of times, including not at all.
- The `bulbayo ...` part is optional.

The conditions are tested in order, and the statements of the first true
one run. If none is true, the statements of the final branch without a
condition run, if there is one.

```
plulai n := 7;
atdoyal (n < 5) {
    shaibe "small";
} bulbayo atdoyal (n < 10) {
    shaibe "medium";
} bulbayo {
    shaibe "large";
}
```

Output:

```
medium
```

### Choosing by value

```
otai (<expression>) {
dai <literal>, ...:
    <statements>
efu:
    <statements>
}
```

- The `dai ...` part may appear any number of times, including not at all.
- The `efu ...` part is optional.

The expression is evaluated once and compared with each literal in order,
using `==`. Literals are integers or strings, and must all be
different. Only the statements of the matching case run (or the default part
if none matches); execution does not continue into the next case. `sonaidel` inside a case leaves the statement early.

```
shoyo d := 1 busale 5
    otai (d) {
    dai 1:
        shaibe "one";
    dai 2, 3:
        shaibe "two or three";
    efu:
        shaibe "something else";
    }
pla d
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
edrushe <condition>
    <statements>
aitudre
```

The condition is tested before each pass; the loop ends when it is
`nonotru`.

```
plulai n := 1;
edrushe n < 100
    n := n * 2;
aitudre
shaibe n;
```

Output:

```
128
```

### Repeat-until loops

```
enala
    <statements>
beldra yelrol <condition>
```

The statements run once, then again **until** the condition is `eretde`.
The condition is tested after each pass.

```
plulai n := 0;
enala
    n := n + 3;
beldra yelrol n > 10
shaibe n;
```

Output:

```
12
```

### Counting loops

```
shoyo <name> := <start> busale <limit> ede <step>
    <statements>
pla <name>
```

- The `ede ...` part is optional.
- The name after `pla` must be the loop variable.

The start, limit and step are evaluated once, before the loop begins; the
step defaults to `1` and must not be `0`. The variable starts at the start
value and changes by the step after each pass. **The limit itself is not included**: with a positive step, the loop
runs while the variable is less than the limit; with a negative step, while it
is greater.

```
shoyo i := 1 busale 6
    yaiyoyai i + " ";
pla i
shaibe "";
shoyo i := 10 busale 0 ede -3
    yaiyoyai i + " ";
pla i
shaibe "";
```

Output:

```
1 2 3 4 5 
10 7 4 1 
```

### Leaving loops early

```
sonaidel;
```

```
deye;
```

`sonaidel` leaves the innermost loop. `deye` skips to the next pass of
the innermost loop (for a counting or for loop, the update still happens).

```
shoyo i := 1 busale 11
    atdoyal (i % 2 == 0) {
        deye;
    }
    atdoyal (i > 7) {
        sonaidel;
    }
    yaiyoyai i + " ";
pla i
shaibe "";
```

Output:

```
1 3 5 7 
```

## 7. Functions

```
nudro <name>(<parameter>, ...) {
    <statements>
}
```

- The list of parameters may be empty.

Functions are declared at the top level of a program, not inside other
statements, and may be called before their declaration. Calling a function
with the wrong number of arguments is an error. Recursion is allowed.

```
druna <expression>;
```

- `<expression>` is optional.

`druna` ends the function and gives back the value, or `aiplai`
without one. A function that ends without `druna` returns `aiplai`.
A `druna` in top-level code ends the program.

A call can be used as a statement, which discards its result:

```
<function>(<argument>, ...);
```

- The list of arguments may be empty.

```
nudro square(x) {
    druna x * x;
}

nudro fact(n) {
    atdoyal (n <= 1) {
        druna 1;
    }
    druna n * fact(n - 1);
}

nudro greet(name) {
    shaibe "Hello, " + name;
}

shaibe square(7);
shaibe fact(10);
greet("Lin");
plulai r := greet("Max");
shaibe r;
```

Output:

```
49
3628800
Hello, Lin
Hello, Max
aiplai
```

## 8. Errors

Errors found before running, such as syntax errors, unknown names and wrong
argument counts, stop the program before anything runs. Errors found while
running stop it at that point. In both cases, the message names the line.

```
shaibe "before";
shaibe 1 / 0;
shaibe "after";
```

Output:

```
before
error: line 2: division by zero
```

## 9. Builtin functions

| Function | Description |
|---|---|
| `dra` | `(x)`: the number of elements of list `x`, or the number of characters of string `x`. |
| `sutse` | `(xs, v)`: appends `v` to the end of list `xs` (changing it) and returns `aiplai`. |
| `sutlarai` | `(v)`: converts any value to the string that printing it would show. |
| `plaltai` | `(s)`: converts a string of decimal digits (optionally with a leading `-`, surrounding spaces allowed) to an integer. An integer is returned unchanged. Anything else is an error. |
| `playadu` | `()`: reads the next line of standard input and returns it as a string without the line ending, or `aiplai` when there is no more input. |

```
plulai xs := [3, 1];
sutse(xs, 4);
shaibe dra(xs);
shaibe dra("hello");
shaibe sutlarai(42) + "!";
shaibe plaltai("12") + 1;
shaibe playadu();
shaibe playadu();
shaibe playadu();
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
aiplai
```

## 10. A complete program

This program reads integers, one per line, until the input ends, and prints
how many there were, their sum and the largest.

```
plulai total := 0;
plulai seen := 0;
plulai best := 0;
plulai line := playadu();
edrushe line <> aiplai
    plulai n := plaltai(line);
    atdoyal (seen == 0) {
        best := n;
    } bulbayo atdoyal (n > best) {
        best := n;
    }
    total := total + n;
    seen := seen + 1;
    line := playadu();
aitudre
shaibe "count " + seen;
shaibe "sum " + total;
shaibe "max " + best;
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

Write a Ailullai program that prints the integers from 1 to `n`, one per
line. If `n` is 0, print nothing.


## Task ID: t0-day-names

# Day names

Standard input contains zero or more lines, each holding one integer.

Write a Ailullai program that prints one line for each input line: the name
of the day of the week for numbers 1 to 7 (`Monday` for 1, `Tuesday` for 2,
`Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday` for 7), and
`invalid` for any other number.


## Task ID: t0-even-odd

# Even and odd

Standard input contains zero or more lines, each holding one integer
(possibly negative, with absolute value at most 1,000,000).

Write a Ailullai program that counts how many of the integers are even and
how many are odd, and prints exactly two lines:

```
even <number of even integers>
odd <number of odd integers>
```


## Task ID: t0-factorial

# Factorial

Standard input contains one line with an integer `n` (0 ≤ n ≤ 20).

Write a Ailullai program that prints `n!`, the product of the integers from
1 to `n`. By definition, `0!` is 1.


## Task ID: t0-fizzbuzz

# FizzBuzz

Standard input contains one line with an integer `n` (1 ≤ n ≤ 1000).

Write a Ailullai program that prints one line for each integer `i` from 1
to `n`:

- `FizzBuzz` if `i` is divisible by both 3 and 5,
- otherwise `Fizz` if `i` is divisible by 3,
- otherwise `Buzz` if `i` is divisible by 5,
- otherwise the number `i` itself.


## Task ID: t0-hello

# Hello

Write a Ailullai program that prints exactly this line:

```
Hello, Utopia!
```


## Task ID: t0-reverse-lines

# Reverse lines

Standard input contains zero or more lines of text.

Write a Ailullai program that prints the same lines in reverse order: the
last line first and the first line last. Print each line exactly as it was
read.

