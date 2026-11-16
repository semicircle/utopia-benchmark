Points where Foshoxsho differs from common languages, and how the solutions handle them:

- **Parity:** division rounds toward positive infinity, so the remainder of an odd number divided by 2 can be `-1` instead of `1`. The even/odd test therefore only checks `x Dodogo 2 == 0`, which is correct for every integer.
- **Switch fall-through:** `Pidok` cases fall through to the next case, so every case ends with `Fosvas;`.
- **Indexing:** lists start at index 1, so the reverse loop runs from `Drash(lines)` down to 1.

<solution task="t0-count">
Sogas n = Drak(Goshvovo());
Paxfasva (Sogas i = 1; i <= n; i = i + 1) {
    Dosfasho i;
}
</solution>

<solution task="t0-day-names">
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas n = Drak(line);
    Pidok (n) {
    Dro 1:
        Dosfasho "Monday";
        Fosvas;
    Dro 2:
        Dosfasho "Tuesday";
        Fosvas;
    Dro 3:
        Dosfasho "Wednesday";
        Fosvas;
    Dro 4:
        Dosfasho "Thursday";
        Fosvas;
    Dro 5:
        Dosfasho "Friday";
        Fosvas;
    Dro 6:
        Dosfasho "Saturday";
        Fosvas;
    Dro 7:
        Dosfasho "Sunday";
        Fosvas;
    Papo:
        Dosfasho "invalid";
    }
    line = Goshvovo();
}
</solution>

<solution task="t0-even-odd">
Sogas evens = 0;
Sogas odds = 0;
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas n = Drak(line);
    Ishsi (n Dodogo 2 == 0) {
        evens = evens + 1;
    } Padri {
        odds = odds + 1;
    }
    line = Goshvovo();
}
Dosfasho "even " + evens;
Dosfasho "odd " + odds;
</solution>

<solution task="t0-factorial">
Sogas n = Drak(Goshvovo());
Sogas r = 1;
Paxfasva (Sogas i = 2; i <= n; i = i + 1) {
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