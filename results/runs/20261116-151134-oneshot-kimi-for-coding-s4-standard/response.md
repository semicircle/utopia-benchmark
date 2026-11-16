<solution task="t0-count">
Trepiho n := Eshiyer(Thoke());
Pil (Trepiho i := 1; i <= n; i := i + 1) {
    Rashar i;
}
</solution>

<solution task="t0-day-names">
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho d := Eshiyer(line);
    Pakru Sher d
    Sher 1
        Rashar "Monday";
    Sher 2
        Rashar "Tuesday";
    Sher 3
        Rashar "Wednesday";
    Sher 4
        Rashar "Thursday";
    Sher 5
        Rashar "Friday";
    Sher 6
        Rashar "Saturday";
    Sher 7
        Rashar "Sunday";
    Sher Thotri
        Rashar "invalid";
    Tho Pakru
    line := Thoke();
}
</solution>

<solution task="t0-even-odd">
Trepiho even := 0;
Trepiho odd := 0;
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho n := Eshiyer(line);
    Mushu n % 2 = 0 Yeshil Hupo
        even := even + 1;
    Tho Thotri Hupo
        odd := odd + 1;
    Tho
    line := Thoke();
}
Rashar "even " + even;
Rashar "odd " + odd;
</solution>

<solution task="t0-factorial">
Trepiho n := Eshiyer(Thoke());
Trepiho r := 1;
Pil (Trepiho i := 2; i <= n; i := i + 1) {
    r := r * i;
}
Rashar r;
</solution>

<solution task="t0-fizzbuzz">
Trepiho n := Eshiyer(Thoke());
Pil (Trepiho i := 1; i <= n; i := i + 1) {
    Mushu i % 15 = 0 Yeshil Hupo
        Rashar "FizzBuzz";
    Tho Thotri Mushu i % 3 = 0 Yeshil Hupo
        Rashar "Fizz";
    Tho Thotri Mushu i % 5 = 0 Yeshil Hupo
        Rashar "Buzz";
    Tho Thotri Hupo
        Rashar i;
    Tho
}
</solution>

<solution task="t0-hello">
Rashar "Hello, Utopia!";
</solution>

<solution task="t0-reverse-lines">
Trepiho lines := [];
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Theki(lines, line);
    line := Thoke();
}
Pil (Trepiho i := Purmo(lines) - 1; i >= 0; i := i - 1) {
    Rashar lines[i];
}
</solution>

<solution task="t1-digits">
Ruyoyo substr(s, lo, hi)
    Trepiho r := "";
    Pil (Trepiho i := lo; i < hi; i := i + 1) {
        r := r + s[i];
    }
    Omel r;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho n := Eshiyer(line);
    Trepiho s := Mitrer(n);
    Trepiho neg := Yaki;
    Mushu s[0] = "-" Yeshil Hupo
        neg := Yupu;
        s := substr(s, 1, Purmo(s));
    Tho
    Trepiho sum := 0;
    Trepiho rev := "";
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        sum := sum + Eshiyer(s[i]);
        rev := s[i] + rev;
    }
    Trepiho r := Eshiyer(rev);
    Mushu neg Yeshil Hupo
        r := -r;
    Tho
    Rashar sum + " " + r;
    line := Thoke();
}
</solution>

<solution task="t1-floordiv">
Ruyoyo substr(s, lo, hi)
    Trepiho r := "";
    Pil (Trepiho i := lo; i < hi; i := i + 1) {
        r := r + s[i];
    }
    Omel r;
Opa

Ruyoyo findsp(s)
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Mushu s[i] = " " Yeshil Hupo
            Omel i;
        Tho
    }
    Omel -1;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho sp := findsp(line);
    Trepiho a := Eshiyer(substr(line, 0, sp));
    Trepiho b := Eshiyer(substr(line, sp + 1, Purmo(line)));
    Trepiho q := a / b;
    Trepiho r := a - b * q;
    Mushu r ~= 0 Yeshil Hupo
        Mushu (r > 0 Pethe b < 0) Hiyikra (r < 0 Pethe b > 0) Yeshil Hupo
            q := q - 1;
            r := a - b * q;
        Tho
    Tho
    Rashar q + " " + r;
    line := Thoke();
}
</solution>

