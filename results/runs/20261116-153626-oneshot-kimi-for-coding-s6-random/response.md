<solution task="t0-count">
troufu n = shufa(bounfou());
sutrarsu i = 1 sou n
    binmi i;
moun i
</solution>

<solution task="t0-day-names">
troufu line = bounfou();
tafashou line ~= furfifan
    troufu n = shufa(line);
    utir (n) {
    sourmar 1:
        binmi "Monday";
        basu;
    sourmar 2:
        binmi "Tuesday";
        basu;
    sourmar 3:
        binmi "Wednesday";
        basu;
    sourmar 4:
        binmi "Thursday";
        basu;
    sourmar 5:
        binmi "Friday";
        basu;
    sourmar 6:
        binmi "Saturday";
        basu;
    sourmar 7:
        binmi "Sunday";
        basu;
    fitru:
        binmi "invalid";
    }
    line = bounfou();
trushou
</solution>

<solution task="t0-even-odd">
troufu even = 0;
troufu odd = 0;
troufu line = bounfou();
tafashou line ~= furfifan
    troufu n = shufa(line);
    sitrartu (n % 2) == 0 fisu drufirsa
        even = even + 1;
    drumin tru drufirsa
        odd = odd + 1;
    drumin
    line = bounfou();
trushou
binmi "even " + even;
binmi "odd " + odd;
</solution>

<solution task="t0-factorial">
troufu n = shufa(bounfou());
troufu result = 1;
sutrarsu i = 1 sou n
    result = result * i;
moun i
binmi result;
</solution>

<solution task="t0-fizzbuzz">
troufu n = shufa(bounfou());
sutrarsu i = 1 sou n
    sitrartu (((i % 3) == 0) dra ((i % 5) == 0)) fisu drufirsa
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
troufu lines = [];
troufu line = bounfou();
tafashou line ~= furfifan
    marboun(lines, line);
    line = bounfou();
trushou
sutrarsu i = utoufa(lines) sou 1 suntru -1
    binmi lines[i];
moun i
</solution>

<solution task="t1-digits">
troufu line = bounfou();
tafashou line ~= furfifan
    troufu n = shufa(line);
    troufu m = n;
    sitrartu n < 0 fisu drufirsa
        m = 0 - n;
    drumin
    troufu sum = 0;
    troufu rev = 0;
    tafashou m > 0
        sum = sum + (m % 10);
        rev = (rev * 10) + (m % 10);
        m = m / 10;
    trushou
    sitrartu n < 0 fisu drufirsa
        binmi (sum + " ") + (0 - rev);
    drumin tru drufirsa
        binmi (sum + " ") + rev;
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t1-floordiv">
tumumin split(s)
    troufu parts = [];
    troufu cur = "";
    sitrartu s == "" fisu drufirsa
        drur parts;
    drumin
    sutrarsu i = 1 sou utoufa(s)
        sitrartu s[i] == " " fisu drufirsa
            sitrartu cur ~= "" fisu drufirsa
                marboun(parts, cur);
            drumin
            cur = "";
        drumin tru drufirsa
            cur = cur + s[i];
        drumin
    moun i
    sitrartu cur ~= "" fisu drufirsa
        marboun(parts, cur);
    drumin
    drur parts;
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu parts = split(line);
    troufu a = shufa(parts[1]);
    troufu b = shufa(parts[2]);
    troufu q = a / b;
    troufu r = a % b;
    sitrartu ((r ~= 0) dra ((r < 0) ~= (b < 0))) fisu drufirsa
        q = q - 1;
        r = r + b;
    drumin
    binmi (q + " ") + r;
    line = bounfou();
trushou
</solution>

<solution task="t1-palindromes">
tumumin isletter(c)
    drur (((c >= "A") dra (c <= "Z")) butrouta ((c >= "a") dra (c <= "z")));
drumin tumumin

tumumin isdigit(c)
    drur (((c >= "0") dra (c <= "9")));
drumin tumumin

