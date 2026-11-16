Below are the 17 solutions. Two features of Gutrur shape the code more than any others:

- **Precedence:** every binary operator has the same precedence, so sub-expressions are parenthesized.
- **No short-circuit:** `suyogur` and `drorsu` always evaluate both sides, so bounds checks are written as nested `dre` statements.

<solution task="t0-hello">
suwe "Hello, Utopia!".
</solution>

<solution task="t0-count">
goyu n <- druwol(uyotho()).
wego i <- 1 setru n
    suwe i.
trer i
</solution>

<solution task="t0-day-names">
goyu days <- ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
goyu line <- uyotho().
omethol line != gursume
    dre wumdror(line) > 0 ethur
        goyu n <- druwol(line).
        dre (n >= 1) suyogur (n <= 7) ethur
            suwe days[n - 1].
        truthor
            suwe "invalid".
        wodrotru dre
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t0-even-odd">
goyu ev <- 0.
goyu od <- 0.
goyu line <- uyotho().
omethol line != gursume
    dre wumdror(line) > 0 ethur
        goyu n <- druwol(line).
        dre (n trumguwu 2) == 0 ethur
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
goyu p <- 1.
wego i <- 1 setru n
    p <- p * i.
trer i
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
goyu line <- uyotho().
omethol line != gursume
    dre wumdror(line) > 0 ethur
        goyu n <- druwol(line).
        goyu a <- n.
        dre n < 0 ethur
            a <- -n.
        wodrotru dre
        goyu s <- 0.
        goyu r <- 0.
        omethol a > 0
            s <- s + (a trumguwu 10).
            r <- (r * 10) + (a trumguwu 10).
            a <- a / 10.
        shusushe
        dre n < 0 ethur
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
    goyu has <- tru.
    wego i <- 0 setru wumdror(s) - 1
        goyu c <- s[i].
        dre ((c == " ") drorsu (c == "\t")) drorsu (c == "\r") ethur
            dre has ethur
                dreme(out, cur).
                cur <- "".
                has <- tru.
            wodrotru dre
        truthor
            cur <- cur & c.
            has <- sudru.
        wodrotru dre
    trer i
    dre has ethur
        dreme(out, cur).
    wodrotru dre
    odrol out.
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu p <- split(line).
    dre wumdror(p) >= 2 ethur
        goyu a <- druwol(p[0]).
        goyu b <- druwol(p[1]).
        goyu q <- a / b.
        goyu r <- a trumguwu b.
        suwe q & " " & r.
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t1-palindromes">
dredrume lowerc(c)
    goyu up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    goyu low <- "abcdefghijklmnopqrstuvwxyz".
    goyu lo <- 0.
    goyu hi <- 25.
    omethol lo < hi
        goyu mid <- (lo + hi) / 2.
        dre up[mid] < c ethur
            lo <- mid + 1.
        truthor
            hi <- mid.
        wodrotru dre
    shusushe
    odrol low[lo].
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu cs <- [].
    wego i <- 0 setru wumdror(line) - 1
        goyu c <- line[i].
        dre ((c >= "a") suyogur (c <= "z")) drorsu ((c >= "0") suyogur (c <= "9")) ethur
            dreme(cs, c).
        yuyuge (c >= "A") suyogur (c <= "Z") ethur
            dreme(cs, lowerc(c)).
        wodrotru dre
    trer i
    goyu n <- wumdror(cs).
    goyu ok <- sudru.
    wego i <- 0 setru (n / 2) - 1
        dre cs[i] != cs[(n - 1) - i] ethur
            ok <- tru.
        wodrotru dre
    trer i
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
    goyu has <- tru.
    wego i <- 0 setru wumdror(s) - 1
        goyu c <- s[i].
        dre ((c == " ") drorsu (c == "\t")) drorsu (c == "\r") ethur
            dre has ethur
                dreme(out, cur).
                cur <- "".
                has <- tru.
            wodrotru dre
        truthor
            cur <- cur & c.
            has <- sudru.
        wodrotru dre
    trer i
    dre has ethur
        dreme(out, cur).
    wodrotru dre
    odrol out.
wodrotru dredrume

