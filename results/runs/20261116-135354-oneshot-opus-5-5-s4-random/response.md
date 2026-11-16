<solution task="t0-count">
Trepiho line := Thoke();
Mushu line ~= Krupelro Yeshil Hupo
    Trepiho n := Eshiyer(line);
    Pil (Trepiho i := 1; i <= n; i := i + 1) {
        Rashar i;
    }
Tho
</solution>

<solution task="t0-day-names">
Ruyoyo blank(s)
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Mushu s[i] ~= " " Pethe s[i] ~= "\t" Pethe s[i] ~= "\r" Yeshil Hupo
            Omel Yaki;
        Tho
    }
    Omel Yupu;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Mushu Shurisho blank(line) Yeshil Hupo
        Trepiho n := Eshiyer(line);
        Pakru Sher n
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
    Tho
    line := Thoke();
}
</solution>

<solution task="t0-even-odd">
Ruyoyo blank(s)
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Mushu s[i] ~= " " Pethe s[i] ~= "\t" Pethe s[i] ~= "\r" Yeshil Hupo
            Omel Yaki;
        Tho
    }
    Omel Yupu;
Opa

Trepiho evens := 0;
Trepiho odds := 0;
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Mushu Shurisho blank(line) Yeshil Hupo
        Trepiho n := Eshiyer(line);
        Mushu n % 2 = 0 Yeshil Hupo
            evens := evens + 1;
        Tho Thotri Hupo
            odds := odds + 1;
        Tho
    Tho
    line := Thoke();
}
Rashar "even " + evens;
Rashar "odd " + odds;
</solution>

<solution task="t0-factorial">
Trepiho n := Eshiyer(Thoke());
Trepiho f := 1;
Pil (Trepiho i := 2; i <= n; i := i + 1) {
    f := f * i;
}
Rashar f;
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
Trepiho xs := [];
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Theki(xs, line);
    line := Thoke();
}
Pil (Trepiho i := Purmo(xs) - 1; i >= 0; i := i - 1) {
    Rashar xs[i];
}
</solution>

<solution task="t1-digits">
Ruyoyo blank(s)
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Mushu s[i] ~= " " Pethe s[i] ~= "\t" Pethe s[i] ~= "\r" Yeshil Hupo
            Omel Yaki;
        Tho
    }
    Omel Yupu;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Mushu Shurisho blank(line) Yeshil Hupo
        Trepiho n := Eshiyer(line);
        Trepiho neg := n < 0;
        Trepiho m := n;
        Mushu neg Yeshil Hupo
            m := -m;
        Tho
        Trepiho s := 0;
        Trepiho r := 0;
        Rokomi (m > 0) {
            Trepiho d := m % 10;
            s := s + d;
            r := r * 10 + d;
            m := m / 10;
        }
        Mushu neg Yeshil Hupo
            r := -r;
        Tho
        Rashar "" + s + " " + r;
    Tho
    line := Thoke();
}
</solution>

<solution task="t1-floordiv">
Ruyoyo split(s)
    Trepiho out := [];
    Trepiho cur := "";
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Trepiho c := s[i];
        Mushu c = " " Hiyikra c = "\t" Hiyikra c = "\r" Yeshil Hupo
            Mushu Purmo(cur) > 0 Yeshil Hupo
                Theki(out, cur);
                cur := "";
            Tho
        Tho Thotri Hupo
            cur := cur + c;
        Tho
    }
    Mushu Purmo(cur) > 0 Yeshil Hupo
        Theki(out, cur);
    Tho
    Omel out;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho toks := split(line);
    Mushu Purmo(toks) >= 2 Yeshil Hupo
        Trepiho a := Eshiyer(toks[0]);
        Trepiho b := Eshiyer(toks[1]);
        Trepiho q := a / b;
        Trepiho r := a - b * q;
        Mushu (r < 0 Pethe b > 0) Hiyikra (r > 0 Pethe b < 0) Yeshil Hupo
            q := q - 1;
            r := r + b;
        Tho
        Rashar "" + q + " " + r;
    Tho
    line := Thoke();
}
</solution>

<solution task="t1-palindromes">
Ruyoyo isAlnum(c)
    Omel (c >= "a" Pethe c <= "z") Hiyikra (c >= "A" Pethe c <= "Z") Hiyikra (c >= "0" Pethe c <= "9");
