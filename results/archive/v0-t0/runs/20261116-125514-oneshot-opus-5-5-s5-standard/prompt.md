Below is the complete reference for Vetthimni, a programming language you have
never seen before, followed by 7 programming tasks.

Write a Vetthimni solution for every task. You cannot run any code, so read the
reference carefully: where Vetthimni differs from languages you know, follow the
reference, not habit. Programs read standard input and write standard
output, and are graded by comparing their output exactly.

Give each solution in exactly this format:

<solution task="TASK-ID">
...Vetthimni source code...
</solution>


# REFERENCE

# The Vetthimni Language Reference

Vetthimni is a small programming language. This reference is complete: it
describes everything the language and its toolchain do. Where Vetthimni
differs from languages you may know, the difference is deliberate, so follow
this document rather than habit.

Every example in this reference was run with the real toolchain, and the
output shown is exactly what it printed.

## 1. Running programs

Vetthimni source files use the extension `.vet`. The toolchain is a
single program named `vetthimni`:

```
vetthimni run program.vet      # check and run a program
vetthimni check program.vet    # only check it for errors, without running it
```

A program reads from standard input and writes to standard output. If an
error occurs, `vetthimni` prints a message to standard error and exits with
status 1. Output printed before the error is kept.

A program may run at most 50,000,000 steps and nest at most 10,000 function
calls. Exceeding either limit is an error.

## 2. Lexical structure

**Layout.** Spaces, tabs, line breaks and indentation have no meaning; use
them freely for readability. A comment starts with `--` and runs to
the end of the line.

**Statement terminator.** Simple statements (declarations, assignments,
calls, printing, jumps, `yiletho`, `chet`, `lidutle`) end with
`.`. Compound statements such as conditionals and loops do not need
one after them, but their syntax is shown in full below.

**Names** of variables, functions and labels are made of letters, digits
and `_`, and must not start with a digit. Names are case-sensitive.

**Keywords** are reserved and cannot be used as names. They are
case-sensitive and must be written exactly as shown:

| Keyword | Meaning |
|---|---|
| `chet` | part of: break statement |
| `dit` | part of: if statement, switch statement, while loop, counting loop, function declaration |
| `emletlel` | the value none |
| `erote` | part of: repeat-until loop |
| `hutro` | part of: if statement |
| `kolethul` | remainder operator |
| `konit` | part of: while loop |
| `lemyunom` | part of: counting loop |
| `lidutle` | part of: continue statement |
| `litthi` | the boolean value false |
| `lotvethu` | logical and |
| `mitho` | part of: while loop, counting loop |
| `miyol` | part of: print statement |
| `motdi` | part of: write statement |
| `nethe` | part of: if statement, while loop, counting loop, function declaration |
| `nime` | logical or |
| `ohetdi` | part of: variable declaration |
| `rilniro` | part of: if statement |
| `rimli` | part of: function declaration |
| `rodilvul` | part of: counting loop |
| `ronuthit` | the boolean value true |
| `thi` | part of: switch statement |
| `thikutli` | part of: counting loop |
| `thumku` | part of: if statement, switch statement |
| `torelro` | part of: switch statement |
| `yiletho` | part of: return statement |
| `yolo` | part of: repeat-until loop |
| `yothicho` | logical not |

The builtin function names (section 9) are also reserved.

**Literals.** Integers are written in decimal (`0`, `42`, `1000`); there are
no fractions. A negative number is written with a minus sign (`-5`). Strings
are written between double quotes, such as `"hello"`. Inside a string, `\n`
is a line break, `\t` a tab, `\"` a double quote and `\\` a backslash.
Booleans are `ronuthit` and `litthi`. The value `emletlel` means "no
value".

## 3. Values

| Type | Examples | Notes |
|---|---|---|
| integer | `0`, `-7`, `123` | 64-bit; overflow wraps around |
| string | `"hi"`, `""` | a sequence of characters; cannot be changed in place |
| boolean | `ronuthit`, `litthi` | the only values allowed as conditions |
| list | `[1, 2, 3]`, `[]`, `["a", 1]` | mutable; may mix types |
| none | `emletlel` | "no value"; returned by functions that return nothing |

Lists are shared, not copied: assigning a list to another variable, or
passing it to a function, gives access to the same list.

```
rimli addOne(xs) nethe
    nimhol(xs, 1).
dit

ohetdi mine = [5].
addOne(mine).
miyol mine.
```

