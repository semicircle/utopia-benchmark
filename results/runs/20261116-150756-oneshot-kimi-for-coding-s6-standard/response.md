<solution task="t0-count">
```
troufu n = shufa(bounfou());
sutrarsu i = 1 sou n
    binmi i;
moun i
```
</solution>

<solution task="t0-day-names">
```
troufu line = bounfou();
tafashou line ~= furfifan
    troufu d = shufa(line);
    utir (d) {
    sourmar 1:
        binmi "Monday";
    sourmar 2:
        binmi "Tuesday";
    sourmar 3:
        binmi "Wednesday";
    sourmar 4:
        binmi "Thursday";
    sourmar 5:
        binmi "Friday";
    sourmar 6:
        binmi "Saturday";
    sourmar 7:
        binmi "Sunday";
    fitru:
        binmi "invalid";
    }
    line = bounfou();
trushou
```
</solution>

<solution task="t0-even-odd">
```
troufu ev = 0;
troufu od = 0;
troufu line = bounfou();
tafashou line ~= furfifan
    troufu n = shufa(line);
    sitrartu n % 2 == 0 fisu drufirsa
        ev = ev + 1;
    drumin tru drufirsa
        od = od + 1;
    drumin
    line = bounfou();
trushou
binmi "even " + ev;
binmi "odd " + od;
```
</solution>

<solution task="t0-factorial">
```
troufu n = shufa(bounfou());
troufu r = 1;
sutrarsu i = 1 sou n
    r = r * i;
moun i
binmi r;
```
</solution>

<solution task="t0-fizzbuzz">
```
troufu n = shufa(bounfou());
sutrarsu i = 1 sou n
    sitrartu i % 15 == 0 fisu drufirsa
        binmi "FizzBuzz";
    drumin tru sitrartu i % 3 == 0 fisu drufirsa
        binmi "Fizz";
    drumin tru sitrartu i % 5 == 0 fisu drufirsa
        binmi "Buzz";
    drumin tru drufirsa
        binmi i;
    drumin
moun i
```
</solution>

<solution task="t0-hello">
```
binmi "Hello, Utopia!";
```
</solution>

<solution task="t0-reverse-lines">
```
troufu lines = [];
troufu line = bounfou();
tafashou line ~= furfifan
    marboun(lines, line);
    line = bounfou();
trushou
troufu i = utoufa(lines) - 1;
tafashou i >= 0
    binmi lines[i];
    i = i - 1;
trushou
```
</solution>

<solution task="t1-digits">
```
troufu line = bounfou();
tafashou line ~= furfifan
    troufu n = shufa(line);
    troufu sign = 1;
    sitrartu n < 0 fisu drufirsa
        sign = -1;
        n = -n;
    drumin
    troufu sum = 0;
    troufu rev = 0;
    sitrartu n == 0 fisu drufirsa
        sum = 0;
        rev = 0;
    drumin
    tafashou n > 0
        troufu d = n % 10;
        sum = sum + d;
        rev = rev * 10 + d;
        n = n / 10;
    trushou
    sitrartu sign == -1 dra rev ~= 0 fisu drufirsa
        rev = -rev;
    drumin
    binmi sum + " " + rev;
    line = bounfou();
trushou
```
</solution>

<solution task="t1-floordiv">
```
tumumin splittok(s)
    troufu parts = [];
    troufu cur = "";
    troufu i = 0;
    tafashou i < utoufa(s)
        troufu c = s[i];
        sitrartu c == " " fisu drufirsa
            sitrartu cur ~= "" fisu drufirsa
                marboun(parts, cur);
            drumin
            cur = "";
        drumin tru drufirsa
            cur = cur + c;
        drumin
        i = i + 1;
    trushou
    sitrartu cur ~= "" fisu drufirsa
        marboun(parts, cur);
    drumin
    drur parts;
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu parts = splittok(line);
    troufu a = shufa(parts[0]);
    troufu b = shufa(parts[1]);
    troufu q = a / b;
    sitrartu a % b ~= 0 dra ((a < 0) ~= (b < 0)) fisu drufirsa
        q = q - 1;
    drumin
    troufu r = a - b * q;
    binmi q + " " + r;
    line = bounfou();
trushou
```
</solution>

