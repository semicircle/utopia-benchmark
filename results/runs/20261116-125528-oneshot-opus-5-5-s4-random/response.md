<solution task="t0-count">
Trepiho n := Eshiyer(Thoke());
Pil (Trepiho i := 1; i <= n; i := i + 1) {
    Rashar i;
}
</solution>

<solution task="t0-day-names">
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho d := Eshiyer(line);
    Pakru Sher d
    Sher 1
        Rashar "Monday";
    Sher 2
        Rashar "Tuesday";
    Sher 3
        Rashar "Wednesday";
    Sher 4
        Rashar "Thursday";
    Sher 5
        Rashar "Friday";
    Sher 6
        Rashar "Saturday";
    Sher 7
        Rashar "Sunday";
    Sher Thotri
        Rashar "invalid";
    Tho Pakru
    line := Thoke();
}
</solution>

<solution task="t0-even-odd">
Trepiho evens := 0;
Trepiho odds := 0;
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho n := Eshiyer(line);
    Mushu n % 2 = 0 Yeshil Hupo
        evens := evens + 1;
    Tho Thotri Hupo
        odds := odds + 1;
    Tho
    line := Thoke();
}
Rashar "even " + evens;
Rashar "odd " + odds;
</solution>

<solution task="t0-factorial">
Trepiho n := Eshiyer(Thoke());
Trepiho f := 1;
Pil (Trepiho i := 2; i <= n; i := i + 1) {
    f := f * i;
}
Rashar f;
</solution>

<solution task="t0-fizzbuzz">
Trepiho n := Eshiyer(Thoke());
Pil (Trepiho i := 1; i <= n; i := i + 1) {
    Mushu i % 15 = 0 Yeshil Hupo
        Rashar "FizzBuzz";
    Tho Thotri Mushu i % 3 = 0 Yeshil Hupo
        Rashar "Fizz";
    Tho Thotri Mushu i % 5 = 0 Yeshil Hupo
        Rashar "Buzz";
    Tho Thotri Hupo
        Rashar i;
    Tho
}
</solution>

<solution task="t0-hello">
Rashar "Hello, Utopia!";
</solution>

<solution task="t0-reverse-lines">
Trepiho lines := [];
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Theki(lines, line);
    line := Thoke();
}
Pil (Trepiho i := Purmo(lines) - 1; i >= 0; i := i - 1) {
    Rashar lines[i];
}
</solution>