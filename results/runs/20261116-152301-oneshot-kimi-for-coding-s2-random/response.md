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
goyu ev <- 0.
goyu od <- 0.
goyu line <- uyotho().
omethol line != gursume
    goyu n <- druwol(line).
    dre n trumguwu 2 == 0 ethur
        ev <- ev + 1.
    truthor
        od <- od + 1.
    wodrotru dre
    line <- uyotho().
shusushe
suwe "even " & ev.
suwe "odd " & od.
</solution>

<solution task="t0-factorial">
goyu n <- druwol(uyotho()).
goyu f <- 1.
wego i <- 2 setru n
    f <- f * i.
trer i
suwe f.
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
goyu lines <- [].
goyu line <- uyotho().
omethol line != gursume
    dreme(lines, line).
    line <- uyotho().
shusushe
goyu n <- wumdror(lines).
wego i <- 1 setru n
    suwe lines[n - i].
trer i
</solution>

<solution task="t1-digits">
dredrume digitsRev(s)
    goyu total <- 0.
    goyu rev <- "".
    goyu n <- wumdror(s).
    wego i <- 0 setru n - 1
        goyu c <- s[i].
        total <- total + druwol(c).
        rev <- c & rev.
    trer i
    goyu r <- [].
    dreme(r, total).
    dreme(r, druwol(rev)).
    odrol r.
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu n <- druwol(line).
    dre n < 0 ethur
        goyu res <- digitsRev(shodrewe(-n)).
        suwe res[0] & " -" & res[1].
    truthor
        goyu res <- digitsRev(shodrewe(n)).
        suwe res[0] & " " & res[1].
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t1-floordiv">
dredrume slice(s, i, j)
    goyu r <- "".
    wego k <- i setru j - 1
        r <- r & s[k].
    trer k
    odrol r.
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu n <- wumdror(line).
    goyu sp <- 0.
    wego i <- 0 setru n - 1
        dre line[i] == " " ethur
            sp <- i.
        wodrotru dre
    trer i
    goyu a <- druwol(slice(line, 0, sp)).
    goyu b <- druwol(slice(line, sp + 1, n)).
    goyu q <- a / b.
    goyu r <- a - (b * q).
    suwe q & " " & r.
    line <- uyotho().
shusushe
</solution>

<solution task="t1-palindromes">
dredrume isAlnum(c)
    odrol ((c >= "A") suyogur (c <= "Z")) drorsu ((c >= "a") suyogur (c <= "z")) drorsu ((c >= "0") suyogur (c <= "9")).
wodrotru dredrume

dredrume toLower(c)
    goyu ups <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    goyu los <- "abcdefghijklmnopqrstuvwxyz".
    wego i <- 0 setru 25
        dre c == ups[i] ethur
            odrol los[i].
        wodrotru dre
    trer i
    odrol c.
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu f <- "".
    goyu n <- wumdror(line).
    wego i <- 0 setru n - 1
        goyu c <- line[i].
        dre isAlnum(c) ethur
            f <- f & toLower(c).
        wodrotru dre
    trer i
    goyu m <- wumdror(f).
    goyu pal <- tru.
    wego i <- 0 setru m / 2 - 1
        dre f[i] != f[m - 1 - i] ethur
            pal <- sudru.
        wodrotru dre
    trer i
    dre pal ethur
        suwe "yes".
    truthor
        suwe "no".
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t1-rank">
goyu first <- uyotho().
goyu xs <- [].
goyu cur <- "".
goyu n <- wumdror(first).
wego i <- 0 setru n - 1
    dre first[i] == " " ethur
        dre wumdror(cur) > 0 ethur
            dreme(xs, druwol(cur)).
        wodrotru dre
        cur <- "".
    truthor
        cur <- cur & first[i].
    wodrotru dre
trer i
dre wumdror(cur) > 0 ethur
    dreme(xs, druwol(cur)).
wodrotru dre

