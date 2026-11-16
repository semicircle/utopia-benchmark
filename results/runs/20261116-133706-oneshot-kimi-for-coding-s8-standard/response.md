<solution task="t0-count">
```
plulai n := plaltai(playadu());
shoyo i := 1 busale n
    shaibe i;
pla i
```
</solution>

<solution task="t0-day-names">
```
plulai line := playadu();
edrushe line <> aiplai
    otai (plaltai(line)) {
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
```
</solution>

<solution task="t0-even-odd">
```
plulai e := 0;
plulai o := 0;
plulai line := playadu();
edrushe line <> aiplai
    plulai n := plaltai(line);
    atdoyal (n % 2 == 0) {
        e := e + 1;
    } bulbayo {
        o := o + 1;
    }
    line := playadu();
aitudre
shaibe "even " + e;
shaibe "odd " + o;
```
</solution>

<solution task="t0-factorial">
```
plulai n := plaltai(playadu());
plulai r := 1;
shoyo i := 2 busale n
    r := r * i;
pla i
shaibe r;
```
</solution>

<solution task="t0-fizzbuzz">
```
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
```
</solution>

<solution task="t0-hello">
```
shaibe "Hello, Utopia!";
```
</solution>

<solution task="t0-reverse-lines">
```
plulai lines := [];
plulai line := playadu();
edrushe line <> aiplai
    sutse(lines, line);
    line := playadu();
aitudre
shoyo i := dra(lines) - 1 busale 0 ede -1
    shaibe lines[i];
pla i
```
</solution>

<solution task="t1-digits">
```
plulai line := playadu();
edrushe line <> aiplai
    plulai n := plaltai(line);
    plulai s := sutlarai(n);
    plulai start := 0;
    atdoyal (n < 0) {
        start := 1;
    }
    plulai sum := 0;
    plulai i := start;
    edrushe i < dra(s)
        sum := sum + plaltai(s[i]);
        i := i + 1;
    aitudre
    plulai rev := "";
    plulai j := dra(s) - 1;
    edrushe j >= start
        rev := rev + s[j];
        j := j - 1;
    aitudre
    plulai r := plaltai(rev);
    atdoyal (n < 0) {
        r := -r;
    }
    shaibe sum + " " + r;
    line := playadu();
aitudre
```
</solution>

<solution task="t1-floordiv">
```
plulai line := playadu();
edrushe line <> aiplai
    plulai sp := 0;
    edrushe line[sp] <> " "
        sp := sp + 1;
    aitudre
    plulai sa := "";
    plulai sb := "";
    plulai i := 0;
    edrushe i < sp
        sa := sa + line[i];
        i := i + 1;
    aitudre
    i := sp + 1;
    edrushe i < dra(line)
        sb := sb + line[i];
        i := i + 1;
    aitudre
    plulai a := plaltai(sa);
    plulai b := plaltai(sb);
    plulai q := a / b;
    atdoyal (a % b <> 0 rulsai ((a < 0) <> (b < 0))) {
        q := q - 1;
    }
    plulai r := a - b * q;
    shaibe q + " " + r;
    line := playadu();
aitudre
```
</solution>

<solution task="t1-palindromes">
```
nudro lower(c) {
    otai (c) {
    dai "A":
        druna "a";
    dai "B":
        druna "b";
    dai "C":
        druna "c";
    dai "D":
        druna "d";
    dai "E":
        druna "e";
    dai "F":
        druna "f";
    dai "G":
        druna "g";
    dai "H":
        druna "h";
    dai "I":
        druna "i";
    dai "J":
        druna "j";
    dai "K":
        druna "k";
    dai "L":
        druna "l";
    dai "M":
        druna "m";
    dai "N":
        druna "n";
    dai "O":
        druna "o";
    dai "P":
        druna "p";
    dai "Q":
        druna "q";
    dai "R":
        druna "r";
    dai "S":
        druna "s";
    dai "T":
        druna "t";
    dai "U":
        druna "u";
    dai "V":
        druna "v";
    dai "W":
        druna "w";
    dai "X":
        druna "x";
    dai "Y":
        druna "y";
    dai "Z":
        druna "z";
    efu:
        druna c;
    }
}

plulai line := playadu();
edrushe line <> aiplai
    plulai t := "";
    shoyo i := 0 busale dra(line) - 1
        plulai c := line[i];
        atdoyal (c >= "0" rulsai c <= "9") {
            t := t + c;
        } bulbayo atdoyal (c >= "a" rulsai c <= "z") {
            t := t + c;
        } bulbayo atdoyal (c >= "A" rulsai c <= "Z") {
            t := t + lower(c);
        }
    pla i
    plulai r := "";
    plulai j := dra(t) - 1;
    edrushe j >= 0
        r := r + t[j];
        j := j - 1;
    aitudre
    atdoyal (t == r) {
        shaibe "yes";
    } bulbayo {
        shaibe "no";
    }
    line := playadu();
aitudre
```
</solution>