goyu first <- uyotho().
dre first != gursume ethur
    goyu toks <- split(first).
    goyu nums <- [].
    wego i <- 0 setru wumdror(toks) - 1
        dreme(nums, druwol(toks[i])).
    trer i
    goyu n <- wumdror(nums).
    goyu line <- uyotho().
    omethol line != gursume
        goyu qt <- split(line).
        dre wumdror(qt) > 0 ethur
            goyu q <- druwol(qt[0]).
            goyu lo <- 0.
            goyu hi <- n.
            omethol lo < hi
                goyu mid <- (lo + hi) / 2.
                dre nums[mid] < q ethur
                    lo <- mid + 1.
                truthor
                    hi <- mid.
                wodrotru dre
            shusushe
            goyu found <- "missing".
            dre lo < n ethur
                dre nums[lo] == q ethur
                    found <- "found".
                wodrotru dre
            wodrotru dre
            suwe lo & " " & found.
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
        wego i <- 0 setru n - 1
            goyu idx <- (i - k) trumguwu n.
            suwe items[idx].
        trer i
    wodrotru dre
wodrotru dre
</solution>

<solution task="t1-weekday">
dredrume num(s, from, to)
    goyu v <- 0.
    wego i <- from setru to
        v <- (v * 10) + druwol(s[i]).
    trer i
    odrol v.
wodrotru dredrume

goyu names <- ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"].
goyu tt <- [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4].
goyu line <- uyotho().
omethol line != gursume
    dre wumdror(line) >= 10 ethur
        goyu y <- num(line, 0, 3).
        goyu m <- num(line, 5, 6).
        goyu d <- num(line, 8, 9).
        dre m < 3 ethur
            y <- y - 1.
        wodrotru dre
        goyu w <- (y + (y / 4) - (y / 100) + (y / 400) + tt[m - 1] + d) trumguwu 7.
        suwe names[w].
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t2-bignum">
dredrume split(s)
    goyu out <- [].
    goyu cur <- "".
    goyu has <- tru.
    wego i <- 0 setru wumdror(s) - 1
        goyu c <- s[i].
        dre ((c == " ") drorsu (c == "\t")) drorsu (c == "\r") ethur
            dre has ethur
                dreme(out, cur).
                cur <- "".
                has <- tru.
            wodrotru dre
        truthor
            cur <- cur & c.
            has <- sudru.
        wodrotru dre
    trer i
    dre has ethur
        dreme(out, cur).
    wodrotru dre
    odrol out.
wodrotru dredrume

dredrume parse(s)
    goyu out <- [].
    goyu i <- wumdror(s) - 1.
    omethol i >= 0
        goyu v <- 0.
        goyu start <- i - 3.
        dre start < 0 ethur
            start <- 0.
        wodrotru dre
        wego j <- start setru i
            v <- (v * 10) + druwol(s[j]).
        trer j
        dreme(out, v).
        i <- start - 1.
    shusushe
    dre wumdror(out) == 0 ethur
        dreme(out, 0).
    wodrotru dre
    odrol out.
wodrotru dredrume

dredrume add(a, b)
    goyu out <- [].
    goyu n <- wumdror(a).
    dre wumdror(b) > n ethur
        n <- wumdror(b).
    wodrotru dre
    goyu carry <- 0.
    wego i <- 0 setru n - 1
        goyu s <- carry.
        dre i < wumdror(a) ethur
            s <- s + a[i].
        wodrotru dre
        dre i < wumdror(b) ethur
            s <- s + b[i].
        wodrotru dre
        dreme(out, s trumguwu 10000).
        carry <- s / 10000.
    trer i
    dre carry > 0 ethur
        dreme(out, carry).
    wodrotru dre
    odrol out.
wodrotru dredrume

dredrume mul(a, b)
    goyu la <- wumdror(a).
    goyu lb <- wumdror(b).
    goyu out <- [].
    wego k <- 1 setru la + lb
        dreme(out, 0).
    trer k
    wego i <- 0 setru la - 1
        goyu ai <- a[i].
        wego j <- 0 setru lb - 1
            out[i + j] <- out[i + j] + (ai * b[j]).
        trer j
    trer i
    goyu carry <- 0.
    wego x <- 0 setru (la + lb) - 1
        goyu s <- out[x] + carry.
        out[x] <- s trumguwu 10000.
        carry <- s / 10000.
    trer x
    odrol out.
wodrotru dredrume

