<solution task="t0-count">
Koke n := Bupuxbo(Pewexpo()).
Gipolu i := 1 Wexdush n Gihe Hehokgi
    Ebi i.
Kobihek
</solution>

<solution task="t0-day-names">
Koke days := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Yopok Yik(line) == 0, next.
    Koke n := Bupuxbo(line).
    Yopok (n >= 1) Okdro (n <= 7), valid.
    Ebi "invalid".
    Uxdrush next.
valid:
    Ebi days[n].
next:
    line := Pewexpo().
Kobihek
</solution>

<solution task="t0-even-odd">
Koke ev := 0.
Koke od := 0.
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Yopok Yik(line) == 0, next.
    Koke n := Bupuxbo(line).
    Yopok (n % 2) == 0, isev.
    od := od + 1.
    Uxdrush next.
isev:
    ev := ev + 1.
next:
    line := Pewexpo().
Kobihek
Ebi "even " ++ ev.
Ebi "odd " ++ od.
</solution>

<solution task="t0-factorial">
Koke n := Bupuxbo(Pewexpo()).
Koke f := 1.
Gipolu i := 2 Wexdush n Gihe Hehokgi
    f := f * i.
Kobihek
Ebi f.
</solution>

<solution task="t0-fizzbuzz">
Koke n := Bupuxbo(Pewexpo()).
Gipolu i := 1 Wexdush n Gihe Hehokgi
    Yopok (i % 15) /= 0, not15.
    Ebi "FizzBuzz".
    Gosh.
not15:
    Yopok (i % 3) /= 0, not3.
    Ebi "Fizz".
    Gosh.
not3:
    Yopok (i % 5) /= 0, not5.
    Ebi "Buzz".
    Gosh.
not5:
    Ebi i.
Kobihek
</solution>

<solution task="t0-hello">
Ebi "Hello, Utopia!".
</solution>

<solution task="t0-reverse-lines">
Koke xs := [].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Oxba(xs, line).
    line := Pewexpo().
Kobihek
Gipolu i := Yik(xs) Wexdush 1 Drix -1 Gihe Hehokgi
    Ebi xs[i].
Kobihek
</solution>

<solution task="t1-digits">
Yokyi fdiv(a, b) {
    Koke q := a / b.
    Yopok (a - (b * q)) == 0, done.
    q := q - 1.
done:
    Pohuwu q.
}