<solution task="t1-palindromes">
```
tumumin lower(c)
    troufu ups = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    troufu los = "abcdefghijklmnopqrstuvwxyz";
    troufu i = 0;
    troufu r = c;
    tafashou i < 26
        sitrartu c == ups[i] fisu drufirsa
            r = los[i];
        drumin
        i = i + 1;
    trushou
    drur r;
drumin tumumin

tumumin isalnum(c)
    drur (c >= "a" dra c <= "z") butrouta (c >= "A" dra c <= "Z") butrouta (c >= "0" dra c <= "9");
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu norm = [];
    troufu i = 0;
    tafashou i < utoufa(line)
        troufu c = line[i];
        sitrartu isalnum(c) fisu drufirsa
            marboun(norm, lower(c));
        drumin
        i = i + 1;
    trushou
    troufu L = utoufa(norm);
    troufu ok = sibitrou;
    troufu j = 0;
    tafashou j <= L / 2 dra ok
        sitrartu norm[j] ~= norm[L - 1 - j] fisu drufirsa
            ok = fufir;
        drumin
        j = j + 1;
    trushou
    sitrartu ok fisu drufirsa
        binmi "yes";
    drumin tru drufirsa
        binmi "no";
    drumin
    line = bounfou();
trushou
```
</solution>

<solution task="t1-rank">
```
tumumin splittok(s)
    troufu parts = [];
    troufu cur = "";
    troufu i = 0;
    tafashou i < utoufa(s)
        troufu c = s[i];
        sitrartu c == " " fisu drufirsa
            sitrartu cur ~= "" fisu drufirsa
                marboun(parts, cur);
            drumin
            cur = "";
        drumin tru drufirsa
            cur = cur + c;
        drumin
        i = i + 1;
    trushou
    sitrartu cur ~= "" fisu drufirsa
        marboun(parts, cur);
    drumin
    drur parts;
drumin tumumin

troufu first = bounfou();
troufu xs = [];
sitrartu first ~= furfifan fisu drufirsa
    troufu toks = splittok(first);
    troufu ti = 0;
    tafashou ti < utoufa(toks)
        marboun(xs, shufa(toks[ti]));
        ti = ti + 1;
    trushou
drumin
troufu line = bounfou();
tafashou line ~= furfifan
    troufu q = shufa(line);
    troufu smaller = 0;
    troufu found = fufir;
    troufu i = 0;
    tafashou i < utoufa(xs)
        sitrartu xs[i] < q fisu drufirsa
            smaller = smaller + 1;
        drumin
        sitrartu xs[i] == q fisu drufirsa
            found = sibitrou;
        drumin
        i = i + 1;
    trushou
    sitrartu found fisu drufirsa
        binmi smaller + " found";
    drumin tru drufirsa
        binmi smaller + " missing";
    drumin
    line = bounfou();
trushou
```
</solution>

<solution task="t1-rotate">
```
troufu k = shufa(bounfou());
troufu items = [];
troufu line = bounfou();
tafashou line ~= furfifan
    marboun(items, line);
    line = bounfou();
trushou
troufu m = utoufa(items);
sitrartu m > 0 fisu drufirsa
    troufu r = k % m;
    sitrartu r < 0 fisu drufirsa
        r = r + m;
    drumin
    sutrarsu p = 0 sou m - 1
        binmi items[(p + m - r) % m];
    moun p
drumin
```
</solution>

<solution task="t1-weekday">
```
tumumin substr(s, a, b)
    troufu r = "";
    troufu i = a;
    tafashou i <= b
        r = r + s[i];
        i = i + 1;
    trushou
    drur r;
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu y = shufa(substr(line, 0, 3));
    troufu m = shufa(substr(line, 5, 6));
    troufu d = shufa(substr(line, 8, 9));
    sitrartu m < 3 fisu drufirsa
        y = y - 1;
    drumin
    troufu t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
    troufu w = (y + y / 4 - y / 100 + y / 400 + t[m - 1] + d) % 7;
    utir (w) {
    sourmar 0:
        binmi "Sunday";
    sourmar 1:
        binmi "Monday";
    sourmar 2:
        binmi "Tuesday";
    sourmar 3:
        binmi "Wednesday";
    sourmar 4:
        binmi "Thursday";
    sourmar 5:
        binmi "Friday";
    sourmar 6:
        binmi "Saturday";
    }
    line = bounfou();
trushou
```
</solution>