Opa

Ruyoyo lower(c)
    Mushu c >= "A" Pethe c <= "Z" Yeshil Hupo
        Trepiho up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        Trepiho lo := "abcdefghijklmnopqrstuvwxyz";
        Pil (Trepiho i := 0; i < 26; i := i + 1) {
            Mushu up[i] = c Yeshil Hupo
                Omel lo[i];
            Tho
        }
    Tho
    Omel c;
Opa

Ruyoyo isPal(s)
    Trepiho cs := [];
    Pil (Trepiho k := 0; k < Purmo(s); k := k + 1) {
        Mushu isAlnum(s[k]) Yeshil Hupo
            Theki(cs, lower(s[k]));
        Tho
    }
    Trepiho i := 0;
    Trepiho j := Purmo(cs) - 1;
    Rokomi (i < j) {
        Mushu cs[i] ~= cs[j] Yeshil Hupo
            Omel Yaki;
        Tho
        i := i + 1;
        j := j - 1;
    }
    Omel Yupu;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Mushu isPal(line) Yeshil Hupo
        Rashar "yes";
    Tho Thotri Hupo
        Rashar "no";
    Tho
    line := Thoke();
}
</solution>

<solution task="t1-rank">
Ruyoyo split(s)
    Trepiho out := [];
    Trepiho cur := "";
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Trepiho c := s[i];
        Mushu c = " " Hiyikra c = "\t" Hiyikra c = "\r" Yeshil Hupo
            Mushu Purmo(cur) > 0 Yeshil Hupo
                Theki(out, cur);
                cur := "";
            Tho
        Tho Thotri Hupo
            cur := cur + c;
        Tho
    }
    Mushu Purmo(cur) > 0 Yeshil Hupo
        Theki(out, cur);
    Tho
    Omel out;
Opa

Ruyoyo lowerBound(xs, q)
    Trepiho lo := 0;
    Trepiho hi := Purmo(xs);
    Rokomi (lo < hi) {
        Trepiho mid := (lo + hi) / 2;
        Mushu xs[mid] < q Yeshil Hupo
            lo := mid + 1;
        Tho Thotri Hupo
            hi := mid;
        Tho
    }
    Omel lo;
Opa

Trepiho first := Thoke();
Mushu first ~= Krupelro Yeshil Hupo
    Trepiho toks := split(first);
    Trepiho xs := [];
    Pil (Trepiho i := 0; i < Purmo(toks); i := i + 1) {
        Theki(xs, Eshiyer(toks[i]));
    }
    Trepiho line := Thoke();
    Rokomi (line ~= Krupelro) {
        Trepiho qt := split(line);
        Mushu Purmo(qt) > 0 Yeshil Hupo
            Trepiho q := Eshiyer(qt[0]);
            Trepiho idx := lowerBound(xs, q);
            Mushu idx < Purmo(xs) Pethe xs[idx] = q Yeshil Hupo
                Rashar "" + idx + " found";
            Tho Thotri Hupo
                Rashar "" + idx + " missing";
            Tho
        Tho
        line := Thoke();
    }
Tho
</solution>

<solution task="t1-rotate">
Trepiho kl := Thoke();
Mushu kl ~= Krupelro Yeshil Hupo
    Trepiho k := Eshiyer(kl);
    Trepiho items := [];
    Trepiho line := Thoke();
    Rokomi (line ~= Krupelro) {
        Theki(items, line);
        line := Thoke();
    }
    Trepiho n := Purmo(items);
    Mushu n > 0 Yeshil Hupo
        Trepiho s := k % n;
        Mushu s < 0 Yeshil Hupo
            s := s + n;
        Tho
        Trepiho start := (n - s) % n;
        Pil (Trepiho i := 0; i < n; i := i + 1) {
            Rashar items[(start + i) % n];
        }
    Tho
Tho
</solution>

<solution task="t1-weekday">
Trepiho t := [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
Trepiho names := ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Mushu Purmo(line) >= 10 Yeshil Hupo
        Trepiho y := Eshiyer(line[0] + line[1] + line[2] + line[3]);
        Trepiho m := Eshiyer(line[5] + line[6]);
        Trepiho d := Eshiyer(line[8] + line[9]);
        Mushu m < 3 Yeshil Hupo
            y := y - 1;
        Tho
        Trepiho w := (y + y / 4 - y / 100 + y / 400 + t[m - 1] + d) % 7;
        Rashar names[w];
    Tho
    line := Thoke();
}
</solution>

