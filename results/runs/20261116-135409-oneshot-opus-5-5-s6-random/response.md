<solution task="t0-count">
troufu n = shufa(bounfou());
sutrarsu i = 1 sou n
    binmi i;
moun i
</solution>

<solution task="t0-day-names">
troufu names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
troufu line = bounfou();
tafashou line ~= furfifan
    sitrartu utoufa(line) > 0 fisu drufirsa
        troufu n = shufa(line);
        sitrartu (n >= 1) dra (n <= 7) fisu drufirsa
            binmi names[n];
        drumin tru drufirsa
            binmi "invalid";
        drumin
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t0-even-odd">
troufu ev = 0;
troufu od = 0;
troufu line = bounfou();
tafashou line ~= furfifan
    sitrartu utoufa(line) > 0 fisu drufirsa
        troufu n = shufa(line);
        sitrartu (n % 2) == 0 fisu drufirsa
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
troufu n = shufa(bounfou());
troufu f = 1;
sutrarsu i = 2 sou n
    f = f * i;
moun i
binmi f;
</solution>

<solution task="t0-fizzbuzz">
troufu n = shufa(bounfou());
sutrarsu i = 1 sou n
    sitrartu (i % 15) == 0 fisu drufirsa
        binmi "FizzBuzz";
    drumin tru sitrartu (i % 3) == 0 fisu drufirsa
        binmi "Fizz";
    drumin tru sitrartu (i % 5) == 0 fisu drufirsa
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
sutrarsu i = utoufa(xs) sou 1 suntru -1
    binmi xs[i];
moun i
</solution>

<solution task="t1-digits">
troufu line = bounfou();
tafashou line ~= furfifan
    sitrartu utoufa(line) > 0 fisu drufirsa
        troufu n = shufa(line);
        troufu neg = n < 0;
        troufu m = n;
        sitrartu neg fisu drufirsa
            m = -n;
        drumin
        troufu total = 0;
        troufu rev = 0;
        tafashou m > 0
            troufu d = m % 10;
            total = total + d;
            rev = (rev * 10) + d;
            m = m / 10;
        trushou
        sitrartu neg fisu drufirsa
            rev = -rev;
        drumin
        binmi (moufunsa(total) + " ") + moufunsa(rev);
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t1-floordiv">
tumumin split(s)
    troufu res = [];
    troufu cur = "";
    sutrarsu i = 1 sou utoufa(s)
        troufu c = s[i];
        sitrartu (c == " ") butrouta (c == "\t") fisu drufirsa
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
        troufu a = shufa(toks[1]);
        troufu b = shufa(toks[2]);
        troufu q = a / b;
        troufu r = a - (b * q);
        sitrartu (r ~= 0) dra ((r < 0) ~= (b < 0)) fisu drufirsa
            q = q - 1;
            r = r + b;
        drumin
        binmi (moufunsa(q) + " ") + moufunsa(r);
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t1-palindromes">
tumumin isal(c)
    sitrartu (c >= "a") dra (c <= "z") fisu drufirsa
        drur sibitrou;
    drumin
    sitrartu (c >= "A") dra (c <= "Z") fisu drufirsa
        drur sibitrou;
    drumin
    sitrartu (c >= "0") dra (c <= "9") fisu drufirsa
        drur sibitrou;
    drumin
    drur fufir;
drumin tumumin

tumumin lowerc(c)
    sitrartu shutoun ((c >= "A") dra (c <= "Z")) fisu drufirsa
        drur c;
    drumin
    troufu up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    troufu lo = "abcdefghijklmnopqrstuvwxyz";
    sutrarsu k = 1 sou 26
        sitrartu up[k] == c fisu drufirsa
            drur lo[k];
        drumin
    moun k
    drur c;
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu t = [];
    sutrarsu i = 1 sou utoufa(line)
        troufu c = line[i];
        sitrartu isal(c) fisu drufirsa
            marboun(t, lowerc(c));
        drumin
    moun i
    troufu n = utoufa(t);
    troufu ok = sibitrou;
    sutrarsu i = 1 sou (n / 2)
        sitrartu t[i] ~= t[(n + 1) - i] fisu drufirsa
            ok = fufir;
        drumin
    moun i
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
    sutrarsu i = 1 sou utoufa(s)
        troufu c = s[i];
        sitrartu (c == " ") butrouta (c == "\t") fisu drufirsa
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
troufu nums = [];
sitrartu first ~= furfifan fisu drufirsa
    troufu toks = split(first);
    sutrarsu i = 1 sou utoufa(toks)
        marboun(nums, shufa(toks[i]));
    moun i
