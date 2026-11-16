Below is the complete reference for Gutrur, a programming language you have
never seen before, followed by 7 programming tasks.

Write a Gutrur solution for every task. You cannot run any code, so read the
reference carefully: where Gutrur differs from languages you know, follow the
reference, not habit. Programs read standard input and write standard
output, and are graded by comparing their output exactly.

Give each solution in exactly this format:

<solution task="TASK-ID">
...Gutrur source code...
</solution>


# REFERENCE

# The Gutrur Language Reference

Gutrur is a small programming language. This reference is complete: it
describes everything the language and its toolchain do. Where Gutrur
differs from languages you may know, the difference is deliberate, so follow
this document rather than habit.

Every example in this reference was run with the real toolchain, and the
output shown is exactly what it printed.

## 1. Running programs

Gutrur source files use the extension `.gut`. The toolchain is a
single program named `gutrur`:

```
gutrur run program.gut      # check and run a program
gutrur check program.gut    # only check it for errors, without running it
```

A program reads from standard input and writes to standard output. If an
error occurs, `gutrur` prints a message to standard error and exits with
status 1. Output printed before the error is kept.

A program may run at most 50,000,000 steps and nest at most 10,000 function
calls. Exceeding either limit is an error.

## 2. Lexical structure

**Layout.** Spaces, tabs, line breaks and indentation have no meaning; use
them freely for readability. A comment starts with `//` and runs to
the end of the line.

**Statement terminator.** Simple statements (declarations, assignments,
calls, printing, jumps, `odrol`, `wuyem`, `omgu`) end with
`.`. Compound statements such as conditionals and loops do not need
one after them, but their syntax is shown in full below.

**Names** of variables, functions and labels are made of letters, digits
and `_`, and must not start with a digit. Names are case-sensitive.

**Keywords** are reserved and cannot be used as names. They are
case-sensitive and must be written exactly as shown:

| Keyword | Meaning |
|---|---|
| `dre` | part of: if statement |
| `dredrume` | part of: function declaration |
| `drorsu` | logical or |
| `ethur` | part of: if statement |
| `ewuyo` | part of: repeat-until loop |
| `goyu` | part of: variable declaration |
| `gugum` | part of: switch statement |
| `gursume` | the value none |
| `meshe` | part of: counting loop |
| `odrol` | part of: return statement |
| `omethol` | part of: while loop |
| `omgu` | part of: continue statement |
| `setru` | part of: counting loop |
| `sho` | part of: repeat-until loop |
| `shogu` | logical not |
| `shusushe` | part of: while loop |
| `sudru` | the boolean value true |
| `suwe` | part of: print statement |
| `suyogur` | logical and |
| `trer` | part of: counting loop |
| `treyur` | part of: repeat-until loop |
| `tru` | the boolean value false |
| `trumguwu` | remainder operator |
| `truthor` | part of: if statement, switch statement |
| `wego` | part of: counting loop |
| `wem` | part of: switch statement |
| `wemgego` | part of: write statement |
| `wodrotru` | part of: if statement, switch statement, function declaration |
| `wuyem` | part of: break statement |
| `yuyuge` | part of: if statement |

The builtin function names (section 9) are also reserved.

**Literals.** Integers are written in decimal (`0`, `42`, `1000`); there are
no fractions. A negative number is written with a minus sign (`-5`). Strings
are written between double quotes, such as `"hello"`. Inside a string, `\n`
is a line break, `\t` a tab, `\"` a double quote and `\\` a backslash.
Booleans are `sudru` and `tru`. The value `gursume` means "no
value".

## 3. Values

| Type | Examples | Notes |
|---|---|---|
| integer | `0`, `-7`, `123` | 64-bit; overflow wraps around |
| string | `"hi"`, `""` | a sequence of characters; cannot be changed in place |
| boolean | `sudru`, `tru` | the only values allowed as conditions |
| list | `[1, 2, 3]`, `[]`, `["a", 1]` | mutable; may mix types |
| none | `gursume` | "no value"; returned by functions that return nothing |

Lists are shared, not copied: assigning a list to another variable, or
passing it to a function, gives access to the same list.

```
dredrume addOne(xs)
    dreme(xs, 1).
wodrotru dredrume

goyu mine <- [5].
addOne(mine).
suwe mine.
```

Output:

```
[5, 1]
```

