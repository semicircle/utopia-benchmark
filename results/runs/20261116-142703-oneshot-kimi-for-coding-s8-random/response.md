<solution task="t0-count">
plulai n := plaltai(playadu());
shoyo i := 1 busale n + 1
    shaibe i;
pla i
</solution>

<solution task="t0-day-names">
plulai line := playadu();
edrushe line <> aiplai
    plulai n := plaltai(line);
    otai (n) {
    dai 1:
        shaibe "Monday";
    dai 2:
        shaibe "Tuesday";
    dai 3:
        shaibe "Wednesday";
    dai 4:
        shaibe "Thursday";
    dai 5:
        shaibe "Friday";
    dai 6:
        shaibe "Saturday";
    dai 7:
        shaibe "Sunday";
    efu:
        shaibe "invalid";
    }
    line := playadu();
aitudre
</solution>

<solution task="t0-even-odd">
plulai even := 0;
plulai odd := 0;
plulai line := playadu();
edrushe line <> aiplai
    plulai n := plaltai(line);
    atdoyal (n % 2 == 0) {
        even := even + 1;
    } bulbayo {
        odd := odd + 1;
    }
    line := playadu();
aitudre
shaibe "even " + even;
shaibe "odd " + odd;
</solution>

<solution task="t0-factorial">
plulai n := plaltai(playadu());
plulai r := 1;
shoyo i := 1 busale n + 1
    r := r * i;
pla i
shaibe r;
</solution>

<solution task="t0-fizzbuzz">
plulai n := plaltai(playadu());
shoyo i := 1 busale n + 1
    atdoyal (i % 3 == 0 rulsai i % 5 == 0) {
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
plulai lines := [];
plulai line := playadu();
edrushe line <> aiplai
    sutse(lines, line);
    line := playadu();
aitudre
plulai i := dra(lines);
edrushe i >= 1
    shaibe lines[i];
    i := i - 1;
aitudre
</solution>

<solution task="t1-digits">
plulai line := playadu();
edrushe line <> aiplai
    plulai n := plaltai(line);
    plulai s := sutlarai(n);
    plulai neg := nonotru;
    plulai digits := "";
    atdoyal (s[1] == "-") {
        neg := eretde;
        shoyo i := 2 busale dra(s) + 1
            digits := digits + s[i];
        pla i
    } bulbayo {
        digits := s;
    }
    plulai sum := 0;
    shoyo i := 1 busale dra(digits) + 1
        sum := sum + plaltai(digits[i]);
    pla i
    plulai rev := "";
    plulai i := dra(digits);
    edrushe i >= 1
        rev := rev + digits[i];
        i := i - 1;
    aitudre
    plulai j := 1;
    edrushe j < dra(rev) rulsai rev[j] == "0"
        j := j + 1;
    aitudre
    plulai trimmed := "";
    shoyo k := j busale dra(rev) + 1
        trimmed := trimmed + rev[k];
    pla k
    plulai val := plaltai(trimmed);
    plulai out := sutlarai(sum) + " ";
    atdoyal (neg rulsai val <> 0) {
        out := out + "-" + sutlarai(val);
    } bulbayo {
        out := out + sutlarai(val);
    }
    shaibe out;
    line := playadu();
aitudre
</solution>

<solution task="t1-floordiv">
nudro split(s) {
    plulai parts := [];
    plulai cur := "";
    plulai i := 1;
    edrushe i <= dra(s)
        plulai c := s[i];
        atdoyal (c == " ") {
            atdoyal (dra(cur) > 0) {
                sutse(parts, cur);
                cur := "";
            }
        } bulbayo {
            cur := cur + c;
        }
        i := i + 1;
    aitudre
    atdoyal (dra(cur) > 0) {
        sutse(parts, cur);
    }
    druna parts;
}

plulai line := playadu();
edrushe line <> aiplai
    plulai parts := split(line);
    plulai a := plaltai(parts[1]);
    plulai b := plaltai(parts[2]);
    plulai q := a / b;
    plulai r := a % b;
    atdoyal (r <> 0 rulsai (a < 0) <> (b < 0)) {
        q := q - 1;
        r := r + b;
    }
    shaibe sutlarai(q) + " " + sutlarai(r);
    line := playadu();
aitudre
</solution>

<solution task="t1-palindromes">
nudro lowerchar(c) {
    plulai ups := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    shoyo i := 1 busale 27
        atdoyal (ups[i] == c) {
            druna "abcdefghijklmnopqrstuvwxyz"[i];
        }
    pla i
    druna c;
}

plulai line := playadu();
edrushe line <> aiplai
    plulai f := "";
    shoyo i := 1 busale dra(line) + 1
        plulai c := line[i];
        atdoyal ((c >= "0" rulsai c <= "9") tobe (c >= "a" rulsai c <= "z") tobe (c >= "A" rulsai c <= "Z")) {
            f := f + lowerchar(c);
        }
    pla i
    plulai ok := eretde;
    plulai i := 1;
    plulai j := dra(f);
    edrushe i < j
        atdoyal (f[i] <> f[j]) {
            ok := nonotru;
        }
        i := i + 1;
        j := j - 1;
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
    plulai parts := [];
    plulai cur := "";
    plulai i := 1;
    edrushe i <= dra(s)
        plulai c := s[i];
        atdoyal (c == " ") {
            atdoyal (dra(cur) > 0) {
                sutse(parts, cur);
                cur := "";
            }
        } bulbayo {
            cur := cur + c;
        }
        i := i + 1;
    aitudre
    atdoyal (dra(cur) > 0) {
        sutse(parts, cur);
    }
    druna parts;
}

