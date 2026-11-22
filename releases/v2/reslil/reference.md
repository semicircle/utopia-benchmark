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
