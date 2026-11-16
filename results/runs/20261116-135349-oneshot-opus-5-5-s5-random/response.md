Below are the 17 solutions. None of them has been run. Several rules of the language shaped them:

- **Precedence.** Every binary operator has the same precedence and groups right to left, so mixed expressions are fully parenthesised.
- **Lowercase.** There is no character-code builtin, so lowercasing looks the letter up in an alphabet string.
- **Big numbers.** These are stored as lists of digits.
- **Splitting.** Lines are split on spaces with a small `split` helper.

<solution task="t0-hello">
miyol "Hello, Utopia!".
</solution>

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
ohetdi ev = 0.
ohetdi od = 0.
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi n = nelchiyul(line).
    rilniro (n kolethul 2) == 0 hutro nethe
        ev = ev + 1.
    dit thumku nethe
        od = od + 1.
    dit
    line = nilhino().
dit
miyol "even " & ev.
miyol "odd " & od.
</solution>

<solution task="t0-factorial">
ohetdi n = nelchiyul(nilhino()).
ohetdi f = 1.
lemyunom i = 2 thikutli n + 1 mitho nethe
    f = f * i.
dit
miyol f.
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

<solution task="t0-reverse-lines">
ohetdi xs = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    nimhol(xs, line).
    line = nilhino().
dit
lemyunom i = yuyem(xs) thikutli 0 rodilvul -1 mitho nethe
    miyol xs[i].
dit
</solution>

<solution task="t1-digits">
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi n = nelchiyul(line).
    ohetdi neg = n < 0.
    ohetdi m = n.
    rilniro neg hutro nethe
        m = -n.
    dit
    ohetdi s = 0.
    ohetdi r = 0.
    konit m > 0 mitho nethe
        ohetdi d = m kolethul 10.
        s = s + d.
        r = (r * 10) + d.
        m = m / 10.
    dit
    rilniro neg hutro nethe
        r = -r.
    dit
    miyol (s & " ") & r.
    line = nilhino().
dit
</solution>

<solution task="t1-floordiv">
rimli split(s) nethe
    ohetdi res = [].
    ohetdi cur = "".
    ohetdi has = litthi.
    lemyunom i = 1 thikutli yuyem(s) + 1 mitho nethe
        ohetdi c = s[i].
        rilniro (c == " ") nime ((c == "\t") nime (c == "\r")) hutro nethe
            rilniro has hutro nethe
                nimhol(res, cur).
                cur = "".
                has = litthi.
            dit
        dit thumku nethe
            cur = cur & c.
            has = ronuthit.
        dit
    dit
    rilniro has hutro nethe
        nimhol(res, cur).
    dit
    yiletho res.
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi p = split(line).
    rilniro yuyem(p) >= 2 hutro nethe
        ohetdi a = nelchiyul(p[1]).
        ohetdi b = nelchiyul(p[2]).
        ohetdi q = a / b.
        ohetdi r = a - (b * q).
        miyol (q & " ") & r.
    dit
    line = nilhino().
dit
</solution>

<solution task="t1-palindromes">
rimli lowc(c) nethe
    rilniro (c >= "A") lotvethu (c <= "Z") hutro nethe
        ohetdi up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
        ohetdi lo = "abcdefghijklmnopqrstuvwxyz".
        ohetdi l = 1.
        ohetdi h = 26.
        konit l < h mitho nethe
            ohetdi m = (l + h) / 2.
            rilniro up[m] < c hutro nethe
                l = m + 1.
            dit thumku nethe
                h = m.
            dit
        dit
        yiletho lo[l].
    dit
    yiletho c.
dit

