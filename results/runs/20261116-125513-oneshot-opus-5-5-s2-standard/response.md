Notes on the Gutrur rules these solutions rely on:

- **End of input:** comparing a string with `gursume` using `!=` gives `sudru`, because values of different types are never equal. So `line != gursume` is a valid end-of-input test.
- **Loops:** I used `omethol` (while) loops with explicit counters. This avoids any doubt about whether a counting loop with an empty range, such as `1 setru 0`, runs.
- **Parity:** `trumguwu` binds tighter than `==`. Negative odd numbers give a remainder of `-1`, so testing `== 0` is correct for negative inputs too.
- **Factorial:** 20! fits in a 64-bit integer, so there is no overflow.

<solution task="t0-count">
goyu n <- druwol(uyotho()).
goyu i <- 1.
omethol i <= n
    suwe i.
    i <- i + 1.
shusushe
</solution>

<solution task="t0-day-names">
goyu line <- uyotho().
omethol line != gursume
    goyu n <- druwol(line).
    wem gugum n
    gugum 1
        suwe "Monday".
    gugum 2
        suwe "Tuesday".
    gugum 3
        suwe "Wednesday".
    gugum 4
        suwe "Thursday".
    gugum 5
        suwe "Friday".
    gugum 6
        suwe "Saturday".
    gugum 7
        suwe "Sunday".
    gugum truthor
        suwe "invalid".
    wodrotru wem
    line <- uyotho().
shusushe
</solution>

<solution task="t0-even-odd">
goyu evens <- 0.
goyu odds <- 0.
goyu line <- uyotho().
omethol line != gursume
    goyu n <- druwol(line).
    dre n trumguwu 2 == 0 ethur
        evens <- evens + 1.
    truthor
        odds <- odds + 1.
    wodrotru dre
    line <- uyotho().
shusushe
suwe "even " & evens.
suwe "odd " & odds.
</solution>

<solution task="t0-factorial">
goyu n <- druwol(uyotho()).
goyu r <- 1.
goyu i <- 2.
omethol i <= n
    r <- r * i.
    i <- i + 1.
shusushe
suwe r.
</solution>

<solution task="t0-fizzbuzz">
goyu n <- druwol(uyotho()).
goyu i <- 1.
omethol i <= n
    dre i trumguwu 15 == 0 ethur
        suwe "FizzBuzz".
    yuyuge i trumguwu 3 == 0 ethur
        suwe "Fizz".
    yuyuge i trumguwu 5 == 0 ethur
        suwe "Buzz".
    truthor
        suwe i.
    wodrotru dre
    i <- i + 1.
shusushe
</solution>

<solution task="t0-hello">
suwe "Hello, Utopia!".
</solution>

<solution task="t0-reverse-lines">
goyu lines <- [].
goyu line <- uyotho().
omethol line != gursume
    dreme(lines, line).
    line <- uyotho().
shusushe
goyu i <- wumdror(lines) - 1.
omethol i >= 0
    suwe lines[i].
    i <- i - 1.
shusushe
</solution>