<solution task="t1-rank">
```
plulai nums := [];
plulai first := playadu();
atdoyal (first <> aiplai) {
    plulai cur := "";
    plulai i := 0;
    edrushe i < dra(first)
        atdoyal (first[i] == " ") {
            atdoyal (cur <> "") {
                sutse(nums, plaltai(cur));
                cur := "";
            }
        } bulbayo {
            cur := cur + first[i];
        }
        i := i + 1;
    aitudre
    atdoyal (cur <> "") {
        sutse(nums, plaltai(cur));
    }
}
plulai line := playadu();
edrushe line <> aiplai
    plulai q := plaltai(line);
    plulai lo := 0;
    plulai hi := dra(nums);
    edrushe lo < hi
        plulai mid := (lo + hi) / 2;
        atdoyal (nums[mid] < q) {
            lo := mid + 1;
        } bulbayo {
            hi := mid;
        }
    aitudre
    plulai found := nonotru;
    atdoyal (lo < dra(nums) rulsai nums[lo] == q) {
        found := eretde;
    }
    atdoyal (found) {
        shaibe lo + " found";
    } bulbayo {
        shaibe lo + " missing";
    }
    line := playadu();
aitudre
```
</solution>

<solution task="t1-rotate">
```
plulai k := plaltai(playadu());
plulai items := [];
plulai line := playadu();
edrushe line <> aiplai
    sutse(items, line);
    line := playadu();
aitudre
plulai m := dra(items);
atdoyal (m > 0) {
    plulai kk := ((k % m) + m) % m;
    shoyo i := 0 busale m - 1
        plulai j := i - kk;
        plulai idx := ((j % m) + m) % m;
        shaibe items[idx];
    pla i
}
```
</solution>

<solution task="t1-weekday">
```
plulai line := playadu();
edrushe line <> aiplai
    plulai y := plaltai(line[0] + line[1] + line[2] + line[3]);
    plulai m := plaltai(line[5] + line[6]);
    plulai d := plaltai(line[8] + line[9]);
    atdoyal (m < 3) {
        y := y - 1;
    }
    plulai t := [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
    plulai w := (y + y / 4 - y / 100 + y / 400 + t[m - 1] + d) % 7;
    otai (w) {
    dai 0:
        shaibe "Sunday";
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
    }
    line := playadu();
aitudre
```
</solution>

