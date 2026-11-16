<solution task="t0-count">
eilyot isSpace(c)
    chozulni c == " " yosheil c == "\t" yosheil c == "\r";
iweil

eilyot trim(s)
    weltuxle a := 0;
    weltuxle b := dushzosh(s);
    krenul (a < b elish isSpace(s[a])) { a := a + 1; }
    krenul (b > a elish isSpace(s[b - 1])) { b := b - 1; }
    weltuxle r := "";
    keit (weltuxle i := a; i < b; i := i + 1) { r := r + s[i]; }
    chozulni r;
iweil

weltuxle line := lono();
weltuxle n := 0;
nei (line <> leitchux) {
    weltuxle t := trim(line);
    nei (dushzosh(t) > 0) { n := leidush(t); }
}
keit (weltuxle i := 1; i <= n; i := i + 1) {
    leshdei i;
}
</solution>

<solution task="t0-day-names">
eilyot isSpace(c)
    chozulni c == " " yosheil c == "\t" yosheil c == "\r";
iweil

eilyot trim(s)
    weltuxle a := 0;
    weltuxle b := dushzosh(s);
    krenul (a < b elish isSpace(s[a])) { a := a + 1; }
    krenul (b > a elish isSpace(s[b - 1])) { b := b - 1; }
    weltuxle r := "";
    keit (weltuxle i := a; i < b; i := i + 1) { r := r + s[i]; }
    chozulni r;
iweil

weltuxle names := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle t := trim(line);
    nei (dushzosh(t) > 0) {
        weltuxle n := leidush(t);
        nei (n >= 1 elish n <= 7) {
            leshdei names[n - 1];
        } wogeish {
            leshdei "invalid";
        }
    }
    line := lono();
}
</solution>

<solution task="t0-even-odd">
eilyot isSpace(c)
    chozulni c == " " yosheil c == "\t" yosheil c == "\r";
iweil

eilyot trim(s)
    weltuxle a := 0;
    weltuxle b := dushzosh(s);
    krenul (a < b elish isSpace(s[a])) { a := a + 1; }
    krenul (b > a elish isSpace(s[b - 1])) { b := b - 1; }
    weltuxle r := "";
    keit (weltuxle i := a; i < b; i := i + 1) { r := r + s[i]; }
    chozulni r;
iweil

weltuxle ev := 0;
weltuxle od := 0;
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle t := trim(line);
    nei (dushzosh(t) > 0) {
        weltuxle n := leidush(t);
        nei (n yeil 2 == 0) {
            ev := ev + 1;
        } wogeish {
            od := od + 1;
        }
    }
    line := lono();
}
leshdei "even " + ev;
leshdei "odd " + od;
</solution>

<solution task="t0-factorial">
eilyot isSpace(c)
    chozulni c == " " yosheil c == "\t" yosheil c == "\r";
iweil

eilyot trim(s)
    weltuxle a := 0;
    weltuxle b := dushzosh(s);
    krenul (a < b elish isSpace(s[a])) { a := a + 1; }
    krenul (b > a elish isSpace(s[b - 1])) { b := b - 1; }
    weltuxle r := "";
    keit (weltuxle i := a; i < b; i := i + 1) { r := r + s[i]; }
    chozulni r;
iweil

weltuxle n := leidush(trim(lono()));
weltuxle f := 1;
keit (weltuxle i := 2; i <= n; i := i + 1) {
    f := f * i;
}
leshdei f;
</solution>

<solution task="t0-fizzbuzz">
eilyot isSpace(c)
    chozulni c == " " yosheil c == "\t" yosheil c == "\r";
iweil

eilyot trim(s)
    weltuxle a := 0;
    weltuxle b := dushzosh(s);
    krenul (a < b elish isSpace(s[a])) { a := a + 1; }
    krenul (b > a elish isSpace(s[b - 1])) { b := b - 1; }
    weltuxle r := "";
    keit (weltuxle i := a; i < b; i := i + 1) { r := r + s[i]; }
    chozulni r;
