<solution task="t0-count">
weltuxle n := leidush(lono());
keit (weltuxle i := 1; i <= n; i := i + 1) {
    leshdei i;
}
</solution>

<solution task="t0-day-names">
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle n := leidush(line);
    nei (n == 1) {
        leshdei "Monday";
    } wogeish nei (n == 2) {
        leshdei "Tuesday";
    } wogeish nei (n == 3) {
        leshdei "Wednesday";
    } wogeish nei (n == 4) {
        leshdei "Thursday";
    } wogeish nei (n == 5) {
        leshdei "Friday";
    } wogeish nei (n == 6) {
        leshdei "Saturday";
    } wogeish nei (n == 7) {
        leshdei "Sunday";
    } wogeish {
        leshdei "invalid";
    }
    line := lono();
}
</solution>

<solution task="t0-even-odd">
weltuxle even := 0;
weltuxle odd := 0;
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle n := leidush(line);
    nei (n yeil 2 == 0) {
        even := even + 1;
    } wogeish {
        odd := odd + 1;
    }
    line := lono();
}
leshdei "even " + even;
leshdei "odd " + odd;
</solution>

<solution task="t0-factorial">
weltuxle n := leidush(lono());
weltuxle f := 1;
keit (weltuxle i := 2; i <= n; i := i + 1) {
    f := f * i;
}
leshdei f;
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
weltuxle i := dushzosh(lines);
krenul (i > 0) {
    i := i - 1;
    leshdei lines[i];
}
</solution>