<solution task="t0-count">
weltuxle line := lono();
weltuxle n := 0;
nei (line <> leitchux) {
    n := leidush(line);
}
keit (weltuxle i := 1; i <= n; i := i + 1) {
    leshdei i;
}
</solution>

<solution task="t0-day-names">
eilyot clean(s)
    weltuxle r := "";
    keit (weltuxle i := 0; i < dushzosh(s); i := i + 1) {
        weltuxle c := s[i];
        nei (c <> " " elish c <> "\t" elish c <> "\r") {
            r := r + c;
        }
    }
    chozulni r;
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle s := clean(line);
    nei (dushzosh(s) > 0) {
        weltuxle n := leidush(s);
        yishzit n eixwo
        1: krei
            leshdei "Monday";
        zushox
        2: krei
            leshdei "Tuesday";
        zushox
        3: krei
            leshdei "Wednesday";
        zushox
        4: krei
            leshdei "Thursday";
        zushox
        5: krei
            leshdei "Friday";
        zushox
        6: krei
            leshdei "Saturday";
        zushox
        7: krei
            leshdei "Sunday";
        zushox
        wogeish krei
            leshdei "invalid";
        zushox zushox
    }
    line := lono();
}
</solution>

<solution task="t0-even-odd">
eilyot clean(s)
    weltuxle r := "";
    keit (weltuxle i := 0; i < dushzosh(s); i := i + 1) {
        weltuxle c := s[i];
        nei (c <> " " elish c <> "\t" elish c <> "\r") {
            r := r + c;
        }
    }
    chozulni r;
iweil

weltuxle evens := 0;
weltuxle odds := 0;
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle s := clean(line);
    nei (dushzosh(s) > 0) {
        weltuxle n := leidush(s);
        nei (n yeil 2 == 0) {
            evens := evens + 1;
        } wogeish {
            odds := odds + 1;
        }
    }
    line := lono();
}
leshdei "even " + evens;
leshdei "odd " + odds;
</solution>

<solution task="t0-factorial">
weltuxle line := lono();
weltuxle n := leidush(line);
weltuxle f := 1;
keit (weltuxle i := 2; i <= n; i := i + 1) {
    f := f * i;
}
leshdei f;
</solution>

<solution task="t0-fizzbuzz">
weltuxle n := leidush(lono());
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
weltuxle lines := [];
weltuxle line := lono();
krenul (line <> leitchux) {
    koshkil(lines, line);
    line := lono();
}
keit (weltuxle i := dushzosh(lines) - 1; i >= 0; i := i - 1) {
    leshdei lines[i];
}
</solution>

<solution task="t1-digits">
eilyot clean(s)
    weltuxle r := "";
    keit (weltuxle i := 0; i < dushzosh(s); i := i + 1) {
        weltuxle c := s[i];
        nei (c <> " " elish c <> "\t" elish c <> "\r") {
            r := r + c;
        }
    }
    chozulni r;
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle s := clean(line);
    nei (dushzosh(s) > 0) {
        weltuxle neg := eikreit;
        weltuxle sum := 0;
        weltuxle rev := 0;
        keit (weltuxle i := dushzosh(s) - 1; i >= 0; i := i - 1) {
            weltuxle c := s[i];
            nei (c == "-") {
                neg := dut;
            } wogeish {
                weltuxle d := leidush(c);
                sum := sum + d;
                rev := rev * 10 + d;
            }
        }
        nei (neg) {
            rev := 0 - rev;
        }
        leshdei sum + " " + rev;
    }
    line := lono();
}
</solution>

<solution task="t1-floordiv">
eilyot split(s)
    weltuxle res := [];
    weltuxle cur := "";
    weltuxle n := dushzosh(s);
    keit (weltuxle i := 0; i < n; i := i + 1) {
        weltuxle c := s[i];
        nei (c == " " yosheil c == "\t" yosheil c == "\r") {
            nei (dushzosh(cur) > 0) {
                koshkil(res, cur);
                cur := "";
            }
        } wogeish {
            cur := cur + c;
        }
    }
    nei (dushzosh(cur) > 0) {
        koshkil(res, cur);
    }
    chozulni res;
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle toks := split(line);
    nei (dushzosh(toks) >= 2) {
        weltuxle a := leidush(toks[0]);
        weltuxle b := leidush(toks[1]);
        weltuxle q := 0 - ((0 - a) / b);
        weltuxle r := a - b * q;
        leshdei q + " " + r;
    }
    line := lono();
}
</solution>