<solution task="t1-palindromes">
Ruyoyo lowerc(c)
    Trepiho up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    Trepiho lo := "abcdefghijklmnopqrstuvwxyz";
    Pil (Trepiho i := 0; i < 26; i := i + 1) {
        Mushu c = up[i] Yeshil Hupo
            Omel lo[i];
        Tho
    }
    Omel c;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho f := "";
    Pil (Trepiho i := 0; i < Purmo(line); i := i + 1) {
        Trepiho c := line[i];
        Mushu (c >= "a" Pethe c <= "z") Hiyikra (c >= "A" Pethe c <= "Z") Hiyikra (c >= "0" Pethe c <= "9") Yeshil Hupo
            f := f + lowerc(c);
        Tho
    }
    Trepiho ok := Yupu;
    Pil (Trepiho i := 0; i < Purmo(f) / 2; i := i + 1) {
        Mushu f[i] ~= f[Purmo(f) - 1 - i] Yeshil Hupo
            ok := Yaki;
        Tho
    }
    Mushu ok Yeshil Hupo
        Rashar "yes";
    Tho Thotri Hupo
        Rashar "no";
    Tho
    line := Thoke();
}
</solution>

<solution task="t1-rank">
Ruyoyo splitints(s)
    Trepiho xs := [];
    Trepiho cur := "";
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Mushu s[i] = " " Yeshil Hupo
            Theki(xs, Eshiyer(cur));
            cur := "";
        Tho Thotri Hupo
            cur := cur + s[i];
        Tho
    }
    Mushu cur ~= "" Yeshil Hupo
        Theki(xs, Eshiyer(cur));
    Tho
    Omel xs;
Opa

Trepiho first := Thoke();
Trepiho xs := splitints(first);
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho q := Eshiyer(line);
    Trepiho smaller := 0;
    Trepiho found := Yaki;
    Pil (Trepiho i := 0; i < Purmo(xs); i := i + 1) {
        Mushu xs[i] < q Yeshil Hupo
            smaller := smaller + 1;
        Tho
        Mushu xs[i] = q Yeshil Hupo
            found := Yupu;
        Tho
    }
    Mushu found Yeshil Hupo
        Rashar smaller + " found";
    Tho Thotri Hupo
        Rashar smaller + " missing";
    Tho
    line := Thoke();
}
</solution>

<solution task="t1-rotate">
Trepiho k := Eshiyer(Thoke());
Trepiho items := [];
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Theki(items, line);
    line := Thoke();
}
Trepiho m := Purmo(items);
Mushu m > 0 Yeshil Hupo
    Trepiho e := ((k % m) + m) % m;
    Pil (Trepiho i := 0; i < m; i := i + 1) {
        Trepiho idx := i - e;
        Mushu idx < 0 Yeshil Hupo
            idx := idx + m;
        Tho
        Rashar items[idx];
    }
Tho
</solution>

<solution task="t1-weekday">
Ruyoyo substr(s, lo, hi)
    Trepiho r := "";
    Pil (Trepiho i := lo; i < hi; i := i + 1) {
        r := r + s[i];
    }
    Omel r;
Opa

Ruyoyo isleap(y)
    Omel (y % 4 = 0 Pethe y % 100 ~= 0) Hiyikra y % 400 = 0;
Opa

