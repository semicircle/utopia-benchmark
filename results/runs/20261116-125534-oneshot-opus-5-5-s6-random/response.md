Notes on how these solutions follow the reference:

- **Precedence:** all binary operators share one precedence and group right to left. So remainder tests are written as `(n % 2) == 0`. Written without parentheses, `n % 2 == 0` would parse as `n % (2 == 0)`.
- **`basu` inside `utir`:** it ends the `utir` statement, not the surrounding loop. The reference's second switch example shows this.
- **Counting loops:** they include the limit. A loop whose start is already past the limit runs zero times, so `n = 0` and empty input need no special handling.
- **Reading input:** the line-reading loops stop when `bounfou()` returns `furfifan`.

<solution task="t0-count">
troufu n = shufa(bounfou());
sutrarsu i = 1 sou n
    binmi i;
moun i
</solution>

<solution task="t0-day-names">
troufu line = bounfou();
tafashou line ~= furfifan
    troufu n = shufa(line);
    utir (n) {
    sourmar 1:
        binmi "Monday";
        basu;
    sourmar 2:
        binmi "Tuesday";
        basu;
    sourmar 3:
        binmi "Wednesday";
        basu;
    sourmar 4:
        binmi "Thursday";
        basu;
    sourmar 5:
        binmi "Friday";
        basu;
    sourmar 6:
        binmi "Saturday";
        basu;
    sourmar 7:
        binmi "Sunday";
        basu;
    fitru:
        binmi "invalid";
    }
    line = bounfou();
trushou
</solution>

<solution task="t0-even-odd">
troufu evens = 0;
troufu odds = 0;
troufu line = bounfou();
tafashou line ~= furfifan
    troufu n = shufa(line);
    sitrartu (n % 2) == 0 fisu drufirsa
        evens = evens + 1;
    drumin tru drufirsa
        odds = odds + 1;
    drumin
    line = bounfou();
trushou
binmi "even " + evens;
binmi "odd " + odds;
</solution>

<solution task="t0-factorial">
troufu n = shufa(bounfou());
troufu f = 1;
sutrarsu i = 1 sou n
    f = f * i;
moun i
binmi f;
</solution>

<solution task="t0-fizzbuzz">
troufu n = shufa(bounfou());
sutrarsu i = 1 sou n
    sitrartu (i % 15) == 0 fisu drufirsa
        binmi "FizzBuzz";
    drumin tru sitrartu (i % 3) == 0 fisu drufirsa
        binmi "Fizz";
    drumin tru sitrartu (i % 5) == 0 fisu drufirsa
        binmi "Buzz";
    drumin tru drufirsa
        binmi i;
    drumin
moun i
</solution>

<solution task="t0-hello">
binmi "Hello, Utopia!";
</solution>

<solution task="t0-reverse-lines">
troufu lines = [];
troufu line = bounfou();
tafashou line ~= furfifan
    marboun(lines, line);
    line = bounfou();
trushou
troufu count = utoufa(lines);
sutrarsu i = count sou 1 suntru -1
    binmi lines[i];
moun i
</solution>