drumin
troufu n = utoufa(nums);
troufu line = bounfou();
tafashou line ~= furfifan
    troufu qt = split(line);
    sitrartu utoufa(qt) > 0 fisu drufirsa
        troufu q = shufa(qt[1]);
        troufu lo = 1;
        troufu hi = n + 1;
        tafashou lo < hi
            troufu mid = (lo + hi) / 2;
            sitrartu nums[mid] < q fisu drufirsa
                lo = mid + 1;
            drumin tru drufirsa
                hi = mid;
            drumin
        trushou
        troufu res = "missing";
        sitrartu (lo <= n) dra (nums[lo] == q) fisu drufirsa
            res = "found";
        drumin
        binmi (moufunsa(lo - 1) + " ") + res;
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t1-rotate">
troufu k = shufa(bounfou());
troufu xs = [];
troufu line = bounfou();
tafashou line ~= furfifan
    marboun(xs, line);
    line = bounfou();
trushou
troufu n = utoufa(xs);
sitrartu n > 0 fisu drufirsa
    troufu s = k % n;
    sitrartu s < 0 fisu drufirsa
        s = s + n;
    drumin
    sutrarsu i = ((n - s) + 1) sou n
        binmi xs[i];
    moun i
    sutrarsu i = 1 sou (n - s)
        binmi xs[i];
    moun i
drumin
</solution>

<solution task="t1-weekday">
tumumin num(s, a, b)
    troufu v = 0;
    sutrarsu i = a sou b
        v = (v * 10) + shufa(s[i]);
    moun i
    drur v;
drumin tumumin

troufu tt = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
troufu names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
troufu line = bounfou();
tafashou line ~= furfifan
    sitrartu utoufa(line) >= 10 fisu drufirsa
        troufu y = num(line, 1, 4);
        troufu m = num(line, 6, 7);
        troufu d = num(line, 9, 10);
        sitrartu m < 3 fisu drufirsa
            y = y - 1;
        drumin
        troufu v = y;
        v = v + (y / 4);
        v = v - (y / 100);
        v = v + (y / 400);
        v = v + tt[m];
        v = v + d;
        v = v % 7;
        binmi names[v + 1];
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t2-bignum">
tumumin split(s)
    troufu res = [];
    troufu cur = "";
    sutrarsu i = 1 sou utoufa(s)
        troufu c = s[i];
        sitrartu (c == " ") butrouta (c == "\t") fisu drufirsa
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

tumumin parse(s)
    troufu res = [];
    troufu e = utoufa(s);
    tafashou e >= 1
        troufu st = e - 3;
        sitrartu st < 1 fisu drufirsa
            st = 1;
        drumin
        troufu v = 0;
        sutrarsu k = st sou e
            v = (v * 10) + shufa(s[k]);
        moun k
        marboun(res, v);
        e = st - 1;
    trushou
    sitrartu utoufa(res) == 0 fisu drufirsa
        marboun(res, 0);
    drumin
    drur res;
drumin tumumin

tumumin fmt(xs)
    troufu n = utoufa(xs);
    tafashou (n > 1) dra (xs[n] == 0)
        n = n - 1;
    trushou
    troufu out = moufunsa(xs[n]);
    sutrarsu i = (n - 1) sou 1 suntru -1
        troufu p = moufunsa(xs[i]);
        tafashou utoufa(p) < 4
            p = "0" + p;
        trushou
        out = out + p;
    moun i
    drur out;
drumin tumumin

tumumin add(a, b)
    troufu res = [];
    troufu carry = 0;
    troufu na = utoufa(a);
    troufu nb = utoufa(b);
    troufu n = na;
    sitrartu nb > n fisu drufirsa
        n = nb;
    drumin
    sutrarsu i = 1 sou n
        troufu v = carry;
        sitrartu i <= na fisu drufirsa
            v = v + a[i];
        drumin
        sitrartu i <= nb fisu drufirsa
            v = v + b[i];
        drumin
        marboun(res, v % 10000);
        carry = v / 10000;
    moun i
    sitrartu carry > 0 fisu drufirsa
        marboun(res, carry);
    drumin
    drur res;
