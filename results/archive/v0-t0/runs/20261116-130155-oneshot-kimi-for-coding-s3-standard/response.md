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
    Pidok (d) {
    Dro 1:
        Dosfasho "Monday";
    Dro 2:
        Dosfasho "Tuesday";
    Dro 3:
        Dosfasho "Wednesday";
    Dro 4:
        Dosfasho "Thursday";
    Dro 5:
        Dosfasho "Friday";
    Dro 6:
        Dosfasho "Saturday";
    Dro 7:
        Dosfasho "Sunday";
    Papo:
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
Sogas f = 1;
Paxfasva (Sogas i = 2; i <= n; i = i + 1) {
    f = f * i;
}
Dosfasho f;
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
Paxfasva (Sogas i = Drash(lines) - 1; i >= 0; i = i - 1) {
    Dosfasho lines[i];
}
</solution>