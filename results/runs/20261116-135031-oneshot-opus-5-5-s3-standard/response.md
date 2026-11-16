Notes on the approach:

- **Splitting lines.** Foshoxsho has no split builtin, so the tasks that read several values per line define a small `split` function.
- **Character tests.** There is no character-code builtin. Letter and digit tests use string ordering, and lowercasing does a lookup in an alphabet string.
- **Big numbers.** `t2-bignum` stores numbers in base 10000 to stay well inside the step limit.
- **Word frequencies.** `t2-wordfreq` merge-sorts the words, counts runs of equal words, then picks the top ten.

<solution task="t0-count">
Sogas line = Goshvovo();
Sogas n = Drak(line);
Paxfasva (Sogas i = 1; i <= n; i = i + 1) {
    Dosfasho i;
}
</solution>

<solution task="t0-day-names">
Sogas names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Ishsi (Drash(line) > 0) {
        Sogas n = Drak(line);
        Ishsi (n >= 1 Fas n <= 7) {
            Dosfasho names[n - 1];
        } Padri {
            Dosfasho "invalid";
        }
    }
    line = Goshvovo();
}
</solution>

<solution task="t0-even-odd">
Sogas ev = 0;
Sogas od = 0;
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Ishsi (Drash(line) > 0) {
        Sogas n = Drak(line);
        Ishsi (n Dodogo 2 == 0) {
            ev = ev + 1;
        } Padri {
            od = od + 1;
        }
    }
    line = Goshvovo();
}
Dosfasho "even " + ev;
Dosfasho "odd " + od;
</solution>

<solution task="t0-factorial">
Sogas n = Drak(Goshvovo());
Sogas f = 1;
Paxfasva (Sogas i = 2; i <= n; i = i + 1) {
    f = f * i;
}
Dosfasho f;
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
    Ishsi (Drash(line) > 0) {
        Sogas n = Drak(line);
        Sogas neg = n < 0;
        Sogas m = n;
        Ishsi (neg) {
            m = -n;
        }
        Sogas s = 0;
        Sogas r = 0;
        Sipokvix (m > 0) {
            Sogas d = m Dodogo 10;
            s = s + d;
            r = r * 10 + d;
            m = m / 10;
        }
        Ishsi (neg) {
            r = -r;
        }
        Dosfasho s + " " + r;
    }
    line = Goshvovo();
}
</solution>

<solution task="t1-floordiv">
Gis split(s) Fodashsa
    Sogas res = [];
    Sogas cur = "";
    Sogas has = Fixpodri;
    Paxfasva (Sogas i = 0; i < Drash(s); i = i + 1) {
        Sogas c = s[i];
        Ishsi (c == " " Gox c == "\t") {
            Ishsi (has) {
                Dragi(res, cur);
                cur = "";
                has = Fixpodri;
            }
        } Padri {
            cur = cur + c;
            has = Pigi;
        }
    }
    Ishsi (has) {
        Dragi(res, cur);
    }
    Asdra res;
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas toks = split(line);
    Ishsi (Drash(toks) >= 2) {
        Sogas a = Drak(toks[0]);
        Sogas b = Drak(toks[1]);
        Sogas q = a / b;
        Sogas r = a - b * q;
        Ishsi ((r < 0 Fas b > 0) Gox (r > 0 Fas b < 0)) {
            q = q - 1;
            r = r + b;
        }
        Dosfasho q + " " + r;
    }
    line = Goshvovo();
}
</solution>

<solution task="t1-palindromes">
Gis lowerChar(c) Fodashsa
    Ishsi (c >= "A" Fas c <= "Z") {
        Sogas U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        Sogas L = "abcdefghijklmnopqrstuvwxyz";
        Sogas lo = 0;
        Sogas hi = 25;
        Sipokvix (lo < hi) {
            Sogas mid = (lo + hi) / 2;
            Ishsi (U[mid] < c) {
                lo = mid + 1;
            } Padri {
                hi = mid;
            }
        }
        Asdra L[lo];
    }
    Asdra c;
