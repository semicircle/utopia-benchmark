<solution task="t0-count">
Sogas n = Drak(Goshvovo());
Paxfasva (Sogas i = 1; i <= n; i = i + 1) {
    Dosfasho i;
}
</solution>

<solution task="t0-day-names">
Gis dayName(d) Fodashsa
    Sogas r = "invalid";
    Pidok (d) {
    Dro 1:
        r = "Monday";
    Dro 2:
        r = "Tuesday";
    Dro 3:
        r = "Wednesday";
    Dro 4:
        r = "Thursday";
    Dro 5:
        r = "Friday";
    Dro 6:
        r = "Saturday";
    Dro 7:
        r = "Sunday";
    Papo:
        r = "invalid";
    }
    Asdra r;
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Dosfasho dayName(Drak(line));
    line = Goshvovo();
}
</solution>

<solution task="t0-even-odd">
Sogas even = 0;
Sogas odd = 0;
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas n = Drak(line);
    Ishsi (n Dodogo 2 == 0) {
        even = even + 1;
    } Padri {
        odd = odd + 1;
    }
    line = Goshvovo();
}
Dosfasho "even " + even;
Dosfasho "odd " + odd;
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
Paxfasva (Sogas i = Drash(lines) - 1; i >= 0; i = i - 1) {
    Dosfasho lines[i];
}
</solution>

<solution task="t1-digits">
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas start = 0;
    Sogas neg = Fixpodri;
    Ishsi ((Drash(line) > 0) Fas (line[0] == "-")) {
        neg = Pigi;
        start = 1;
    }
    Sogas ds = [];
    Sogas sum = 0;
    Paxfasva (Sogas i = start; i < Drash(line); i = i + 1) {
        Sogas c = line[i];
        sum = sum + Drak(c);
        Dragi(ds, c);
    }
    Sogas rev = "";
    Sogas started = Fixpodri;
    Paxfasva (Sogas i = Drash(ds) - 1; i >= 0; i = i - 1) {
        Ishsi (started) {
            rev = rev + ds[i];
        } Padri Ishsi (ds[i] ~= "0") {
            started = Pigi;
            rev = rev + ds[i];
        }
    }
    Ishsi (rev == "") {
        rev = "0";
    }
    Sogas out = rev;
    Ishsi (neg Fas (rev ~= "0")) {
        out = "-" + rev;
    }
    Dosfasho sum + " " + out;
    line = Goshvovo();
}
</solution>

<solution task="t1-floordiv">
Gis tokens(line) Fodashsa
    Sogas out = [];
    Sogas cur = "";
    Sogas i = 0;
    Sipokvix (i < Drash(line)) {
        Sogas c = line[i];
        Ishsi (c == " ") {
            Ishsi (Drash(cur) > 0) {
                Dragi(out, cur);
                cur = "";
            }
        } Padri {
            cur = cur + c;
        }
        i = i + 1;
    }
    Ishsi (Drash(cur) > 0) {
        Dragi(out, cur);
    }
    Asdra out;
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas t = tokens(line);
    Sogas a = Drak(t[0]);
    Sogas b = Drak(t[1]);
    Sogas q = a / b;
    Sogas r = a Dodogo b;
    Ishsi ((r ~= 0) Fas ((r > 0) ~= (b > 0))) {
        q = q - 1;
        r = r + b;
    }
    Dosfasho q + " " + r;
    line = Goshvovo();
}
</solution>

<solution task="t1-palindromes">
Gis isAlnum(c) Fodashsa
    Ishsi (((c >= "A") Fas (c <= "Z")) Gox ((c >= "a") Fas (c <= "z")) Gox ((c >= "0") Fas (c <= "9"))) {
        Asdra Pigi;
    }
    Asdra Fixpodri;
Gosafax

