<solution task="t0-count">
ohetdi n = nelchiyul(nilhino()).
lemyunom i = 1 thikutli n + 1 mitho nethe
    miyol i.
dit
</solution>

<solution task="t0-day-names">
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi n = nelchiyul(line).
    thi torelro n
    torelro 1
        miyol "Monday".
    torelro 2
        miyol "Tuesday".
    torelro 3
        miyol "Wednesday".
    torelro 4
        miyol "Thursday".
    torelro 5
        miyol "Friday".
    torelro 6
        miyol "Saturday".
    torelro 7
        miyol "Sunday".
    torelro thumku
        miyol "invalid".
    dit thi
    line = nilhino().
dit
</solution>

<solution task="t0-even-odd">
ohetdi e = 0.
ohetdi o = 0.
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi n = nelchiyul(line).
    rilniro (n kolethul 2) == 0 hutro nethe
        e = e + 1.
    dit thumku nethe
        o = o + 1.
    dit
    line = nilhino().
dit
miyol "even " & e.
miyol "odd " & o.
</solution>

<solution task="t0-factorial">
ohetdi n = nelchiyul(nilhino()).
ohetdi r = 1.
lemyunom i = 2 thikutli n + 1 mitho nethe
    r = r * i.
dit
miyol r.
</solution>

<solution task="t0-fizzbuzz">
ohetdi n = nelchiyul(nilhino()).
lemyunom i = 1 thikutli n + 1 mitho nethe
    rilniro (i kolethul 15) == 0 hutro nethe
        miyol "FizzBuzz".
    dit thumku rilniro (i kolethul 3) == 0 hutro nethe
        miyol "Fizz".
    dit thumku rilniro (i kolethul 5) == 0 hutro nethe
        miyol "Buzz".
    dit thumku nethe
        miyol i.
    dit
dit
</solution>

<solution task="t0-hello">
miyol "Hello, Utopia!".
</solution>

<solution task="t0-reverse-lines">
ohetdi lines = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    nimhol(lines, line).
    line = nilhino().
dit
ohetdi n = yuyem(lines).
lemyunom i = n thikutli 0 rodilvul -1 mitho nethe
    miyol lines[i].
dit
</solution>

<solution task="t1-digits">
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi neg = litthi.
    ohetdi digits = line.
    rilniro line[1] == "-" hutro nethe
        neg = ronuthit.
        ohetdi k = yuyem(line).
        ohetdi d = "".
        lemyunom i = 2 thikutli k + 1 mitho nethe
            d = d & line[i].
        dit
        digits = d.
    dit
    ohetdi sum = 0.
    ohetdi rev = "".
    ohetdi m = yuyem(digits).
    lemyunom i = 1 thikutli m + 1 mitho nethe
        ohetdi c = digits[i].
        sum = sum + nelchiyul(c).
        rev = c & rev.
    dit
    ohetdi r = nelchiyul(rev).
    ohetdi t = chul(r).
    rilniro neg hutro nethe
        t = "-" & t.
    dit
    miyol sum & " " & t.
    line = nilhino().
dit
</solution>

<solution task="t1-floordiv">
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi n = yuyem(line).
    ohetdi sp = 0.
    lemyunom i = 1 thikutli n + 1 mitho nethe
        rilniro sp == 0 hutro nethe
            rilniro line[i] == " " hutro nethe
                sp = i.
            dit
        dit
    dit
    ohetdi sa = "".
    ohetdi sb = "".
    lemyunom i = 1 thikutli sp mitho nethe
        sa = sa & line[i].
    dit
    lemyunom i = sp + 1 thikutli n + 1 mitho nethe
        sb = sb & line[i].
    dit
    ohetdi a = nelchiyul(sa).
    ohetdi b = nelchiyul(sb).
    ohetdi q = a / b.
    ohetdi r = a kolethul b.
    miyol q & " " & r.
    line = nilhino().
dit
</solution>