goyu line <- uyotho().
omethol line != gursume
    goyu q <- druwol(line).
    goyu smaller <- 0.
    goyu present <- tru.
    goyu m <- wumdror(xs).
    wego i <- 0 setru m - 1
        dre xs[i] < q ethur
            smaller <- smaller + 1.
        wodrotru dre
        dre xs[i] == q ethur
            present <- sudru.
        wodrotru dre
    trer i
    dre present ethur
        suwe smaller & " found".
    truthor
        suwe smaller & " missing".
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t1-rotate">
goyu k <- druwol(uyotho()).
goyu items <- [].
goyu line <- uyotho().
omethol line != gursume
    dreme(items, line).
    line <- uyotho().
shusushe
goyu m <- wumdror(items).
dre m > 0 ethur
    goyu kk <- k trumguwu m.
    wego i <- 0 setru m - 1
        goyu idx <- (i - kk) trumguwu m.
        suwe items[idx].
    trer i
wodrotru dre
</solution>

<solution task="t1-weekday">
dredrume slice(s, i, j)
    goyu r <- "".
    wego k <- i setru j - 1
        r <- r & s[k].
    trer k
    odrol r.
wodrotru dredrume

dredrume weekday(y, m, d)
    dre m <= 2 ethur
        y <- y - 1.
    wodrotru dre
    goyu mm <- m.
    dre m > 2 ethur
        mm <- m - 3.
    truthor
        mm <- m + 9.
    wodrotru dre
    goyu doy <- (153 * mm + 2) / 5 + d - 1.
    goyu doe <- (y * 365) + (y / 4) - (y / 100) + (y / 400) + doy.
    goyu w <- doe trumguwu 7.
    wem gugum w
    gugum 0
        odrol "Wednesday".
    gugum 1
        odrol "Thursday".
    gugum 2
        odrol "Friday".
    gugum 3
        odrol "Saturday".
    gugum 4
        odrol "Sunday".
    gugum 5
        odrol "Monday".
    gugum 6
        odrol "Tuesday".
    wodrotru wem
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu y <- druwol(slice(line, 0, 4)).
    goyu m <- druwol(slice(line, 5, 7)).
    goyu d <- druwol(slice(line, 8, 10)).
    suwe weekday(y, m, d).
    line <- uyotho().
shusushe
</solution>

<solution task="t2-bignum">
dredrume slice(s, i, j)
    goyu r <- "".
    wego k <- i setru j - 1
        r <- r & s[k].
    trer k
    odrol r.
wodrotru dredrume

dredrume parseBig(s)
    goyu n <- wumdror(s).
    goyu ds <- [].
    wego i <- 0 setru n - 1
        dreme(ds, druwol(s[n - 1 - i])).
    trer i
    odrol ds.
wodrotru dredrume

dredrume bigToString(ds)
    goyu n <- wumdror(ds).
    dre n == 0 ethur
        odrol "0".
    wodrotru dre
    goyu hi <- n - 1.
    omethol (hi > 0) suyogur (ds[hi] == 0)
        hi <- hi - 1.
    shusushe
    goyu r <- "".
    wego i <- hi setru 0 meshe -1
        r <- r & shodrewe(ds[i]).
    trer i
    odrol r.
wodrotru dredrume

dredrume bigAdd(a, b)
    goyu r <- [].
    goyu carry <- 0.
    goyu i <- 0.
    goyu na <- wumdror(a).
    goyu nb <- wumdror(b).
    omethol (i < na) drorsu (i < nb) drorsu (carry != 0)
        goyu s <- carry.
        dre i < na ethur
            s <- s + a[i].
        wodrotru dre
        dre i < nb ethur
            s <- s + b[i].
        wodrotru dre
        dreme(r, s trumguwu 10).
        carry <- s / 10.
        i <- i + 1.
    shusushe
    odrol r.
wodrotru dredrume