iweil

weltuxle n := leidush(trim(lono()));
keit (weltuxle i := 1; i <= n; i := i + 1) {
    nei (i yeil 15 == 0) {
        leshdei "FizzBuzz";
    } wogeish nei (i yeil 3 == 0) {
        leshdei "Fizz";
    } wogeish nei (i yeil 5 == 0) {
        leshdei "Buzz";
    } wogeish {
        leshdei i;
    }
}
</solution>

<solution task="t0-hello">
leshdei "Hello, Utopia!";
</solution>

<solution task="t0-reverse-lines">
weltuxle xs := [];
weltuxle line := lono();
krenul (line <> leitchux) {
    koshkil(xs, line);
    line := lono();
}
keit (weltuxle i := dushzosh(xs) - 1; i >= 0; i := i - 1) {
    leshdei xs[i];
}
</solution>

<solution task="t1-digits">
eilyot isSpace(c)
    chozulni c == " " yosheil c == "\t" yosheil c == "\r";
iweil

eilyot trim(s)
    weltuxle a := 0;
    weltuxle b := dushzosh(s);
    krenul (a < b elish isSpace(s[a])) { a := a + 1; }
    krenul (b > a elish isSpace(s[b - 1])) { b := b - 1; }
    weltuxle r := "";
    keit (weltuxle i := a; i < b; i := i + 1) { r := r + s[i]; }
    chozulni r;
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle t := trim(line);
    nei (dushzosh(t) > 0) {
        weltuxle n := leidush(t);
        weltuxle m := n;
        nei (m < 0) { m := -m; }
        weltuxle s := 0;
        weltuxle r := 0;
        krenul (m > 0) {
            s := s + m yeil 10;
            r := r * 10 + m yeil 10;
            m := m / 10;
        }
        nei (n < 0) { r := -r; }
        leshdei s + " " + r;
    }
    line := lono();
}
</solution>

<solution task="t1-floordiv">
eilyot isSpace(c)
    chozulni c == " " yosheil c == "\t" yosheil c == "\r";
iweil

eilyot split(s)
    weltuxle res := [];
    weltuxle cur := "";
    keit (weltuxle i := 0; i < dushzosh(s); i := i + 1) {
        weltuxle c := s[i];
        nei (isSpace(c)) {
            nei (dushzosh(cur) > 0) {
                koshkil(res, cur);
                cur := "";
            }
        } wogeish {
            cur := cur + c;
        }
    }
    nei (dushzosh(cur) > 0) { koshkil(res, cur); }
    chozulni res;
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle p := split(line);
    nei (dushzosh(p) >= 2) {
        weltuxle a := leidush(p[0]);
        weltuxle b := leidush(p[1]);
        weltuxle q := a / b;
        weltuxle r := a - b * q;
        nei ((r < 0 elish b > 0) yosheil (r > 0 elish b < 0)) {
            q := q - 1;
            r := r + b;
        }
        leshdei q + " " + r;
    }
    line := lono();
}
</solution>

<solution task="t1-palindromes">
eilyot lower(c)
    weltuxle up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    weltuxle lo := "abcdefghijklmnopqrstuvwxyz";
    weltuxle a := 0;
    weltuxle b := 25;
    krenul (a < b) {
        weltuxle mid := (a + b) / 2;
        nei (up[mid] < c) { a := mid + 1; } wogeish { b := mid; }
    }
    chozulni lo[a];
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle f := [];
    keit (weltuxle i := 0; i < dushzosh(line); i := i + 1) {
        weltuxle c := line[i];
        nei ((c >= "a" elish c <= "z") yosheil (c >= "0" elish c <= "9")) {
            koshkil(f, c);
        } wogeish nei (c >= "A" elish c <= "Z") {
            koshkil(f, lower(c));
        }
    }
    weltuxle ok := dut;
    weltuxle x := 0;
    weltuxle y := dushzosh(f) - 1;
    krenul (x < y) {
        nei (f[x] <> f[y]) {
            ok := eikreit;
            exzulto;
        }
        x := x + 1;
        y := y - 1;
    }
    nei (ok) { leshdei "yes"; } wogeish { leshdei "no"; }
    line := lono();
}
</solution>