Printing shows integers in decimal, strings without quotes, booleans and
`gursume` as their keywords, and lists in brackets with strings quoted.

## 4. Variables and simple statements

A variable must be declared before it is used:

```
goyu <name> <- <expression>.
```

Assignment changes an existing variable. Assigning to a name that was never
declared is an error.

```
<name> <- <expression>.
```

Each function has one flat set of variables. A variable declared anywhere in
a function, including inside a loop or a branch, is visible from that point
to the end of the function. Declaring an existing variable again simply
assigns to it. The top-level code of a program has its own variables, which
functions cannot see.

`suwe` prints a value followed by a line break. `wemgego` prints a
value without a line break.

```
suwe <expression>.
```

```
wemgego <expression>.
```

```
goyu x <- 5.
x <- x + 2.
goyu name <- "Ada".
suwe name & " has " & x & " apples".
goyu flag <- x > 6.
suwe flag.
suwe gursume.
```

Output:

```
Ada has 7 apples
sudru
gursume
```

## 5. Expressions

### Operators

| Operator | Meaning |
|---|---|
| `-x` | negation |
| `shogu x` | logical not |
| `a * b` | multiplication |
| `a / b` | integer division (see below) |
| `a trumguwu b` | remainder (see below) |
| `a + b` | addition |
| `a - b` | subtraction |
| `a & b` | joining text (see below) |
| `a == b` | equal |
| `a != b` | not equal |
| `a < b`, `a <= b`, `a > b`, `a >= b` | ordering |
| `a suyogur b` | logical and |
| `a drorsu b` | logical or |

Note the spellings: assignment is `<-` and equality is `==`. Because `<-` is one token, write `a < -1` with a space
when comparing with a negative number.

### Grouping and precedence

Operators group the usual mathematical way. From tightest to loosest:
negation and `shogu`; then `*`, `/` and `trumguwu`; then `+` and `-` and `&`; then the comparisons; then
`suyogur`; then `drorsu`. Operators of the same level group from left to
right, so `10 - 4 - 3` means `(10 - 4) - 3`. Parentheses group explicitly.

```
suwe 2 + 3 * 4.
suwe 10 - 4 - 3.
suwe (2 + 3) * 4.
suwe 2 + (3 * 4).
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
dredrume show(x)
    suwe "evaluating " & x.
    odrol x.
wodrotru dredrume

suwe show(10) - show(4).
```

Output:

```
evaluating 10
evaluating 4
6
```

Arguments of a function call are evaluated from left to right.

```
dredrume show(x)
    suwe "evaluating " & x.
    odrol x.
wodrotru dredrume

dredrume pair(a, b)
    odrol a & b.
wodrotru dredrume

suwe pair(show(1), show(2)).
```

Output:

```
evaluating 1
evaluating 2
12
```

### Integer arithmetic

Division of integers gives an integer. The exact result is rounded toward zero,
so `7 / 2` is `3` and `-7 / 2` is `-3`. The remainder `a trumguwu b` is always `a - b * (a / b)` using that
division, so its sign follows from the rounding rule. Dividing by zero is an
error.

```
suwe 7 / 2.
suwe -7 / 2.
suwe 7 trumguwu 2.
suwe -7 trumguwu 2.
suwe 6 / 3.
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
suwe "n = " & 5.
suwe "a" & "b" & "c".
```

Output:

```
n = 5
abc
```

Strings can be compared with `<`, `<=`, `>` and `>=`, character by character
(by character code). Comparing values of different types with `==` gives
`tru`; ordering them is an error.

### Lists and indexing

`x[i]` is element `i` of list `x`, or the one-character string at position
`i` of string `x`. **Indexes start at 0**: the first element
is `x[0]`. List elements can be replaced with `x[i] <- value.`.

```
<name>[<index>] <- <expression>.
```

```
goyu xs <- [10, 20, 30].
suwe xs[1].
xs[1] <- 99.
suwe xs.
goyu word <- "abc".
suwe word[1].
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
goyu a <- [1, 2].
goyu b <- [1, 2].
goyu c <- a.
dreme(c, 3).
suwe a.
dre a == c ethur
    suwe "a equals c".
wodrotru dre
dre a == [1, 2, 3] ethur
    suwe "a equals a new list with the same elements".
truthor
    suwe "a does not equal a new list with the same elements".
wodrotru dre
```

Output:

```
[1, 2, 3]
a equals c
a equals a new list with the same elements
```

### Logic and conditions

Conditions must be booleans: there is no "truthiness", and using an integer,
string, list or `gursume` as a condition is an error. The operands of
`suyogur`, `drorsu` and `shogu` must also be booleans.

`suyogur` and `drorsu` evaluate their right operand only when needed: if the
left operand of `suyogur` is `tru`, or the left operand of `drorsu`
is `sudru`, the right operand is not evaluated.

```
dredrume check(name, result)
    suwe "checking " & name.
    odrol result.
wodrotru dredrume

dre check("left", sudru) drorsu check("right", tru) ethur
    suwe "yes".
wodrotru dre
dre check("left", tru) suyogur check("right", sudru) ethur
    suwe "yes".
truthor
    suwe "no".
wodrotru dre
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
dre <condition> ethur
    <statements>
yuyuge <condition> ethur
    <statements>
truthor
    <statements>
wodrotru dre
```

- The `yuyuge ...` part may appear any number of times, including not at all.
- The `truthor ...` part is optional.

The conditions are tested in order, and the statements of the first true
one run. If none is true, the statements of the final branch without a
condition run, if there is one.

```
goyu n <- 7.
dre n < 5 ethur
    suwe "small".
yuyuge n < 10 ethur
    suwe "medium".
truthor
    suwe "large".
wodrotru dre
```

Output:

```
medium
```

### Choosing by value

```
wem gugum <expression>
gugum <literal>, ...
    <statements>
gugum truthor
    <statements>
wodrotru wem
```

- The `gugum ...` part may appear any number of times, including not at all.
- The `gugum truthor ...` part is optional.

The expression is evaluated once and compared with each literal in order,
using `==`. Literals are integers or strings, and must all be
different. Only the statements of the matching case run (or the default part,
if none matches and there is one). `wuyem` inside it refers to the enclosing loop, not
to this statement.

```
wego d <- 1 setru 4
    wem gugum d
    gugum 1
        suwe "one".
    gugum 2, 3
        suwe "two or three".
    gugum truthor
        suwe "something else".
    wodrotru wem
trer d
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
omethol <condition>
    <statements>
shusushe
```

The condition is tested before each pass; the loop ends when it is
`tru`.

```
goyu n <- 1.
omethol n < 100
    n <- n * 2.
shusushe
suwe n.
```

Output:

```
128
```

### Repeat-until loops

```
treyur
    <statements>
sho ewuyo <condition>
```

The statements run once, then again **until** the condition is `sudru`.
The condition is tested after each pass.

```
goyu n <- 0.
treyur
    n <- n + 3.
sho ewuyo n > 10
suwe n.
```

Output:

```
12
```

### Counting loops

```
wego <name> <- <start> setru <limit> meshe <step>
    <statements>
trer <name>
```

- The `meshe ...` part is optional.
- The name after `trer` must be the loop variable.

The start, limit and step are evaluated once, before the loop begins; the
step defaults to `1` and must not be `0`. The variable starts at the start
value and changes by the step after each pass. The loop runs while the variable has not passed the
limit; **the limit itself is included**.

```
wego i <- 1 setru 5
    wemgego i & " ".
trer i
suwe "".
wego i <- 10 setru 1 meshe -3
    wemgego i & " ".
trer i
suwe "".
```

Output:

```
1 2 3 4 5 
10 7 4 1 
```

### Leaving loops early

```
wuyem.
```

```
omgu.
```

`wuyem` leaves the innermost loop. `omgu` skips to the next pass of
the innermost loop (for a counting or for loop, the update still happens).

```
wego i <- 1 setru 10
    dre i trumguwu 2 == 0 ethur
        omgu.
    wodrotru dre
    dre i > 7 ethur
        wuyem.
    wodrotru dre
    wemgego i & " ".
trer i
suwe "".
```

Output:

```
1 3 5 7 
```

## 7. Functions

```
dredrume <name>(<parameter>, ...)
    <statements>
wodrotru dredrume
```

- The list of parameters may be empty.

Functions are declared at the top level of a program, not inside other
statements, and may be called before their declaration. Calling a function
with the wrong number of arguments is an error. Recursion is allowed.

```
odrol <expression>.
```

- `<expression>` is optional.