<solution task="t1-palindromes">
eilyot lower(c)
    nei (c < "A" yosheil c > "Z") {
        chozulni c;
    }
    weltuxle up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    weltuxle low := "abcdefghijklmnopqrstuvwxyz";
    weltuxle lo := 0;
    weltuxle hi := 25;
    krenul (lo < hi) {
        weltuxle mid := lo + (hi - lo - 1) / 2;
        nei (up[mid] < c) {
            lo := mid + 1;
        } wogeish {
            hi := mid;
        }
    }
    chozulni low[lo];
iweil

eilyot isalnum(c)
    chozulni (c >= "a" elish c <= "z") yosheil (c >= "A" elish c <= "Z") yosheil (c >= "0" elish c <= "9");
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle cs := [];
    weltuxle n := dushzosh(line);
    keit (weltuxle i := 0; i < n; i := i + 1) {
        weltuxle c := line[i];
        nei (isalnum(c)) {
            koshkil(cs, lower(c));
        }
    }
    weltuxle lo := 0;
    weltuxle hi := dushzosh(cs) - 1;
    weltuxle ok := dut;
    krenul (lo < hi) {
        nei (cs[lo] <> cs[hi]) {
            ok := eikreit;
            exzulto;
        }
        lo := lo + 1;
        hi := hi - 1;
    }
    nei (ok) {
        leshdei "yes";
    } wogeish {
        leshdei "no";
    }
    line := lono();
}
</solution>

<solution task="t1-rank">
eilyot split(s)
    weltuxle res := [];
    weltuxle cur := "";
    weltuxle n := dushzosh(s);
    keit (weltuxle i := 0; i < n; i := i + 1) {
        weltuxle c := s[i];
        nei (c == " " yosheil c == "\t" yosheil c == "\r") {
            nei (dushzosh(cur) > 0) {
                koshkil(res, cur);
                cur := "";
            }
        } wogeish {
            cur := cur + c;
        }
    }
    nei (dushzosh(cur) > 0) {
        koshkil(res, cur);
    }
    chozulni res;
iweil

weltuxle first := lono();
nei (first <> leitchux) {
    weltuxle toks := split(first);
    weltuxle xs := [];
    keit (weltuxle i := 0; i < dushzosh(toks); i := i + 1) {
        koshkil(xs, leidush(toks[i]));
    }
    weltuxle n := dushzosh(xs);
    weltuxle line := lono();
    krenul (line <> leitchux) {
        weltuxle qt := split(line);
        nei (dushzosh(qt) > 0) {
            weltuxle q := leidush(qt[0]);
            weltuxle lo := 0;
            weltuxle hi := n;
            krenul (lo < hi) {
                weltuxle mid := lo + (hi - lo - 1) / 2;
                nei (xs[mid] < q) {
                    lo := mid + 1;
                } wogeish {
                    hi := mid;
                }
            }
            nei (lo < n elish xs[lo] == q) {
                leshdei lo + " found";
            } wogeish {
                leshdei lo + " missing";
            }
        }
        line := lono();
    }
}
</solution>

<solution task="t1-rotate">
eilyot clean(s)
    weltuxle r := "";
    keit (weltuxle i := 0; i < dushzosh(s); i := i + 1) {
        weltuxle c := s[i];
        nei (c <> " " elish c <> "\t" elish c <> "\r") {
            r := r + c;
        }
    }
    chozulni r;
iweil

weltuxle first := lono();
nei (first <> leitchux) {
    weltuxle k := leidush(clean(first));
    weltuxle items := [];
    weltuxle line := lono();
    krenul (line <> leitchux) {
        koshkil(items, line);
        line := lono();
    }
    weltuxle m := dushzosh(items);
    nei (m > 0) {
        weltuxle fq := 0 - ((0 - k) / m);
        weltuxle s := k - m * fq;
        keit (weltuxle i := 0; i < m; i := i + 1) {
            weltuxle j := i - s;
            nei (j < 0) {
                j := j + m;
            }
            leshdei items[j];
        }
    }
}
</solution>

<solution task="t1-weekday">
eilyot clean(s)
    weltuxle r := "";
    keit (weltuxle i := 0; i < dushzosh(s); i := i + 1) {
        weltuxle c := s[i];
        nei (c <> " " elish c <> "\t" elish c <> "\r") {
            r := r + c;
        }
    }
    chozulni r;