Output:

```
[5, 1]
```

Printing shows integers in decimal, strings without quotes, booleans and
`emletlel` as their keywords, and lists in brackets with strings quoted.

## 4. Variables and simple statements

A variable must be declared before it is used:

```
ohetdi <name> = <expression>.
```

Assignment changes an existing variable. Assigning to a name that was never
declared is an error.

```
<name> = <expression>.
```

Each function has one flat set of variables. A variable declared anywhere in
a function, including inside a loop or a branch, is visible from that point
to the end of the function. Declaring an existing variable again simply
assigns to it. The top-level code of a program has its own variables, which
functions cannot see.

`miyol` prints a value followed by a line break. `motdi` prints a
value without a line break.

```
miyol <expression>.
```

```
motdi <expression>.
```

```
ohetdi x = 5.
x = x + 2.
ohetdi name = "Ada".
miyol name & " has " & x & " apples".
ohetdi flag = x > 6.
miyol flag.
miyol emletlel.
```

Output:

```
Ada has 7 apples
ronuthit
emletlel
```

## 5. Expressions

### Operators

| Operator | Meaning |
|---|---|
| `-x` | negation |
| `yothicho x` | logical not |
| `a * b` | multiplication |
| `a / b` | integer division (see below) |
| `a kolethul b` | remainder (see below) |
| `a + b` | addition |
| `a - b` | subtraction |
| `a & b` | joining text (see below) |
| `a == b` | equal |
| `a <> b` | not equal |
| `a < b`, `a <= b`, `a > b`, `a >= b` | ordering |
| `a lotvethu b` | logical and |
| `a nime b` | logical or |

Note the spellings: assignment is `=` and equality is `==`. Because `--` starts a comment, write `a - -1` with a
space when subtracting a negative number.

### Grouping and precedence

Operators group the usual mathematical way. From tightest to loosest:
negation and `yothicho`; then `*`, `/` and `kolethul`; then `+` and `-` and `&`; then the comparisons; then
`lotvethu`; then `nime`. Operators of the same level group from left to
right, so `10 - 4 - 3` means `(10 - 4) - 3`. Parentheses group explicitly.

```
miyol 2 + 3 * 4.
miyol 10 - 4 - 3.
miyol (2 + 3) * 4.
miyol 2 + (3 * 4).
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
rimli show(x) nethe
    miyol "evaluating " & x.
    yiletho x.
dit

miyol show(10) - show(4).
```

Output:

```
evaluating 10
evaluating 4
6
```

Arguments of a function call are evaluated from left to right.

```
rimli show(x) nethe
    miyol "evaluating " & x.
    yiletho x.
dit

rimli pair(a, b) nethe
    yiletho a & b.
dit

miyol pair(show(1), show(2)).
```

Output:

```
evaluating 1
evaluating 2
12
```

### Integer arithmetic

Division of integers gives an integer. The exact result is rounded toward zero,
so `7 / 2` is `3` and `-7 / 2` is `-3`. The remainder `a kolethul b` is always `a - b * (a / b)` using that
division, so its sign follows from the rounding rule. Dividing by zero is an
error.

```
miyol 7 / 2.
miyol -7 / 2.
miyol 7 kolethul 2.
miyol -7 kolethul 2.
miyol 6 / 3.
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
miyol "n = " & 5.
miyol "a" & "b" & "c".
```

Output:

```
n = 5
abc
```

Strings can be compared with `<`, `<=`, `>` and `>=`, character by character
(by character code). Comparing values of different types with `==` gives
`litthi`; ordering them is an error.

### Lists and indexing

`x[i]` is element `i` of list `x`, or the one-character string at position
`i` of string `x`. **Indexes start at 0**: the first element
is `x[0]`. List elements can be replaced with `x[i] = value.`.

```
<name>[<index>] = <expression>.
```

```
ohetdi xs = [10, 20, 30].
miyol xs[1].
xs[1] = 99.
miyol xs.
ohetdi word = "abc".
miyol word[1].
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
ohetdi a = [1, 2].
ohetdi b = [1, 2].
ohetdi c = a.
nimhol(c, 3).
miyol a.
rilniro a == c hutro nethe
    miyol "a equals c".
dit
rilniro a == [1, 2, 3] hutro nethe
    miyol "a equals a new list with the same elements".
dit thumku nethe
    miyol "a does not equal a new list with the same elements".
dit
```

Output:

```
[1, 2, 3]
a equals c
a equals a new list with the same elements
```

### Logic and conditions

Conditions must be booleans: there is no "truthiness", and using an integer,
string, list or `emletlel` as a condition is an error. The operands of
`lotvethu`, `nime` and `yothicho` must also be booleans.

`lotvethu` and `nime` evaluate their right operand only when needed: if the
left operand of `lotvethu` is `litthi`, or the left operand of `nime`
is `ronuthit`, the right operand is not evaluated.

```
rimli check(name, result) nethe
    miyol "checking " & name.
    yiletho result.
dit

rilniro check("left", ronuthit) nime check("right", litthi) hutro nethe
    miyol "yes".
dit
rilniro check("left", litthi) lotvethu check("right", ronuthit) hutro nethe
    miyol "yes".
dit thumku nethe
    miyol "no".
dit
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
rilniro <condition> hutro nethe
    <statements>
dit thumku rilniro <condition> hutro nethe
    <statements>
dit thumku nethe
    <statements>
dit
```

- The `thumku rilniro ...` part may appear any number of times, including not at all.
- The `thumku nethe ...` part is optional.

The conditions are tested in order, and the statements of the first true
one run. If none is true, the statements of the final branch without a
condition run, if there is one.

```
ohetdi n = 7.
rilniro n < 5 hutro nethe
    miyol "small".
dit thumku rilniro n < 10 hutro nethe
    miyol "medium".
dit thumku nethe
    miyol "large".
dit
```

Output:

```
medium
```

### Choosing by value

```
thi torelro <expression>
torelro <literal>, ...
    <statements>
torelro thumku
    <statements>
dit thi
```

- The `torelro ...` part may appear any number of times, including not at all.
- The `torelro thumku ...` part is optional.

The expression is evaluated once and compared with each literal in order,
using `==`. Literals are integers or strings, and must all be
different. Only the statements of the matching case run (or the default part,
if none matches and there is one). `chet` inside it refers to the enclosing loop, not
to this statement.

```
lemyunom d = 1 thikutli 4 mitho nethe
    thi torelro d
    torelro 1
        miyol "one".
    torelro 2, 3
        miyol "two or three".
    torelro thumku
        miyol "something else".
    dit thi
dit
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
konit <condition> mitho nethe
    <statements>
dit
```

The condition is tested before each pass; the loop ends when it is
`litthi`.

```
ohetdi n = 1.
konit n < 100 mitho nethe
    n = n * 2.
dit
miyol n.
```

Output:

```
128
```

### Repeat-until loops

```
yolo
    <statements>
erote <condition>.
```

The statements run once, then again **until** the condition is `ronuthit`.
The condition is tested after each pass.

```
ohetdi n = 0.
yolo
    n = n + 3.
erote n > 10.
miyol n.
```

Output:

```
12
```

### Counting loops

```
lemyunom <name> = <start> thikutli <limit> rodilvul <step> mitho nethe
    <statements>
dit
```

- The `rodilvul ...` part is optional.

The start, limit and step are evaluated once, before the loop begins; the
step defaults to `1` and must not be `0`. The variable starts at the start
value and changes by the step after each pass. The loop runs while the variable has not passed the
limit; **the limit itself is included**.

```
lemyunom i = 1 thikutli 5 mitho nethe
    motdi i & " ".
dit
miyol "".
lemyunom i = 10 thikutli 1 rodilvul -3 mitho nethe
    motdi i & " ".
dit
miyol "".
```

Output:

```
1 2 3 4 5 
10 7 4 1 
```

### Leaving loops early

```
chet.
```

```
lidutle.
```

`chet` leaves the innermost loop. `lidutle` skips to the next pass of
the innermost loop (for a counting or for loop, the update still happens).

```
lemyunom i = 1 thikutli 10 mitho nethe
    rilniro i kolethul 2 == 0 hutro nethe
        lidutle.
    dit
    rilniro i > 7 hutro nethe
        chet.
    dit
    motdi i & " ".
dit
miyol "".
```

Output:

```
1 3 5 7 
```

## 7. Functions

```
rimli <name>(<parameter>, ...) nethe
    <statements>
dit
```

- The list of parameters may be empty.

Functions are declared at the top level of a program, not inside other
statements, and may be called before their declaration. Calling a function
with the wrong number of arguments is an error. Recursion is allowed.

```
yiletho <expression>.
```

