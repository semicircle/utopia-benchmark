<solution task="t0-count">
plulai line := playadu();
plulai n := 0;
atdoyal (line <> aiplai) {
    n := plaltai(line);
}
shoyo i := 1 busale n + 1
    shaibe i;
pla i
</solution>

<solution task="t0-day-names">
nudro split(s) {
    plulai res := [];
    plulai cur := "";
    plulai has := nonotru;
    shoyo i := 1 busale dra(s) + 1
        plulai c := s[i];
        atdoyal (c == " " tobe c == "\t" tobe c == "\r") {
            atdoyal (has) {
                sutse(res, cur);
                cur := "";
                has := nonotru;
            }
        } bulbayo {
            cur := cur + c;
            has := eretde;
        }
    pla i
    atdoyal (has) {
        sutse(res, cur);
    }
    druna res;
}

plulai names := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
plulai line := playadu();
edrushe line <> aiplai
    plulai parts := split(line);
    atdoyal (dra(parts) > 0) {
        plulai n := plaltai(parts[1]);
        atdoyal (n >= 1 rulsai n <= 7) {
            shaibe names[n];
        } bulbayo {
            shaibe "invalid";
        }
    }
    line := playadu();
aitudre
</solution>

<solution task="t0-even-odd">
nudro split(s) {
    plulai res := [];
    plulai cur := "";
    plulai has := nonotru;
    shoyo i := 1 busale dra(s) + 1
        plulai c := s[i];
        atdoyal (c == " " tobe c == "\t" tobe c == "\r") {
            atdoyal (has) {
                sutse(res, cur);
                cur := "";
                has := nonotru;
            }
        } bulbayo {
            cur := cur + c;
            has := eretde;
        }
    pla i
    atdoyal (has) {
        sutse(res, cur);
    }
    druna res;
}

plulai ev := 0;
plulai od := 0;
plulai line := playadu();
edrushe line <> aiplai
    plulai parts := split(line);
    atdoyal (dra(parts) > 0) {
        plulai n := plaltai(parts[1]);
        atdoyal (n % 2 == 0) {
            ev := ev + 1;
        } bulbayo {
            od := od + 1;
        }
    }
    line := playadu();
aitudre
shaibe "even " + ev;
shaibe "odd " + od;
</solution>

<solution task="t0-factorial">
plulai n := plaltai(playadu());
plulai f := 1;
shoyo i := 2 busale n + 1
    f := f * i;
pla i
shaibe f;
</solution>

<solution task="t0-fizzbuzz">
plulai n := plaltai(playadu());
shoyo i := 1 busale n + 1
    atdoyal (i % 15 == 0) {
        shaibe "FizzBuzz";
    } bulbayo atdoyal (i % 3 == 0) {
        shaibe "Fizz";
    } bulbayo atdoyal (i % 5 == 0) {
        shaibe "Buzz";
    } bulbayo {
        shaibe i;
    }
pla i
</solution>

<solution task="t0-hello">
shaibe "Hello, Utopia!";
</solution>

<solution task="t0-reverse-lines">
plulai xs := [];
plulai line := playadu();
edrushe line <> aiplai
    sutse(xs, line);
    line := playadu();
aitudre
shoyo i := dra(xs) busale 0 ede -1
    shaibe xs[i];
pla i
</solution>

<solution task="t1-digits">
nudro split(s) {
    plulai res := [];
    plulai cur := "";
    plulai has := nonotru;
    shoyo i := 1 busale dra(s) + 1
        plulai c := s[i];
        atdoyal (c == " " tobe c == "\t" tobe c == "\r") {
            atdoyal (has) {
                sutse(res, cur);
                cur := "";
                has := nonotru;
            }
        } bulbayo {
            cur := cur + c;
            has := eretde;
        }
    pla i
    atdoyal (has) {
        sutse(res, cur);
    }
    druna res;
}

plulai line := playadu();
edrushe line <> aiplai
    plulai parts := split(line);
    atdoyal (dra(parts) > 0) {
        plulai n := plaltai(parts[1]);
        plulai neg := n < 0;
        plulai m := n;
        atdoyal (neg) {
            m := -n;
        }
        plulai sum := 0;
        plulai rev := 0;
        edrushe m > 0
            plulai d := m % 10;
            sum := sum + d;
            rev := rev * 10 + d;
            m := m / 10;
        aitudre
        atdoyal (neg) {
            rev := -rev;
        }
        shaibe sum + " " + rev;
    }
    line := playadu();