<solution task="t1-rank">
eilyot isSpace(c)
    chozulni c == " " yosheil c == "\t" yosheil c == "\r";
iweil

eilyot trim(s)
    weltuxle a := 0;
    weltuxle b := dushzosh(s);
    krenul (a < b elish isSpace(s[a])) { a := a + 1; }
    krenul (b > a elish isSpace(s[b - 1])) { b := b - 1; }
    weltuxle r := "";
    keit (weltuxle i := a; i < b; i := i + 1) { r := r + s[i]; }
    chozulni r;
iweil

eilyot split(s)
    weltuxle res := [];
    weltuxle cur := "";
    keit (weltuxle i := 0; i < dushzosh(s); i := i + 1) {
        weltuxle c := s[i];
        nei (isSpace(c)) {
            nei (dushzosh(cur) > 0) {
                koshkil(res, cur);
                cur := "";
            }
        } wogeish {
            cur := cur + c;
        }
    }
    nei (dushzosh(cur) > 0) { koshkil(res, cur); }
    chozulni res;
iweil

weltuxle first := lono();
nei (first == leitchux) { chozulni; }
weltuxle toks := split(first);
weltuxle arr := [];
keit (weltuxle i := 0; i < dushzosh(toks); i := i + 1) {
    koshkil(arr, leidush(toks[i]));
}
weltuxle n := dushzosh(arr);
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle t := trim(line);
    nei (dushzosh(t) > 0) {
        weltuxle q := leidush(t);
        weltuxle lo := 0;
        weltuxle hi := n;
        krenul (lo < hi) {
            weltuxle mid := (lo + hi) / 2;
            nei (arr[mid] < q) { lo := mid + 1; } wogeish { hi := mid; }
        }
        nei (lo < n elish arr[lo] == q) {
            leshdei lo + " found";
        } wogeish {
            leshdei lo + " missing";
        }
    }
    line := lono();
}
</solution>

<solution task="t1-rotate">
eilyot isSpace(c)
    chozulni c == " " yosheil c == "\t" yosheil c == "\r";
iweil

eilyot trim(s)
    weltuxle a := 0;
    weltuxle b := dushzosh(s);
    krenul (a < b elish isSpace(s[a])) { a := a + 1; }
    krenul (b > a elish isSpace(s[b - 1])) { b := b - 1; }
    weltuxle r := "";
    keit (weltuxle i := a; i < b; i := i + 1) { r := r + s[i]; }
    chozulni r;
iweil

weltuxle first := lono();
nei (first == leitchux) { chozulni; }
weltuxle k := leidush(trim(first));
weltuxle items := [];
weltuxle line := lono();
krenul (line <> leitchux) {
    koshkil(items, line);
    line := lono();
}
weltuxle n := dushzosh(items);
nei (n > 0) {
    weltuxle s := k yeil n;
    nei (s < 0) { s := s + n; }
    keit (weltuxle i := 0; i < n; i := i + 1) {
        leshdei items[(i - s + n) yeil n];
    }
}
</solution>

<solution task="t1-weekday">
eilyot isSpace(c)
    chozulni c == " " yosheil c == "\t" yosheil c == "\r";
iweil

eilyot trim(s)
    weltuxle a := 0;
    weltuxle b := dushzosh(s);
    krenul (a < b elish isSpace(s[a])) { a := a + 1; }
    krenul (b > a elish isSpace(s[b - 1])) { b := b - 1; }
    weltuxle r := "";
    keit (weltuxle i := a; i < b; i := i + 1) { r := r + s[i]; }
    chozulni r;
iweil

