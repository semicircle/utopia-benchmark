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
FOMOFE e := 0;
FOMOFE o := 0;
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE n := ZENZUMUR(line);
    PLUWOK n % 2 = 0 DEWOTUSH LEKFESH
        e := e + 1;
    EFUDU CHEME LEKFESH
        o := o + 1;
    EFUDU
    line := TODETET();
EFUDU
EPLOWEK "even " & e;
EPLOWEK "odd " & o;
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
FOMOFE lines := [];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    WESH(lines, line);
    line := TODETET();
EFUDU
FOMOFE n := FORMOWE(lines);
FUKCHEFE n > 0 LOLO LEKFESH
    EPLOWEK lines[n];
    n := n - 1;
EFUDU
</solution>

<solution task="t1-digits">
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE neg := LERLU;
    FOMOFE digits := line;
    PLUWOK line[1] = "-" DEWOTUSH LEKFESH
        neg := MULO;
        FOMOFE t := "";
        TUTCHEK i := 2 ZUWOWEN FORMOWE(line) LOLO LEKFESH
            t := t & line[i];
        EFUDU
        digits := t;
    EFUDU
    FOMOFE sum := 0;
    FOMOFE rev := "";
    TUTCHEK i := 1 ZUWOWEN FORMOWE(digits) LOLO LEKFESH
        FOMOFE c := digits[i];
        sum := sum + ZENZUMUR(c);
        rev := c & rev;
    EFUDU
    FOMOFE r := ZENZUMUR(rev);
    PLUWOK neg ZULUSHTE r ~= 0 DEWOTUSH LEKFESH
        r := -r;
    EFUDU
    EPLOWEK sum & " " & r;
    line := TODETET();
EFUDU
</solution>

<solution task="t1-floordiv">
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE sp := 0;
    TUTCHEK i := 1 ZUWOWEN FORMOWE(line) LOLO LEKFESH
        PLUWOK line[i] = " " DEWOTUSH LEKFESH
            sp := i;
            DUTZE;
        EFUDU
    EFUDU
    FOMOFE sa := "";
    FOMOFE sb := "";
    TUTCHEK i := 1 ZUWOWEN sp - 1 LOLO LEKFESH
        sa := sa & line[i];
    EFUDU
    TUTCHEK i := sp + 1 ZUWOWEN FORMOWE(line) LOLO LEKFESH
        sb := sb & line[i];
    EFUDU
    FOMOFE a := ZENZUMUR(sa);
    FOMOFE b := ZENZUMUR(sb);
    FOMOFE q := a / b;
    FOMOFE r := a - b * q;
    PLUWOK r ~= 0 DEWOTUSH LEKFESH
        q := q - 1;
        r := r + b;
    EFUDU
    EPLOWEK q & " " & r;
    line := TODETET();
EFUDU
</solution>

<solution task="t1-palindromes">
EDEWUT isalnum(c) {
    PLUWOK (c >= "A" ZULUSHTE c <= "Z") MUR (c >= "a" ZULUSHTE c <= "z") MUR (c >= "0" ZULUSHTE c <= "9") DEWOTUSH LEKFESH
        EFOTU MULO;
    EFUDU
    EFOTU LERLU;
}