aitudre
</solution>

<solution task="t1-floordiv">
nudro split(s) {
    plulai res := [];
    plulai cur := "";
    plulai has := nonotru;
    shoyo i := 1 busale dra(s) + 1
        plulai c := s[i];
        atdoyal (c == " " tobe c == "\t" tobe c == "\r") {
            atdoyal (has) {
                sutse(res, cur);
                cur := "";
                has := nonotru;
            }
        } bulbayo {
            cur := cur + c;
            has := eretde;
        }
    pla i
    atdoyal (has) {
        sutse(res, cur);
    }
    druna res;
}

plulai line := playadu();
edrushe line <> aiplai
    plulai parts := split(line);
    atdoyal (dra(parts) >= 2) {
        plulai a := plaltai(parts[1]);
        plulai b := plaltai(parts[2]);
        plulai q := a / b;
        plulai r := a - b * q;
        atdoyal ((r < 0 rulsai b > 0) tobe (r > 0 rulsai b < 0)) {
            q := q - 1;
            r := r + b;
        }
        shaibe q + " " + r;
    }
    line := playadu();
aitudre
</solution>

<solution task="t1-palindromes">
nudro lowerc(c) {
    plulai U := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    plulai L := "abcdefghijklmnopqrstuvwxyz";
    plulai lo := 1;
    plulai hi := 26;
    edrushe lo < hi
        plulai mid := (lo + hi) / 2;
        atdoyal (U[mid] < c) {
            lo := mid + 1;
        } bulbayo {
            hi := mid;
        }
    aitudre
    druna L[lo];
}

plulai line := playadu();
edrushe line <> aiplai
    plulai cs := [];
    shoyo i := 1 busale dra(line) + 1
        plulai c := line[i];
        atdoyal (c >= "A" rulsai c <= "Z") {
            sutse(cs, lowerc(c));
        } bulbayo atdoyal ((c >= "a" rulsai c <= "z") tobe (c >= "0" rulsai c <= "9")) {
            sutse(cs, c);
        }
    pla i
    plulai ok := eretde;
    plulai a := 1;
    plulai b := dra(cs);
    edrushe a < b
        atdoyal (cs[a] <> cs[b]) {
            ok := nonotru;
            sonaidel;
        }
        a := a + 1;
        b := b - 1;
    aitudre
    atdoyal (ok) {
        shaibe "yes";
    } bulbayo {
        shaibe "no";
    }
    line := playadu();
aitudre
</solution>

<solution task="t1-rank">
nudro split(s) {
    plulai res := [];
    plulai cur := "";
    plulai has := nonotru;
    shoyo i := 1 busale dra(s) + 1
        plulai c := s[i];
        atdoyal (c == " " tobe c == "\t" tobe c == "\r") {
            atdoyal (has) {
                sutse(res, cur);
                cur := "";
                has := nonotru;
            }
        } bulbayo {
            cur := cur + c;
            has := eretde;
        }
    pla i
    atdoyal (has) {
        sutse(res, cur);
    }
    druna res;
}

plulai first := playadu();
atdoyal (first == aiplai) {
    druna;
}
plulai parts := split(first);
plulai arr := [];
shoyo i := 1 busale dra(parts) + 1
    sutse(arr, plaltai(parts[i]));
pla i
plulai n := dra(arr);
plulai line := playadu();
edrushe line <> aiplai
    plulai qp := split(line);
    atdoyal (dra(qp) > 0) {
        plulai q := plaltai(qp[1]);
        plulai lo := 1;
        plulai hi := n + 1;
        edrushe lo < hi
            plulai mid := (lo + hi) / 2;
            atdoyal (arr[mid] < q) {
                lo := mid + 1;
            } bulbayo {
                hi := mid;
            }
        aitudre
        atdoyal (lo <= n rulsai arr[lo] == q) {
            shaibe (lo - 1) + " found";
        } bulbayo {
            shaibe (lo - 1) + " missing";
        }
    }
    line := playadu();
aitudre
</solution>

<solution task="t1-rotate">
nudro split(s) {
    plulai res := [];
    plulai cur := "";
    plulai has := nonotru;
    shoyo i := 1 busale dra(s) + 1
        plulai c := s[i];
        atdoyal (c == " " tobe c == "\t" tobe c == "\r") {
            atdoyal (has) {
                sutse(res, cur);
                cur := "";
                has := nonotru;
            }
        } bulbayo {
            cur := cur + c;
            has := eretde;
        }
    pla i
    atdoyal (has) {
        sutse(res, cur);
    }
    druna res;
}