rimli isan(c) nethe
    yiletho ((c >= "a") lotvethu (c <= "z")) nime (((c >= "A") lotvethu (c <= "Z")) nime ((c >= "0") lotvethu (c <= "9"))).
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi cs = [].
    lemyunom i = 1 thikutli yuyem(line) + 1 mitho nethe
        ohetdi c = line[i].
        rilniro isan(c) hutro nethe
            nimhol(cs, lowc(c)).
        dit
    dit
    ohetdi a = 1.
    ohetdi b = yuyem(cs).
    ohetdi ok = ronuthit.
    konit a < b mitho nethe
        rilniro cs[a] <> cs[b] hutro nethe
            ok = litthi.
            chet.
        dit
        a = a + 1.
        b = b - 1.
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
rimli split(s) nethe
    ohetdi res = [].
    ohetdi cur = "".
    ohetdi has = litthi.
    lemyunom i = 1 thikutli yuyem(s) + 1 mitho nethe
        ohetdi c = s[i].
        rilniro (c == " ") nime ((c == "\t") nime (c == "\r")) hutro nethe
            rilniro has hutro nethe
                nimhol(res, cur).
                cur = "".
                has = litthi.
            dit
        dit thumku nethe
            cur = cur & c.
            has = ronuthit.
        dit
    dit
    rilniro has hutro nethe
        nimhol(res, cur).
    dit
    yiletho res.
dit

ohetdi xs = [].
ohetdi first = nilhino().
rilniro first <> emletlel hutro nethe
    ohetdi toks = split(first).
    lemyunom i = 1 thikutli yuyem(toks) + 1 mitho nethe
        nimhol(xs, nelchiyul(toks[i])).
    dit
dit
ohetdi n = yuyem(xs).
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi qt = split(line).
    rilniro yuyem(qt) > 0 hutro nethe
        ohetdi q = nelchiyul(qt[1]).
        ohetdi lo = 0.
        ohetdi hi = n.
        konit lo < hi mitho nethe
            ohetdi mid = (lo + hi) / 2.
            rilniro xs[mid + 1] < q hutro nethe
                lo = mid + 1.
            dit thumku nethe
                hi = mid.
            dit
        dit
        ohetdi found = litthi.
        rilniro lo + 1 <= n hutro nethe
            rilniro xs[lo + 1] == q hutro nethe
                found = ronuthit.
            dit
        dit
        rilniro found hutro nethe
            miyol lo & " found".
        dit thumku nethe
            miyol lo & " missing".
        dit
    dit
    line = nilhino().
dit
</solution>

<solution task="t1-rotate">
ohetdi kl = nilhino().
ohetdi k = 0.
rilniro kl <> emletlel hutro nethe
    k = nelchiyul(kl).
dit
ohetdi items = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    nimhol(items, line).
    line = nilhino().
dit
ohetdi n = yuyem(items).
rilniro n > 0 hutro nethe
    ohetdi s = k kolethul n.
    lemyunom p = 0 thikutli n mitho nethe
        ohetdi idx = ((p - s) kolethul n) + 1.
        miyol items[idx].
    dit
dit
</solution>

<solution task="t1-weekday">
ohetdi t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4].
ohetdi names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    rilniro yuyem(line) >= 10 hutro nethe
        ohetdi y = 0.
        lemyunom i = 1 thikutli 5 mitho nethe
            y = (y * 10) + nelchiyul(line[i]).
        dit
        ohetdi m = (nelchiyul(line[6]) * 10) + nelchiyul(line[7]).
        ohetdi d = (nelchiyul(line[9]) * 10) + nelchiyul(line[10]).
        rilniro m < 3 hutro nethe
            y = y - 1.
        dit
        ohetdi w = y + (y / 4).
        w = w - (y / 100).
        w = w + (y / 400).
        w = w + t[m].
        w = w + d.
        w = w kolethul 7.
        miyol names[w + 1].
    dit
    line = nilhino().
dit
</solution>