Gis lowerChar(c) Fodashsa
    Sogas up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    Sogas lo = "abcdefghijklmnopqrstuvwxyz";
    Paxfasva (Sogas i = 0; i < 26; i = i + 1) {
        Ishsi (c == up[i]) {
            Asdra lo[i];
        }
    }
    Asdra c;
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas chars = [];
    Paxfasva (Sogas i = 0; i < Drash(line); i = i + 1) {
        Sogas c = line[i];
        Ishsi (isAlnum(c)) {
            Dragi(chars, lowerChar(c));
        }
    }
    Sogas ok = Pigi;
    Sogas L = Drash(chars);
    Paxfasva (Sogas i = 0; i < L / 2; i = i + 1) {
        Ishsi (chars[i] ~= chars[L - 1 - i]) {
            ok = Fixpodri;
            Fosvas;
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
Gis tokens(line) Fodashsa
    Sogas out = [];
    Sogas cur = "";
    Sogas i = 0;
    Sipokvix (i < Drash(line)) {
        Sogas c = line[i];
        Ishsi (c == " ") {
            Ishsi (Drash(cur) > 0) {
                Dragi(out, cur);
                cur = "";
            }
        } Padri {
            cur = cur + c;
        }
        i = i + 1;
    }
    Ishsi (Drash(cur) > 0) {
        Dragi(out, cur);
    }
    Asdra out;
Gosafax

Gis lowerBound(xs, x) Fodashsa
    Sogas lo = 0;
    Sogas hi = Drash(xs);
    Sipokvix (lo < hi) {
        Sogas mid = (lo + hi) / 2;
        Ishsi (xs[mid] < x) {
            lo = mid + 1;
        } Padri {
            hi = mid;
        }
    }
    Asdra lo;
Gosafax

Sogas first = Goshvovo();
Ishsi (first ~= Dridrak) {
    Sogas toks = tokens(first);
    Sogas xs = [];
    Paxfasva (Sogas i = 0; i < Drash(toks); i = i + 1) {
        Dragi(xs, Drak(toks[i]));
    }
    Sogas line = Goshvovo();
    Sipokvix (line ~= Dridrak) {
        Sogas q = Drak(line);
        Sogas idx = lowerBound(xs, q);
        Sogas msg = "missing";
        Ishsi ((idx < Drash(xs)) Fas (xs[idx] == q)) {
            msg = "found";
        }
        Dosfasho idx + " " + msg;
        line = Goshvovo();
    }
}
</solution>

<solution task="t1-rotate">
Sogas kline = Goshvovo();
Ishsi (kline == Dridrak) {
    Asdra;
}
Sogas k = Drak(kline);
Sogas items = [];
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Dragi(items, line);
    line = Goshvovo();
}
Sogas m = Drash(items);
Ishsi (m > 0) {
    Sogas r = k Dodogo m;
    Ishsi (r < 0) {
        r = r + m;
    }
    Sogas start = m - r;
    Ishsi (start == m) {
        start = 0;
    }
    Paxfasva (Sogas t = 0; t < m; t = t + 1) {
        Sogas idx = start + t;
        Ishsi (idx >= m) {
            idx = idx - m;
        }
        Dosfasho items[idx];
    }
}
</solution>

<solution task="t1-weekday">
Gis part(s, start, len) Fodashsa
    Sogas r = "";
    Paxfasva (Sogas i = 0; i < len; i = i + 1) {
        r = r + s[start + i];
    }
    Asdra r;
Gosafax

Gis weekdayName(h) Fodashsa
    Sogas r = "";
    Pidok (h) {
    Dro 0:
        r = "Saturday";
    Dro 1:
        r = "Sunday";
    Dro 2:
        r = "Monday";
    Dro 3:
        r = "Tuesday";
    Dro 4:
        r = "Wednesday";
    Dro 5:
        r = "Thursday";
    Dro 6:
        r = "Friday";
    Papo:
        r = "";
    }
    Asdra r;
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas y = Drak(part(line, 0, 4));
    Sogas mo = Drak(part(line, 5, 2));
    Sogas da = Drak(part(line, 8, 2));
    Ishsi (mo <= 2) {
        y = y - 1;
        mo = mo + 12;
    }
    Sogas k = y Dodogo 100;
    Sogas j = y / 100;
    Sogas h = (da + (13 * (mo + 1)) / 5 + k + k / 4 + j / 4 + 5 * j) Dodogo 7;
    Dosfasho weekdayName(h);
    line = Goshvovo();
}
</solution>

<solution task="t2-bignum">
Gis intToDigit(n) Fodashsa
    Sogas ds = "0123456789";
    Asdra ds[n];
Gosafax

Gis addNums(a, b) Fodashsa
    Sogas i = Drash(a) - 1;
    Sogas j = Drash(b) - 1;
    Sogas carry = 0;
    Sogas rev = "";
    Gosh {
        Sogas s = carry;
        Ishsi (i >= 0) {
            s = s + Drak(a[i]);
            i = i - 1;
        }
        Ishsi (j >= 0) {
            s = s + Drak(b[j]);
            j = j - 1;
        }
        rev = rev + intToDigit(s Dodogo 10);
        carry = s / 10;
    } Sipokvix ((i >= 0) Gox (j >= 0) Gox (carry > 0));
    Sogas res = "";
    Sogas started = Fixpodri;
    Paxfasva (Sogas k = Drash(rev) - 1; k >= 0; k = k - 1) {
        Ishsi (started) {
            res = res + rev[k];
        } Padri Ishsi (rev[k] ~= "0") {
            started = Pigi;
            res = res + rev[k];
        }
    }
    Ishsi (res == "") {
        res = "0";
    }
    Asdra res;
Gosafax

