The 17 solutions follow, one per task in the order given. None of them has been run.

A few choices apply to several tasks:
- **Splitting lines:** Yemora has no substring or split builtin, so I wrote a `split` function. It breaks a line on spaces, tabs and carriage returns.
- **Character tests:** there is no character-code builtin. Letters and digits are recognised by comparing one-character strings, for example `c >= "a" Pethe c <= "z"`. Upper-case letters are converted by a lookup in an alphabet string.
- **Empty lines:** tasks that parse integers skip completely empty lines instead of failing on them.

<solution task="t0-count">
Trepiho n := Eshiyer(Thoke());
Pil (Trepiho i := 1; i <= n; i := i + 1) {
    Rashar i;
}
</solution>

<solution task="t0-day-names">
Trepiho names := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Mushu line ~= "" Yeshil Hupo
        Trepiho n := Eshiyer(line);
        Mushu n >= 1 Pethe n <= 7 Yeshil Hupo
            Rashar names[n - 1];
        Tho Thotri Hupo
            Rashar "invalid";
        Tho
    Tho
    line := Thoke();
}
</solution>

<solution task="t0-even-odd">
Trepiho ev := 0;
Trepiho od := 0;
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Mushu line ~= "" Yeshil Hupo
        Trepiho n := Eshiyer(line);
        Mushu n % 2 = 0 Yeshil Hupo
            ev := ev + 1;
        Tho Thotri Hupo
            od := od + 1;
        Tho
    Tho
    line := Thoke();
}
Rashar "even " + ev;
Rashar "odd " + od;
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
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Mushu line ~= "" Yeshil Hupo
        Trepiho n := Eshiyer(line);
        Trepiho neg := n < 0;
        Mushu neg Yeshil Hupo
            n := 0 - n;
        Tho
        Trepiho s := 0;
        Trepiho r := 0;
        Rokomi (n > 0) {
            Trepiho d := n % 10;
            s := s + d;
            r := r * 10 + d;
            n := n / 10;
        }
        Mushu neg Yeshil Hupo
            r := 0 - r;
        Tho
        Rashar s + " " + r;
    Tho
    line := Thoke();
}
</solution>

<solution task="t1-floordiv">
Ruyoyo split(s)
    Trepiho res := [];
    Trepiho cur := "";
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Trepiho c := s[i];
        Mushu c = " " Hiyikra c = "\t" Hiyikra c = "\r" Yeshil Hupo
            Mushu Purmo(cur) > 0 Yeshil Hupo
                Theki(res, cur);
                cur := "";
            Tho
        Tho Thotri Hupo
            cur := cur + c;
        Tho
    }
    Mushu Purmo(cur) > 0 Yeshil Hupo
        Theki(res, cur);
    Tho
    Omel res;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho toks := split(line);
    Mushu Purmo(toks) >= 2 Yeshil Hupo
        Trepiho a := Eshiyer(toks[0]);
        Trepiho b := Eshiyer(toks[1]);
        Trepiho q := a / b;
        Trepiho r := a % b;
        Mushu (r < 0 Pethe b > 0) Hiyikra (r > 0 Pethe b < 0) Yeshil Hupo
            q := q - 1;
            r := r + b;
        Tho
        Rashar q + " " + r;
    Tho
    line := Thoke();
}
</solution>

<solution task="t1-palindromes">
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

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho cs := [];
    Pil (Trepiho i := 0; i < Purmo(line); i := i + 1) {
        Trepiho c := line[i];
        Mushu (c >= "a" Pethe c <= "z") Hiyikra (c >= "0" Pethe c <= "9") Yeshil Hupo
            Theki(cs, c);
        Tho Thotri Mushu c >= "A" Pethe c <= "Z" Yeshil Hupo
            Theki(cs, lower(c));
        Tho
    }
    Trepiho ok := Yupu;
    Trepiho a := 0;
    Trepiho b := Purmo(cs) - 1;
    Rokomi (a < b) {
        Mushu cs[a] ~= cs[b] Yeshil Hupo
            ok := Yaki;
            Kiyetrel;
        Tho
        a := a + 1;
        b := b - 1;
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
Ruyoyo split(s)
    Trepiho res := [];
    Trepiho cur := "";
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Trepiho c := s[i];
        Mushu c = " " Hiyikra c = "\t" Hiyikra c = "\r" Yeshil Hupo
            Mushu Purmo(cur) > 0 Yeshil Hupo
                Theki(res, cur);
                cur := "";
            Tho
        Tho Thotri Hupo
            cur := cur + c;
        Tho
    }
    Mushu Purmo(cur) > 0 Yeshil Hupo
        Theki(res, cur);
    Tho
    Omel res;
