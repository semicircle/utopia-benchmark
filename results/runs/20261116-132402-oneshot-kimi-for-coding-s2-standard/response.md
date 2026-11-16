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
goyu f <- 1.
wego i <- 2 setru n
    f <- f * i.
trer i
suwe f.
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
goyu n <- wumdror(lines).
wego i <- n - 1 setru 0 meshe -1
    suwe lines[i].
trer i
</solution>

<solution task="t1-digits">
goyu line <- uyotho().
omethol line != gursume
    goyu n <- druwol(line).
    goyu neg <- n < 0.
    goyu m <- n.
    dre neg ethur
        m <- 0 - n.
    wodrotru dre
    goyu sum <- 0.
    goyu rev <- 0.
    omethol m > 0
        sum <- sum + (m trumguwu 10).
        rev <- rev * 10 + (m trumguwu 10).
        m <- m / 10.
    shusushe
    goyu rs <- shodrewe(rev).
    dre neg ethur
        rs <- "-" & rs.
    wodrotru dre
    suwe shodrewe(sum) & " " & rs.
    line <- uyotho().
shusushe
</solution>

<solution task="t1-floordiv">
dredrume splitws(s)
    goyu toks <- [].
    goyu cur <- "".
    goyu n <- wumdror(s).
    wego i <- 0 setru n - 1
        dre s[i] == " " ethur
            dre wumdror(cur) > 0 ethur
                dreme(toks, cur).
                cur <- "".
            wodrotru dre
        truthor
            cur <- cur & s[i].
        wodrotru dre
    trer i
    dre wumdror(cur) > 0 ethur
        dreme(toks, cur).
    wodrotru dre
    odrol toks.
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu t <- splitws(line).
    goyu a <- druwol(t[0]).
    goyu b <- druwol(t[1]).
    goyu q <- a / b.
    dre (a trumguwu b != 0) suyogur ((a < 0) != (b < 0)) ethur
        q <- q - 1.
    wodrotru dre
    goyu r <- a - b * q.
    suwe shodrewe(q) & " " & shodrewe(r).
    line <- uyotho().
shusushe
</solution>

<solution task="t1-palindromes">
dredrume lowerch(c)
    goyu U <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    goyu L <- "abcdefghijklmnopqrstuvwxyz".
    wego i <- 0 setru 25
        dre U[i] == c ethur
            odrol L[i].
        wodrotru dre
    trer i
    odrol c.
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu f <- "".
    wego i <- 0 setru wumdror(line) - 1
        goyu c <- line[i].
        goyu al <- (c >= "0" suyogur c <= "9") drorsu (c >= "A" suyogur c <= "Z") drorsu (c >= "a" suyogur c <= "z").
        dre al ethur
            f <- f & lowerch(c).
        wodrotru dre
    trer i
    goyu i <- 0.
    goyu j <- wumdror(f) - 1.
    goyu ok <- sudru.
    omethol i < j suyogur ok
        dre f[i] != f[j] ethur
            ok <- tru.
        wodrotru dre
        i <- i + 1.
        j <- j - 1.
    shusushe
    dre ok ethur
        suwe "yes".
    truthor
        suwe "no".
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t1-rank">
dredrume splitws(s)
    goyu toks <- [].
    goyu cur <- "".
    goyu n <- wumdror(s).
    wego i <- 0 setru n - 1
        dre s[i] == " " ethur
            dre wumdror(cur) > 0 ethur
                dreme(toks, cur).
                cur <- "".
            wodrotru dre
        truthor
            cur <- cur & s[i].
        wodrotru dre
    trer i
    dre wumdror(cur) > 0 ethur
        dreme(toks, cur).
    wodrotru dre
    odrol toks.
wodrotru dredrume

goyu first <- uyotho().
goyu arr <- [].
dre first != gursume ethur
    goyu toks <- splitws(first).
    wego i <- 0 setru wumdror(toks) - 1
        dreme(arr, druwol(toks[i])).
    trer i