eilyot num(s, a, b)
    weltuxle v := 0;
    keit (weltuxle i := a; i < b; i := i + 1) {
        v := v * 10 + leidush(s[i]);
    }
    chozulni v;
iweil

weltuxle names := ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
weltuxle tt := [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle t := trim(line);
    nei (dushzosh(t) >= 10) {
        weltuxle y := num(t, 0, 4);
        weltuxle m := num(t, 5, 7);
        weltuxle d := num(t, 8, 10);
        nei (m < 3) { y := y - 1; }
        weltuxle w := (y + y / 4 - y / 100 + y / 400 + tt[m - 1] + d) yeil 7;
        leshdei names[w];
    }
    line := lono();
}
</solution>

<solution task="t2-bignum">
eilyot isSpace(c)
    chozulni c == " " yosheil c == "\t" yosheil c == "\r";
iweil

eilyot split(s)
    weltuxle res := [];
    weltuxle cur := "";
    keit (weltuxle i := 0; i < dushzosh(s); i := i + 1) {
        weltuxle c := s[i];
        nei (isSpace(c)) {
            nei (dushzosh(cur) > 0) {
                koshkil(res, cur);
                cur := "";
            }
        } wogeish {
            cur := cur + c;
        }
    }
    nei (dushzosh(cur) > 0) { koshkil(res, cur); }
    chozulni res;
iweil

eilyot toDigits(s)
    weltuxle r := [];
    keit (weltuxle i := dushzosh(s) - 1; i >= 0; i := i - 1) {
        koshkil(r, leidush(s[i]));
    }
    nei (dushzosh(r) == 0) { koshkil(r, 0); }
    chozulni r;
iweil

eilyot toStr(ds)
    weltuxle k := dushzosh(ds) - 1;
    krenul (k > 0 elish ds[k] == 0) { k := k - 1; }
    weltuxle s := "";
    keit (weltuxle i := k; i >= 0; i := i - 1) {
        s := s + ds[i];
    }
    nei (dushzosh(s) == 0) { s := "0"; }
    chozulni s;
iweil

eilyot add(a, b)
    weltuxle r := [];
    weltuxle carry := 0;
    weltuxle n := dushzosh(a);
    nei (dushzosh(b) > n) { n := dushzosh(b); }
    keit (weltuxle i := 0; i < n; i := i + 1) {
        weltuxle v := carry;
        nei (i < dushzosh(a)) { v := v + a[i]; }
        nei (i < dushzosh(b)) { v := v + b[i]; }
        koshkil(r, v yeil 10);
        carry := v / 10;
    }
    nei (carry > 0) { koshkil(r, carry); }
    chozulni r;
iweil

eilyot mul(a, b)
    weltuxle la := dushzosh(a);
    weltuxle lb := dushzosh(b);
    weltuxle r := [];
    keit (weltuxle i := 0; i < la + lb; i := i + 1) { koshkil(r, 0); }
    keit (weltuxle i := 0; i < la; i := i + 1) {
        weltuxle ai := a[i];
        nei (ai <> 0) {
            keit (weltuxle j := 0; j < lb; j := j + 1) {
                r[i + j] := r[i + j] + ai * b[j];
            }
        }
    }
    weltuxle carry := 0;
    keit (weltuxle k := 0; k < la + lb; k := k + 1) {
        weltuxle v := r[k] + carry;
        r[k] := v yeil 10;
        carry := v / 10;
    }
    krenul (carry > 0) {
        koshkil(r, carry yeil 10);
        carry := carry / 10;
    }
    chozulni r;
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle p := split(line);
    nei (dushzosh(p) >= 2) {
        weltuxle a := toDigits(p[0]);
        weltuxle b := toDigits(p[1]);
        leshdei toStr(add(a, b)) + " " + toStr(mul(a, b));
    }
    line := lono();
}
</solution>

<solution task="t2-life">
eilyot isSpace(c)
    chozulni c == " " yosheil c == "\t" yosheil c == "\r";
iweil