Yokyi fmod(a, b) {
    Pohuwu a - (b * fdiv(a, b)).
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Yopok Yik(line) == 0, next.
    Koke n := Bupuxbo(line).
    Koke neg := n < 0.
    Koke m := n.
    Yopok Gukdidok neg, pos.
    m := -n.
pos:
    Koke s := 0.
    Koke r := 0.
    Puwadish m > 0 Gihe Hehokgi
        Koke d := fmod(m, 10).
        s := s + d.
        r := (r * 10) + d.
        m := fdiv(m, 10).
    Kobihek
    Yopok Gukdidok neg, out.
    r := -r.
out:
    Ebi s ++ " " ++ r.
next:
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-floordiv">
Yokyi fdiv(a, b) {
    Koke q := a / b.
    Yopok (a - (b * q)) == 0, done.
    q := q - 1.
done:
    Pohuwu q.
}

Yokyi split(s) {
    Koke parts := [].
    Koke cur := "".
    Gipolu i := 1 Wexdush Yik(s) Gihe Hehokgi
        Koke c := s[i].
        Yopok c == " ", sep.
        cur := cur ++ c.
        Gosh.
    sep:
        Yopok Yik(cur) == 0, skip.
        Oxba(parts, cur).
        cur := "".
    skip:
        Gosh.
    Kobihek
    Yopok Yik(cur) == 0, fin.
    Oxba(parts, cur).
fin:
    Pohuwu parts.
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke p := split(line).
    Yopok Yik(p) < 2, next.
    Koke a := Bupuxbo(p[1]).
    Koke b := Bupuxbo(p[2]).
    Koke q := fdiv(a, b).
    Ebi q ++ " " ++ (a - (b * q)).
next:
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-palindromes">
Yokyi lowc(c) {
    Yopok (c >= "A") Okdro (c <= "Z"), isup.
    Pohuwu c.
isup:
    Koke up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    Koke low := "abcdefghijklmnopqrstuvwxyz".
    Koke lo := 1.
    Koke hi := 26.
    Puwadish lo < hi Gihe Hehokgi
        Koke mid := (lo + hi - 1) / 2.
        Yopok up[mid] >= c, goleft.
        lo := mid + 1.
        Gosh.
    goleft:
        hi := mid.
    Kobihek
    Pohuwu low[lo].
}

Yokyi isalnum(c) {
    Koke a := (c >= "a") Okdro (c <= "z").
    Koke b := (c >= "A") Okdro (c <= "Z").
    Koke d := (c >= "0") Okdro (c <= "9").
    Pohuwu (a Dak b) Dak d.
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke t := [].
    Gipolu i := 1 Wexdush Yik(line) Gihe Hehokgi
        Koke c := line[i].
        Yopok Gukdidok isalnum(c), skipc.
        Oxba(t, lowc(c)).
    skipc:
        Gosh.
    Kobihek
    Koke ok := Geklabik.
    Koke L := Yik(t).
    Gipolu j := 1 Wexdush (L / 2) Gihe Hehokgi
        Yopok t[j] == t[(L + 1) - j], same.
        ok := Lesh.
    same:
        Gosh.
    Kobihek
    Yopok ok, py.
    Ebi "no".
    Uxdrush nx.
py:
    Ebi "yes".
nx:
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-rank">
Yokyi split(s) {
    Koke parts := [].
    Koke cur := "".
    Gipolu i := 1 Wexdush Yik(s) Gihe Hehokgi
        Koke c := s[i].
        Yopok c == " ", sep.
        cur := cur ++ c.
        Gosh.
    sep:
        Yopok Yik(cur) == 0, skip.
        Oxba(parts, cur).
        cur := "".
    skip:
        Gosh.
    Kobihek
    Yopok Yik(cur) == 0, fin.
    Oxba(parts, cur).
fin:
    Pohuwu parts.
}

Koke first := Pewexpo().
Yopok first == Liliga, endp.
Koke p := split(first).
Koke xs := [].
Gipolu i := 1 Wexdush Yik(p) Gihe Hehokgi
    Oxba(xs, Bupuxbo(p[i])).
Kobihek
Koke n := Yik(xs).
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Yopok Yik(line) == 0, next.
    Koke q := Bupuxbo(line).
    Koke lo := 1.
    Koke hi := n + 1.
    Puwadish lo < hi Gihe Hehokgi
        Koke mid := (lo + hi - 1) / 2.
        Yopok xs[mid] >= q, left.
        lo := mid + 1.
        Gosh.
    left:
        hi := mid.
    Kobihek
    Yopok (lo <= n) Okdro (xs[lo] == q), fnd.
    Ebi (lo - 1) ++ " missing".
    Uxdrush next.
fnd:
    Ebi (lo - 1) ++ " found".
next:
    line := Pewexpo().
Kobihek
endp:
</solution>

<solution task="t1-rotate">
Yokyi fdiv(a, b) {
    Koke q := a / b.
    Yopok (a - (b * q)) == 0, done.
    q := q - 1.
done:
    Pohuwu q.
}

Yokyi fmod(a, b) {
    Pohuwu a - (b * fdiv(a, b)).
}

Koke first := Pewexpo().
Yopok first == Liliga, endp.
Koke k := Bupuxbo(first).
Koke items := [].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Oxba(items, line).
    line := Pewexpo().
Kobihek
Koke n := Yik(items).
Gipolu j := 1 Wexdush n Gihe Hehokgi
    Ebi items[fmod((j - 1) - k, n) + 1].
Kobihek
endp:
</solution>

<solution task="t1-weekday">
Yokyi fdiv(a, b) {
    Koke q := a / b.
    Yopok (a - (b * q)) == 0, done.
    q := q - 1.
done:
    Pohuwu q.
}

Yokyi num(s, a, b) {
    Koke v := 0.
    Gipolu i := a Wexdush b Gihe Hehokgi
        v := (v * 10) + Bupuxbo(s[i]).
    Kobihek
    Pohuwu v.
}

Koke names := ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"].
Koke tt := [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Yopok Yik(line) < 10, next.
    Koke y := num(line, 1, 4).
    Koke m := num(line, 6, 7).
    Koke d := num(line, 9, 10).
    Yopok m >= 3, nodec.
    y := y - 1.
nodec:
    Koke s := y + fdiv(y, 4) - fdiv(y, 100) + fdiv(y, 400) + tt[m] + d.
    Ebi names[(s - (7 * fdiv(s, 7))) + 1].
next:
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-bignum">
Yokyi fdiv(a, b) {
    Koke q := a / b.
    Yopok (a - (b * q)) == 0, done.
    q := q - 1.
done:
    Pohuwu q.
}

Yokyi split(s) {
    Koke parts := [].
    Koke cur := "".
    Gipolu i := 1 Wexdush Yik(s) Gihe Hehokgi
        Koke c := s[i].
        Yopok c == " ", sep.
        cur := cur ++ c.
        Gosh.
    sep:
        Yopok Yik(cur) == 0, skip.
        Oxba(parts, cur).
        cur := "".
    skip:
        Gosh.
    Kobihek
    Yopok Yik(cur) == 0, fin.
    Oxba(parts, cur).
fin:
    Pohuwu parts.
}

Yokyi digits(s) {
    Koke r := [].
    Gipolu i := Yik(s) Wexdush 1 Drix -1 Gihe Hehokgi
        Oxba(r, Bupuxbo(s[i])).
    Kobihek
    Pohuwu r.
}

Yokyi tostr(r) {
    Koke n := Yik(r).
    Puwadish (n > 1) Okdro (r[n] == 0) Gihe Hehokgi
        n := n - 1.
    Kobihek
    Koke s := "".
    Gipolu i := n Wexdush 1 Drix -1 Gihe Hehokgi
        s := s ++ r[i].
    Kobihek
    Pohuwu s.
}

Yokyi add(a, b) {
    Koke r := [].
    Koke n := Yik(a).
    Yopok Yik(b) <= n, ok.
    n := Yik(b).
ok:
    Koke c := 0.
    Gipolu i := 1 Wexdush n Gihe Hehokgi
        Koke s := c.
        Yopok i > Yik(a), noa.
        s := s + a[i].
    noa:
        Yopok i > Yik(b), nob.
        s := s + b[i].
    nob:
        c := 0.
        Yopok s < 10, nc.
        s := s - 10.
        c := 1.
    nc:
        Oxba(r, s).
    Kobihek
    Yopok c == 0, fin.
    Oxba(r, c).
fin:
    Pohuwu r.
}

Yokyi mul(a, b) {
    Koke la := Yik(a).
    Koke lb := Yik(b).
    Koke r := [].
    Gipolu i := 1 Wexdush (la + lb) Gihe Hehokgi
        Oxba(r, 0).
    Kobihek
    Gipolu i := 1 Wexdush la Gihe Hehokgi
        Koke ai := a[i].
        Yopok ai == 0, skipi.
        Gipolu j := 1 Wexdush lb Gihe Hehokgi
            Koke k := (i + j) - 1.
            r[k] := r[k] + (ai * b[j]).
        Kobihek
    skipi:
        Gosh.
    Kobihek
    Koke c := 0.
    Gipolu i := 1 Wexdush (la + lb) Gihe Hehokgi
        Koke v := r[i] + c.
        c := fdiv(v, 10).
        r[i] := v - (c * 10).
    Kobihek
    Pohuwu r.
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke p := split(line).
    Yopok Yik(p) < 2, next.
    Koke a := digits(p[1]).
    Koke b := digits(p[2]).
    Koke sm := tostr(add(a, b)).
    Koke pr := tostr(mul(a, b)).
    Ebi sm ++ " " ++ pr.
next:
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-life">
Koke g := Bupuxbo(Pewexpo()).
Koke rows := [].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Yopok Yik(line) == 0, sk.
    Oxba(rows, line).
sk:
    line := Pewexpo().
Kobihek
Koke R := Yik(rows).
Yopok R == 0, endp.
Koke C := Yik(rows[1]).
Koke W := C + 2.
Koke H := R + 2.
Koke cur := [].
Gipolu k := 1 Wexdush (W * H) Gihe Hehokgi
    Oxba(cur, 0).
Kobihek
Gipolu i := 1 Wexdush R Gihe Hehokgi
    Koke s := rows[i].
    Gipolu j := 1 Wexdush C Gihe Hehokgi
        Yopok s[j] /= "#", dead.
        cur[((i * W) + j) + 1] := 1.
    dead:
        Gosh.
    Kobihek
Kobihek
Gipolu t := 1 Wexdush g Gihe Hehokgi
    Koke nxt := [].
    Gipolu k := 1 Wexdush (W * H) Gihe Hehokgi
        Oxba(nxt, 0).
    Kobihek
    Gipolu i := 1 Wexdush R Gihe Hehokgi
        Gipolu j := 1 Wexdush C Gihe Hehokgi
            Koke p := ((i * W) + j) + 1.
            Koke nb := cur[p - 1] + cur[p + 1] + cur[p - W] + cur[p + W] + cur[(p - W) - 1] + cur[(p - W) + 1] + cur[(p + W) - 1] + cur[(p + W) + 1].
            Yopok (nb == 3) Dak ((nb == 2) Okdro (cur[p] == 1)), live.
            Gosh.
        live:
            nxt[p] := 1.
        Kobihek
    Kobihek
    cur := nxt.
Kobihek
Gipolu i := 1 Wexdush R Gihe Hehokgi
    Koke s := "".
    Gipolu j := 1 Wexdush C Gihe Hehokgi
        Yopok cur[((i * W) + j) + 1] == 1, al.
        s := s ++ ".".
        Gosh.
    al:
        s := s ++ "#".
    Kobihek
    Ebi s.
Kobihek
endp:
</solution>

<solution task="t2-rpn">
Yokyi split(s) {
    Koke parts := [].
    Koke cur := "".
    Gipolu i := 1 Wexdush Yik(s) Gihe Hehokgi
        Koke c := s[i].
        Yopok c == " ", sep.
        cur := cur ++ c.
        Gosh.
    sep:
        Yopok Yik(cur) == 0, skip.
        Oxba(parts, cur).
        cur := "".
    skip:
        Gosh.
    Kobihek
    Yopok Yik(cur) == 0, fin.
    Oxba(parts, cur).
fin:
    Pohuwu parts.
}

Yokyi tdiv(a, b) {
    Koke q := a / b.
    Yopok (a - (b * q)) == 0, done.
    Yopok (a < 0) /= (b < 0), done.
    q := q - 1.
done:
    Pohuwu q.
}

Yokyi isint(t) {
    Koke n := Yik(t).
    Koke st := 1.
    Yopok t[1] /= "-", nos.
    st := 2.
nos:
    Yopok st > n, bad.
    Gipolu i := st Wexdush n Gihe Hehokgi
        Koke c := t[i].
        Yopok (c < "0") Dak (c > "9"), bad.
    Kobihek
    Pohuwu Geklabik.
bad:
    Pohuwu Lesh.
}

Yokyi evalline(line) {
    Koke toks := split(line).
    Yopok Yik(toks) == 0, err.
    Koke st := [].
    Koke sp := 0.
    Gipolu i := 1 Wexdush Yik(toks) Gihe Hehokgi
        Koke t := toks[i].
        Yopok isint(t), push.
        Yopok sp < 2, err.
        Koke b := st[sp].
        Koke a := st[sp - 1].
        sp := sp - 1.
        Koke r := 0.
        Dru t Ihedrux
        "+": Hehokgi
            r := a + b.
        Kobihek
        "-": Hehokgi
            r := a - b.
        Kobihek
        "*": Hehokgi
            r := a * b.
        Kobihek
        "/": Hehokgi
            Yopok b == 0, err.
            r := tdiv(a, b).
        Kobihek
        "%": Hehokgi
            Yopok b == 0, err.
            r := a - (b * tdiv(a, b)).
        Kobihek
        Hishyeko Hehokgi
            Uxdrush err.
        Kobihek Kobihek
        st[sp] := r.
        Gosh.
    push:
        sp := sp + 1.
        Yopok sp <= Yik(st), setv.
        Oxba(st, Bupuxbo(t)).
        Gosh.
    setv:
        st[sp] := Bupuxbo(t).
    Kobihek
    Yopok sp /= 1, err.
    Pohuwu Yawishbo(st[1]).
err:
    Pohuwu "error".
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Ebi evalline(line).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-wordfreq">
Yokyi lowc(c) {
    Yopok (c >= "A") Okdro (c <= "Z"), isup.
    Pohuwu c.
isup:
    Koke up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    Koke low := "abcdefghijklmnopqrstuvwxyz".
    Koke lo := 1.
    Koke hi := 26.
    Puwadish lo < hi Gihe Hehokgi
        Koke mid := (lo + hi - 1) / 2.
        Yopok up[mid] >= c, goleft.
        lo := mid + 1.
        Gosh.
    goleft:
        hi := mid.
    Kobihek
    Pohuwu low[lo].
}

Yokyi less(x, y, mode) {
    Yopok mode == 1, m1.
    Koke cx := x[2].
    Koke cy := y[2].
    Yopok cx /= cy, diff.
    Pohuwu x[1] < y[1].
diff:
    Pohuwu cx > cy.
m1:
    Pohuwu x < y.
}

Yokyi msort(xs, mode) {
    Koke n := Yik(xs).
    Yopok n > 1, go.
    Pohuwu xs.
go:
    Koke h := n / 2.
    Koke a := [].
    Koke b := [].
    Gipolu i := 1 Wexdush h Gihe Hehokgi
        Oxba(a, xs[i]).
    Kobihek
    Gipolu i := h + 1 Wexdush n Gihe Hehokgi
        Oxba(b, xs[i]).
    Kobihek
    a := msort(a, mode).
    b := msort(b, mode).
    Koke r := [].
    Koke i := 1.
    Koke j := 1.
    Koke la := Yik(a).
    Koke lb := Yik(b).
    Puwadish (i <= la) Okdro (j <= lb) Gihe Hehokgi
        Yopok less(b[j], a[i], mode), takeb.
        Oxba(r, a[i]).
        i := i + 1.
        Gosh.
    takeb:
        Oxba(r, b[j]).
        j := j + 1.
    Kobihek
    Puwadish i <= la Gihe Hehokgi
        Oxba(r, a[i]).
        i := i + 1.
    Kobihek
    Puwadish j <= lb Gihe Hehokgi
        Oxba(r, b[j]).
        j := j + 1.
    Kobihek
    Pohuwu r.
}

Koke words := [].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke cur := "".
    Gipolu i := 1 Wexdush Yik(line) Gihe Hehokgi
        Koke c := line[i].
        Yopok ((c >= "a") Okdro (c <= "z")) Dak ((c >= "A") Okdro (c <= "Z")), letter.
        Yopok Yik(cur) == 0, nl.
        Oxba(words, cur).
        cur := "".
    nl:
        Gosh.
    letter:
        cur := cur ++ lowc(c).
    Kobihek
    Yopok Yik(cur) == 0, eol.
    Oxba(words, cur).
eol:
    line := Pewexpo().
Kobihek

Koke sw := msort(words, 1).
Koke pairs := [].
Koke k := 1.
Koke n := Yik(sw).
Puwadish k <= n Gihe Hehokgi
    Koke w := sw[k].
    Koke cnt := 0.
    Puwadish (k <= n) Okdro (sw[k] == w) Gihe Hehokgi
        cnt := cnt + 1.
        k := k + 1.
    Kobihek
    Oxba(pairs, [w, cnt]).
Kobihek
Koke sp := msort(pairs, 2).
Koke m := Yik(sp).
Yopok m <= 10, ok10.
m := 10.
ok10:
Gipolu i := 1 Wexdush m Gihe Hehokgi
    Koke e := sp[i].
    Ebi e[1] ++ " " ++ e[2].
Kobihek
</solution>