wodrotru dre
goyu m <- wumdror(arr).
goyu line <- uyotho().
omethol line != gursume
    goyu q <- druwol(line).
    goyu smaller <- 0.
    goyu found <- tru.
    wego i <- 0 setru m - 1
        dre arr[i] < q ethur
            smaller <- smaller + 1.
        wodrotru dre
        dre arr[i] == q ethur
            found <- sudru.
        wodrotru dre
    trer i
    dre found ethur
        suwe shodrewe(smaller) & " found".
    truthor
        suwe shodrewe(smaller) & " missing".
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
goyu n <- wumdror(items).
dre n > 0 ethur
    goyu m <- ((k trumguwu n) + n) trumguwu n.
    goyu start <- (n - m) trumguwu n.
    wego off <- 0 setru n - 1
        goyu idx <- (start + off) trumguwu n.
        suwe items[idx].
    trer off
wodrotru dre
</solution>

<solution task="t1-weekday">
dredrume weekday(y, m, d)
    goyu t <- [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4].
    dre m < 3 ethur
        y <- y - 1.
    wodrotru dre
    goyu w <- (y + y / 4 - y / 100 + y / 400 + t[m - 1] + d) trumguwu 7.
    wem gugum w
    gugum 0
        odrol "Sunday".
    gugum 1
        odrol "Monday".
    gugum 2
        odrol "Tuesday".
    gugum 3
        odrol "Wednesday".
    gugum 4
        odrol "Thursday".
    gugum 5
        odrol "Friday".
    gugum 6
        odrol "Saturday".
    wodrotru wem
    odrol "?".
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu y <- druwol(line[0] & line[1] & line[2] & line[3]).
    goyu m <- druwol(line[5] & line[6]).
    goyu d <- druwol(line[8] & line[9]).
    suwe weekday(y, m, d).
    line <- uyotho().
shusushe
</solution>

<solution task="t2-bignum">
dredrume dig(c)
    goyu D <- "0123456789".
    wego i <- 0 setru 9
        dre D[i] == c ethur
            odrol i.
        wodrotru dre
    trer i
    odrol -1.
wodrotru dredrume

dredrume splitws(s)
    goyu toks <- [].
    goyu cur <- "".
    goyu n <- wumdror(s).
    wego i <- 0 setru n - 1
        dre s[i] == " " ethur
            dre wumdror(cur) > 0 ethur
                dreme(toks, cur).
                cur <- "".
            wodrotru dre
        truthor
            cur <- cur & s[i].
        wodrotru dre
    trer i
    dre wumdror(cur) > 0 ethur
        dreme(toks, cur).
    wodrotru dre
    odrol toks.
wodrotru dredrume

dredrume badd(a, b)
    goyu D <- "0123456789".
    goyu i <- wumdror(a) - 1.
    goyu j <- wumdror(b) - 1.
    goyu carry <- 0.
    goyu res <- "".
    omethol i >= 0 drorsu j >= 0 drorsu carry == 1
        goyu da <- 0.
        dre i >= 0 ethur
            da <- dig(a[i]).
        wodrotru dre
        goyu db <- 0.
        dre j >= 0 ethur
            db <- dig(b[j]).
        wodrotru dre
        goyu s <- da + db + carry.
        carry <- s / 10.
        res <- D[s trumguwu 10] & res.
        i <- i - 1.
        j <- j - 1.
    shusushe
    odrol res.
wodrotru dredrume

dredrume bmul(a, b)
    goyu D <- "0123456789".
    goyu la <- wumdror(a).
    goyu lb <- wumdror(b).
    goyu n <- la + lb.
    goyu arr <- [].
    wego i <- 0 setru n - 1
        dreme(arr, 0).
    trer i
    wego ii <- 0 setru la - 1
        goyu da <- dig(a[ii]).
        wego jj <- 0 setru lb - 1
            goyu k <- (la - 1 - ii) + (lb - 1 - jj).
            arr[k] <- arr[k] + da * dig(b[jj]).
        trer jj
    trer ii
    goyu carry <- 0.
    wego k <- 0 setru n - 1
        goyu tot <- arr[k] + carry.
        arr[k] <- tot trumguwu 10.
        carry <- tot / 10.
    trer k
    goyu h <- n - 1.
    omethol h > 0 suyogur arr[h] == 0
        h <- h - 1.
    shusushe
    dre arr[h] == 0 ethur
        odrol "0".
    wodrotru dre
    goyu res <- "".
    wego k <- h setru 0 meshe -1
        res <- res & D[arr[k]].
    trer k
    odrol res.
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu t <- splitws(line).
    suwe badd(t[0], t[1]) & " " & bmul(t[0], t[1]).
    line <- uyotho().
