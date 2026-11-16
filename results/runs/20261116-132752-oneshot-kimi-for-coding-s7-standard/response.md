<solution task="t0-count">
FOMOFE n := ZENZUMUR(TODETET());
TUTCHEK i := 1 ZUWOWEN n LOLO LEKFESH
    EPLOWEK i;
EFUDU
</solution>

<solution task="t0-day-names">
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE n := ZENZUMUR(line);
    ZET n CHU
    1: LEKFESH
        EPLOWEK "Monday";
    EFUDU
    2: LEKFESH
        EPLOWEK "Tuesday";
    EFUDU
    3: LEKFESH
        EPLOWEK "Wednesday";
    EFUDU
    4: LEKFESH
        EPLOWEK "Thursday";
    EFUDU
    5: LEKFESH
        EPLOWEK "Friday";
    EFUDU
    6: LEKFESH
        EPLOWEK "Saturday";
    EFUDU
    7: LEKFESH
        EPLOWEK "Sunday";
    EFUDU
    CHEME LEKFESH
        EPLOWEK "invalid";
    EFUDU EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t0-even-odd">
FOMOFE even := 0;
FOMOFE odd := 0;
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE n := ZENZUMUR(line);
    PLUWOK n % 2 = 0 DEWOTUSH LEKFESH
        even := even + 1;
    EFUDU CHEME LEKFESH
        odd := odd + 1;
    EFUDU
    line := TODETET();
EFUDU
EPLOWEK "even " & even;
EPLOWEK "odd " & odd;
</solution>

<solution task="t0-factorial">
FOMOFE n := ZENZUMUR(TODETET());
FOMOFE r := 1;
TUTCHEK i := 2 ZUWOWEN n LOLO LEKFESH
    r := r * i;
EFUDU
EPLOWEK r;
</solution>

<solution task="t0-fizzbuzz">
FOMOFE n := ZENZUMUR(TODETET());
TUTCHEK i := 1 ZUWOWEN n LOLO LEKFESH
    PLUWOK i % 3 = 0 ZULUSHTE i % 5 = 0 DEWOTUSH LEKFESH
        EPLOWEK "FizzBuzz";
    EFUDU CHEME PLUWOK i % 3 = 0 DEWOTUSH LEKFESH
        EPLOWEK "Fizz";
    EFUDU CHEME PLUWOK i % 5 = 0 DEWOTUSH LEKFESH
        EPLOWEK "Buzz";
    EFUDU CHEME LEKFESH
        EPLOWEK i;
    EFUDU
EFUDU
</solution>

<solution task="t0-hello">
EPLOWEK "Hello, Utopia!";
</solution>

<solution task="t0-reverse-lines">
FOMOFE lines := [];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    WESH(lines, line);
    line := TODETET();
EFUDU
FOMOFE i := FORMOWE(lines) - 1;
FUKCHEFE i >= 0 LOLO LEKFESH
    EPLOWEK lines[i];
    i := i - 1;
EFUDU
</solution>

<solution task="t1-digits">
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE n := ZENZUMUR(line);
    FOMOFE neg := n < 0;
    FOMOFE m := n;
    PLUWOK neg DEWOTUSH LEKFESH
        m := -n;
    EFUDU
    FOMOFE sum := 0;
    FOMOFE rev := 0;
    FUKCHEFE m > 0 LOLO LEKFESH
        sum := sum + m % 10;
        rev := rev * 10 + m % 10;
        m := m / 10;
    EFUDU
    FOMOFE out := rev;
    PLUWOK neg DEWOTUSH LEKFESH
        out := -rev;
    EFUDU
    EPLOWEK sum & " " & out;
    line := TODETET();
EFUDU
</solution>