Opa

Trepiho first := Thoke();
Mushu first = Krupelro Yeshil Hupo
    Omel;
Tho
Trepiho toks := split(first);
Trepiho arr := [];
Pil (Trepiho i := 0; i < Purmo(toks); i := i + 1) {
    Theki(arr, Eshiyer(toks[i]));
}
Trepiho n := Purmo(arr);
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho qt := split(line);
    Mushu Purmo(qt) > 0 Yeshil Hupo
        Trepiho q := Eshiyer(qt[0]);
        Trepiho lo := 0;
        Trepiho hi := n;
        Rokomi (lo < hi) {
            Trepiho mid := (lo + hi) / 2;
            Mushu arr[mid] < q Yeshil Hupo
                lo := mid + 1;
            Tho Thotri Hupo
                hi := mid;
            Tho
        }
        Mushu lo < n Pethe arr[lo] = q Yeshil Hupo
            Rashar lo + " found";
        Tho Thotri Hupo
            Rashar lo + " missing";
        Tho
    Tho
    line := Thoke();
}
</solution>

<solution task="t1-rotate">
Trepiho first := Thoke();
Mushu first = Krupelro Yeshil Hupo
    Omel;
Tho
Trepiho k := Eshiyer(first);
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
    Pil (Trepiho i := 0; i < n; i := i + 1) {
        Rashar items[(i - s + n) % n];
    }
Tho
</solution>

<solution task="t1-weekday">
Trepiho names := ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
Trepiho t := [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Mushu Purmo(line) >= 10 Yeshil Hupo
        Trepiho y := Eshiyer(line[0]) * 1000 + Eshiyer(line[1]) * 100 + Eshiyer(line[2]) * 10 + Eshiyer(line[3]);
        Trepiho m := Eshiyer(line[5]) * 10 + Eshiyer(line[6]);
        Trepiho d := Eshiyer(line[8]) * 10 + Eshiyer(line[9]);
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
    Trepiho res := [];
    Trepiho cur := "";
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Trepiho c := s[i];
        Mushu c = " " Hiyikra c = "\t" Hiyikra c = "\r" Yeshil Hupo
            Mushu Purmo(cur) > 0 Yeshil Hupo
                Theki(res, cur);
                cur := "";
            Tho
        Tho Thotri Hupo
            cur := cur + c;
        Tho
    }
    Mushu Purmo(cur) > 0 Yeshil Hupo
        Theki(res, cur);
    Tho
    Omel res;
Opa

Ruyoyo todigits(s)
    Trepiho ds := [];
    Pil (Trepiho i := Purmo(s) - 1; i >= 0; i := i - 1) {
        Theki(ds, Eshiyer(s[i]));
    }
    Omel ds;
Opa

Ruyoyo tostr(ds)
    Trepiho top := Purmo(ds) - 1;
    Rokomi (top > 0 Pethe ds[top] = 0) {
        top := top - 1;
    }
    Trepiho s := "";
    Pil (Trepiho i := top; i >= 0; i := i - 1) {
        s := s + ds[i];
    }
    Omel s;
Opa

Ruyoyo add(a, b)
    Trepiho la := Purmo(a);
    Trepiho lb := Purmo(b);
    Trepiho n := la;
    Mushu lb > n Yeshil Hupo
        n := lb;
    Tho
    Trepiho res := [];
    Trepiho carry := 0;
    Pil (Trepiho i := 0; i < n; i := i + 1) {
        Trepiho x := carry;
        Mushu i < la Yeshil Hupo
            x := x + a[i];
        Tho
        Mushu i < lb Yeshil Hupo
            x := x + b[i];
        Tho
        Theki(res, x % 10);
        carry := x / 10;
    }
    Mushu carry > 0 Yeshil Hupo
        Theki(res, carry);
    Tho
    Omel res;
Opa