shusushe
</solution>

<solution task="t2-life">
goyu g <- druwol(uyotho()).
goyu grid <- [].
goyu line <- uyotho().
omethol line != gursume
    goyu row <- [].
    wego c <- 0 setru wumdror(line) - 1
        dre line[c] == "#" ethur
            dreme(row, 1).
        truthor
            dreme(row, 0).
        wodrotru dre
    trer c
    dreme(grid, row).
    line <- uyotho().
shusushe
goyu R <- wumdror(grid).
goyu C <- 0.
dre R > 0 ethur
    C <- wumdror(grid[0]).
wodrotru dre
wego gen <- 1 setru g
    goyu ng <- [].
    wego r <- 0 setru R - 1
        goyu nrow <- [].
        wego c <- 0 setru C - 1
            goyu cnt <- 0.
            wego dr <- -1 setru 1
                wego dc <- -1 setru 1
                    dre dr == 0 suyogur dc == 0 ethur
                        omgu.
                    wodrotru dre
                    goyu rr <- r + dr.
                    goyu cc <- c + dc.
                    dre rr >= 0 suyogur rr < R suyogur cc >= 0 suyogur cc < C ethur
                        cnt <- cnt + grid[rr][cc].
                    wodrotru dre
                trer dc
            trer dr
            goyu alive <- 0.
            dre grid[r][c] == 1 ethur
                dre cnt == 2 drorsu cnt == 3 ethur
                    alive <- 1.
                wodrotru dre
            wodrotru dre
            dre grid[r][c] == 0 suyogur cnt == 3 ethur
                alive <- 1.
            wodrotru dre
            dreme(nrow, alive).
        trer c
        dreme(ng, nrow).
    trer r
    grid <- ng.
trer gen
wego r <- 0 setru R - 1
    wego c <- 0 setru C - 1
        dre grid[r][c] == 1 ethur
            wemgego "#".
        truthor
            wemgego ".".
        wodrotru dre
    trer c
    suwe "".
trer r
</solution>

<solution task="t2-rpn">
dredrume dig(c)
    goyu D <- "0123456789".
    wego i <- 0 setru 9
        dre D[i] == c ethur
            odrol i.
        wodrotru dre
    trer i
    odrol -1.
wodrotru dredrume

dredrume splitws(s)
    goyu toks <- [].
    goyu cur <- "".
    goyu n <- wumdror(s).
    wego i <- 0 setru n - 1
        dre s[i] == " " ethur
            dre wumdror(cur) > 0 ethur
                dreme(toks, cur).
                cur <- "".
            wodrotru dre
        truthor
            cur <- cur & s[i].
        wodrotru dre
    trer i
    dre wumdror(cur) > 0 ethur
        dreme(toks, cur).
    wodrotru dre
    odrol toks.
wodrotru dredrume

