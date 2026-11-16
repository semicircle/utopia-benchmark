<solution task="t0-count">
Trepiho n := Eshiyer(Thoke());
Pil (Trepiho i := 1; i <= n; i := i + 1) {
    Rashar i;
}
</solution>

<solution task="t0-day-names">
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
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
Trepiho f := 1;
Pil (Trepiho i := 2; i <= n; i := i + 1) {
    f := f * i;
}
Rashar f;
</solution>

<solution task="t0-fizzbuzz">
Trepiho n := Eshiyer(Thoke());
Pil (Trepiho i := 1; i <= n; i := i + 1) {
    Mushu i % 3 = 0 Pethe i % 5 = 0 Yeshil Hupo
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
Trepiho i := Purmo(lines) - 1;
Rokomi (i >= 0) {
    Rashar lines[i];
    i := i - 1;
}
</solution>

<solution task="t1-digits">
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho n := Eshiyer(line);
    Trepiho s := Mitrer(n);
    Trepiho sum := 0;
    Trepiho rev := "";
    Trepiho neg := Yaki;
    Trepiho L := Purmo(s);
    Pil (Trepiho i := 0; i < L; i := i + 1) {
        Trepiho ch := s[i];
        Mushu ch = "-" Yeshil Hupo
            neg := Yupu;
        Tho Thotri Mushu ch >= "0" Pethe ch <= "9" Yeshil Hupo
            sum := sum + Eshiyer(ch);
        Tho
    }
    Pil (Trepiho i := L - 1; i >= 0; i := i - 1) {
        Trepiho ch := s[i];
        Mushu ch >= "0" Pethe ch <= "9" Yeshil Hupo
            rev := rev + ch;
        Tho
    }
    Trepiho r := Eshiyer(rev);
    Rurmopa sum + " ";
    Mushu neg Pethe r ~= 0 Yeshil Hupo
        Rashar "-" + r;
    Tho Thotri Hupo
        Rashar r;
    Tho
    line := Thoke();
}
</solution>

<solution task="t1-floordiv">
Ruyoyo substr(s, i, j)
    Trepiho r := "";
    Pil (Trepiho k := i; k < j; k := k + 1) {
        r := r + s[k];
    }
    Omel r;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho sp := 0;
    Pil (Trepiho i := 0; i < Purmo(line); i := i + 1) {
        Mushu line[i] = " " Yeshil Hupo
            sp := i;
        Tho
    }
    Trepiho a := Eshiyer(substr(line, 0, sp));
    Trepiho b := Eshiyer(substr(line, sp + 1, Purmo(line)));
    Trepiho q := a / b;
    Trepiho rem := a - b * q;
    Mushu rem ~= 0 Pethe (rem < 0) ~= (b < 0) Yeshil Hupo
        q := q - 1;
    Tho
    Rashar q + " " + (a - b * q);
    line := Thoke();
}
</solution>

