<solution task="t0-count">
plulai n := plaltai(playadu());
shoyo i := 1 busale n
    shaibe i;
pla i
</solution>

<solution task="t0-day-names">
plulai line := playadu();
edrushe line <> aiplai
    atdoyal (dra(line) > 0) {
        plulai v := plaltai(line);
        otai (v) {
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
    }
    line := playadu();
aitudre
</solution>

<solution task="t0-even-odd">
plulai ev := 0;
plulai od := 0;
plulai line := playadu();
edrushe line <> aiplai
    atdoyal (dra(line) > 0) {
        plulai v := plaltai(line);
        atdoyal (v % 2 == 0) {
            ev := ev + 1;
        } bulbayo {
            od := od + 1;
        }
    }
    line := playadu();
aitudre
shaibe "even " + ev;
shaibe "odd " + od;
</solution>

<solution task="t0-factorial">
plulai n := plaltai(playadu());
plulai f := 1;
shoyo i := 1 busale n
    f := f * i;
pla i
shaibe f;
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
plulai xs := [];
plulai line := playadu();
edrushe line <> aiplai
    sutse(xs, line);
    line := playadu();
aitudre
plulai i := dra(xs) - 1;
edrushe i >= 0
    shaibe xs[i];
    i := i - 1;
aitudre
</solution>