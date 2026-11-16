<solution task="t0-count">
goyu n <- druwol(uyotho()).
wego i <- 1 setru n
    suwe i.
trer i
</solution>

<solution task="t0-day-names">
goyu line <- uyotho().
omethol line != gursume
    goyu d <- druwol(line).
    dre d == 1 ethur
        suwe "Monday".
    yuyuge d == 2 ethur
        suwe "Tuesday".
    yuyuge d == 3 ethur
        suwe "Wednesday".
    yuyuge d == 4 ethur
        suwe "Thursday".
    yuyuge d == 5 ethur
        suwe "Friday".
    yuyuge d == 6 ethur
        suwe "Saturday".
    yuyuge d == 7 ethur
        suwe "Sunday".
    truthor
        suwe "invalid".
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t0-even-odd">
goyu e <- 0.
goyu o <- 0.
goyu line <- uyotho().
omethol line != gursume
    goyu n <- druwol(line).
    dre n trumguwu 2 == 0 ethur
        e <- e + 1.
    truthor
        o <- o + 1.
    wodrotru dre
    line <- uyotho().
shusushe
suwe "even " & e.
suwe "odd " & o.
</solution>

<solution task="t0-factorial">
goyu n <- druwol(uyotho()).
goyu r <- 1.
wego i <- 1 setru n
    r <- r * i.
trer i
suwe r.
</solution>

<solution task="t0-fizzbuzz">
goyu n <- druwol(uyotho()).
wego i <- 1 setru n
    dre i trumguwu 15 == 0 ethur
        suwe "FizzBuzz".
    yuyuge i trumguwu 3 == 0 ethur
        suwe "Fizz".
    yuyuge i trumguwu 5 == 0 ethur
        suwe "Buzz".
    truthor
        suwe i.
    wodrotru dre
trer i
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
goyu k <- wumdror(lines).
omethol k > 0
    k <- k - 1.
    suwe lines[k].
shusushe
</solution>