tumumin lowerchar(c)
    troufu upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    troufu lower = "abcdefghijklmnopqrstuvwxyz";
    sutrarsu i = 1 sou 26
        sitrartu c == upper[i] fisu drufirsa
            drur lower[i];
        drumin
    moun i
    drur c;
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu cleaned = "";
    sutrarsu i = 1 sou utoufa(line)
        troufu c = line[i];
        sitrartu isletter(c) fisu drufirsa
            cleaned = cleaned + lowerchar(c);
        drumin tru sitrartu isdigit(c) fisu drufirsa
            cleaned = cleaned + c;
        drumin
    moun i
    troufu ok = sibitrou;
    sutrarsu i = 1 sou (utoufa(cleaned) / 2)
        sitrartu cleaned[i] ~= cleaned[((utoufa(cleaned) - i) + 1)] fisu drufirsa
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
    troufu parts = [];
    troufu cur = "";
    sitrartu s == "" fisu drufirsa
        drur parts;
    drumin
    sutrarsu i = 1 sou utoufa(s)
        sitrartu s[i] == " " fisu drufirsa
            sitrartu cur ~= "" fisu drufirsa
                marboun(parts, cur);
            drumin
            cur = "";
        drumin tru drufirsa
            cur = cur + s[i];
        drumin
    moun i
    sitrartu cur ~= "" fisu drufirsa
        marboun(parts, cur);
    drumin
    drur parts;
drumin tumumin

troufu first = bounfou();
troufu nums = [];
sitrartu first ~= "" fisu drufirsa
    troufu toks = split(first);
    sutrarsu i = 1 sou utoufa(toks)
        marboun(nums, shufa(toks[i]));
    moun i
drumin
troufu line = bounfou();
tafashou line ~= furfifan
    troufu q = shufa(line);
    troufu smaller = 0;
    troufu found = fufir;
    sutrarsu i = 1 sou utoufa(nums)
        sitrartu nums[i] < q fisu drufirsa
            smaller = smaller + 1;
        drumin
        sitrartu nums[i] == q fisu drufirsa
            found = sibitrou;
        drumin
    moun i
    troufu label = "missing";
    sitrartu found fisu drufirsa
        label = "found";
    drumin
    binmi (smaller + " ") + label;
    line = bounfou();
trushou
</solution>

<solution task="t1-rotate">
troufu k = shufa(bounfou());
troufu items = [];
troufu line = bounfou();
tafashou line ~= furfifan
    marboun(items, line);
    line = bounfou();
trushou
troufu n = utoufa(items);
sitrartu n > 0 fisu drufirsa
    troufu kk = k % n;
    sitrartu k < 0 fisu drufirsa
        kk = n - ((0 - k) % n);
        sitrartu kk == n fisu drufirsa
            kk = 0;
        drumin
    drumin
    sitrartu kk == 0 fisu drufirsa
        sutrarsu i = 1 sou n
            binmi items[i];
        moun i
    drumin tru drufirsa
        troufu start = ((n - kk) + 1);
        sutrarsu i = start sou n
            binmi items[i];
        moun i
        sutrarsu i = 1 sou (start - 1)
            binmi items[i];
        moun i
    drumin
drumin
</solution>

<solution task="t1-weekday">
tumumin substr(s, a, b)
    troufu out = "";
    sutrarsu i = a sou b
        out = out + s[i];
    moun i
    drur out;
drumin tumumin

tumumin weekdaynum(date)
    troufu y = shufa(substr(date, 1, 4));
    troufu m = shufa(substr(date, 6, 7));
    troufu d = shufa(substr(date, 9, 10));
    troufu yy = y - 1;
    troufu days = ((((365 * yy) + (yy / 4)) - (yy / 100)) + (yy / 400));
    troufu leap = (((y % 4) == 0) dra (((y % 100) ~= 0) butrouta ((y % 400) == 0)));
    troufu offsets = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
    sitrartu leap fisu drufirsa
        offsets = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335];
    drumin
    days = (days + offsets[m]) + (d - 1);
    drur days % 7;
drumin tumumin