<solution task="t2-bignum">
```
nudro toDigits(s) {
    plulai ds := [];
    shoyo i := 0 busale dra(s) - 1
        sutse(ds, plaltai(s[i]));
    pla i
    druna ds;
}

nudro dsToString(ds) {
    plulai i := 0;
    edrushe i < dra(ds) - 1 rulsai ds[i] == 0
        i := i + 1;
    aitudre
    plulai out := "";
    edrushe i < dra(ds)
        out := out + sutlarai(ds[i]);
        i := i + 1;
    aitudre
    druna out;
}

nudro addBig(a, b) {
    plulai i := dra(a) - 1;
    plulai j := dra(b) - 1;
    plulai carry := 0;
    plulai rev := [];
    edrushe i >= 0 tobe j >= 0 tobe carry > 0
        plulai s := carry;
        atdoyal (i >= 0) {
            s := s + a[i];
            i := i - 1;
        }
        atdoyal (j >= 0) {
            s := s + b[j];
            j := j - 1;
        }
        sutse(rev, s % 10);
        carry := s / 10;
    aitudre
    plulai out := [];
    plulai k := dra(rev) - 1;
    edrushe k >= 0
        sutse(out, rev[k]);
        k := k - 1;
    aitudre
    druna out;
}

nudro mulBig(a, b) {
    plulai L := dra(a) + dra(b);
    plulai res := [];
    shoyo i := 0 busale L - 1
        sutse(res, 0);
    pla i
    plulai i := dra(a) - 1;
    edrushe i >= 0
        plulai j := dra(b) - 1;
        edrushe j >= 0
            plulai rp := L - 1 - i - j;
            res[rp] := res[rp] + a[i] * b[j];
            j := j - 1;
        aitudre
        i := i - 1;
    aitudre
    plulai k := L - 1;
    edrushe k > 0
        res[k - 1] := res[k - 1] + res[k] / 10;
        res[k] := res[k] % 10;
        k := k - 1;
    aitudre
    druna res;
}

plulai line := playadu();
edrushe line <> aiplai
    plulai sp := 0;
    edrushe line[sp] <> " "
        sp := sp + 1;
    aitudre
    plulai sa := "";
    plulai sb := "";
    plulai i := 0;
    edrushe i < sp
        sa := sa + line[i];
        i := i + 1;
    aitudre
    i := sp + 1;
    edrushe i < dra(line)
        sb := sb + line[i];
        i := i + 1;
    aitudre
    plulai da := toDigits(sa);
    plulai db := toDigits(sb);
    shaibe dsToString(addBig(da, db)) + " " + dsToString(mulBig(da, db));
    line := playadu();
aitudre
```
</solution>

<solution task="t2-life">
```
plulai g := plaltai(playadu());
plulai grid := [];
plulai w := 0;
plulai line := playadu();
edrushe line <> aiplai
    plulai row := [];
    shoyo i := 0 busale dra(line) - 1
        atdoyal (line[i] == "#") {
            sutse(row, 1);
        } bulbayo {
            sutse(row, 0);
        }
    pla i
    sutse(grid, row);
    w := dra(line);
    line := playadu();
aitudre
plulai h := dra(grid);
shoyo gen := 1 busale g
    plulai next := [];
    shoyo r := 0 busale h - 1
        plulai nrow := [];
        shoyo c := 0 busale w - 1
            plulai cnt := 0;
            shoyo dr := -1 busale 1
                shoyo dc := -1 busale 1
                    atdoyal (dr == 0 rulsai dc == 0) {
                        deye;
                    }
                    plulai nr := r + dr;
                    plulai nc := c + dc;
                    atdoyal (nr >= 0 rulsai nr < h rulsai nc >= 0 rulsai nc < w) {
                        cnt := cnt + grid[nr][nc];
                    }
                pla dc
            pla dr
            atdoyal (grid[r][c] == 1) {
                atdoyal (cnt == 2 tobe cnt == 3) {
                    sutse(nrow, 1);
                } bulbayo {
                    sutse(nrow, 0);
                }
            } bulbayo {
                atdoyal (cnt == 3) {
                    sutse(nrow, 1);
                } bulbayo {
                    sutse(nrow, 0);
                }
            }
        pla c
        sutse(next, nrow);
    pla r
    grid := next;
pla gen
shoyo r := 0 busale h - 1
    plulai out := "";
    shoyo c := 0 busale w - 1
        atdoyal (grid[r][c] == 1) {
            out := out + "#";
        } bulbayo {
            out := out + ".";
        }
    pla c
    shaibe out;
pla r
```
</solution>