Gis mulNums(a, b) Fodashsa
    Sogas la = Drash(a);
    Sogas lb = Drash(b);
    Sogas res = [];
    Paxfasva (Sogas i = 0; i < la + lb; i = i + 1) {
        Dragi(res, 0);
    }
    Paxfasva (Sogas ii = la - 1; ii >= 0; ii = ii - 1) {
        Sogas carry = 0;
        Paxfasva (Sogas jj = lb - 1; jj >= 0; jj = jj - 1) {
            Sogas cur = res[ii + jj + 1] + Drak(a[ii]) * Drak(b[jj]) + carry;
            res[ii + jj + 1] = cur Dodogo 10;
            carry = cur / 10;
        }
        res[ii] = res[ii] + carry;
    }
    Sogas out = "";
    Sogas started = Fixpodri;
    Paxfasva (Sogas i = 0; i < la + lb; i = i + 1) {
        Ishsi (started) {
            out = out + intToDigit(res[i]);
        } Padri Ishsi (res[i] ~= 0) {
            started = Pigi;
            out = out + intToDigit(res[i]);
        }
    }
    Ishsi (out == "") {
        out = "0";
    }
    Asdra out;
Gosafax

Gis tokens(line) Fodashsa
    Sogas out = [];
    Sogas cur = "";
    Sogas i = 0;
    Sipokvix (i < Drash(line)) {
        Sogas c = line[i];
        Ishsi (c == " ") {
            Ishsi (Drash(cur) > 0) {
                Dragi(out, cur);
                cur = "";
            }
        } Padri {
            cur = cur + c;
        }
        i = i + 1;
    }
    Ishsi (Drash(cur) > 0) {
        Dragi(out, cur);
    }
    Asdra out;
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas t = tokens(line);
    Ishsi (Drash(t) == 2) {
        Dosfasho addNums(t[0], t[1]) + " " + mulNums(t[0], t[1]);
    }
    line = Goshvovo();
}
</solution>

<solution task="t2-life">
Gis neigh(grid, r, c) Fodashsa
    Sogas rows = Drash(grid);
    Sogas cols = Drash(grid[0]);
    Sogas n = 0;
    Paxfasva (Sogas dr = -1; dr <= 1; dr = dr + 1) {
        Paxfasva (Sogas dc = -1; dc <= 1; dc = dc + 1) {
            Ishsi ((dr == 0) Fas (dc == 0)) {
                Diga;
            }
            Sogas rr = r + dr;
            Sogas cc = c + dc;
            Ishsi ((rr >= 0) Fas (rr < rows) Fas (cc >= 0) Fas (cc < cols)) {
                Ishsi (grid[rr][cc] == "#") {
                    n = n + 1;
                }
            }
        }
    }
    Asdra n;
Gosafax

Sogas gline = Goshvovo();
Ishsi (gline == Dridrak) {
    Asdra;
}
Sogas g = Drak(gline);
Sogas grid = [];
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas row = [];
    Paxfasva (Sogas i = 0; i < Drash(line); i = i + 1) {
        Dragi(row, line[i]);
    }
    Dragi(grid, row);
    line = Goshvovo();
}
Sogas gen = 0;
Sipokvix (gen < g) {
    Sogas ng = [];
    Paxfasva (Sogas r = 0; r < Drash(grid); r = r + 1) {
        Sogas nrow = [];
        Paxfasva (Sogas c = 0; c < Drash(grid[r]); c = c + 1) {
            Sogas n = neigh(grid, r, c);
            Ishsi (grid[r][c] == "#") {
                Ishsi ((n == 2) Gox (n == 3)) {
                    Dragi(nrow, "#");
                } Padri {
                    Dragi(nrow, ".");
                }
            } Padri {
                Ishsi (n == 3) {
                    Dragi(nrow, "#");
                } Padri {
                    Dragi(nrow, ".");
                }
            }
        }
        Dragi(ng, nrow);
    }
    grid = ng;
    gen = gen + 1;
}
Paxfasva (Sogas r = 0; r < Drash(grid); r = r + 1) {
    Paxfasva (Sogas c = 0; c < Drash(grid[r]); c = c + 1) {
        Axdis grid[r][c];
    }
    Dosfasho "";
}
</solution>

<solution task="t2-rpn">
Gis tokens(line) Fodashsa
    Sogas out = [];
    Sogas cur = "";
    Sogas i = 0;
    Sipokvix (i < Drash(line)) {
        Sogas c = line[i];
        Ishsi (c == " ") {
            Ishsi (Drash(cur) > 0) {
                Dragi(out, cur);
                cur = "";
            }
        } Padri {
            cur = cur + c;
        }
        i = i + 1;
    }
    Ishsi (Drash(cur) > 0) {
        Dragi(out, cur);
    }
    Asdra out;
Gosafax

