<solution task="t0-count">
Sogas n = Drak(Goshvovo());
Paxfasva (Sogas i = 1; i <= n; i = i + 1) {
    Dosfasho i;
}
</solution>

<solution task="t0-day-names">
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Pidok (line) {
    Dro "1":
        Dosfasho "Monday";
        Fosvas;
    Dro "2":
        Dosfasho "Tuesday";
        Fosvas;
    Dro "3":
        Dosfasho "Wednesday";
        Fosvas;
    Dro "4":
        Dosfasho "Thursday";
        Fosvas;
    Dro "5":
        Dosfasho "Friday";
        Fosvas;
    Dro "6":
        Dosfasho "Saturday";
        Fosvas;
    Dro "7":
        Dosfasho "Sunday";
        Fosvas;
    Papo:
        Dosfasho "invalid";
    }
    line = Goshvovo();
}
</solution>

<solution task="t0-even-odd">
Sogas ev = 0;
Sogas od = 0;
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas n = Drak(line);
    Ishsi (n Dodogo 2 == 0) {
        ev = ev + 1;
    } Padri {
        od = od + 1;
    }
    line = Goshvovo();
}
Dosfasho "even " + ev;
Dosfasho "odd " + od;
</solution>

<solution task="t0-factorial">
Sogas n = Drak(Goshvovo());
Sogas r = 1;
Paxfasva (Sogas i = 2; i <= n; i = i + 1) {
    r = r * i;
}
Dosfasho r;
</solution>

<solution task="t0-fizzbuzz">
Sogas n = Drak(Goshvovo());
Paxfasva (Sogas i = 1; i <= n; i = i + 1) {
    Ishsi (i Dodogo 15 == 0) {
        Dosfasho "FizzBuzz";
    } Padri Ishsi (i Dodogo 3 == 0) {
        Dosfasho "Fizz";
    } Padri Ishsi (i Dodogo 5 == 0) {
        Dosfasho "Buzz";
    } Padri {
        Dosfasho i;
    }
}
</solution>

<solution task="t0-hello">
Dosfasho "Hello, Utopia!";
</solution>

<solution task="t0-reverse-lines">
Sogas lines = [];
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Dragi(lines, line);
    line = Goshvovo();
}
Sogas i = Drash(lines);
Sipokvix (i >= 1) {
    Dosfasho lines[i];
    i = i - 1;
}
</solution>

<solution task="t1-digits">
Gis substr(s, i, j) Fodashsa
    Sogas r = "";
    Paxfasva (Sogas k = i; k <= j; k = k + 1) {
        r = r + s[k];
    }
    Asdra r;
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas s = line;
    Sogas neg = Fixpodri;
    Ishsi (s[1] == "-") {
        neg = Pigi;
        s = substr(s, 2, Drash(s));
    }
    Sogas total = 0;
    Sogas rev = "";
    Paxfasva (Sogas i = 1; i <= Drash(s); i = i + 1) {
        total = total + Drak(s[i]);
        rev = s[i] + rev;
    }
    Sogas r = Drak(rev);
    Ishsi (r == 0) {
        Dosfasho total + " 0";
    } Padri Ishsi (neg) {
        Dosfasho total + " -" + r;
    } Padri {
        Dosfasho total + " " + r;
    }
    line = Goshvovo();
}
</solution>

<solution task="t1-floordiv">
Gis substr(s, i, j) Fodashsa
    Sogas r = "";
    Paxfasva (Sogas k = i; k <= j; k = k + 1) {
        r = r + s[k];
    }
    Asdra r;
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas p = 0;
    Paxfasva (Sogas i = 1; i <= Drash(line); i = i + 1) {
        Ishsi (p == 0) {
            Ishsi (line[i] == " ") {
                p = i;
            }
        }
    }
    Sogas a = Drak(substr(line, 1, p - 1));
    Sogas b = Drak(substr(line, p + 1, Drash(line)));
    Sogas q = a / b;
    Ishsi (a - b * q ~= 0) {
        q = q - 1;
    }
    Dosfasho q + " " + (a - b * q);
    line = Goshvovo();
}
</solution>

