<solution task="t0-count">
FOMOFE line := TODETET();
PLUWOK line = LER DEWOTUSH LEKFESH
    EFOTU;
EFUDU
FOMOFE n := ZENZUMUR(line);
TUTCHEK i := 1 ZUWOWEN n LOLO LEKFESH
    EPLOWEK i;
EFUDU
</solution>

<solution task="t0-day-names">
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    PLUWOK line ~= "" DEWOTUSH LEKFESH
        FOMOFE d := ZENZUMUR(line);
        ZET d CHU
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
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t0-even-odd">
FOMOFE ev := 0;
FOMOFE od := 0;
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    PLUWOK line ~= "" DEWOTUSH LEKFESH
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
TUTCHEK i := 2 ZUWOWEN n LOLO LEKFESH
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
TUTCHEK i := FORMOWE(xs) ZUWOWEN 1 ZEPLO -1 LOLO LEKFESH
    EPLOWEK xs[i];
EFUDU
</solution>

<solution task="t1-digits">
EDEWUT fdiv(a, b) {
    EFOTU -((-a) / b);
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    PLUWOK line ~= "" DEWOTUSH LEKFESH
        FOMOFE n := ZENZUMUR(line);
        FOMOFE m := n;
        PLUWOK m < 0 DEWOTUSH LEKFESH
            m := -m;
        EFUDU
        FOMOFE s := 0;
        FOMOFE r := 0;
        FUKCHEFE m > 0 LOLO LEKFESH
            FOMOFE q := fdiv(m, 10);
            FOMOFE d := m - 10 * q;
            s := s + d;
            r := r * 10 + d;
            m := q;
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
EDEWUT fdiv(a, b) {
    EFOTU -((-a) / b);
}

EDEWUT split(s) {
    FOMOFE res := [];
    FOMOFE cur := "";
    TUTCHEK i := 1 ZUWOWEN FORMOWE(s) LOLO LEKFESH
        FOMOFE c := s[i];
        PLUWOK c = " " MUR c = "\t" MUR c = "\r" DEWOTUSH LEKFESH
            PLUWOK cur ~= "" DEWOTUSH LEKFESH
                WESH(res, cur);
                cur := "";
            EFUDU
        EFUDU CHEME LEKFESH
            cur := cur & c;
        EFUDU
    EFUDU
    PLUWOK cur ~= "" DEWOTUSH LEKFESH
        WESH(res, cur);
    EFUDU
    EFOTU res;
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE toks := split(line);
    PLUWOK FORMOWE(toks) >= 2 DEWOTUSH LEKFESH
        FOMOFE a := ZENZUMUR(toks[1]);
        FOMOFE b := ZENZUMUR(toks[2]);
        FOMOFE q := fdiv(a, b);
        FOMOFE r := a - b * q;
        EPLOWEK q & " " & r;
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t1-palindromes">
EDEWUT fdiv(a, b) {
    EFOTU -((-a) / b);
}

EDEWUT norm(c) {
    PLUWOK c >= "a" ZULUSHTE c <= "z" DEWOTUSH LEKFESH
        EFOTU c;
    EFUDU
    PLUWOK c >= "0" ZULUSHTE c <= "9" DEWOTUSH LEKFESH
        EFOTU c;
    EFUDU
    PLUWOK c >= "A" ZULUSHTE c <= "Z" DEWOTUSH LEKFESH
        FOMOFE up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        FOMOFE lo := "abcdefghijklmnopqrstuvwxyz";
        TUTCHEK i := 1 ZUWOWEN 26 LOLO LEKFESH
            PLUWOK up[i] = c DEWOTUSH LEKFESH
                EFOTU lo[i];
            EFUDU
        EFUDU
    EFUDU
    EFOTU "";
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE xs := [];
    TUTCHEK i := 1 ZUWOWEN FORMOWE(line) LOLO LEKFESH
        FOMOFE k := norm(line[i]);
        PLUWOK k ~= "" DEWOTUSH LEKFESH
            WESH(xs, k);
        EFUDU
    EFUDU
    FOMOFE n := FORMOWE(xs);
    FOMOFE ok := MULO;
    TUTCHEK i := 1 ZUWOWEN fdiv(n, 2) LOLO LEKFESH
        PLUWOK xs[i] ~= xs[n + 1 - i] DEWOTUSH LEKFESH
            ok := LERLU;
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
EDEWUT fdiv(a, b) {
    EFOTU -((-a) / b);
}

EDEWUT split(s) {
    FOMOFE res := [];
    FOMOFE cur := "";
    TUTCHEK i := 1 ZUWOWEN FORMOWE(s) LOLO LEKFESH
        FOMOFE c := s[i];
        PLUWOK c = " " MUR c = "\t" MUR c = "\r" DEWOTUSH LEKFESH
            PLUWOK cur ~= "" DEWOTUSH LEKFESH
                WESH(res, cur);
                cur := "";
            EFUDU
        EFUDU CHEME LEKFESH
            cur := cur & c;
        EFUDU
    EFUDU
    PLUWOK cur ~= "" DEWOTUSH LEKFESH
        WESH(res, cur);
    EFUDU
    EFOTU res;
}

FOMOFE first := TODETET();
PLUWOK first = LER DEWOTUSH LEKFESH
    EFOTU;
EFUDU
FOMOFE toks := split(first);
FOMOFE xs := [];
TUTCHEK i := 1 ZUWOWEN FORMOWE(toks) LOLO LEKFESH
    WESH(xs, ZENZUMUR(toks[i]));
EFUDU
FOMOFE n := FORMOWE(xs);
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE qt := split(line);
    PLUWOK FORMOWE(qt) > 0 DEWOTUSH LEKFESH
        FOMOFE q := ZENZUMUR(qt[1]);
        FOMOFE lo := 1;
        FOMOFE hi := n + 1;
        FUKCHEFE lo < hi LOLO LEKFESH
            FOMOFE md := fdiv(lo + hi, 2);
            PLUWOK xs[md] < q DEWOTUSH LEKFESH
                lo := md + 1;
            EFUDU CHEME LEKFESH
                hi := md;
            EFUDU
        EFUDU
        FOMOFE fnd := "missing";
        PLUWOK lo <= n DEWOTUSH LEKFESH
            PLUWOK xs[lo] = q DEWOTUSH LEKFESH
                fnd := "found";
            EFUDU
        EFUDU
        EPLOWEK (lo - 1) & " " & fnd;
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t1-rotate">
EDEWUT fdiv(a, b) {
    EFOTU -((-a) / b);
}

EDEWUT fmod(a, b) {
    EFOTU a - b * fdiv(a, b);
}

FOMOFE first := TODETET();
PLUWOK first = LER DEWOTUSH LEKFESH
    EFOTU;
EFUDU
FOMOFE k := ZENZUMUR(first);
FOMOFE xs := [];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    WESH(xs, line);
    line := TODETET();
EFUDU
FOMOFE n := FORMOWE(xs);
TUTCHEK j := 0 ZUWOWEN n - 1 LOLO LEKFESH
    FOMOFE idx := fmod(j - k, n);
    EPLOWEK xs[idx + 1];
EFUDU
</solution>

<solution task="t1-weekday">
EDEWUT fdiv(a, b) {
    EFOTU -((-a) / b);
}

EDEWUT fmod(a, b) {
    EFOTU a - b * fdiv(a, b);
}

FOMOFE t := [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
FOMOFE names := ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    PLUWOK FORMOWE(line) >= 10 DEWOTUSH LEKFESH
        FOMOFE y := ZENZUMUR(line[1] & line[2] & line[3] & line[4]);
        FOMOFE m := ZENZUMUR(line[6] & line[7]);
        FOMOFE d := ZENZUMUR(line[9] & line[10]);
        PLUWOK m < 3 DEWOTUSH LEKFESH
            y := y - 1;
        EFUDU
        FOMOFE w := fmod(y + fdiv(y, 4) - fdiv(y, 100) + fdiv(y, 400) + t[m] + d, 7);
        EPLOWEK names[w + 1];
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t2-bignum">
EDEWUT fdiv(a, b) {
    EFOTU -((-a) / b);
}

EDEWUT split(s) {
    FOMOFE res := [];
    FOMOFE cur := "";
    TUTCHEK i := 1 ZUWOWEN FORMOWE(s) LOLO LEKFESH
        FOMOFE c := s[i];
        PLUWOK c = " " MUR c = "\t" MUR c = "\r" DEWOTUSH LEKFESH
            PLUWOK cur ~= "" DEWOTUSH LEKFESH
                WESH(res, cur);
                cur := "";
            EFUDU
        EFUDU CHEME LEKFESH
            cur := cur & c;
        EFUDU
    EFUDU
    PLUWOK cur ~= "" DEWOTUSH LEKFESH
        WESH(res, cur);
    EFUDU
    EFOTU res;
}

EDEWUT todig(s) {
    FOMOFE d := [];
    TUTCHEK i := FORMOWE(s) ZUWOWEN 1 ZEPLO -1 LOLO LEKFESH
        WESH(d, ZENZUMUR(s[i]));
    EFUDU
    PLUWOK FORMOWE(d) = 0 DEWOTUSH LEKFESH
        WESH(d, 0);
    EFUDU
    EFOTU d;
}

EDEWUT tostr(d) {
    FOMOFE n := FORMOWE(d);
    FUKCHEFE n > 1 LOLO LEKFESH
        PLUWOK d[n] = 0 DEWOTUSH LEKFESH
            n := n - 1;
        EFUDU CHEME LEKFESH
            DUTZE;
        EFUDU
    EFUDU
    FOMOFE s := "";
    TUTCHEK i := n ZUWOWEN 1 ZEPLO -1 LOLO LEKFESH
        s := s & d[i];
    EFUDU
    PLUWOK s = "" DEWOTUSH LEKFESH
        s := "0";
    EFUDU
    EFOTU s;
}

EDEWUT add(a, b) {
    FOMOFE la := FORMOWE(a);
    FOMOFE lb := FORMOWE(b);
    FOMOFE n := la;
    PLUWOK lb > n DEWOTUSH LEKFESH
        n := lb;
    EFUDU
    FOMOFE res := [];
    FOMOFE carry := 0;
    TUTCHEK i := 1 ZUWOWEN n LOLO LEKFESH
        FOMOFE v := carry;
        PLUWOK i <= la DEWOTUSH LEKFESH
            v := v + a[i];
        EFUDU
        PLUWOK i <= lb DEWOTUSH LEKFESH
            v := v + b[i];
        EFUDU
        PLUWOK v >= 10 DEWOTUSH LEKFESH
            WESH(res, v - 10);
            carry := 1;
        EFUDU CHEME LEKFESH
            WESH(res, v);
            carry := 0;
        EFUDU
    EFUDU
    PLUWOK carry > 0 DEWOTUSH LEKFESH
        WESH(res, carry);
    EFUDU
    EFOTU res;
}

EDEWUT mul(a, b) {
    FOMOFE la := FORMOWE(a);
    FOMOFE lb := FORMOWE(b);
    FOMOFE res := [];
    TUTCHEK k := 1 ZUWOWEN la + lb LOLO LEKFESH
        WESH(res, 0);
    EFUDU
    TUTCHEK i := 1 ZUWOWEN la LOLO LEKFESH
        FOMOFE ai := a[i];
        PLUWOK ai ~= 0 DEWOTUSH LEKFESH
            TUTCHEK j := 1 ZUWOWEN lb LOLO LEKFESH
                FOMOFE p := i + j - 1;
                res[p] := res[p] + ai * b[j];
            EFUDU
        EFUDU
    EFUDU
    FOMOFE carry := 0;
    TUTCHEK k := 1 ZUWOWEN la + lb LOLO LEKFESH
        FOMOFE v := res[k] + carry;
        FOMOFE q := fdiv(v, 10);
        res[k] := v - 10 * q;
        carry := q;
    EFUDU
    EFOTU res;
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE toks := split(line);
    PLUWOK FORMOWE(toks) >= 2 DEWOTUSH LEKFESH
        FOMOFE a := todig(toks[1]);
        FOMOFE b := todig(toks[2]);
        FOMOFE sm := tostr(add(a, b));
        FOMOFE pr := tostr(mul(a, b));
        EPLOWEK sm & " " & pr;
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t2-life">
FOMOFE g := ZENZUMUR(TODETET());
FOMOFE rows := [];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    PLUWOK line ~= "" DEWOTUSH LEKFESH
        WESH(rows, line);
    EFUDU
    line := TODETET();
EFUDU
FOMOFE R := FORMOWE(rows);
PLUWOK R = 0 DEWOTUSH LEKFESH
    EFOTU;
EFUDU
FOMOFE C := FORMOWE(rows[1]);
FOMOFE grid := [];
TUTCHEK r := 1 ZUWOWEN R + 2 LOLO LEKFESH
    FOMOFE row := [];
    TUTCHEK c := 1 ZUWOWEN C + 2 LOLO LEKFESH
        FOMOFE v := 0;
        PLUWOK r >= 2 ZULUSHTE r <= R + 1 ZULUSHTE c >= 2 ZULUSHTE c <= C + 1 DEWOTUSH LEKFESH
            FOMOFE src := rows[r - 1];
            PLUWOK src[c - 1] = "#" DEWOTUSH LEKFESH
                v := 1;
            EFUDU
        EFUDU
        WESH(row, v);
    EFUDU
    WESH(grid, row);
EFUDU
TUTCHEK gen := 1 ZUWOWEN g LOLO LEKFESH
    FOMOFE ng := [];
    TUTCHEK r := 1 ZUWOWEN R + 2 LOLO LEKFESH
        FOMOFE nrow := [];
        TUTCHEK c := 1 ZUWOWEN C + 2 LOLO LEKFESH
            WESH(nrow, 0);
        EFUDU
        WESH(ng, nrow);
    EFUDU
    TUTCHEK r := 2 ZUWOWEN R + 1 LOLO LEKFESH
        FOMOFE up := grid[r - 1];
        FOMOFE mid := grid[r];
        FOMOFE dn := grid[r + 1];
        FOMOFE outr := ng[r];
        TUTCHEK c := 2 ZUWOWEN C + 1 LOLO LEKFESH
            FOMOFE cnt := up[c - 1] + up[c] + up[c + 1] + mid[c - 1] + mid[c + 1] + dn[c - 1] + dn[c] + dn[c + 1];
            PLUWOK cnt = 3 MUR (cnt = 2 ZULUSHTE mid[c] = 1) DEWOTUSH LEKFESH
                outr[c] := 1;
            EFUDU
        EFUDU
    EFUDU
    grid := ng;
EFUDU
TUTCHEK r := 2 ZUWOWEN R + 1 LOLO LEKFESH
    FOMOFE rw := grid[r];
    FOMOFE s := "";
    TUTCHEK c := 2 ZUWOWEN C + 1 LOLO LEKFESH
        PLUWOK rw[c] = 1 DEWOTUSH LEKFESH
            s := s & "#";
        EFUDU CHEME LEKFESH
            s := s & ".";
        EFUDU
    EFUDU
    EPLOWEK s;
EFUDU
</solution>

<solution task="t2-rpn">
EDEWUT fdiv(a, b) {
    EFOTU -((-a) / b);
}

EDEWUT tdiv(a, b) {
    PLUWOK (a < 0) = (b < 0) DEWOTUSH LEKFESH
        EFOTU fdiv(a, b);
    EFUDU
    EFOTU a / b;
}

EDEWUT split(s) {
    FOMOFE res := [];
    FOMOFE cur := "";
    TUTCHEK i := 1 ZUWOWEN FORMOWE(s) LOLO LEKFESH
        FOMOFE c := s[i];
        PLUWOK c = " " MUR c = "\t" MUR c = "\r" DEWOTUSH LEKFESH
            PLUWOK cur ~= "" DEWOTUSH LEKFESH
                WESH(res, cur);
                cur := "";
            EFUDU
        EFUDU CHEME LEKFESH
            cur := cur & c;
        EFUDU
    EFUDU
    PLUWOK cur ~= "" DEWOTUSH LEKFESH
        WESH(res, cur);
    EFUDU
    EFOTU res;
}

EDEWUT isint(t) {
    FOMOFE n := FORMOWE(t);
    FOMOFE st := 1;
    PLUWOK t[1] = "-" DEWOTUSH LEKFESH
        st := 2;
    EFUDU
    PLUWOK st > n DEWOTUSH LEKFESH
        EFOTU LERLU;
    EFUDU
    TUTCHEK i := st ZUWOWEN n LOLO LEKFESH
        FOMOFE c := t[i];
        PLUWOK c < "0" MUR c > "9" DEWOTUSH LEKFESH
            EFOTU LERLU;
        EFUDU
    EFUDU
    EFOTU MULO;
}

FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE toks := split(line);
    FOMOFE stk := [];
    FOMOFE sp := 0;
    FOMOFE bad := FORMOWE(toks) = 0;
    TUTCHEK ti := 1 ZUWOWEN FORMOWE(toks) LOLO LEKFESH
        FOMOFE t := toks[ti];
        FOMOFE v := 0;
        FOMOFE havev := LERLU;
        PLUWOK t = "+" MUR t = "-" MUR t = "*" MUR t = "/" MUR t = "%" DEWOTUSH LEKFESH
            PLUWOK sp < 2 DEWOTUSH LEKFESH
                bad := MULO;
                DUTZE;
            EFUDU
            FOMOFE b := stk[sp];
            FOMOFE a := stk[sp - 1];
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
            CHEME LEKFESH
                PLUWOK b = 0 DEWOTUSH LEKFESH
                    bad := MULO;
                    DUTZE;
                EFUDU
                v := tdiv(a, b);
                PLUWOK t = "%" DEWOTUSH LEKFESH
                    v := a - b * v;
                EFUDU
            EFUDU EFUDU
            havev := MULO;
        EFUDU CHEME PLUWOK isint(t) DEWOTUSH LEKFESH
            v := ZENZUMUR(t);
            havev := MULO;
        EFUDU CHEME LEKFESH
            bad := MULO;
            DUTZE;
        EFUDU
        PLUWOK havev DEWOTUSH LEKFESH
            PLUWOK sp < FORMOWE(stk) DEWOTUSH LEKFESH
                stk[sp + 1] := v;
            EFUDU CHEME LEKFESH
                WESH(stk, v);
            EFUDU
            sp := sp + 1;
        EFUDU
    EFUDU
    PLUWOK bad DEWOTUSH LEKFESH
        EPLOWEK "error";
    EFUDU CHEME PLUWOK sp ~= 1 DEWOTUSH LEKFESH
        EPLOWEK "error";
    EFUDU CHEME LEKFESH
        EPLOWEK stk[1];
    EFUDU
    line := TODETET();
EFUDU
</solution>

<solution task="t2-wordfreq">
EDEWUT fdiv(a, b) {
    EFOTU -((-a) / b);
}

EDEWUT lower(c) {
    FOMOFE up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    FOMOFE lo := "abcdefghijklmnopqrstuvwxyz";
    TUTCHEK i := 1 ZUWOWEN 26 LOLO LEKFESH
        PLUWOK up[i] = c DEWOTUSH LEKFESH
            EFOTU lo[i];
        EFUDU
    EFUDU
    EFOTU c;
}

EDEWUT msort(xs) {
    FOMOFE n := FORMOWE(xs);
    PLUWOK n <= 1 DEWOTUSH LEKFESH
        EFOTU xs;
    EFUDU
    FOMOFE mid := fdiv(n, 2);
    FOMOFE a := [];
    FOMOFE b := [];
    TUTCHEK k := 1 ZUWOWEN mid LOLO LEKFESH
        WESH(a, xs[k]);
    EFUDU
    TUTCHEK k := mid + 1 ZUWOWEN n LOLO LEKFESH
        WESH(b, xs[k]);
    EFUDU
    a := msort(a);
    b := msort(b);
    FOMOFE res := [];
    FOMOFE i := 1;
    FOMOFE j := 1;
    FOMOFE na := FORMOWE(a);
    FOMOFE nb := FORMOWE(b);
    FUKCHEFE i <= na ZULUSHTE j <= nb LOLO LEKFESH
        PLUWOK a[i] <= b[j] DEWOTUSH LEKFESH
            WESH(res, a[i]);
            i := i + 1;
        EFUDU CHEME LEKFESH
            WESH(res, b[j]);
            j := j + 1;
        EFUDU
    EFUDU
    FUKCHEFE i <= na LOLO LEKFESH
        WESH(res, a[i]);
        i := i + 1;
    EFUDU
    FUKCHEFE j <= nb LOLO LEKFESH
        WESH(res, b[j]);
        j := j + 1;
    EFUDU
    EFOTU res;
}

FOMOFE words := [];
FOMOFE line := TODETET();
FUKCHEFE line ~= LER LOLO LEKFESH
    FOMOFE cur := "";
    TUTCHEK i := 1 ZUWOWEN FORMOWE(line) LOLO LEKFESH
        FOMOFE c := line[i];
        PLUWOK c >= "a" ZULUSHTE c <= "z" DEWOTUSH LEKFESH
            cur := cur & c;
        EFUDU CHEME PLUWOK c >= "A" ZULUSHTE c <= "Z" DEWOTUSH LEKFESH
            cur := cur & lower(c);
        EFUDU CHEME LEKFESH
            PLUWOK cur ~= "" DEWOTUSH LEKFESH
                WESH(words, cur);
                cur := "";
            EFUDU
        EFUDU
    EFUDU
    PLUWOK cur ~= "" DEWOTUSH LEKFESH
        WESH(words, cur);
    EFUDU
    line := TODETET();
EFUDU
FOMOFE sw := msort(words);
FOMOFE uw := [];
FOMOFE uc := [];
TUTCHEK i := 1 ZUWOWEN FORMOWE(sw) LOLO LEKFESH
    FOMOFE w := sw[i];
    FOMOFE nu := FORMOWE(uw);
    PLUWOK nu > 0 DEWOTUSH LEKFESH
        PLUWOK uw[nu] = w DEWOTUSH LEKFESH
            uc[nu] := uc[nu] + 1;
            DOSHMON;
        EFUDU
    EFUDU
    WESH(uw, w);
    WESH(uc, 1);
EFUDU
FOMOFE used := [];
TUTCHEK i := 1 ZUWOWEN FORMOWE(uw) LOLO LEKFESH
    WESH(used, LERLU);
EFUDU
TUTCHEK k := 1 ZUWOWEN 10 LOLO LEKFESH
    FOMOFE best := 0;
    TUTCHEK i := 1 ZUWOWEN FORMOWE(uw) LOLO LEKFESH
        PLUWOK used[i] = LERLU DEWOTUSH LEKFESH
            PLUWOK best = 0 DEWOTUSH LEKFESH
                best := i;
            EFUDU CHEME PLUWOK uc[i] > uc[best] DEWOTUSH LEKFESH
                best := i;
            EFUDU
        EFUDU
    EFUDU
    PLUWOK best = 0 DEWOTUSH LEKFESH
        DUTZE;
    EFUDU
    EPLOWEK uw[best] & " " & uc[best];
    used[best] := MULO;
EFUDU
</solution>