<solution task="t1-floordiv">
EDEWUT splitSpaces(s) {
    FOMOFE toks := [];
    FOMOFE cur := "";
    FOMOFE i := 0;
    FUKCHEFE i < FORMOWE(s) LOLO LEKFESH
        PLUWOK s[i] = " " DEWOTUSH LEKFESH
            PLUWOK cur ~= "" DEWOTUSH LEKFESH
                WESH(toks, cur);
                cur := "";
            EFUDU
        EFUDU CHEME LEKFESH
            cur := cur & s[i];
        EFUDU
        i := i + 1;
    EFUDU
    PLUWOK cur ~= "" DEWOTUSH LEKFESH
        WESH(toks, cur);
    EFUDU
    EFOTU toks;
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE parts := splitSpaces(line);
    FOMOFE a := ZENZUMUR(parts[0]);
    FOMOFE b := ZENZUMUR(parts[1]);
    FOMOFE q := a / b;
    FOMOFE r := a % b;
    PLUWOK r ~= 0 ZULUSHTE ((r > 0) ~= (b > 0)) DEWOTUSH LEKFESH
        q := q - 1;
    EFUDU
    r := a - b * q;
    EPLOWEK q & " " & r;
    line := TODETET();
EFUDU
</solution>

<solution task="t1-palindromes">
EDEWUT isLetter(c) {
    EFOTU (c >= "A" ZULUSHTE c <= "Z") MUR (c >= "a" ZULUSHTE c <= "z");
}

EDEWUT isAlnum(c) {
    EFOTU (c >= "0" ZULUSHTE c <= "9") MUR isLetter(c);
}

EDEWUT lc(c) {
    FOMOFE alpha := "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    FOMOFE i := 0;
    FUKCHEFE i < 26 LOLO LEKFESH
        PLUWOK alpha[i] = c DEWOTUSH LEKFESH
            EFOTU alpha[i + 26];
        EFUDU
        i := i + 1;
    EFUDU
    EFOTU c;
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE f := "";
    FOMOFE i := 0;
    FUKCHEFE i < FORMOWE(line) LOLO LEKFESH
        PLUWOK isAlnum(line[i]) DEWOTUSH LEKFESH
            f := f & line[i];
        EFUDU
        i := i + 1;
    EFUDU
    FOMOFE ok := MULO;
    FOMOFE lo := 0;
    FOMOFE hi := FORMOWE(f) - 1;
    FUKCHEFE lo < hi LOLO LEKFESH
        PLUWOK lc(f[lo]) ~= lc(f[hi]) DEWOTUSH LEKFESH
            ok := LERLU;
        EFUDU
        lo := lo + 1;
        hi := hi - 1;
    EFUDU
    PLUWOK ok DEWOTUSH LEKFESH
        EPLOWEK "yes";
    EFUDU CHEME LEKFESH
        EPLOWEK "no";
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t1-rank">
EDEWUT splitSpaces(s) {
    FOMOFE toks := [];
    FOMOFE cur := "";
    FOMOFE i := 0;
    FUKCHEFE i < FORMOWE(s) LOLO LEKFESH
        PLUWOK s[i] = " " DEWOTUSH LEKFESH
            PLUWOK cur ~= "" DEWOTUSH LEKFESH
                WESH(toks, cur);
                cur := "";
            EFUDU
        EFUDU CHEME LEKFESH
            cur := cur & s[i];
        EFUDU
        i := i + 1;
    EFUDU
    PLUWOK cur ~= "" DEWOTUSH LEKFESH
        WESH(toks, cur);
    EFUDU
    EFOTU toks;
}

FOMOFE first := TODETET();
FOMOFE parts := splitSpaces(first);
FOMOFE xs := [];
FOMOFE i := 0;
FUKCHEFE i < FORMOWE(parts) LOLO LEKFESH
    WESH(xs, ZENZUMUR(parts[i]));
    i := i + 1;
EFUDU

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE q := ZENZUMUR(line);
    FOMOFE n := FORMOWE(xs);
    FOMOFE lo := 0;
    FOMOFE hi := n;
    FUKCHEFE lo < hi LOLO LEKFESH
        FOMOFE mid := (lo + hi) / 2;
        PLUWOK xs[mid] < q DEWOTUSH LEKFESH
            lo := mid + 1;
        EFUDU CHEME LEKFESH
            hi := mid;
        EFUDU
    EFUDU
    WOFE lo & " ";
    PLUWOK lo < n ZULUSHTE xs[lo] = q DEWOTUSH LEKFESH
        EPLOWEK "found";
    EFUDU CHEME LEKFESH
        EPLOWEK "missing";
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t1-rotate">
FOMOFE k := ZENZUMUR(TODETET());
FOMOFE items := [];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    WESH(items, line);
    line := TODETET();
EFUDU
FOMOFE n := FORMOWE(items);
PLUWOK n > 0 DEWOTUSH LEKFESH
    FOMOFE r := k % n;
    PLUWOK r < 0 DEWOTUSH LEKFESH
        r := r + n;
    EFUDU
    TUTCHEK i := n - r ZUWOWEN n - 1 LOLO LEKFESH
        EPLOWEK items[i];
    EFUDU
    TUTCHEK i := 0 ZUWOWEN n - r - 1 LOLO LEKFESH
        EPLOWEK items[i];
    EFUDU
EFUDU
</solution>

<solution task="t1-weekday">
EDEWUT weekday(y, m, d) {
    FOMOFE yy := y - 1;
    FOMOFE days := yy * 365 + yy / 4 - yy / 100 + yy / 400;
    FOMOFE mdays := [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    FOMOFE leap := (y % 4 = 0 ZULUSHTE y % 100 ~= 0) MUR y % 400 = 0;
    PLUWOK leap DEWOTUSH LEKFESH
        mdays[1] := 29;
    EFUDU
    FOMOFE i := 0;
    FUKCHEFE i < m - 1 LOLO LEKFESH
        days := days + mdays[i];
        i := i + 1;
    EFUDU
    days := days + d - 1;
    FOMOFE w := days % 7;
    ZET w CHU
    0: LEKFESH
        EFOTU "Monday";
    EFUDU
    1: LEKFESH
        EFOTU "Tuesday";
    EFUDU
    2: LEKFESH
        EFOTU "Wednesday";
    EFUDU
    3: LEKFESH
        EFOTU "Thursday";
    EFUDU
    4: LEKFESH
        EFOTU "Friday";
    EFUDU
    5: LEKFESH
        EFOTU "Saturday";
    EFUDU
    CHEME LEKFESH
        EFOTU "Sunday";
    EFUDU EFUDU
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE y := ZENZUMUR(line[0] & line[1] & line[2] & line[3]);
    FOMOFE m := ZENZUMUR(line[5] & line[6]);
    FOMOFE d := ZENZUMUR(line[8] & line[9]);
    EPLOWEK weekday(y, m, d);
    line := TODETET();
EFUDU
</solution>

<solution task="t2-bignum">
EDEWUT splitSpaces(s) {
    FOMOFE toks := [];
    FOMOFE cur := "";
    FOMOFE i := 0;
    FUKCHEFE i < FORMOWE(s) LOLO LEKFESH
        PLUWOK s[i] = " " DEWOTUSH LEKFESH
            PLUWOK cur ~= "" DEWOTUSH LEKFESH
                WESH(toks, cur);
                cur := "";
            EFUDU
        EFUDU CHEME LEKFESH
            cur := cur & s[i];
        EFUDU
        i := i + 1;
    EFUDU
    PLUWOK cur ~= "" DEWOTUSH LEKFESH
        WESH(toks, cur);
    EFUDU
    EFOTU toks;
}

EDEWUT toDigits(s) {
    FOMOFE ds := [];
    FOMOFE i := FORMOWE(s) - 1;
    FUKCHEFE i >= 0 LOLO LEKFESH
        WESH(ds, ZENZUMUR(s[i]));
        i := i - 1;
    EFUDU
    EFOTU ds;
}

EDEWUT trim(ds) {
    FOMOFE i := FORMOWE(ds);
    FUKCHEFE i > 1 ZULUSHTE ds[i - 1] = 0 LOLO LEKFESH
        i := i - 1;
    EFUDU
    FOMOFE r := [];
    FOMOFE j := 0;
    FUKCHEFE j < i LOLO LEKFESH
        WESH(r, ds[j]);
        j := j + 1;
    EFUDU
    EFOTU r;
}

EDEWUT addBig(a, b) {
    FOMOFE r := [];
    FOMOFE i := 0;
    FOMOFE carry := 0;
    FOMOFE la := FORMOWE(a);
    FOMOFE lb := FORMOWE(b);
    FUKCHEFE i < la MUR i < lb MUR carry > 0 LOLO LEKFESH
        FOMOFE s := carry;
        PLUWOK i < la DEWOTUSH LEKFESH
            s := s + a[i];
        EFUDU
        PLUWOK i < lb DEWOTUSH LEKFESH
            s := s + b[i];
        EFUDU
        WESH(r, s % 10);
        carry := s / 10;
        i := i + 1;
    EFUDU
    EFOTU trim(r);
}

EDEWUT mulBig(a, b) {
    FOMOFE la := FORMOWE(a);
    FOMOFE lb := FORMOWE(b);
    FOMOFE r := [];
    TUTCHEK i := 0 ZUWOWEN la + lb - 1 LOLO LEKFESH
        WESH(r, 0);
    EFUDU
    TUTCHEK i := 0 ZUWOWEN la - 1 LOLO LEKFESH
        FOMOFE carry := 0;
        TUTCHEK j := 0 ZUWOWEN lb - 1 LOLO LEKFESH
            FOMOFE s := r[i + j] + a[i] * b[j] + carry;
            r[i + j] := s % 10;
            carry := s / 10;
        EFUDU
        FOMOFE k := i + lb;
        FUKCHEFE carry > 0 LOLO LEKFESH
            FOMOFE s := r[k] + carry;
            r[k] := s % 10;
            carry := s / 10;
            k := k + 1;
        EFUDU
    EFUDU
    EFOTU trim(r);
}

EDEWUT toStr(ds) {
    FOMOFE s := "";
    FOMOFE i := FORMOWE(ds) - 1;
    FUKCHEFE i >= 0 LOLO LEKFESH
        s := s & ECHEK(ds[i]);
        i := i - 1;
    EFUDU
    EFOTU s;
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE parts := splitSpaces(line);
    FOMOFE a := toDigits(parts[0]);
    FOMOFE b := toDigits(parts[1]);
    EPLOWEK toStr(addBig(a, b)) & " " & toStr(mulBig(a, b));
    line := TODETET();
EFUDU
</solution>

<solution task="t2-life">
FOMOFE g := ZENZUMUR(TODETET());
FOMOFE grid := [];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE row := [];
    FOMOFE i := 0;
    FUKCHEFE i < FORMOWE(line) LOLO LEKFESH
        PLUWOK line[i] = "#" DEWOTUSH LEKFESH
            WESH(row, 1);
        EFUDU CHEME LEKFESH
            WESH(row, 0);
        EFUDU
        i := i + 1;
    EFUDU
    WESH(grid, row);
    line := TODETET();
EFUDU
FOMOFE R := FORMOWE(grid);
FOMOFE C := 0;
PLUWOK R > 0 DEWOTUSH LEKFESH
    C := FORMOWE(grid[0]);
EFUDU

TUTCHEK gen := 1 ZUWOWEN g LOLO LEKFESH
    FOMOFE ng := [];
    TUTCHEK r := 0 ZUWOWEN R - 1 LOLO LEKFESH
        FOMOFE nrow := [];
        TUTCHEK c := 0 ZUWOWEN C - 1 LOLO LEKFESH
            FOMOFE cnt := 0;
            TUTCHEK dr := -1 ZUWOWEN 1 LOLO LEKFESH
                TUTCHEK dc := -1 ZUWOWEN 1 LOLO LEKFESH
                    PLUWOK TEMO (dr = 0 ZULUSHTE dc = 0) DEWOTUSH LEKFESH
                        FOMOFE rr := r + dr;
                        FOMOFE cc := c + dc;
                        PLUWOK rr >= 0 ZULUSHTE rr < R ZULUSHTE cc >= 0 ZULUSHTE cc < C DEWOTUSH LEKFESH
                            cnt := cnt + grid[rr][cc];
                        EFUDU
                    EFUDU
                EFUDU
            EFUDU
            FOMOFE alive := 0;
            PLUWOK grid[r][c] = 1 DEWOTUSH LEKFESH
                PLUWOK cnt = 2 MUR cnt = 3 DEWOTUSH LEKFESH
                    alive := 1;
                EFUDU
            EFUDU CHEME PLUWOK cnt = 3 DEWOTUSH LEKFESH
                alive := 1;
            EFUDU
            WESH(nrow, alive);
        EFUDU
        WESH(ng, nrow);
    EFUDU
    grid := ng;
EFUDU

TUTCHEK r := 0 ZUWOWEN R - 1 LOLO LEKFESH
    FOMOFE s := "";
    TUTCHEK c := 0 ZUWOWEN C - 1 LOLO LEKFESH
        PLUWOK grid[r][c] = 1 DEWOTUSH LEKFESH
            s := s & "#";
        EFUDU CHEME LEKFESH
            s := s & ".";
        EFUDU
    EFUDU
    EPLOWEK s;
EFUDU
</solution>

<solution task="t2-rpn">
EDEWUT splitSpaces(s) {
    FOMOFE toks := [];
    FOMOFE cur := "";
    FOMOFE i := 0;
    FUKCHEFE i < FORMOWE(s) LOLO LEKFESH
        PLUWOK s[i] = " " DEWOTUSH LEKFESH
            PLUWOK cur ~= "" DEWOTUSH LEKFESH
                WESH(toks, cur);
                cur := "";
            EFUDU
        EFUDU CHEME LEKFESH
            cur := cur & s[i];
        EFUDU
        i := i + 1;
    EFUDU
    PLUWOK cur ~= "" DEWOTUSH LEKFESH
        WESH(toks, cur);
    EFUDU
    EFOTU toks;
}

EDEWUT isInt(s) {
    PLUWOK FORMOWE(s) = 0 DEWOTUSH LEKFESH
        EFOTU LERLU;
    EFUDU
    FOMOFE i := 0;
    PLUWOK s[0] = "-" DEWOTUSH LEKFESH
        PLUWOK FORMOWE(s) = 1 DEWOTUSH LEKFESH
            EFOTU LERLU;
        EFUDU
        i := 1;
    EFUDU
    FUKCHEFE i < FORMOWE(s) LOLO LEKFESH
        FOMOFE c := s[i];
        PLUWOK TEMO (c >= "0" ZULUSHTE c <= "9") DEWOTUSH LEKFESH
            EFOTU LERLU;
        EFUDU
        i := i + 1;
    EFUDU
    EFOTU MULO;
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE toks := splitSpaces(line);
    FOMOFE st := [];
    FOMOFE size := 0;
    FOMOFE err := LERLU;
    FOMOFE i := 0;
    FUKCHEFE i < FORMOWE(toks) LOLO LEKFESH
        FOMOFE t := toks[i];
        PLUWOK err = LERLU DEWOTUSH LEKFESH
            PLUWOK isInt(t) DEWOTUSH LEKFESH
                WESH(st, ZENZUMUR(t));
                size := size + 1;
            EFUDU CHEME PLUWOK t = "+" MUR t = "-" MUR t = "*" MUR t = "/" MUR t = "%" DEWOTUSH LEKFESH
                PLUWOK size < 2 DEWOTUSH LEKFESH
                    err := MULO;
                EFUDU CHEME LEKFESH
                    FOMOFE b := st[size - 1];
                    FOMOFE a := st[size - 2];
                    size := size - 2;
                    FOMOFE v := 0;
                    PLUWOK t = "+" DEWOTUSH LEKFESH
                        v := a + b;
                    EFUDU CHEME PLUWOK t = "-" DEWOTUSH LEKFESH
                        v := a - b;
                    EFUDU CHEME PLUWOK t = "*" DEWOTUSH LEKFESH
                        v := a * b;
                    EFUDU CHEME PLUWOK t = "/" DEWOTUSH LEKFESH
                        PLUWOK b = 0 DEWOTUSH LEKFESH
                            err := MULO;
                        EFUDU CHEME LEKFESH
                            v := a / b;
                        EFUDU
                    EFUDU CHEME LEKFESH
                        PLUWOK b = 0 DEWOTUSH LEKFESH
                            err := MULO;
                        EFUDU CHEME LEKFESH
                            v := a % b;
                        EFUDU
                    EFUDU
                    PLUWOK err = LERLU DEWOTUSH LEKFESH
                        WESH(st, v);
                        size := size + 1;
                    EFUDU
                EFUDU
            EFUDU CHEME LEKFESH
                err := MULO;
            EFUDU
        EFUDU
        i := i + 1;
    EFUDU
    PLUWOK err = MULO DEWOTUSH LEKFESH
        EPLOWEK "error";
    EFUDU CHEME PLUWOK size = 1 DEWOTUSH LEKFESH
        EPLOWEK st[0];
    EFUDU CHEME LEKFESH
        EPLOWEK "error";
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t2-wordfreq">
EDEWUT isLetter(c) {
    EFOTU (c >= "A" ZULUSHTE c <= "Z") MUR (c >= "a" ZULUSHTE c <= "z");
}

EDEWUT lc(c) {
    FOMOFE alpha := "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    FOMOFE i := 0;
    FUKCHEFE i < 26 LOLO LEKFESH
        PLUWOK alpha[i] = c DEWOTUSH LEKFESH
            EFOTU alpha[i + 26];
        EFUDU
        i := i + 1;
    EFUDU
    EFOTU c;
}

EDEWUT addWord(entries, w) {
    FOMOFE j := 0;
    FOMOFE found := LERLU;
    FUKCHEFE j < FORMOWE(entries) LOLO LEKFESH
        PLUWOK entries[j][0] = w DEWOTUSH LEKFESH
            entries[j][1] := entries[j][1] + 1;
            found := MULO;
        EFUDU
        j := j + 1;
    EFUDU
    PLUWOK TEMO found DEWOTUSH LEKFESH
        WESH(entries, [w, 1]);
    EFUDU
}

EDEWUT before(x, y) {
    PLUWOK x[1] > y[1] DEWOTUSH LEKFESH
        EFOTU MULO;
    EFUDU
    PLUWOK x[1] = y[1] ZULUSHTE x[0] < y[0] DEWOTUSH LEKFESH
        EFOTU MULO;
    EFUDU
    EFOTU LERLU;
}

FOMOFE entries := [];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE cur := "";
    FOMOFE i := 0;
    FUKCHEFE i < FORMOWE(line) LOLO LEKFESH
        FOMOFE c := line[i];
        PLUWOK isLetter(c) DEWOTUSH LEKFESH
            cur := cur & lc(c);
        EFUDU CHEME PLUWOK cur ~= "" DEWOTUSH LEKFESH
            addWord(entries, cur);
            cur := "";
        EFUDU
        i := i + 1;
    EFUDU
    PLUWOK cur ~= "" DEWOTUSH LEKFESH
        addWord(entries, cur);
    EFUDU
    line := TODETET();
EFUDU

FOMOFE m := FORMOWE(entries);
TUTCHEK i := 1 ZUWOWEN m - 1 LOLO LEKFESH
    FOMOFE j := i;
    FUKCHEFE j > 0 ZULUSHTE before(entries[j], entries[j - 1]) LOLO LEKFESH
        FOMOFE tmp := entries[j];
        entries[j] := entries[j - 1];
        entries[j - 1] := tmp;
        j := j - 1;
    EFUDU
EFUDU

FOMOFE lim := m;
PLUWOK lim > 10 DEWOTUSH LEKFESH
    lim := 10;
EFUDU
TUTCHEK i := 0 ZUWOWEN lim - 1 LOLO LEKFESH
    EPLOWEK entries[i][0] & " " & entries[i][1];
EFUDU
</solution>