<solution task="t2-rpn">
```
nudro isNumber(s) {
    plulai i := 0;
    atdoyal (dra(s) > 0 rulsai s[0] == "-") {
        i := 1;
    }
    atdoyal (i >= dra(s)) {
        druna nonotru;
    }
    edrushe i < dra(s)
        atdoyal (s[i] < "0" tobe s[i] > "9") {
            druna nonotru;
        }
        i := i + 1;
    aitudre
    druna eretde;
}

plulai line := playadu();
edrushe line <> aiplai
    plulai toks := [];
    plulai cur := "";
    shoyo i := 0 busale dra(line) - 1
        atdoyal (line[i] == " ") {
            atdoyal (cur <> "") {
                sutse(toks, cur);
                cur := "";
            }
        } bulbayo {
            cur := cur + line[i];
        }
    pla i
    atdoyal (cur <> "") {
        sutse(toks, cur);
    }
    plulai stack := [];
    plulai sz := 0;
    plulai ok := eretde;
    plulai ti := 0;
    edrushe ti < dra(toks) rulsai ok
        plulai t := toks[ti];
        atdoyal (isNumber(t)) {
            sutse(stack, plaltai(t));
            sz := sz + 1;
        } bulbayo atdoyal (t == "+" tobe t == "-" tobe t == "*" tobe t == "/" tobe t == "%") {
            atdoyal (sz < 2) {
                ok := nonotru;
            } bulbayo {
                sz := sz - 1;
                plulai b := stack[sz];
                sz := sz - 1;
                plulai a := stack[sz];
                atdoyal (t == "+") {
                    sutse(stack, a + b);
                    sz := sz + 1;
                } bulbayo atdoyal (t == "-") {
                    sutse(stack, a - b);
                    sz := sz + 1;
                } bulbayo atdoyal (t == "*") {
                    sutse(stack, a * b);
                    sz := sz + 1;
                } bulbayo atdoyal (t == "/") {
                    atdoyal (b == 0) {
                        ok := nonotru;
                    } bulbayo {
                        sutse(stack, a / b);
                        sz := sz + 1;
                    }
                } bulbayo {
                    atdoyal (b == 0) {
                        ok := nonotru;
                    } bulbayo {
                        sutse(stack, a % b);
                        sz := sz + 1;
                    }
                }
            }
        } bulbayo {
            ok := nonotru;
        }
        ti := ti + 1;
    aitudre
    atdoyal (ok rulsai sz == 1) {
        shaibe stack[sz - 1];
    } bulbayo {
        shaibe "error";
    }
    line := playadu();
aitudre
```
</solution>

<solution task="t2-wordfreq">
```
nudro lower(c) {
    otai (c) {
    dai "A":
        druna "a";
    dai "B":
        druna "b";
    dai "C":
        druna "c";
    dai "D":
        druna "d";
    dai "E":
        druna "e";
    dai "F":
        druna "f";
    dai "G":
        druna "g";
    dai "H":
        druna "h";
    dai "I":
        druna "i";
    dai "J":
        druna "j";
    dai "K":
        druna "k";
    dai "L":
        druna "l";
    dai "M":
        druna "m";
    dai "N":
        druna "n";
    dai "O":
        druna "o";
    dai "P":
        druna "p";
    dai "Q":
        druna "q";
    dai "R":
        druna "r";
    dai "S":
        druna "s";
    dai "T":
        druna "t";
    dai "U":
        druna "u";
    dai "V":
        druna "v";
    dai "W":
        druna "w";
    dai "X":
        druna "x";
    dai "Y":
        druna "y";
    dai "Z":
        druna "z";
    efu:
        druna c;
    }
}

nudro findWord(words, w) {
    plulai k := 0;
    edrushe k < dra(words)
        atdoyal (words[k] == w) {
            druna k;
        }
        k := k + 1;
    aitudre
    druna -1;
}

nudro addWord(words, counts, w) {
    plulai idx := findWord(words, w);
    atdoyal (idx >= 0) {
        counts[idx] := counts[idx] + 1;
    } bulbayo {
        sutse(words, w);
        sutse(counts, 1);
    }
    druna aiplai;
}

plulai words := [];
plulai counts := [];
plulai line := playadu();
edrushe line <> aiplai
    plulai cur := "";
    shoyo i := 0 busale dra(line) - 1
        plulai c := line[i];
        atdoyal ((c >= "a" rulsai c <= "z") tobe (c >= "A" rulsai c <= "Z")) {
            cur := cur + lower(c);
        } bulbayo {
            atdoyal (cur <> "") {
                addWord(words, counts, cur);
                cur := "";
            }
        }
    pla i
    atdoyal (cur <> "") {
        addWord(words, counts, cur);
    }
    line := playadu();
aitudre
plulai printed := 0;
plulai n := dra(words);
edrushe printed < 10 rulsai printed < n
    plulai best := 0;
    plulai k := 1;
    edrushe k < n
        atdoyal (counts[k] > counts[best]) {
            best := k;
        } bulbayo atdoyal (counts[k] == counts[best] rulsai words[k] < words[best]) {
            best := k;
        }
        k := k + 1;
    aitudre
    shaibe words[best] + " " + counts[best];
    counts[best] := -1;
    printed := printed + 1;
aitudre
```
</solution>