<solution task="t1-palindromes">
Ruyoyo lower(c)
    Trepiho ups := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    Trepiho los := "abcdefghijklmnopqrstuvwxyz";
    Mushu c >= "A" Pethe c <= "Z" Yeshil Hupo
        Pil (Trepiho i := 0; i < 26; i := i + 1) {
            Mushu c = ups[i] Yeshil Hupo
                Omel los[i];
            Tho
        }
    Tho
    Omel c;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho t := "";
    Pil (Trepiho i := 0; i < Purmo(line); i := i + 1) {
        Trepiho c := line[i];
        Mushu (c >= "a" Pethe c <= "z") Hiyikra (c >= "A" Pethe c <= "Z") Hiyikra (c >= "0" Pethe c <= "9") Yeshil Hupo
            t := t + lower(c);
        Tho
    }
    Trepiho L := Purmo(t);
    Trepiho ok := Yupu;
    Pil (Trepiho i := 0; i < L / 2; i := i + 1) {
        Mushu t[i] ~= t[L - 1 - i] Yeshil Hupo
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
Trepiho first := Thoke();
Trepiho xs := [];
Trepiho cur := "";
Pil (Trepiho i := 0; i < Purmo(first); i := i + 1) {
    Mushu first[i] = " " Yeshil Hupo
        Mushu cur ~= "" Yeshil Hupo
            Theki(xs, Eshiyer(cur));
            cur := "";
        Tho
    Tho Thotri Hupo
        cur := cur + first[i];
    Tho
}
Mushu cur ~= "" Yeshil Hupo
    Theki(xs, Eshiyer(cur));
Tho

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho q := Eshiyer(line);
    Trepiho cnt := 0;
    Trepiho found := Yaki;
    Pil (Trepiho i := 0; i < Purmo(xs); i := i + 1) {
        Mushu xs[i] < q Yeshil Hupo
            cnt := cnt + 1;
        Tho
        Mushu xs[i] = q Yeshil Hupo
            found := Yupu;
        Tho
    }
    Rurmopa cnt + " ";
    Mushu found Yeshil Hupo
        Rashar "found";
    Tho Thotri Hupo
        Rashar "missing";
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
    Trepiho r := k % m;
    Mushu r < 0 Yeshil Hupo
        r := r + m;
    Tho
    Pil (Trepiho i := m - r; i < m; i := i + 1) {
        Rashar items[i];
    }
    Pil (Trepiho i := 0; i < m - r; i := i + 1) {
        Rashar items[i];
    }
Tho
</solution>

<solution task="t1-weekday">
Ruyoyo substr(s, i, j)
    Trepiho r := "";
    Pil (Trepiho k := i; k < j; k := k + 1) {
        r := r + s[k];
    }
    Omel r;
Opa

Ruyoyo days_from_civil(y, m, d)
    Mushu m <= 2 Yeshil Hupo
        y := y - 1;
    Tho
    Trepiho era := y / 400;
    Mushu y < 0 Yeshil Hupo
        era := (y - 399) / 400;
    Tho
    Trepiho yoe := y - era * 400;
    Trepiho mp := (m + 9) % 12;
    Trepiho doy := (153 * mp + 2) / 5 + d - 1;
    Trepiho doe := yoe * 365 + yoe / 4 - yoe / 100 + doy;
    Omel era * 146097 + doe - 719468;
Opa

Ruyoyo weekday_name(w)
    Mushu w = 0 Yeshil Hupo
        Omel "Sunday";
    Tho Thotri Mushu w = 1 Yeshil Hupo
        Omel "Monday";
    Tho Thotri Mushu w = 2 Yeshil Hupo
        Omel "Tuesday";
    Tho Thotri Mushu w = 3 Yeshil Hupo
        Omel "Wednesday";
    Tho Thotri Mushu w = 4 Yeshil Hupo
        Omel "Thursday";
    Tho Thotri Mushu w = 5 Yeshil Hupo
        Omel "Friday";
    Tho
    Omel "Saturday";
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho y := Eshiyer(substr(line, 0, 4));
    Trepiho m := Eshiyer(substr(line, 5, 7));
    Trepiho d := Eshiyer(substr(line, 8, 10));
    Trepiho days := days_from_civil(y, m, d);
    Trepiho w := (days + 4) % 7;
    Mushu w < 0 Yeshil Hupo
        w := w + 7;
    Tho
    Rashar weekday_name(w);
    line := Thoke();
}
</solution>

<solution task="t2-bignum">
Ruyoyo substr(s, i, j)
    Trepiho r := "";
    Pil (Trepiho k := i; k < j; k := k + 1) {
        r := r + s[k];
    }
    Omel r;
Opa

Ruyoyo srev(s)
    Trepiho r := "";
    Pil (Trepiho i := Purmo(s) - 1; i >= 0; i := i - 1) {
        r := r + s[i];
    }
    Omel r;
Opa

Ruyoyo strip(s)
    Trepiho i := 0;
    Rokomi (i < Purmo(s) - 1 Pethe s[i] = "0") {
        i := i + 1;
    }
    Omel substr(s, i, Purmo(s));
Opa

Ruyoyo add(a, b)
    Trepiho ra := srev(a);
    Trepiho rb := srev(b);
    Trepiho res := "";
    Trepiho carry := 0;
    Trepiho n := Purmo(ra);
    Mushu Purmo(rb) > n Yeshil Hupo
        n := Purmo(rb);
    Tho
    Pil (Trepiho i := 0; i < n; i := i + 1) {
        Trepiho da := 0;
        Trepiho db := 0;
        Mushu i < Purmo(ra) Yeshil Hupo
            da := Eshiyer(ra[i]);
        Tho
        Mushu i < Purmo(rb) Yeshil Hupo
            db := Eshiyer(rb[i]);
        Tho
        Trepiho t := da + db + carry;
        res := res + Mitrer(t % 10);
        carry := t / 10;
    }
    Mushu carry > 0 Yeshil Hupo
        res := res + Mitrer(carry);
    Tho
    Omel srev(res);
Opa