<solution task="t1-palindromes">
Gis alnum(c) Fodashsa
    Ishsi (("A" <= c Fas c <= "Z") Gox ("a" <= c Fas c <= "z") Gox ("0" <= c Fas c <= "9")) {
        Asdra Pigi;
    }
    Asdra Fixpodri;
Gosafax

Gis tolower(c) Fodashsa
    Sogas ups = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    Sogas los = "abcdefghijklmnopqrstuvwxyz";
    Paxfasva (Sogas i = 1; i <= 26; i = i + 1) {
        Ishsi (c == ups[i]) {
            Asdra los[i];
        }
    }
    Asdra c;
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas t = "";
    Paxfasva (Sogas i = 1; i <= Drash(line); i = i + 1) {
        Ishsi (alnum(line[i])) {
            t = t + tolower(line[i]);
        }
    }
    Sogas n = Drash(t);
    Sogas ok = Pigi;
    Paxfasva (Sogas i = 1; i <= n; i = i + 1) {
        Ishsi (t[i] ~= t[n + 1 - i]) {
            ok = Fixpodri;
        }
    }
    Ishsi (ok) {
        Dosfasho "yes";
    } Padri {
        Dosfasho "no";
    }
    line = Goshvovo();
}
</solution>

<solution task="t1-rank">
Gis split(s) Fodashsa
    Sogas parts = [];
    Sogas cur = "";
    Paxfasva (Sogas i = 1; i <= Drash(s); i = i + 1) {
        Ishsi (s[i] == " ") {
            Ishsi (cur ~= "") {
                Dragi(parts, cur);
            }
            cur = "";
        } Padri {
            cur = cur + s[i];
        }
    }
    Ishsi (cur ~= "") {
        Dragi(parts, cur);
    }
    Asdra parts;
Gosafax

Sogas first = Goshvovo();
Sogas nums = [];
Ishsi (first ~= Dridrak) {
    Ishsi (first ~= "") {
        nums = split(first);
    }
}
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas q = Drak(line);
    Sogas less = 0;
    Sogas found = Fixpodri;
    Paxfasva (Sogas i = 1; i <= Drash(nums); i = i + 1) {
        Sogas v = Drak(nums[i]);
        Ishsi (v < q) {
            less = less + 1;
        }
        Ishsi (v == q) {
            found = Pigi;
        }
    }
    Ishsi (found) {
        Dosfasho less + " found";
    } Padri {
        Dosfasho less + " missing";
    }
    line = Goshvovo();
}
</solution>

<solution task="t1-rotate">
Sogas kline = Goshvovo();
Ishsi (kline ~= Dridrak) {
    Sogas k = Drak(kline);
    Sogas items = [];
    Sogas line = Goshvovo();
    Sipokvix (line ~= Dridrak) {
        Dragi(items, line);
        line = Goshvovo();
    }
    Sogas n = Drash(items);
    Ishsi (n > 0) {
        k = k Dodogo n;
        Ishsi (k < 0) {
            k = k + n;
        }
        Paxfasva (Sogas j = 1; j <= n; j = j + 1) {
            Sogas idx = j - k;
            Ishsi (idx < 1) {
                idx = idx + n;
            }
            Dosfasho items[idx];
        }
    }
}
</solution>

<solution task="t1-weekday">
Gis substr(s, i, j) Fodashsa
    Sogas r = "";
    Paxfasva (Sogas k = i; k <= j; k = k + 1) {
        r = r + s[k];
    }
    Asdra r;
Gosafax

Gis floordiv(a, b) Fodashsa
    Sogas q = a / b;
    Ishsi (a - b * q ~= 0) {
        q = q - 1;
    }
    Asdra q;
Gosafax

Gis isleap(y) Fodashsa
    Ishsi (y Dodogo 400 == 0) {
        Asdra Pigi;
    }
    Ishsi (y Dodogo 100 == 0) {
        Asdra Fixpodri;
    }
    Asdra y Dodogo 4 == 0;
Gosafax

Gis daysbefore(y) Fodashsa
    Sogas yy = y - 1;
    Asdra 365 * yy + floordiv(yy, 4) - floordiv(yy, 100) + floordiv(yy, 400);