plulai first := playadu();
plulai arr := [];
atdoyal (first <> aiplai) {
    plulai toks := split(first);
    shoyo i := 1 busale dra(toks) + 1
        sutse(arr, plaltai(toks[i]));
    pla i
}
plulai line := playadu();
edrushe line <> aiplai
    plulai q := plaltai(line);
    plulai smaller := 0;
    plulai found := nonotru;
    shoyo i := 1 busale dra(arr) + 1
        atdoyal (arr[i] < q) {
            smaller := smaller + 1;
        }
        atdoyal (arr[i] == q) {
            found := eretde;
        }
    pla i
    atdoyal (found) {
        shaibe sutlarai(smaller) + " found";
    } bulbayo {
        shaibe sutlarai(smaller) + " missing";
    }
    line := playadu();
aitudre
</solution>

<solution task="t1-rotate">
plulai k := plaltai(playadu());
plulai items := [];
plulai line := playadu();
edrushe line <> aiplai
    sutse(items, line);
    line := playadu();
aitudre
plulai m := dra(items);
atdoyal (m > 0) {
    plulai shift := ((k % m) + m) % m;
    plulai start := m - shift + 1;
    shoyo j := start busale start + m
        shaibe items[j];
    pla j
}
</solution>

<solution task="t1-weekday">
nudro substr(s, a, b) {
    plulai r := "";
    shoyo i := a busale b + 1
        r := r + s[i];
    pla i
    druna r;
}

nudro isleap(y) {
    druna (y % 4 == 0 rulsai y % 100 <> 0) tobe y % 400 == 0;
}

