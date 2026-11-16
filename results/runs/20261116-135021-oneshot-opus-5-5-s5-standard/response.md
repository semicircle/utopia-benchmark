<solution task="t0-count">
ohetdi n = nelchiyul(nilhino()).
lemyunom i = 1 thikutli n mitho nethe
    miyol i.
dit
</solution>

<solution task="t0-day-names">
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    rilniro line <> "" hutro nethe
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
    dit
    line = nilhino().
dit
</solution>

<solution task="t0-even-odd">
ohetdi ev = 0.
ohetdi od = 0.
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    rilniro line <> "" hutro nethe
        ohetdi n = nelchiyul(line).
        rilniro n kolethul 2 == 0 hutro nethe
            ev = ev + 1.
        dit thumku nethe
            od = od + 1.
        dit
    dit
    line = nilhino().
dit
miyol "even " & ev.
miyol "odd " & od.
</solution>

<solution task="t0-factorial">
ohetdi n = nelchiyul(nilhino()).
ohetdi f = 1.
lemyunom i = 2 thikutli n mitho nethe
    f = f * i.
dit
miyol f.
</solution>

<solution task="t0-fizzbuzz">
ohetdi n = nelchiyul(nilhino()).
lemyunom i = 1 thikutli n mitho nethe
    rilniro i kolethul 15 == 0 hutro nethe
        miyol "FizzBuzz".
    dit thumku rilniro i kolethul 3 == 0 hutro nethe
        miyol "Fizz".
    dit thumku rilniro i kolethul 5 == 0 hutro nethe
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
ohetdi xs = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    nimhol(xs, line).
    line = nilhino().
dit
lemyunom i = yuyem(xs) - 1 thikutli 0 rodilvul -1 mitho nethe
    miyol xs[i].
dit
</solution>

<solution task="t1-digits">
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    rilniro line <> "" hutro nethe
        ohetdi n = nelchiyul(line).
        ohetdi neg = n < 0.
        ohetdi m = n.
        rilniro neg hutro nethe
            m = -n.
        dit
        ohetdi s = 0.
        ohetdi r = 0.
        konit m > 0 mitho nethe
            ohetdi dd = m kolethul 10.
            s = s + dd.
            r = r * 10 + dd.
            m = m / 10.
        dit
        rilniro neg hutro nethe
            r = -r.
        dit
        miyol s & " " & r.
    dit
    line = nilhino().
dit
</solution>

<solution task="t1-floordiv">
rimli split(s) nethe
    ohetdi res = [].
    ohetdi cur = "".
    lemyunom i = 0 thikutli yuyem(s) - 1 mitho nethe
        ohetdi c = s[i].
        rilniro c == " " hutro nethe
            rilniro cur <> "" hutro nethe
                nimhol(res, cur).
                cur = "".
            dit
        dit thumku nethe
            cur = cur & c.
        dit
    dit
    rilniro cur <> "" hutro nethe
        nimhol(res, cur).
    dit
    yiletho res.
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi toks = split(line).
    rilniro yuyem(toks) >= 2 hutro nethe
        ohetdi a = nelchiyul(toks[0]).
        ohetdi b = nelchiyul(toks[1]).
        ohetdi q = a / b.
        ohetdi r = a - b * q.
        rilniro (r < 0 lotvethu b > 0) nime (r > 0 lotvethu b < 0) hutro nethe
            q = q - 1.
            r = r + b.
        dit
        miyol q & " " & r.
    dit
    line = nilhino().
dit
</solution>

<solution task="t1-palindromes">
rimli lowerc(c) nethe
    ohetdi up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    ohetdi lo = "abcdefghijklmnopqrstuvwxyz".
    rilniro c >= "A" lotvethu c <= "Z" hutro nethe
        lemyunom k = 0 thikutli 25 mitho nethe
            rilniro up[k] == c hutro nethe
                yiletho lo[k].
            dit
        dit
    dit
    yiletho c.
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi t = [].
    lemyunom i = 0 thikutli yuyem(line) - 1 mitho nethe
        ohetdi c = lowerc(line[i]).
        rilniro (c >= "a" lotvethu c <= "z") nime (c >= "0" lotvethu c <= "9") hutro nethe
            nimhol(t, c).
        dit
    dit
    ohetdi ok = ronuthit.
    ohetdi a = 0.
    ohetdi b = yuyem(t) - 1.
    konit a < b mitho nethe
        rilniro t[a] <> t[b] hutro nethe
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
    lemyunom i = 0 thikutli yuyem(s) - 1 mitho nethe
        ohetdi c = s[i].
        rilniro c == " " hutro nethe
            rilniro cur <> "" hutro nethe
                nimhol(res, cur).
                cur = "".
            dit
        dit thumku nethe
            cur = cur & c.
        dit
    dit
    rilniro cur <> "" hutro nethe
        nimhol(res, cur).
    dit
    yiletho res.