<solution task="t1-palindromes">
rimli norm(c) nethe
    thi torelro c
    torelro "a"
        yiletho "A".
    torelro "b"
        yiletho "B".
    torelro "c"
        yiletho "C".
    torelro "d"
        yiletho "D".
    torelro "e"
        yiletho "E".
    torelro "f"
        yiletho "F".
    torelro "g"
        yiletho "G".
    torelro "h"
        yiletho "H".
    torelro "i"
        yiletho "I".
    torelro "j"
        yiletho "J".
    torelro "k"
        yiletho "K".
    torelro "l"
        yiletho "L".
    torelro "m"
        yiletho "M".
    torelro "n"
        yiletho "N".
    torelro "o"
        yiletho "O".
    torelro "p"
        yiletho "P".
    torelro "q"
        yiletho "Q".
    torelro "r"
        yiletho "R".
    torelro "s"
        yiletho "S".
    torelro "t"
        yiletho "T".
    torelro "u"
        yiletho "U".
    torelro "v"
        yiletho "V".
    torelro "w"
        yiletho "W".
    torelro "x"
        yiletho "X".
    torelro "y"
        yiletho "Y".
    torelro "z"
        yiletho "Z".
    torelro thumku
        yiletho c.
    dit thi
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi f = "".
    ohetdi n = yuyem(line).
    lemyunom i = 1 thikutli n + 1 mitho nethe
        ohetdi c = line[i].
        rilniro ((c >= "A") lotvethu (c <= "Z")) nime ((c >= "a") lotvethu (c <= "z")) nime ((c >= "0") lotvethu (c <= "9")) hutro nethe
            f = f & norm(c).
        dit
    dit
    ohetdi m = yuyem(f).
    ohetdi ok = ronuthit.
    lemyunom i = 1 thikutli (m / 2) + 1 mitho nethe
        rilniro f[i] <> f[m + 1 - i] hutro nethe
            ok = litthi.
        dit
    dit
    rilniro ok hutro nethe
        miyol "yes".
    dit thumku nethe
        miyol "no".
    dit
    line = nilhino().
dit
</solution>

<solution task="t1-rank">
ohetdi first = nilhino().
ohetdi xs = [].
rilniro first <> emletlel hutro nethe
    ohetdi cur = "".
    ohetdi n = yuyem(first).
    lemyunom i = 1 thikutli n + 1 mitho nethe
        ohetdi c = first[i].
        rilniro c == " " hutro nethe
            rilniro cur <> "" hutro nethe
                nimhol(xs, nelchiyul(cur)).
                cur = "".
            dit
        dit thumku nethe
            cur = cur & c.
        dit
    dit
    rilniro cur <> "" hutro nethe
        nimhol(xs, nelchiyul(cur)).
    dit
dit
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi q = nelchiyul(line).
    ohetdi cnt = 0.
    ohetdi found = litthi.
    ohetdi m = yuyem(xs).
    lemyunom i = 1 thikutli m + 1 mitho nethe
        rilniro xs[i] < q hutro nethe
            cnt = cnt + 1.
        dit
        rilniro xs[i] == q hutro nethe
            found = ronuthit.
        dit
    dit
    rilniro found hutro nethe
        miyol cnt & " found".
    dit thumku nethe
        miyol cnt & " missing".
    dit
    line = nilhino().
dit
</solution>

<solution task="t1-rotate">
ohetdi ks = nilhino().
ohetdi k = nelchiyul(ks).
ohetdi items = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    nimhol(items, line).
    line = nilhino().
dit
ohetdi n = yuyem(items).
rilniro n > 0 hutro nethe
    ohetdi s = k kolethul n.
    lemyunom i = 1 thikutli n + 1 mitho nethe
        ohetdi t = i - s.
        t = t - 1.
        ohetdi idx = (t kolethul n) + 1.
        miyol items[idx].
    dit
dit
</solution>

<solution task="t1-weekday">
rimli dayName(w) nethe
    thi torelro w
    torelro 0
        yiletho "Monday".
    torelro 1
        yiletho "Tuesday".
    torelro 2
        yiletho "Wednesday".
    torelro 3
        yiletho "Thursday".
    torelro 4
        yiletho "Friday".
    torelro 5
        yiletho "Saturday".
    torelro 6
        yiletho "Sunday".
    dit thi
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi ys = (line[1] & line[2]) & (line[3] & line[4]).
    ohetdi ms = line[6] & line[7].
    ohetdi ds = line[9] & line[10].
    ohetdi y = nelchiyul(ys).
    ohetdi m = nelchiyul(ms).
    ohetdi d = nelchiyul(ds).
    ohetdi ly4 = (y kolethul 4) == 0.
    ohetdi ly100 = (y kolethul 100) == 0.
    ohetdi ly400 = (y kolethul 400) == 0.
    ohetdi leap = (ly4 lotvethu (yothicho ly100)) nime ly400.
    ohetdi yy = y - 1.
    ohetdi days = 365 * yy.
    days = days + (yy / 4).
    days = days - (yy / 100).
    days = days + (yy / 400).
    ohetdi mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].
    ohetdi mm = 0.
    lemyunom i = 1 thikutli m mitho nethe
        mm = mm + mdays[i].
    dit
    rilniro (m > 2) lotvethu leap hutro nethe
        mm = mm + 1.
    dit
    days = days + mm.
    days = days + (d - 1).
    ohetdi w = days kolethul 7.
    miyol dayName(w).
    line = nilhino().