dredrume bigMul(a, b)
    goyu na <- wumdror(a).
    goyu nb <- wumdror(b).
    goyu r <- [].
    wego i <- 0 setru na + nb - 1
        dreme(r, 0).
    trer i
    wego i <- 0 setru na - 1
        goyu carry <- 0.
        wego j <- 0 setru nb - 1
            goyu cur <- r[i + j] + (a[i] * b[j]) + carry.
            r[i + j] <- cur trumguwu 10.
            carry <- cur / 10.
        trer j
        goyu p <- i + nb.
        omethol carry > 0
            goyu cur <- r[p] + carry.
            r[p] <- cur trumguwu 10.
            carry <- cur / 10.
            p <- p + 1.
        shusushe
    trer i
    odrol r.
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu n <- wumdror(line).
    goyu sp <- 0.
    wego i <- 0 setru n - 1
        dre line[i] == " " ethur
            sp <- i.
        wodrotru dre
    trer i
    goyu a <- parseBig(slice(line, 0, sp)).
    goyu b <- parseBig(slice(line, sp + 1, n)).
    suwe bigToString(bigAdd(a, b)) & " " & bigToString(bigMul(a, b)).
    line <- uyotho().
shusushe
</solution>

<solution task="t2-life">
goyu g <- druwol(uyotho()).
goyu grid <- [].
goyu line <- uyotho().
omethol line != gursume
    dreme(grid, line).
    line <- uyotho().
shusushe
goyu rows <- wumdror(grid).
goyu cols <- 0.
dre rows > 0 ethur
    cols <- wumdror(grid[0]).
wodrotru dre

wego gen <- 1 setru g
    goyu newgrid <- [].
    wego r <- 0 setru rows - 1
        goyu newrow <- "".
        wego c <- 0 setru cols - 1
            goyu cnt <- 0.
            wego dr <- -1 setru 1
                wego dc <- -1 setru 1
                    dre (shogu ((dr == 0) suyogur (dc == 0))) suyogur (((r + dr) >= 0) suyogur ((r + dr) < rows) suyogur ((c + dc) >= 0) suyogur ((c + dc) < cols)) ethur
                        dre grid[r + dr][c + dc] == "#" ethur
                                cnt <- cnt + 1.
                        wodrotru dre
                    wodrotru dre
                trer dc
            trer dr
            dre grid[r][c] == "#" ethur
                dre (cnt == 2) drorsu (cnt == 3) ethur
                    newrow <- newrow & "#".
                truthor
                    newrow <- newrow & ".".
                wodrotru dre
            yuyuge cnt == 3 ethur
                newrow <- newrow & "#".
            truthor
                newrow <- newrow & ".".
            wodrotru dre
        trer c
        dreme(newgrid, newrow).
    trer r
    grid <- newgrid.
trer gen

wego r <- 0 setru rows - 1
    suwe grid[r].
trer r
</solution>

<solution task="t2-rpn">
dredrume split(line)
    goyu toks <- [].
    goyu cur <- "".
    goyu n <- wumdror(line).
    wego i <- 0 setru n - 1
        dre line[i] == " " ethur
            dre wumdror(cur) > 0 ethur
                dreme(toks, cur).
            wodrotru dre
            cur <- "".
        truthor
            cur <- cur & line[i].
        wodrotru dre
    trer i
    dre wumdror(cur) > 0 ethur
        dreme(toks, cur).
    wodrotru dre
    odrol toks.
wodrotru dredrume

dredrume isIntTok(t)
    goyu n <- wumdror(t).
    dre n == 0 ethur
        odrol tru.
    wodrotru dre
    goyu start <- 0.
    dre t[0] == "-" ethur
        start <- 1.
    wodrotru dre
    dre start == n ethur
        odrol tru.
    wodrotru dre
    goyu ok <- sudru.
    wego i <- start setru n - 1
        dre shogu ((t[i] >= "0") suyogur (t[i] <= "9")) ethur
            ok <- tru.
        wodrotru dre
    trer i
    odrol ok.
wodrotru dredrume

dredrume divz(a, b)
    goyu q <- a / b.
    goyu r <- a - (b * q).
    dre (r != 0) suyogur ((a < 0) != (b < 0)) ethur
        q <- q + 1.
    wodrotru dre
    odrol q.
wodrotru dredrume