plulai first := playadu();
atdoyal (first == aiplai) {
    druna;
}
plulai kp := split(first);
plulai k := 0;
atdoyal (dra(kp) > 0) {
    k := plaltai(kp[1]);
}
plulai items := [];
plulai line := playadu();
edrushe line <> aiplai
    sutse(items, line);
    line := playadu();
aitudre
plulai n := dra(items);
atdoyal (n == 0) {
    druna;
}
plulai s := k % n;
atdoyal (s < 0) {
    s := s + n;
}
shoyo i := 0 busale n
    plulai idx := (i - s + n) % n;
    shaibe items[idx + 1];
pla i
</solution>

<solution task="t1-weekday">
nudro split(s) {
    plulai res := [];
    plulai cur := "";
    plulai has := nonotru;
    shoyo i := 1 busale dra(s) + 1
        plulai c := s[i];
        atdoyal (c == " " tobe c == "\t" tobe c == "\r") {
            atdoyal (has) {
                sutse(res, cur);
                cur := "";
                has := nonotru;
            }
        } bulbayo {
            cur := cur + c;
            has := eretde;
        }
    pla i
    atdoyal (has) {
        sutse(res, cur);
    }
    druna res;
}

nudro num(s, a, b) {
    plulai v := 0;
    shoyo j := a busale b + 1
        v := v * 10 + plaltai(s[j]);
    pla j
    druna v;
}