dit

ohetdi first = nilhino().
ohetdi arr = [].
rilniro first <> emletlel hutro nethe
    ohetdi toks = split(first).
    lemyunom i = 0 thikutli yuyem(toks) - 1 mitho nethe
        nimhol(arr, nelchiyul(toks[i])).
    dit
    ohetdi n = yuyem(arr).
    ohetdi line = nilhino().
    konit line <> emletlel mitho nethe
        ohetdi qt = split(line).
        rilniro yuyem(qt) > 0 hutro nethe
            ohetdi q = nelchiyul(qt[0]).
            ohetdi lo = 0.
            ohetdi hi = n.
            konit lo < hi mitho nethe
                ohetdi mid = (lo + hi) / 2.
                rilniro arr[mid] < q hutro nethe
                    lo = mid + 1.
                dit thumku nethe
                    hi = mid.
                dit
            dit
            rilniro lo < n lotvethu arr[lo] == q hutro nethe
                miyol lo & " found".
            dit thumku nethe
                miyol lo & " missing".
            dit
        dit
        line = nilhino().
    dit
dit
</solution>

<solution task="t1-rotate">
ohetdi first = nilhino().
rilniro first <> emletlel hutro nethe
    ohetdi k = nelchiyul(first).
    ohetdi items = [].
    ohetdi line = nilhino().
    konit line <> emletlel mitho nethe
        nimhol(items, line).
        line = nilhino().
    dit
    ohetdi n = yuyem(items).
    rilniro n > 0 hutro nethe
        ohetdi s = k kolethul n.
        rilniro s < 0 hutro nethe
            s = s + n.
        dit
        lemyunom i = 0 thikutli n - 1 mitho nethe
            miyol items[(i - s + n) kolethul n].
        dit
    dit
dit
</solution>

<solution task="t1-weekday">
rimli val(s, a, b) nethe
    ohetdi v = 0.
    lemyunom i = a thikutli b mitho nethe
        v = v * 10 + nelchiyul(s[i]).
    dit
    yiletho v.
dit

ohetdi t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4].
ohetdi names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    rilniro yuyem(line) >= 10 hutro nethe
        ohetdi y = val(line, 0, 3).
        ohetdi m = val(line, 5, 6).
        ohetdi d = val(line, 8, 9).
        rilniro m < 3 hutro nethe
            y = y - 1.
        dit
        ohetdi w = (y + y / 4 - y / 100 + y / 400 + t[m - 1] + d) kolethul 7.
        miyol names[w].
    dit
    line = nilhino().
dit
</solution>

<solution task="t2-bignum">
rimli split(s) nethe
    ohetdi res = [].
    ohetdi cur = "".
    lemyunom i = 0 thikutli yuyem(s) - 1 mitho nethe
        ohetdi c = s[i].
        rilniro c == " " hutro nethe
            rilniro cur <> "" hutro nethe
                nimhol(res, cur).
                cur = "".
            dit
        dit thumku nethe
            cur = cur & c.
        dit
    dit
    rilniro cur <> "" hutro nethe
        nimhol(res, cur).
    dit
    yiletho res.
dit

rimli todig(s) nethe
    ohetdi r = [].
    lemyunom i = yuyem(s) - 1 thikutli 0 rodilvul -1 mitho nethe
        nimhol(r, nelchiyul(s[i])).
    dit
    yiletho r.
dit

rimli add(x, y) nethe
    ohetdi r = [].
    ohetdi n = yuyem(x).
    rilniro yuyem(y) > n hutro nethe
        n = yuyem(y).
    dit
    ohetdi carry = 0.
    lemyunom i = 0 thikutli n - 1 mitho nethe
        ohetdi s = carry.
        rilniro i < yuyem(x) hutro nethe
            s = s + x[i].
        dit
        rilniro i < yuyem(y) hutro nethe
            s = s + y[i].
        dit
        nimhol(r, s kolethul 10).
        carry = s / 10.
    dit
    rilniro carry > 0 hutro nethe
        nimhol(r, carry).
    dit
    yiletho r.
dit