Gosafax

Sogas names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
Sogas mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas y = Drak(substr(line, 1, 4));
    Sogas m = Drak(substr(line, 6, 7));
    Sogas d = Drak(substr(line, 9, 10));
    Sogas doy = d;
    Paxfasva (Sogas i = 1; i < m; i = i + 1) {
        doy = doy + mdays[i];
    }
    Ishsi (m > 2) {
        Ishsi (isleap(y)) {
            doy = doy + 1;
        }
    }
    Sogas offset = daysbefore(y) + doy - 1;
    Dosfasho names[(offset Dodogo 7) + 1];
    line = Goshvovo();
}
</solution>

<solution task="t2-bignum">
Gis substr(s, i, j) Fodashsa
    Sogas r = "";
    Paxfasva (Sogas k = i; k <= j; k = k + 1) {
        r = r + s[k];
    }
    Asdra r;
Gosafax

Gis split(s) Fodashsa
    Sogas parts = [];
    Sogas cur = "";
    Paxfasva (Sogas i = 1; i <= Drash(s); i = i + 1) {
        Ishsi (s[i] == " ") {
            Ishsi (cur ~= "") {
                Dragi(parts, cur);
            }
            cur = "";
        } Padri {
            cur = cur + s[i];
        }
    }
    Ishsi (cur ~= "") {
        Dragi(parts, cur);
    }
    Asdra parts;
Gosafax

Gis toChunks(s) Fodashsa
    Sogas chunks = [];
    Sogas i = Drash(s);
    Gosh {
        Sogas lo = i - 3;
        Ishsi (lo < 1) {
            lo = 1;
        }
        Sogas v = 0;
        Paxfasva (Sogas k = lo; k <= i; k = k + 1) {
            v = v * 10 + Drak(s[k]);
        }
        Dragi(chunks, v);
        i = lo - 1;
    } Sipokvix (i >= 1);
    Asdra chunks;
Gosafax

Gis pad4(v) Fodashsa
    Sogas s = Igo(v);
    Sogas r = s;
    Paxfasva (Sogas i = Drash(s) + 1; i <= 4; i = i + 1) {
        r = "0" + r;
    }
    Asdra r;
Gosafax

Gis chunksToStr(cs) Fodashsa
    Sogas n = Drash(cs);
    Sipokvix (n > 1) {
        Ishsi (cs[n] == 0) {
            n = n - 1;
        } Padri {
            Fosvas;
        }
    }
    Sogas r = Igo(cs[n]);
    Paxfasva (Sogas i = n - 1; i >= 1; i = i - 1) {
        r = r + pad4(cs[i]);
    }
    Asdra r;
Gosafax

Gis addBig(a, b) Fodashsa
    Sogas r = [];
    Sogas carry = 0;
    Sogas n = Drash(a);
    Ishsi (Drash(b) > n) {
        n = Drash(b);
    }
    Paxfasva (Sogas i = 1; i <= n; i = i + 1) {
        Sogas av = 0;
        Sogas bv = 0;
        Ishsi (i <= Drash(a)) {
            av = a[i];
        }
        Ishsi (i <= Drash(b)) {
            bv = b[i];
        }
        Sogas cur = av + bv + carry;
        Ishsi (cur >= 10000) {
            cur = cur - 10000;
            carry = 1;
        } Padri {
            carry = 0;
        }
        Dragi(r, cur);
    }
    Ishsi (carry == 1) {
        Dragi(r, 1);
    }
    Asdra r;
Gosafax

Gis mulBig(a, b) Fodashsa
    Sogas r = [];
    Paxfasva (Sogas i = 1; i <= Drash(a) + Drash(b); i = i + 1) {
        Dragi(r, 0);
    }
    Paxfasva (Sogas i = 1; i <= Drash(a); i = i + 1) {
        Sogas carry = 0;
        Paxfasva (Sogas j = 1; j <= Drash(b); j = j + 1) {
            Sogas cur = r[i + j - 1] + a[i] * b[j] + carry;
            r[i + j - 1] = cur Dodogo 10000;
            carry = cur / 10000;
        }
        r[i + Drash(b)] = r[i + Drash(b)] + carry;
    }
    Asdra r;
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas parts = split(line);
    Sogas as = parts[1];
    Sogas bs = parts[2];
    Dosfasho chunksToStr(addBig(toChunks(as), toChunks(bs))) + " " + chunksToStr(mulBig(toChunks(as), toChunks(bs)));
    line = Goshvovo();
}
</solution>