Ruyoyo mul(a, b)
    Trepiho la := Purmo(a);
    Trepiho lb := Purmo(b);
    Trepiho res := [];
    Pil (Trepiho k := 0; k < la + lb; k := k + 1) {
        Theki(res, 0);
    }
    Pil (Trepiho i := 0; i < la; i := i + 1) {
        Trepiho ai := a[i];
        Mushu ai ~= 0 Yeshil Hupo
            Pil (Trepiho j := 0; j < lb; j := j + 1) {
                res[i + j] := res[i + j] + ai * b[j];
            }
        Tho
    }
    Trepiho carry := 0;
    Pil (Trepiho k := 0; k < la + lb; k := k + 1) {
        Trepiho x := res[k] + carry;
        res[k] := x % 10;
        carry := x / 10;
    }
    Rokomi (carry > 0) {
        Theki(res, carry % 10);
        carry := carry / 10;
    }
    Omel res;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho toks := split(line);
    Mushu Purmo(toks) >= 2 Yeshil Hupo
        Trepiho a := todigits(toks[0]);
        Trepiho b := todigits(toks[1]);
        Rashar tostr(add(a, b)) + " " + tostr(mul(a, b));
    Tho
    line := Thoke();
}
</solution>

<solution task="t2-life">
Trepiho g := Eshiyer(Thoke());
Trepiho grid := [];
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Mushu line ~= "" Yeshil Hupo
        Trepiho row := [];
        Pil (Trepiho j := 0; j < Purmo(line); j := j + 1) {
            Mushu line[j] = "#" Yeshil Hupo
                Theki(row, 1);
            Tho Thotri Mushu line[j] = "." Yeshil Hupo
                Theki(row, 0);
            Tho
        }
        Theki(grid, row);
    Tho
    line := Thoke();
}
Trepiho h := Purmo(grid);
Trepiho w := 0;
Mushu h > 0 Yeshil Hupo
    w := Purmo(grid[0]);
Tho
Pil (Trepiho gen := 0; gen < g; gen := gen + 1) {
    Trepiho ng := [];
    Pil (Trepiho i := 0; i < h; i := i + 1) {
        Trepiho nr := [];
        Trepiho cr := grid[i];
        Pil (Trepiho j := 0; j < w; j := j + 1) {
            Trepiho cnt := 0;
            Pil (Trepiho di := -1; di <= 1; di := di + 1) {
                Pil (Trepiho dj := -1; dj <= 1; dj := dj + 1) {
                    Trepiho ii := i + di;
                    Trepiho jj := j + dj;
                    Mushu (di ~= 0 Hiyikra dj ~= 0) Pethe ii >= 0 Pethe ii < h Pethe jj >= 0 Pethe jj < w Yeshil Hupo
                        Trepiho rr := grid[ii];
                        cnt := cnt + rr[jj];
                    Tho
                }
            }
            Mushu cr[j] = 1 Yeshil Hupo
                Mushu cnt = 2 Hiyikra cnt = 3 Yeshil Hupo
                    Theki(nr, 1);
                Tho Thotri Hupo
                    Theki(nr, 0);
                Tho
            Tho Thotri Hupo
                Mushu cnt = 3 Yeshil Hupo
                    Theki(nr, 1);
                Tho Thotri Hupo
                    Theki(nr, 0);
                Tho
            Tho
        }
        Theki(ng, nr);
    }
    grid := ng;
}
Pil (Trepiho i := 0; i < h; i := i + 1) {
    Trepiho s := "";
    Trepiho cr := grid[i];
    Pil (Trepiho j := 0; j < w; j := j + 1) {
        Mushu cr[j] = 1 Yeshil Hupo
            s := s + "#";
        Tho Thotri Hupo
            s := s + ".";
        Tho
    }
    Rashar s;
}
</solution>

<solution task="t2-rpn">
Ruyoyo split(s)
    Trepiho res := [];
    Trepiho cur := "";
    Pil (Trepiho i := 0; i < Purmo(s); i := i + 1) {
        Trepiho c := s[i];
        Mushu c = " " Hiyikra c = "\t" Hiyikra c = "\r" Yeshil Hupo
            Mushu Purmo(cur) > 0 Yeshil Hupo
                Theki(res, cur);
                cur := "";
            Tho
        Tho Thotri Hupo
            cur := cur + c;
        Tho
    }
    Mushu Purmo(cur) > 0 Yeshil Hupo
        Theki(res, cur);
    Tho
    Omel res;
Opa

Ruyoyo isInt(t)
    Trepiho start := 0;
    Mushu Purmo(t) > 0 Pethe t[0] = "-" Yeshil Hupo
        start := 1;
    Tho
    Mushu start >= Purmo(t) Yeshil Hupo
        Omel Yaki;
    Tho
    Pil (Trepiho i := start; i < Purmo(t); i := i + 1) {
        Trepiho c := t[i];
        Mushu Shurisho (c >= "0" Pethe c <= "9") Yeshil Hupo
            Omel Yaki;
        Tho
    }
    Omel Yupu;