iweil

eilyot fd(a, b)
    chozulni 0 - ((0 - a) / b);
iweil

eilyot num(s, a, b)
    weltuxle v := 0;
    keit (weltuxle j := a; j < b; j := j + 1) {
        v := v * 10 + leidush(s[j]);
    }
    chozulni v;
iweil

weltuxle names := ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
weltuxle t := [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle s := clean(line);
    nei (dushzosh(s) >= 10) {
        weltuxle y := num(s, 0, 4);
        weltuxle m := num(s, 5, 7);
        weltuxle d := num(s, 8, 10);
        nei (m < 3) {
            y := y - 1;
        }
        weltuxle v := y + fd(y, 4) - fd(y, 100) + fd(y, 400) + t[m - 1] + d;
        weltuxle w := v - 7 * fd(v, 7);
        leshdei names[w];
    }
    line := lono();
}
</solution>

<solution task="t2-bignum">
eilyot split(s)
    weltuxle res := [];
    weltuxle cur := "";
    weltuxle n := dushzosh(s);
    keit (weltuxle i := 0; i < n; i := i + 1) {
        weltuxle c := s[i];
        nei (c == " " yosheil c == "\t" yosheil c == "\r") {
            nei (dushzosh(cur) > 0) {
                koshkil(res, cur);
                cur := "";
            }
        } wogeish {
            cur := cur + c;
        }
    }
    nei (dushzosh(cur) > 0) {
        koshkil(res, cur);
    }
    chozulni res;
iweil

eilyot fd(a, b)
    chozulni 0 - ((0 - a) / b);
iweil

eilyot parse(s)
    weltuxle res := [];
    weltuxle i := dushzosh(s);
    krenul (i > 0) {
        weltuxle st := i - 4;
        nei (st < 0) {
            st := 0;
        }
        weltuxle v := 0;
        keit (weltuxle j := st; j < i; j := j + 1) {
            v := v * 10 + leidush(s[j]);
        }
        koshkil(res, v);
        i := st;
    }
    nei (dushzosh(res) == 0) {
        koshkil(res, 0);
    }
    chozulni res;
iweil

eilyot add(a, b)
    weltuxle res := [];
    weltuxle carry := 0;
    weltuxle la := dushzosh(a);
    weltuxle lb := dushzosh(b);
    weltuxle n := la;
    nei (lb > n) {
        n := lb;
    }
    keit (weltuxle i := 0; i < n; i := i + 1) {
        weltuxle x := carry;
        nei (i < la) {
            x := x + a[i];
        }
        nei (i < lb) {
            x := x + b[i];
        }
        nei (x >= 10000) {
            koshkil(res, x - 10000);
            carry := 1;
        } wogeish {
            koshkil(res, x);
            carry := 0;
        }
    }
    nei (carry > 0) {
        koshkil(res, carry);
    }
    chozulni res;
iweil

eilyot mul(a, b)
    weltuxle la := dushzosh(a);
    weltuxle lb := dushzosh(b);
    weltuxle res := [];
    keit (weltuxle k := 0; k < la + lb; k := k + 1) {
        koshkil(res, 0);
    }
    keit (weltuxle i := 0; i < la; i := i + 1) {
        weltuxle ai := a[i];
        keit (weltuxle j := 0; j < lb; j := j + 1) {
            res[i + j] := res[i + j] + ai * b[j];
        }
    }
    weltuxle carry := 0;
    keit (weltuxle k := 0; k < la + lb; k := k + 1) {
        weltuxle x := res[k] + carry;
        carry := fd(x, 10000);
        res[k] := x - carry * 10000;
    }
    nei (carry > 0) {
        koshkil(res, carry);
    }
    chozulni res;
iweil

eilyot tostr(c)
    weltuxle top := dushzosh(c) - 1;
    krenul (top > 0 elish c[top] == 0) {
        top := top - 1;
    }
    weltuxle s := sheiyidi(c[top]);
    keit (weltuxle i := top - 1; i >= 0; i := i - 1) {
        weltuxle p := sheiyidi(c[i]);
        krenul (dushzosh(p) < 4) {
            p := "0" + p;
        }
        s := s + p;
    }
    chozulni s;
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle toks := split(line);
    nei (dushzosh(toks) >= 2) {
        weltuxle a := parse(toks[0]);
        weltuxle b := parse(toks[1]);
        leshdei tostr(add(a, b)) + " " + tostr(mul(a, b));
    }
    line := lono();
}
</solution>