plulai mdays := [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
plulai names := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

plulai line := playadu();
edrushe line <> aiplai
    plulai y := plaltai(substr(line, 1, 4));
    plulai m := plaltai(substr(line, 6, 7));
    plulai d := plaltai(substr(line, 9, 10));
    plulai leaps := (y - 1) / 4 - (y - 1) / 100 + (y - 1) / 400;
    plulai n := 365 * (y - 1) + leaps + mdays[m] + (d - 1);
    atdoyal (isleap(y) rulsai m > 2) {
        n := n + 1;
    }
    shaibe names[n % 7 + 1];
    line := playadu();
aitudre
</solution>

<solution task="t2-bignum">
nudro split(s) {
    plulai parts := [];
    plulai cur := "";
    plulai i := 1;
    edrushe i <= dra(s)
        plulai c := s[i];
        atdoyal (c == " ") {
            atdoyal (dra(cur) > 0) {
                sutse(parts, cur);
                cur := "";
            }
        } bulbayo {
            cur := cur + c;
        }
        i := i + 1;
    aitudre
    atdoyal (dra(cur) > 0) {
        sutse(parts, cur);
    }
    druna parts;
}

nudro toLSB(s) {
    plulai r := [];
    plulai i := dra(s);
    edrushe i >= 1
        sutse(r, plaltai(s[i]));
        i := i - 1;
    aitudre
    druna r;
}

nudro lsbToStr(x) {
    plulai s := "";
    plulai i := dra(x);
    edrushe i >= 1
        s := s + sutlarai(x[i]);
        i := i - 1;
    aitudre
    druna s;
}

nudro bigadd(a, b) {
    plulai la := dra(a);
    plulai lb := dra(b);
    plulai n := la;
    atdoyal (lb > la) {
        n := lb;
    }
    plulai res := [];
    plulai carry := 0;
    shoyo i := 1 busale n + 1
        plulai da := 0;
        plulai db := 0;
        atdoyal (i <= la) {
            da := a[i];
        }
        atdoyal (i <= lb) {
            db := b[i];
        }
        plulai t := da + db + carry;
        sutse(res, t % 10);
        carry := t / 10;
    pla i
    atdoyal (carry > 0) {
        sutse(res, carry);
    }
    druna res;
}

nudro bigmul(a, b) {
    plulai la := dra(a);
    plulai lb := dra(b);
    plulai res := [];
    shoyo p := 1 busale la + lb + 1
        sutse(res, 0);
    pla p
    shoyo i := 1 busale la + 1
        plulai carry := 0;
        shoyo j := 1 busale lb + 1
            plulai p := i + j - 1;
            plulai t := res[p] + a[i] * b[j] + carry;
            res[p] := t % 10;
            carry := t / 10;
        pla j
        plulai p := i + lb;
        edrushe carry > 0
            plulai t := res[p] + carry;
            res[p] := t % 10;
            carry := t / 10;
            p := p + 1;
        aitudre
    pla i
    plulai n := dra(res);
    edrushe n > 1 rulsai res[n] == 0
        n := n - 1;
    aitudre
    plulai out := [];
    shoyo i := 1 busale n + 1
        sutse(out, res[i]);
    pla i
    druna out;
}

plulai line := playadu();
edrushe line <> aiplai
    plulai parts := split(line);
    plulai a := toLSB(parts[1]);
    plulai b := toLSB(parts[2]);
    shaibe lsbToStr(bigadd(a, b)) + " " + lsbToStr(bigmul(a, b));
    line := playadu();
aitudre
</solution>

<solution task="t2-life">
plulai g := plaltai(playadu());
plulai grid := [];
plulai line := playadu();
edrushe line <> aiplai
    sutse(grid, line);
    line := playadu();
aitudre
plulai rows := dra(grid);
plulai cols := dra(grid[1]);
shoyo gen := 1 busale g + 1
    plulai next := [];
    shoyo r := 1 busale rows + 1
        plulai row := "";
        shoyo c := 1 busale cols + 1
            plulai cnt := 0;
            shoyo dr := -1 busale 2
                shoyo dc := -1 busale 2
                    atdoyal (dr <> 0 tobe dc <> 0) {
                        plulai rr := r + dr;
                        plulai cc := c + dc;
                        atdoyal (rr >= 1 rulsai rr <= rows rulsai cc >= 1 rulsai cc <= cols) {
                            atdoyal (grid[rr][cc] == "#") {
                                cnt := cnt + 1;
                            }
                        }
                    }
                pla dc
            pla dr
            plulai alive := grid[r][c] == "#";
            plulai na := nonotru;
            atdoyal (alive rulsai (cnt == 2 tobe cnt == 3)) {
                na := eretde;
            }
            atdoyal (tul alive rulsai cnt == 3) {
                na := eretde;
            }
            atdoyal (na) {
                row := row + "#";
            } bulbayo {
                row := row + ".";
            }
        pla c
        sutse(next, row);
    pla r
    grid := next;
pla gen
shoyo r := 1 busale rows + 1
    shaibe grid[r];
pla r
</solution>

<solution task="t2-rpn">
nudro split(s) {
    plulai parts := [];
    plulai cur := "";
    plulai i := 1;
    edrushe i <= dra(s)
        plulai c := s[i];
        atdoyal (c == " ") {
            atdoyal (dra(cur) > 0) {
                sutse(parts, cur);
                cur := "";
            }
        } bulbayo {
            cur := cur + c;
        }
        i := i + 1;
    aitudre
    atdoyal (dra(cur) > 0) {
        sutse(parts, cur);
    }
    druna parts;
}

nudro isop(tok) {
    druna tok == "+" tobe tok == "-" tobe tok == "*" tobe tok == "/" tobe tok == "%";
}

nudro isnum(tok) {
    plulai n := dra(tok);
    atdoyal (n == 0) {
        druna nonotru;
    }
    plulai i := 1;
    atdoyal (tok[1] == "-") {
        atdoyal (n == 1) {
            druna nonotru;
        }
        i := 2;
    }
    edrushe i <= n
        plulai c := tok[i];
        atdoyal (tul (c >= "0" rulsai c <= "9")) {
            druna nonotru;
        }
        i := i + 1;
    aitudre
    druna eretde;
}

plulai line := playadu();
edrushe line <> aiplai
    plulai toks := split(line);
    plulai vals := [];
    plulai sp := 0;
    plulai err := nonotru;
    atdoyal (dra(toks) == 0) {
        err := eretde;
    }
    plulai ti := 1;
    edrushe ti <= dra(toks) rulsai tul err
        plulai tok := toks[ti];
        atdoyal (isop(tok)) {
            atdoyal (sp < 2) {
                err := eretde;
            } bulbayo {
                plulai b := vals[sp];
                sp := sp - 1;
                plulai a := vals[sp];
                sp := sp - 1;
                plulai r := 0;
                plulai bad := nonotru;
                otai (tok) {
                dai "+":
                    r := a + b;
                dai "-":
                    r := a - b;
                dai "*":
                    r := a * b;
                dai "/":
                    atdoyal (b == 0) {
                        bad := eretde;
                    } bulbayo {
                        r := a / b;
                    }
                dai "%":
                    atdoyal (b == 0) {
                        bad := eretde;
                    } bulbayo {
                        r := a % b;
                    }
                }
                atdoyal (bad) {
                    err := eretde;
                } bulbayo {
                    sp := sp + 1;
                    atdoyal (sp > dra(vals)) {
                        sutse(vals, r);
                    } bulbayo {
                        vals[sp] := r;
                    }
                }
            }
        } bulbayo atdoyal (isnum(tok)) {
            sp := sp + 1;
            atdoyal (sp > dra(vals)) {
                sutse(vals, plaltai(tok));
            } bulbayo {
                vals[sp] := plaltai(tok);
            }
        } bulbayo {
            err := eretde;
        }
        ti := ti + 1;
    aitudre
    atdoyal (err tobe sp <> 1) {
        shaibe "error";
    } bulbayo {
        shaibe vals[1];
    }
    line := playadu();
aitudre
</solution>

<solution task="t2-wordfreq">
nudro isletter(c) {
    druna (c >= "a" rulsai c <= "z") tobe (c >= "A" rulsai c <= "Z");
}

nudro lowerchar(c) {
    plulai ups := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    shoyo i := 1 busale 27
        atdoyal (ups[i] == c) {
            druna "abcdefghijklmnopqrstuvwxyz"[i];
        }
    pla i
    druna c;
}

nudro addword(words, counts, w) {
    plulai idx := 0;
    shoyo i := 1 busale dra(words) + 1
        atdoyal (words[i] == w) {
            idx := i;
        }
    pla i
    atdoyal (idx == 0) {
        sutse(words, w);
        sutse(counts, 1);
    } bulbayo {
        counts[idx] := counts[idx] + 1;
    }
}

plulai words := [];
plulai counts := [];
plulai line := playadu();
edrushe line <> aiplai
    plulai cur := "";
    shoyo i := 1 busale dra(line) + 1
        plulai c := line[i];
        atdoyal (isletter(c)) {
            cur := cur + lowerchar(c);
        } bulbayo {
            atdoyal (dra(cur) > 0) {
                addword(words, counts, cur);
                cur := "";
            }
        }
    pla i
    atdoyal (dra(cur) > 0) {
        addword(words, counts, cur);
    }
    line := playadu();
aitudre
plulai d := dra(words);
plulai idx := [];
shoyo i := 1 busale d + 1
    sutse(idx, i);
pla i
shoyo i := 1 busale d + 1
    plulai bi := i;
    shoyo j := i + 1 busale d + 1
        plulai a := idx[bi];
        plulai b := idx[j];
        atdoyal (counts[b] > counts[a] tobe (counts[b] == counts[a] rulsai words[b] < words[a])) {
            bi := j;
        }
    pla j
    plulai t := idx[i];
    idx[i] := idx[bi];
    idx[bi] := t;
pla i
plulai lim := d;
atdoyal (lim > 10) {
    lim := 10;
}
shoyo i := 1 busale lim + 1
    shaibe words[idx[i]] + " " + counts[idx[i]];
pla i
</solution>