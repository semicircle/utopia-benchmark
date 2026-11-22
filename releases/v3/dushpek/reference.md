# The Dushpek Language Reference

Dushpek is a small programming language. This reference is complete: it
describes everything the language and its toolchain do. Where Dushpek
differs from languages you may know, the difference is deliberate, so follow
this document rather than habit.

Every example in this reference was run with the real toolchain, and the
output shown is exactly what it printed.

## 1. Running programs

Dushpek source files use the extension `.dus`. The toolchain is a
single program named `dushpek`:

```
dushpek run program.dus      # check and run a program
dushpek check program.dus    # only check it for errors, without running it
```

A program reads from standard input and writes to standard output. If an
error occurs, `dushpek` prints a message to standard error and exits with
status 1. Output printed before the error is kept.

A program may run at most 50,000,000 steps and nest at most 10,000 function
calls. Exceeding either limit is an error.

## 2. Lexical structure

**Layout.** Spaces, tabs, line breaks and indentation have no meaning; use
them freely for readability. A comment starts with `//` and runs to
the end of the line.

**Statement terminator.** Simple statements (declarations, assignments,
calls, printing, jumps, `Pohuwu`, `Kewi`, `Gosh`) end with
`.`. Compound statements such as conditionals and loops do not need
one after them, but their syntax is shown in full below.

**Names** of variables, functions and labels are made of letters, digits
and `_`, and must not start with a digit. Names are case-sensitive.

**Keywords** are reserved and cannot be used as names. They are
case-sensitive and must be written exactly as shown:

| Keyword | Meaning |
|---|---|
| `Dak` | logical or |
| `Drix` | part of: counting loop |
| `Dru` | part of: switch statement |
| `Ebi` | part of: print statement |
| `Eshdoyi` | part of: repeat-until loop |
| `Geklabik` | the boolean value true |
| `Gihe` | part of: while loop, counting loop |
| `Gipolu` | part of: counting loop |
| `Gosh` | part of: continue statement |
| `Gukdidok` | logical not |
| `Hehokgi` | part of: switch statement, while loop, counting loop |
| `Hishyeko` | part of: switch statement |
| `Ihedrux` | part of: switch statement |
| `Kewi` | part of: break statement |
| `Kobihek` | part of: switch statement, while loop, counting loop |
| `Koke` | part of: variable declaration |
| `Lesh` | the boolean value false |
| `Liliga` | the value none |
| `Okdro` | logical and |
| `Peshdro` | part of: repeat-until loop |
| `Pohuwu` | part of: return statement |
| `Puwadish` | part of: while loop |
| `Uxdrush` | part of: jump |
| `Wexdush` | part of: counting loop |
| `Wuhadi` | part of: write statement |
| `Yokyi` | part of: function declaration |
| `Yopok` | part of: conditional jump |

The builtin function names (section 9) are also reserved.

**Literals.** Integers are written in decimal (`0`, `42`, `1000`); there are
no fractions. A negative number is written with a minus sign (`-5`). Strings
are written between double quotes, such as `"hello"`. Inside a string, `\n`
is a line break, `\t` a tab, `\"` a double quote and `\\` a backslash.
Booleans are `Geklabik` and `Lesh`. The value `Liliga` means "no
value".

## 3. Values

| Type | Examples | Notes |
|---|---|---|
| integer | `0`, `-7`, `123` | 64-bit; overflow wraps around |
| string | `"hi"`, `""` | a sequence of characters; cannot be changed in place |
| boolean | `Geklabik`, `Lesh` | the only values allowed as conditions |
| list | `[1, 2, 3]`, `[]`, `["a", 1]` | mutable; may mix types |
| none | `Liliga` | "no value"; returned by functions that return nothing |

Lists are shared, not copied: assigning a list to another variable, or
passing it to a function, gives access to the same list.

```
Yokyi addOne(xs) {
    Oxba(xs, 1).
}

Koke mine := [5].
addOne(mine).
Ebi mine.
```

Output:

```
[5, 1]
```

Printing shows integers in decimal, strings without quotes, booleans and
`Liliga` as their keywords, and lists in brackets with strings quoted.

