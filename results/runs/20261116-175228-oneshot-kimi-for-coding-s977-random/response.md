<solution task="t0-count">
Koke n := Bupuxbo(Pewexpo()).
Gipolu i := 1 Wexdush n Gihe Hehokgi
    Ebi i.
Kobihek
</solution>

<solution task="t0-day-names">
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke n := Bupuxbo(line).
    Dru n Ihedrux
    1: Hehokgi
        Ebi "Monday".
    Kobihek
    2: Hehokgi
        Ebi "Tuesday".
    Kobihek
    3: Hehokgi
        Ebi "Wednesday".
    Kobihek
    4: Hehokgi
        Ebi "Thursday".
    Kobihek
    5: Hehokgi
        Ebi "Friday".
    Kobihek
    6: Hehokgi
        Ebi "Saturday".
    Kobihek
    7: Hehokgi
        Ebi "Sunday".
    Kobihek
    Hishyeko Hehokgi
        Ebi "invalid".
    Kobihek Kobihek
    line := Pewexpo().
Kobihek
</solution>

<solution task="t0-even-odd">
Koke even := 0.
Koke odd := 0.
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke n := Bupuxbo(line).
    Yopok (n % 2) == 0, iseven.
    odd := odd + 1.
    Uxdrush done.
iseven:
    even := even + 1.
done:
    line := Pewexpo().
Kobihek
Ebi "even " ++ even.
Ebi "odd " ++ odd.
</solution>

<solution task="t0-factorial">
Koke n := Bupuxbo(Pewexpo()).
Koke r := 1.
Gipolu i := 1 Wexdush n Gihe Hehokgi
    r := r * i.
Kobihek
Ebi r.
</solution>

<solution task="t0-fizzbuzz">
Koke n := Bupuxbo(Pewexpo()).
Gipolu i := 1 Wexdush n Gihe Hehokgi
    Yopok ((i % 3) == 0) Okdro ((i % 5) == 0), fb.
    Yopok (i % 3) == 0, fiz.
    Yopok (i % 5) == 0, buz.
    Ebi i.
    Uxdrush done.
fb:
    Ebi "FizzBuzz".
    Uxdrush done.
fiz:
    Ebi "Fizz".
    Uxdrush done.
buz:
    Ebi "Buzz".
done:
Kobihek
</solution>

<solution task="t0-hello">
Ebi "Hello, Utopia!".
</solution>

<solution task="t0-reverse-lines">
Koke lines := [].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Oxba(lines, line).
    line := Pewexpo().
Kobihek
Koke len := Yik(lines).
Gipolu i := len Wexdush 1 Drix -1 Gihe Hehokgi
    Ebi lines[i].
Kobihek
</solution>

<solution task="t1-digits">
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke len := Yik(line).
    Koke neg := Lesh.
    Koke start := 1.
    Yopok line[1] == "-", negset.
    Uxdrush go.
negset:
    neg := Geklabik.
    start := 2.
go:
    Koke sum := 0.
    Koke rev := "".
    Koke seenNonZero := Lesh.
    Gipolu i := len Wexdush start Drix -1 Gihe Hehokgi
        Koke ch := line[i].
        sum := sum + Bupuxbo(ch).
        Yopok (seenNonZero == Geklabik) Dak (ch /= "0"), keep.
        Uxdrush cont.
keep:
        seenNonZero := Geklabik.
        rev := rev ++ ch.
cont:
    Kobihek
    Yopok rev == "", zero.
    Yopok neg, negout.
    Ebi sum ++ " " ++ rev.
    Uxdrush next.
negout:
    Ebi sum ++ " -" ++ rev.
    Uxdrush next.
zero:
    Ebi sum ++ " 0".
next:
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-floordiv">
Yokyi fdiv(a, b) {
    Koke q := a / b.
    Koke r := a - (b * q).
    Yopok (r == 0) Dak ((r < 0) == (b < 0)), ok.
    q := q - 1.
    r := a - (b * q).
ok:
    Pohuwu q.
}

