Below is the complete reference for Foshoxsho, a programming language you have
never seen before, followed by 7 programming tasks.

Write a Foshoxsho solution for every task. You cannot run any code, so read the
reference carefully: where Foshoxsho differs from languages you know, follow the
reference, not habit. Programs read standard input and write standard
output, and are graded by comparing their output exactly.

Give each solution in exactly this format:

<solution task="TASK-ID">
...Foshoxsho source code...
</solution>


# REFERENCE

# The Foshoxsho Language Reference

Foshoxsho is a small programming language. This reference is complete: it
describes everything the language and its toolchain do. Where Foshoxsho
differs from languages you may know, the difference is deliberate, so follow
this document rather than habit.

Every example in this reference was run with the real toolchain, and the
output shown is exactly what it printed.

## 1. Running programs

Foshoxsho source files use the extension `.fos`. The toolchain is a
single program named `foshoxsho`:

```
foshoxsho run program.fos      # check and run a program
foshoxsho check program.fos    # only check it for errors, without running it
```

A program reads from standard input and writes to standard output. If an
error occurs, `foshoxsho` prints a message to standard error and exits with
status 1. Output printed before the error is kept.

A program may run at most 50,000,000 steps and nest at most 10,000 function
calls. Exceeding either limit is an error.

## 2. Lexical structure

**Layout.** Spaces, tabs, line breaks and indentation have no meaning; use
them freely for readability. A comment starts with `//` and runs to
the end of the line.

**Statement terminator.** Simple statements (declarations, assignments,
calls, printing, jumps, `Asdra`, `Fosvas`, `Diga`) end with
`;`. Compound statements such as conditionals and loops do not need
one after them, but their syntax is shown in full below.

**Names** of variables, functions and labels are made of letters, digits
and `_`, and must not start with a digit. Names are case-sensitive.

**Keywords** are reserved and cannot be used as names. They are
case-sensitive and must be written exactly as shown:

| Keyword | Meaning |
|---|---|
| `Asdra` | part of: return statement |
| `Ashgik` | logical not |
| `Axdis` | part of: write statement |
| `Diga` | part of: continue statement |
| `Dodogo` | remainder operator |
| `Dosfasho` | part of: print statement |
| `Dridrak` | the value none |
| `Dro` | part of: switch statement |
| `Fas` | logical and |
| `Fixpodri` | the boolean value false |
| `Fodashsa` | part of: function declaration |
| `Fosvas` | part of: break statement |
| `Gis` | part of: function declaration |
| `Gosafax` | part of: function declaration |
| `Gosh` | part of: do-while loop |
| `Gox` | logical or |
| `Ishsi` | part of: if statement |
| `Padri` | part of: if statement |
| `Papo` | part of: switch statement |
| `Paxfasva` | part of: for loop |
| `Pidok` | part of: switch statement |
| `Pigi` | the boolean value true |
| `Sipokvix` | part of: while loop, do-while loop |
| `Sogas` | part of: variable declaration |

The builtin function names (section 9) are also reserved.

**Literals.** Integers are written in decimal (`0`, `42`, `1000`); there are
no fractions. A negative number is written with a minus sign (`-5`). Strings
are written between double quotes, such as `"hello"`. Inside a string, `\n`
is a line break, `\t` a tab, `\"` a double quote and `\\` a backslash.
Booleans are `Pigi` and `Fixpodri`. The value `Dridrak` means "no
value".

## 3. Values

| Type | Examples | Notes |
|---|---|---|
| integer | `0`, `-7`, `123` | 64-bit; overflow wraps around |
| string | `"hi"`, `""` | a sequence of characters; cannot be changed in place |
| boolean | `Pigi`, `Fixpodri` | the only values allowed as conditions |
| list | `[1, 2, 3]`, `[]`, `["a", 1]` | mutable; may mix types |
| none | `Dridrak` | "no value"; returned by functions that return nothing |

Lists are shared, not copied: assigning a list to another variable, or
passing it to a function, gives access to the same list.

```
Gis addOne(xs) Fodashsa
    Dragi(xs, 1);
Gosafax

Sogas mine = [5];
addOne(mine);
Dosfasho mine;
```

Output:

```
[5, 1]
```