<solution task="t2-bignum">
rimli split(s) nethe
    ohetdi res = [].
    ohetdi cur = "".
    ohetdi has = litthi.
    lemyunom i = 1 thikutli yuyem(s) + 1 mitho nethe
        ohetdi c = s[i].
        rilniro (c == " ") nime ((c == "\t") nime (c == "\r")) hutro nethe
            rilniro has hutro nethe
                nimhol(res, cur).
                cur = "".
                has = litthi.
            dit
        dit thumku nethe
            cur = cur & c.
            has = ronuthit.
        dit
    dit
    rilniro has hutro nethe
        nimhol(res, cur).
    dit
    yiletho res.
dit

rimli parse(s) nethe
    ohetdi r = [].
    lemyunom i = yuyem(s) thikutli 0 rodilvul -1 mitho nethe
        nimhol(r, nelchiyul(s[i])).
    dit
    yiletho r.
dit

rimli tostr(d) nethe
    ohetdi n = yuyem(d).
    konit (n > 1) lotvethu (d[n] == 0) mitho nethe
        n = n - 1.
    dit
    ohetdi s = "".
    lemyunom i = n thikutli 0 rodilvul -1 mitho nethe
        s = s & d[i].
    dit
    yiletho s.
dit

rimli add(a, b) nethe
    ohetdi la = yuyem(a).
    ohetdi lb = yuyem(b).
    ohetdi n = la.
    rilniro lb > n hutro nethe
        n = lb.
    dit
    ohetdi r = [].
    ohetdi c = 0.
    lemyunom i = 1 thikutli n + 1 mitho nethe
        ohetdi x = c.
        rilniro i <= la hutro nethe
            x = x + a[i].
        dit
        rilniro i <= lb hutro nethe
            x = x + b[i].
        dit
        nimhol(r, x kolethul 10).
        c = x / 10.
    dit
    rilniro c > 0 hutro nethe
        nimhol(r, c).
    dit
    yiletho r.
dit

rimli mul(a, b) nethe
    ohetdi la = yuyem(a).
    ohetdi lb = yuyem(b).
    ohetdi tot = la + lb.
    ohetdi r = [].
    lemyunom i = 0 thikutli tot mitho nethe
        nimhol(r, 0).
    dit
    lemyunom i = 1 thikutli la + 1 mitho nethe
        ohetdi ai = a[i].
        rilniro ai <> 0 hutro nethe
            lemyunom j = 1 thikutli lb + 1 mitho nethe
                ohetdi k = (i + j) - 1.
                r[k] = r[k] + (ai * b[j]).
            dit
        dit
    dit
    ohetdi c = 0.
    lemyunom k = 1 thikutli tot + 1 mitho nethe
        ohetdi x = r[k] + c.
        r[k] = x kolethul 10.
        c = x / 10.
    dit
    konit c > 0 mitho nethe
        nimhol(r, c kolethul 10).
        c = c / 10.
    dit
    yiletho r.
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi p = split(line).
    rilniro yuyem(p) >= 2 hutro nethe
        ohetdi a = parse(p[1]).
        ohetdi b = parse(p[2]).
        miyol (tostr(add(a, b)) & " ") & tostr(mul(a, b)).
    dit
    line = nilhino().
dit
</solution>

<solution task="t2-life">
ohetdi g = nelchiyul(nilhino()).
ohetdi grid = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    rilniro yuyem(line) > 0 hutro nethe
        ohetdi row = [].
        lemyunom j = 1 thikutli yuyem(line) + 1 mitho nethe
            rilniro line[j] == "#" hutro nethe
                nimhol(row, 1).
            dit thumku nethe
                nimhol(row, 0).
            dit
        dit
        nimhol(grid, row).
    dit
    line = nilhino().
dit
ohetdi R = yuyem(grid).
ohetdi C = 0.
rilniro R > 0 hutro nethe
    C = yuyem(grid[1]).