Ruyoyo daysbefore(y, m)
    Trepiho t := [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
    Trepiho d := t[m - 1];
    Mushu m > 2 Pethe isleap(y) Yeshil Hupo
        d := d + 1;
    Tho
    Omel d;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho y := Eshiyer(substr(line, 0, 4));
    Trepiho m := Eshiyer(substr(line, 5, 7));
    Trepiho d := Eshiyer(substr(line, 8, 10));
    Trepiho y1 := y - 1;
    Trepiho leaps := y1 / 4 - y1 / 100 + y1 / 400;
    Trepiho days := 365 * y1 + leaps + daysbefore(y, m) + (d - 1);
    Trepiho w := days % 7;
    Pakru Sher w
    Sher 0
        Rashar "Monday";
    Sher 1
        Rashar "Tuesday";
    Sher 2
        Rashar "Wednesday";
    Sher 3
        Rashar "Thursday";
    Sher 4
        Rashar "Friday";
    Sher 5
        Rashar "Saturday";
    Sher Thotri
        Rashar "Sunday";
    Tho Pakru
    line := Thoke();
}
</solution>

<solution task="t2-bignum">
Ruyoyo substr(s, lo, hi)
    Trepiho r := "";
    Pil (Trepiho i := lo; i < hi; i := i + 1) {
        r := r + s[i];
    }
    Omel r;
Opa

Ruyoyo findsp(s)
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Mushu s[i] = " " Yeshil Hupo
            Omel i;
        Tho
    }
    Omel -1;
Opa

Ruyoyo dig(s, i)
    Mushu i < 0 Yeshil Hupo
        Omel 0;
    Tho
    Omel Eshiyer(s[i]);
Opa

Ruyoyo badd(a, b)
    Trepiho i := Purmo(a) - 1;
    Trepiho j := Purmo(b) - 1;
    Trepiho carry := 0;
    Trepiho res := "";
    Hemorhor {
        Trepiho da := dig(a, i);
        Trepiho db := dig(b, j);
        Trepiho sum := da + db + carry;
        res := Mitrer(sum % 10) + res;
        carry := sum / 10;
        i := i - 1;
        j := j - 1;
    } Rokomi (i >= 0 Hiyikra j >= 0 Hiyikra carry > 0);
    Mushu carry > 0 Yeshil Hupo
        res := Mitrer(carry) + res;
    Tho
    Omel res;
Opa

Ruyoyo bmul(a, b)
    Trepiho la := Purmo(a);
    Trepiho lb := Purmo(b);
    Trepiho res := [];
    Pil (Trepiho i := 0; i < la + lb; i := i + 1) {
        Theki(res, 0);
    }
    Pil (Trepiho i := la - 1; i >= 0; i := i - 1) {
        Pil (Trepiho j := lb - 1; j >= 0; j := j - 1) {
            Trepiho p := Eshiyer(a[i]) * Eshiyer(b[j]);
            Trepiho pos := i + j + 1;
            Trepiho s := res[pos] + p;
            res[pos] := s % 10;
            Trepiho c := s / 10;
            Trepiho k := pos - 1;
            Rokomi (c > 0) {
                Trepiho s2 := res[k] + c;
                res[k] := s2 % 10;
                c := s2 / 10;
                k := k - 1;
            }
        }
    }
    Trepiho st := 0;
    Rokomi (st < la + lb - 1 Pethe res[st] = 0) {
        st := st + 1;
    }
    Trepiho out := "";
    Pil (Trepiho i := st; i < la + lb; i := i + 1) {
        out := out + Mitrer(res[i]);
    }
    Omel out;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho sp := findsp(line);
    Trepiho a := substr(line, 0, sp);
    Trepiho b := substr(line, sp + 1, Purmo(line));
    Rashar badd(a, b) + " " + bmul(a, b);
    line := Thoke();
}
</solution>

