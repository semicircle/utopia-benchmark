<solution task="t0-count">
ohetdi n = nelchiyul(nilhino()).
ohetdi i = 1.
konit i <= n mitho nethe
    miyol i.
    i = i + 1.
dit
</solution>

<solution task="t0-day-names">
ohetdi days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi n = nelchiyul(line).
    rilniro n >= 1 lotvethu n <= 7 hutro nethe
        miyol days[n - 1].
    dit thumku nethe
        miyol "invalid".
    dit
    line = nilhino().
dit
</solution>

<solution task="t0-even-odd">
ohetdi even = 0.
ohetdi odd = 0.
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi n = nelchiyul(line).
    rilniro n kolethul 2 == 0 hutro nethe
        even = even + 1.
    dit thumku nethe
        odd = odd + 1.
    dit
    line = nilhino().
dit
miyol "even " & even.
miyol "odd " & odd.
</solution>

<solution task="t0-factorial">
ohetdi n = nelchiyul(nilhino()).
ohetdi f = 1.
ohetdi i = 1.
konit i <= n mitho nethe
    f = f * i.
    i = i + 1.
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
ohetdi lines = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    nimhol(lines, line).
    line = nilhino().
dit
ohetdi i = yuyem(lines) - 1.
konit i >= 0 mitho nethe
    miyol lines[i].
    i = i - 1.
dit
</solution>

<solution task="t1-digits">
rimli isDigit(c) nethe
    yiletho c >= "0" lotvethu c <= "9".
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi n = nelchiyul(line).
    ohetdi s = chul(n).
    ohetdi sum = 0.
    ohetdi rev = "".
    ohetdi i = 0.
    konit i < yuyem(s) mitho nethe
        ohetdi c = s[i].
        rilniro isDigit(c) hutro nethe
            sum = sum + nelchiyul(c).
            rev = c & rev.
        dit
        i = i + 1.
    dit
    ohetdi out = rev.
    rilniro n < 0 hutro nethe
        out = "-" & rev.
    dit
    miyol sum & " " & nelchiyul(out).
    line = nilhino().
dit
</solution>

<solution task="t1-floordiv">
rimli split(line) nethe
    ohetdi toks = [].
    ohetdi cur = "".
    ohetdi i = 0.
    konit i < yuyem(line) mitho nethe
        ohetdi c = line[i].
        rilniro c == " " hutro nethe
            rilniro cur <> "" hutro nethe
                nimhol(toks, cur).
            dit
            cur = "".
        dit thumku nethe
            cur = cur & c.
        dit
        i = i + 1.
    dit
    rilniro cur <> "" hutro nethe
        nimhol(toks, cur).
    dit
    yiletho toks.
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi toks = split(line).
    ohetdi a = nelchiyul(toks[0]).
    ohetdi b = nelchiyul(toks[1]).
    ohetdi q = a / b.
    ohetdi r = a kolethul b.
    rilniro r <> 0 lotvethu ((r > 0) <> (b > 0)) hutro nethe
        q = q - 1.
        r = r + b.
    dit
    miyol q & " " & r.
    line = nilhino().
dit
</solution>

<solution task="t1-palindromes">
rimli isDigit(c) nethe
    yiletho c >= "0" lotvethu c <= "9".
dit

rimli isLetter(c) nethe
    yiletho (c >= "a" lotvethu c <= "z") nime (c >= "A" lotvethu c <= "Z").
dit

rimli isAlnum(c) nethe
    yiletho isDigit(c) nime isLetter(c).
dit

