Notes on the Wochu rules that affect these solutions:

- **Remainder:** division rounds up, so `7 yeil 2` is `-1`. Every divisibility test therefore checks `x yeil k == 0`. This holds for any sign, because the remainder is 0 exactly when the division is exact.
- **Empty lines:** in the tasks that read numbers, empty input lines are skipped, since `leidush` would fail on them. In the reverse-lines task, empty lines are kept exactly as read.

<solution task="t0-count">
weltuxle n := leidush(lono());
keit (weltuxle i := 1; i <= n; i := i + 1) {
    leshdei i;
}
</solution>

<solution task="t0-day-names">
weltuxle line := lono();
krenul (line <> leitchux) {
    nei (dushzosh(line) > 0) {
        weltuxle d := leidush(line);
        yishzit d eixwo
        1: krei
            leshdei "Monday";
        zushox
        2: krei
            leshdei "Tuesday";
        zushox
        3: krei
            leshdei "Wednesday";
        zushox
        4: krei
            leshdei "Thursday";
        zushox
        5: krei
            leshdei "Friday";
        zushox
        6: krei
            leshdei "Saturday";
        zushox
        7: krei
            leshdei "Sunday";
        zushox
        wogeish krei
            leshdei "invalid";
        zushox zushox
    }
    line := lono();
}
</solution>

<solution task="t0-even-odd">
weltuxle evens := 0;
weltuxle odds := 0;
weltuxle line := lono();
krenul (line <> leitchux) {
    nei (dushzosh(line) > 0) {
        weltuxle v := leidush(line);
        nei (v yeil 2 == 0) {
            evens := evens + 1;
        } wogeish {
            odds := odds + 1;
        }
    }
    line := lono();
}
leshdei "even " + evens;
leshdei "odd " + odds;
</solution>

<solution task="t0-factorial">
weltuxle n := leidush(lono());
weltuxle r := 1;
keit (weltuxle i := 2; i <= n; i := i + 1) {
    r := r * i;
}
leshdei r;
</solution>

<solution task="t0-fizzbuzz">
weltuxle n := leidush(lono());
keit (weltuxle i := 1; i <= n; i := i + 1) {
    nei (i yeil 15 == 0) {
        leshdei "FizzBuzz";
    } wogeish nei (i yeil 3 == 0) {
        leshdei "Fizz";
    } wogeish nei (i yeil 5 == 0) {
        leshdei "Buzz";
    } wogeish {
        leshdei i;
    }
}
</solution>

<solution task="t0-hello">
leshdei "Hello, Utopia!";
</solution>

<solution task="t0-reverse-lines">
weltuxle lines := [];
weltuxle line := lono();
krenul (line <> leitchux) {
    koshkil(lines, line);
    line := lono();
}
keit (weltuxle i := dushzosh(lines) - 1; i >= 0; i := i - 1) {
    leshdei lines[i];
}
</solution>