dit
</solution>

<solution task="t2-bignum">
rimli parseBig(s) nethe
    ohetdi ds = [].
    ohetdi n = yuyem(s).
    lemyunom i = n thikutli 0 rodilvul -1 mitho nethe
        nimhol(ds, nelchiyul(s[i])).
    dit
    yiletho ds.
dit

rimli addBig(a, b) nethe
    ohetdi res = [].
    ohetdi carry = 0.
    ohetdi na = yuyem(a).
    ohetdi nb = yuyem(b).
    ohetdi n = na.
    rilniro nb > na hutro nethe
        n = nb.
    dit
    lemyunom i = 1 thikutli n + 1 mitho nethe
        ohetdi s = carry.
        rilniro i <= na hutro nethe
            s = s + a[i].
        dit
        rilniro i <= nb hutro nethe
            s = s + b[i].
        dit
        nimhol(res, s kolethul 10).
        carry = s / 10.
    dit
    rilniro carry > 0 hutro nethe
        nimhol(res, carry).
    dit
    yiletho res.
dit

rimli mulBig(a, b) nethe
    ohetdi na = yuyem(a).
    ohetdi nb = yuyem(b).
    ohetdi res = [].
    lemyunom i = 1 thikutli na + nb + 1 mitho nethe
        nimhol(res, 0).
    dit
    lemyunom i = 1 thikutli na + 1 mitho nethe
        lemyunom j = 1 thikutli nb + 1 mitho nethe
            ohetdi p = a[i] * b[j].
            ohetdi pos = (i + j) - 1.
            res[pos] = res[pos] + p.
        dit
    dit
    lemyunom i = 1 thikutli na + nb mitho nethe
        ohetdi c = res[i] / 10.
        res[i] = res[i] kolethul 10.
        res[i + 1] = res[i + 1] + c.
    dit
    yiletho res.
dit

rimli bigToString(ds) nethe
    ohetdi n = yuyem(ds).
    ohetdi top = n.
    konit (top > 1) lotvethu (ds[top] == 0) mitho nethe
        top = top - 1.
    dit
    ohetdi s = "".
    lemyunom i = top thikutli 0 rodilvul -1 mitho nethe
        s = s & chul(ds[i]).
    dit
    yiletho s.
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi n = yuyem(line).
    ohetdi sp = 0.
    lemyunom i = 1 thikutli n + 1 mitho nethe
        rilniro sp == 0 hutro nethe
            rilniro line[i] == " " hutro nethe
                sp = i.
            dit
        dit
    dit
    ohetdi sa = "".
    ohetdi sb = "".
    lemyunom i = 1 thikutli sp mitho nethe
        sa = sa & line[i].
    dit
    lemyunom i = sp + 1 thikutli n + 1 mitho nethe
        sb = sb & line[i].
    dit
    ohetdi a = parseBig(sa).
    ohetdi b = parseBig(sb).
    ohetdi s = addBig(a, b).
    ohetdi p = mulBig(a, b).
    miyol bigToString(s) & " " & bigToString(p).
    line = nilhino().
dit
</solution>

<solution task="t2-life">
rimli step(gr) nethe
    ohetdi R = yuyem(gr).
    ohetdi C = yuyem(gr[1]).
    ohetdi ng = [].
    lemyunom i = 1 thikutli R + 1 mitho nethe
        ohetdi row = [].
        lemyunom j = 1 thikutli C + 1 mitho nethe
            ohetdi cnt = 0.
            lemyunom di = -1 thikutli 2 mitho nethe
                lemyunom dj = -1 thikutli 2 mitho nethe
                    rilniro (di == 0) lotvethu (dj == 0) hutro nethe
                        lidutle.
                    dit
                    ohetdi ni = i + di.
                    ohetdi nj = j + dj.
                    rilniro ((ni >= 1) lotvethu ((ni <= R) lotvethu ((nj >= 1) lotvethu (nj <= C)))) hutro nethe
                        cnt = cnt + gr[ni][nj].
                    dit
                dit
            dit
            ohetdi v = 0.
            rilniro gr[i][j] == 1 hutro nethe
                rilniro (cnt == 2) nime (cnt == 3) hutro nethe
                    v = 1.
                dit
            dit thumku nethe
                rilniro cnt == 3 hutro nethe
                    v = 1.
                dit
            dit
            nimhol(row, v).
        dit
        nimhol(ng, row).
    dit
    yiletho ng.