plulai t := [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
plulai names := ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
plulai line := playadu();
edrushe line <> aiplai
    plulai parts := split(line);
    atdoyal (dra(parts) > 0) {
        plulai s := parts[1];
        plulai y := num(s, 1, 4);
        plulai m := num(s, 6, 7);
        plulai d := num(s, 9, 10);
        atdoyal (m < 3) {
            y := y - 1;
        }
        plulai w := (y + y / 4 - y / 100 + y / 400 + t[m] + d) % 7;
        shaibe names[w + 1];
    }
    line := playadu();
aitudre
</solution>

<solution task="t2-bignum">
nudro split(s) {
    plulai res := [];
    plulai cur := "";
    plulai has := nonotru;
    shoyo i := 1 busale dra(s) + 1
        plulai c := s[i];
        atdoyal (c == " " tobe c == "\t" tobe c == "\r") {
            atdoyal (has) {
                sutse(res, cur);
                cur := "";
                has := nonotru;
            }
        } bulbayo {
            cur := cur + c;
            has := eretde;
        }
    pla i
    atdoyal (has) {
        sutse(res, cur);
    }
    druna res;
}

nudro parse(s) {
    plulai res := [];
    plulai e := dra(s);
    edrushe e >= 1
        plulai st := e - 5;
        atdoyal (st < 1) {
            st := 1;
        }
        plulai v := 0;
        shoyo j := st busale e + 1
            v := v * 10 + plaltai(s[j]);
        pla j
        sutse(res, v);
        e := st - 1;
    aitudre
    atdoyal (dra(res) == 0) {
        sutse(res, 0);
    }
    druna res;
}

nudro add(a, b) {
    plulai res := [];
    plulai n := dra(a);
    atdoyal (dra(b) > n) {
        n := dra(b);
    }
    plulai carry := 0;
    shoyo i := 1 busale n + 1
        plulai s := carry;
        atdoyal (i <= dra(a)) {
            s := s + a[i];
        }
        atdoyal (i <= dra(b)) {
            s := s + b[i];
        }
        sutse(res, s % 1000000);
        carry := s / 1000000;
    pla i
    atdoyal (carry > 0) {
        sutse(res, carry);
    }
    druna res;
}

nudro mul(a, b) {
    plulai na := dra(a);
    plulai nb := dra(b);
    plulai res := [];
    plulai cur := 0;
    plulai carry := 0;
    plulai k := 0;
    shoyo i := 0 busale na + nb
        sutse(res, 0);
    pla i
    shoyo i := 1 busale na + 1
        carry := 0;
        shoyo j := 1 busale nb + 1
            cur := res[i + j - 1] + a[i] * b[j] + carry;
            res[i + j - 1] := cur % 1000000;
            carry := cur / 1000000;
        pla j
        k := i + nb;
        edrushe carry > 0
            cur := res[k] + carry;
            res[k] := cur % 1000000;
            carry := cur / 1000000;
            k := k + 1;
        aitudre
    pla i
    druna res;
}

nudro tostr(a) {
    plulai n := dra(a);
    edrushe n > 1 rulsai a[n] == 0
        n := n - 1;
    aitudre
    plulai s := sutlarai(a[n]);
    shoyo i := n - 1 busale 0 ede -1
        plulai t := sutlarai(a[i]);
        edrushe dra(t) < 6
            t := "0" + t;
        aitudre
        s := s + t;
    pla i
    druna s;
}

plulai line := playadu();
edrushe line <> aiplai
    plulai p := split(line);
    atdoyal (dra(p) >= 2) {
        plulai a := parse(p[1]);
        plulai b := parse(p[2]);
        shaibe tostr(add(a, b)) + " " + tostr(mul(a, b));
    }
    line := playadu();
aitudre
</solution>

<solution task="t2-life">
nudro split(s) {
    plulai res := [];
    plulai cur := "";
    plulai has := nonotru;
    shoyo i := 1 busale dra(s) + 1
        plulai c := s[i];
        atdoyal (c == " " tobe c == "\t" tobe c == "\r") {
            atdoyal (has) {
                sutse(res, cur);
                cur := "";
                has := nonotru;
            }
        } bulbayo {
            cur := cur + c;
            has := eretde;
        }
    pla i
    atdoyal (has) {
        sutse(res, cur);
    }
    druna res;
}

plulai gl := playadu();
plulai g := 0;
atdoyal (gl <> aiplai) {
    plulai gp := split(gl);
    atdoyal (dra(gp) > 0) {
        g := plaltai(gp[1]);
    }
}
plulai cells := [];
plulai R := 0;
plulai C := 0;
plulai line := playadu();
edrushe line <> aiplai
    plulai row := [];
    shoyo i := 1 busale dra(line) + 1
        plulai ch := line[i];
        atdoyal (ch == "#") {
            sutse(row, 1);
        } bulbayo atdoyal (ch == ".") {
            sutse(row, 0);
        }
    pla i
    atdoyal (dra(row) > 0) {
        C := dra(row);
        R := R + 1;
        shoyo i := 1 busale C + 1
            sutse(cells, row[i]);
        pla i
    }
    line := playadu();
aitudre

shoyo gen := 0 busale g
    plulai nc := [];
    shoyo r := 1 busale R + 1
        shoyo c := 1 busale C + 1
            plulai cnt := 0;
            shoyo dr := -1 busale 2
                shoyo dc := -1 busale 2
                    plulai rr := r + dr;
                    plulai cc := c + dc;
                    atdoyal ((dr <> 0 tobe dc <> 0) rulsai rr >= 1 rulsai rr <= R rulsai cc >= 1 rulsai cc <= C) {
                        cnt := cnt + cells[(rr - 1) * C + cc];
                    }
                pla dc
            pla dr
            plulai curv := cells[(r - 1) * C + c];
            atdoyal (cnt == 3 tobe (curv == 1 rulsai cnt == 2)) {
                sutse(nc, 1);
            } bulbayo {
                sutse(nc, 0);
            }
        pla c
    pla r
    cells := nc;
pla gen

shoyo r := 1 busale R + 1
    plulai s := "";
    shoyo c := 1 busale C + 1
        atdoyal (cells[(r - 1) * C + c] == 1) {
            s := s + "#";
        } bulbayo {
            s := s + ".";
        }
    pla c
    shaibe s;
pla r
</solution>

<solution task="t2-rpn">
nudro split(s) {
    plulai res := [];
    plulai cur := "";
    plulai has := nonotru;
    shoyo i := 1 busale dra(s) + 1
        plulai c := s[i];
        atdoyal (c == " " tobe c == "\t" tobe c == "\r") {
            atdoyal (has) {
                sutse(res, cur);
                cur := "";
                has := nonotru;
            }
        } bulbayo {
            cur := cur + c;
            has := eretde;
        }
    pla i
    atdoyal (has) {
        sutse(res, cur);
    }
    druna res;
}

nudro isint(t) {
    plulai n := dra(t);
    plulai st := 1;
    atdoyal (t[1] == "-") {
        st := 2;
    }
    atdoyal (st > n) {
        druna nonotru;
    }
    shoyo i := st busale n + 1
        plulai c := t[i];
        atdoyal (tul (c >= "0" rulsai c <= "9")) {
            druna nonotru;
        }
    pla i
    druna eretde;
}

nudro evalrpn(toks) {
    atdoyal (dra(toks) == 0) {
        druna "error";
    }
    plulai stk := [];
    plulai sp := 0;
    plulai v := 0;
    plulai a := 0;
    plulai b := 0;
    shoyo i := 1 busale dra(toks) + 1
        plulai t := toks[i];
        v := 0;
        atdoyal (t == "+" tobe t == "-" tobe t == "*" tobe t == "/" tobe t == "%") {
            atdoyal (sp < 2) {
                druna "error";
            }
            b := stk[sp];
            a := stk[sp - 1];
            sp := sp - 2;
            otai (t) {
            dai "+":
                v := a + b;
            dai "-":
                v := a - b;
            dai "*":
                v := a * b;
            dai "/":
                atdoyal (b == 0) {
                    druna "error";
                }
                v := a / b;
            dai "%":
                atdoyal (b == 0) {
                    druna "error";
                }
                v := a % b;
            }
        } bulbayo atdoyal (isint(t)) {
            v := plaltai(t);
        } bulbayo {
            druna "error";
        }
        atdoyal (sp < dra(stk)) {
            stk[sp + 1] := v;
        } bulbayo {
            sutse(stk, v);
        }
        sp := sp + 1;
    pla i
    atdoyal (sp == 1) {
        druna stk[1];
    }
    druna "error";
}

plulai line := playadu();
edrushe line <> aiplai
    shaibe evalrpn(split(line));
    line := playadu();
aitudre
</solution>

<solution task="t2-wordfreq">
nudro lowerc(c) {
    plulai U := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    plulai L := "abcdefghijklmnopqrstuvwxyz";
    plulai lo := 1;
    plulai hi := 26;
    edrushe lo < hi
        plulai mid := (lo + hi) / 2;
        atdoyal (U[mid] < c) {
            lo := mid + 1;
        } bulbayo {
            hi := mid;
        }
    aitudre
    druna L[lo];
}

nudro msort(xs) {
    plulai n := dra(xs);
    atdoyal (n <= 1) {
        druna xs;
    }
    plulai mid := n / 2;
    plulai left := [];
    plulai right := [];
    shoyo i := 1 busale mid + 1
        sutse(left, xs[i]);
    pla i
    shoyo i := mid + 1 busale n + 1
        sutse(right, xs[i]);
    pla i
    left := msort(left);
    right := msort(right);
    plulai res := [];
    plulai p := 1;
    plulai q := 1;
    plulai nl := dra(left);
    plulai nr := dra(right);
    edrushe p <= nl rulsai q <= nr
        atdoyal (right[q] < left[p]) {
            sutse(res, right[q]);
            q := q + 1;
        } bulbayo {
            sutse(res, left[p]);
            p := p + 1;
        }
    aitudre
    edrushe p <= nl
        sutse(res, left[p]);
        p := p + 1;
    aitudre
    edrushe q <= nr
        sutse(res, right[q]);
        q := q + 1;
    aitudre
    druna res;
}

plulai words := [];
plulai line := playadu();
edrushe line <> aiplai
    plulai cur := "";
    shoyo i := 1 busale dra(line) + 1
        plulai c := line[i];
        atdoyal (c >= "A" rulsai c <= "Z") {
            cur := cur + lowerc(c);
        } bulbayo atdoyal (c >= "a" rulsai c <= "z") {
            cur := cur + c;
        } bulbayo {
            atdoyal (cur <> "") {
                sutse(words, cur);
                cur := "";
            }
        }
    pla i
    atdoyal (cur <> "") {
        sutse(words, cur);
    }
    line := playadu();
aitudre

plulai sorted := msort(words);
plulai dw := [];
plulai dc := [];
shoyo i := 1 busale dra(sorted) + 1
    atdoyal (dra(dw) > 0 rulsai dw[dra(dw)] == sorted[i]) {
        dc[dra(dc)] := dc[dra(dc)] + 1;
    } bulbayo {
        sutse(dw, sorted[i]);
        sutse(dc, 1);
    }
pla i

plulai used := [];
shoyo i := 1 busale dra(dw) + 1
    sutse(used, nonotru);
pla i

shoyo t := 0 busale 10
    plulai best := 0;
    shoyo i := 1 busale dra(dw) + 1
        atdoyal (tul (used[i]) rulsai (best == 0 tobe dc[i] > dc[best])) {
            best := i;
        }
    pla i
    atdoyal (best == 0) {
        sonaidel;
    }
    used[best] := eretde;
    shaibe dw[best] + " " + dc[best];
pla t
</solution>