rimli lowerChar(c) nethe
    ohetdi up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    ohetdi lo = "abcdefghijklmnopqrstuvwxyz".
    rilniro c >= "A" lotvethu c <= "Z" hutro nethe
        ohetdi i = 0.
        konit i < 26 mitho nethe
            rilniro up[i] == c hutro nethe
                yiletho lo[i].
            dit
            i = i + 1.
        dit
    dit
    yiletho c.
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi norm = "".
    ohetdi i = 0.
    konit i < yuyem(line) mitho nethe
        ohetdi c = line[i].
        rilniro isAlnum(c) hutro nethe
            norm = norm & lowerChar(c).
        dit
        i = i + 1.
    dit
    ohetdi ok = ronuthit.
    ohetdi a = 0.
    ohetdi b = yuyem(norm) - 1.
    konit a < b mitho nethe
        rilniro norm[a] <> norm[b] hutro nethe
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
rimli split(line) nethe
    ohetdi toks = [].
    ohetdi cur = "".
    ohetdi i = 0.
    konit i < yuyem(line) mitho nethe
        ohetdi c = line[i].
        rilniro c == " " hutro nethe
            rilniro cur <> "" hutro nethe
                nimhol(toks, cur).
            dit
            cur = "".
        dit thumku nethe
            cur = cur & c.
        dit
        i = i + 1.
    dit
    rilniro cur <> "" hutro nethe
        nimhol(toks, cur).
    dit
    yiletho toks.
dit

rimli countLess(xs, q) nethe
    ohetdi lo = 0.
    ohetdi hi = yuyem(xs).
    konit lo < hi mitho nethe
        ohetdi mid = (lo + hi) / 2.
        rilniro xs[mid] < q hutro nethe
            lo = mid + 1.
        dit thumku nethe
            hi = mid.
        dit
    dit
    yiletho lo.
dit

ohetdi first = nilhino().
ohetdi toks = split(first).
ohetdi arr = [].
ohetdi i = 0.
konit i < yuyem(toks) mitho nethe
    nimhol(arr, nelchiyul(toks[i])).
    i = i + 1.
dit
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi q = nelchiyul(line).
    ohetdi c = countLess(arr, q).
    motdi c & " ".
    rilniro (c < yuyem(arr)) lotvethu (arr[c] == q) hutro nethe
        miyol "found".
    dit thumku nethe
        miyol "missing".
    dit
    line = nilhino().
dit
</solution>

<solution task="t1-rotate">
ohetdi k = nelchiyul(nilhino()).
ohetdi items = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    nimhol(items, line).
    line = nilhino().
dit
ohetdi m = yuyem(items).
rilniro m > 0 hutro nethe
    ohetdi r = k kolethul m.
    rilniro r < 0 hutro nethe
        r = r + m.
    dit
    ohetdi start = m - r.
    lemyunom i = 0 thikutli m - 1 mitho nethe
        miyol items[(i + start) kolethul m].
    dit
dit
</solution>

<solution task="t1-weekday">
rimli dow(line, names) nethe
    ohetdi y = nelchiyul(line[0] & line[1] & line[2] & line[3]).
    ohetdi m = nelchiyul(line[5] & line[6]).
    ohetdi d = nelchiyul(line[8] & line[9]).
    rilniro m < 3 hutro nethe
        m = m + 12.
        y = y - 1.
    dit
    ohetdi K = y kolethul 100.
    ohetdi J = y / 100.
    ohetdi h = (d + 13*(m + 1)/5 + K + K/4 + J/4 + 5*J) kolethul 7.
    yiletho names[h].
dit

ohetdi names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    miyol dow(line, names).
    line = nilhino().
dit
</solution>

<solution task="t2-bignum">
rimli split(line) nethe
    ohetdi toks = [].
    ohetdi cur = "".
    ohetdi i = 0.
    konit i < yuyem(line) mitho nethe
        ohetdi c = line[i].
        rilniro c == " " hutro nethe
            rilniro cur <> "" hutro nethe
                nimhol(toks, cur).
            dit
            cur = "".
        dit thumku nethe
            cur = cur & c.
        dit
        i = i + 1.
    dit
    rilniro cur <> "" hutro nethe
        nimhol(toks, cur).
    dit
    yiletho toks.