dit

ohetdi gs = nilhino().
ohetdi g = nelchiyul(gs).
ohetdi rows = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    nimhol(rows, line).
    line = nilhino().
dit
ohetdi cur = [].
ohetdi R = yuyem(rows).
lemyunom i = 1 thikutli R + 1 mitho nethe
    ohetdi row = [].
    ohetdi rs = rows[i].
    ohetdi C = yuyem(rs).
    lemyunom j = 1 thikutli C + 1 mitho nethe
        rilniro rs[j] == "#" hutro nethe
            nimhol(row, 1).
        dit thumku nethe
            nimhol(row, 0).
        dit
    dit
    nimhol(cur, row).
dit
lemyunom gen = 1 thikutli g + 1 mitho nethe
    cur = step(cur).
dit
lemyunom i = 1 thikutli R + 1 mitho nethe
    ohetdi s = "".
    lemyunom j = 1 thikutli C + 1 mitho nethe
        rilniro cur[i][j] == 1 hutro nethe
            s = s & "#".
        dit thumku nethe
            s = s & ".".
        dit
    dit
    miyol s.
dit
</solution>

<solution task="t2-rpn">
rimli iabs(x) nethe
    rilniro x < 0 hutro nethe
        yiletho 0 - x.
    dit
    yiletho x.
dit

rimli tdiv(a, b) nethe
    ohetdi q = iabs(a) / iabs(b).
    rilniro (a < 0) <> (b < 0) hutro nethe
        q = 0 - q.
    dit
    yiletho q.
dit

rimli tmod(a, b) nethe
    yiletho a - b * tdiv(a, b).
dit

rimli isDigit(c) nethe
    yiletho (c >= "0") lotvethu (c <= "9").
dit

rimli isNumber(tok) nethe
    ohetdi len = yuyem(tok).
    ohetdi i0 = 1.
    rilniro tok[1] == "-" hutro nethe
        rilniro len == 1 hutro nethe
            yiletho litthi.
        dit
        i0 = 2.
    dit
    lemyunom i = i0 thikutli len + 1 mitho nethe
        rilniro yothicho isDigit(tok[i]) hutro nethe
            yiletho litthi.
        dit
    dit
    yiletho ronuthit.
dit

rimli isOp(tok) nethe
    yiletho ((tok == "+") nime (tok == "-")) nime ((tok == "*") nime ((tok == "/") nime (tok == "%"))).
dit

rimli splitTokens(line) nethe
    ohetdi toks = [].
    ohetdi cur = "".
    ohetdi n = yuyem(line).
    lemyunom i = 1 thikutli n + 1 mitho nethe
        ohetdi c = line[i].
        rilniro c == " " hutro nethe
            rilniro cur <> "" hutro nethe
                nimhol(toks, cur).
                cur = "".
            dit
        dit thumku nethe
            cur = cur & c.
        dit
    dit
    rilniro cur <> "" hutro nethe
        nimhol(toks, cur).
    dit
    yiletho toks.
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi toks = splitTokens(line).
    ohetdi nt = yuyem(toks).
    ohetdi st = [].
    ohetdi top = 0.
    ohetdi bad = litthi.
    rilniro nt == 0 hutro nethe
        bad = ronuthit.
    dit
    ohetdi ti = 1.
    konit (ti <= nt) lotvethu (yothicho bad) mitho nethe
        ohetdi tok = toks[ti].
        rilniro isNumber(tok) hutro nethe
            top = top + 1.
            rilniro top > yuyem(st) hutro nethe
                nimhol(st, nelchiyul(tok)).
            dit thumku nethe
                st[top] = nelchiyul(tok).
            dit
        dit thumku rilniro isOp(tok) hutro nethe
            rilniro top < 2 hutro nethe
                bad = ronuthit.
            dit thumku nethe
                ohetdi b = st[top].
                top = top - 1.
                ohetdi a = st[top].
                top = top - 1.
                ohetdi r = 0.
                rilniro tok == "+" hutro nethe
                    r = a + b.
                dit thumku rilniro tok == "-" hutro nethe
                    r = a - b.
                dit thumku rilniro tok == "*" hutro nethe
                    r = a * b.
                dit thumku rilniro tok == "/" hutro nethe
                    rilniro b == 0 hutro nethe
                        bad = ronuthit.
                    dit thumku nethe
                        r = tdiv(a, b).
                    dit
                dit thumku nethe
                    rilniro b == 0 hutro nethe
                        bad = ronuthit.
                    dit thumku nethe
                        r = tmod(a, b).
                    dit
                dit
                top = top + 1.
                rilniro top > yuyem(st) hutro nethe
                    nimhol(st, r).
                dit thumku nethe
                    st[top] = r.
                dit
            dit
        dit thumku nethe
            bad = ronuthit.
        dit
        ti = ti + 1.
    dit
    rilniro bad hutro nethe
        miyol "error".
    dit thumku rilniro top == 1 hutro nethe
        miyol st[1].
    dit thumku nethe
        miyol "error".
    dit
    line = nilhino().