Gosafax

Gis isAlnum(c) Fodashsa
    Asdra (c >= "a" Fas c <= "z") Gox (c >= "A" Fas c <= "Z") Gox (c >= "0" Fas c <= "9");
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
    Sogas a = 0;
    Sogas b = Drash(chars) - 1;
    Sipokvix (a < b) {
        Ishsi (chars[a] ~= chars[b]) {
            ok = Fixpodri;
            Fosvas;
        }
        a = a + 1;
        b = b - 1;
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
    Sogas res = [];
    Sogas cur = "";
    Sogas has = Fixpodri;
    Paxfasva (Sogas i = 0; i < Drash(s); i = i + 1) {
        Sogas c = s[i];
        Ishsi (c == " " Gox c == "\t") {
            Ishsi (has) {
                Dragi(res, cur);
                cur = "";
                has = Fixpodri;
            }
        } Padri {
            cur = cur + c;
            has = Pigi;
        }
    }
    Ishsi (has) {
        Dragi(res, cur);
    }
    Asdra res;
Gosafax

Sogas first = Goshvovo();
Ishsi (first ~= Dridrak) {
    Sogas toks = split(first);
    Sogas a = [];
    Paxfasva (Sogas i = 0; i < Drash(toks); i = i + 1) {
        Dragi(a, Drak(toks[i]));
    }
    Sogas n = Drash(a);
    Sogas line = Goshvovo();
    Sipokvix (line ~= Dridrak) {
        Ishsi (Drash(line) > 0) {
            Sogas q = Drak(line);
            Sogas lo = 0;
            Sogas hi = n;
            Sipokvix (lo < hi) {
                Sogas mid = (lo + hi) / 2;
                Ishsi (a[mid] < q) {
                    lo = mid + 1;
                } Padri {
                    hi = mid;
                }
            }
            Ishsi (lo < n Fas a[lo] == q) {
                Dosfasho lo + " found";
            } Padri {
                Dosfasho lo + " missing";
            }
        }
        line = Goshvovo();
    }
}
</solution>

<solution task="t1-rotate">
Sogas first = Goshvovo();
Ishsi (first ~= Dridrak) {
    Sogas k = Drak(first);
    Sogas items = [];
    Sogas line = Goshvovo();
    Sipokvix (line ~= Dridrak) {
        Dragi(items, line);
        line = Goshvovo();
    }
    Sogas n = Drash(items);
    Ishsi (n > 0) {
        Sogas s = k Dodogo n;
        Ishsi (s < 0) {
            s = s + n;
        }
        Paxfasva (Sogas i = 0; i < n; i = i + 1) {
            Dosfasho items[(i - s + n) Dodogo n];
        }
    }
}
</solution>

<solution task="t1-weekday">
Gis num(s, a, b) Fodashsa
    Sogas v = 0;
    Paxfasva (Sogas i = a; i < b; i = i + 1) {
        v = v * 10 + Drak(s[i]);
    }
    Asdra v;
Gosafax

Sogas names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
Sogas t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Ishsi (Drash(line) >= 10) {
        Sogas y = num(line, 0, 4);
        Sogas m = num(line, 5, 7);
        Sogas d = num(line, 8, 10);
        Ishsi (m < 3) {
            y = y - 1;
        }
        Sogas w = (y + y / 4 - y / 100 + y / 400 + t[m - 1] + d) Dodogo 7;
        Dosfasho names[w];
    }
    line = Goshvovo();
}
</solution>

<solution task="t2-bignum">
Gis split(s) Fodashsa
    Sogas res = [];
    Sogas cur = "";
    Sogas has = Fixpodri;
    Paxfasva (Sogas i = 0; i < Drash(s); i = i + 1) {
        Sogas c = s[i];
        Ishsi (c == " " Gox c == "\t") {
            Ishsi (has) {
                Dragi(res, cur);
                cur = "";
                has = Fixpodri;
            }
        } Padri {
            cur = cur + c;
            has = Pigi;
        }
    }
    Ishsi (has) {
        Dragi(res, cur);
    }
    Asdra res;
