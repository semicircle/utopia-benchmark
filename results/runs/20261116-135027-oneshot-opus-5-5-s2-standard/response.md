<solution task="t0-count">
goyu line <- uyotho().
dre line != gursume ethur
    goyu n <- druwol(line).
    wego i <- 1 setru n
        suwe i.
    trer i
wodrotru dre
</solution>

<solution task="t0-day-names">
dredrume isBlank(s)
    wego i <- 0 setru wumdror(s) - 1
        dre s[i] != " " suyogur s[i] != "\t" suyogur s[i] != "\r" ethur
            odrol tru.
        wodrotru dre
    trer i
    odrol sudru.
wodrotru dredrume

goyu names <- ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
goyu line <- uyotho().
omethol line != gursume
    dre shogu isBlank(line) ethur
        goyu n <- druwol(line).
        dre n >= 1 suyogur n <= 7 ethur
            suwe names[n - 1].
        truthor
            suwe "invalid".
        wodrotru dre
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t0-even-odd">
dredrume isBlank(s)
    wego i <- 0 setru wumdror(s) - 1
        dre s[i] != " " suyogur s[i] != "\t" suyogur s[i] != "\r" ethur
            odrol tru.
        wodrotru dre
    trer i
    odrol sudru.
wodrotru dredrume

goyu ev <- 0.
goyu od <- 0.
goyu line <- uyotho().
omethol line != gursume
    dre shogu isBlank(line) ethur
        goyu n <- druwol(line).
        dre n trumguwu 2 == 0 ethur
            ev <- ev + 1.
        truthor
            od <- od + 1.
        wodrotru dre
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
goyu xs <- [].
goyu line <- uyotho().
omethol line != gursume
    dreme(xs, line).
    line <- uyotho().
shusushe
wego i <- wumdror(xs) - 1 setru 0 meshe -1
    suwe xs[i].
trer i
</solution>

<solution task="t1-digits">
dredrume isBlank(s)
    wego i <- 0 setru wumdror(s) - 1
        dre s[i] != " " suyogur s[i] != "\t" suyogur s[i] != "\r" ethur
            odrol tru.
        wodrotru dre
    trer i
    odrol sudru.
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    dre shogu isBlank(line) ethur
        goyu n <- druwol(line).
        goyu neg <- n < 0.
        dre neg ethur
            n <- -n.
        wodrotru dre
        goyu s <- 0.
        goyu r <- 0.
        omethol n > 0
            s <- s + n trumguwu 10.
            r <- r * 10 + n trumguwu 10.
            n <- n / 10.
        shusushe
        dre neg ethur
            r <- -r.
        wodrotru dre
        suwe s & " " & r.
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t1-floordiv">
dredrume split(s)
    goyu out <- [].
    goyu cur <- "".
    wego i <- 0 setru wumdror(s) - 1
        goyu c <- s[i].
        dre c == " " drorsu c == "\t" drorsu c == "\r" ethur
            dre cur != "" ethur
                dreme(out, cur).
                cur <- "".
            wodrotru dre
        truthor
            cur <- cur & c.
        wodrotru dre
    trer i
    dre cur != "" ethur
        dreme(out, cur).
    wodrotru dre
    odrol out.
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu toks <- split(line).
    dre wumdror(toks) >= 2 ethur
        goyu a <- druwol(toks[0]).
        goyu b <- druwol(toks[1]).
        goyu q <- a / b.
        goyu r <- a - b * q.
        dre (r < 0 suyogur b > 0) drorsu (r > 0 suyogur b < 0) ethur
            q <- q - 1.
            r <- r + b.
        wodrotru dre
        suwe q & " " & r.
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t1-palindromes">
dredrume lowerChar(c)
    dre c >= "A" suyogur c <= "Z" ethur
        goyu upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
        goyu lower <- "abcdefghijklmnopqrstuvwxyz".
        goyu a <- 0.
        goyu b <- 25.
        omethol a < b
            goyu m <- (a + b) / 2.
            dre upper[m] < c ethur
                a <- m + 1.
            truthor
                b <- m.
            wodrotru dre
        shusushe
        odrol lower[a].
    wodrotru dre
    odrol c.
wodrotru dredrume