<solution task="t2-bignum">
Ruyoyo split(s)
    Trepiho out := [];
    Trepiho cur := "";
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Trepiho c := s[i];
        Mushu c = " " Hiyikra c = "\t" Hiyikra c = "\r" Yeshil Hupo
            Mushu Purmo(cur) > 0 Yeshil Hupo
                Theki(out, cur);
                cur := "";
            Tho
        Tho Thotri Hupo
            cur := cur + c;
        Tho
    }
    Mushu Purmo(cur) > 0 Yeshil Hupo
        Theki(out, cur);
    Tho
    Omel out;
Opa

Ruyoyo toLimbs(s)
    Trepiho out := [];
    Trepiho i := Purmo(s);
    Rokomi (i > 0) {
        Trepiho start := i - 4;
        Mushu start < 0 Yeshil Hupo
            start := 0;
        Tho
        Trepiho v := 0;
        Pil (Trepiho j := start; j < i; j := j + 1) {
            v := v * 10 + Eshiyer(s[j]);
        }
        Theki(out, v);
        i := start;
    }
    Mushu Purmo(out) = 0 Yeshil Hupo
        Theki(out, 0);
    Tho
    Omel out;
Opa

Ruyoyo addL(a, b)
    Trepiho out := [];
    Trepiho carry := 0;
    Trepiho n := Purmo(a);
    Mushu Purmo(b) > n Yeshil Hupo
        n := Purmo(b);
    Tho
    Pil (Trepiho i := 0; i < n; i := i + 1) {
        Trepiho s := carry;
        Mushu i < Purmo(a) Yeshil Hupo
            s := s + a[i];
        Tho
        Mushu i < Purmo(b) Yeshil Hupo
            s := s + b[i];
        Tho
        Theki(out, s % 10000);
        carry := s / 10000;
    }
    Mushu carry > 0 Yeshil Hupo
        Theki(out, carry);
    Tho
    Omel out;
Opa

Ruyoyo mulL(a, b)
    Trepiho res := [];
    Trepiho total := Purmo(a) + Purmo(b);
    Pil (Trepiho i := 0; i < total; i := i + 1) {
        Theki(res, 0);
    }
    Pil (i := 0; i < Purmo(a); i := i + 1) {
        Trepiho ai := a[i];
        Mushu ai ~= 0 Yeshil Hupo
            Pil (Trepiho j := 0; j < Purmo(b); j := j + 1) {
                res[i + j] := res[i + j] + ai * b[j];
            }
        Tho
    }
    Trepiho carry := 0;
    Pil (Trepiho k := 0; k < total; k := k + 1) {
        Trepiho v := res[k] + carry;
        res[k] := v % 10000;
        carry := v / 10000;
    }
    Omel res;
Opa

Ruyoyo toStr(x)
    Trepiho top := Purmo(x) - 1;
    Rokomi (top > 0 Pethe x[top] = 0) {
        top := top - 1;
    }
    Trepiho out := Mitrer(x[top]);
    Pil (Trepiho k := top - 1; k >= 0; k := k - 1) {
        Trepiho s := Mitrer(x[k]);
        Rokomi (Purmo(s) < 4) {
            s := "0" + s;
        }
        out := out + s;
    }
    Omel out;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho toks := split(line);
    Mushu Purmo(toks) >= 2 Yeshil Hupo
        Trepiho a := toLimbs(toks[0]);
        Trepiho b := toLimbs(toks[1]);
        Rashar toStr(addL(a, b)) + " " + toStr(mulL(a, b));
    Tho
    line := Thoke();
}
</solution>