<solution task="t2-life">
Trepiho g := Eshiyer(Thoke());
Trepiho grid := [];
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Theki(grid, line);
    line := Thoke();
}
Trepiho rows := Purmo(grid);
Trepiho cols := Purmo(grid[0]);
Pil (Trepiho gen := 0; gen < g; gen := gen + 1) {
    Trepiho next := [];
    Pil (Trepiho r := 0; r < rows; r := r + 1) {
        Trepiho row := "";
        Pil (Trepiho c := 0; c < cols; c := c + 1) {
            Trepiho cnt := 0;
            Pil (Trepiho dr := -1; dr <= 1; dr := dr + 1) {
                Pil (Trepiho dc := -1; dc <= 1; dc := dc + 1) {
                    Mushu dr = 0 Pethe dc = 0 Yeshil Hupo
                        Tril;
                    Tho
                    Trepiho rr := r + dr;
                    Trepiho cc := c + dc;
                    Mushu rr >= 0 Pethe rr < rows Pethe cc >= 0 Pethe cc < cols Yeshil Hupo
                        Mushu grid[rr][cc] = "#" Yeshil Hupo
                            cnt := cnt + 1;
                        Tho
                    Tho
                }
            }
            Mushu grid[r][c] = "#" Yeshil Hupo
                Mushu cnt = 2 Hiyikra cnt = 3 Yeshil Hupo
                    row := row + "#";
                Tho Thotri Hupo
                    row := row + ".";
                Tho
            Tho Thotri Hupo
                Mushu cnt = 3 Yeshil Hupo
                    row := row + "#";
                Tho Thotri Hupo
                    row := row + ".";
                Tho
            Tho
        }
        Theki(next, row);
    }
    grid := next;
}
Pil (Trepiho r := 0; r < rows; r := r + 1) {
    Rashar grid[r];
}
</solution>

<solution task="t2-rpn">
Ruyoyo splitstr(s)
    Trepiho toks := [];
    Trepiho cur := "";
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Mushu s[i] = " " Yeshil Hupo
            Mushu cur ~= "" Yeshil Hupo
                Theki(toks, cur);
                cur := "";
            Tho
        Tho Thotri Hupo
            cur := cur + s[i];
        Tho
    }
    Mushu cur ~= "" Yeshil Hupo
        Theki(toks, cur);
    Tho
    Omel toks;
Opa

Ruyoyo isnum(t)
    Trepiho n := Purmo(t);
    Mushu n = 0 Yeshil Hupo
        Omel Yaki;
    Tho
    Trepiho i := 0;
    Mushu t[0] = "-" Yeshil Hupo
        Mushu n = 1 Yeshil Hupo
            Omel Yaki;
        Tho
        i := 1;
    Tho
    Pil (; i < n; i := i + 1) {
        Mushu Shurisho (t[i] >= "0" Pethe t[i] <= "9") Yeshil Hupo
            Omel Yaki;
        Tho
    }
    Omel Yupu;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho toks := splitstr(line);
    Trepiho st := [];
    Trepiho sn := 0;
    Trepiho bad := Yaki;
    Trepiho i := 0;
    Rokomi (i < Purmo(toks) Pethe Shurisho bad) {
        Trepiho t := toks[i];
        Mushu isnum(t) Yeshil Hupo
            Theki(st, Eshiyer(t));
            sn := sn + 1;
        Tho Thotri Mushu t = "+" Yeshil Hupo
            Mushu sn < 2 Yeshil Hupo
                bad := Yupu;
            Tho Thotri Hupo
                Trepiho b := st[sn - 1];
                Trepiho a := st[sn - 2];
                sn := sn - 2;
                Theki(st, a + b);
                sn := sn + 1;
            Tho
        Tho Thotri Mushu t = "-" Yeshil Hupo
            Mushu sn < 2 Yeshil Hupo
                bad := Yupu;
            Tho Thotri Hupo
                Trepiho b := st[sn - 1];
                Trepiho a := st[sn - 2];
                sn := sn - 2;
                Theki(st, a - b);
                sn := sn + 1;
            Tho
        Tho Thotri Mushu t = "*" Yeshil Hupo
            Mushu sn < 2 Yeshil Hupo
                bad := Yupu;
            Tho Thotri Hupo
                Trepiho b := st[sn - 1];
                Trepiho a := st[sn - 2];
                sn := sn - 2;
                Theki(st, a * b);
                sn := sn + 1;
            Tho
        Tho Thotri Mushu t = "/" Yeshil Hupo
            Mushu sn < 2 Yeshil Hupo
                bad := Yupu;
            Tho Thotri Mushu st[sn - 1] = 0 Yeshil Hupo
                bad := Yupu;
            Tho Thotri Hupo
                Trepiho b := st[sn - 1];
                Trepiho a := st[sn - 2];
                sn := sn - 2;
                Theki(st, a / b);
                sn := sn + 1;
            Tho
        Tho Thotri Mushu t = "%" Yeshil Hupo
            Mushu sn < 2 Yeshil Hupo
                bad := Yupu;
            Tho Thotri Mushu st[sn - 1] = 0 Yeshil Hupo
                bad := Yupu;
            Tho Thotri Hupo
                Trepiho b := st[sn - 1];
                Trepiho a := st[sn - 2];
                sn := sn - 2;
                Theki(st, a % b);
                sn := sn + 1;
            Tho
        Tho Thotri Hupo
            bad := Yupu;
        Tho
        i := i + 1;
    }
    Mushu bad Hiyikra sn ~= 1 Yeshil Hupo
        Rashar "error";
    Tho Thotri Hupo
        Rashar st[0];
    Tho
    line := Thoke();
}
</solution>

