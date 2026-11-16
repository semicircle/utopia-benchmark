<solution task="t0-count">
plulai n := plaltai(playadu());
shoyo i := 1 busale n + 1
    shaibe i;
pla i
</solution>

<solution task="t0-day-names">
plulai line := playadu();
edrushe line <> aiplai
    plulai n := plaltai(line);
    otai (n) {
    dai 1:
        shaibe "Monday";
    dai 2:
        shaibe "Tuesday";
    dai 3:
        shaibe "Wednesday";
    dai 4:
        shaibe "Thursday";
    dai 5:
        shaibe "Friday";
    dai 6:
        shaibe "Saturday";
    dai 7:
        shaibe "Sunday";
    efu:
        shaibe "invalid";
    }
    line := playadu();
aitudre
</solution>

<solution task="t0-even-odd">
plulai evens := 0;
plulai odds := 0;
plulai line := playadu();
edrushe line <> aiplai
    plulai n := plaltai(line);
    atdoyal (n % 2 == 0) {
        evens := evens + 1;
    } bulbayo {
        odds := odds + 1;
    }
    line := playadu();
aitudre
shaibe "even " + evens;
shaibe "odd " + odds;
</solution>

<solution task="t0-factorial">
plulai n := plaltai(playadu());
plulai f := 1;
shoyo i := 2 busale n + 1
    f := f * i;
pla i
shaibe f;
</solution>

<solution task="t0-fizzbuzz">
plulai n := plaltai(playadu());
shoyo i := 1 busale n + 1
    atdoyal (i % 15 == 0) {
        shaibe "FizzBuzz";
    } bulbayo atdoyal (i % 3 == 0) {
        shaibe "Fizz";
    } bulbayo atdoyal (i % 5 == 0) {
        shaibe "Buzz";
    } bulbayo {
        shaibe i;
    }
pla i
</solution>

<solution task="t0-hello">
shaibe "Hello, Utopia!";
</solution>

<solution task="t0-reverse-lines">
plulai xs := [];
plulai line := playadu();
edrushe line <> aiplai
    sutse(xs, line);
    line := playadu();
aitudre
shoyo i := dra(xs) busale 0 ede -1
    shaibe xs[i];
pla i
</solution>