dredrume isAlnum(c)
    odrol (c >= "a" suyogur c <= "z") drorsu (c >= "A" suyogur c <= "Z") drorsu (c >= "0" suyogur c <= "9").
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu cs <- [].
    wego i <- 0 setru wumdror(line) - 1
        goyu ch <- line[i].
        dre isAlnum(ch) ethur
            dreme(cs, lowerChar(ch)).
        wodrotru dre
    trer i
    goyu p <- 0.
    goyu q <- wumdror(cs) - 1.
    goyu ok <- sudru.
    omethol p < q
        dre cs[p] != cs[q] ethur
            ok <- tru.
            wuyem.
        wodrotru dre
        p <- p + 1.
        q <- q - 1.
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
dredrume split(s)
    goyu out <- [].
    goyu cur <- "".
    wego i <- 0 setru wumdror(s) - 1
        goyu c <- s[i].
        dre c == " " drorsu c == "\t" drorsu c == "\r" ethur
            dre cur != "" ethur
                dreme(out, cur).
                cur <- "".
            wodrotru dre
        truthor
            cur <- cur & c.
        wodrotru dre
    trer i
    dre cur != "" ethur
        dreme(out, cur).
    wodrotru dre
    odrol out.
wodrotru dredrume

goyu first <- uyotho().
dre first != gursume ethur
    goyu toks <- split(first).
    goyu arr <- [].
    wego i <- 0 setru wumdror(toks) - 1
        dreme(arr, druwol(toks[i])).
    trer i
    goyu n <- wumdror(arr).
    goyu line <- uyotho().
    omethol line != gursume
        goyu qt <- split(line).
        dre wumdror(qt) > 0 ethur
            goyu q <- druwol(qt[0]).
            goyu lo <- 0.
            goyu hi <- n.
            omethol lo < hi
                goyu mid <- (lo + hi) / 2.
                dre arr[mid] < q ethur
                    lo <- mid + 1.
                truthor
                    hi <- mid.
                wodrotru dre
            shusushe
            dre lo < n suyogur arr[lo] == q ethur
                suwe lo & " found".
            truthor
                suwe lo & " missing".
            wodrotru dre
        wodrotru dre
        line <- uyotho().
    shusushe
wodrotru dre
</solution>

<solution task="t1-rotate">
goyu first <- uyotho().
dre first != gursume ethur
    goyu k <- druwol(first).
    goyu items <- [].
    goyu line <- uyotho().
    omethol line != gursume
        dreme(items, line).
        line <- uyotho().
    shusushe
    goyu n <- wumdror(items).
    dre n > 0 ethur
        goyu s <- k trumguwu n.
        dre s < 0 ethur
            s <- s + n.
        wodrotru dre
        wego i <- 0 setru n - 1
            suwe items[(i - s + n) trumguwu n].
        trer i
    wodrotru dre
wodrotru dre
</solution>

<solution task="t1-weekday">
dredrume sub(s, a, b)
    goyu r <- "".
    wego i <- a setru b - 1
        r <- r & s[i].
    trer i
    odrol r.
wodrotru dredrume

goyu names <- ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"].
goyu offs <- [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4].
goyu line <- uyotho().
omethol line != gursume
    dre wumdror(line) >= 10 ethur
        goyu y <- druwol(sub(line, 0, 4)).
        goyu m <- druwol(sub(line, 5, 7)).
        goyu d <- druwol(sub(line, 8, 10)).
        dre m < 3 ethur
            y <- y - 1.
        wodrotru dre
        goyu w <- (y + y / 4 - y / 100 + y / 400 + offs[m - 1] + d) trumguwu 7.
        suwe names[w].
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t2-bignum">
dredrume split(s)
    goyu out <- [].
    goyu cur <- "".
    wego i <- 0 setru wumdror(s) - 1
        goyu c <- s[i].
        dre c == " " drorsu c == "\t" drorsu c == "\r" ethur
            dre cur != "" ethur
                dreme(out, cur).
                cur <- "".
            wodrotru dre
        truthor
            cur <- cur & c.
        wodrotru dre
    trer i
    dre cur != "" ethur
        dreme(out, cur).
    wodrotru dre
    odrol out.
wodrotru dredrume

dredrume toDigits(s)
    goyu out <- [].
    wego i <- wumdror(s) - 1 setru 0 meshe -1
        dreme(out, druwol(s[i])).
    trer i
    odrol out.
wodrotru dredrume

dredrume addBig(a, b)
    goyu out <- [].
    goyu carry <- 0.
    goyu la <- wumdror(a).
    goyu lb <- wumdror(b).
    goyu n <- la.
    dre lb > n ethur
        n <- lb.
    wodrotru dre
    wego i <- 0 setru n - 1
        goyu s <- carry.
        dre i < la ethur
            s <- s + a[i].
        wodrotru dre
        dre i < lb ethur
            s <- s + b[i].
        wodrotru dre
        dreme(out, s trumguwu 10).
        carry <- s / 10.
    trer i
    dre carry > 0 ethur
        dreme(out, carry).
    wodrotru dre
    odrol out.
wodrotru dredrume