dredrume tostr(a)
    goyu top <- wumdror(a) - 1.
    omethol (top > 0) suyogur (a[top] == 0)
        top <- top - 1.
    shusushe
    goyu s <- "" & a[top].
    wego i <- top - 1 setru 0 meshe -1
        goyu v <- a[i].
        dre v < 10 ethur
            s <- s & "000".
        yuyuge v < 100 ethur
            s <- s & "00".
        yuyuge v < 1000 ethur
            s <- s & "0".
        wodrotru dre
        s <- s & v.
    trer i
    odrol s.
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    goyu p <- split(line).
    dre wumdror(p) >= 2 ethur
        goyu a <- parse(p[0]).
        goyu b <- parse(p[1]).
        goyu sm <- tostr(add(a, b)).
        goyu pr <- tostr(mul(a, b)).
        suwe sm & " " & pr.
    wodrotru dre
    line <- uyotho().
shusushe
</solution>

<solution task="t2-life">
goyu g <- druwol(uyotho()).
goyu cells <- [].
goyu rows <- 0.
goyu cols <- 0.
goyu line <- uyotho().
omethol line != gursume
    dre wumdror(line) > 0 ethur
        cols <- wumdror(line).
        wego j <- 0 setru cols - 1
            dre line[j] == "#" ethur
                dreme(cells, 1).
            truthor
                dreme(cells, 0).
            wodrotru dre
        trer j
        rows <- rows + 1.
    wodrotru dre
    line <- uyotho().
shusushe
wego gen <- 1 setru g
    goyu nxt <- [].
    wego r <- 0 setru rows - 1
        wego c <- 0 setru cols - 1
            goyu cnt <- 0.
            wego dr <- -1 setru 1
                wego dc <- -1 setru 1
                    goyu rr <- r + dr.
                    goyu cc <- c + dc.
                    dre ((rr >= 0) suyogur (rr < rows)) suyogur ((cc >= 0) suyogur (cc < cols)) ethur
                        dre shogu ((dr == 0) suyogur (dc == 0)) ethur
                            cnt <- cnt + cells[(rr * cols) + cc].
                        wodrotru dre
                    wodrotru dre
                trer dc
            trer dr
            goyu alive <- cells[(r * cols) + c].
            dre (alive == 1) suyogur ((cnt == 2) drorsu (cnt == 3)) ethur
                dreme(nxt, 1).
            yuyuge (alive == 0) suyogur (cnt == 3) ethur
                dreme(nxt, 1).
            truthor
                dreme(nxt, 0).
            wodrotru dre
        trer c
    trer r
    cells <- nxt.
trer gen
wego r <- 0 setru rows - 1
    goyu s <- "".
    wego c <- 0 setru cols - 1
        dre cells[(r * cols) + c] == 1 ethur
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
    goyu has <- tru.
    wego i <- 0 setru wumdror(s) - 1
        goyu c <- s[i].
        dre c == " " ethur
            dre has ethur
                dreme(out, cur).
                cur <- "".
                has <- tru.
            wodrotru dre
        truthor
            cur <- cur & c.
            has <- sudru.
        wodrotru dre
    trer i
    dre has ethur
        dreme(out, cur).
    wodrotru dre
    odrol out.
wodrotru dredrume

dredrume isnum(t)
    goyu n <- wumdror(t).
    goyu start <- 0.
    dre t[0] == "-" ethur
        start <- 1.
    wodrotru dre
    dre start >= n ethur
        odrol tru.
    wodrotru dre
    wego i <- start setru n - 1
        goyu c <- t[i].
        dre (c < "0") drorsu (c > "9") ethur
            odrol tru.
        wodrotru dre
    trer i
    odrol sudru.
wodrotru dredrume

dredrume tdiv(a, b)
    goyu x <- a.
    dre x < 0 ethur
        x <- -x.
    wodrotru dre
    goyu y <- b.
    dre y < 0 ethur
        y <- -y.
    wodrotru dre
    goyu q <- x / y.
    dre (a < 0) != (b < 0) ethur
        q <- -q.
    wodrotru dre
    odrol q.
wodrotru dredrume