<solution task="t2-life">
Gis cell(grid, r, c) Fodashsa
    Ishsi (r < 1) {
        Asdra ".";
    }
    Ishsi (r > Drash(grid)) {
        Asdra ".";
    }
    Sogas row = grid[r];
    Ishsi (c < 1) {
        Asdra ".";
    }
    Ishsi (c > Drash(row)) {
        Asdra ".";
    }
    Asdra row[c];
Gosafax

Gis ncount(grid, r, c) Fodashsa
    Sogas n = 0;
    Paxfasva (Sogas dr = -1; dr <= 1; dr = dr + 1) {
        Paxfasva (Sogas dc = -1; dc <= 1; dc = dc + 1) {
            Ishsi (dr ~= 0 Gox dc ~= 0) {
                Ishsi (cell(grid, r + dr, c + dc) == "#") {
                    n = n + 1;
                }
            }
        }
    }
    Asdra n;
Gosafax

Sogas gline = Goshvovo();
Ishsi (gline ~= Dridrak) {
    Sogas g = Drak(gline);
    Sogas grid = [];
    Sogas line = Goshvovo();
    Sipokvix (line ~= Dridrak) {
        Dragi(grid, line);
        line = Goshvovo();
    }
    Paxfasva (Sogas gen = 1; gen <= g; gen = gen + 1) {
        Sogas next = [];
        Paxfasva (Sogas r = 1; r <= Drash(grid); r = r + 1) {
            Sogas row = "";
            Paxfasva (Sogas c = 1; c <= Drash(grid[r]); c = c + 1) {
                Sogas n = ncount(grid, r, c);
                Ishsi (grid[r][c] == "#") {
                    Ishsi (n == 2 Gox n == 3) {
                        row = row + "#";
                    } Padri {
                        row = row + ".";
                    }
                } Padri {
                    Ishsi (n == 3) {
                        row = row + "#";
                    } Padri {
                        row = row + ".";
                    }
                }
            }
            Dragi(next, row);
        }
        grid = next;
    }
    Paxfasva (Sogas r = 1; r <= Drash(grid); r = r + 1) {
        Dosfasho grid[r];
    }
}
</solution>

<solution task="t2-rpn">
Gis split(s) Fodashsa
    Sogas parts = [];
    Sogas cur = "";
    Paxfasva (Sogas i = 1; i <= Drash(s); i = i + 1) {
        Ishsi (s[i] == " ") {
            Ishsi (cur ~= "") {
                Dragi(parts, cur);
            }
            cur = "";
        } Padri {
            cur = cur + s[i];
        }
    }
    Ishsi (cur ~= "") {
        Dragi(parts, cur);
    }
    Asdra parts;
Gosafax

Gis take(xs, n) Fodashsa
    Sogas r = [];
    Paxfasva (Sogas i = 1; i <= n; i = i + 1) {
        Dragi(r, xs[i]);
    }
    Asdra r;
Gosafax

Gis isDigit(c) Fodashsa
    Asdra "0" <= c Fas c <= "9";
Gosafax

Gis isOp(t) Fodashsa
    Asdra t == "+" Gox t == "-" Gox t == "*" Gox t == "/" Gox t == "%";
Gosafax

Gis isIntTok(t) Fodashsa
    Sogas n = Drash(t);
    Ishsi (n == 0) {
        Asdra Fixpodri;
    }
    Sogas i = 1;
    Ishsi (t[1] == "-") {
        Ishsi (n == 1) {
            Asdra Fixpodri;
        }
        i = 2;
    }
    Paxfasva (Sogas k = i; k <= n; k = k + 1) {
        Ishsi (Ashgik (isDigit(t[k]))) {
            Asdra Fixpodri;
        }
    }
    Asdra Pigi;
Gosafax