Gosafax

Gis parse(s) Fodashsa
    Sogas res = [];
    Sogas e = Drash(s);
    Sipokvix (e > 0) {
        Sogas st = e - 4;
        Ishsi (st < 0) {
            st = 0;
        }
        Sogas v = 0;
        Paxfasva (Sogas i = st; i < e; i = i + 1) {
            v = v * 10 + Drak(s[i]);
        }
        Dragi(res, v);
        e = st;
    }
    Ishsi (Drash(res) == 0) {
        Dragi(res, 0);
    }
    Asdra res;
Gosafax

Gis show(x) Fodashsa
    Sogas top = Drash(x) - 1;
    Sipokvix (top > 0 Fas x[top] == 0) {
        top = top - 1;
    }
    Sogas out = Igo(x[top]);
    Paxfasva (Sogas i = top - 1; i >= 0; i = i - 1) {
        Sogas v = x[i];
        Ishsi (v < 1000) {
            out = out + "0";
        }
        Ishsi (v < 100) {
            out = out + "0";
        }
        Ishsi (v < 10) {
            out = out + "0";
        }
        out = out + v;
    }
    Asdra out;
Gosafax

Gis add(a, b) Fodashsa
    Sogas res = [];
    Sogas carry = 0;
    Sogas la = Drash(a);
    Sogas lb = Drash(b);
    Sogas n = la;
    Ishsi (lb > n) {
        n = lb;
    }
    Paxfasva (Sogas i = 0; i < n; i = i + 1) {
        Sogas s = carry;
        Ishsi (i < la) {
            s = s + a[i];
        }
        Ishsi (i < lb) {
            s = s + b[i];
        }
        Dragi(res, s Dodogo 10000);
        carry = s / 10000;
    }
    Ishsi (carry > 0) {
        Dragi(res, carry);
    }
    Asdra res;
Gosafax

Gis mul(a, b) Fodashsa
    Sogas la = Drash(a);
    Sogas lb = Drash(b);
    Sogas res = [];
    Paxfasva (Sogas k = 0; k < la + lb; k = k + 1) {
        Dragi(res, 0);
    }
    Paxfasva (Sogas i = 0; i < la; i = i + 1) {
        Sogas x = a[i];
        Ishsi (x ~= 0) {
            Paxfasva (Sogas j = 0; j < lb; j = j + 1) {
                res[i + j] = res[i + j] + x * b[j];
            }
        }
    }
    Sogas carry = 0;
    Paxfasva (Sogas k = 0; k < la + lb; k = k + 1) {
        Sogas v = res[k] + carry;
        res[k] = v Dodogo 10000;
        carry = v / 10000;
    }
    Asdra res;
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas toks = split(line);
    Ishsi (Drash(toks) >= 2) {
        Sogas a = parse(toks[0]);
        Sogas b = parse(toks[1]);
        Dosfasho show(add(a, b)) + " " + show(mul(a, b));
    }
    line = Goshvovo();
}
</solution>