Ruyoyo mul(a, b)
    Trepiho ra := srev(a);
    Trepiho rb := srev(b);
    Trepiho res := [];
    Pil (Trepiho i := 0; i < Purmo(ra) + Purmo(rb); i := i + 1) {
        Theki(res, 0);
    }
    Pil (Trepiho i := 0; i < Purmo(ra); i := i + 1) {
        Pil (Trepiho j := 0; j < Purmo(rb); j := j + 1) {
            res[i + j] := res[i + j] + Eshiyer(ra[i]) * Eshiyer(rb[j]);
        }
    }
    Pil (Trepiho i := 0; i < Purmo(res); i := i + 1) {
        Trepiho v := res[i];
        res[i] := v % 10;
        Mushu v / 10 > 0 Yeshil Hupo
            Mushu i + 1 < Purmo(res) Yeshil Hupo
                res[i + 1] := res[i + 1] + v / 10;
            Tho Thotri Hupo
                Theki(res, v / 10);
            Tho
        Tho
    }
    Trepiho s := "";
    Pil (Trepiho i := Purmo(res) - 1; i >= 0; i := i - 1) {
        s := s + Mitrer(res[i]);
    }
    Omel strip(s);
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho sp := 0;
    Pil (Trepiho i := 0; i < Purmo(line); i := i + 1) {
        Mushu line[i] = " " Yeshil Hupo
            sp := i;
        Tho
    }
    Trepiho a := substr(line, 0, sp);
    Trepiho b := substr(line, sp + 1, Purmo(line));
    Rashar add(a, b) + " " + mul(a, b);
    line := Thoke();
}
</solution>

<solution task="t2-life">
Ruyoyo count_neighbors(grid, R, C, r, c)
    Trepiho total := 0;
    Pil (Trepiho dr := -1; dr <= 1; dr := dr + 1) {
        Pil (Trepiho dc := -1; dc <= 1; dc := dc + 1) {
            Mushu dr = 0 Pethe dc = 0 Yeshil Hupo
                Tril;
            Tho
            Trepiho rr := r + dr;
            Trepiho cc := c + dc;
            Mushu rr >= 0 Pethe rr < R Pethe cc >= 0 Pethe cc < C Yeshil Hupo
                Mushu grid[rr][cc] = "#" Yeshil Hupo
                    total := total + 1;
                Tho
            Tho
        }
    }
    Omel total;
Opa

Ruyoyo next_gen(grid, R, C)
    Trepiho newgrid := [];
    Pil (Trepiho r := 0; r < R; r := r + 1) {
        Trepiho row := "";
        Pil (Trepiho c := 0; c < C; c := c + 1) {
            Trepiho nb := count_neighbors(grid, R, C, r, c);
            Mushu grid[r][c] = "#" Yeshil Hupo
                Mushu nb = 2 Hiyikra nb = 3 Yeshil Hupo
                    row := row + "#";
                Tho Thotri Hupo
                    row := row + ".";
                Tho
            Tho Thotri Hupo
                Mushu nb = 3 Yeshil Hupo
                    row := row + "#";
                Tho Thotri Hupo
                    row := row + ".";
                Tho
            Tho
        }
        Theki(newgrid, row);
    }
    Omel newgrid;
Opa

Trepiho g := Eshiyer(Thoke());
Trepiho grid := [];
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Theki(grid, line);
    line := Thoke();
}
Trepiho R := Purmo(grid);
Trepiho C := Purmo(grid[0]);
Pil (Trepiho gen := 0; gen < g; gen := gen + 1) {
    grid := next_gen(grid, R, C);
}
Pil (Trepiho r := 0; r < R; r := r + 1) {
    Rashar grid[r];
}
</solution>

<solution task="t2-rpn">
Ruyoyo tokenize(line)
    Trepiho toks := [];
    Trepiho cur := "";
    Pil (Trepiho i := 0; i < Purmo(line); i := i + 1) {
        Mushu line[i] = " " Yeshil Hupo
            Mushu cur ~= "" Yeshil Hupo
                Theki(toks, cur);
                cur := "";
            Tho
        Tho Thotri Hupo
            cur := cur + line[i];
        Tho
    }
    Mushu cur ~= "" Yeshil Hupo
        Theki(toks, cur);
    Tho
    Omel toks;
Opa

