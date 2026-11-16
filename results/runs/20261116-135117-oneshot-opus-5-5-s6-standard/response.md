<solution task="t0-count">
tumumin trim(s)
    troufu a = 0;
    troufu b = utoufa(s) - 1;
    tafashou a <= b dra s[a] <= " "
        a = a + 1;
    trushou
    tafashou b >= a dra s[b] <= " "
        b = b - 1;
    trushou
    troufu r = "";
    sutrarsu i = a sou b
        r = r + s[i];
    moun i
    drur r;
drumin tumumin

troufu line = bounfou();
sitrartu line == furfifan fisu drufirsa
    drur;
drumin
troufu n = shufa(trim(line));
sutrarsu i = 1 sou n
    binmi i;
moun i
</solution>

<solution task="t0-day-names">
tumumin trim(s)
    troufu a = 0;
    troufu b = utoufa(s) - 1;
    tafashou a <= b dra s[a] <= " "
        a = a + 1;
    trushou
    tafashou b >= a dra s[b] <= " "
        b = b - 1;
    trushou
    troufu r = "";
    sutrarsu i = a sou b
        r = r + s[i];
    moun i
    drur r;
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu t = trim(line);
    sitrartu utoufa(t) > 0 fisu drufirsa
        troufu n = shufa(t);
        utir (n) {
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
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t0-even-odd">
tumumin trim(s)
    troufu a = 0;
    troufu b = utoufa(s) - 1;
    tafashou a <= b dra s[a] <= " "
        a = a + 1;
    trushou
    tafashou b >= a dra s[b] <= " "
        b = b - 1;
    trushou
    troufu r = "";
    sutrarsu i = a sou b
        r = r + s[i];
    moun i
    drur r;
drumin tumumin

troufu ev = 0;
troufu od = 0;
troufu line = bounfou();
tafashou line ~= furfifan
    troufu t = trim(line);
    sitrartu utoufa(t) > 0 fisu drufirsa
        troufu n = shufa(t);
        sitrartu n % 2 == 0 fisu drufirsa
            ev = ev + 1;
        drumin tru drufirsa
            od = od + 1;
        drumin
    drumin
    line = bounfou();
trushou
binmi "even " + ev;
binmi "odd " + od;
</solution>

<solution task="t0-factorial">
tumumin trim(s)
    troufu a = 0;
    troufu b = utoufa(s) - 1;
    tafashou a <= b dra s[a] <= " "
        a = a + 1;
    trushou
    tafashou b >= a dra s[b] <= " "
        b = b - 1;
    trushou
    troufu r = "";
    sutrarsu i = a sou b
        r = r + s[i];
    moun i
    drur r;
drumin tumumin

troufu n = shufa(trim(bounfou()));
troufu f = 1;
sutrarsu i = 1 sou n
    f = f * i;
moun i
binmi f;
</solution>

<solution task="t0-fizzbuzz">
tumumin trim(s)
    troufu a = 0;
    troufu b = utoufa(s) - 1;
    tafashou a <= b dra s[a] <= " "
        a = a + 1;
    trushou
    tafashou b >= a dra s[b] <= " "
        b = b - 1;
    trushou
    troufu r = "";
    sutrarsu i = a sou b
        r = r + s[i];
    moun i
    drur r;
drumin tumumin

troufu n = shufa(trim(bounfou()));
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
</solution>

<solution task="t0-hello">
binmi "Hello, Utopia!";
</solution>

<solution task="t0-reverse-lines">
troufu xs = [];
troufu line = bounfou();
tafashou line ~= furfifan
    marboun(xs, line);
    line = bounfou();
trushou
sutrarsu i = utoufa(xs) - 1 sou 0 suntru -1
    binmi xs[i];
moun i
</solution>

<solution task="t1-digits">
tumumin trim(s)
    troufu a = 0;
    troufu b = utoufa(s) - 1;
    tafashou a <= b dra s[a] <= " "
        a = a + 1;
    trushou
    tafashou b >= a dra s[b] <= " "
        b = b - 1;
    trushou
    troufu r = "";
    sutrarsu i = a sou b
        r = r + s[i];
    moun i
    drur r;
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu t = trim(line);
    sitrartu utoufa(t) > 0 fisu drufirsa
        troufu n = shufa(t);
        troufu m = n;
        sitrartu m < 0 fisu drufirsa
            m = -m;
        drumin
        troufu sm = 0;
        troufu rev = 0;
        tafashou m > 0
            troufu d = m % 10;
            sm = sm + d;
            rev = rev * 10 + d;
            m = m / 10;
        trushou
        sitrartu n < 0 fisu drufirsa
            rev = -rev;
        drumin
        binmi sm + " " + rev;
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t1-floordiv">
tumumin split(s)
    troufu res = [];
    troufu cur = "";
    sutrarsu i = 0 sou utoufa(s) - 1
        troufu c = s[i];
        sitrartu c <= " " fisu drufirsa
            sitrartu utoufa(cur) > 0 fisu drufirsa
                marboun(res, cur);
                cur = "";
            drumin
        drumin tru drufirsa
            cur = cur + c;
        drumin
    moun i
    sitrartu utoufa(cur) > 0 fisu drufirsa
        marboun(res, cur);
    drumin
    drur res;
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu toks = split(line);
    sitrartu utoufa(toks) >= 2 fisu drufirsa
        troufu a = shufa(toks[0]);
        troufu b = shufa(toks[1]);
        troufu q = a / b;
        troufu r = a - b * q;
        sitrartu (r < 0 dra b > 0) butrouta (r > 0 dra b < 0) fisu drufirsa
            q = q - 1;
            r = r + b;
        drumin
        binmi q + " " + r;
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t1-palindromes">
tumumin lower(c)
    sitrartu c >= "A" dra c <= "Z" fisu drufirsa
        troufu up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        troufu low = "abcdefghijklmnopqrstuvwxyz";
        troufu lo = 0;
        troufu hi = 25;
        tafashou lo < hi
            troufu mid = (lo + hi) / 2;
            sitrartu up[mid] < c fisu drufirsa
                lo = mid + 1;
            drumin tru drufirsa
                hi = mid;
            drumin
        trushou
        drur low[lo];
    drumin
    drur c;
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu cs = [];
    sutrarsu i = 0 sou utoufa(line) - 1
        troufu c = line[i];
        sitrartu (c >= "a" dra c <= "z") butrouta (c >= "A" dra c <= "Z") butrouta (c >= "0" dra c <= "9") fisu drufirsa
            marboun(cs, lower(c));
        drumin
    moun i
    troufu ok = sibitrou;
    troufu p = 0;
    troufu q = utoufa(cs) - 1;
    tafashou p < q
        sitrartu cs[p] ~= cs[q] fisu drufirsa
            ok = fufir;
            basu;
        drumin
        p = p + 1;
        q = q - 1;
    trushou
    sitrartu ok fisu drufirsa
        binmi "yes";
    drumin tru drufirsa
        binmi "no";
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t1-rank">
tumumin split(s)
    troufu res = [];
    troufu cur = "";
    sutrarsu i = 0 sou utoufa(s) - 1
        troufu c = s[i];
        sitrartu c <= " " fisu drufirsa
            sitrartu utoufa(cur) > 0 fisu drufirsa
                marboun(res, cur);
                cur = "";
            drumin
        drumin tru drufirsa
            cur = cur + c;
        drumin
    moun i
    sitrartu utoufa(cur) > 0 fisu drufirsa
        marboun(res, cur);
    drumin
    drur res;
drumin tumumin

troufu first = bounfou();
sitrartu first == furfifan fisu drufirsa
    drur;
drumin
troufu toks = split(first);
troufu nums = [];
sutrarsu i = 0 sou utoufa(toks) - 1
    marboun(nums, shufa(toks[i]));
moun i
troufu n = utoufa(nums);
troufu line = bounfou();
tafashou line ~= furfifan
    troufu qt = split(line);
    sitrartu utoufa(qt) > 0 fisu drufirsa
        troufu q = shufa(qt[0]);
        troufu lo = 0;
        troufu hi = n;
        tafashou lo < hi
            troufu mid = (lo + hi) / 2;
            sitrartu nums[mid] < q fisu drufirsa
                lo = mid + 1;
            drumin tru drufirsa
                hi = mid;
            drumin
        trushou
        sitrartu lo < n dra nums[lo] == q fisu drufirsa
            binmi lo + " found";
        drumin tru drufirsa
            binmi lo + " missing";
        drumin
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t1-rotate">
tumumin trim(s)
    troufu a = 0;
    troufu b = utoufa(s) - 1;
    tafashou a <= b dra s[a] <= " "
        a = a + 1;
    trushou
    tafashou b >= a dra s[b] <= " "
        b = b - 1;
    trushou
    troufu r = "";
    sutrarsu i = a sou b
        r = r + s[i];
    moun i
    drur r;
drumin tumumin

troufu first = bounfou();
sitrartu first == furfifan fisu drufirsa
    drur;
drumin
troufu k = shufa(trim(first));
troufu items = [];
troufu line = bounfou();
tafashou line ~= furfifan
    marboun(items, line);
    line = bounfou();
trushou
troufu n = utoufa(items);
sitrartu n > 0 fisu drufirsa
    troufu s = k % n;
    sitrartu s < 0 fisu drufirsa
        s = s + n;
    drumin
    sutrarsu i = 0 sou n - 1
        binmi items[(i - s + n) % n];
    moun i
drumin
</solution>

<solution task="t1-weekday">
tumumin trim(s)
    troufu a = 0;
    troufu b = utoufa(s) - 1;
    tafashou a <= b dra s[a] <= " "
        a = a + 1;
    trushou
    tafashou b >= a dra s[b] <= " "
        b = b - 1;
    trushou
    troufu r = "";
    sutrarsu i = a sou b
        r = r + s[i];
    moun i
    drur r;
drumin tumumin

tumumin dval(c)
    troufu ds = "0123456789";
    sutrarsu i = 0 sou 9
        sitrartu ds[i] == c fisu drufirsa
            drur i;
        drumin
    moun i
    drur 0;
drumin tumumin

tumumin num(s, a, b)
    troufu v = 0;
    sutrarsu i = a sou b
        v = v * 10 + dval(s[i]);
    moun i
    drur v;
drumin tumumin

troufu names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
troufu tt = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
troufu line = bounfou();
tafashou line ~= furfifan
    troufu t = trim(line);
    sitrartu utoufa(t) >= 10 fisu drufirsa
        troufu y = num(t, 0, 3);
        troufu m = num(t, 5, 6);
        troufu d = num(t, 8, 9);
        sitrartu m < 3 fisu drufirsa
            y = y - 1;
        drumin
        troufu w = (y + y / 4 - y / 100 + y / 400 + tt[m - 1] + d) % 7;
        binmi names[w];
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t2-bignum">
tumumin split(s)
    troufu res = [];
    troufu cur = "";
    sutrarsu i = 0 sou utoufa(s) - 1
        troufu c = s[i];
        sitrartu c <= " " fisu drufirsa
            sitrartu utoufa(cur) > 0 fisu drufirsa
                marboun(res, cur);
                cur = "";
            drumin
        drumin tru drufirsa
            cur = cur + c;
        drumin
    moun i
    sitrartu utoufa(cur) > 0 fisu drufirsa
        marboun(res, cur);
    drumin
    drur res;
drumin tumumin

tumumin dval(c)
    troufu ds = "0123456789";
    sutrarsu i = 0 sou 9
        sitrartu ds[i] == c fisu drufirsa
            drur i;
        drumin
    moun i
    drur 0;
drumin tumumin

tumumin toLimbs(s)
    troufu res = [];
    troufu cur = 0;
    troufu p = 1;
    sutrarsu i = utoufa(s) - 1 sou 0 suntru -1
        cur = cur + dval(s[i]) * p;
        p = p * 10;
        sitrartu p == 10000 fisu drufirsa
            marboun(res, cur);
            cur = 0;
            p = 1;
        drumin
    moun i
    sitrartu p > 1 fisu drufirsa
        marboun(res, cur);
    drumin
    sitrartu utoufa(res) == 0 fisu drufirsa
        marboun(res, 0);
    drumin
    drur res;
drumin tumumin

tumumin add(a, b)
    troufu res = [];
    troufu carry = 0;
    troufu n = utoufa(a);
    sitrartu utoufa(b) > n fisu drufirsa
        n = utoufa(b);
    drumin
    sutrarsu i = 0 sou n - 1
        troufu s = carry;
        sitrartu i < utoufa(a) fisu drufirsa
            s = s + a[i];
        drumin
        sitrartu i < utoufa(b) fisu drufirsa
            s = s + b[i];
        drumin
        marboun(res, s % 10000);
        carry = s / 10000;
    moun i
    sitrartu carry > 0 fisu drufirsa
        marboun(res, carry);
    drumin
    drur res;
drumin tumumin

tumumin mul(a, b)
    troufu res = [];
    troufu la = utoufa(a);
    troufu lb = utoufa(b);
    sutrarsu i = 0 sou la + lb - 1
        marboun(res, 0);
    moun i
    sutrarsu i = 0 sou la - 1
        troufu carry = 0;
        troufu ai = a[i];
        sutrarsu j = 0 sou lb - 1
            troufu cur = res[i + j] + ai * b[j] + carry;
            res[i + j] = cur % 10000;
            carry = cur / 10000;
        moun j
        troufu k = i + lb;
        tafashou carry > 0
            troufu cur2 = res[k] + carry;
            res[k] = cur2 % 10000;
            carry = cur2 / 10000;
            k = k + 1;
        trushou
    moun i
    drur res;
drumin tumumin

tumumin toStr(a)
    troufu top = utoufa(a) - 1;
    tafashou top > 0 dra a[top] == 0
        top = top - 1;
    trushou
    troufu s = moufunsa(a[top]);
    sutrarsu i = top - 1 sou 0 suntru -1
        troufu v = a[i];
        sitrartu v < 1000 fisu drufirsa
            s = s + "0";
        drumin
        sitrartu v < 100 fisu drufirsa
            s = s + "0";
        drumin
        sitrartu v < 10 fisu drufirsa
            s = s + "0";
        drumin
        s = s + v;
    moun i
    drur s;
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu toks = split(line);
    sitrartu utoufa(toks) >= 2 fisu drufirsa
        troufu x = toLimbs(toks[0]);
        troufu y = toLimbs(toks[1]);
        binmi toStr(add(x, y)) + " " + toStr(mul(x, y));
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t2-life">
tumumin trim(s)
    troufu a = 0;
    troufu b = utoufa(s) - 1;
    tafashou a <= b dra s[a] <= " "
        a = a + 1;
    trushou
    tafashou b >= a dra s[b] <= " "
        b = b - 1;
    trushou
    troufu r = "";
    sutrarsu i = a sou b
        r = r + s[i];
    moun i
    drur r;
drumin tumumin

troufu g = shufa(trim(bounfou()));
troufu grid = [];
troufu line = bounfou();
tafashou line ~= furfifan
    troufu t = trim(line);
    sitrartu utoufa(t) > 0 fisu drufirsa
        troufu row = [];
        sutrarsu j = 0 sou utoufa(t) - 1
            sitrartu t[j] == "#" fisu drufirsa
                marboun(row, 1);
            drumin tru drufirsa
                marboun(row, 0);
            drumin
        moun j
        marboun(grid, row);
    drumin
    line = bounfou();
trushou
troufu h = utoufa(grid);
troufu w = 0;
sitrartu h > 0 fisu drufirsa
    w = utoufa(grid[0]);
drumin
sutrarsu gen = 1 sou g
    troufu ng = [];
    sutrarsu r = 0 sou h - 1
        troufu nrow = [];
        troufu crow = grid[r];
        sutrarsu c = 0 sou w - 1
            troufu cnt = 0;
            sutrarsu dr = -1 sou 1
                troufu rr = r + dr;
                sitrartu rr >= 0 dra rr < h fisu drufirsa
                    troufu prow = grid[rr];
                    sutrarsu dc = -1 sou 1
                        troufu cc = c + dc;
                        sitrartu cc >= 0 dra cc < w dra (dr ~= 0 butrouta dc ~= 0) fisu drufirsa
                            cnt = cnt + prow[cc];
                        drumin
                    moun dc
                drumin
            moun dr
            troufu alive = crow[c];
            sitrartu cnt == 3 butrouta (alive == 1 dra cnt == 2) fisu drufirsa
                marboun(nrow, 1);
            drumin tru drufirsa
                marboun(nrow, 0);
            drumin
        moun c
        marboun(ng, nrow);
    moun r
    grid = ng;
moun gen
sutrarsu r = 0 sou h - 1
    troufu orow = grid[r];
    troufu out = "";
    sutrarsu c = 0 sou w - 1
        sitrartu orow[c] == 1 fisu drufirsa
            out = out + "#";
        drumin tru drufirsa
            out = out + ".";
        drumin
    moun c
    binmi out;
moun r
</solution>

<solution task="t2-rpn">
tumumin split(s)
    troufu res = [];
    troufu cur = "";
    sutrarsu i = 0 sou utoufa(s) - 1
        troufu c = s[i];
        sitrartu c <= " " fisu drufirsa
            sitrartu utoufa(cur) > 0 fisu drufirsa
                marboun(res, cur);
                cur = "";
            drumin
        drumin tru drufirsa
            cur = cur + c;
        drumin
    moun i
    sitrartu utoufa(cur) > 0 fisu drufirsa
        marboun(res, cur);
    drumin
    drur res;
drumin tumumin

tumumin isNum(t)
    troufu start = 0;
    sitrartu t[0] == "-" fisu drufirsa
        start = 1;
    drumin
    sitrartu start >= utoufa(t) fisu drufirsa
        drur fufir;
    drumin
    sutrarsu i = start sou utoufa(t) - 1
        sitrartu t[i] < "0" butrouta t[i] > "9" fisu drufirsa
            drur fufir;
        drumin
    moun i
    drur sibitrou;
drumin tumumin

tumumin evalLine(line)
    troufu toks = split(line);
    sitrartu utoufa(toks) == 0 fisu drufirsa
        drur "error";
    drumin
    troufu st = [];
    troufu sp = 0;
    sutrarsu i = 0 sou utoufa(toks) - 1
        troufu t = toks[i];
        sitrartu isNum(t) fisu drufirsa
            troufu v = shufa(t);
            sitrartu sp < utoufa(st) fisu drufirsa
                st[sp] = v;
            drumin tru drufirsa
                marboun(st, v);
            drumin
            sp = sp + 1;
        drumin tru sitrartu t == "+" butrouta t == "-" butrouta t == "*" butrouta t == "/" butrouta t == "%" fisu drufirsa
            sitrartu sp < 2 fisu drufirsa
                drur "error";
            drumin
            troufu b = st[sp - 1];
            troufu a = st[sp - 2];
            sp = sp - 2;
            troufu r = 0;
            utir (t) {
            sourmar "+":
                r = a + b;
            sourmar "-":
                r = a - b;
            sourmar "*":
                r = a * b;
            sourmar "/":
                sitrartu b == 0 fisu drufirsa
                    drur "error";
                drumin
                r = a / b;
            sourmar "%":
                sitrartu b == 0 fisu drufirsa
                    drur "error";
                drumin
                r = a % b;
            }
            st[sp] = r;
            sp = sp + 1;
        drumin tru drufirsa
            drur "error";
        drumin
    moun i
    sitrartu sp ~= 1 fisu drufirsa
        drur "error";
    drumin
    drur moufunsa(st[0]);
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    binmi evalLine(line);
    line = bounfou();
trushou
</solution>

<solution task="t2-wordfreq">
tumumin lower(c)
    sitrartu c >= "A" dra c <= "Z" fisu drufirsa
        troufu up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        troufu low = "abcdefghijklmnopqrstuvwxyz";
        troufu lo = 0;
        troufu hi = 25;
        tafashou lo < hi
            troufu mid = (lo + hi) / 2;
            sitrartu up[mid] < c fisu drufirsa
                lo = mid + 1;
            drumin tru drufirsa
                hi = mid;
            drumin
        trushou
        drur low[lo];
    drumin
    drur c;
drumin tumumin

tumumin msort(xs, lo, hi)
    sitrartu hi - lo <= 1 fisu drufirsa
        troufu r = [];
        sitrartu hi - lo == 1 fisu drufirsa
            marboun(r, xs[lo]);
        drumin
        drur r;
    drumin
    troufu mid = (lo + hi) / 2;
    troufu a = msort(xs, lo, mid);
    troufu b = msort(xs, mid, hi);
    troufu res = [];
    troufu i = 0;
    troufu j = 0;
    troufu na = utoufa(a);
    troufu nb = utoufa(b);
    tafashou i < na dra j < nb
        sitrartu a[i] <= b[j] fisu drufirsa
            marboun(res, a[i]);
            i = i + 1;
        drumin tru drufirsa
            marboun(res, b[j]);
            j = j + 1;
        drumin
    trushou
    tafashou i < na
        marboun(res, a[i]);
        i = i + 1;
    trushou
    tafashou j < nb
        marboun(res, b[j]);
        j = j + 1;
    trushou
    drur res;
drumin tumumin

troufu words = [];
troufu line = bounfou();
tafashou line ~= furfifan
    troufu cur = "";
    sutrarsu i = 0 sou utoufa(line) - 1
        troufu c = line[i];
        sitrartu (c >= "a" dra c <= "z") butrouta (c >= "A" dra c <= "Z") fisu drufirsa
            cur = cur + lower(c);
        drumin tru drufirsa
            sitrartu utoufa(cur) > 0 fisu drufirsa
                marboun(words, cur);
                cur = "";
            drumin
        drumin
    moun i
    sitrartu utoufa(cur) > 0 fisu drufirsa
        marboun(words, cur);
    drumin
    line = bounfou();
trushou
troufu sorted = msort(words, 0, utoufa(words));
troufu uw = [];
troufu uc = [];
sutrarsu i = 0 sou utoufa(sorted) - 1
    troufu wd = sorted[i];
    troufu nu = utoufa(uw);
    sitrartu nu > 0 dra uw[nu - 1] == wd fisu drufirsa
        uc[nu - 1] = uc[nu - 1] + 1;
    drumin tru drufirsa
        marboun(uw, wd);
        marboun(uc, 1);
    drumin
moun i
sutrarsu k = 1 sou 10
    troufu best = -1;
    sutrarsu i = 0 sou utoufa(uw) - 1
        sitrartu uc[i] > 0 dra (best == -1 butrouta uc[i] > uc[best]) fisu drufirsa
            best = i;
        drumin
    moun i
    sitrartu best == -1 fisu drufirsa
        basu;
    drumin
    binmi uw[best] + " " + uc[best];
    uc[best] = 0;
moun k
</solution>