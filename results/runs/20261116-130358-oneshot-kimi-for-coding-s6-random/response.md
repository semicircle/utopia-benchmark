<solution task="t0-count">
troufu n = shufa(bounfou());
sutrarsu i = 1 sou n
    binmi i;
moun i
</solution>

<solution task="t0-day-names">
troufu line = bounfou();
tafashou line ~= furfifan
    troufu d = shufa(line);
    utir (d) {
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
troufu even = 0;
troufu odd = 0;
troufu line = bounfou();
tafashou line ~= furfifan
    troufu n = shufa(line);
    sitrartu (n % 2) == 0 fisu drufirsa
        even = even + 1;
    drumin tru drufirsa
        odd = odd + 1;
    drumin
    line = bounfou();
trushou
binmi "even " + even;
binmi "odd " + odd;
</solution>

<solution task="t0-factorial">
troufu n = shufa(bounfou());
troufu result = 1;
sutrarsu i = 1 sou n
    result = result * i;
moun i
binmi result;
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
troufu k = utoufa(lines);
tafashou k >= 1
    binmi lines[k];
    k = k - 1;
trushou
</solution>