## 4. Variables and simple statements

A variable must be declared before it is used:

```
Koke <name> := <expression>.
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

`Ebi` prints a value followed by a line break. `Wuhadi` prints a
value without a line break.

```
Ebi <expression>.
```

```
Wuhadi <expression>.
```

```
Koke x := 5.
x := x + 2.
Koke name := "Ada".
Ebi name ++ " has " ++ x ++ " apples".
Koke flag := x > 6.
Ebi flag.
Ebi Liliga.
```

Output:

```
Ada has 7 apples
Geklabik
Liliga
```

## 5. Expressions

### Operators

| Operator | Meaning |
|---|---|
| `-x` | negation |
| `Gukdidok x` | logical not |
| `a * b` | multiplication |
| `a / b` | integer division (see below) |
| `a % b` | remainder (see below) |
| `a + b` | addition |
| `a - b` | subtraction |
| `a ++ b` | joining text (see below) |
| `a == b` | equal |
| `a /= b` | not equal |
| `a < b`, `a <= b`, `a > b`, `a >= b` | ordering |
| `a Okdro b` | logical and |
| `a Dak b` | logical or |

Note the spellings: assignment is `:=` and equality is `==`.

### Grouping and precedence

**All binary operators have the same precedence and group from left to
right.** There is no "multiplication first" rule: `2 + 3 * 4` means
`(2 + 3) * 4`. This applies to every binary operator, including comparisons
and `Okdro`/`Dak`, so `a < b Okdro c < d` means
`((a < b) Okdro c) < d`; write `(a < b) Okdro (c < d)` instead. Negation
and `Gukdidok` bind tighter than any binary operator. Parentheses group explicitly.

```
Ebi 2 + 3 * 4.
Ebi 10 - 4 - 3.
Ebi (2 + 3) * 4.
Ebi 2 + (3 * 4).
```

Output:

```
20
3
20
14
```

### Order of evaluation

**The two operands of a binary operator are evaluated right operand first**,
then the left one.

```
Yokyi show(x) {
    Ebi "evaluating " ++ x.
    Pohuwu x.
}

Ebi show(10) - show(4).
```

Output:

```
evaluating 4
evaluating 10
6
```

**Arguments of a function call are evaluated from right to left**: the last
argument first. They are still passed in the order written.

```
Yokyi show(x) {
    Ebi "evaluating " ++ x.
    Pohuwu x.
}

Yokyi pair(a, b) {
    Pohuwu a ++ b.
}

Ebi pair(show(1), show(2)).
```

Output:

```
evaluating 2
evaluating 1
12
```

### Integer arithmetic

Division of integers gives an integer. **The exact result is rounded up, toward positive infinity**, so
`7 / 2` is `4` and `-7 / 2` is `-3`. The remainder `a % b` is always `a - b * (a / b)` using that
division, so its sign follows from the rounding rule. Dividing by zero is an
error.

```
Ebi 7 / 2.
Ebi -7 / 2.
Ebi 7 % 2.
Ebi -7 % 2.
Ebi 6 / 3.
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

`++` converts both operands to text (as printing would show them)
and joins them. `+` only adds integers.

```
Ebi "n = " ++ 5.
Ebi "a" ++ "b" ++ "c".
```

Output:

```
n = 5
abc
```

Strings can be compared with `<`, `<=`, `>` and `>=`, character by character
(by character code). Comparing values of different types with `==` gives
`Lesh`; ordering them is an error.

### Lists and indexing

`x[i]` is element `i` of list `x`, or the one-character string at position
`i` of string `x`. **Indexes start at 1**: the first element
is `x[1]`. List elements can be replaced with `x[i] := value.`.

```
<name>[<index>] := <expression>.
```