<solution task="t2-life">
Sogas g = Drak(Goshvovo());
Sogas grid = [];
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Ishsi (Drash(line) > 0) {
        Sogas row = [];
        Paxfasva (Sogas i = 0; i < Drash(line); i = i + 1) {
            Dragi(row, line[i] == "#");
        }
        Dragi(grid, row);
    }
    line = Goshvovo();
}
Sogas h = Drash(grid);
Sogas w = 0;
Ishsi (h > 0) {
    Sogas r0 = grid[0];
    w = Drash(r0);
}
Paxfasva (Sogas gen = 0; gen < g; gen = gen + 1) {
    Sogas ng = [];
    Paxfasva (Sogas r = 0; r < h; r = r + 1) {
        Sogas nrow = [];
        Paxfasva (Sogas c = 0; c < w; c = c + 1) {
            Sogas cnt = 0;
            Paxfasva (Sogas dr = -1; dr <= 1; dr = dr + 1) {
                Sogas rr = r + dr;
                Ishsi (rr >= 0 Fas rr < h) {
                    Sogas orow = grid[rr];
                    Paxfasva (Sogas dc = -1; dc <= 1; dc = dc + 1) {
                        Sogas cc = c + dc;
                        Ishsi ((dr ~= 0 Gox dc ~= 0) Fas cc >= 0 Fas cc < w) {
                            Ishsi (orow[cc]) {
                                cnt = cnt + 1;
                            }
                        }
                    }
                }
            }
            Sogas crow = grid[r];
            Sogas alive = crow[c];
            Sogas nv = Fixpodri;
            Ishsi (alive) {
                nv = cnt == 2 Gox cnt == 3;
            } Padri {
                nv = cnt == 3;
            }
            Dragi(nrow, nv);
        }
        Dragi(ng, nrow);
    }
    grid = ng;
}
Paxfasva (Sogas r = 0; r < h; r = r + 1) {
    Sogas prow = grid[r];
    Sogas out = "";
    Paxfasva (Sogas c = 0; c < w; c = c + 1) {
        Ishsi (prow[c]) {
            out = out + "#";
        } Padri {
            out = out + ".";
        }
    }
    Dosfasho out;
}
</solution>

<solution task="t2-rpn">
Gis split(s) Fodashsa
    Sogas res = [];
    Sogas cur = "";
    Sogas has = Fixpodri;
    Paxfasva (Sogas i = 0; i < Drash(s); i = i + 1) {
        Sogas c = s[i];
        Ishsi (c == " " Gox c == "\t") {
            Ishsi (has) {
                Dragi(res, cur);
                cur = "";
                has = Fixpodri;
            }
        } Padri {
            cur = cur + c;
            has = Pigi;
        }
    }
    Ishsi (has) {
        Dragi(res, cur);
    }
    Asdra res;
Gosafax

Gis isInt(t) Fodashsa
    Sogas n = Drash(t);
    Sogas st = 0;
    Ishsi (n > 0 Fas t[0] == "-") {
        st = 1;
    }
    Ishsi (n <= st) {
        Asdra Fixpodri;
    }
    Paxfasva (Sogas i = st; i < n; i = i + 1) {
        Sogas c = t[i];
        Ishsi (c < "0" Gox c > "9") {
            Asdra Fixpodri;
        }
    }
    Asdra Pigi;
Gosafax

Gis evalLine(line) Fodashsa
    Sogas toks = split(line);
    Ishsi (Drash(toks) == 0) {
        Asdra Dridrak;
    }
    Sogas st = [];
    Sogas sp = 0;
    Paxfasva (Sogas i = 0; i < Drash(toks); i = i + 1) {
        Sogas t = toks[i];
        Ishsi (isInt(t)) {
            Sogas v = Drak(t);
            Ishsi (sp < Drash(st)) {
                st[sp] = v;
            } Padri {
                Dragi(st, v);
            }
            sp = sp + 1;
        } Padri Ishsi (t == "+" Gox t == "-" Gox t == "*" Gox t == "/" Gox t == "%") {
            Ishsi (sp < 2) {
                Asdra Dridrak;
            }
            Sogas b = st[sp - 1];
            Sogas a = st[sp - 2];
            sp = sp - 2;
            Sogas r = 0;
            Pidok (t) {
            Dro "+":
                r = a + b;
            Dro "-":
                r = a - b;
            Dro "*":
                r = a * b;
            Dro "/":
                Ishsi (b == 0) {
                    Asdra Dridrak;
                }
                r = a / b;
            Papo:
                Ishsi (b == 0) {
                    Asdra Dridrak;
                }
                r = a Dodogo b;
            }
            Ishsi (sp < Drash(st)) {
                st[sp] = r;
            } Padri {
                Dragi(st, r);
            }
            sp = sp + 1;
        } Padri {
            Asdra Dridrak;
        }
    }
    Ishsi (sp ~= 1) {
        Asdra Dridrak;
    }
    Asdra st[0];
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas res = evalLine(line);
    Ishsi (res == Dridrak) {
        Dosfasho "error";
    } Padri {
        Dosfasho res;
    }
    line = Goshvovo();
}
</solution>