tumumin weekdayname(w)
    utir (w) {
    sourmar 0:
        drur "Monday";
    sourmar 1:
        drur "Tuesday";
    sourmar 2:
        drur "Wednesday";
    sourmar 3:
        drur "Thursday";
    sourmar 4:
        drur "Friday";
    sourmar 5:
        drur "Saturday";
    sourmar 6:
        drur "Sunday";
    }
    drur "Monday";
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    binmi weekdayname(weekdaynum(line));
    line = bounfou();
trushou
</solution>

<solution task="t2-bignum">
tumumin split(s)
    troufu parts = [];
    troufu cur = "";
    sitrartu s == "" fisu drufirsa
        drur parts;
    drumin
    sutrarsu i = 1 sou utoufa(s)
        sitrartu s[i] == " " fisu drufirsa
            sitrartu cur ~= "" fisu drufirsa
                marboun(parts, cur);
            drumin
            cur = "";
        drumin tru drufirsa
            cur = cur + s[i];
        drumin
    moun i
    sitrartu cur ~= "" fisu drufirsa
        marboun(parts, cur);
    drumin
    drur parts;
drumin tumumin

tumumin charval(c)
    troufu ds = "0123456789";
    sutrarsu i = 1 sou 10
        sitrartu c == ds[i] fisu drufirsa
            drur (i - 1);
        drumin
    moun i
    drur -1;
drumin tumumin

tumumin digitchar(d)
    troufu ds = "0123456789";
    drur ds[(d + 1)];
drumin tumumin

tumumin todigits(s)
    troufu ds = [];
    sutrarsu i = 1 sou utoufa(s)
        marboun(ds, charval(s[i]));
    moun i
    drur ds;
drumin tumumin

tumumin flip(xs)
    troufu out = [];
    sutrarsu i = utoufa(xs) sou 1 suntru -1
        marboun(out, xs[i]);
    moun i
    drur out;
drumin tumumin

tumumin undigits(ds)
    troufu i = 1;
    tafashou (i < utoufa(ds)) dra (ds[i] == 0)
        i = i + 1;
    trushou
    troufu out = "";
    sutrarsu j = i sou utoufa(ds)
        out = out + digitchar(ds[j]);
    moun j
    drur out;
drumin tumumin

tumumin bigadd(a, b)
    troufu da = todigits(a);
    troufu db = todigits(b);
    troufu i = utoufa(da);
    troufu j = utoufa(db);
    troufu carry = 0;
    troufu out = [];
    tafashou ((i >= 1) butrouta (j >= 1)) butrouta (carry ~= 0)
        troufu sum = carry;
        sitrartu i >= 1 fisu drufirsa
            sum = sum + da[i];
            i = i - 1;
        drumin
        sitrartu j >= 1 fisu drufirsa
            sum = sum + db[j];
            j = j - 1;
        drumin
        marboun(out, sum % 10);
        carry = sum / 10;
    trushou
    drur undigits(flip(out));
drumin tumumin

tumumin bigmul(a, b)
    sitrartu a == "0" fisu drufirsa
        drur "0";
    drumin
    sitrartu b == "0" fisu drufirsa
        drur "0";
    drumin
    troufu da = todigits(a);
    troufu db = todigits(b);
    troufu total = (utoufa(da) + utoufa(db)) + 1;
    troufu res = [];
    sutrarsu i = 1 sou total
        marboun(res, 0);
    moun i
    sutrarsu ia = utoufa(da) sou 1 suntru -1
        sutrarsu ib = utoufa(db) sou 1 suntru -1
            troufu offset = ((utoufa(da) - ia) + (utoufa(db) - ib));
            troufu idx = total - offset;
            res[idx] = res[idx] + (da[ia] * db[ib]);
        moun ib
    moun ia
    sutrarsu idx = total sou 2 suntru -1
        troufu carry = res[idx] / 10;
        res[idx] = res[idx] % 10;
        res[idx - 1] = res[idx - 1] + carry;
    moun idx
    drur undigits(res);
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu parts = split(line);
    binmi (bigadd(parts[1], parts[2]) + " ") + bigmul(parts[1], parts[2]);
    line = bounfou();