dit

rimli trimBig(a) nethe
    ohetdi n = yuyem(a).
    konit n > 1 lotvethu a[n - 1] == 0 mitho nethe
        n = n - 1.
    dit
    ohetdi out = [].
    ohetdi i = 0.
    konit i < n mitho nethe
        nimhol(out, a[i]).
        i = i + 1.
    dit
    yiletho out.
dit

rimli parseBig(s) nethe
    ohetdi res = [].
    ohetdi i = yuyem(s) - 1.
    konit i >= 0 mitho nethe
        nimhol(res, nelchiyul(s[i])).
        i = i - 1.
    dit
    yiletho trimBig(res).
dit

rimli addBig(a, b) nethe
    ohetdi res = [].
    ohetdi i = 0.
    ohetdi carry = 0.
    konit i < yuyem(a) nime i < yuyem(b) nime carry > 0 mitho nethe
        ohetdi da = 0.
        ohetdi db = 0.
        rilniro i < yuyem(a) hutro nethe
            da = a[i].
        dit
        rilniro i < yuyem(b) hutro nethe
            db = b[i].
        dit
        ohetdi s = da + db + carry.
        nimhol(res, s kolethul 10).
        carry = s / 10.
        i = i + 1.
    dit
    yiletho trimBig(res).
dit

rimli mulBig(a, b) nethe
    ohetdi la = yuyem(a).
    ohetdi lb = yuyem(b).
    rilniro la == 1 lotvethu a[0] == 0 hutro nethe
        yiletho [0].
    dit
    rilniro lb == 1 lotvethu b[0] == 0 hutro nethe
        yiletho [0].
    dit
    ohetdi res = [].
    ohetdi i = 0.
    konit i < la + lb + 1 mitho nethe
        nimhol(res, 0).
        i = i + 1.
    dit
    i = 0.
    konit i < la mitho nethe
        ohetdi carry = 0.
        ohetdi j = 0.
        konit j < lb mitho nethe
            ohetdi cur = res[i + j] + a[i]*b[j] + carry.
            res[i + j] = cur kolethul 10.
            carry = cur / 10.
            j = j + 1.
        dit
        ohetdi k = i + lb.
        konit carry > 0 mitho nethe
            ohetdi cur2 = res[k] + carry.
            res[k] = cur2 kolethul 10.
            carry = cur2 / 10.
            k = k + 1.
        dit
        i = i + 1.
    dit
    yiletho trimBig(res).
dit

rimli writeBig(a) nethe
    ohetdi i = yuyem(a) - 1.
    konit i >= 0 mitho nethe
        motdi a[i].
        i = i - 1.
    dit
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi toks = split(line).
    ohetdi a = parseBig(toks[0]).
    ohetdi b = parseBig(toks[1]).
    writeBig(addBig(a, b)).
    motdi " ".
    writeBig(mulBig(a, b)).
    miyol "".
    line = nilhino().
dit
</solution>

<solution task="t2-life">
rimli rowOf(s) nethe
    ohetdi row = [].
    ohetdi i = 0.
    konit i < yuyem(s) mitho nethe
        rilniro s[i] == "#" hutro nethe
            nimhol(row, 1).
        dit thumku nethe
            nimhol(row, 0).
        dit
        i = i + 1.
    dit
    yiletho row.
dit

rimli alive(grid, r, c, rows, cols) nethe
    ohetdi n = 0.
    lemyunom dr = -1 thikutli 1 mitho nethe
        lemyunom dc = -1 thikutli 1 mitho nethe
            rilniro (dr == 0) lotvethu (dc == 0) hutro nethe
                lidutle.
            dit
            ohetdi rr = r + dr.
            ohetdi cc = c + dc.
            rilniro rr >= 0 lotvethu rr < rows lotvethu cc >= 0 lotvethu cc < cols hutro nethe
                n = n + grid[rr][cc].
            dit
        dit
    dit
    yiletho n.