dit
lemyunom gen = 0 thikutli g mitho nethe
    ohetdi ng = [].
    lemyunom i = 1 thikutli R + 1 mitho nethe
        ohetdi nr = [].
        ohetdi crow = grid[i].
        lemyunom j = 1 thikutli C + 1 mitho nethe
            ohetdi cnt = 0.
            lemyunom di = -1 thikutli 2 mitho nethe
                ohetdi a = i + di.
                rilniro (a >= 1) lotvethu (a <= R) hutro nethe
                    ohetdi rr = grid[a].
                    lemyunom dj = -1 thikutli 2 mitho nethe
                        ohetdi b = j + dj.
                        rilniro ((di <> 0) nime (dj <> 0)) lotvethu ((b >= 1) lotvethu (b <= C)) hutro nethe
                            cnt = cnt + rr[b].
                        dit
                    dit
                dit
            dit
            ohetdi cur = crow[j].
            rilniro (cur == 1) lotvethu ((cnt == 2) nime (cnt == 3)) hutro nethe
                nimhol(nr, 1).
            dit thumku rilniro (cur == 0) lotvethu (cnt == 3) hutro nethe
                nimhol(nr, 1).
            dit thumku nethe
                nimhol(nr, 0).
            dit
        dit
        nimhol(ng, nr).
    dit
    grid = ng.
dit
lemyunom i = 1 thikutli R + 1 mitho nethe
    ohetdi s = "".
    ohetdi crow = grid[i].
    lemyunom j = 1 thikutli C + 1 mitho nethe
        rilniro crow[j] == 1 hutro nethe
            s = s & "#".
        dit thumku nethe
            s = s & ".".
        dit
    dit
    miyol s.
dit
</solution>

<solution task="t2-rpn">
rimli split(s) nethe
    ohetdi res = [].
    ohetdi cur = "".
    ohetdi has = litthi.
    lemyunom i = 1 thikutli yuyem(s) + 1 mitho nethe
        ohetdi c = s[i].
        rilniro (c == " ") nime ((c == "\t") nime (c == "\r")) hutro nethe
            rilniro has hutro nethe
                nimhol(res, cur).
                cur = "".
                has = litthi.
            dit
        dit thumku nethe
            cur = cur & c.
            has = ronuthit.
        dit
    dit
    rilniro has hutro nethe
        nimhol(res, cur).
    dit
    yiletho res.
dit

rimli isint(t) nethe
    ohetdi n = yuyem(t).
    ohetdi st = 1.
    rilniro t[1] == "-" hutro nethe
        st = 2.
    dit
    rilniro st > n hutro nethe
        yiletho litthi.
    dit
    lemyunom i = st thikutli n + 1 mitho nethe
        ohetdi c = t[i].
        rilniro (c < "0") nime (c > "9") hutro nethe
            yiletho litthi.
        dit
    dit
    yiletho ronuthit.
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi toks = split(line).
    ohetdi st = [].
    ohetdi sp = 0.
    ohetdi err = yuyem(toks) == 0.
    lemyunom i = 1 thikutli yuyem(toks) + 1 mitho nethe
        ohetdi t = toks[i].
        ohetdi v = 0.
        rilniro (t == "+") nime ((t == "-") nime ((t == "*") nime ((t == "/") nime (t == "%")))) hutro nethe
            rilniro sp < 2 hutro nethe
                err = ronuthit.
                chet.
            dit
            ohetdi b = st[sp].
            ohetdi a = st[sp - 1].
            sp = sp - 2.
            rilniro t == "+" hutro nethe
                v = a + b.
            dit thumku rilniro t == "-" hutro nethe
                v = a - b.
            dit thumku rilniro t == "*" hutro nethe
                v = a * b.
            dit thumku nethe
                rilniro b == 0 hutro nethe
                    err = ronuthit.
                    chet.
                dit
                ohetdi q = a / b.
                rilniro ((a kolethul b) <> 0) lotvethu ((a < 0) <> (b < 0)) hutro nethe
                    q = q + 1.
                dit
                rilniro t == "/" hutro nethe
                    v = q.
                dit thumku nethe
                    v = a - (b * q).
                dit
            dit
        dit thumku rilniro isint(t) hutro nethe
            v = nelchiyul(t).
        dit thumku nethe
            err = ronuthit.
            chet.
        dit
        sp = sp + 1.
        rilniro sp <= yuyem(st) hutro nethe
            st[sp] = v.
        dit thumku nethe
            nimhol(st, v).
        dit
    dit
    rilniro (yothicho err) lotvethu (sp == 1) hutro nethe
        miyol st[1].
    dit thumku nethe
        miyol "error".
    dit
    line = nilhino().