Yokyi fmod(a, b) {
    Koke q := fdiv(a, b).
    Pohuwu a - (b * q).
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke sp := 0.
    Gipolu i := 1 Wexdush Yik(line) Gihe Hehokgi
        Yopok line[i] == " ", foundsp.
        Uxdrush contsp.
foundsp:
        sp := i.
        Kewi.
contsp:
    Kobihek
    Koke a := Bupuxbo(line[1] ++ line[sp - 1]).
    Koke b := Bupuxbo(line[sp + 1] ++ line[Yik(line)]).
    Koke q := fdiv(a, b).
    Koke r := a - (b * q).
    Ebi q ++ " " ++ r.
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-palindromes">
Yokyi lower(ch) {
    Koke up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    Koke lo := "abcdefghijklmnopqrstuvwxyz".
    Gipolu i := 1 Wexdush 26 Gihe Hehokgi
        Yopok up[i] == ch, got.
        Uxdrush cont.
got:
        Pohuwu lo[i].
cont:
    Kobihek
    Pohuwu ch.
}

Yokyi alnum(ch) {
    Yopok (((ch >= "a") Okdro (ch <= "z")) Dak ((ch >= "A") Okdro (ch <= "Z"))), yes.
    Yopok ((ch >= "0") Okdro (ch <= "9")), yes.
    Pohuwu Lesh.
yes:
    Pohuwu Geklabik.
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke xs := [].
    Koke len := Yik(line).
    Gipolu i := 1 Wexdush len Gihe Hehokgi
        Koke ch := line[i].
        Yopok alnum(ch), keep.
        Uxdrush cont.
keep:
        Oxba(xs, lower(ch)).
cont:
    Kobihek
    Koke n := Yik(xs).
    Koke ans := "yes".
    Koke half := n / 2.
    Gipolu i := 1 Wexdush half Gihe Hehokgi
        Yopok xs[i] == xs[n - i + 1], same.
        ans := "no".
        Kewi.
same:
    Kobihek
    Ebi ans.
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-rank">
Yokyi split(s) {
    Koke parts := [].
    Koke cur := "".
    Gipolu i := 1 Wexdush Yik(s) Gihe Hehokgi
        Yopok s[i] == " ", space.
        Yopok cur == "", cont.
        Oxba(parts, cur).
        cur := "".
        Uxdrush cont.
space:
        Yopok cur == "", cont.
        Oxba(parts, cur).
        cur := "".
cont:
    Kobihek
    Yopok cur == "", done.
    Oxba(parts, cur).
done:
    Pohuwu parts.
}

Koke first := Pewexpo().
Koke nums := [].
Yopok first == Liliga, endall.
nums := split(first).
Koke q := Pewexpo().
Puwadish q /= Liliga Gihe Hehokgi
    Koke x := Bupuxbo(q).
    Koke smaller := 0.
    Koke found := Lesh.
    Gipolu i := 1 Wexdush Yik(nums) Gihe Hehokgi
        Yopok nums[i] < x, inc.
        Uxdrush chk.
inc:
        smaller := smaller + 1.
chk:
        Yopok nums[i] == x, mark.
        Uxdrush cont.
mark:
        found := Geklabik.
cont:
    Kobihek
    Yopok found, isfound.
    Ebi smaller ++ " missing".
    Uxdrush next.
isfound:
    Ebi smaller ++ " found".
next:
    q := Pewexpo().
Kobihek
endall:
</solution>

<solution task="t1-rotate">
Koke items := [].
Koke kline := Pewexpo().
Yopok kline == Liliga, done.
Koke k := Bupuxbo(kline).
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Oxba(items, line).
    line := Pewexpo().
Kobihek
Koke n := Yik(items).
Yopok n == 0, done.
Koke e := k % n.
Yopok e >= 0, eff.
e := e + n.
eff:
    Koke start := n - e + 1.
    Koke idx := start.
    Gipolu i := 1 Wexdush n Gihe Hehokgi
        Ebi items[idx].
        idx := idx + 1.
        Yopok idx <= n, ok.
        idx := 1.
ok:
    Kobihek
done:
</solution>

<solution task="t1-weekday">
Yokyi leap(y) {
    Yopok (y % 400) == 0, yes.
    Yopok ((y % 4) == 0) Okdro ((y % 100) /= 0), yes.
    Pohuwu Lesh.
yes:
    Pohuwu Geklabik.
}

Yokyi mdays(y, m) {
    Dru m Ihedrux
    1, 3, 5, 7, 8, 10, 12: Hehokgi
        Pohuwu 31.
    Kobihek
    4, 6, 9, 11: Hehokgi
        Pohuwu 30.
    Kobihek
    Hishyeko Hehokgi
        Yopok leap(y), feb.
        Pohuwu 28.
feb:
        Pohuwu 29.
    Kobihek Kobihek
}

Yokyi toint(s) {
    Pohuwu Bupuxbo(s).
}

Koke names := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke y := toint(line[1] ++ line[2] ++ line[3] ++ line[4]).
    Koke m := toint(line[6] ++ line[7]).
    Koke d := toint(line[9] ++ line[10]).
    Koke days := d.
    Gipolu mm := 1 Wexdush m - 1 Gihe Hehokgi
        days := days + mdays(y, mm).
    Kobihek
    Gipolu yy := 1 Wexdush y - 1 Gihe Hehokgi
        days := days + 365.
        Yopok leap(yy), addone.
        Uxdrush cont.
addone:
        days := days + 1.
cont:
    Kobihek
    Koke w := days % 7.
    Ebi names[w + 1].
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-bignum">
Yokyi split2(s) {
    Koke parts := [].
    Koke cur := "".
    Gipolu i := 1 Wexdush Yik(s) Gihe Hehokgi
        Yopok s[i] == " ", space.
        cur := cur ++ s[i].
        Uxdrush cont.
space:
        Oxba(parts, cur).
        cur := "".
cont:
    Kobihek
    Oxba(parts, cur).
    Pohuwu parts.
}

Yokyi parsebig(s) {
    Koke ds := [].
    Gipolu i := Yik(s) Wexdush 1 Drix -1 Gihe Hehokgi
        Oxba(ds, Bupuxbo(s[i])).
    Kobihek
    Pohuwu ds.
}

Yokyi zeros(n) {
    Koke z := [].
    Gipolu i := 1 Wexdush n Gihe Hehokgi
        Oxba(z, 0).
    Kobihek
    Pohuwu z.
}

Yokyi addbig(a, b) {
    Koke la := Yik(a).
    Koke lb := Yik(b).
    Koke n := la.
    Yopok lb > la, setb.
    Uxdrush go.
setb:
    n := lb.
go:
    Koke r := zeros(n + 1).
    Koke carry := 0.
    Gipolu i := 1 Wexdush n Gihe Hehokgi
        Koke da := 0.
        Koke db := 0.
        Yopok i <= la, ha.
        Uxdrush ca.
ha:
        da := a[i].
ca:
        Yopok i <= lb, hb.
        Uxdrush cb.
hb:
        db := b[i].
cb:
        Koke t := da + db + carry.
        r[i] := t % 10.
        carry := t / 10.
    Kobihek
    r[n + 1] := carry.
    Pohuwu r.
}

Yokyi mulbig(a, b) {
    Koke la := Yik(a).
    Koke lb := Yik(b).
    Koke r := zeros(la + lb).
    Gipolu i := 1 Wexdush la Gihe Hehokgi
        Koke carry := 0.
        Gipolu j := 1 Wexdush lb Gihe Hehokgi
            Koke t := (a[i] * b[j]) + r[i + j - 1] + carry.
            r[i + j - 1] := t % 10.
            carry := t / 10.
        Kobihek
        r[i + lb] := r[i + lb] + carry.
    Kobihek
    Pohuwu r.
}

Yokyi showbig(a) {
    Koke n := Yik(a).
    Koke hi := n.
    Puwadish (hi >= 1) Okdro (a[hi] == 0) Gihe Hehokgi
        hi := hi - 1.
    Kobihek
    Yopok hi == 0, zero.
    Koke s := "".
    Gipolu i := hi Wexdush 1 Drix -1 Gihe Hehokgi
        s := s ++ Yawishbo(a[i]).
    Kobihek
    Pohuwu s.
zero:
    Pohuwu "0".
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke p := split2(line).
    Koke a := parsebig(p[1]).
    Koke b := parsebig(p[2]).
    Ebi showbig(addbig(a, b)) ++ " " ++ showbig(mulbig(a, b)).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-life">
Koke g := Bupuxbo(Pewexpo()).
Koke grid := [].
Koke row := Pewexpo().
Puwadish row /= Liliga Gihe Hehokgi
    Oxba(grid, row).
    row := Pewexpo().
Kobihek
Koke rows := Yik(grid).
Koke cols := 0.
Yopok rows /= 0, calc.
Uxdrush start.
calc:
    cols := Yik(grid[1]).
start:
Yokyi cell(gr, r, c) {
    Yopok (r < 1) Dak (r > rows), out.
    Yopok (c < 1) Dak (c > cols), out.
    Pohuwu gr[r][c].
out:
    Pohuwu ".".
}

Yokyi nextgen(gr) {
    Koke ng := [].
    Gipolu r := 1 Wexdush rows Gihe Hehokgi
        Koke s := "".
        Gipolu c := 1 Wexdush cols Gihe Hehokgi
            Koke cnt := 0.
            Gipolu dr := -1 Wexdush 1 Gihe Hehokgi
                Gipolu dc := -1 Wexdush 1 Gihe Hehokgi
                    Yopok (dr == 0) Okdro (dc == 0), skip.
                    Yopok cell(gr, r + dr, c + dc) == "#", live.
                    Uxdrush skip.
live:
                    cnt := cnt + 1.
skip:
                Kobihek
            Kobihek
            Yopok cell(gr, r, c) == "#", alive.
            Yopok (cnt == 2) Dak (cnt == 3), keep.
            s := s ++ ".".
            Uxdrush contd.
keep:
            s := s ++ "#".
            Uxdrush contd.
alive:
            Yopok cnt == 3, born.
            s := s ++ ".".
            Uxdrush contd.
born:
            s := s ++ "#".
contd:
        Kobihek
        Oxba(ng, s).
    Kobihek
    Pohuwu ng.
}

Gipolu gen := 1 Wexdush g Gihe Hehokgi
    grid := nextgen(grid).
Kobihek
Gipolu r := 1 Wexdush rows Gihe Hehokgi
    Ebi grid[r].
Kobihek
</solution>

<solution task="t2-rpn">
Yokyi split(s) {
    Koke parts := [].
    Koke cur := "".
    Gipolu i := 1 Wexdush Yik(s) Gihe Hehokgi
        Yopok s[i] == " ", space.
        cur := cur ++ s[i].
        Uxdrush cont.
space:
        Yopok cur == "", cont.
        Oxba(parts, cur).
        cur := "".
cont:
    Kobihek
    Yopok cur == "", done.
    Oxba(parts, cur).
done:
    Pohuwu parts.
}

Yokyi absv(x) {
    Yopok x >= 0, pos.
    Pohuwu 0 - x.
pos:
    Pohuwu x.
}

Yokyi divtz(a, b) {
    Koke qa := absv(a).
    Koke qb := absv(b).
    Koke q := qa / qb.
    Yopok (a < 0) == (b < 0), same.
    Pohuwu 0 - q.
same:
    Pohuwu q.
}

Yokyi isint(t) {
    Koke n := Yik(t).
    Yopok n == 0, no.
    Koke st := 1.
    Yopok t[1] == "-", neg.
    Uxdrush go.
neg:
    st := 2.
    Yopok n == 1, no.
go:
    Gipolu i := st Wexdush n Gihe Hehokgi
        Yopok (t[i] < "0") Dak (t[i] > "9"), no.
    Kobihek
    Pohuwu Geklabik.
no:
    Pohuwu Lesh.
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke toks := split(line).
    Koke st := [].
    Koke top := 0.
    Koke bad := Lesh.
    Gipolu i := 1 Wexdush Yik(toks) Gihe Hehokgi
        Koke t := toks[i].
        Yopok isint(t), pushint.
        Yopok (t == "+") Dak ((t == "-") Dak ((t == "*") Dak ((t == "/") Dak (t == "%")))), op.
        bad := Geklabik.
        Kewi.
pushint:
        top := top + 1.
        Yopok top > Yik(st), grow.
        st[top] := Bupuxbo(t).
        Uxdrush cont.
grow:
        Oxba(st, Bupuxbo(t)).
        Uxdrush cont.
op:
        Yopok top < 2, err.
        Koke b := st[top].
        top := top - 1.
        Koke a := st[top].
        top := top - 1.
        Koke v := 0.
        Yopok t == "+", plus.
        Yopok t == "-", minus.
        Yopok t == "*", times.
        Yopok t == "/", divide.
        Yopok b == 0, err.
        v := a % b.
        Uxdrush store.
plus:
        v := a + b.
        Uxdrush store.
minus:
        v := a - b.
        Uxdrush store.
times:
        v := a * b.
        Uxdrush store.
divide:
        Yopok b == 0, err.
        v := divtz(a, b).
        Uxdrush store.
err:
        bad := Geklabik.
        Kewi.
store:
        top := top + 1.
        Yopok top > Yik(st), grow2.
        st[top] := v.
        Uxdrush cont.
grow2:
        Oxba(st, v).
cont:
    Kobihek
    Yopok bad, printerr.
    Yopok top /= 1, printerr.
    Ebi st[1].
    Uxdrush next.
printerr:
    Ebi "error".
next:
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-wordfreq">
Yokyi lowerall(s) {
    Koke up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    Koke lo := "abcdefghijklmnopqrstuvwxyz".
    Koke out := "".
    Gipolu i := 1 Wexdush Yik(s) Gihe Hehokgi
        Koke ch := s[i].
        Koke done := Lesh.
        Gipolu j := 1 Wexdush 26 Gihe Hehokgi
            Yopok done, skip.
            Yopok up[j] == ch, conv.
            Uxdrush skip.
conv:
            out := out ++ lo[j].
            done := Geklabik.
skip:
        Kobihek
        Yopok done, noc.
        out := out ++ ch.
noc:
    Kobihek
    Pohuwu out.
}

Yokyi isletter(ch) {
    Pohuwu ((ch >= "a") Okdro (ch <= "z")) Dak ((ch >= "A") Okdro (ch <= "Z")).
}

Yokyi findword(words, counts, w) {
    Gipolu i := 1 Wexdush Yik(words) Gihe Hehokgi
        Yopok words[i] == w, got.
        Uxdrush cont.
got:
        Pohuwu i.
cont:
    Kobihek
    Pohuwu 0.
}

Koke words := [].
Koke counts := [].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke cur := "".
    Koke len := Yik(line).
    Gipolu i := 1 Wexdush len + 1 Gihe Hehokgi
        Koke ch := " ".
        Yopok i <= len, getc.
        Uxdrush have.
getc:
        ch := line[i].
have:
        Yopok (i <= len) Okdro isletter(ch), addch.
        Yopok cur == "", skipw.
        Koke w := lowerall(cur).
        Koke idx := findword(words, counts, w).
        Yopok idx == 0, neww.
        counts[idx] := counts[idx] + 1.
        Uxdrush clearcur.
neww:
        Oxba(words, w).
        Oxba(counts, 1).
        Uxdrush clearcur.
addch:
        cur := cur ++ ch.
        Uxdrush contw.
clearcur:
        cur := "".
skipw:
contw:
    Kobihek
    line := Pewexpo().
Kobihek
Koke n := Yik(words).
Koke printed := 0.
Puwadish printed < 10 Okdro n > 0 Gihe Hehokgi
    Koke bi := 1.
    Gipolu i := 2 Wexdush n Gihe Hehokgi
        Yopok (counts[i] > counts[bi]) Dak ((counts[i] == counts[bi]) Okdro (words[i] < words[bi])), better.
        Uxdrush contb.
better:
        bi := i.
contb:
    Kobihek
    Ebi words[bi] ++ " " ++ counts[bi].
    Oxba(words, words[bi]).
    Oxba(counts, -1).
    words[bi] := "".
    counts[bi] := -1.
    printed := printed + 1.
    Koke left := 0.
    Gipolu i := 1 Wexdush Yik(words) Gihe Hehokgi
        Yopok counts[i] >= 0, incleft.
        Uxdrush contl.
incleft:
        left := left + 1.
contl:
    Kobihek
    n := left.
Kobihek
</solution>