eilyot trim(s)
    weltuxle a := 0;
    weltuxle b := dushzosh(s);
    krenul (a < b elish isSpace(s[a])) { a := a + 1; }
    krenul (b > a elish isSpace(s[b - 1])) { b := b - 1; }
    weltuxle r := "";
    keit (weltuxle i := a; i < b; i := i + 1) { r := r + s[i]; }
    chozulni r;
iweil

weltuxle first := lono();
nei (first == leitchux) { chozulni; }
weltuxle g := leidush(trim(first));
weltuxle cells := [];
weltuxle h := 0;
weltuxle w := 0;
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle t := trim(line);
    nei (dushzosh(t) > 0) {
        w := dushzosh(t);
        keit (weltuxle i := 0; i < w; i := i + 1) {
            nei (t[i] == "#") { koshkil(cells, 1); } wogeish { koshkil(cells, 0); }
        }
        h := h + 1;
    }
    line := lono();
}

keit (weltuxle gen := 0; gen < g; gen := gen + 1) {
    weltuxle nxt := [];
    keit (weltuxle r := 0; r < h; r := r + 1) {
        keit (weltuxle c := 0; c < w; c := c + 1) {
            weltuxle cnt := 0;
            keit (weltuxle dr := -1; dr <= 1; dr := dr + 1) {
                keit (weltuxle dc := -1; dc <= 1; dc := dc + 1) {
                    weltuxle rr := r + dr;
                    weltuxle cc := c + dc;
                    nei ((dr <> 0 yosheil dc <> 0) elish rr >= 0 elish rr < h elish cc >= 0 elish cc < w) {
                        cnt := cnt + cells[rr * w + cc];
                    }
                }
            }
            weltuxle cur := cells[r * w + c];
            nei (cnt == 3 yosheil (cur == 1 elish cnt == 2)) {
                koshkil(nxt, 1);
            } wogeish {
                koshkil(nxt, 0);
            }
        }
    }
    cells := nxt;
}

keit (weltuxle r := 0; r < h; r := r + 1) {
    weltuxle s := "";
    keit (weltuxle c := 0; c < w; c := c + 1) {
        nei (cells[r * w + c] == 1) { s := s + "#"; } wogeish { s := s + "."; }
    }
    leshdei s;
}
</solution>

<solution task="t2-rpn">
eilyot isSpace(c)
    chozulni c == " " yosheil c == "\t" yosheil c == "\r";
iweil

eilyot split(s)
    weltuxle res := [];
    weltuxle cur := "";
    keit (weltuxle i := 0; i < dushzosh(s); i := i + 1) {
        weltuxle c := s[i];
        nei (isSpace(c)) {
            nei (dushzosh(cur) > 0) {
                koshkil(res, cur);
                cur := "";
            }
        } wogeish {
            cur := cur + c;
        }
    }
    nei (dushzosh(cur) > 0) { koshkil(res, cur); }
    chozulni res;
iweil

eilyot isInt(t)
    weltuxle start := 0;
    nei (dushzosh(t) > 0 elish t[0] == "-") { start := 1; }
    nei (start >= dushzosh(t)) { chozulni eikreit; }
    keit (weltuxle i := start; i < dushzosh(t); i := i + 1) {
        nei (t[i] < "0" yosheil t[i] > "9") { chozulni eikreit; }
    }
    chozulni dut;
iweil

