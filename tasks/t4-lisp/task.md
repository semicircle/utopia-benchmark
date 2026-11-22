# Lisp interpreter

Standard input holds a program in a small Lisp. Write a {{.Lang}} program
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