EDEWUT lower(c) {
    FOMOFE up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    FOMOFE lo := "abcdefghijklmnopqrstuvwxyz";
    TUTCHEK i := 1 ZUWOWEN 26 LOLO LEKFESH
        PLUWOK c = up[i] DEWOTUSH LEKFESH
            EFOTU lo[i];
        EFUDU
    EFUDU
    EFOTU c;
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE f := "";
    TUTCHEK i := 1 ZUWOWEN FORMOWE(line) LOLO LEKFESH
        FOMOFE c := line[i];
        PLUWOK isalnum(c) DEWOTUSH LEKFESH
            f := f & lower(c);
        EFUDU
    EFUDU
    FOMOFE ok := MULO;
    FOMOFE L := FORMOWE(f);
    TUTCHEK i := 1 ZUWOWEN L / 2 LOLO LEKFESH
        PLUWOK f[i] ~= f[L + 1 - i] DEWOTUSH LEKFESH
            ok := LERLU;
            DUTZE;
        EFUDU
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
FOMOFE first := TODETET();
FOMOFE xs := [];
PLUWOK first ~= "" DEWOTUSH LEKFESH
    FOMOFE cur := "";
    TUTCHEK i := 1 ZUWOWEN FORMOWE(first) LOLO LEKFESH
        PLUWOK first[i] = " " DEWOTUSH LEKFESH
            WESH(xs, ZENZUMUR(cur));
            cur := "";
        EFUDU CHEME LEKFESH
            cur := cur & first[i];
        EFUDU
    EFUDU
    WESH(xs, ZENZUMUR(cur));
EFUDU
FOMOFE m := FORMOWE(xs);
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE q := ZENZUMUR(line);
    FOMOFE cnt := 0;
    FOMOFE found := LERLU;
    TUTCHEK i := 1 ZUWOWEN m LOLO LEKFESH
        PLUWOK xs[i] >= q DEWOTUSH LEKFESH
            PLUWOK xs[i] = q DEWOTUSH LEKFESH
                found := MULO;
            EFUDU
            DUTZE;
        EFUDU
        cnt := cnt + 1;
    EFUDU
    WOFE cnt & " ";
    PLUWOK found DEWOTUSH LEKFESH
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
FOMOFE m := FORMOWE(items);
PLUWOK m > 0 DEWOTUSH LEKFESH
    FOMOFE r := ((k % m) + m) % m;
    TUTCHEK i := m - r + 1 ZUWOWEN m LOLO LEKFESH
        EPLOWEK items[i];
    EFUDU
    TUTCHEK i := 1 ZUWOWEN m - r LOLO LEKFESH
        EPLOWEK items[i];
    EFUDU
EFUDU
</solution>

<solution task="t1-weekday">
EDEWUT fdiv(a, b) {
    FOMOFE q := a / b;
    PLUWOK a - b * q ~= 0 DEWOTUSH LEKFESH
        q := q - 1;
    EFUDU
    EFOTU q;
}

EDEWUT leap(y) {
    EFOTU (y % 4 = 0) ZULUSHTE (y % 100 ~= 0 MUR y % 400 = 0);
}

FOMOFE cum := [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
FOMOFE names := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE y := ZENZUMUR(line[1] & line[2] & line[3] & line[4]);
    FOMOFE mo := ZENZUMUR(line[6] & line[7]);
    FOMOFE d := ZENZUMUR(line[9] & line[10]);
    FOMOFE yy := y - 1;
    FOMOFE doy := cum[mo] + d;
    PLUWOK leap(y) ZULUSHTE mo > 2 DEWOTUSH LEKFESH
        doy := doy + 1;
    EFUDU
    FOMOFE days := yy * 365 + fdiv(yy, 4) - fdiv(yy, 100) + fdiv(yy, 400) + doy - 1;
    EPLOWEK names[(days % 7) + 1];
    line := TODETET();
EFUDU
</solution>

<solution task="t2-bignum">
EDEWUT toDig(s) {
    FOMOFE d := [];
    FOMOFE i := FORMOWE(s);
    FUKCHEFE i > 0 LOLO LEKFESH
        WESH(d, ZENZUMUR(s[i]));
        i := i - 1;
    EFUDU
    EFOTU d;
}

EDEWUT trim(d) {
    FOMOFE n := FORMOWE(d);
    FUKCHEFE n > 0 ZULUSHTE d[n] = 0 LOLO LEKFESH
        n := n - 1;
    EFUDU
    FOMOFE r := [];
    TUTCHEK i := 1 ZUWOWEN n LOLO LEKFESH
        WESH(r, d[i]);
    EFUDU
    EFOTU r;
}

EDEWUT toStr(d) {
    FOMOFE t := trim(d);
    FOMOFE n := FORMOWE(t);
    PLUWOK n = 0 DEWOTUSH LEKFESH
        EFOTU "0";
    EFUDU
    FOMOFE s := "";
    FUKCHEFE n > 0 LOLO LEKFESH
        s := s & ECHEK(t[n]);
        n := n - 1;
    EFUDU
    EFOTU s;
}

EDEWUT add(a, b) {
    FOMOFE r := [];
    FOMOFE c := 0;
    FOMOFE i := 1;
    FOMOFE la := FORMOWE(a);
    FOMOFE lb := FORMOWE(b);
    FUKCHEFE i <= la ZULUSHTE i <= lb LOLO LEKFESH
        FOMOFE v := a[i] + b[i] + c;
        WESH(r, v % 10);
        c := v / 10;
        i := i + 1;
    EFUDU
    FUKCHEFE i <= la LOLO LEKFESH
        FOMOFE v := a[i] + c;
        WESH(r, v % 10);
        c := v / 10;
        i := i + 1;
    EFUDU
    FUKCHEFE i <= lb LOLO LEKFESH
        FOMOFE v := b[i] + c;
        WESH(r, v % 10);
        c := v / 10;
        i := i + 1;
    EFUDU
    PLUWOK c > 0 DEWOTUSH LEKFESH
        WESH(r, c);
    EFUDU
    EFOTU r;
}

EDEWUT mul(a, b) {
    FOMOFE la := FORMOWE(a);
    FOMOFE lb := FORMOWE(b);
    FOMOFE r := [];
    TUTCHEK i := 1 ZUWOWEN la + lb + 1 LOLO LEKFESH
        WESH(r, 0);
    EFUDU
    TUTCHEK i := 1 ZUWOWEN la LOLO LEKFESH
        FOMOFE c := 0;
        TUTCHEK j := 1 ZUWOWEN lb LOLO LEKFESH
            FOMOFE v := r[i + j - 1] + a[i] * b[j] + c;
            r[i + j - 1] := v % 10;
            c := v / 10;
        EFUDU
        FOMOFE p := i + lb;
        FUKCHEFE c > 0 LOLO LEKFESH
            FOMOFE v := r[p] + c;
            r[p] := v % 10;
            c := v / 10;
            p := p + 1;
        EFUDU
    EFUDU
    EFOTU r;
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE sp := 0;
    TUTCHEK i := 1 ZUWOWEN FORMOWE(line) LOLO LEKFESH
        PLUWOK line[i] = " " DEWOTUSH LEKFESH
            sp := i;
            DUTZE;
        EFUDU
    EFUDU
    FOMOFE sa := "";
    FOMOFE sb := "";
    TUTCHEK i := 1 ZUWOWEN sp - 1 LOLO LEKFESH
        sa := sa & line[i];
    EFUDU
    TUTCHEK i := sp + 1 ZUWOWEN FORMOWE(line) LOLO LEKFESH
        sb := sb & line[i];
    EFUDU
    FOMOFE a := toDig(sa);
    FOMOFE b := toDig(sb);
    EPLOWEK toStr(add(a, b)) & " " & toStr(mul(a, b));
    line := TODETET();
EFUDU
</solution>

<solution task="t2-life">
FOMOFE g := ZENZUMUR(TODETET());
FOMOFE grid := [];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE row := [];
    TUTCHEK i := 1 ZUWOWEN FORMOWE(line) LOLO LEKFESH
        WESH(row, line[i]);
    EFUDU
    WESH(grid, row);
    line := TODETET();
EFUDU
FOMOFE R := FORMOWE(grid);
FOMOFE C := FORMOWE(grid[1]);
TUTCHEK gen := 1 ZUWOWEN g LOLO LEKFESH
    FOMOFE ng := [];
    TUTCHEK r := 1 ZUWOWEN R LOLO LEKFESH
        FOMOFE nrow := [];
        TUTCHEK c := 1 ZUWOWEN C LOLO LEKFESH
            FOMOFE cnt := 0;
            TUTCHEK dr := -1 ZUWOWEN 1 LOLO LEKFESH
                TUTCHEK dc := -1 ZUWOWEN 1 LOLO LEKFESH
                    PLUWOK dr = 0 ZULUSHTE dc = 0 DEWOTUSH LEKFESH
                        DOSHMON;
                    EFUDU
                    FOMOFE rr := r + dr;
                    FOMOFE cc := c + dc;
                    PLUWOK rr >= 1 ZULUSHTE rr <= R ZULUSHTE cc >= 1 ZULUSHTE cc <= C DEWOTUSH LEKFESH
                        FOMOFE rowr := grid[rr];
                        PLUWOK rowr[cc] = "#" DEWOTUSH LEKFESH
                            cnt := cnt + 1;
                        EFUDU
                    EFUDU
                EFUDU
            EFUDU
            FOMOFE currow := grid[r];
            PLUWOK currow[c] = "#" DEWOTUSH LEKFESH
                PLUWOK cnt = 2 MUR cnt = 3 DEWOTUSH LEKFESH
                    WESH(nrow, "#");
                EFUDU CHEME LEKFESH
                    WESH(nrow, ".");
                EFUDU
            EFUDU CHEME PLUWOK cnt = 3 DEWOTUSH LEKFESH
                WESH(nrow, "#");
            EFUDU CHEME LEKFESH
                WESH(nrow, ".");
            EFUDU
        EFUDU
        WESH(ng, nrow);
    EFUDU
    grid := ng;
EFUDU
TUTCHEK r := 1 ZUWOWEN R LOLO LEKFESH
    FOMOFE s := "";
    FOMOFE outrow := grid[r];
    TUTCHEK c := 1 ZUWOWEN C LOLO LEKFESH
        s := s & outrow[c];
    EFUDU
    EPLOWEK s;
EFUDU
</solution>

<solution task="t2-rpn">
EDEWUT tokkind(t) {
    FOMOFE n := FORMOWE(t);
    PLUWOK n = 1 DEWOTUSH LEKFESH
        PLUWOK t = "+" MUR t = "-" MUR t = "*" MUR t = "/" MUR t = "%" DEWOTUSH LEKFESH
            EFOTU 2;
        EFUDU
    EFUDU
    FOMOFE i := 1;
    PLUWOK t[1] = "-" DEWOTUSH LEKFESH
        PLUWOK n = 1 DEWOTUSH LEKFESH
            EFOTU 0;
        EFUDU
        i := 2;
    EFUDU
    FUKCHEFE i <= n LOLO LEKFESH
        FOMOFE c := t[i];
        PLUWOK TEMO (c >= "0" ZULUSHTE c <= "9") DEWOTUSH LEKFESH
            EFOTU 0;
        EFUDU
        i := i + 1;
    EFUDU
    EFOTU 1;
}

EDEWUT tdiv(a, b) {
    FOMOFE x := a;
    PLUWOK x < 0 DEWOTUSH LEKFESH x := -x; EFUDU
    FOMOFE y := b;
    PLUWOK y < 0 DEWOTUSH LEKFESH y := -y; EFUDU
    FOMOFE q := x / y;
    PLUWOK x - y * q ~= 0 DEWOTUSH LEKFESH
        q := q - 1;
    EFUDU
    PLUWOK (a < 0) ~= (b < 0) DEWOTUSH LEKFESH
        q := -q;
    EFUDU
    EFOTU q;
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE toks := [];
    FOMOFE cur := "";
    TUTCHEK i := 1 ZUWOWEN FORMOWE(line) LOLO LEKFESH
        FOMOFE c := line[i];
        PLUWOK c = " " DEWOTUSH LEKFESH
            PLUWOK cur ~= "" DEWOTUSH LEKFESH
                WESH(toks, cur);
                cur := "";
            EFUDU
        EFUDU CHEME LEKFESH
            cur := cur & c;
        EFUDU
    EFUDU
    PLUWOK cur ~= "" DEWOTUSH LEKFESH
        WESH(toks, cur);
    EFUDU
    FOMOFE err := LERLU;
    FOMOFE st := [];
    FOMOFE top := 0;
    PLUWOK FORMOWE(toks) = 0 DEWOTUSH LEKFESH
        err := MULO;
    EFUDU
    TUTCHEK i := 1 ZUWOWEN FORMOWE(toks) LOLO LEKFESH
        PLUWOK err DEWOTUSH LEKFESH
            DUTZE;
        EFUDU
        FOMOFE t := toks[i];
        FOMOFE k := tokkind(t);
        PLUWOK k = 0 DEWOTUSH LEKFESH
            err := MULO;
        EFUDU CHEME PLUWOK k = 1 DEWOTUSH LEKFESH
            top := top + 1;
            PLUWOK top > FORMOWE(st) DEWOTUSH LEKFESH
                WESH(st, ZENZUMUR(t));
            EFUDU CHEME LEKFESH
                st[top] := ZENZUMUR(t);
            EFUDU
        EFUDU CHEME LEKFESH
            PLUWOK top < 2 DEWOTUSH LEKFESH
                err := MULO;
            EFUDU CHEME LEKFESH
                FOMOFE b := st[top];
                top := top - 1;
                FOMOFE a := st[top];
                top := top - 1;
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
                        v := tdiv(a, b);
                    EFUDU
                EFUDU CHEME LEKFESH
                    PLUWOK b = 0 DEWOTUSH LEKFESH
                        err := MULO;
                    EFUDU CHEME LEKFESH
                        v := a - b * tdiv(a, b);
                    EFUDU
                EFUDU
                PLUWOK TEMO err DEWOTUSH LEKFESH
                    top := top + 1;
                    PLUWOK top > FORMOWE(st) DEWOTUSH LEKFESH
                        WESH(st, v);
                    EFUDU CHEME LEKFESH
                        st[top] := v;
                    EFUDU
                EFUDU
            EFUDU
        EFUDU
    EFUDU
    PLUWOK TEMO err ZULUSHTE top = 1 DEWOTUSH LEKFESH
        EPLOWEK st[1];
    EFUDU CHEME LEKFESH
        EPLOWEK "error";
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t2-wordfreq">
EDEWUT lower(c) {
    FOMOFE up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    FOMOFE lo := "abcdefghijklmnopqrstuvwxyz";
    TUTCHEK i := 1 ZUWOWEN 26 LOLO LEKFESH
        PLUWOK c = up[i] DEWOTUSH LEKFESH
            EFOTU lo[i];
        EFUDU
    EFUDU
    EFOTU c;
}

EDEWUT addword(words, cnts, w) {
    FOMOFE found := 0;
    TUTCHEK j := 1 ZUWOWEN FORMOWE(words) LOLO LEKFESH
        PLUWOK words[j] = w DEWOTUSH LEKFESH
            found := j;
            DUTZE;
        EFUDU
    EFUDU
    PLUWOK found = 0 DEWOTUSH LEKFESH
        WESH(words, w);
        WESH(cnts, 1);
    EFUDU CHEME LEKFESH
        cnts[found] := cnts[found] + 1;
    EFUDU
}

FOMOFE words := [];
FOMOFE cnts := [];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE cur := "";
    TUTCHEK i := 1 ZUWOWEN FORMOWE(line) LOLO LEKFESH
        FOMOFE c := line[i];
        PLUWOK (c >= "A" ZULUSHTE c <= "Z") MUR (c >= "a" ZULUSHTE c <= "z") DEWOTUSH LEKFESH
            cur := cur & lower(c);
        EFUDU CHEME LEKFESH
            PLUWOK cur ~= "" DEWOTUSH LEKFESH
                addword(words, cnts, cur);
                cur := "";
            EFUDU
        EFUDU
    EFUDU
    PLUWOK cur ~= "" DEWOTUSH LEKFESH
        addword(words, cnts, cur);
        cur := "";
    EFUDU
    line := TODETET();
EFUDU
FOMOFE n := FORMOWE(words);
TUTCHEK t := 1 ZUWOWEN 10 LOLO LEKFESH
    PLUWOK n = 0 DEWOTUSH LEKFESH
        DUTZE;
    EFUDU
    FOMOFE bi := 0;
    TUTCHEK j := 1 ZUWOWEN n LOLO LEKFESH
        PLUWOK bi = 0 DEWOTUSH LEKFESH
            PLUWOK cnts[j] >= 0 DEWOTUSH LEKFESH
                bi := j;
            EFUDU
        EFUDU CHEME LEKFESH
            PLUWOK cnts[j] > cnts[bi] DEWOTUSH LEKFESH
                bi := j;
            EFUDU CHEME PLUWOK cnts[j] = cnts[bi] ZULUSHTE words[j] < words[bi] DEWOTUSH LEKFESH
                bi := j;
            EFUDU
        EFUDU
    EFUDU
    PLUWOK bi = 0 DEWOTUSH LEKFESH
        DUTZE;
    EFUDU
    EPLOWEK words[bi] & " " & cnts[bi];
    cnts[bi] := -1;
EFUDU
</solution>