trushou
</solution>

<solution task="t2-life">
tumumin nextcell(alive, neighbors)
    sitrartu alive fisu drufirsa
        sitrartu ((neighbors == 2) butrouta (neighbors == 3)) fisu drufirsa
            drur "#";
        drumin
        drur ".";
    drumin
    sitrartu neighbors == 3 fisu drufirsa
        drur "#";
    drumin
    drur ".";
drumin tumumin

troufu g = shufa(bounfou());
troufu grid = [];
troufu line = bounfou();
tafashou line ~= furfifan
    marboun(grid, line);
    line = bounfou();
trushou
troufu rows = utoufa(grid);
troufu cols = utoufa(grid[1]);
troufu gen = 0;
tafashou gen < g
    troufu nextgrid = [];
    sutrarsu r = 1 sou rows
        troufu nextrow = "";
        sutrarsu c = 1 sou cols
            troufu neighbors = 0;
            sutrarsu dr = -1 sou 1
                sutrarsu dc = -1 sou 1
                    sitrartu (dr == 0) dra (dc == 0) fisu drufirsa
                        samu;
                    drumin
                    troufu rr = r + dr;
                    troufu cc = c + dc;
                    sitrartu ((rr >= 1) dra ((rr <= rows) dra ((cc >= 1) dra (cc <= cols)))) fisu drufirsa
                        sitrartu grid[rr][cc] == "#" fisu drufirsa
                            neighbors = neighbors + 1;
                        drumin
                    drumin
                moun dc
            moun dr
            nextrow = nextrow + nextcell(grid[r][c] == "#", neighbors);
        moun c
        marboun(nextgrid, nextrow);
    moun r
    grid = nextgrid;
    gen = gen + 1;
trushou
sutrarsu r = 1 sou rows
    binmi grid[r];
moun r
</solution>

<solution task="t2-rpn">
tumumin split(s)
    troufu parts = [];
    troufu cur = "";
    sitrartu s == "" fisu drufirsa
        drur parts;
    drumin
    sutrarsu i = 1 sou utoufa(s)
        sitrartu s[i] == " " fisu drufirsa
            sitrartu cur ~= "" fisu drufirsa
                marboun(parts, cur);
            drumin
            cur = "";
        drumin tru drufirsa
            cur = cur + s[i];
        drumin
    moun i
    sitrartu cur ~= "" fisu drufirsa
        marboun(parts, cur);
    drumin
    drur parts;
drumin tumumin

tumumin isdigit(c)
    drur ((c >= "0") dra (c <= "9"));
drumin tumumin

tumumin isint(s)
    sitrartu utoufa(s) == 0 fisu drufirsa
        drur fufir;
    drumin
    troufu start = 1;
    sitrartu s[1] == "-" fisu drufirsa
        sitrartu utoufa(s) == 1 fisu drufirsa
            drur fufir;
        drumin
        start = 2;
    drumin
    sutrarsu i = start sou utoufa(s)
        sitrartu (shutoun (isdigit(s[i]))) fisu drufirsa
            drur fufir;
        drumin
    moun i
    drur sibitrou;
drumin tumumin

tumumin isop(s)
    drur (((s == "+") butrouta (s == "-")) butrouta ((s == "*") butrouta ((s == "/") butrouta (s == "%"))));
drumin tumumin