<solution task="t2-wordfreq">
Gis lowerChar(c) Fodashsa
    Ishsi (c >= "A" Fas c <= "Z") {
        Sogas U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        Sogas L = "abcdefghijklmnopqrstuvwxyz";
        Sogas lo = 0;
        Sogas hi = 25;
        Sipokvix (lo < hi) {
            Sogas mid = (lo + hi) / 2;
            Ishsi (U[mid] < c) {
                lo = mid + 1;
            } Padri {
                hi = mid;
            }
        }
        Asdra L[lo];
    }
    Asdra c;
Gosafax

Gis isLetter(c) Fodashsa
    Asdra (c >= "a" Fas c <= "z") Gox (c >= "A" Fas c <= "Z");
Gosafax

Gis msort(a) Fodashsa
    Sogas n = Drash(a);
    Ishsi (n <= 1) {
        Asdra a;
    }
    Sogas mid = n / 2;
    Sogas left = [];
    Sogas right = [];
    Paxfasva (Sogas i = 0; i < n; i = i + 1) {
        Ishsi (i < mid) {
            Dragi(left, a[i]);
        } Padri {
            Dragi(right, a[i]);
        }
    }
    left = msort(left);
    right = msort(right);
    Sogas res = [];
    Sogas p = 0;
    Sogas q = 0;
    Sogas ln = Drash(left);
    Sogas rn = Drash(right);
    Sipokvix (p < ln Fas q < rn) {
        Ishsi (right[q] < left[p]) {
            Dragi(res, right[q]);
            q = q + 1;
        } Padri {
            Dragi(res, left[p]);
            p = p + 1;
        }
    }
    Sipokvix (p < ln) {
        Dragi(res, left[p]);
        p = p + 1;
    }
    Sipokvix (q < rn) {
        Dragi(res, right[q]);
        q = q + 1;
    }
    Asdra res;
Gosafax

Sogas words = [];
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas cur = "";
    Paxfasva (Sogas i = 0; i < Drash(line); i = i + 1) {
        Sogas c = line[i];
        Ishsi (isLetter(c)) {
            cur = cur + lowerChar(c);
        } Padri {
            Ishsi (cur ~= "") {
                Dragi(words, cur);
                cur = "";
            }
        }
    }
    Ishsi (cur ~= "") {
        Dragi(words, cur);
    }
    line = Goshvovo();
}
Sogas sorted = msort(words);
Sogas dw = [];
Sogas dc = [];
Sogas nd = 0;
Paxfasva (Sogas i = 0; i < Drash(sorted); i = i + 1) {
    Sogas w = sorted[i];
    Ishsi (nd > 0 Fas dw[nd - 1] == w) {
        dc[nd - 1] = dc[nd - 1] + 1;
    } Padri {
        Dragi(dw, w);
        Dragi(dc, 1);
        nd = nd + 1;
    }
}
Sogas used = [];
Paxfasva (Sogas i = 0; i < nd; i = i + 1) {
    Dragi(used, Fixpodri);
}
Paxfasva (Sogas k = 0; k < 10; k = k + 1) {
    Sogas best = -1;
    Paxfasva (Sogas i = 0; i < nd; i = i + 1) {
        Ishsi (Ashgik (used[i])) {
            Ishsi (best == -1 Gox dc[i] > dc[best]) {
                best = i;
            }
        }
    }
    Ishsi (best == -1) {
        Fosvas;
    }
    used[best] = Pigi;
    Dosfasho dw[best] + " " + dc[best];
}
</solution>