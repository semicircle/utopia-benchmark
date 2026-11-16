<solution task="t0-count">
troufu n = shufa(bounfou());
sutrarsu i = 1 sou n
    binmi i;
moun i
</solution>

<solution task="t0-day-names">
troufu line = bounfou();
tafashou line ~= furfifan
    sitrartu line ~= "" fisu drufirsa
        troufu d = shufa(line);
        utir (d) {
        sourmar 1:
            binmi "Monday";
        sourmar 2:
            binmi "Tuesday";
        sourmar 3:
            binmi "Wednesday";
        sourmar 4:
            binmi "Thursday";
        sourmar 5:
            binmi "Friday";
        sourmar 6:
            binmi "Saturday";
        sourmar 7:
            binmi "Sunday";
        fitru:
            binmi "invalid";
        }
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t0-even-odd">
troufu evens = 0;
troufu odds = 0;
troufu line = bounfou();
tafashou line ~= furfifan
    sitrartu line ~= "" fisu drufirsa
        troufu n = shufa(line);
        sitrartu n % 2 == 0 fisu drufirsa
            evens = evens + 1;
        drumin tru drufirsa
            odds = odds + 1;
        drumin
    drumin
    line = bounfou();
trushou
binmi "even " + evens;
binmi "odd " + odds;
</solution>

<solution task="t0-factorial">
troufu n = shufa(bounfou());
troufu f = 1;
sutrarsu i = 2 sou n
    f = f * i;
moun i
binmi f;
</solution>

<solution task="t0-fizzbuzz">
troufu n = shufa(bounfou());
sutrarsu i = 1 sou n
    sitrartu i % 15 == 0 fisu drufirsa
        binmi "FizzBuzz";
    drumin tru sitrartu i % 3 == 0 fisu drufirsa
        binmi "Fizz";
    drumin tru sitrartu i % 5 == 0 fisu drufirsa
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
troufu xs = [];
troufu line = bounfou();
tafashou line ~= furfifan
    marboun(xs, line);
    line = bounfou();
trushou
troufu i = utoufa(xs) - 1;
tafashou i >= 0
    binmi xs[i];
    i = i - 1;
trushou
</solution>