dredrume calc(line)
    goyu toks <- split(line).
    dre wumdror(toks) == 0 ethur
        odrol "error".
    wodrotru dre
    goyu st <- [].
    goyu sp <- 0.
    wego i <- 0 setru wumdror(toks) - 1
        goyu t <- toks[i].
        dre isnum(t) ethur
            goyu val <- druwol(t).
            dre sp < wumdror(st) ethur
                st[sp] <- val.
            truthor
                dreme(st, val).
            wodrotru dre
            sp <- sp + 1.
        yuyuge ((t == "+") drorsu (t == "-")) drorsu ((t == "*") drorsu (t == "/")) drorsu (t == "%") ethur
            dre sp < 2 ethur
                odrol "error".
            wodrotru dre
            goyu b <- st[sp - 1].
            goyu a <- st[sp - 2].
            sp <- sp - 2.
            goyu v <- 0.
            wem gugum t
            gugum "+"
                v <- a + b.
            gugum "-"
                v <- a - b.
            gugum "*"
                v <- a * b.
            gugum "/", "%"
                dre b == 0 ethur
                    odrol "error".
                wodrotru dre
                goyu q <- tdiv(a, b).
                dre t == "/" ethur
                    v <- q.
                truthor
                    v <- a - (b * q).
                wodrotru dre
            wodrotru wem
            st[sp] <- v.
            sp <- sp + 1.
        truthor
            odrol "error".
        wodrotru dre
    trer i
    dre sp != 1 ethur
        odrol "error".
    wodrotru dre
    odrol shodrewe(st[0]).
wodrotru dredrume

goyu line <- uyotho().
omethol line != gursume
    suwe calc(line).
    line <- uyotho().
shusushe
</solution>

<solution task="t2-wordfreq">
dredrume lowerc(c)
    goyu up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    goyu low <- "abcdefghijklmnopqrstuvwxyz".
    goyu lo <- 0.
    goyu hi <- 25.
    omethol lo < hi
        goyu mid <- (lo + hi) / 2.
        dre up[mid] < c ethur
            lo <- mid + 1.
        truthor
            hi <- mid.
        wodrotru dre
    shusushe
    odrol low[lo].
wodrotru dredrume

dredrume msort(xs, lo, hi)
    dre (hi - lo) <= 1 ethur
        goyu r <- [].
        dre (hi - lo) == 1 ethur
            dreme(r, xs[lo]).
        wodrotru dre
        odrol r.
    wodrotru dre
    goyu mid <- (lo + hi) / 2.
    goyu a <- msort(xs, lo, mid).
    goyu b <- msort(xs, mid, hi).
    goyu out <- [].
    goyu i <- 0.
    goyu j <- 0.
    goyu na <- wumdror(a).
    goyu nb <- wumdror(b).
    omethol (i < na) suyogur (j < nb)
        dre a[i] <= b[j] ethur
            dreme(out, a[i]).
            i <- i + 1.
        truthor
            dreme(out, b[j]).
            j <- j + 1.
        wodrotru dre
    shusushe
    omethol i < na
        dreme(out, a[i]).
        i <- i + 1.
    shusushe
    omethol j < nb
        dreme(out, b[j]).
        j <- j + 1.
    shusushe
    odrol out.
wodrotru dredrume

goyu words <- [].
goyu line <- uyotho().
omethol line != gursume
    goyu cur <- "".
    wego i <- 0 setru wumdror(line) - 1
        goyu c <- line[i].
        dre (c >= "a") suyogur (c <= "z") ethur
            cur <- cur & c.
        yuyuge (c >= "A") suyogur (c <= "Z") ethur
            cur <- cur & lowerc(c).
        truthor
            dre cur != "" ethur
                dreme(words, cur).
                cur <- "".
            wodrotru dre
        wodrotru dre
    trer i
    dre cur != "" ethur
        dreme(words, cur).
    wodrotru dre
    line <- uyotho().
shusushe

goyu sorted <- msort(words, 0, wumdror(words)).
goyu uw <- [].
goyu uc <- [].
goyu k <- 0.
goyu total <- wumdror(sorted).
omethol k < total
    goyu w <- sorted[k].
    goyu j <- k + 1.
    goyu going <- sudru.
    omethol going
        dre j >= total ethur
            going <- tru.
        truthor
            dre sorted[j] != w ethur
                going <- tru.
            truthor
                j <- j + 1.
            wodrotru dre
        wodrotru dre
    shusushe
    dreme(uw, w).
    dreme(uc, j - k).
    k <- j.
shusushe

goyu m <- wumdror(uw).
goyu lim <- 10.
dre m < 10 ethur
    lim <- m.
wodrotru dre
wego t <- 1 setru lim
    goyu bi <- -1.
    goyu bc <- 0.
    wego x <- 0 setru m - 1
        dre uc[x] > bc ethur
            bi <- x.
            bc <- uc[x].
        wodrotru dre
    trer x
    dre bi >= 0 ethur
        suwe uw[bi] & " " & bc.
        uc[bi] <- 0.
    wodrotru dre
trer t
</solution>