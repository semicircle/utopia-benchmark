<solution task="t0-count">
FOMOFE line := TODETET();
FOMOFE n := 0;
PLUWOK line ~= LER DEWOTUSH LEKFESH
    n := ZENZUMUR(line);
EFUDU
TUTCHEK i := 1 ZUWOWEN n LOLO LEKFESH
    EPLOWEK i;
EFUDU
</solution>

<solution task="t0-day-names">
FOMOFE names := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    PLUWOK FORMOWE(line) > 0 DEWOTUSH LEKFESH
        FOMOFE n := ZENZUMUR(line);
        PLUWOK n >= 1 ZULUSHTE n <= 7 DEWOTUSH LEKFESH
            EPLOWEK names[n - 1];
        EFUDU CHEME LEKFESH
            EPLOWEK "invalid";
        EFUDU
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t0-even-odd">
FOMOFE ev := 0;
FOMOFE od := 0;
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    PLUWOK FORMOWE(line) > 0 DEWOTUSH LEKFESH
        FOMOFE n := ZENZUMUR(line);
        PLUWOK n % 2 = 0 DEWOTUSH LEKFESH
            ev := ev + 1;
        EFUDU CHEME LEKFESH
            od := od + 1;
        EFUDU
    EFUDU
    line := TODETET();
EFUDU
EPLOWEK "even " & ev;
EPLOWEK "odd " & od;
</solution>

<solution task="t0-factorial">
FOMOFE n := ZENZUMUR(TODETET());
FOMOFE f := 1;
TUTCHEK i := 1 ZUWOWEN n LOLO LEKFESH
    f := f * i;
EFUDU
EPLOWEK f;
</solution>

<solution task="t0-fizzbuzz">
FOMOFE n := ZENZUMUR(TODETET());
TUTCHEK i := 1 ZUWOWEN n LOLO LEKFESH
    PLUWOK i % 15 = 0 DEWOTUSH LEKFESH
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
FOMOFE xs := [];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    WESH(xs, line);
    line := TODETET();
EFUDU
TUTCHEK i := FORMOWE(xs) - 1 ZUWOWEN 0 ZEPLO -1 LOLO LEKFESH
    EPLOWEK xs[i];
EFUDU
</solution>