Printing shows integers in decimal, strings without quotes, booleans and
`Dridrak` as their keywords, and lists in brackets with strings quoted.

## 4. Variables and simple statements

A variable must be declared before it is used:

```
Sogas <name> = <expression>;
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

`Dosfasho` prints a value followed by a line break. `Axdis` prints a
value without a line break.

```
Dosfasho <expression>;
```

```
Axdis <expression>;
```

```
Sogas x = 5;
x = x + 2;
Sogas name = "Ada";
Dosfasho name + " has " + x + " apples";
Sogas flag = x > 6;
Dosfasho flag;
Dosfasho Dridrak;
```

Output:

```
Ada has 7 apples
Pigi
Dridrak
```

## 5. Expressions

### Operators

| Operator | Meaning |
|---|---|
| `-x` | negation |
| `Ashgik x` | logical not |
| `a * b` | multiplication |
| `a / b` | integer division (see below) |
| `a Dodogo b` | remainder (see below) |
| `a + b` | addition, or joining text (see below) |
| `a - b` | subtraction |
| `a == b` | equal |
| `a ~= b` | not equal |
| `a < b`, `a <= b`, `a > b`, `a >= b` | ordering |
| `a Fas b` | logical and |
| `a Gox b` | logical or |

Note the spellings: assignment is `=` and equality is `==`.

### Grouping and precedence

Operators group the usual mathematical way. From tightest to loosest:
negation and `Ashgik`; then `*`, `/` and `Dodogo`; then `+` and `-`; then the comparisons; then
`Fas`; then `Gox`. Operators of the same level group from left to
right, so `10 - 4 - 3` means `(10 - 4) - 3`. Parentheses group explicitly.

```
Dosfasho 2 + 3 * 4;
Dosfasho 10 - 4 - 3;
Dosfasho (2 + 3) * 4;
Dosfasho 2 + (3 * 4);
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
Gis show(x) Fodashsa
    Dosfasho "evaluating " + x;
    Asdra x;
Gosafax

Dosfasho show(10) - show(4);
```

Output:

```
evaluating 10
evaluating 4
6
```

Arguments of a function call are evaluated from left to right.

```
Gis show(x) Fodashsa
    Dosfasho "evaluating " + x;
    Asdra x;
Gosafax

Gis pair(a, b) Fodashsa
    Asdra Igo(a) + b;
Gosafax

