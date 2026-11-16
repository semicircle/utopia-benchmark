Notes on the Wokluwu rules these solutions rely on:
- Counting loops include their limit, and a loop whose start is already past the limit does not run. So `n = 0` prints nothing.
- `x % 2` is `-1` for negative odd numbers. The even test therefore compares the remainder with `0`.
- `TODETET()` returns `LER` at end of input, which ends each reading loop.

<solution task="t0-count">
FOMOFE n := ZENZUMUR(TODETET());
TUTCHEK i := 1 ZUWOWEN n LOLO LEKFESH
    EPLOWEK i;
EFUDU
</solution>

<solution task="t0-day-names">
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE d := ZENZUMUR(line);
    ZET d CHU
    1: LEKFESH
        EPLOWEK "Monday";
    EFUDU
    2: LEKFESH
        EPLOWEK "Tuesday";
    EFUDU
    3: LEKFESH
        EPLOWEK "Wednesday";
    EFUDU
    4: LEKFESH
        EPLOWEK "Thursday";
    EFUDU
    5: LEKFESH
        EPLOWEK "Friday";
    EFUDU
    6: LEKFESH
        EPLOWEK "Saturday";
    EFUDU
    7: LEKFESH
        EPLOWEK "Sunday";
    EFUDU
    CHEME LEKFESH
        EPLOWEK "invalid";
    EFUDU EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t0-even-odd">
FOMOFE evens := 0;
FOMOFE odds := 0;
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE n := ZENZUMUR(line);
    PLUWOK n % 2 = 0 DEWOTUSH LEKFESH
        evens := evens + 1;
    EFUDU CHEME LEKFESH
        odds := odds + 1;
    EFUDU
    line := TODETET();
EFUDU
EPLOWEK "even " & evens;
EPLOWEK "odd " & odds;
</solution>

<solution task="t0-factorial">
FOMOFE n := ZENZUMUR(TODETET());
FOMOFE f := 1;
TUTCHEK i := 2 ZUWOWEN n LOLO LEKFESH
    f := f * i;
EFUDU
EPLOWEK f;
</solution>

<solution task="t0-fizzbuzz">
FOMOFE n := ZENZUMUR(TODETET());
TUTCHEK i := 1 ZUWOWEN n LOLO LEKFESH
    PLUWOK i % 15 = 0 DEWOTUSH LEKFESH
        EPLOWEK "FizzBuzz";
    EFUDU CHEME PLUWOK i % 3 = 0 DEWOTUSH LEKFESH
        EPLOWEK "Fizz";
    EFUDU CHEME PLUWOK i % 5 = 0 DEWOTUSH LEKFESH
        EPLOWEK "Buzz";
    EFUDU CHEME LEKFESH
        EPLOWEK i;
    EFUDU
EFUDU
</solution>

<solution task="t0-hello">
EPLOWEK "Hello, Utopia!";
</solution>

<solution task="t0-reverse-lines">
FOMOFE lines := [];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    WESH(lines, line);
    line := TODETET();
EFUDU
FOMOFE k := FORMOWE(lines) - 1;
FUKCHEFE k >= 0 LOLO LEKFESH
    EPLOWEK lines[k];
    k := k - 1;
EFUDU
</solution>