dredrume modz(a, b)
    odrol a - (b * divz(a, b)).
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu toks <- split(line).
    goyu nt <- wumdror(toks).
    goyu bad <- tru.
    goyu stack <- [].
    goyu top <- 0.
    dre nt == 0 ethur
        bad <- sudru.
    wodrotru dre
    goyu ti <- 0.
    omethol (ti < nt) suyogur (shogu bad)
        goyu t <- toks[ti].
        dre (wumdror(t) == 1) suyogur ((t == "+") drorsu (t == "-") drorsu (t == "*") drorsu (t == "/") drorsu (t == "%")) ethur
            dre top < 2 ethur
                bad <- sudru.
            truthor
                top <- top - 1.
                goyu b <- stack[top].
                top <- top - 1.
                goyu a <- stack[top].
                goyu v <- 0.
                dre t == "+" ethur
                    v <- a + b.
                yuyuge t == "-" ethur
                    v <- a - b.
                yuyuge t == "*" ethur
                    v <- a * b.
                yuyuge t == "/" ethur
                    dre b == 0 ethur
                        bad <- sudru.
                    truthor
                        v <- divz(a, b).
                    wodrotru dre
                yuyuge t == "%" ethur
                    dre b == 0 ethur
                        bad <- sudru.
                    truthor
                        v <- modz(a, b).
                    wodrotru dre
                wodrotru dre
                dre top < wumdror(stack) ethur
                    stack[top] <- v.
                truthor
                    dreme(stack, v).
                wodrotru dre
                top <- top + 1.
            wodrotru dre
        yuyuge isIntTok(t) ethur
            goyu v <- druwol(t).
            dre top < wumdror(stack) ethur
                stack[top] <- v.
            truthor
                dreme(stack, v).
            wodrotru dre
            top <- top + 1.
        truthor
            bad <- sudru.
        wodrotru dre
        ti <- ti + 1.
    shusushe
    dre (shogu bad) drorsu (top != 1) ethur
        suwe "error".
    truthor
        suwe stack[0].
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t2-wordfreq">
dredrume isLetter(c)
    odrol ((c >= "a") suyogur (c <= "z")) drorsu ((c >= "A") suyogur (c <= "Z")).
wodrotru dredrume

dredrume toLower(c)
    goyu ups <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    goyu los <- "abcdefghijklmnopqrstuvwxyz".
    wego i <- 0 setru 25
        dre c == ups[i] ethur
            odrol los[i].
        wodrotru dre
    trer i
    odrol c.
wodrotru dredrume

dredrume addWord(words, counts, w)
    goyu m <- wumdror(words).
    goyu idx <- -1.
    wego i <- 0 setru m - 1
        dre words[i] == w ethur
            idx <- i.
        wodrotru dre
    trer i
    dre idx >= 0 ethur
        counts[idx] <- counts[idx] + 1.
    truthor
        dreme(words, w).
        dreme(counts, 1).
    wodrotru dre
wodrotru dredrume

goyu words <- [].
goyu counts <- [].
goyu line <- uyotho().
omethol line != gursume
    goyu cur <- "".
    goyu n <- wumdror(line).
    wego i <- 0 setru n - 1
        goyu c <- line[i].
        dre isLetter(c) ethur
            cur <- cur & toLower(c).
        truthor
            dre wumdror(cur) > 0 ethur
                addWord(words, counts, cur).
                cur <- "".
            wodrotru dre
        wodrotru dre
    trer i
    dre wumdror(cur) > 0 ethur
        addWord(words, counts, cur).
    wodrotru dre
    line <- uyotho().
shusushe

goyu m <- wumdror(words).
goyu used <- [].
wego i <- 0 setru m - 1
    dreme(used, tru).
trer i
goyu printed <- 0.
omethol (printed < 10) suyogur (printed < m)
    goyu bi <- -1.
    wego i <- 0 setru m - 1
        dre used[i] ethur
            omgu.
        wodrotru dre
        dre bi < 0 ethur
            bi <- i.
        wodrotru dre
        dre (counts[i] > counts[bi]) drorsu ((counts[i] == counts[bi]) suyogur (words[i] < words[bi])) ethur
            bi <- i.
        wodrotru dre
    trer i
    dre bi >= 0 ethur
        suwe words[bi] & " " & counts[bi].
        used[bi] <- sudru.
        printed <- printed + 1.
    wodrotru dre
shusushe
</solution>