Gis isOp(t) Fodashsa
    Ishsi (Drash(t) == 1) {
        Sogas c = t[0];
        Ishsi ((c == "+") Gox (c == "-") Gox (c == "*") Gox (c == "/") Gox (c == "%")) {
            Asdra Pigi;
        }
    }
    Asdra Fixpodri;
Gosafax

Gis isInt(t) Fodashsa
    Sogas L = Drash(t);
    Ishsi (L == 0) {
        Asdra Fixpodri;
    }
    Sogas s = 0;
    Ishsi (t[0] == "-") {
        Ishsi (L < 2) {
            Asdra Fixpodri;
        }
        s = 1;
    }
    Paxfasva (Sogas i = s; i < L; i = i + 1) {
        Sogas c = t[i];
        Ishsi (Ashgik ((c >= "0") Fas (c <= "9"))) {
            Asdra Fixpodri;
        }
    }
    Asdra Pigi;
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas toks = tokens(line);
    Sogas st = [];
    Sogas top = 0;
    Sogas bad = Fixpodri;
    Ishsi (Drash(toks) == 0) {
        bad = Pigi;
    }
    Paxfasva (Sogas ti = 0; ((ti < Drash(toks)) Fas (Ashgik bad)); ti = ti + 1) {
        Sogas t = toks[ti];
        Ishsi (isOp(t)) {
            Ishsi (top < 2) {
                bad = Pigi;
                Fosvas;
            }
            Sogas b = st[top - 1];
            Sogas a = st[top - 2];
            Sogas res = 0;
            Ishsi (t[0] == "+") {
                res = a + b;
            } Padri Ishsi (t[0] == "-") {
                res = a - b;
            } Padri Ishsi (t[0] == "*") {
                res = a * b;
            } Padri Ishsi (t[0] == "/") {
                Ishsi (b == 0) {
                    bad = Pigi;
                    Fosvas;
                }
                res = a / b;
            } Padri {
                Ishsi (b == 0) {
                    bad = Pigi;
                    Fosvas;
                }
                res = a Dodogo b;
            }
            st[top - 2] = res;
            top = top - 1;
        } Padri Ishsi (isInt(t)) {
            Dragi(st, Drak(t));
            top = top + 1;
        } Padri {
            bad = Pigi;
            Fosvas;
        }
    }
    Ishsi ((Ashgik bad) Fas (top == 1)) {
        Dosfasho st[0];
    } Padri {
        Dosfasho "error";
    }
    line = Goshvovo();
}
</solution>

<solution task="t2-wordfreq">
Gis isLetter(c) Fodashsa
    Ishsi (((c >= "A") Fas (c <= "Z")) Gox ((c >= "a") Fas (c <= "z"))) {
        Asdra Pigi;
    }
    Asdra Fixpodri;
Gosafax

Gis lowerChar(c) Fodashsa
    Sogas up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    Sogas lo = "abcdefghijklmnopqrstuvwxyz";
    Paxfasva (Sogas i = 0; i < 26; i = i + 1) {
        Ishsi (c == up[i]) {
            Asdra lo[i];
        }
    }
    Asdra c;
Gosafax

Gis addWord(w, words, counts) Fodashsa
    Sogas found = -1;
    Paxfasva (Sogas j = 0; j < Drash(words); j = j + 1) {
        Ishsi (words[j] == w) {
            found = j;
            Fosvas;
        }
    }
    Ishsi (found >= 0) {
        counts[found] = counts[found] + 1;
    } Padri {
        Dragi(words, w);
        Dragi(counts, 1);
    }
    Asdra Dridrak;
Gosafax

Sogas words = [];
Sogas counts = [];
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas cur = "";
    Paxfasva (Sogas i = 0; i < Drash(line); i = i + 1) {
        Sogas c = line[i];
        Ishsi (isLetter(c)) {
            cur = cur + lowerChar(c);
        } Padri {
            Ishsi (cur ~= "") {
                addWord(cur, words, counts);
                cur = "";
            }
        }
    }
    Ishsi (cur ~= "") {
        addWord(cur, words, counts);
    }
    line = Goshvovo();
}
Sogas D = Drash(words);
Paxfasva (Sogas t = 0; (t < 10) Fas (t < D); t = t + 1) {
    Sogas best = -1;
    Paxfasva (Sogas j = 0; j < D; j = j + 1) {
        Ishsi (counts[j] ~= -1) {
            Ishsi (best == -1) {
                best = j;
            } Padri Ishsi (counts[j] > counts[best]) {
                best = j;
            } Padri Ishsi ((counts[j] == counts[best]) Fas (words[j] < words[best])) {
                best = j;
            }
        }
    }
    Dosfasho words[best] + " " + counts[best];
    counts[best] = -1;
}
</solution>