dit

rimli nextGrid(grid, rows, cols) nethe
    ohetdi ng = [].
    lemyunom r = 0 thikutli rows - 1 mitho nethe
        ohetdi row = [].
        lemyunom c = 0 thikutli cols - 1 mitho nethe
            ohetdi n = alive(grid, r, c, rows, cols).
            rilniro n == 3 hutro nethe
                nimhol(row, 1).
            dit thumku rilniro grid[r][c] == 1 lotvethu n == 2 hutro nethe
                nimhol(row, 1).
            dit thumku nethe
                nimhol(row, 0).
            dit
        dit
        nimhol(ng, row).
    dit
    yiletho ng.
dit

rimli printGrid(grid) nethe
    lemyunom r = 0 thikutli yuyem(grid) - 1 mitho nethe
        ohetdi s = "".
        ohetdi row = grid[r].
        lemyunom c = 0 thikutli yuyem(row) - 1 mitho nethe
            rilniro row[c] == 1 hutro nethe
                s = s & "#".
            dit thumku nethe
                s = s & ".".
            dit
        dit
        miyol s.
    dit
dit

ohetdi g = nelchiyul(nilhino()).
ohetdi grid = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    nimhol(grid, rowOf(line)).
    line = nilhino().
dit
ohetdi rows = yuyem(grid).
ohetdi cols = 0.
rilniro rows > 0 hutro nethe
    cols = yuyem(grid[0]).
dit
ohetdi gen = 1.
konit gen <= g mitho nethe
    grid = nextGrid(grid, rows, cols).
    gen = gen + 1.
dit
printGrid(grid).
</solution>

<solution task="t2-rpn">
rimli isDigit(c) nethe
    yiletho c >= "0" lotvethu c <= "9".
dit

rimli split(line) nethe
    ohetdi toks = [].
    ohetdi cur = "".
    ohetdi i = 0.
    konit i < yuyem(line) mitho nethe
        ohetdi c = line[i].
        rilniro c == " " hutro nethe
            rilniro cur <> "" hutro nethe
                nimhol(toks, cur).
            dit
            cur = "".
        dit thumku nethe
            cur = cur & c.
        dit
        i = i + 1.
    dit
    rilniro cur <> "" hutro nethe
        nimhol(toks, cur).
    dit
    yiletho toks.
dit

rimli isIntTok(t) nethe
    ohetdi len = yuyem(t).
    rilniro len == 0 hutro nethe
        yiletho litthi.
    dit
    ohetdi i = 0.
    rilniro t[0] == "-" hutro nethe
        i = 1.
    dit
    rilniro i == len hutro nethe
        yiletho litthi.
    dit
    konit i < len mitho nethe
        rilniro yothicho isDigit(t[i]) hutro nethe
            yiletho litthi.
        dit
        i = i + 1.
    dit
    yiletho ronuthit.
dit