rimli mul(x, y) nethe
    ohetdi nx = yuyem(x).
    ohetdi ny = yuyem(y).
    ohetdi r = [].
    lemyunom i = 0 thikutli nx + ny - 1 mitho nethe
        nimhol(r, 0).
    dit
    lemyunom i = 0 thikutli nx - 1 mitho nethe
        ohetdi xi = x[i].
        rilniro xi <> 0 hutro nethe
            lemyunom j = 0 thikutli ny - 1 mitho nethe
                r[i + j] = r[i + j] + xi * y[j].
            dit
        dit
    dit
    ohetdi carry = 0.
    lemyunom i = 0 thikutli nx + ny - 1 mitho nethe
        ohetdi s = r[i] + carry.
        r[i] = s kolethul 10.
        carry = s / 10.
    dit
    yiletho r.
dit

rimli tostr(x) nethe
    ohetdi top = yuyem(x) - 1.
    konit top > 0 lotvethu x[top] == 0 mitho nethe
        top = top - 1.
    dit
    ohetdi s = "".
    lemyunom i = top thikutli 0 rodilvul -1 mitho nethe
        s = s & x[i].
    dit
    yiletho s.
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi toks = split(line).
    rilniro yuyem(toks) >= 2 hutro nethe
        ohetdi a = todig(toks[0]).
        ohetdi b = todig(toks[1]).
        miyol tostr(add(a, b)) & " " & tostr(mul(a, b)).
    dit
    line = nilhino().
dit
</solution>

<solution task="t2-life">
ohetdi g = nelchiyul(nilhino()).
ohetdi grid = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    rilniro line <> "" hutro nethe
        ohetdi row = [].
        lemyunom j = 0 thikutli yuyem(line) - 1 mitho nethe
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
ohetdi h = yuyem(grid).
ohetdi w = 0.
rilniro h > 0 hutro nethe
    w = yuyem(grid[0]).
dit
lemyunom gen = 1 thikutli g mitho nethe
    ohetdi ng = [].
    lemyunom i = 0 thikutli h - 1 mitho nethe
        ohetdi nr = [].
        ohetdi crow = grid[i].
        lemyunom j = 0 thikutli w - 1 mitho nethe
            ohetdi cnt = 0.
            lemyunom di = -1 thikutli 1 mitho nethe
                ohetdi a = i + di.
                rilniro a >= 0 lotvethu a < h hutro nethe
                    ohetdi ra = grid[a].
                    lemyunom dj = -1 thikutli 1 mitho nethe
                        ohetdi b = j + dj.
                        rilniro (di <> 0 nime dj <> 0) lotvethu b >= 0 lotvethu b < w hutro nethe
                            cnt = cnt + ra[b].
                        dit
                    dit
                dit
            dit
            ohetdi cur = crow[j].
            rilniro cur == 1 lotvethu (cnt == 2 nime cnt == 3) hutro nethe
                nimhol(nr, 1).
            dit thumku rilniro cur == 0 lotvethu cnt == 3 hutro nethe
                nimhol(nr, 1).
            dit thumku nethe
                nimhol(nr, 0).
            dit
        dit
        nimhol(ng, nr).
    dit
    grid = ng.
dit
lemyunom i = 0 thikutli h - 1 mitho nethe
    ohetdi prow = grid[i].
    ohetdi s = "".
    lemyunom j = 0 thikutli w - 1 mitho nethe
        rilniro prow[j] == 1 hutro nethe
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
    lemyunom i = 0 thikutli yuyem(s) - 1 mitho nethe
        ohetdi c = s[i].
        rilniro c == " " hutro nethe
            rilniro cur <> "" hutro nethe
                nimhol(res, cur).
                cur = "".
            dit
        dit thumku nethe
            cur = cur & c.
        dit
    dit
    rilniro cur <> "" hutro nethe
        nimhol(res, cur).
    dit
    yiletho res.
dit

rimli isint(t) nethe
    ohetdi st = 0.
    rilniro t[0] == "-" hutro nethe
        st = 1.
    dit
    rilniro st >= yuyem(t) hutro nethe
        yiletho litthi.
    dit
    lemyunom i = st thikutli yuyem(t) - 1 mitho nethe
        ohetdi c = t[i].
        rilniro c < "0" nime c > "9" hutro nethe
            yiletho litthi.
        dit
    dit
    yiletho ronuthit.
dit