<solution task="t2-bignum">
```
tumumin splittok(s)
    troufu parts = [];
    troufu cur = "";
    troufu i = 0;
    tafashou i < utoufa(s)
        troufu c = s[i];
        sitrartu c == " " fisu drufirsa
            sitrartu cur ~= "" fisu drufirsa
                marboun(parts, cur);
            drumin
            cur = "";
        drumin tru drufirsa
            cur = cur + c;
        drumin
        i = i + 1;
    trushou
    sitrartu cur ~= "" fisu drufirsa
        marboun(parts, cur);
    drumin
    drur parts;
drumin tumumin

tumumin parsebig(s)
    troufu ds = [];
    troufu i = utoufa(s) - 1;
    tafashou i >= 0
        marboun(ds, shufa(s[i]));
        i = i - 1;
    trushou
    drur ds;
drumin tumumin

tumumin addbig(a, b)
    troufu r = [];
    troufu carry = 0;
    troufu i = 0;
    tafashou i < utoufa(a) butrouta i < utoufa(b) butrouta carry ~= 0
        troufu s = carry;
        sitrartu i < utoufa(a) fisu drufirsa
            s = s + a[i];
        drumin
        sitrartu i < utoufa(b) fisu drufirsa
            s = s + b[i];
        drumin
        marboun(r, s % 10);
        carry = s / 10;
        i = i + 1;
    trushou
    drur r;
drumin tumumin

tumumin mulbig(a, b)
    troufu r = [];
    troufu total = utoufa(a) + utoufa(b);
    sutrarsu i = 0 sou total - 1
        marboun(r, 0);
    moun i
    troufu i = 0;
    tafashou i < utoufa(a)
        troufu carry = 0;
        troufu j = 0;
        tafashou j < utoufa(b)
            troufu cur = r[i + j] + a[i] * b[j] + carry;
            r[i + j] = cur % 10;
            carry = cur / 10;
            j = j + 1;
        trushou
        troufu p = i + utoufa(b);
        tafashou carry > 0
            troufu cur = r[p] + carry;
            r[p] = cur % 10;
            carry = cur / 10;
            p = p + 1;
        trushou
        i = i + 1;
    trushou
    drur r;
drumin tumumin

tumumin bigtos(ds)
    troufu hi = utoufa(ds) - 1;
    tafashou hi > 0 dra ds[hi] == 0
        hi = hi - 1;
    trushou
    troufu s = "";
    tafashou hi >= 0
        s = s + moufunsa(ds[hi]);
        hi = hi - 1;
    trushou
    drur s;
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu parts = splittok(line);
    troufu a = parsebig(parts[0]);
    troufu b = parsebig(parts[1]);
    binmi bigtos(addbig(a, b)) + " " + bigtos(mulbig(a, b));
    line = bounfou();
trushou
```
</solution>

<solution task="t2-life">
```
troufu g = shufa(bounfou());
troufu rows = [];
troufu line = bounfou();
tafashou line ~= furfifan
    marboun(rows, line);
    line = bounfou();
trushou
troufu R = utoufa(rows);
troufu C = utoufa(rows[0]);

sutrarsu gen = 0 sou g - 1
    troufu nrows = [];
    sutrarsu r = 0 sou R - 1
        troufu nrow = "";
        sutrarsu c = 0 sou C - 1
            troufu cnt = 0;
            sutrarsu dr = -1 sou 1
                sutrarsu dc = -1 sou 1
                    sitrartu shutoun (dr == 0 dra dc == 0) fisu drufirsa
                        troufu rr = r + dr;
                        troufu cc = c + dc;
                        sitrartu rr >= 0 dra rr < R dra cc >= 0 dra cc < C fisu drufirsa
                            sitrartu rows[rr][cc] == "#" fisu drufirsa
                                cnt = cnt + 1;
                            drumin
                        drumin
                    drumin
                moun dc
            moun dr
            troufu alive = rows[r][c] == "#";
            troufu na = fufir;
            sitrartu alive fisu drufirsa
                sitrartu cnt == 2 butrouta cnt == 3 fisu drufirsa
                    na = sibitrou;
                drumin
            drumin tru drufirsa
                sitrartu cnt == 3 fisu drufirsa
                    na = sibitrou;
                drumin
            drumin
            sitrartu na fisu drufirsa
                nrow = nrow + "#";
            drumin tru drufirsa
                nrow = nrow + ".";
            drumin
        moun c
        marboun(nrows, nrow);
    moun r
    rows = nrows;
moun gen

sutrarsu r = 0 sou R - 1
    binmi rows[r];
moun r
```
</solution>