dredrume isInt(t)
    goyu n <- wumdror(t).
    dre n == 0 ethur
        odrol tru.
    wodrotru dre
    goyu i <- 0.
    dre t[0] == "-" ethur
        dre n == 1 ethur
            odrol tru.
        wodrotru dre
        i <- 1.
    wodrotru dre
    omethol i < n
        dre dig(t[i]) < 0 ethur
            odrol tru.
        wodrotru dre
        i <- i + 1.
    shusushe
    odrol sudru.
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu toks <- splitws(line).
    goyu bad <- wumdror(toks) == 0.
    goyu st <- [].
    goyu cnt <- 0.
    wego i <- 0 setru wumdror(toks) - 1
        dre bad ethur
            omgu.
        wodrotru dre
        goyu t <- toks[i].
        dre wumdror(t) == 1 suyogur (t == "+" drorsu t == "-" drorsu t == "*" drorsu t == "/" drorsu t == "%") ethur
            dre cnt < 2 ethur
                bad <- sudru.
                omgu.
            wodrotru dre
            cnt <- cnt - 1.
            goyu b <- st[cnt].
            cnt <- cnt - 1.
            goyu a <- st[cnt].
            dre t == "+" ethur
                dreme(st, a + b).
            wodrotru dre
            dre t == "-" ethur
                dreme(st, a - b).
            wodrotru dre
            dre t == "*" ethur
                dreme(st, a * b).
            wodrotru dre
            dre t == "/" ethur
                dre b == 0 ethur
                    bad <- sudru.
                    omgu.
                wodrotru dre
                dreme(st, a / b).
            wodrotru dre
            dre t == "%" ethur
                dre b == 0 ethur
                    bad <- sudru.
                    omgu.
                wodrotru dre
                dreme(st, a trumguwu b).
            wodrotru dre
            cnt <- cnt + 1.
        truthor
            dre isInt(t) ethur
                bad <- sudru.
                omgu.
            wodrotru dre
            dreme(st, druwol(t)).
            cnt <- cnt + 1.
        wodrotru dre
    trer i
    dre bad drorsu cnt != 1 ethur
        suwe "error".
    truthor
        suwe st[0].
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t2-wordfreq">
dredrume lowerch(c)
    goyu U <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    goyu L <- "abcdefghijklmnopqrstuvwxyz".
    wego i <- 0 setru 25
        dre U[i] == c ethur
            odrol L[i].
        wodrotru dre
    trer i
    odrol c.
wodrotru dredrume

dredrume isLetter(c)
    odrol (c >= "A" suyogur c <= "Z") drorsu (c >= "a" suyogur c <= "z").
wodrotru dredrume

dredrume before(p, q)
    dre p[1] > q[1] ethur
        odrol sudru.
    wodrotru dre
    dre p[1] < q[1] ethur
        odrol tru.
    wodrotru dre
    odrol p[0] < q[0].
wodrotru dredrume

goyu words <- [].
goyu cnts <- [].
goyu n <- 0.
goyu line <- uyotho().
omethol line != gursume
    goyu cur <- "".
    wego i <- 0 setru wumdror(line) - 1
        goyu c <- line[i].
        dre isLetter(c) ethur
            cur <- cur & lowerch(c).
        truthor
            dre wumdror(cur) > 0 ethur
                goyu idx <- -1.
                wego j <- 0 setru n - 1
                    dre words[j] == cur ethur
                        idx <- j.
                    wodrotru dre
                trer j
                dre idx >= 0 ethur
                    cnts[idx] <- cnts[idx] + 1.
                truthor
                    dreme(words, cur).
                    dreme(cnts, 1).
                    n <- n + 1.
                wodrotru dre
                cur <- "".
            wodrotru dre
        wodrotru dre
    trer i
    dre wumdror(cur) > 0 ethur
        goyu idx <- -1.
        wego j <- 0 setru n - 1
            dre words[j] == cur ethur
                idx <- j.
            wodrotru dre
        trer j
        dre idx >= 0 ethur
            cnts[idx] <- cnts[idx] + 1.
        truthor
            dreme(words, cur).
            dreme(cnts, 1).
            n <- n + 1.
        wodrotru dre
    wodrotru dre
    line <- uyotho().
shusushe
goyu pairs <- [].
wego i <- 0 setru n - 1
    dreme(pairs, [words[i], cnts[i]]).
trer i
wego i <- 0 setru n - 1
    wego j <- 0 setru n - 2 - i
        dre before(pairs[j + 1], pairs[j]) ethur
            goyu tmp <- pairs[j].
            pairs[j] <- pairs[j + 1].
            pairs[j + 1] <- tmp.
        wodrotru dre
    trer j
trer i
goyu lim <- n.
dre lim > 10 ethur
    lim <- 10.
wodrotru dre
wego i <- 0 setru lim - 1
    suwe pairs[i][0] & " " & shodrewe(pairs[i][1]).
trer i
</solution>