- `<expression>` is optional.

`yiletho` ends the function and gives back the value, or `emletlel`
without one. A function that ends without `yiletho` returns `emletlel`.
A `yiletho` in top-level code ends the program.

A call can be used as a statement, which discards its result:

```
<function>(<argument>, ...).
```

- The list of arguments may be empty.

```
rimli square(x) nethe
    yiletho x * x.
dit

rimli fact(n) nethe
    rilniro n <= 1 hutro nethe
        yiletho 1.
    dit
    yiletho n * fact(n - 1).
dit

rimli greet(name) nethe
    miyol "Hello, " & name.
dit

miyol square(7).
miyol fact(10).
greet("Lin").
ohetdi r = greet("Max").
miyol r.
```

Output:

```
49
3628800
Hello, Lin
Hello, Max
emletlel
```

## 8. Errors

Errors found before running, such as syntax errors, unknown names and wrong
argument counts, stop the program before anything runs. Errors found while
running stop it at that point. In both cases, the message names the line.

```
miyol "before".
miyol 1 / 0.
miyol "after".
```

Output:

```
before
error: line 2: division by zero
```

## 9. Builtin functions

| Function | Description |
|---|---|
| `yuyem` | `(x)`: the number of elements of list `x`, or the number of characters of string `x`. |
| `nimhol` | `(xs, v)`: appends `v` to the end of list `xs` (changing it) and returns `emletlel`. |
| `chul` | `(v)`: converts any value to the string that printing it would show. |
| `nelchiyul` | `(s)`: converts a string of decimal digits (optionally with a leading `-`, surrounding spaces allowed) to an integer. An integer is returned unchanged. Anything else is an error. |
| `nilhino` | `()`: reads the next line of standard input and returns it as a string without the line ending, or `emletlel` when there is no more input. |

```
ohetdi xs = [3, 1].
nimhol(xs, 4).
miyol yuyem(xs).
miyol yuyem("hello").
miyol chul(42) & "!".
miyol nelchiyul("12") + 1.
miyol nilhino().
miyol nilhino().
miyol nilhino().
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
emletlel
```

## 10. A complete program

This program reads integers, one per line, until the input ends, and prints
how many there were, their sum and the largest.

```
ohetdi total = 0.
ohetdi seen = 0.
ohetdi best = 0.
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi n = nelchiyul(line).
    rilniro seen == 0 hutro nethe
        best = n.
    dit thumku rilniro n > best hutro nethe
        best = n.
    dit
    total = total + n.
    seen = seen + 1.
    line = nilhino().
dit
miyol "count " & seen.
miyol "sum " & total.
miyol "max " & best.
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

Write a Vetthimni program that prints the integers from 1 to `n`, one per
line. If `n` is 0, print nothing.


## Task ID: t0-day-names

# Day names

Standard input contains zero or more lines, each holding one integer.

Write a Vetthimni program that prints one line for each input line: the name
of the day of the week for numbers 1 to 7 (`Monday` for 1, `Tuesday` for 2,
`Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday` for 7), and
`invalid` for any other number.


## Task ID: t0-even-odd

# Even and odd

Standard input contains zero or more lines, each holding one integer
(possibly negative, with absolute value at most 1,000,000).

Write a Vetthimni program that counts how many of the integers are even and
how many are odd, and prints exactly two lines:

```
even <number of even integers>
odd <number of odd integers>
```


## Task ID: t0-factorial

# Factorial

Standard input contains one line with an integer `n` (0 ≤ n ≤ 20).

Write a Vetthimni program that prints `n!`, the product of the integers from
1 to `n`. By definition, `0!` is 1.


## Task ID: t0-fizzbuzz

# FizzBuzz

Standard input contains one line with an integer `n` (1 ≤ n ≤ 1000).

Write a Vetthimni program that prints one line for each integer `i` from 1
to `n`:

- `FizzBuzz` if `i` is divisible by both 3 and 5,
- otherwise `Fizz` if `i` is divisible by 3,
- otherwise `Buzz` if `i` is divisible by 5,
- otherwise the number `i` itself.


## Task ID: t0-hello

# Hello

Write a Vetthimni program that prints exactly this line:

```
Hello, Utopia!
```


## Task ID: t0-reverse-lines

# Reverse lines

Standard input contains zero or more lines of text.

Write a Vetthimni program that prints the same lines in reverse order: the
last line first and the first line last. Print each line exactly as it was
read.