Dosfasho pair(show(1), show(2));
```

Output:

```
evaluating 1
evaluating 2
12
```

### Integer arithmetic

Division of integers gives an integer. The exact result is rounded toward zero,
so `7 / 2` is `3` and `-7 / 2` is `-3`. The remainder `a Dodogo b` is always `a - b * (a / b)` using that
division, so its sign follows from the rounding rule. Dividing by zero is an
error.

```
Dosfasho 7 / 2;
Dosfasho -7 / 2;
Dosfasho 7 Dodogo 2;
Dosfasho -7 Dodogo 2;
Dosfasho 6 / 3;
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
Dosfasho "n = " + 5;
Dosfasho "a" + "b" + "c";
```

Output:

```
n = 5
abc
```

Strings can be compared with `<`, `<=`, `>` and `>=`, character by character
(by character code). Comparing values of different types with `==` gives
`Fixpodri`; ordering them is an error.

### Lists and indexing

`x[i]` is element `i` of list `x`, or the one-character string at position
`i` of string `x`. **Indexes start at 0**: the first element
is `x[0]`. List elements can be replaced with `x[i] = value;`.

```
<name>[<index>] = <expression>;
```

```
Sogas xs = [10, 20, 30];
Dosfasho xs[1];
xs[1] = 99;
Dosfasho xs;
Sogas word = "abc";
Dosfasho word[1];
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
Sogas a = [1, 2];
Sogas b = [1, 2];
Sogas c = a;
Dragi(c, 3);
Dosfasho a;
Ishsi (a == c) {
    Dosfasho "a equals c";
}
Ishsi (a == [1, 2, 3]) {
    Dosfasho "a equals a new list with the same elements";
} Padri {
    Dosfasho "a does not equal a new list with the same elements";
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
string, list or `Dridrak` as a condition is an error. The operands of
`Fas`, `Gox` and `Ashgik` must also be booleans.

`Fas` and `Gox` evaluate their right operand only when needed: if the
left operand of `Fas` is `Fixpodri`, or the left operand of `Gox`
is `Pigi`, the right operand is not evaluated.

```
Gis check(name, result) Fodashsa
    Dosfasho "checking " + name;
    Asdra result;
Gosafax

Ishsi (check("left", Pigi) Gox check("right", Fixpodri)) {
    Dosfasho "yes";
}
Ishsi (check("left", Fixpodri) Fas check("right", Pigi)) {
    Dosfasho "yes";
} Padri {
    Dosfasho "no";
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
Ishsi (<condition>) {
    <statements>
} Padri Ishsi (<condition>) {
    <statements>
} Padri {
    <statements>
}
```

- The `Padri Ishsi ...` part may appear any number of times, including not at all.
- The `Padri ...` part is optional.

The conditions are tested in order, and the statements of the first true
one run. If none is true, the statements of the final branch without a
condition run, if there is one.

```
Sogas n = 7;
Ishsi (n < 5) {
    Dosfasho "small";
} Padri Ishsi (n < 10) {
    Dosfasho "medium";
} Padri {
    Dosfasho "large";
}
```

Output:

```
medium
```

### Choosing by value

```
Pidok (<expression>) {
Dro <literal>, ...:
    <statements>
Papo:
    <statements>
}
```

- The `Dro ...` part may appear any number of times, including not at all.
- The `Papo ...` part is optional.

The expression is evaluated once and compared with each literal in order,
using `==`. Literals are integers or strings, and must all be
different. Only the statements of the matching case run (or the default part
if none matches); execution does not continue into the next case. `Fosvas` inside a case leaves the statement early.

```
Paxfasva (Sogas d = 1; d <= 4; d = d + 1) {
    Pidok (d) {
    Dro 1:
        Dosfasho "one";
    Dro 2, 3:
        Dosfasho "two or three";
    Papo:
        Dosfasho "something else";
    }
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
Sipokvix (<condition>) {
    <statements>
}
```

The condition is tested before each pass; the loop ends when it is
`Fixpodri`.

```
Sogas n = 1;
Sipokvix (n < 100) {
    n = n * 2;
}
Dosfasho n;
```

Output:

```
128
```

### Do-while loops

```
Gosh {
    <statements>
} Sipokvix (<condition>);
```

The statements run once, then again for as long as the condition is
`Pigi`. The condition is tested after each pass.

```
Sogas n = 0;
Gosh {
    n = n + 3;
} Sipokvix (n <= 10);
Dosfasho n;
```

Output:

```
12
```

### For loops

```
Paxfasva (<initializer>; <condition>; <update>) {
    <statements>
}
```

- `<initializer>` and `<update>` are each a declaration or assignment written without the final `;`; either may be left out.

The initializer runs once. Then, while the condition is `Pigi`, the
statements run, followed by the update.

```
Paxfasva (Sogas i = 0; i < 3; i = i + 1) {
    Dosfasho i;
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
Fosvas;
```

```
Diga;
```

`Fosvas` leaves the innermost loop. `Diga` skips to the next pass of
the innermost loop (for a counting or for loop, the update still happens).

```
Paxfasva (Sogas i = 1; i <= 10; i = i + 1) {
    Ishsi (i Dodogo 2 == 0) {
        Diga;
    }
    Ishsi (i > 7) {
        Fosvas;
    }
    Axdis i + " ";
}
Dosfasho "";
```

Output:

```
1 3 5 7 
```

## 7. Functions

```
Gis <name>(<parameter>, ...) Fodashsa
    <statements>
Gosafax
```

- The list of parameters may be empty.

Functions are declared at the top level of a program, not inside other
statements, and may be called before their declaration. Calling a function
with the wrong number of arguments is an error. Recursion is allowed.

```
Asdra <expression>;
```

- `<expression>` is optional.

`Asdra` ends the function and gives back the value, or `Dridrak`
without one. A function that ends without `Asdra` returns `Dridrak`.
A `Asdra` in top-level code ends the program.

A call can be used as a statement, which discards its result:

```
<function>(<argument>, ...);
```

- The list of arguments may be empty.

```
Gis square(x) Fodashsa
    Asdra x * x;
Gosafax

Gis fact(n) Fodashsa
    Ishsi (n <= 1) {
        Asdra 1;
    }
    Asdra n * fact(n - 1);
Gosafax

Gis greet(name) Fodashsa
    Dosfasho "Hello, " + name;
Gosafax

Dosfasho square(7);
Dosfasho fact(10);
greet("Lin");
Sogas r = greet("Max");
Dosfasho r;
```

Output:

```
49
3628800
Hello, Lin
Hello, Max
Dridrak
```

## 8. Errors

Errors found before running, such as syntax errors, unknown names and wrong
argument counts, stop the program before anything runs. Errors found while
running stop it at that point. In both cases, the message names the line.

```
Dosfasho "before";
Dosfasho 1 / 0;
Dosfasho "after";
```

Output:

```
before
error: line 2: division by zero
```

## 9. Builtin functions

| Function | Description |
|---|---|
| `Drash` | `(x)`: the number of elements of list `x`, or the number of characters of string `x`. |
| `Dragi` | `(xs, v)`: appends `v` to the end of list `xs` (changing it) and returns `Dridrak`. |
| `Igo` | `(v)`: converts any value to the string that printing it would show. |
| `Drak` | `(s)`: converts a string of decimal digits (optionally with a leading `-`, surrounding spaces allowed) to an integer. An integer is returned unchanged. Anything else is an error. |
| `Goshvovo` | `()`: reads the next line of standard input and returns it as a string without the line ending, or `Dridrak` when there is no more input. |

```
Sogas xs = [3, 1];
Dragi(xs, 4);
Dosfasho Drash(xs);
Dosfasho Drash("hello");
Dosfasho Igo(42) + "!";
Dosfasho Drak("12") + 1;
Dosfasho Goshvovo();
Dosfasho Goshvovo();
Dosfasho Goshvovo();
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
Dridrak
```

## 10. A complete program

This program reads integers, one per line, until the input ends, and prints
how many there were, their sum and the largest.

```
Sogas total = 0;
Sogas seen = 0;
Sogas best = 0;
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas n = Drak(line);
    Ishsi (seen == 0) {
        best = n;
    } Padri Ishsi (n > best) {
        best = n;
    }
    total = total + n;
    seen = seen + 1;
    line = Goshvovo();
}
Dosfasho "count " + seen;
Dosfasho "sum " + total;
Dosfasho "max " + best;
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

Write a Foshoxsho program that prints the integers from 1 to `n`, one per
line. If `n` is 0, print nothing.


## Task ID: t0-day-names

# Day names

Standard input contains zero or more lines, each holding one integer.

Write a Foshoxsho program that prints one line for each input line: the name
of the day of the week for numbers 1 to 7 (`Monday` for 1, `Tuesday` for 2,
`Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday` for 7), and
`invalid` for any other number.


## Task ID: t0-even-odd

# Even and odd

Standard input contains zero or more lines, each holding one integer
(possibly negative, with absolute value at most 1,000,000).

Write a Foshoxsho program that counts how many of the integers are even and
how many are odd, and prints exactly two lines:

```
even <number of even integers>
odd <number of odd integers>
```


## Task ID: t0-factorial

# Factorial

Standard input contains one line with an integer `n` (0 ≤ n ≤ 20).

Write a Foshoxsho program that prints `n!`, the product of the integers from
1 to `n`. By definition, `0!` is 1.


## Task ID: t0-fizzbuzz

# FizzBuzz

Standard input contains one line with an integer `n` (1 ≤ n ≤ 1000).

Write a Foshoxsho program that prints one line for each integer `i` from 1
to `n`:

- `FizzBuzz` if `i` is divisible by both 3 and 5,
- otherwise `Fizz` if `i` is divisible by 3,
- otherwise `Buzz` if `i` is divisible by 5,
- otherwise the number `i` itself.


## Task ID: t0-hello

# Hello

Write a Foshoxsho program that prints exactly this line:

```
Hello, Utopia!
```


## Task ID: t0-reverse-lines

# Reverse lines

Standard input contains zero or more lines of text.

Write a Foshoxsho program that prints the same lines in reverse order: the
last line first and the first line last. Print each line exactly as it was
read.