Opa

Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho toks := split(line);
    Trepiho st := [];
    Trepiho sp := 0;
    Trepiho err := Purmo(toks) = 0;
    Pil (Trepiho i := 0; i < Purmo(toks) Pethe Shurisho err; i := i + 1) {
        Trepiho t := toks[i];
        Trepiho havev := Yaki;
        Trepiho v := 0;
        Mushu t = "+" Hiyikra t = "-" Hiyikra t = "*" Hiyikra t = "/" Hiyikra t = "%" Yeshil Hupo
            Mushu sp < 2 Yeshil Hupo
                err := Yupu;
            Tho Thotri Hupo
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
                Sher "/", "%"
                    Mushu b = 0 Yeshil Hupo
                        err := Yupu;
                    Tho Thotri Mushu t = "/" Yeshil Hupo
                        v := a / b;
                    Tho Thotri Hupo
                        v := a % b;
                    Tho
                Tho Pakru
                havev := Yupu;
            Tho
        Tho Thotri Mushu isInt(t) Yeshil Hupo
            v := Eshiyer(t);
            havev := Yupu;
        Tho Thotri Hupo
            err := Yupu;
        Tho
        Mushu havev Pethe Shurisho err Yeshil Hupo
            Mushu sp < Purmo(st) Yeshil Hupo
                st[sp] := v;
            Tho Thotri Hupo
                Theki(st, v);
            Tho
            sp := sp + 1;
        Tho
    }
    Mushu err Hiyikra sp ~= 1 Yeshil Hupo
        Rashar "error";
    Tho Thotri Hupo
        Rashar st[0];
    Tho
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

Ruyoyo msort(xs)
    Trepiho n := Purmo(xs);
    Mushu n <= 1 Yeshil Hupo
        Omel xs;
    Tho
    Trepiho mid := n / 2;
    Trepiho left := [];
    Trepiho right := [];
    Pil (Trepiho i := 0; i < n; i := i + 1) {
        Mushu i < mid Yeshil Hupo
            Theki(left, xs[i]);
        Tho Thotri Hupo
            Theki(right, xs[i]);
        Tho
    }
    left := msort(left);
    right := msort(right);
    Trepiho res := [];
    Trepiho a := 0;
    Trepiho b := 0;
    Trepiho la := Purmo(left);
    Trepiho lb := Purmo(right);
    Rokomi (a < la Pethe b < lb) {
        Mushu left[a] <= right[b] Yeshil Hupo
            Theki(res, left[a]);
            a := a + 1;
        Tho Thotri Hupo
            Theki(res, right[b]);
            b := b + 1;
        Tho
    }
    Rokomi (a < la) {
        Theki(res, left[a]);
        a := a + 1;
    }
    Rokomi (b < lb) {
        Theki(res, right[b]);
        b := b + 1;
    }
    Omel res;
Opa

Trepiho words := [];
Trepiho line := Thoke();
Rokomi (line ~= Krupelro) {
    Trepiho cur := "";
    Pil (Trepiho i := 0; i < Purmo(line); i := i + 1) {
        Trepiho c := line[i];
        Mushu c >= "a" Pethe c <= "z" Yeshil Hupo
            cur := cur + c;
        Tho Thotri Mushu c >= "A" Pethe c <= "Z" Yeshil Hupo
            cur := cur + lower(c);
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
words := msort(words);
Trepiho uw := [];
Trepiho uc := [];
Pil (Trepiho i := 0; i < Purmo(words); i := i + 1) {
    Trepiho wd := words[i];
    Mushu Purmo(uw) > 0 Pethe uw[Purmo(uw) - 1] = wd Yeshil Hupo
        uc[Purmo(uc) - 1] := uc[Purmo(uc) - 1] + 1;
    Tho Thotri Hupo
        Theki(uw, wd);
        Theki(uc, 1);
    Tho
}
Trepiho used := [];
Pil (Trepiho i := 0; i < Purmo(uw); i := i + 1) {
    Theki(used, Yaki);
}
Pil (Trepiho k := 0; k < 10 Pethe k < Purmo(uw); k := k + 1) {
    Trepiho best := -1;
    Pil (Trepiho j := 0; j < Purmo(uw); j := j + 1) {
        Mushu Shurisho used[j] Yeshil Hupo
            Mushu best = -1 Yeshil Hupo
                best := j;
            Tho Thotri Mushu uc[j] > uc[best] Yeshil Hupo
                best := j;
            Tho
        Tho
    }
    used[best] := Yupu;
    Rashar uw[best] + " " + uc[best];
}
</solution>