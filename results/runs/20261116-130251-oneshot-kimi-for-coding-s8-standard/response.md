<solution task="t0-count">
plulai n := plaltai(playadu());
shoyo i := 1 busale n
    shaibe i;
pla i
</solution>

<solution task="t0-day-names">
plulai line := playadu();
edrushe line <> aiplai
    plulai d := plaltai(line);
    otai (d) {
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
plulai even := 0;
plulai odd := 0;
plulai line := playadu();
edrushe line <> aiplai
    plulai n := plaltai(line);
    atdoyal (n % 2 == 0) {
        even := even + 1;
    } bulbayo {
        odd := odd + 1;
    }
    line := playadu();
aitudre
shaibe "even " + even;
shaibe "odd " + odd;
</solution>

<solution task="t0-factorial">
plulai n := plaltai(playadu());
plulai result := 1;
shoyo i := 2 busale n
    result := result * i;
pla i
shaibe result;
</solution>

<solution task="t0-fizzbuzz">
plulai n := plaltai(playadu());
shoyo i := 1 busale n
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
plulai lines := [];
plulai line := playadu();
edrushe line <> aiplai
    sutse(lines, line);
    line := playadu();
aitudre
shoyo i := dra(lines) - 1 busale 0 ede -1
    shaibe lines[i];
pla i
</solution>