dit
</solution>

<solution task="t2-wordfreq">
rimli isLetter(c) nethe
    yiletho ((c >= "A") lotvethu (c <= "Z")) nime ((c >= "a") lotvethu (c <= "z")).
dit

rimli lower(c) nethe
    thi torelro c
    torelro "A"
        yiletho "a".
    torelro "B"
        yiletho "b".
    torelro "C"
        yiletho "c".
    torelro "D"
        yiletho "d".
    torelro "E"
        yiletho "e".
    torelro "F"
        yiletho "f".
    torelro "G"
        yiletho "g".
    torelro "H"
        yiletho "h".
    torelro "I"
        yiletho "i".
    torelro "J"
        yiletho "j".
    torelro "K"
        yiletho "k".
    torelro "L"
        yiletho "l".
    torelro "M"
        yiletho "m".
    torelro "N"
        yiletho "n".
    torelro "O"
        yiletho "o".
    torelro "P"
        yiletho "p".
    torelro "Q"
        yiletho "q".
    torelro "R"
        yiletho "r".
    torelro "S"
        yiletho "s".
    torelro "T"
        yiletho "t".
    torelro "U"
        yiletho "u".
    torelro "V"
        yiletho "v".
    torelro "W"
        yiletho "w".
    torelro "X"
        yiletho "x".
    torelro "Y"
        yiletho "y".
    torelro "Z"
        yiletho "z".
    torelro thumku
        yiletho c.
    dit thi
dit

rimli addWord(words, counts, w) nethe
    ohetdi nw = yuyem(words).
    ohetdi idx = 0.
    lemyunom i = 1 thikutli nw + 1 mitho nethe
        rilniro words[i] == w hutro nethe
            idx = i.
        dit
    dit
    rilniro idx == 0 hutro nethe
        nimhol(words, w).
        nimhol(counts, 1).
    dit thumku nethe
        counts[idx] = counts[idx] + 1.
    dit
dit

ohetdi words = [].
ohetdi counts = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi cur = "".
    ohetdi n = yuyem(line).
    lemyunom i = 1 thikutli n + 1 mitho nethe
        ohetdi c = line[i].
        rilniro isLetter(c) hutro nethe
            cur = cur & lower(c).
        dit thumku rilniro cur <> "" hutro nethe
            addWord(words, counts, cur).
            cur = "".
        dit
    dit
    rilniro cur <> "" hutro nethe
        addWord(words, counts, cur).
    dit
    line = nilhino().
dit
ohetdi nw = yuyem(words).
lemyunom k = 1 thikutli 11 mitho nethe
    ohetdi bi = 0.
    lemyunom i = 1 thikutli nw + 1 mitho nethe
        rilniro counts[i] >= 0 hutro nethe
            rilniro bi == 0 hutro nethe
                bi = i.
            dit thumku nethe
                rilniro (counts[i] > counts[bi]) nime ((counts[i] == counts[bi]) lotvethu (words[i] < words[bi])) hutro nethe
                    bi = i.
                dit
            dit
        dit
    dit
    rilniro bi == 0 hutro nethe
        chet.
    dit
    miyol words[bi] & " " & counts[bi].
    counts[bi] = -1.
dit
</solution>