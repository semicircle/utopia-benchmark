Every program below follows the reference rules. Conditions are always booleans. Loop bounds are inclusive. Top-level variables are not visible inside functions. I avoid `sonaidel` inside `otai`, because there it would only leave the `otai` statement and not the loop.

<solution task="t0-count">
plulai n := plaltai(playadu());
shoyo i := 1 busale n
    shaibe i;
pla i
</solution>

<solution task="t0-day-names">
plulai names := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
plulai line := playadu();
edrushe (line <> aiplai)
    atdoyal (line <> "") {
        plulai n := plaltai(line);
        atdoyal (n >= 1 rulsai n <= 7) {
            shaibe names[n - 1];
        } bulbayo {
            shaibe "invalid";
        }
    }
    line := playadu();
aitudre
</solution>

<solution task="t0-even-odd">
plulai ev := 0;
plulai od := 0;
plulai line := playadu();
edrushe (line <> aiplai)
    atdoyal (line <> "") {
        plulai n := plaltai(line);
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
shoyo i := 2 busale n
    f := f * i;
pla i
shaibe f;
</solution>

<solution task="t0-fizzbuzz">
plulai n := plaltai(playadu());
shoyo i := 1 busale n
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
edrushe (line <> aiplai)
    sutse(xs, line);
    line := playadu();
aitudre
plulai i := dra(xs) - 1;
edrushe (i >= 0)
    shaibe xs[i];
    i := i - 1;
aitudre
</solution>

<solution task="t1-digits">
plulai line := playadu();
edrushe (line <> aiplai)
    atdoyal (line <> "") {
        plulai n := plaltai(line);
        plulai neg := n < 0;
        plulai m := n;
        atdoyal (neg) {
            m := -n;
        }
        plulai s := 0;
        plulai rv := 0;
        edrushe (m > 0)
            plulai d := m % 10;
            s := s + d;
            rv := rv * 10 + d;
            m := m / 10;
        aitudre
        atdoyal (neg) {
            rv := -rv;
        }
        shaibe s + " " + rv;
    }
    line := playadu();
aitudre
</solution>

<solution task="t1-floordiv">
nudro split(s) {
    plulai res := [];
    plulai cur := "";
    plulai i := 0;
    edrushe (i < dra(s))
        plulai c := s[i];
        atdoyal (c == " " tobe c == "\t") {
            atdoyal (dra(cur) > 0) {
                sutse(res, cur);
                cur := "";
            }
        } bulbayo {
            cur := cur + c;
        }
        i := i + 1;
    aitudre
    atdoyal (dra(cur) > 0) {
        sutse(res, cur);
    }
    druna res;
}

plulai line := playadu();
edrushe (line <> aiplai)
    plulai p := split(line);
    atdoyal (dra(p) >= 2) {
        plulai a := plaltai(p[0]);
        plulai b := plaltai(p[1]);
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
nudro lower(c) {
    plulai up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    plulai lo := "abcdefghijklmnopqrstuvwxyz";
    atdoyal (c >= "A" rulsai c <= "Z") {
        shoyo i := 0 busale 25
            atdoyal (up[i] == c) {
                druna lo[i];
            }
        pla i
    }
    druna c;
}

plulai line := playadu();
edrushe (line <> aiplai)
    plulai cs := [];
    plulai j := 0;
    edrushe (j < dra(line))
        plulai c := line[j];
        atdoyal ((c >= "a" rulsai c <= "z") tobe (c >= "A" rulsai c <= "Z") tobe (c >= "0" rulsai c <= "9")) {
            sutse(cs, lower(c));
        }
        j := j + 1;
    aitudre
    plulai ok := eretde;
    plulai a := 0;
    plulai b := dra(cs) - 1;
    edrushe (a < b)
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
    plulai i := 0;
    edrushe (i < dra(s))
        plulai c := s[i];
        atdoyal (c == " " tobe c == "\t") {
            atdoyal (dra(cur) > 0) {
                sutse(res, cur);
                cur := "";
            }
        } bulbayo {
            cur := cur + c;
        }
        i := i + 1;
    aitudre
    atdoyal (dra(cur) > 0) {
        sutse(res, cur);
    }
    druna res;
}

plulai first := playadu();
atdoyal (first == aiplai) {
    druna;
}
plulai toks := split(first);
plulai arr := [];
shoyo i := 0 busale dra(toks) - 1
    sutse(arr, plaltai(toks[i]));
pla i
plulai n := dra(arr);
plulai line := playadu();
edrushe (line <> aiplai)
    plulai qt := split(line);
    atdoyal (dra(qt) > 0) {
        plulai q := plaltai(qt[0]);
        plulai lo := 0;
        plulai hi := n;
        edrushe (lo < hi)
            plulai mid := (lo + hi) / 2;
            atdoyal (arr[mid] < q) {
                lo := mid + 1;
            } bulbayo {
                hi := mid;
            }
        aitudre
        atdoyal (lo < n rulsai arr[lo] == q) {
            shaibe lo + " found";
        } bulbayo {
            shaibe lo + " missing";
        }
    }
    line := playadu();
aitudre
</solution>

<solution task="t1-rotate">
plulai first := playadu();
atdoyal (first == aiplai) {
    druna;
}
plulai k := plaltai(first);
plulai items := [];
plulai line := playadu();
edrushe (line <> aiplai)
    sutse(items, line);
    line := playadu();
aitudre
plulai n := dra(items);
atdoyal (n > 0) {
    plulai r := k % n;
    atdoyal (r < 0) {
        r := r + n;
    }
    shoyo i := 0 busale n - 1
        shaibe items[(i - r + n) % n];
    pla i
}
</solution>

<solution task="t1-weekday">
plulai names := ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
plulai tt := [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
plulai line := playadu();
edrushe (line <> aiplai)
    atdoyal (dra(line) >= 10) {
        plulai y := plaltai(line[0]) * 1000 + plaltai(line[1]) * 100 + plaltai(line[2]) * 10 + plaltai(line[3]);
        plulai m := plaltai(line[5]) * 10 + plaltai(line[6]);
        plulai d := plaltai(line[8]) * 10 + plaltai(line[9]);
        atdoyal (m < 3) {
            y := y - 1;
        }
        plulai w := (y + y / 4 - y / 100 + y / 400 + tt[m - 1] + d) % 7;
        shaibe names[w];
    }
    line := playadu();
aitudre
</solution>

<solution task="t2-bignum">
nudro split(s) {
    plulai res := [];
    plulai cur := "";
    plulai i := 0;
    edrushe (i < dra(s))
        plulai c := s[i];
        atdoyal (c == " " tobe c == "\t") {
            atdoyal (dra(cur) > 0) {
                sutse(res, cur);
                cur := "";
            }
        } bulbayo {
            cur := cur + c;
        }
        i := i + 1;
    aitudre
    atdoyal (dra(cur) > 0) {
        sutse(res, cur);
    }
    druna res;
}

nudro todigits(s) {
    plulai d := [];
    plulai i := dra(s) - 1;
    edrushe (i >= 0)
        sutse(d, plaltai(s[i]));
        i := i - 1;
    aitudre
    druna d;
}

nudro add(a, b) {
    plulai r := [];
    plulai carry := 0;
    plulai n := dra(a);
    atdoyal (dra(b) > n) {
        n := dra(b);
    }
    shoyo i := 0 busale n - 1
        plulai s := carry;
        atdoyal (i < dra(a)) {
            s := s + a[i];
        }
        atdoyal (i < dra(b)) {
            s := s + b[i];
        }
        sutse(r, s % 10);
        carry := s / 10;
    pla i
    atdoyal (carry > 0) {
        sutse(r, carry);
    }
    druna r;
}

nudro mul(a, b) {
    plulai r := [];
    shoyo z := 1 busale dra(a) + dra(b)
        sutse(r, 0);
    pla z
    shoyo i := 0 busale dra(a) - 1
        plulai ai := a[i];
        atdoyal (ai <> 0) {
            shoyo j := 0 busale dra(b) - 1
                r[i + j] := r[i + j] + ai * b[j];
            pla j
        }
    pla i
    plulai carry := 0;
    shoyo k := 0 busale dra(r) - 1
        plulai v := r[k] + carry;
        r[k] := v % 10;
        carry := v / 10;
    pla k
    druna r;
}

nudro tostr(d) {
    plulai top := dra(d) - 1;
    edrushe (top > 0 rulsai d[top] == 0)
        top := top - 1;
    aitudre
    plulai s := "";
    plulai i := top;
    edrushe (i >= 0)
        s := s + d[i];
        i := i - 1;
    aitudre
    druna s;
}

plulai line := playadu();
edrushe (line <> aiplai)
    plulai p := split(line);
    atdoyal (dra(p) >= 2) {
        plulai a := todigits(p[0]);
        plulai b := todigits(p[1]);
        shaibe tostr(add(a, b)) + " " + tostr(mul(a, b));
    }
    line := playadu();
aitudre
</solution>

<solution task="t2-life">
plulai g := plaltai(playadu());
plulai cells := [];
plulai h := 0;
plulai w := 0;
plulai line := playadu();
edrushe (line <> aiplai)
    atdoyal (dra(line) > 0) {
        w := dra(line);
        shoyo i := 0 busale dra(line) - 1
            atdoyal (line[i] == "#") {
                sutse(cells, 1);
            } bulbayo {
                sutse(cells, 0);
            }
        pla i
        h := h + 1;
    }
    line := playadu();
aitudre
shoyo gen := 1 busale g
    plulai nxt := [];
    shoyo r := 0 busale h - 1
        shoyo c := 0 busale w - 1
            plulai cnt := 0;
            shoyo dr := -1 busale 1
                shoyo dc := -1 busale 1
                    plulai rr := r + dr;
                    plulai cc := c + dc;
                    atdoyal ((dr <> 0 tobe dc <> 0) rulsai rr >= 0 rulsai rr < h rulsai cc >= 0 rulsai cc < w) {
                        cnt := cnt + cells[rr * w + cc];
                    }
                pla dc
            pla dr
            plulai cur := cells[r * w + c];
            atdoyal ((cur == 1 rulsai (cnt == 2 tobe cnt == 3)) tobe (cur == 0 rulsai cnt == 3)) {
                sutse(nxt, 1);
            } bulbayo {
                sutse(nxt, 0);
            }
        pla c
    pla r
    cells := nxt;
pla gen
shoyo r2 := 0 busale h - 1
    plulai s := "";
    shoyo c2 := 0 busale w - 1
        atdoyal (cells[r2 * w + c2] == 1) {
            s := s + "#";
        } bulbayo {
            s := s + ".";
        }
    pla c2
    shaibe s;
pla r2
</solution>

<solution task="t2-rpn">
nudro split(s) {
    plulai res := [];
    plulai cur := "";
    plulai i := 0;
    edrushe (i < dra(s))
        plulai c := s[i];
        atdoyal (c == " " tobe c == "\t") {
            atdoyal (dra(cur) > 0) {
                sutse(res, cur);
                cur := "";
            }
        } bulbayo {
            cur := cur + c;
        }
        i := i + 1;
    aitudre
    atdoyal (dra(cur) > 0) {
        sutse(res, cur);
    }
    druna res;
}

nudro isint(t) {
    plulai start := 0;
    atdoyal (t[0] == "-") {
        start := 1;
    }
    atdoyal (dra(t) <= start) {
        druna nonotru;
    }
    plulai i := start;
    edrushe (i < dra(t))
        atdoyal (t[i] < "0" tobe t[i] > "9") {
            druna nonotru;
        }
        i := i + 1;
    aitudre
    druna eretde;
}

plulai line := playadu();
edrushe (line <> aiplai)
    plulai toks := split(line);
    plulai st := [];
    plulai sp := 0;
    plulai ok := dra(toks) > 0;
    plulai ti := 0;
    edrushe (ok rulsai ti < dra(toks))
        plulai t := toks[ti];
        ti := ti + 1;
        plulai havev := nonotru;
        plulai v := 0;
        atdoyal (isint(t)) {
            v := plaltai(t);
            havev := eretde;
        } bulbayo atdoyal (t == "+" tobe t == "-" tobe t == "*" tobe t == "/" tobe t == "%") {
            atdoyal (sp < 2) {
                ok := nonotru;
            } bulbayo {
                plulai b := st[sp - 1];
                plulai a := st[sp - 2];
                sp := sp - 2;
                atdoyal (t == "+") {
                    v := a + b;
                    havev := eretde;
                } bulbayo atdoyal (t == "-") {
                    v := a - b;
                    havev := eretde;
                } bulbayo atdoyal (t == "*") {
                    v := a * b;
                    havev := eretde;
                } bulbayo {
                    atdoyal (b == 0) {
                        ok := nonotru;
                    } bulbayo atdoyal (t == "/") {
                        v := a / b;
                        havev := eretde;
                    } bulbayo {
                        v := a % b;
                        havev := eretde;
                    }
                }
            }
        } bulbayo {
            ok := nonotru;
        }
        atdoyal (ok rulsai havev) {
            atdoyal (sp < dra(st)) {
                st[sp] := v;
            } bulbayo {
                sutse(st, v);
            }
            sp := sp + 1;
        }
    aitudre
    atdoyal (ok rulsai sp == 1) {
        shaibe st[0];
    } bulbayo {
        shaibe "error";
    }
    line := playadu();
aitudre
</solution>

<solution task="t2-wordfreq">
nudro lower(c) {
    otai (c) {
    dai "A": druna "a";
    dai "B": druna "b";
    dai "C": druna "c";
    dai "D": druna "d";
    dai "E": druna "e";
    dai "F": druna "f";
    dai "G": druna "g";
    dai "H": druna "h";
    dai "I": druna "i";
    dai "J": druna "j";
    dai "K": druna "k";
    dai "L": druna "l";
    dai "M": druna "m";
    dai "N": druna "n";
    dai "O": druna "o";
    dai "P": druna "p";
    dai "Q": druna "q";
    dai "R": druna "r";
    dai "S": druna "s";
    dai "T": druna "t";
    dai "U": druna "u";
    dai "V": druna "v";
    dai "W": druna "w";
    dai "X": druna "x";
    dai "Y": druna "y";
    dai "Z": druna "z";
    }
    druna c;
}

nudro msort(xs) {
    plulai n := dra(xs);
    atdoyal (n <= 1) {
        druna xs;
    }
    plulai mid := n / 2;
    plulai left := [];
    plulai right := [];
    plulai i := 0;
    edrushe (i < mid)
        sutse(left, xs[i]);
        i := i + 1;
    aitudre
    edrushe (i < n)
        sutse(right, xs[i]);
        i := i + 1;
    aitudre
    left := msort(left);
    right := msort(right);
    plulai res := [];
    plulai a := 0;
    plulai b := 0;
    plulai la := dra(left);
    plulai lb := dra(right);
    edrushe (a < la rulsai b < lb)
        atdoyal (left[a] <= right[b]) {
            sutse(res, left[a]);
            a := a + 1;
        } bulbayo {
            sutse(res, right[b]);
            b := b + 1;
        }
    aitudre
    edrushe (a < la)
        sutse(res, left[a]);
        a := a + 1;
    aitudre
    edrushe (b < lb)
        sutse(res, right[b]);
        b := b + 1;
    aitudre
    druna res;
}

plulai words := [];
plulai line := playadu();
edrushe (line <> aiplai)
    plulai cur := "";
    plulai i := 0;
    plulai ln := dra(line);
    edrushe (i < ln)
        plulai c := line[i];
        atdoyal (c >= "a" rulsai c <= "z") {
            cur := cur + c;
        } bulbayo atdoyal (c >= "A" rulsai c <= "Z") {
            cur := cur + lower(c);
        } bulbayo {
            atdoyal (cur <> "") {
                sutse(words, cur);
                cur := "";
            }
        }
        i := i + 1;
    aitudre
    atdoyal (cur <> "") {
        sutse(words, cur);
    }
    line := playadu();
aitudre
words := msort(words);
plulai uw := [];
plulai uc := [];
plulai m := 0;
plulai j := 0;
edrushe (j < dra(words))
    atdoyal (m > 0 rulsai uw[m - 1] == words[j]) {
        uc[m - 1] := uc[m - 1] + 1;
    } bulbayo {
        sutse(uw, words[j]);
        sutse(uc, 1);
        m := m + 1;
    }
    j := j + 1;
aitudre
plulai t := 0;
edrushe (t < 10)
    plulai best := -1;
    plulai bi := -1;
    plulai k := 0;
    edrushe (k < m)
        atdoyal (uc[k] > best) {
            best := uc[k];
            bi := k;
        }
        k := k + 1;
    aitudre
    atdoyal (bi < 0) {
        sonaidel;
    }
    shaibe uw[bi] + " " + uc[bi];
    uc[bi] := -1;
    t := t + 1;
aitudre
</solution>