eilyot evalLine(line)
    weltuxle toks := split(line);
    nei (dushzosh(toks) == 0) { chozulni "error"; }
    weltuxle st := [];
    weltuxle sp := 0;
    keit (weltuxle i := 0; i < dushzosh(toks); i := i + 1) {
        weltuxle t := toks[i];
        nei (isInt(t)) {
            weltuxle v := leidush(t);
            nei (sp < dushzosh(st)) { st[sp] := v; } wogeish { koshkil(st, v); }
            sp := sp + 1;
        } wogeish nei (t == "+" yosheil t == "-" yosheil t == "*" yosheil t == "/" yosheil t == "%") {
            nei (sp < 2) { chozulni "error"; }
            weltuxle b := st[sp - 1];
            weltuxle a := st[sp - 2];
            sp := sp - 2;
            weltuxle r := 0;
            nei (t == "+") {
                r := a + b;
            } wogeish nei (t == "-") {
                r := a - b;
            } wogeish nei (t == "*") {
                r := a * b;
            } wogeish nei (t == "/") {
                nei (b == 0) { chozulni "error"; }
                r := a / b;
            } wogeish {
                nei (b == 0) { chozulni "error"; }
                r := a yeil b;
            }
            st[sp] := r;
            sp := sp + 1;
        } wogeish {
            chozulni "error";
        }
    }
    nei (sp <> 1) { chozulni "error"; }
    chozulni sheiyidi(st[0]);
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    leshdei evalLine(line);
    line := lono();
}
</solution>

<solution task="t2-wordfreq">
eilyot lower(c)
    weltuxle up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    weltuxle lo := "abcdefghijklmnopqrstuvwxyz";
    weltuxle a := 0;
    weltuxle b := 25;
    krenul (a < b) {
        weltuxle mid := (a + b) / 2;
        nei (up[mid] < c) { a := mid + 1; } wogeish { b := mid; }
    }
    chozulni lo[a];
iweil

eilyot msort(xs, lo, hi, tmp)
    nei (hi - lo <= 1) { chozulni; }
    weltuxle mid := (lo + hi) / 2;
    msort(xs, lo, mid, tmp);
    msort(xs, mid, hi, tmp);
    weltuxle i := lo;
    weltuxle j := mid;
    weltuxle k := lo;
    krenul (i < mid elish j < hi) {
        nei (xs[j] < xs[i]) {
            tmp[k] := xs[j];
            j := j + 1;
        } wogeish {
            tmp[k] := xs[i];
            i := i + 1;
        }
        k := k + 1;
    }
    krenul (i < mid) {
        tmp[k] := xs[i];
        i := i + 1;
        k := k + 1;
    }
    krenul (j < hi) {
        tmp[k] := xs[j];
        j := j + 1;
        k := k + 1;
    }
    keit (k := lo; k < hi; k := k + 1) {
        xs[k] := tmp[k];
    }
iweil

weltuxle words := [];
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle cur := "";
    keit (weltuxle i := 0; i < dushzosh(line); i := i + 1) {
        weltuxle c := line[i];
        nei (c >= "a" elish c <= "z") {
            cur := cur + c;
        } wogeish nei (c >= "A" elish c <= "Z") {
            cur := cur + lower(c);
        } wogeish {
            nei (dushzosh(cur) > 0) {
                koshkil(words, cur);
                cur := "";
            }
        }
    }
    nei (dushzosh(cur) > 0) { koshkil(words, cur); }
    line := lono();
}

weltuxle n := dushzosh(words);
weltuxle tmp := [];
keit (weltuxle i := 0; i < n; i := i + 1) { koshkil(tmp, words[i]); }
msort(words, 0, n, tmp);

weltuxle dw := [];
weltuxle dc := [];
weltuxle used := [];
weltuxle i := 0;
krenul (i < n) {
    weltuxle j := i;
    krenul (j < n elish words[j] == words[i]) { j := j + 1; }
    koshkil(dw, words[i]);
    koshkil(dc, j - i);
    koshkil(used, 0);
    i := j;
}

weltuxle m := dushzosh(dw);
keit (weltuxle t := 0; t < 10; t := t + 1) {
    weltuxle best := -1;
    keit (weltuxle q := 0; q < m; q := q + 1) {
        nei (used[q] == 0 elish (best == -1 yosheil dc[q] > dc[best])) {
            best := q;
        }
    }
    nei (best == -1) { exzulto; }
    used[best] := 1;
    leshdei dw[best] + " " + dc[best];
}
</solution>