troufu line = bounfou();
tafashou line ~= furfifan
    troufu toks = split(line);
    troufu stack = [];
    troufu top = 0;
    troufu bad = fufir;
    sitrartu utoufa(toks) == 0 fisu drufirsa
        bad = sibitrou;
    drumin
    sutrarsu i = 1 sou utoufa(toks)
        troufu tok = toks[i];
        sitrartu bad fisu drufirsa
            samu;
        drumin
        sitrartu isint(tok) fisu drufirsa
            top = top + 1;
            sitrartu top > utoufa(stack) fisu drufirsa
                marboun(stack, 0);
            drumin
            stack[top] = shufa(tok);
        drumin tru sitrartu isop(tok) fisu drufirsa
            sitrartu top < 2 fisu drufirsa
                bad = sibitrou;
                samu;
            drumin
            troufu b = stack[top];
            troufu a = stack[top - 1];
            top = top - 1;
            sitrartu tok == "+" fisu drufirsa
                stack[top] = a + b;
            drumin tru sitrartu tok == "-" fisu drufirsa
                stack[top] = a - b;
            drumin tru sitrartu tok == "*" fisu drufirsa
                stack[top] = a * b;
            drumin tru sitrartu tok == "/" fisu drufirsa
                sitrartu b == 0 fisu drufirsa
                    bad = sibitrou;
                    samu;
                drumin
                stack[top] = a / b;
            drumin tru drufirsa
                sitrartu b == 0 fisu drufirsa
                    bad = sibitrou;
                    samu;
                drumin
                stack[top] = a % b;
            drumin
        drumin tru drufirsa
            bad = sibitrou;
        drumin
    moun i
    sitrartu bad fisu drufirsa
        binmi "error";
    drumin tru sitrartu top == 1 fisu drufirsa
        binmi stack[1];
    drumin tru drufirsa
        binmi "error";
    drumin
    line = bounfou();
trushou
</solution>

<solution task="t2-wordfreq">
tumumin isletter(c)
    drur (((c >= "A") dra (c <= "Z")) butrouta ((c >= "a") dra (c <= "z")));
drumin tumumin

tumumin isdigit(c)
    drur ((c >= "0") dra (c <= "9"));
drumin tumumin

tumumin lowerchar(c)
    troufu upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    troufu lower = "abcdefghijklmnopqrstuvwxyz";
    sutrarsu i = 1 sou 26
        sitrartu c == upper[i] fisu drufirsa
            drur lower[i];
        drumin
    moun i
    drur c;
drumin tumumin

tumumin findword(words, w)
    sutrarsu i = 1 sou utoufa(words)
        sitrartu words[i] == w fisu drufirsa
            drur i;
        drumin
    moun i
    drur 0;
drumin tumumin

troufu words = [];
troufu counts = [];
troufu line = bounfou();
tafashou line ~= furfifan
    troufu cur = "";
    sutrarsu i = 1 sou utoufa(line)
        troufu c = line[i];
        sitrartu isletter(c) fisu drufirsa
            cur = cur + lowerchar(c);
        drumin tru sitrartu isdigit(c) fisu drufirsa
            cur = cur + c;
        drumin tru drufirsa
            sitrartu cur ~= "" fisu drufirsa
                troufu p = findword(words, cur);
                sitrartu p == 0 fisu drufirsa
                    marboun(words, cur);
                    marboun(counts, 1);
                drumin tru drufirsa
                    counts[p] = counts[p] + 1;
                drumin
                cur = "";
            drumin
        drumin
    moun i
    sitrartu cur ~= "" fisu drufirsa
        troufu p = findword(words, cur);
        sitrartu p == 0 fisu drufirsa
            marboun(words, cur);
            marboun(counts, 1);
        drumin tru drufirsa
            counts[p] = counts[p] + 1;
        drumin
    drumin
    line = bounfou();
trushou
troufu m = utoufa(words);
troufu used = [];
sutrarsu i = 1 sou m
    marboun(used, fufir);
moun i
sutrarsu printed = 1 sou 10
    troufu best = 0;
    sutrarsu j = 1 sou m
        sitrartu used[j] ~= sibitrou fisu drufirsa
            sitrartu best == 0 fisu drufirsa
                best = j;
            drumin tru sitrartu counts[j] > counts[best] fisu drufirsa
                best = j;
            drumin tru sitrartu ((counts[j] == counts[best]) dra (words[j] < words[best])) fisu drufirsa
                best = j;
            drumin
        drumin
    moun j
    sitrartu best == 0 fisu drufirsa
        basu;
    drumin
    binmi (words[best] + " ") + counts[best];
    used[best] = sibitrou;
moun printed
</solution>