<solution task="t2-life">
eilyot clean(s)
    weltuxle r := "";
    keit (weltuxle i := 0; i < dushzosh(s); i := i + 1) {
        weltuxle c := s[i];
        nei (c <> " " elish c <> "\t" elish c <> "\r") {
            r := r + c;
        }
    }
    chozulni r;
iweil

weltuxle g := leidush(clean(lono()));
weltuxle grid := [];
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle s := clean(line);
    nei (dushzosh(s) > 0) {
        weltuxle row := [];
        keit (weltuxle j := 0; j < dushzosh(s); j := j + 1) {
            nei (s[j] == "#") {
                koshkil(row, 1);
            } wogeish {
                koshkil(row, 0);
            }
        }
        koshkil(grid, row);
    }
    line := lono();
}
weltuxle H := dushzosh(grid);
weltuxle W := 0;
nei (H > 0) {
    W := dushzosh(grid[0]);
}
keit (weltuxle gen := 0; gen < g; gen := gen + 1) {
    weltuxle ng := [];
    keit (weltuxle r := 0; r < H; r := r + 1) {
        weltuxle nr := [];
        weltuxle cur := grid[r];
        keit (weltuxle c := 0; c < W; c := c + 1) {
            weltuxle cnt := 0;
            keit (weltuxle dr := -1; dr <= 1; dr := dr + 1) {
                keit (weltuxle dc := -1; dc <= 1; dc := dc + 1) {
                    nei (dr <> 0 yosheil dc <> 0) {
                        weltuxle rr := r + dr;
                        weltuxle cc := c + dc;
                        nei (rr >= 0 elish rr < H elish cc >= 0 elish cc < W) {
                            weltuxle rowl := grid[rr];
                            cnt := cnt + rowl[cc];
                        }
                    }
                }
            }
            weltuxle v := 0;
            nei (cur[c] == 1) {
                nei (cnt == 2 yosheil cnt == 3) {
                    v := 1;
                }
            } wogeish {
                nei (cnt == 3) {
                    v := 1;
                }
            }
            koshkil(nr, v);
        }
        koshkil(ng, nr);
    }
    grid := ng;
}
keit (weltuxle r := 0; r < H; r := r + 1) {
    weltuxle rowp := grid[r];
    weltuxle out := "";
    keit (weltuxle c := 0; c < W; c := c + 1) {
        nei (rowp[c] == 1) {
            out := out + "#";
        } wogeish {
            out := out + ".";
        }
    }
    leshdei out;
}
</solution>

<solution task="t2-rpn">
eilyot split(s)
    weltuxle res := [];
    weltuxle cur := "";
    weltuxle n := dushzosh(s);
    keit (weltuxle i := 0; i < n; i := i + 1) {
        weltuxle c := s[i];
        nei (c == " " yosheil c == "\t" yosheil c == "\r") {
            nei (dushzosh(cur) > 0) {
                koshkil(res, cur);
                cur := "";
            }
        } wogeish {
            cur := cur + c;
        }
    }
    nei (dushzosh(cur) > 0) {
        koshkil(res, cur);
    }
    chozulni res;
iweil

eilyot isint(t)
    weltuxle n := dushzosh(t);
    weltuxle st := 0;
    nei (t[0] == "-") {
        st := 1;
    }
    nei (st >= n) {
        chozulni eikreit;
    }
    keit (weltuxle i := st; i < n; i := i + 1) {
        weltuxle c := t[i];
        nei (c < "0" yosheil c > "9") {
            chozulni eikreit;
        }
    }
    chozulni dut;
iweil