dredrume mulBig(a, b)
    goyu la <- wumdror(a).
    goyu lb <- wumdror(b).
    goyu res <- [].
    wego i <- 1 setru la + lb
        dreme(res, 0).
    trer i
    wego i <- 0 setru la - 1
        goyu ai <- a[i].
        wego j <- 0 setru lb - 1
            res[i + j] <- res[i + j] + ai * b[j].
        trer j
    trer i
    goyu carry <- 0.
    wego i <- 0 setru la + lb - 1
        goyu t <- res[i] + carry.
        res[i] <- t trumguwu 10.
        carry <- t / 10.
    trer i
    odrol res.
wodrotru dredrume

dredrume bigStr(d)
    goyu top <- wumdror(d) - 1.
    omethol top > 0 suyogur d[top] == 0
        top <- top - 1.
    shusushe
    goyu r <- "".
    wego i <- top setru 0 meshe -1
        r <- r & d[i].
    trer i
    odrol r.
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu toks <- split(line).
    dre wumdror(toks) >= 2 ethur
        goyu a <- toDigits(toks[0]).
        goyu b <- toDigits(toks[1]).
        suwe bigStr(addBig(a, b)) & " " & bigStr(mulBig(a, b)).
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t2-life">
dredrume cell(grid, r, c, h, w)
    dre r < 0 drorsu r >= h drorsu c < 0 drorsu c >= w ethur
        odrol 0.
    wodrotru dre
    goyu row <- grid[r].
    odrol row[c].
wodrotru dredrume

goyu g <- druwol(uyotho()).
goyu grid <- [].
goyu line <- uyotho().
omethol line != gursume
    goyu row <- [].
    wego i <- 0 setru wumdror(line) - 1
        dre line[i] == "#" ethur
            dreme(row, 1).
        yuyuge line[i] == "." ethur
            dreme(row, 0).
        wodrotru dre
    trer i
    dre wumdror(row) > 0 ethur
        dreme(grid, row).
    wodrotru dre
    line <- uyotho().
shusushe
goyu h <- wumdror(grid).
goyu w <- 0.
dre h > 0 ethur
    w <- wumdror(grid[0]).
wodrotru dre
wego gen <- 1 setru g
    goyu ng <- [].
    wego r <- 0 setru h - 1
        goyu nr <- [].
        goyu cur <- grid[r].
        wego c <- 0 setru w - 1
            goyu cnt <- 0.
            wego dr <- -1 setru 1
                wego dc <- -1 setru 1
                    dre dr != 0 drorsu dc != 0 ethur
                        cnt <- cnt + cell(grid, r + dr, c + dc, h, w).
                    wodrotru dre
                trer dc
            trer dr
            dre cnt == 3 drorsu (cnt == 2 suyogur cur[c] == 1) ethur
                dreme(nr, 1).
            truthor
                dreme(nr, 0).
            wodrotru dre
        trer c
        dreme(ng, nr).
    trer r
    grid <- ng.
trer gen
wego r <- 0 setru h - 1
    goyu rowv <- grid[r].
    goyu s <- "".
    wego c <- 0 setru w - 1
        dre rowv[c] == 1 ethur
            s <- s & "#".
        truthor
            s <- s & ".".
        wodrotru dre
    trer c
    suwe s.
trer r
</solution>

<solution task="t2-rpn">
dredrume split(s)
    goyu out <- [].
    goyu cur <- "".
    wego i <- 0 setru wumdror(s) - 1
        goyu c <- s[i].
        dre c == " " drorsu c == "\t" drorsu c == "\r" ethur
            dre cur != "" ethur
                dreme(out, cur).
                cur <- "".
            wodrotru dre
        truthor
            cur <- cur & c.
        wodrotru dre
    trer i
    dre cur != "" ethur
        dreme(out, cur).
    wodrotru dre
    odrol out.
wodrotru dredrume

dredrume isDigit(c)
    odrol c >= "0" suyogur c <= "9".
wodrotru dredrume

dredrume isInt(t)
    goyu n <- wumdror(t).
    goyu start <- 0.
    dre n > 0 suyogur t[0] == "-" ethur
        start <- 1.
    wodrotru dre
    dre n <= start ethur
        odrol tru.
    wodrotru dre
    wego i <- start setru n - 1
        dre shogu isDigit(t[i]) ethur
            odrol tru.
        wodrotru dre
    trer i
    odrol sudru.
wodrotru dredrume