drumin tumumin

tumumin mul(a, b)
    troufu na = utoufa(a);
    troufu nb = utoufa(b);
    troufu res = [];
    sutrarsu i = 1 sou (na + nb)
        marboun(res, 0);
    moun i
    sutrarsu i = 1 sou na
        troufu carry = 0;
        troufu ai = a[i];
        sutrarsu j = 1 sou nb
            troufu idx = (i + j) - 1;
            troufu v = (res[idx] + (ai * b[j])) + carry;
            res[idx] = v % 10000;
            carry = v / 10000;
        moun j
        troufu k = i + nb;
        tafashou carry > 0
            troufu v2 = res[k] + carry;
            res[k] = v2 % 10000;
            carry = v2 / 10000;
            k = k + 1;
        trushou
    moun i
    drur res;
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu toks = split(line);
    sitrartu utoufa(toks) >= 2 fisu drufirsa
        troufu x = parse(toks[1]);
        troufu y = parse(toks[2]);
        troufu sm = fmt(add(x, y));
        troufu pr = fmt(mul(x, y));
        binmi (sm + " ") + pr;
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t2-life">
troufu g = shufa(bounfou());
troufu grid = [];
troufu line = bounfou();
tafashou line ~= furfifan
    sitrartu utoufa(line) > 0 fisu drufirsa
        troufu row = [];
        sutrarsu j = 1 sou utoufa(line)
            sitrartu line[j] == "#" fisu drufirsa
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
    w = utoufa(grid[1]);
drumin
sutrarsu gen = 1 sou g
    troufu ng = [];
    sutrarsu i = 1 sou h
        troufu nrow = [];
        sutrarsu j = 1 sou w
            troufu cnt = 0;
            sutrarsu di = -1 sou 1
                troufu ni = i + di;
                sitrartu (ni >= 1) dra (ni <= h) fisu drufirsa
                    troufu r = grid[ni];
                    sutrarsu dj = -1 sou 1
                        troufu nj = j + dj;
                        sitrartu (nj >= 1) dra (nj <= w) fisu drufirsa
                            sitrartu (di ~= 0) butrouta (dj ~= 0) fisu drufirsa
                                cnt = cnt + r[nj];
                            drumin
                        drumin
                    moun dj
                drumin
            moun di
            troufu cur = grid[i];
            troufu alive = cur[j];
            sitrartu (cnt == 3) butrouta ((alive == 1) dra (cnt == 2)) fisu drufirsa
                marboun(nrow, 1);
            drumin tru drufirsa
                marboun(nrow, 0);
            drumin
        moun j
        marboun(ng, nrow);
    moun i
    grid = ng;
moun gen
sutrarsu i = 1 sou h
    troufu rr = grid[i];
    troufu out = "";
    sutrarsu j = 1 sou w
        sitrartu rr[j] == 1 fisu drufirsa
            out = out + "#";
        drumin tru drufirsa
            out = out + ".";
        drumin
    moun j
    binmi out;
moun i
</solution>

<solution task="t2-rpn">
tumumin split(s)
    troufu res = [];
    troufu cur = "";
    sutrarsu i = 1 sou utoufa(s)
        troufu c = s[i];
        sitrartu (c == " ") butrouta (c == "\t") fisu drufirsa
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

tumumin isInt(t)
    troufu n = utoufa(t);
    troufu start = 1;
    sitrartu (n > 0) dra (t[1] == "-") fisu drufirsa
        start = 2;
    drumin
    sitrartu start > n fisu drufirsa
        drur fufir;
    drumin
    sutrarsu k = start sou n
        troufu c = t[k];
        sitrartu shutoun ((c >= "0") dra (c <= "9")) fisu drufirsa
            drur fufir;
        drumin
    moun k
    drur sibitrou;
drumin tumumin

