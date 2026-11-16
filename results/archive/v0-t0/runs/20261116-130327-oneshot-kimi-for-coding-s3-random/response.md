<solution task="t0-count">
Sogas n = Drak(Goshvovo());
Paxfasva (Sogas i = 1; i <= n; i = i + 1) {
    Dosfasho i;
}
</solution>

<solution task="t0-day-names">
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas d = Drak(line);
    Ishsi (d == 1) {
        Dosfasho "Monday";
    } Padri Ishsi (d == 2) {
        Dosfasho "Tuesday";
    } Padri Ishsi (d == 3) {
        Dosfasho "Wednesday";
    } Padri Ishsi (d == 4) {
        Dosfasho "Thursday";
    } Padri Ishsi (d == 5) {
        Dosfasho "Friday";
    } Padri Ishsi (d == 6) {
        Dosfasho "Saturday";
    } Padri Ishsi (d == 7) {
        Dosfasho "Sunday";
    } Padri {
        Dosfasho "invalid";
    }
    line = Goshvovo();
}
</solution>

<solution task="t0-even-odd">
Sogas even = 0;
Sogas odd = 0;
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas n = Drak(line);
    Ishsi (n Dodogo 2 == 0) {
        even = even + 1;
    } Padri {
        odd = odd + 1;
    }
    line = Goshvovo();
}
Dosfasho "even " + even;
Dosfasho "odd " + odd;
</solution>

<solution task="t0-factorial">
Sogas n = Drak(Goshvovo());
Sogas r = 1;
Paxfasva (Sogas i = 1; i <= n; i = i + 1) {
    r = r * i;
}
Dosfasho r;
</solution>

<solution task="t0-fizzbuzz">
Sogas n = Drak(Goshvovo());
Paxfasva (Sogas i = 1; i <= n; i = i + 1) {
    Ishsi (i Dodogo 15 == 0) {
        Dosfasho "FizzBuzz";
    } Padri Ishsi (i Dodogo 3 == 0) {
        Dosfasho "Fizz";
    } Padri Ishsi (i Dodogo 5 == 0) {
        Dosfasho "Buzz";
    } Padri {
        Dosfasho i;
    }
}
</solution>

<solution task="t0-hello">
Dosfasho "Hello, Utopia!";
</solution>

<solution task="t0-reverse-lines">
Sogas lines = [];
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Dragi(lines, line);
    line = Goshvovo();
}
Paxfasva (Sogas i = Drash(lines); i >= 1; i = i - 1) {
    Dosfasho lines[i];
}
</solution>