Gis divz(a, b) Fodashsa
    Sogas q = a / b;
    Sogas r = a - b * q;
    Ishsi (r ~= 0) {
        Ishsi (r < 0 ~= (a < 0)) {
            Ishsi (r < 0 == (b < 0)) {
                q = q + 1;
            } Padri {
                q = q - 1;
            }
        }
    }
    Asdra q;
Gosafax

Gis modz(a, b) Fodashsa
    Asdra a - b * divz(a, b);
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas toks = split(line);
    Sogas st = [];
    Sogas err = Fixpodri;
    Paxfasva (Sogas ti = 1; ti <= Drash(toks); ti = ti + 1) {
        Ishsi (Ashgik err) {
            Sogas t = toks[ti];
            Ishsi (isOp(t)) {
                Ishsi (Drash(st) < 2) {
                    err = Pigi;
                } Padri {
                    Sogas b = st[Drash(st)];
                    Sogas a = st[Drash(st) - 1];
                    st = take(st, Drash(st) - 2);
                    Ishsi (t == "+") {
                        Dragi(st, a + b);
                    } Padri Ishsi (t == "-") {
                        Dragi(st, a - b);
                    } Padri Ishsi (t == "*") {
                        Dragi(st, a * b);
                    } Padri {
                        Ishsi (b == 0) {
                            err = Pigi;
                        } Padri {
                            Ishsi (t == "/") {
                                Dragi(st, divz(a, b));
                            } Padri {
                                Dragi(st, modz(a, b));
                            }
                        }
                    }
                }
            } Padri Ishsi (isIntTok(t)) {
                Dragi(st, Drak(t));
            } Padri {
                err = Pigi;
            }
        }
    }
    Ishsi (err Gox Drash(st) ~= 1) {
        Dosfasho "error";
    } Padri {
        Dosfasho st[1];
    }
    line = Goshvovo();
}
</solution>

<solution task="t2-wordfreq">
Gis isLetter(c) Fodashsa
    Asdra ("A" <= c Fas c <= "Z") Gox ("a" <= c Fas c <= "z");
Gosafax

Gis tolower(c) Fodashsa
    Sogas ups = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    Sogas los = "abcdefghijklmnopqrstuvwxyz";
    Paxfasva (Sogas i = 1; i <= 26; i = i + 1) {
        Ishsi (c == ups[i]) {
            Asdra los[i];
        }
    }
    Asdra c;
Gosafax

Gis addWord(words, counts, w) Fodashsa
    Paxfasva (Sogas i = 1; i <= Drash(words); i = i + 1) {
        Ishsi (words[i] == w) {
            counts[i] = counts[i] + 1;
            Asdra;
        }
    }
    Dragi(words, w);
    Dragi(counts, 1);
Gosafax

Gis without(xs, k) Fodashsa
    Sogas r = [];
    Paxfasva (Sogas i = 1; i <= Drash(xs); i = i + 1) {
        Ishsi (i ~= k) {
            Dragi(r, xs[i]);
        }
    }
    Asdra r;
Gosafax

Sogas words = [];
Sogas counts = [];
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas cur = "";
    Paxfasva (Sogas i = 1; i <= Drash(line); i = i + 1) {
        Sogas c = line[i];
        Ishsi (isLetter(c)) {
            cur = cur + tolower(c);
        } Padri {
            Ishsi (cur ~= "") {
                addWord(words, counts, cur);
                cur = "";
            }
        }
    }
    Ishsi (cur ~= "") {
        addWord(words, counts, cur);
    }
    line = Goshvovo();
}

Paxfasva (Sogas t = 1; t <= 10; t = t + 1) {
    Ishsi (Drash(words) == 0) {
        Fosvas;
    }
    Sogas bi = 1;
    Paxfasva (Sogas i = 2; i <= Drash(words); i = i + 1) {
        Ishsi (counts[i] > counts[bi]) {
            bi = i;
        } Padri Ishsi (counts[i] == counts[bi]) {
            Ishsi (words[i] < words[bi]) {
                bi = i;
            }
        }
    }
    Dosfasho words[bi] + " " + counts[bi];
    words = without(words, bi);
    counts = without(counts, bi);
}
</solution>