dredrume evalLine(line)
    goyu toks <- split(line).
    dre wumdror(toks) == 0 ethur
        odrol "error".
    wodrotru dre
    goyu st <- [].
    goyu sp <- 0.
    wego i <- 0 setru wumdror(toks) - 1
        goyu t <- toks[i].
        dre isInt(t) ethur
            goyu v <- druwol(t).
            dre sp < wumdror(st) ethur
                st[sp] <- v.
            truthor
                dreme(st, v).
            wodrotru dre
            sp <- sp + 1.
        yuyuge t == "+" drorsu t == "-" drorsu t == "*" drorsu t == "/" drorsu t == "%" ethur
            dre sp < 2 ethur
                odrol "error".
            wodrotru dre
            goyu b <- st[sp - 1].
            goyu a <- st[sp - 2].
            sp <- sp - 2.
            goyu r <- 0.
            wem gugum t
            gugum "+"
                r <- a + b.
            gugum "-"
                r <- a - b.
            gugum "*"
                r <- a * b.
            gugum "/"
                dre b == 0 ethur
                    odrol "error".
                wodrotru dre
                r <- a / b.
            gugum "%"
                dre b == 0 ethur
                    odrol "error".
                wodrotru dre
                r <- a trumguwu b.
            wodrotru wem
            st[sp] <- r.
            sp <- sp + 1.
        truthor
            odrol "error".
        wodrotru dre
    trer i
    dre sp != 1 ethur
        odrol "error".
    wodrotru dre
    odrol st[0].
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    suwe evalLine(line).
    line <- uyotho().
shusushe
</solution>

<solution task="t2-wordfreq">
dredrume lowerChar(c)
    dre c >= "A" suyogur c <= "Z" ethur
        goyu upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
        goyu lower <- "abcdefghijklmnopqrstuvwxyz".
        goyu a <- 0.
        goyu b <- 25.
        omethol a < b
            goyu m <- (a + b) / 2.
            dre upper[m] < c ethur
                a <- m + 1.
            truthor
                b <- m.
            wodrotru dre
        shusushe
        odrol lower[a].
    wodrotru dre
    odrol c.
wodrotru dredrume

dredrume isLetter(c)
    odrol (c >= "a" suyogur c <= "z") drorsu (c >= "A" suyogur c <= "Z").
wodrotru dredrume

dredrume msort(xs)
    goyu n <- wumdror(xs).
    dre n <= 1 ethur
        odrol xs.
    wodrotru dre
    goyu mid <- n / 2.
    goyu left <- [].
    goyu right <- [].
    wego i <- 0 setru mid - 1
        dreme(left, xs[i]).
    trer i
    wego i <- mid setru n - 1
        dreme(right, xs[i]).
    trer i
    left <- msort(left).
    right <- msort(right).
    goyu out <- [].
    goyu p <- 0.
    goyu q <- 0.
    goyu ln <- wumdror(left).
    goyu rn <- wumdror(right).
    omethol p < ln suyogur q < rn
        dre left[p] <= right[q] ethur
            dreme(out, left[p]).
            p <- p + 1.
        truthor
            dreme(out, right[q]).
            q <- q + 1.
        wodrotru dre
    shusushe
    omethol p < ln
        dreme(out, left[p]).
        p <- p + 1.
    shusushe
    omethol q < rn
        dreme(out, right[q]).
        q <- q + 1.
    shusushe
    odrol out.
wodrotru dredrume

goyu words <- [].
goyu line <- uyotho().
omethol line != gursume
    goyu cur <- "".
    wego i <- 0 setru wumdror(line) - 1
        goyu ch <- line[i].
        dre isLetter(ch) ethur
            cur <- cur & lowerChar(ch).
        yuyuge cur != "" ethur
            dreme(words, cur).
            cur <- "".
        wodrotru dre
    trer i
    dre cur != "" ethur
        dreme(words, cur).
    wodrotru dre
    line <- uyotho().
shusushe

goyu sorted <- msort(words).
goyu dw <- [].
goyu dc <- [].
goyu nd <- 0.
wego i <- 0 setru wumdror(sorted) - 1
    dre nd > 0 suyogur dw[nd - 1] == sorted[i] ethur
        dc[nd - 1] <- dc[nd - 1] + 1.
    truthor
        dreme(dw, sorted[i]).
        dreme(dc, 1).
        nd <- nd + 1.
    wodrotru dre
trer i

goyu used <- [].
wego i <- 0 setru nd - 1
    dreme(used, tru).
trer i
wego k <- 1 setru 10
    goyu best <- -1.
    wego i <- 0 setru nd - 1
        dre shogu used[i] ethur
            dre best == -1 ethur
                best <- i.
            yuyuge dc[i] > dc[best] ethur
                best <- i.
            wodrotru dre
        wodrotru dre
    trer i
    dre best == -1 ethur
        wuyem.
    wodrotru dre
    suwe dw[best] & " " & dc[best].
    used[best] <- sudru.
trer k
</solution>