```
Koke xs := [10, 20, 30].
Ebi xs[1].
xs[1] := 99.
Ebi xs.
Koke word := "abc".
Ebi word[1].
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
Koke xs := [10, 20, 30].
Ebi xs[3].
Ebi xs[4].
Ebi xs[-1].
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
Koke a := [1, 2].
Koke b := [1, 2].
Koke c := a.
Oxba(c, 3).
Ebi a.
Yopok a /= c, endif1.
Ebi "a equals c".
endif1:
Yopok a /= [1, 2, 3], else3.
Ebi "a equals a new list with the same elements".
Uxdrush endif2.
else3:
Ebi "a does not equal a new list with the same elements".
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
string, list or `Liliga` as a condition is an error. The operands of
`Okdro`, `Dak` and `Gukdidok` must also be booleans.

`Okdro` and `Dak` evaluate their right operand only when needed: if the
left operand of `Okdro` is `Lesh`, or the left operand of `Dak`
is `Geklabik`, the right operand is not evaluated.

```
Yokyi check(name, result) {
    Ebi "checking " ++ name.
    Pohuwu result.
}

Yopok Gukdidok (check("left", Geklabik) Dak check("right", Lesh)), endif1.
Ebi "yes".
endif1:
Yopok Gukdidok (check("left", Lesh) Okdro check("right", Geklabik)), else3.
Ebi "yes".
Uxdrush endif2.
else3:
Ebi "no".
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
Dru <expression> Ihedrux
<literal>, ...: Hehokgi
    <statements>
Kobihek
Hishyeko Hehokgi
    <statements>
Kobihek Kobihek
```

- The `<literal> ...` part may appear any number of times, including not at all.
- The `Hishyeko Hehokgi ...` part is optional.

The expression is evaluated once and compared with each literal in order,
using `==`. Literals are integers or strings, and must all be
different. Only the statements of the matching case run (or the default part,
if none matches and there is one). `Kewi` inside it refers to the enclosing loop, not
to this statement.

```
Gipolu d := 1 Wexdush 4 Gihe Hehokgi
    Dru d Ihedrux
    1: Hehokgi
        Ebi "one".
    Kobihek
    2, 3: Hehokgi
        Ebi "two or three".
    Kobihek
    Hishyeko Hehokgi
        Ebi "something else".
    Kobihek Kobihek
Kobihek
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
Puwadish <condition> Gihe Hehokgi
    <statements>
Kobihek
```

The condition is tested before each pass; the loop ends when it is
`Lesh`.

```
Koke n := 1.
Puwadish n < 100 Gihe Hehokgi
    n := n * 2.
Kobihek
Ebi n.
```

Output:

```
128
```

### Repeat-until loops

```
Eshdoyi
    <statements>
Peshdro <condition>.
```

The statements run once, then again **until** the condition is `Geklabik`.
The condition is tested after each pass.

```
Koke n := 0.
Eshdoyi
    n := n + 3.
Peshdro n > 10.
Ebi n.
```

Output:

```
12
```

### Counting loops

```
Gipolu <name> := <start> Wexdush <limit> Drix <step> Gihe Hehokgi
    <statements>
Kobihek
```

- The `Drix ...` part is optional.

The start, limit and step are evaluated once, before the loop begins; the
step defaults to `1` and must not be `0`. The variable starts at the start
value and changes by the step after each pass. The loop runs while the variable has not passed the
limit; **the limit itself is included**.

```
Gipolu i := 1 Wexdush 5 Gihe Hehokgi
    Wuhadi i ++ " ".
Kobihek
Ebi "".
Gipolu i := 10 Wexdush 1 Drix -3 Gihe Hehokgi
    Wuhadi i ++ " ".
Kobihek
Ebi "".
```

Output:

```
1 2 3 4 5 
10 7 4 1 
```

### Leaving loops early

```
Kewi.
```

```
Gosh.
```

`Kewi` leaves the innermost loop. `Gosh` skips to the next pass of
the innermost loop (for a counting or for loop, the update still happens).

```
Yokyi div_(a, b) {
    Koke q := a / b.
    Koke r := a - (b * q).
    Yopok r == 0, endif3.
    Yopok r < 0 == (a < 0), endif4.
    Yopok r < 0 /= (b < 0), else6.
    q := q + 1.
    Uxdrush endif5.
else6:
    q := q - 1.
endif5:
endif4:
endif3:
    Pohuwu q.
}

Yokyi mod_(a, b) {
    Pohuwu a - (b * div_(a, b)).
}

Gipolu i := 1 Wexdush 10 Gihe Hehokgi
    Yopok mod_(i, 2) /= 0, endif1.
    Gosh.
