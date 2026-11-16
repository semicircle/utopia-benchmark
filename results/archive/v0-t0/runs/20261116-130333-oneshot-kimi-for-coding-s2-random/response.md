<solution task="t0-count">
goyu n <- druwol(uyotho()).
wego i <- 1 setru n
    suwe i.
trer i
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
goyu even <- 0.
goyu odd <- 0.
goyu line <- uyotho().
omethol line != gursume
    goyu n <- druwol(line).
    dre n trumguwu 2 == 0 ethur
        even <- even + 1.
    truthor
        odd <- odd + 1.
    wodrotru dre
    line <- uyotho().
shusushe
suwe "even " & even.
suwe "odd " & odd.
</solution>

<solution task="t0-factorial">
goyu n <- druwol(uyotho()).
goyu result <- 1.
wego i <- 1 setru n
    result <- result * i.
trer i
suwe result.
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
goyu count <- wumdror(lines).
wego i <- count - 1 setru 0 meshe -1
    suwe lines[i].
trer i
</solution>