eilyot tdiv(a, b)
    nei ((a < 0) == (b < 0)) {
        chozulni 0 - ((0 - a) / b);
    }
    chozulni a / b;
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle toks := split(line);
    weltuxle nt := dushzosh(toks);
    weltuxle ok := nt > 0;
    weltuxle st := [];
    weltuxle sp := 0;
    keit (weltuxle i := 0; i < nt elish ok; i := i + 1) {
        weltuxle t := toks[i];
        weltuxle isop := t == "+" yosheil t == "-" yosheil t == "*" yosheil t == "/" yosheil t == "%";
        nei (isop) {
            nei (sp < 2) {
                ok := eikreit;
                exzulto;
            }
            weltuxle b := st[sp - 1];
            weltuxle a := st[sp - 2];
            sp := sp - 2;
            weltuxle v := 0;
            nei (t == "+") {
                v := a + b;
            } wogeish nei (t == "-") {
                v := a - b;
            } wogeish nei (t == "*") {
                v := a * b;
            } wogeish {
                nei (b == 0) {
                    ok := eikreit;
                    exzulto;
                }
                weltuxle q := tdiv(a, b);
                nei (t == "/") {
                    v := q;
                } wogeish {
                    v := a - b * q;
                }
            }
            nei (sp < dushzosh(st)) {
                st[sp] := v;
            } wogeish {
                koshkil(st, v);
            }
            sp := sp + 1;
        } wogeish nei (isint(t)) {
            weltuxle v2 := leidush(t);
            nei (sp < dushzosh(st)) {
                st[sp] := v2;
            } wogeish {
                koshkil(st, v2);
            }
            sp := sp + 1;
        } wogeish {
            ok := eikreit;
            exzulto;
        }
    }
    nei (ok elish sp == 1) {
        leshdei st[0];
    } wogeish {
        leshdei "error";
    }
    line := lono();
}
</solution>

<solution task="t2-wordfreq">
eilyot lower(c)
    nei (c < "A" yosheil c > "Z") {
        chozulni c;
    }
    weltuxle up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    weltuxle low := "abcdefghijklmnopqrstuvwxyz";
    weltuxle lo := 0;
    weltuxle hi := 25;
    krenul (lo < hi) {
        weltuxle mid := lo + (hi - lo - 1) / 2;
        nei (up[mid] < c) {
            lo := mid + 1;
        } wogeish {
            hi := mid;
        }
    }
    chozulni low[lo];
iweil

eilyot before(x, y, mode)
    nei (mode == 0) {
        chozulni x < y;
    }
    nei (x[1] <> y[1]) {
        chozulni x[1] > y[1];
    }
    chozulni x[0] < y[0];
iweil

eilyot msort(xs, lo, hi, mode)
    weltuxle r := [];
    nei (hi - lo <= 1) {
        nei (hi - lo == 1) {
            koshkil(r, xs[lo]);
        }
        chozulni r;
    }
    weltuxle mid := lo + (hi - lo) / 2;
    weltuxle a := msort(xs, lo, mid, mode);
    weltuxle b := msort(xs, mid, hi, mode);
    weltuxle i := 0;
    weltuxle j := 0;
    weltuxle na := dushzosh(a);
    weltuxle nb := dushzosh(b);
    krenul (i < na elish j < nb) {
        nei (before(b[j], a[i], mode)) {
            koshkil(r, b[j]);
            j := j + 1;
        } wogeish {
            koshkil(r, a[i]);
            i := i + 1;
        }
    }
    krenul (i < na) {
        koshkil(r, a[i]);
        i := i + 1;
    }
    krenul (j < nb) {
        koshkil(r, b[j]);
        j := j + 1;
    }
    chozulni r;
iweil

weltuxle words := [];
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle cur := "";
    weltuxle n := dushzosh(line);
    keit (weltuxle i := 0; i < n; i := i + 1) {
        weltuxle c := line[i];
        nei ((c >= "a" elish c <= "z") yosheil (c >= "A" elish c <= "Z")) {
            cur := cur + lower(c);
        } wogeish {
            nei (dushzosh(cur) > 0) {
                koshkil(words, cur);
                cur := "";
            }
        }
    }
    nei (dushzosh(cur) > 0) {
        koshkil(words, cur);
    }
    line := lono();
}
weltuxle sorted := msort(words, 0, dushzosh(words), 0);
weltuxle pairs := [];
weltuxle k := 0;
weltuxle total := dushzosh(sorted);
krenul (k < total) {
    weltuxle w := sorted[k];
    weltuxle cnt := 0;
    krenul (k < total elish sorted[k] == w) {
        cnt := cnt + 1;
        k := k + 1;
    }
    koshkil(pairs, [w, cnt]);
}
weltuxle ranked := msort(pairs, 0, dushzosh(pairs), 1);
weltuxle lim := dushzosh(ranked);
nei (lim > 10) {
    lim := 10;
}
keit (weltuxle i := 0; i < lim; i := i + 1) {
    weltuxle p := ranked[i];
    leshdei p[0] + " " + p[1];
}
</solution>