endif1:
    Yopok i <= 7, endif2.
    Kewi.
endif2:
    Wuhadi i ++ " ".
Kobihek
Ebi "".
```

Output:

```
1 3 5 7 
```

### Labels and jumps
Dushpek has no if statement; decisions are made with conditional jumps.

A label marks a position in a function. It does not end with `.`:

```
<label>:
```

A jump continues execution at a label in the same function:

```
Uxdrush <label>.
```

A conditional jump jumps only if the condition is `Geklabik`; otherwise
execution continues with the next statement:

```
Yopok <condition>, <label>.
```

Each label name may be defined only once in a function. Jumps may go
forward or backward, and into or out of any block in the same function.

```
Koke n := 7.
Yopok n >= 5, else2.
Ebi "small".
Uxdrush endif1.
else2:
Yopok n >= 10, else3.
Ebi "medium".
Uxdrush endif1.
else3:
Ebi "large".
endif1:
```

Output:

```
medium
```

## 7. Functions

```
Yokyi <name>(<parameter>, ...) {
    <statements>
}
```

- The list of parameters may be empty.

Functions are declared at the top level of a program, not inside other
statements, and may be called before their declaration. Calling a function
with the wrong number of arguments is an error. Recursion is allowed.

```
Pohuwu <expression>.
```

- `<expression>` is optional.

`Pohuwu` ends the function and gives back the value, or `Liliga`
without one. A function that ends without `Pohuwu` returns `Liliga`.
A `Pohuwu` in top-level code ends the program.

A call can be used as a statement, which discards its result:

```
<function>(<argument>, ...).
```

- The list of arguments may be empty.

```
Yokyi square(x) {
    Pohuwu x * x.
}

Yokyi fact(n) {
    Yopok n > 1, endif1.
    Pohuwu 1.
endif1:
    Pohuwu n * fact(n - 1).
}

Yokyi greet(name) {
    Ebi "Hello, " ++ name.
}

Ebi square(7).
Ebi fact(10).
greet("Lin").
Koke r := greet("Max").
Ebi r.
```

Output:

```
49
3628800
Hello, Lin
Hello, Max
Liliga
```

## 8. Errors

Errors found before running, such as syntax errors, unknown names and wrong
argument counts, stop the program before anything runs. Errors found while
running stop it at that point. In both cases, the message names the line.

```
Ebi "before".
Ebi 1 / 0.
Ebi "after".
```

Output:

```
before
error: line 2: division by zero
```

## 9. Builtin functions

| Function | Description |
|---|---|
| `Yik` | `(x)`: the number of elements of list `x`, or the number of characters of string `x`. |
| `Oxba` | `(xs, v)`: appends `v` to the end of list `xs` (changing it) and returns `Liliga`. |
| `Yawishbo` | `(v)`: converts any value to the string that printing it would show. |
| `Bupuxbo` | `(s)`: converts a string of decimal digits (optionally with a leading `-`, surrounding spaces allowed) to an integer. An integer is returned unchanged. Anything else is an error. |
| `Pewexpo` | `()`: reads the next line of standard input and returns it as a string without the line ending, or `Liliga` when there is no more input. |

```
Koke xs := [3, 1].
Oxba(xs, 4).
Ebi Yik(xs).
Ebi Yik("hello").
Ebi Yawishbo(42) ++ "!".
Ebi Bupuxbo("12") + 1.
Ebi Pewexpo().
Ebi Pewexpo().
Ebi Pewexpo().
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
Liliga
```

## 10. A complete program

This program reads integers, one per line, until the input ends, and prints
how many there were, their sum and the largest.

```
Koke total := 0.
Koke seen := 0.
Koke best := 0.
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke n := Bupuxbo(line).
    Yopok seen /= 0, else2.
    best := n.
    Uxdrush endif1.
else2:
    Yopok n <= best, endif1.
    best := n.
endif1:
    total := total + n.
    seen := seen + 1.
    line := Pewexpo().
Kobihek
Ebi "count " ++ seen.
Ebi "sum " ++ total.
Ebi "max " ++ best.
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