<solution task="t2-wordfreq">
Ruyoyo lowerc(c)
    Trepiho up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    Trepiho lo := "abcdefghijklmnopqrstuvwxyz";
    Pil (Trepiho i := 0; i < 26; i := i + 1) {
        Mushu c = up[i] Yeshil Hupo
            Omel lo[i];
        Tho
    }
    Omel c;
Opa

Ruyoyo mergesort(a)
    Trepiho n := Purmo(a);
    Mushu n <= 1 Yeshil Hupo
        Omel a;
    Tho
    Trepiho mid := n / 2;
    Trepiho left := [];
    Trepiho right := [];
    Pil (Trepiho i := 0; i < mid; i := i + 1) {
        Theki(left, a[i]);
    }
    Pil (Trepiho i := mid; i < n; i := i + 1) {
        Theki(right, a[i]);
    }
    left := mergesort(left);
    right := mergesort(right);
    Trepiho res := [];
    Trepiho i := 0;
    Trepiho j := 0;
    Rokomi (i < Purmo(left) Hiyikra j < Purmo(right)) {
        Mushu j >= Purmo(right) Hiyikra (i < Purmo(left) Pethe left[i] <= right[j]) Yeshil Hupo
            Theki(res, left[i]);
            i := i + 1;
        Tho Thotri Hupo
            Theki(res, right[j]);
            j := j + 1;
        Tho
    }
    Omel res;
Opa

Trepiho words := [];
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho cur := "";
    Pil (Trepiho i := 0; i < Purmo(line); i := i + 1) {
        Trepiho c := line[i];
        Mushu (c >= "a" Pethe c <= "z") Hiyikra (c >= "A" Pethe c <= "Z") Yeshil Hupo
            cur := cur + lowerc(c);
        Tho Thotri Hupo
            Mushu cur ~= "" Yeshil Hupo
                Theki(words, cur);
                cur := "";
            Tho
        Tho
    }
    Mushu cur ~= "" Yeshil Hupo
        Theki(words, cur);
    Tho
    line := Thoke();
}
Trepiho sw := mergesort(words);
Trepiho uq := [];
Trepiho ct := [];
Trepiho i := 0;
Rokomi (i < Purmo(sw)) {
    Trepiho w := sw[i];
    Trepiho c := 0;
    Rokomi (i < Purmo(sw) Pethe sw[i] = w) {
        c := c + 1;
        i := i + 1;
    }
    Theki(uq, w);
    Theki(ct, c);
}
Pil (Trepiho t := 0; t < 10 Pethe t < Purmo(uq); t := t + 1) {
    Trepiho best := 0;
    Pil (Trepiho j := 1; j < Purmo(uq); j := j + 1) {
        Mushu ct[j] > ct[best] Yeshil Hupo
            best := j;
        Tho
    }
    Rashar uq[best] + " " + ct[best];
    ct[best] := -1;
}
</solution>