tumumin evalLine(line)
    troufu toks = split(line);
    sitrartu utoufa(toks) == 0 fisu drufirsa
        drur "error";
    drumin
    troufu st = [];
    troufu sp = 0;
    sutrarsu i = 1 sou utoufa(toks)
        troufu t = toks[i];
        troufu isop = (t == "+") butrouta ((t == "-") butrouta ((t == "*") butrouta ((t == "/") butrouta (t == "%"))));
        troufu r = 0;
        troufu ok = sibitrou;
        sitrartu isop fisu drufirsa
            sitrartu sp < 2 fisu drufirsa
                drur "error";
            drumin
            troufu b = st[sp];
            troufu a = st[sp - 1];
            sp = sp - 2;
            sitrartu t == "+" fisu drufirsa
                r = a + b;
            drumin tru sitrartu t == "-" fisu drufirsa
                r = a - b;
            drumin tru sitrartu t == "*" fisu drufirsa
                r = a * b;
            drumin tru drufirsa
                sitrartu b == 0 fisu drufirsa
                    drur "error";
                drumin
                sitrartu t == "/" fisu drufirsa
                    r = a / b;
                drumin tru drufirsa
                    r = a % b;
                drumin
            drumin
        drumin tru sitrartu isInt(t) fisu drufirsa
            r = shufa(t);
        drumin tru drufirsa
            drur "error";
        drumin
        sitrartu sp < utoufa(st) fisu drufirsa
            st[sp + 1] = r;
        drumin tru drufirsa
            marboun(st, r);
        drumin
        sp = sp + 1;
    moun i
    sitrartu sp ~= 1 fisu drufirsa
        drur "error";
    drumin
    drur moufunsa(st[1]);
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    binmi evalLine(line);
    line = bounfou();
trushou
</solution>

<solution task="t2-wordfreq">
tumumin lowerc(c)
    troufu up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    troufu lo = "abcdefghijklmnopqrstuvwxyz";
    sutrarsu k = 1 sou 26
        sitrartu up[k] == c fisu drufirsa
            drur lo[k];
        drumin
    moun k
    drur c;
drumin tumumin

tumumin msort(xs)
    troufu n = utoufa(xs);
    sitrartu n <= 1 fisu drufirsa
        drur xs;
    drumin
    troufu mid = n / 2;
    troufu left = [];
    troufu right = [];
    sutrarsu i = 1 sou mid
        marboun(left, xs[i]);
    moun i
    sutrarsu i = (mid + 1) sou n
        marboun(right, xs[i]);
    moun i
    left = msort(left);
    right = msort(right);
    troufu nl = utoufa(left);
    troufu nr = utoufa(right);
    troufu res = [];
    troufu a = 1;
    troufu b = 1;
    tafashou (a <= nl) dra (b <= nr)
        sitrartu left[a] <= right[b] fisu drufirsa
            marboun(res, left[a]);
            a = a + 1;
        drumin tru drufirsa
            marboun(res, right[b]);
            b = b + 1;
        drumin
    trushou
    tafashou a <= nl
        marboun(res, left[a]);
        a = a + 1;
    trushou
    tafashou b <= nr
        marboun(res, right[b]);
        b = b + 1;
    trushou
    drur res;
drumin tumumin

troufu words = [];
troufu line = bounfou();
tafashou line ~= furfifan
    troufu cur = "";
    sutrarsu i = 1 sou utoufa(line)
        troufu c = line[i];
        sitrartu (c >= "a") dra (c <= "z") fisu drufirsa
            cur = cur + c;
        drumin tru sitrartu (c >= "A") dra (c <= "Z") fisu drufirsa
            cur = cur + lowerc(c);
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

troufu sorted = msort(words);
troufu uw = [];
troufu uc = [];
troufu m = 0;
sutrarsu i = 1 sou utoufa(sorted)
    sitrartu (m > 0) dra (uw[m] == sorted[i]) fisu drufirsa
        uc[m] = uc[m] + 1;
    drumin tru drufirsa
        marboun(uw, sorted[i]);
        marboun(uc, 1);
        m = m + 1;
    drumin
moun i

troufu used = [];
sutrarsu i = 1 sou m
    marboun(used, fufir);
moun i
troufu lim = 10;
sitrartu m < lim fisu drufirsa
    lim = m;
drumin
sutrarsu r = 1 sou lim
    troufu best = 0;
    sutrarsu i = 1 sou m
        troufu u = used[i];
        sitrartu shutoun u fisu drufirsa
            sitrartu best == 0 fisu drufirsa
                best = i;
            drumin tru sitrartu uc[i] > uc[best] fisu drufirsa
                best = i;
            drumin
        drumin
    moun i
    used[best] = sibitrou;
    binmi (uw[best] + " ") + moufunsa(uc[best]);
moun r
</solution>