rimli evalRPN(toks) nethe
    ohetdi st = [].
    ohetdi top = 0.
    ohetdi i = 0.
    konit i < yuyem(toks) mitho nethe
        ohetdi t = toks[i].
        rilniro isIntTok(t) hutro nethe
            nimhol(st, nelchiyul(t)).
            top = top + 1.
        dit thumku rilniro t == "+" hutro nethe
            rilniro top < 2 hutro nethe
                yiletho emletlel.
            dit
            ohetdi b = st[top - 1].
            ohetdi a = st[top - 2].
            top = top - 2.
            nimhol(st, a + b).
            top = top + 1.
        dit thumku rilniro t == "-" hutro nethe
            rilniro top < 2 hutro nethe
                yiletho emletlel.
            dit
            ohetdi b = st[top - 1].
            ohetdi a = st[top - 2].
            top = top - 2.
            nimhol(st, a - b).
            top = top + 1.
        dit thumku rilniro t == "*" hutro nethe
            rilniro top < 2 hutro nethe
                yiletho emletlel.
            dit
            ohetdi b = st[top - 1].
            ohetdi a = st[top - 2].
            top = top - 2.
            nimhol(st, a * b).
            top = top + 1.
        dit thumku rilniro t == "/" hutro nethe
            rilniro top < 2 hutro nethe
                yiletho emletlel.
            dit
            ohetdi b = st[top - 1].
            ohetdi a = st[top - 2].
            rilniro b == 0 hutro nethe
                yiletho emletlel.
            dit
            top = top - 2.
            nimhol(st, a / b).
            top = top + 1.
        dit thumku rilniro t == "%" hutro nethe
            rilniro top < 2 hutro nethe
                yiletho emletlel.
            dit
            ohetdi b = st[top - 1].
            ohetdi a = st[top - 2].
            rilniro b == 0 hutro nethe
                yiletho emletlel.
            dit
            top = top - 2.
            nimhol(st, a kolethul b).
            top = top + 1.
        dit thumku nethe
            yiletho emletlel.
        dit
        i = i + 1.
    dit
    rilniro top == 1 hutro nethe
        yiletho st[0].
    dit thumku nethe
        yiletho emletlel.
    dit
dit

ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi toks = split(line).
    ohetdi res = evalRPN(toks).
    rilniro res == emletlel hutro nethe
        miyol "error".
    dit thumku nethe
        miyol res.
    dit
    line = nilhino().
dit
</solution>

<solution task="t2-wordfreq">
rimli isDigit(c) nethe
    yiletho c >= "0" lotvethu c <= "9".
dit

rimli isLetter(c) nethe
    yiletho (c >= "a" lotvethu c <= "z") nime (c >= "A" lotvethu c <= "Z").
dit

rimli lowerChar(c) nethe
    ohetdi up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    ohetdi lo = "abcdefghijklmnopqrstuvwxyz".
    rilniro c >= "A" lotvethu c <= "Z" hutro nethe
        ohetdi i = 0.
        konit i < 26 mitho nethe
            rilniro up[i] == c hutro nethe
                yiletho lo[i].
            dit
            i = i + 1.
        dit
    dit
    yiletho c.
dit

rimli addWord(ws, fs, w) nethe
    ohetdi i = 0.
    konit i < yuyem(ws) mitho nethe
        rilniro ws[i] == w hutro nethe
            fs[i] = fs[i] + 1.
            yiletho emletlel.
        dit
        i = i + 1.
    dit
    nimhol(ws, w).
    nimhol(fs, 1).
    yiletho emletlel.
dit

ohetdi words = [].
ohetdi freqs = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi cur = "".
    ohetdi i = 0.
    konit i < yuyem(line) mitho nethe
        ohetdi c = line[i].
        rilniro isLetter(c) hutro nethe
            cur = cur & lowerChar(c).
        dit thumku nethe
            rilniro cur <> "" hutro nethe
                addWord(words, freqs, cur).
            dit
            cur = "".
        dit
        i = i + 1.
    dit
    rilniro cur <> "" hutro nethe
        addWord(words, freqs, cur).
    dit
    line = nilhino().
dit

ohetdi n = yuyem(words).
ohetdi printed = 0.
konit printed < 10 lotvethu printed < n mitho nethe
    ohetdi best = -1.
    ohetdi i = 0.
    konit i < n mitho nethe
        rilniro freqs[i] >= 0 hutro nethe
            rilniro best == -1 hutro nethe
                best = i.
            dit thumku rilniro freqs[i] > freqs[best] hutro nethe
                best = i.
            dit thumku rilniro freqs[i] == freqs[best] lotvethu words[i] < words[best] hutro nethe
                best = i.
            dit
        dit
        i = i + 1.
    dit
    miyol words[best] & " " & freqs[best].
    freqs[best] = -1.
    printed = printed + 1.
dit
</solution>