Ruyoyo is_number(t)
    Trepiho L := Purmo(t);
    Mushu L = 0 Yeshil Hupo
        Omel Yaki;
    Tho
    Trepiho start := 0;
    Mushu t[0] = "-" Yeshil Hupo
        Mushu L = 1 Yeshil Hupo
            Omel Yaki;
        Tho
        start := 1;
    Tho
    Pil (Trepiho i := start; i < L; i := i + 1) {
        Mushu Shurisho (t[i] >= "0" Pethe t[i] <= "9") Yeshil Hupo
            Omel Yaki;
        Tho
    }
    Omel Yupu;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho toks := tokenize(line);
    Trepiho err := Yaki;
    Trepiho stack := [];
    Pil (Trepiho j := 0; j < Purmo(toks); j := j + 1) {
        Theki(stack, 0);
    }
    Trepiho top := 0;
    Mushu Purmo(toks) = 0 Yeshil Hupo
        err := Yupu;
    Tho
    Trepiho i := 0;
    Rokomi (i < Purmo(toks) Pethe Shurisho err) {
        Trepiho t := toks[i];
        Mushu is_number(t) Yeshil Hupo
            stack[top] := Eshiyer(t);
            top := top + 1;
        Tho Thotri Mushu t = "+" Hiyikra t = "-" Hiyikra t = "*" Hiyikra t = "/" Hiyikra t = "%" Yeshil Hupo
            Mushu top < 2 Yeshil Hupo
                err := Yupu;
            Tho Thotri Hupo
                top := top - 1;
                Trepiho b := stack[top];
                top := top - 1;
                Trepiho a := stack[top];
                Mushu t = "+" Yeshil Hupo
                    stack[top] := a + b;
                    top := top + 1;
                Tho Thotri Mushu t = "-" Yeshil Hupo
                    stack[top] := a - b;
                    top := top + 1;
                Tho Thotri Mushu t = "*" Yeshil Hupo
                    stack[top] := a * b;
                    top := top + 1;
                Tho Thotri Mushu t = "/" Yeshil Hupo
                    Mushu b = 0 Yeshil Hupo
                        err := Yupu;
                    Tho Thotri Hupo
                        stack[top] := a / b;
                        top := top + 1;
                    Tho
                Tho Thotri Hupo
                    Mushu b = 0 Yeshil Hupo
                        err := Yupu;
                    Tho Thotri Hupo
                        stack[top] := a % b;
                        top := top + 1;
                    Tho
                Tho
            Tho
        Tho Thotri Hupo
            err := Yupu;
        Tho
        i := i + 1;
    }
    Mushu err Yeshil Hupo
        Rashar "error";
    Tho Thotri Mushu top ~= 1 Yeshil Hupo
        Rashar "error";
    Tho Thotri Hupo
        Rashar stack[0];
    Tho
    line := Thoke();
}
</solution>

<solution task="t2-wordfreq">
Ruyoyo lower(c)
    Trepiho ups := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    Trepiho los := "abcdefghijklmnopqrstuvwxyz";
    Mushu c >= "A" Pethe c <= "Z" Yeshil Hupo
        Pil (Trepiho i := 0; i < 26; i := i + 1) {
            Mushu c = ups[i] Yeshil Hupo
                Omel los[i];
            Tho
        }
    Tho
    Omel c;
Opa

Trepiho words := [];
Trepiho counts := [];
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho cur := "";
    Pil (Trepiho i := 0; i <= Purmo(line); i := i + 1) {
        Trepiho c := " ";
        Trepiho isletter := Yaki;
        Mushu i < Purmo(line) Yeshil Hupo
            c := line[i];
            Mushu (c >= "a" Pethe c <= "z") Hiyikra (c >= "A" Pethe c <= "Z") Yeshil Hupo
                isletter := Yupu;
            Tho
        Tho
        Mushu isletter Yeshil Hupo
            cur := cur + lower(c);
        Tho Thotri Mushu cur ~= "" Yeshil Hupo
            Trepiho idx := -1;
            Pil (Trepiho j := 0; j < Purmo(words); j := j + 1) {
                Mushu words[j] = cur Yeshil Hupo
                    idx := j;
                Tho
            }
            Mushu idx >= 0 Yeshil Hupo
                counts[idx] := counts[idx] + 1;
            Tho Thotri Hupo
                Theki(words, cur);
                Theki(counts, 1);
            Tho
            cur := "";
        Tho
    }
    line := Thoke();
}

Pil (Trepiho t := 0; t < 10; t := t + 1) {
    Trepiho best := -1;
    Pil (Trepiho j := 0; j < Purmo(words); j := j + 1) {
        Mushu counts[j] >= 0 Yeshil Hupo
            Mushu best < 0 Yeshil Hupo
                best := j;
            Tho Thotri Mushu counts[j] > counts[best] Yeshil Hupo
                best := j;
            Tho Thotri Mushu counts[j] = counts[best] Pethe words[j] < words[best] Yeshil Hupo
                best := j;
            Tho
        Tho
    }
    Mushu best >= 0 Yeshil Hupo
        Rashar words[best] + " " + counts[best];
        counts[best] := -1;
    Tho
}
</solution>