<solution task="t2-rpn">
```
tumumin splittok(s)
    troufu parts = [];
    troufu cur = "";
    troufu i = 0;
    tafashou i < utoufa(s)
        troufu c = s[i];
        sitrartu c == " " fisu drufirsa
            sitrartu cur ~= "" fisu drufirsa
                marboun(parts, cur);
            drumin
            cur = "";
        drumin tru drufirsa
            cur = cur + c;
        drumin
        i = i + 1;
    trushou
    sitrartu cur ~= "" fisu drufirsa
        marboun(parts, cur);
    drumin
    drur parts;
drumin tumumin

tumumin isint(s)
    troufu n = utoufa(s);
    sitrartu n == 0 fisu drufirsa
        drur fufir;
    drumin
    troufu i = 0;
    sitrartu s[0] == "-" fisu drufirsa
        sitrartu n == 1 fisu drufirsa
            drur fufir;
        drumin
        i = 1;
    drumin
    tafashou i < n
        troufu c = s[i];
        sitrartu shutoun (c >= "0" dra c <= "9") fisu drufirsa
            drur fufir;
        drumin
        i = i + 1;
    trushou
    drur sibitrou;
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu toks = splittok(line);
    troufu st = [];
    troufu sn = 0;
    troufu err = fufir;
    troufu ti = 0;
    tafashou ti < utoufa(toks) dra shutoun err
        troufu tok = toks[ti];
        sitrartu isint(tok) fisu drufirsa
            sitrartu sn < utoufa(st) fisu drufirsa
                st[sn] = shufa(tok);
            drumin tru drufirsa
                marboun(st, shufa(tok));
            drumin
            sn = sn + 1;
        drumin tru sitrartu (tok == "+") butrouta (tok == "-") butrouta (tok == "*") butrouta (tok == "/") butrouta (tok == "%") fisu drufirsa
            sitrartu sn < 2 fisu drufirsa
                err = sibitrou;
            drumin tru drufirsa
                troufu b = st[sn - 1];
                troufu a = st[sn - 2];
                sn = sn - 2;
                troufu r = 0;
                sitrartu tok == "+" fisu drufirsa
                    r = a + b;
                drumin tru sitrartu tok == "-" fisu drufirsa
                    r = a - b;
                drumin tru sitrartu tok == "*" fisu drufirsa
                    r = a * b;
                drumin tru sitrartu tok == "/" fisu drufirsa
                    sitrartu b == 0 fisu drufirsa
                        err = sibitrou;
                    drumin tru drufirsa
                        r = a / b;
                    drumin
                drumin tru drufirsa
                    sitrartu b == 0 fisu drufirsa
                        err = sibitrou;
                    drumin tru drufirsa
                        r = a % b;
                    drumin
                drumin
                sitrartu shutoun err fisu drufirsa
                    sitrartu sn < utoufa(st) fisu drufirsa
                        st[sn] = r;
                    drumin tru drufirsa
                        marboun(st, r);
                    drumin
                    sn = sn + 1;
                drumin
            drumin
        drumin tru drufirsa
            err = sibitrou;
        drumin
        ti = ti + 1;
    trushou
    sitrartu err butrouta sn ~= 1 fisu drufirsa
        binmi "error";
    drumin tru drufirsa
        binmi st[0];
    drumin
    line = bounfou();
trushou
```
</solution>

<solution task="t2-wordfreq">
```
tumumin lower(c)
    troufu ups = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    troufu los = "abcdefghijklmnopqrstuvwxyz";
    troufu i = 0;
    troufu r = c;
    tafashou i < 26
        sitrartu c == ups[i] fisu drufirsa
            r = los[i];
        drumin
        i = i + 1;
    trushou
    drur r;
drumin tumumin

tumumin isaz(c)
    drur (c >= "a" dra c <= "z") butrouta (c >= "A" dra c <= "Z");
drumin tumumin

tumumin addword(words, counts, w)
    troufu j = 0;
    troufu found = fufir;
    tafashou j < utoufa(words) dra shutoun found
        sitrartu words[j] == w fisu drufirsa
            found = sibitrou;
        drumin
        j = j + 1;
    trushou
    sitrartu found fisu drufirsa
        counts[j - 1] = counts[j - 1] + 1;
    drumin tru drufirsa
        marboun(words, w);
        marboun(counts, 1);
    drumin
drumin tumumin

troufu words = [];
troufu counts = [];
troufu line = bounfou();
tafashou line ~= furfifan
    troufu cur = "";
    troufu i = 0;
    troufu n = utoufa(line);
    tafashou i < n
        troufu c = line[i];
        sitrartu isaz(c) fisu drufirsa
            cur = cur + lower(c);
        drumin tru sitrartu cur ~= "" fisu drufirsa
            addword(words, counts, cur);
            cur = "";
        drumin
        i = i + 1;
    trushou
    sitrartu cur ~= "" fisu drufirsa
        addword(words, counts, cur);
    drumin
    line = bounfou();
trushou

troufu m = utoufa(words);
troufu idx = [];
sutrarsu i = 0 sou m - 1
    marboun(idx, i);
moun i
sutrarsu i = 0 sou m - 2
    troufu bi = i;
    sutrarsu j = i + 1 sou m - 1
        troufu a = idx[bi];
        troufu b = idx[j];
        sitrartu (counts[b] > counts[a]) butrouta (counts[b] == counts[a] dra words[b] < words[a]) fisu drufirsa
            bi = j;
        drumin
    moun j
    troufu tmp = idx[i];
    idx[i] = idx[bi];
    idx[bi] = tmp;
moun i

troufu lim = m;
sitrartu lim > 10 fisu drufirsa
    lim = 10;
drumin
sutrarsu i = 0 sou lim - 1
    binmi words[idx[i]] + " " + counts[idx[i]];
moun i
```
</solution>