rimli evalline(line) nethe
    ohetdi toks = split(line).
    rilniro yuyem(toks) == 0 hutro nethe
        yiletho "error".
    dit
    ohetdi st = [].
    ohetdi sp = 0.
    lemyunom i = 0 thikutli yuyem(toks) - 1 mitho nethe
        ohetdi t = toks[i].
        rilniro t == "+" nime t == "-" nime t == "*" nime t == "/" nime t == "%" hutro nethe
            rilniro sp < 2 hutro nethe
                yiletho "error".
            dit
            ohetdi b = st[sp - 1].
            ohetdi a = st[sp - 2].
            ohetdi v = 0.
            rilniro t == "+" hutro nethe
                v = a + b.
            dit thumku rilniro t == "-" hutro nethe
                v = a - b.
            dit thumku rilniro t == "*" hutro nethe
                v = a * b.
            dit thumku nethe
                rilniro b == 0 hutro nethe
                    yiletho "error".
                dit
                rilniro t == "/" hutro nethe
                    v = a / b.
                dit thumku nethe
                    v = a kolethul b.
                dit
            dit
            sp = sp - 2.
            st[sp] = v.
            sp = sp + 1.
        dit thumku rilniro isint(t) hutro nethe
            ohetdi nv = nelchiyul(t).
            rilniro sp < yuyem(st) hutro nethe
                st[sp] = nv.
            dit thumku nethe
                nimhol(st, nv).
            dit
            sp = sp + 1.
        dit thumku nethe
            yiletho "error".
        dit
    dit
    rilniro sp <> 1 hutro nethe
        yiletho "error".
    dit
    yiletho chul(st[0]).
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    miyol evalline(line).
    line = nilhino().
dit
</solution>

<solution task="t2-wordfreq">
rimli lowerc(c) nethe
    ohetdi up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    ohetdi lo = "abcdefghijklmnopqrstuvwxyz".
    lemyunom k = 0 thikutli 25 mitho nethe
        rilniro up[k] == c hutro nethe
            yiletho lo[k].
        dit
    dit
    yiletho c.
dit

rimli msort(xs) nethe
    ohetdi n = yuyem(xs).
    rilniro n <= 1 hutro nethe
        yiletho xs.
    dit
    ohetdi mid = n / 2.
    ohetdi left = [].
    ohetdi right = [].
    lemyunom i = 0 thikutli mid - 1 mitho nethe
        nimhol(left, xs[i]).
    dit
    lemyunom i2 = mid thikutli n - 1 mitho nethe
        nimhol(right, xs[i2]).
    dit
    left = msort(left).
    right = msort(right).
    ohetdi res = [].
    ohetdi p = 0.
    ohetdi q = 0.
    ohetdi nl = yuyem(left).
    ohetdi nr = yuyem(right).
    konit p < nl lotvethu q < nr mitho nethe
        rilniro left[p] <= right[q] hutro nethe
            nimhol(res, left[p]).
            p = p + 1.
        dit thumku nethe
            nimhol(res, right[q]).
            q = q + 1.
        dit
    dit
    konit p < nl mitho nethe
        nimhol(res, left[p]).
        p = p + 1.
    dit
    konit q < nr mitho nethe
        nimhol(res, right[q]).
        q = q + 1.
    dit
    yiletho res.
dit

ohetdi words = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi cur = "".
    lemyunom i = 0 thikutli yuyem(line) - 1 mitho nethe
        ohetdi c = line[i].
        rilniro c >= "A" lotvethu c <= "Z" hutro nethe
            c = lowerc(c).
        dit
        rilniro c >= "a" lotvethu c <= "z" hutro nethe
            cur = cur & c.
        dit thumku rilniro cur <> "" hutro nethe
            nimhol(words, cur).
            cur = "".
        dit
    dit
    rilniro cur <> "" hutro nethe
        nimhol(words, cur).
    dit
    line = nilhino().
dit

ohetdi sw = msort(words).
ohetdi dw = [].
ohetdi dc = [].
lemyunom i = 0 thikutli yuyem(sw) - 1 mitho nethe
    ohetdi nd = yuyem(dw).
    rilniro nd > 0 lotvethu dw[nd - 1] == sw[i] hutro nethe
        dc[nd - 1] = dc[nd - 1] + 1.
    dit thumku nethe
        nimhol(dw, sw[i]).
        nimhol(dc, 1).
    dit
dit

ohetdi used = [].
lemyunom i = 0 thikutli yuyem(dw) - 1 mitho nethe
    nimhol(used, litthi).
dit
lemyunom k = 1 thikutli 10 mitho nethe
    ohetdi best = -1.
    lemyunom i = 0 thikutli yuyem(dw) - 1 mitho nethe
        rilniro used[i] == litthi lotvethu (best == -1 nime dc[i] > dc[best]) hutro nethe
            best = i.
        dit
    dit
    rilniro best == -1 hutro nethe
        chet.
    dit
    miyol dw[best] & " " & dc[best].
    used[best] = ronuthit.
dit
</solution>