`odrol` ends the function and gives back the value, or `gursume`
without one. A function that ends without `odrol` returns `gursume`.
A `odrol` in top-level code ends the program.

A call can be used as a statement, which discards its result:

```
<function>(<argument>, ...).
```

- The list of arguments may be empty.

```
dredrume square(x)
    odrol x * x.
wodrotru dredrume

dredrume fact(n)
    dre n <= 1 ethur
        odrol 1.
    wodrotru dre
    odrol n * fact(n - 1).
wodrotru dredrume

dredrume greet(name)
    suwe "Hello, " & name.
wodrotru dredrume

suwe square(7).
suwe fact(10).
greet("Lin").
goyu r <- greet("Max").
suwe r.
```

Output:

```
49
3628800
Hello, Lin
Hello, Max
gursume
```

## 8. Errors

Errors found before running, such as syntax errors, unknown names and wrong
argument counts, stop the program before anything runs. Errors found while
running stop it at that point. In both cases, the message names the line.

```
suwe "before".
suwe 1 / 0.
suwe "after".
```

Output:

```
before
error: line 2: division by zero
```

## 9. Builtin functions

| Function | Description |
|---|---|
| `wumdror` | `(x)`: the number of elements of list `x`, or the number of characters of string `x`. |
| `dreme` | `(xs, v)`: appends `v` to the end of list `xs` (changing it) and returns `gursume`. |
| `shodrewe` | `(v)`: converts any value to the string that printing it would show. |
| `druwol` | `(s)`: converts a string of decimal digits (optionally with a leading `-`, surrounding spaces allowed) to an integer. An integer is returned unchanged. Anything else is an error. |
| `uyotho` | `()`: reads the next line of standard input and returns it as a string without the line ending, or `gursume` when there is no more input. |

```
goyu xs <- [3, 1].
dreme(xs, 4).
suwe wumdror(xs).
suwe wumdror("hello").
suwe shodrewe(42) & "!".
suwe druwol("12") + 1.
suwe uyotho().
suwe uyotho().
suwe uyotho().
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
gursume
```

## 10. A complete program

This program reads integers, one per line, until the input ends, and prints
how many there were, their sum and the largest.

```
goyu total <- 0.
goyu seen <- 0.
goyu best <- 0.
goyu line <- uyotho().
omethol line != gursume
    goyu n <- druwol(line).
    dre seen == 0 ethur
        best <- n.
    yuyuge n > best ethur
        best <- n.
    wodrotru dre
    total <- total + n.
    seen <- seen + 1.
    line <- uyotho().
shusushe
suwe "count " & seen.
suwe "sum " & total.
suwe "max " & best.
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

Write a Gutrur program that prints the integers from 1 to `n`, one per
line. If `n` is 0, print nothing.


## Task ID: t0-day-names

# Day names

Standard input contains zero or more lines, each holding one integer.

Write a Gutrur program that prints one line for each input line: the name
of the day of the week for numbers 1 to 7 (`Monday` for 1, `Tuesday` for 2,
`Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday` for 7), and
`invalid` for any other number.


## Task ID: t0-even-odd

# Even and odd

Standard input contains zero or more lines, each holding one integer
(possibly negative, with absolute value at most 1,000,000).

Write a Gutrur program that counts how many of the integers are even and
how many are odd, and prints exactly two lines:

```
even <number of even integers>
odd <number of odd integers>
```


## Task ID: t0-factorial

# Factorial

Standard input contains one line with an integer `n` (0 ≤ n ≤ 20).

Write a Gutrur program that prints `n!`, the product of the integers from
1 to `n`. By definition, `0!` is 1.


## Task ID: t0-fizzbuzz

# FizzBuzz

Standard input contains one line with an integer `n` (1 ≤ n ≤ 1000).

Write a Gutrur program that prints one line for each integer `i` from 1
to `n`:

- `FizzBuzz` if `i` is divisible by both 3 and 5,
- otherwise `Fizz` if `i` is divisible by 3,
- otherwise `Buzz` if `i` is divisible by 5,
- otherwise the number `i` itself.


## Task ID: t0-hello

# Hello

Write a Gutrur program that prints exactly this line:

```
Hello, Utopia!
```


## Task ID: t0-reverse-lines

# Reverse lines

Standard input contains zero or more lines of text.

Write a Gutrur program that prints the same lines in reverse order: the
last line first and the first line last. Print each line exactly as it was
read.

