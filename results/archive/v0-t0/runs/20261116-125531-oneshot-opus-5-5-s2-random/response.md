<solution task="t0-count">
goyu n <- druwol(uyotho()).
dre n >= 1 ethur
    wego i <- 1 setru n
        suwe i.
    trer i
wodrotru dre
</solution>

<solution task="t0-day-names">
goyu line <- uyotho().
omethol line != gursume
    goyu d <- druwol(line).
    wem gugum d
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
    dre (n trumguwu 2) == 0 ethur
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
goyu p <- 1.
dre n >= 1 ethur
    wego i <- 1 setru n
        p <- p * i.
    trer i
wodrotru dre
suwe p.
</solution>

<solution task="t0-fizzbuzz">
goyu n <- druwol(uyotho()).
wego i <- 1 setru n
    dre (i trumguwu 15) == 0 ethur
        suwe "FizzBuzz".
    yuyuge (i trumguwu 3) == 0 ethur
        suwe "Fizz".
    yuyuge (i trumguwu 5) == 0 ethur
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
goyu xs <- [].
goyu line <- uyotho().
omethol line != gursume
    dreme(xs, line).
    line <- uyotho().
shusushe
dre wumdror(xs) > 0 ethur
    wego i <- (wumdror(xs) - 1) setru 0 meshe -1
        suwe xs[i].
    trer i
wodrotru dre
</solution>