<solution task="t2-life">
Ruyoyo step(g, R, C)
    Trepiho ng := [];
    Pil (Trepiho r := 0; r < R; r := r + 1) {
        Trepiho row := [];
        Trepiho cur := g[r];
        Pil (Trepiho c := 0; c < C; c := c + 1) {
            Trepiho cnt := 0;
            Pil (Trepiho dr := -1; dr <= 1; dr := dr + 1) {
                Pil (Trepiho dc := -1; dc <= 1; dc := dc + 1) {
                    Mushu dr ~= 0 Hiyikra dc ~= 0 Yeshil Hupo
                        Trepiho rr := r + dr;
                        Trepiho cc := c + dc;
                        Mushu rr >= 0 Pethe rr < R Pethe cc >= 0 Pethe cc < C Yeshil Hupo
                            Trepiho nrow := g[rr];
                            cnt := cnt + nrow[cc];
                        Tho
                    Tho
                }
            }
            Mushu cur[c] = 1 Yeshil Hupo
                Mushu cnt = 2 Hiyikra cnt = 3 Yeshil Hupo
                    Theki(row, 1);
                Tho Thotri Hupo
                    Theki(row, 0);
                Tho
            Tho Thotri Hupo
                Mushu cnt = 3 Yeshil Hupo
                    Theki(row, 1);
                Tho Thotri Hupo
                    Theki(row, 0);
                Tho
            Tho
        }
        Theki(ng, row);
    }
    Omel ng;
Opa

Trepiho gens := Eshiyer(Thoke());
Trepiho grid := [];
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Mushu Purmo(line) > 0 Yeshil Hupo
        Trepiho row := [];
        Pil (Trepiho c := 0; c < Purmo(line); c := c + 1) {
            Mushu line[c] = "#" Yeshil Hupo
                Theki(row, 1);
            Tho Thotri Mushu line[c] = "." Yeshil Hupo
                Theki(row, 0);
            Tho
        }
        Theki(grid, row);
    Tho
    line := Thoke();
}
Trepiho R := Purmo(grid);
Mushu R > 0 Yeshil Hupo
    Trepiho C := Purmo(grid[0]);
    Pil (Trepiho k := 0; k < gens; k := k + 1) {
        grid := step(grid, R, C);
    }
    Pil (Trepiho r := 0; r < R; r := r + 1) {
        Trepiho rw := grid[r];
        Trepiho s := "";
        Pil (c := 0; c < C; c := c + 1) {
            Mushu rw[c] = 1 Yeshil Hupo
                s := s + "#";
            Tho Thotri Hupo
                s := s + ".";
            Tho
        }
        Rashar s;
    }
Tho
</solution>

<solution task="t2-rpn">
Ruyoyo split(s)
    Trepiho out := [];
    Trepiho cur := "";
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Trepiho c := s[i];
        Mushu c = " " Yeshil Hupo
            Mushu Purmo(cur) > 0 Yeshil Hupo
                Theki(out, cur);
                cur := "";
            Tho
        Tho Thotri Hupo
            cur := cur + c;
        Tho
    }
    Mushu Purmo(cur) > 0 Yeshil Hupo
        Theki(out, cur);
    Tho
    Omel out;
Opa

Ruyoyo isInt(t)
    Trepiho st := 0;
    Mushu t[0] = "-" Yeshil Hupo
        st := 1;
    Tho
    Mushu Purmo(t) <= st Yeshil Hupo
        Omel Yaki;
    Tho
    Pil (Trepiho i := st; i < Purmo(t); i := i + 1) {
        Mushu t[i] < "0" Hiyikra t[i] > "9" Yeshil Hupo
            Omel Yaki;
        Tho
    }
    Omel Yupu;
Opa

Ruyoyo evalRpn(s)
    Trepiho toks := split(s);
    Mushu Purmo(toks) = 0 Yeshil Hupo
        Omel "error";
    Tho
    Trepiho st := [];
    Trepiho sp := 0;
    Pil (Trepiho i := 0; i < Purmo(toks); i := i + 1) {
        Trepiho t := toks[i];
        Trepiho v := 0;
        Mushu t = "+" Hiyikra t = "-" Hiyikra t = "*" Hiyikra t = "/" Hiyikra t = "%" Yeshil Hupo
            Mushu sp < 2 Yeshil Hupo
                Omel "error";
            Tho
            Trepiho b := st[sp - 1];
            Trepiho a := st[sp - 2];
            sp := sp - 2;
            Pakru Sher t
            Sher "+"
                v := a + b;
            Sher "-"
                v := a - b;
            Sher "*"
                v := a * b;
            Sher "/"
                Mushu b = 0 Yeshil Hupo
                    Omel "error";
                Tho
                v := a / b;
            Sher "%"
                Mushu b = 0 Yeshil Hupo
                    Omel "error";
                Tho
                v := a % b;
            Tho Pakru
        Tho Thotri Mushu isInt(t) Yeshil Hupo
            v := Eshiyer(t);
        Tho Thotri Hupo
            Omel "error";
        Tho
        Mushu sp < Purmo(st) Yeshil Hupo
            st[sp] := v;
        Tho Thotri Hupo
            Theki(st, v);
        Tho
        sp := sp + 1;
    }
    Mushu sp ~= 1 Yeshil Hupo
        Omel "error";
    Tho
    Omel Mitrer(st[0]);
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Rashar evalRpn(line);
    line := Thoke();
}
</solution>