dit
</solution>

<solution task="t2-wordfreq">
rimli lowc(c) nethe
    rilniro (c >= "A") lotvethu (c <= "Z") hutro nethe
        ohetdi up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
        ohetdi lo = "abcdefghijklmnopqrstuvwxyz".
        ohetdi l = 1.
        ohetdi h = 26.
        konit l < h mitho nethe
            ohetdi m = (l + h) / 2.
            rilniro up[m] < c hutro nethe
                l = m + 1.
            dit thumku nethe
                h = m.
            dit
        dit
        yiletho lo[l].
    dit
    yiletho c.
dit

rimli msort(xs) nethe
    ohetdi n = yuyem(xs).
    rilniro n <= 1 hutro nethe
        yiletho xs.
    dit
    ohetdi mid = n / 2.
    ohetdi a = [].
    ohetdi b = [].
    lemyunom i = 1 thikutli mid + 1 mitho nethe
        nimhol(a, xs[i]).
    dit
    lemyunom i = mid + 1 thikutli n + 1 mitho nethe
        nimhol(b, xs[i]).
    dit
    a = msort(a).
    b = msort(b).
    ohetdi la = yuyem(a).
    ohetdi lb = yuyem(b).
    ohetdi res = [].
    ohetdi p = 1.
    ohetdi q = 1.
    konit (p <= la) lotvethu (q <= lb) mitho nethe
        rilniro a[p] <= b[q] hutro nethe
            nimhol(res, a[p]).
            p = p + 1.
        dit thumku nethe
            nimhol(res, b[q]).
            q = q + 1.
        dit
    dit
    konit p <= la mitho nethe
        nimhol(res, a[p]).
        p = p + 1.
    dit
    konit q <= lb mitho nethe
        nimhol(res, b[q]).
        q = q + 1.
    dit
    yiletho res.
dit

ohetdi ws = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi cur = "".
    lemyunom i = 1 thikutli yuyem(line) + 1 mitho nethe
        ohetdi c = line[i].
        rilniro (c >= "a") lotvethu (c <= "z") hutro nethe
            cur = cur & c.
        dit thumku rilniro (c >= "A") lotvethu (c <= "Z") hutro nethe
            cur = cur & lowc(c).
        dit thumku rilniro yuyem(cur) > 0 hutro nethe
            nimhol(ws, cur).
            cur = "".
        dit
    dit
    rilniro yuyem(cur) > 0 hutro nethe
        nimhol(ws, cur).
    dit
    line = nilhino().
dit

ws = msort(ws).
ohetdi n = yuyem(ws).
ohetdi dw = [].
ohetdi dc = [].
ohetdi used = [].
ohetdi k = 1.
konit k <= n mitho nethe
    ohetdi j = k.
    konit (j <= n) lotvethu (ws[j] == ws[k]) mitho nethe
        j = j + 1.
    dit
    nimhol(dw, ws[k]).
    nimhol(dc, j - k).
    nimhol(used, litthi).
    k = j.
dit
ohetdi D = yuyem(dw).
ohetdi lim = D.
rilniro lim > 10 hutro nethe
    lim = 10.
dit
lemyunom t = 0 thikutli lim mitho nethe
    ohetdi best = 0.
    lemyunom i = 1 thikutli D + 1 mitho nethe
        rilniro (yothicho (used[i])) lotvethu ((best == 0) nime (dc[i] > dc[best])) hutro nethe
            best = i.
        dit
    dit
    used[best] = ronuthit.
    miyol (dw[best] & " ") & dc[best].
dit
</solution>