<solution task="t1-digits">
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    PLUWOK FORMOWE(line) > 0 DEWOTUSH LEKFESH
        FOMOFE n := ZENZUMUR(line);
        FOMOFE a := n;
        PLUWOK a < 0 DEWOTUSH LEKFESH
            a := -a;
        EFUDU
        FOMOFE s := 0;
        FOMOFE r := 0;
        FUKCHEFE a > 0 LOLO LEKFESH
            s := s + a % 10;
            r := r * 10 + a % 10;
            a := a / 10;
        EFUDU
        PLUWOK n < 0 DEWOTUSH LEKFESH
            r := -r;
        EFUDU
        EPLOWEK s & " " & r;
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t1-floordiv">
EDEWUT split(s) {
    FOMOFE parts := [];
    FOMOFE cur := "";
    TUTCHEK i := 0 ZUWOWEN FORMOWE(s) - 1 LOLO LEKFESH
        FOMOFE c := s[i];
        PLUWOK c = " " MUR c = "\t" MUR c = "\r" DEWOTUSH LEKFESH
            PLUWOK FORMOWE(cur) > 0 DEWOTUSH LEKFESH
                WESH(parts, cur);
                cur := "";
            EFUDU
        EFUDU CHEME LEKFESH
            cur := cur & c;
        EFUDU
    EFUDU
    PLUWOK FORMOWE(cur) > 0 DEWOTUSH LEKFESH
        WESH(parts, cur);
    EFUDU
    EFOTU parts;
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE p := split(line);
    PLUWOK FORMOWE(p) >= 2 DEWOTUSH LEKFESH
        FOMOFE a := ZENZUMUR(p[0]);
        FOMOFE b := ZENZUMUR(p[1]);
        FOMOFE q := a / b;
        FOMOFE r := a - b * q;
        PLUWOK (r < 0 ZULUSHTE b > 0) MUR (r > 0 ZULUSHTE b < 0) DEWOTUSH LEKFESH
            q := q - 1;
            r := r + b;
        EFUDU
        EPLOWEK q & " " & r;
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t1-palindromes">
EDEWUT lowerChar(c) {
    FOMOFE up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    FOMOFE lo := "abcdefghijklmnopqrstuvwxyz";
    PLUWOK c >= "A" ZULUSHTE c <= "Z" DEWOTUSH LEKFESH
        TUTCHEK i := 0 ZUWOWEN 25 LOLO LEKFESH
            PLUWOK up[i] = c DEWOTUSH LEKFESH
                EFOTU lo[i];
            EFUDU
        EFUDU
    EFUDU
    EFOTU c;
}

EDEWUT isAlnum(c) {
    EFOTU (c >= "a" ZULUSHTE c <= "z") MUR (c >= "0" ZULUSHTE c <= "9");
}

EDEWUT check(line) {
    FOMOFE t := [];
    TUTCHEK i := 0 ZUWOWEN FORMOWE(line) - 1 LOLO LEKFESH
        FOMOFE c := lowerChar(line[i]);
        PLUWOK isAlnum(c) DEWOTUSH LEKFESH
            WESH(t, c);
        EFUDU
    EFUDU
    FOMOFE a := 0;
    FOMOFE b := FORMOWE(t) - 1;
    FUKCHEFE a < b LOLO LEKFESH
        PLUWOK t[a] ~= t[b] DEWOTUSH LEKFESH
            EFOTU "no";
        EFUDU
        a := a + 1;
        b := b - 1;
    EFUDU
    EFOTU "yes";
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    EPLOWEK check(line);
    line := TODETET();
EFUDU
</solution>

<solution task="t1-rank">
EDEWUT split(s) {
    FOMOFE parts := [];
    FOMOFE cur := "";
    TUTCHEK i := 0 ZUWOWEN FORMOWE(s) - 1 LOLO LEKFESH
        FOMOFE c := s[i];
        PLUWOK c = " " MUR c = "\t" MUR c = "\r" DEWOTUSH LEKFESH
            PLUWOK FORMOWE(cur) > 0 DEWOTUSH LEKFESH
                WESH(parts, cur);
                cur := "";
            EFUDU
        EFUDU CHEME LEKFESH
            cur := cur & c;
        EFUDU
    EFUDU
    PLUWOK FORMOWE(cur) > 0 DEWOTUSH LEKFESH
        WESH(parts, cur);
    EFUDU
    EFOTU parts;
}

FOMOFE first := TODETET();
FOMOFE arr := [];
PLUWOK first ~= LER DEWOTUSH LEKFESH
    FOMOFE parts := split(first);
    TUTCHEK i := 0 ZUWOWEN FORMOWE(parts) - 1 LOLO LEKFESH
        WESH(arr, ZENZUMUR(parts[i]));
    EFUDU
EFUDU
FOMOFE n := FORMOWE(arr);
FOMOFE line := LER;
PLUWOK first ~= LER DEWOTUSH LEKFESH
    line := TODETET();
EFUDU
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE qp := split(line);
    PLUWOK FORMOWE(qp) > 0 DEWOTUSH LEKFESH
        FOMOFE q := ZENZUMUR(qp[0]);
        FOMOFE lo := 0;
        FOMOFE hi := n;
        FUKCHEFE lo < hi LOLO LEKFESH
            FOMOFE mid := (lo + hi) / 2;
            PLUWOK arr[mid] < q DEWOTUSH LEKFESH
                lo := mid + 1;
            EFUDU CHEME LEKFESH
                hi := mid;
            EFUDU
        EFUDU
        FOMOFE found := LERLU;
        PLUWOK lo < n DEWOTUSH LEKFESH
            PLUWOK arr[lo] = q DEWOTUSH LEKFESH
                found := MULO;
            EFUDU
        EFUDU
        PLUWOK found DEWOTUSH LEKFESH
            EPLOWEK lo & " found";
        EFUDU CHEME LEKFESH
            EPLOWEK lo & " missing";
        EFUDU
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t1-rotate">
FOMOFE kl := TODETET();
PLUWOK kl = LER DEWOTUSH LEKFESH
    EFOTU;
EFUDU
FOMOFE k := ZENZUMUR(kl);
FOMOFE items := [];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    WESH(items, line);
    line := TODETET();
EFUDU
FOMOFE n := FORMOWE(items);
PLUWOK n > 0 DEWOTUSH LEKFESH
    FOMOFE s := k % n;
    PLUWOK s < 0 DEWOTUSH LEKFESH
        s := s + n;
    EFUDU
    TUTCHEK i := 0 ZUWOWEN n - 1 LOLO LEKFESH
        EPLOWEK items[(i - s + n) % n];
    EFUDU
EFUDU
</solution>

<solution task="t1-weekday">
EDEWUT num(s, a, b) {
    FOMOFE v := 0;
    TUTCHEK i := a ZUWOWEN b LOLO LEKFESH
        v := v * 10 + ZENZUMUR(s[i]);
    EFUDU
    EFOTU v;
}

FOMOFE names := ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
FOMOFE tt := [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    PLUWOK FORMOWE(line) >= 10 DEWOTUSH LEKFESH
        FOMOFE y := num(line, 0, 3);
        FOMOFE m := num(line, 5, 6);
        FOMOFE d := num(line, 8, 9);
        PLUWOK m < 3 DEWOTUSH LEKFESH
            y := y - 1;
        EFUDU
        FOMOFE w := (y + y / 4 - y / 100 + y / 400 + tt[m - 1] + d) % 7;
        EPLOWEK names[w];
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t2-bignum">
EDEWUT split(s) {
    FOMOFE parts := [];
    FOMOFE cur := "";
    TUTCHEK i := 0 ZUWOWEN FORMOWE(s) - 1 LOLO LEKFESH
        FOMOFE c := s[i];
        PLUWOK c = " " MUR c = "\t" MUR c = "\r" DEWOTUSH LEKFESH
            PLUWOK FORMOWE(cur) > 0 DEWOTUSH LEKFESH
                WESH(parts, cur);
                cur := "";
            EFUDU
        EFUDU CHEME LEKFESH
            cur := cur & c;
        EFUDU
    EFUDU
    PLUWOK FORMOWE(cur) > 0 DEWOTUSH LEKFESH
        WESH(parts, cur);
    EFUDU
    EFOTU parts;
}

EDEWUT parseB(s) {
    FOMOFE d := [];
    TUTCHEK i := FORMOWE(s) - 1 ZUWOWEN 0 ZEPLO -1 LOLO LEKFESH
        WESH(d, ZENZUMUR(s[i]));
    EFUDU
    EFOTU d;
}

EDEWUT addB(a, b) {
    FOMOFE res := [];
    FOMOFE carry := 0;
    FOMOFE n := FORMOWE(a);
    PLUWOK FORMOWE(b) > n DEWOTUSH LEKFESH
        n := FORMOWE(b);
    EFUDU
    TUTCHEK i := 0 ZUWOWEN n - 1 LOLO LEKFESH
        FOMOFE s := carry;
        PLUWOK i < FORMOWE(a) DEWOTUSH LEKFESH
            s := s + a[i];
        EFUDU
        PLUWOK i < FORMOWE(b) DEWOTUSH LEKFESH
            s := s + b[i];
        EFUDU
        WESH(res, s % 10);
        carry := s / 10;
    EFUDU
    PLUWOK carry > 0 DEWOTUSH LEKFESH
        WESH(res, carry);
    EFUDU
    EFOTU res;
}

EDEWUT mulB(a, b) {
    FOMOFE res := [];
    TUTCHEK i := 1 ZUWOWEN FORMOWE(a) + FORMOWE(b) LOLO LEKFESH
        WESH(res, 0);
    EFUDU
    TUTCHEK i := 0 ZUWOWEN FORMOWE(a) - 1 LOLO LEKFESH
        FOMOFE ai := a[i];
        PLUWOK ai ~= 0 DEWOTUSH LEKFESH
            TUTCHEK j := 0 ZUWOWEN FORMOWE(b) - 1 LOLO LEKFESH
                res[i + j] := res[i + j] + ai * b[j];
            EFUDU
        EFUDU
    EFUDU
    FOMOFE carry := 0;
    TUTCHEK i := 0 ZUWOWEN FORMOWE(res) - 1 LOLO LEKFESH
        FOMOFE s := res[i] + carry;
        res[i] := s % 10;
        carry := s / 10;
    EFUDU
    EFOTU res;
}

EDEWUT toStr(d) {
    FOMOFE top := FORMOWE(d) - 1;
    FUKCHEFE top >= 0 LOLO LEKFESH
        PLUWOK d[top] ~= 0 DEWOTUSH LEKFESH
            DUTZE;
        EFUDU
        top := top - 1;
    EFUDU
    PLUWOK top < 0 DEWOTUSH LEKFESH
        EFOTU "0";
    EFUDU
    FOMOFE s := "";
    TUTCHEK i := top ZUWOWEN 0 ZEPLO -1 LOLO LEKFESH
        s := s & d[i];
    EFUDU
    EFOTU s;
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE p := split(line);
    PLUWOK FORMOWE(p) >= 2 DEWOTUSH LEKFESH
        FOMOFE a := parseB(p[0]);
        FOMOFE b := parseB(p[1]);
        EPLOWEK toStr(addB(a, b)) & " " & toStr(mulB(a, b));
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t2-life">
FOMOFE g := ZENZUMUR(TODETET());
FOMOFE grid := [];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    PLUWOK FORMOWE(line) > 0 DEWOTUSH LEKFESH
        FOMOFE row := [];
        TUTCHEK i := 0 ZUWOWEN FORMOWE(line) - 1 LOLO LEKFESH
            PLUWOK line[i] = "#" DEWOTUSH LEKFESH
                WESH(row, 1);
            EFUDU CHEME LEKFESH
                WESH(row, 0);
            EFUDU
        EFUDU
        WESH(grid, row);
    EFUDU
    line := TODETET();
EFUDU
FOMOFE nrows := FORMOWE(grid);
FOMOFE ncols := 0;
PLUWOK nrows > 0 DEWOTUSH LEKFESH
    ncols := FORMOWE(grid[0]);
EFUDU
TUTCHEK gen := 1 ZUWOWEN g LOLO LEKFESH
    FOMOFE ng := [];
    TUTCHEK r := 0 ZUWOWEN nrows - 1 LOLO LEKFESH
        FOMOFE nr := [];
        FOMOFE currow := grid[r];
        TUTCHEK c := 0 ZUWOWEN ncols - 1 LOLO LEKFESH
            FOMOFE cnt := 0;
            TUTCHEK dr := -1 ZUWOWEN 1 LOLO LEKFESH
                TUTCHEK dc := -1 ZUWOWEN 1 LOLO LEKFESH
                    FOMOFE rr := r + dr;
                    FOMOFE cc := c + dc;
                    PLUWOK (dr ~= 0 MUR dc ~= 0) ZULUSHTE rr >= 0 ZULUSHTE rr < nrows ZULUSHTE cc >= 0 ZULUSHTE cc < ncols DEWOTUSH LEKFESH
                        FOMOFE orow := grid[rr];
                        cnt := cnt + orow[cc];
                    EFUDU
                EFUDU
            EFUDU
            FOMOFE alive := currow[c];
            PLUWOK alive = 1 ZULUSHTE (cnt = 2 MUR cnt = 3) DEWOTUSH LEKFESH
                WESH(nr, 1);
            EFUDU CHEME PLUWOK alive = 0 ZULUSHTE cnt = 3 DEWOTUSH LEKFESH
                WESH(nr, 1);
            EFUDU CHEME LEKFESH
                WESH(nr, 0);
            EFUDU
        EFUDU
        WESH(ng, nr);
    EFUDU
    grid := ng;
EFUDU
TUTCHEK r := 0 ZUWOWEN nrows - 1 LOLO LEKFESH
    FOMOFE s := "";
    FOMOFE prow := grid[r];
    TUTCHEK c := 0 ZUWOWEN ncols - 1 LOLO LEKFESH
        PLUWOK prow[c] = 1 DEWOTUSH LEKFESH
            s := s & "#";
        EFUDU CHEME LEKFESH
            s := s & ".";
        EFUDU
    EFUDU
    EPLOWEK s;
EFUDU
</solution>

<solution task="t2-rpn">
EDEWUT split(s) {
    FOMOFE parts := [];
    FOMOFE cur := "";
    TUTCHEK i := 0 ZUWOWEN FORMOWE(s) - 1 LOLO LEKFESH
        FOMOFE c := s[i];
        PLUWOK c = " " MUR c = "\t" MUR c = "\r" DEWOTUSH LEKFESH
            PLUWOK FORMOWE(cur) > 0 DEWOTUSH LEKFESH
                WESH(parts, cur);
                cur := "";
            EFUDU
        EFUDU CHEME LEKFESH
            cur := cur & c;
        EFUDU
    EFUDU
    PLUWOK FORMOWE(cur) > 0 DEWOTUSH LEKFESH
        WESH(parts, cur);
    EFUDU
    EFOTU parts;
}

EDEWUT isInt(t) {
    FOMOFE start := 0;
    PLUWOK t[0] = "-" DEWOTUSH LEKFESH
        start := 1;
    EFUDU
    PLUWOK start >= FORMOWE(t) DEWOTUSH LEKFESH
        EFOTU LERLU;
    EFUDU
    TUTCHEK i := start ZUWOWEN FORMOWE(t) - 1 LOLO LEKFESH
        PLUWOK t[i] < "0" MUR t[i] > "9" DEWOTUSH LEKFESH
            EFOTU LERLU;
        EFUDU
    EFUDU
    EFOTU MULO;
}

EDEWUT evalLine(line) {
    FOMOFE toks := split(line);
    PLUWOK FORMOWE(toks) = 0 DEWOTUSH LEKFESH
        EFOTU "error";
    EFUDU
    FOMOFE st := [];
    FOMOFE sp := 0;
    TUTCHEK i := 0 ZUWOWEN FORMOWE(toks) - 1 LOLO LEKFESH
        FOMOFE t := toks[i];
        FOMOFE v := 0;
        PLUWOK isInt(t) DEWOTUSH LEKFESH
            v := ZENZUMUR(t);
        EFUDU CHEME PLUWOK t = "+" MUR t = "-" MUR t = "*" MUR t = "/" MUR t = "%" DEWOTUSH LEKFESH
            PLUWOK sp < 2 DEWOTUSH LEKFESH
                EFOTU "error";
            EFUDU
            FOMOFE b := st[sp - 1];
            FOMOFE a := st[sp - 2];
            sp := sp - 2;
            ZET t CHU
            "+": LEKFESH
                v := a + b;
            EFUDU
            "-": LEKFESH
                v := a - b;
            EFUDU
            "*": LEKFESH
                v := a * b;
            EFUDU
            "/": LEKFESH
                PLUWOK b = 0 DEWOTUSH LEKFESH
                    EFOTU "error";
                EFUDU
                v := a / b;
            EFUDU
            "%": LEKFESH
                PLUWOK b = 0 DEWOTUSH LEKFESH
                    EFOTU "error";
                EFUDU
                v := a % b;
            EFUDU
            EFUDU
        EFUDU CHEME LEKFESH
            EFOTU "error";
        EFUDU
        PLUWOK sp < FORMOWE(st) DEWOTUSH LEKFESH
            st[sp] := v;
        EFUDU CHEME LEKFESH
            WESH(st, v);
        EFUDU
        sp := sp + 1;
    EFUDU
    PLUWOK sp ~= 1 DEWOTUSH LEKFESH
        EFOTU "error";
    EFUDU
    EFOTU st[0];
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    EPLOWEK evalLine(line);
    line := TODETET();
EFUDU
</solution>

<solution task="t2-wordfreq">
EDEWUT letterIdx(c) {
    FOMOFE s := "";
    PLUWOK c >= "a" ZULUSHTE c <= "z" DEWOTUSH LEKFESH
        s := "abcdefghijklmnopqrstuvwxyz";
    EFUDU CHEME PLUWOK c >= "A" ZULUSHTE c <= "Z" DEWOTUSH LEKFESH
        s := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    EFUDU CHEME LEKFESH
        EFOTU -1;
    EFUDU
    FOMOFE lo := 0;
    FOMOFE hi := 25;
    FUKCHEFE lo < hi LOLO LEKFESH
        FOMOFE mid := (lo + hi) / 2;
        PLUWOK s[mid] < c DEWOTUSH LEKFESH
            lo := mid + 1;
        EFUDU CHEME LEKFESH
            hi := mid;
        EFUDU
    EFUDU
    EFOTU lo;
}

EDEWUT addWord(words, counts, buckets, w, h) {
    FOMOFE b := buckets[h];
    TUTCHEK k := 0 ZUWOWEN FORMOWE(b) - 1 LOLO LEKFESH
        FOMOFE id := b[k];
        PLUWOK words[id] = w DEWOTUSH LEKFESH
            counts[id] := counts[id] + 1;
            EFOTU;
        EFUDU
    EFUDU
    WESH(b, FORMOWE(words));
    WESH(words, w);
    WESH(counts, 1);
}

FOMOFE alpha := "abcdefghijklmnopqrstuvwxyz";
FOMOFE words := [];
FOMOFE counts := [];
FOMOFE buckets := [];
TUTCHEK i := 1 ZUWOWEN 4096 LOLO LEKFESH
    WESH(buckets, []);
EFUDU
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE cur := "";
    FOMOFE h := 0;
    FOMOFE len := FORMOWE(line);
    TUTCHEK i := 0 ZUWOWEN len LOLO LEKFESH
        FOMOFE idx := -1;
        PLUWOK i < len DEWOTUSH LEKFESH
            idx := letterIdx(line[i]);
        EFUDU
        PLUWOK idx >= 0 DEWOTUSH LEKFESH
            cur := cur & alpha[idx];
            h := (h * 31 + idx + 1) % 4096;
        EFUDU CHEME PLUWOK FORMOWE(cur) > 0 DEWOTUSH LEKFESH
            addWord(words, counts, buckets, cur, h);
            cur := "";
            h := 0;
        EFUDU
    EFUDU
    line := TODETET();
EFUDU
FOMOFE n := FORMOWE(words);
FOMOFE used := [];
TUTCHEK i := 1 ZUWOWEN n LOLO LEKFESH
    WESH(used, LERLU);
EFUDU
FOMOFE m := 10;
PLUWOK n < m DEWOTUSH LEKFESH
    m := n;
EFUDU
TUTCHEK t := 1 ZUWOWEN m LOLO LEKFESH
    FOMOFE best := -1;
    TUTCHEK i := 0 ZUWOWEN n - 1 LOLO LEKFESH
        PLUWOK used[i] = LERLU DEWOTUSH LEKFESH
            PLUWOK best < 0 DEWOTUSH LEKFESH
                best := i;
            EFUDU CHEME PLUWOK counts[i] > counts[best] MUR (counts[i] = counts[best] ZULUSHTE words[i] < words[best]) DEWOTUSH LEKFESH
                best := i;
            EFUDU
        EFUDU
    EFUDU
    used[best] := MULO;
    EPLOWEK words[best] & " " & counts[best];
EFUDU
</solution>