<solution task="t2-wordfreq">
Ruyoyo lower(c)
    Trepiho up := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    Trepiho lo := "abcdefghijklmnopqrstuvwxyz";
    Pil (Trepiho i := 0; i < 26; i := i + 1) {
        Mushu up[i] = c Yeshil Hupo
            Omel lo[i];
        Tho
    }
    Omel c;
Opa

Ruyoyo extract(s, words)
    Trepiho cur := "";
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Trepiho c := s[i];
        Mushu c >= "a" Pethe c <= "z" Yeshil Hupo
            cur := cur + c;
        Tho Thotri Mushu c >= "A" Pethe c <= "Z" Yeshil Hupo
            cur := cur + lower(c);
        Tho Thotri Hupo
            Mushu Purmo(cur) > 0 Yeshil Hupo
                Theki(words, cur);
                cur := "";
            Tho
        Tho
    }
    Mushu Purmo(cur) > 0 Yeshil Hupo
        Theki(words, cur);
    Tho
Opa

Ruyoyo msort(xs)
    Trepiho n := Purmo(xs);
    Mushu n <= 1 Yeshil Hupo
        Omel xs;
    Tho
    Trepiho mid := n / 2;
    Trepiho a := [];
    Trepiho b := [];
    Pil (Trepiho i := 0; i < mid; i := i + 1) {
        Theki(a, xs[i]);
    }
    Pil (i := mid; i < n; i := i + 1) {
        Theki(b, xs[i]);
    }
    a := msort(a);
    b := msort(b);
    Trepiho out := [];
    i := 0;
    Trepiho j := 0;
    Rokomi (i < Purmo(a) Pethe j < Purmo(b)) {
        Mushu a[i] <= b[j] Yeshil Hupo
            Theki(out, a[i]);
            i := i + 1;
        Tho Thotri Hupo
            Theki(out, b[j]);
            j := j + 1;
        Tho
    }
    Rokomi (i < Purmo(a)) {
        Theki(out, a[i]);
        i := i + 1;
    }
    Rokomi (j < Purmo(b)) {
        Theki(out, b[j]);
        j := j + 1;
    }
    Omel out;
Opa

Trepiho words := [];
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    extract(line, words);
    line := Thoke();
}
words := msort(words);
Trepiho distinct := [];
Trepiho counts := [];
Pil (Trepiho i := 0; i < Purmo(words); i := i + 1) {
    Trepiho last := Purmo(distinct) - 1;
    Mushu last >= 0 Pethe distinct[last] = words[i] Yeshil Hupo
        counts[last] := counts[last] + 1;
    Tho Thotri Hupo
        Theki(distinct, words[i]);
        Theki(counts, 1);
    Tho
}
Trepiho used := [];
Pil (i := 0; i < Purmo(distinct); i := i + 1) {
    Theki(used, Yaki);
}
Pil (Trepiho k := 0; k < 10; k := k + 1) {
    Trepiho best := -1;
    Pil (Trepiho j := 0; j < Purmo(distinct); j := j + 1) {
        Mushu Shurisho used[j] Yeshil Hupo
            Mushu best = -1 Hiyikra counts[j] > counts[best] Yeshil Hupo
                best := j;
            Tho
        Tho
    }
    Mushu best = -1 Yeshil Hupo
        Kiyetrel;
    Tho
    used[best] := Yupu;
    Rashar distinct[best] + " " + counts[best];
}
</solution>