<solution task="t0-count">
Sogas line = Goshvovo();
Sogas n = 0;
Ishsi (line ~= Dridrak) {
    n = Drak(line);
}
Paxfasva (Sogas i = 1; i <= n; i = i + 1) {
    Dosfasho i;
}
</solution>

<solution task="t0-day-names">
Sogas names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Ishsi (line ~= "") {
        Sogas n = Drak(line);
        Ishsi (n >= 1 Fas n <= 7) {
            Dosfasho names[n];
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
    Ishsi (line ~= "") {
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
Sogas i = Drash(lines);
Sipokvix (i >= 1) {
    Dosfasho lines[i];
    i = i - 1;
}
</solution>

<solution task="t1-digits">
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Ishsi (line ~= "") {
        Sogas n = Drak(line);
        Sogas neg = n < 0;
        Sogas a = n;
        Ishsi (neg) {
            a = -n;
        }
        Sogas s = Igo(a);
        Sogas sum = 0;
        Sogas rev = 0;
        Sogas i = Drash(s);
        Sipokvix (i >= 1) {
            Sogas d = Drak(s[i]);
            sum = sum + d;
            rev = rev * 10 + d;
            i = i - 1;
        }
        Ishsi (neg) {
            rev = -rev;
        }
        Dosfasho sum + " " + rev;
    }
    line = Goshvovo();
}
</solution>

<solution task="t1-floordiv">
Gis split(s) Fodashsa
    Sogas res = [];
    Sogas cur = "";
    Sogas i = 1;
    Sogas n = Drash(s);
    Sipokvix (i <= n) {
        Sogas c = s[i];
        Ishsi (c == " " Gox c == "\t" Gox c == "\r") {
            Ishsi (cur ~= "") {
                Dragi(res, cur);
                cur = "";
            }
        } Padri {
            cur = cur + c;
        }
        i = i + 1;
    }
    Ishsi (cur ~= "") {
        Dragi(res, cur);
    }
    Asdra res;
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas p = split(line);
    Ishsi (Drash(p) >= 2) {
        Sogas a = Drak(p[1]);
        Sogas b = Drak(p[2]);
        Sogas q = -((-a) / b);
        Sogas r = a - b * q;
        Dosfasho q + " " + r;
    }
    line = Goshvovo();
}
</solution>

<solution task="t1-palindromes">
Gis lowerOf(c) Fodashsa
    Sogas up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    Sogas low = "abcdefghijklmnopqrstuvwxyz";
    Paxfasva (Sogas i = 1; i <= 26; i = i + 1) {
        Ishsi (up[i] == c) {
            Asdra low[i];
        }
    }
    Asdra c;
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas chars = [];
    Sogas n = Drash(line);
    Paxfasva (Sogas i = 1; i <= n; i = i + 1) {
        Sogas c = line[i];
        Ishsi ((c >= "a" Fas c <= "z") Gox (c >= "0" Fas c <= "9")) {
            Dragi(chars, c);
        } Padri Ishsi (c >= "A" Fas c <= "Z") {
            Dragi(chars, lowerOf(c));
        }
    }
    Sogas a = 1;
    Sogas b = Drash(chars);
    Sogas ok = Pigi;
    Sipokvix (a < b) {
        Ishsi (chars[a] ~= chars[b]) {
            ok = Fixpodri;
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
    Sogas i = 1;
    Sogas n = Drash(s);
    Sipokvix (i <= n) {
        Sogas c = s[i];
        Ishsi (c == " " Gox c == "\t" Gox c == "\r") {
            Ishsi (cur ~= "") {
                Dragi(res, cur);
                cur = "";
            }
        } Padri {
            cur = cur + c;
        }
        i = i + 1;
    }
    Ishsi (cur ~= "") {
        Dragi(res, cur);
    }
    Asdra res;
Gosafax

Sogas first = Goshvovo();
Sogas arr = [];
Ishsi (first ~= Dridrak) {
    Sogas toks = split(first);
    Paxfasva (Sogas i = 1; i <= Drash(toks); i = i + 1) {
        Dragi(arr, Drak(toks[i]));
    }
}
Sogas n = Drash(arr);
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas qt = split(line);
    Ishsi (Drash(qt) > 0) {
        Sogas q = Drak(qt[1]);
        Sogas lo = 1;
        Sogas hi = n + 1;
        Sipokvix (lo < hi) {
            Sogas mid = (lo + hi - 1) / 2;
            Ishsi (arr[mid] < q) {
                lo = mid + 1;
            } Padri {
                hi = mid;
            }
        }
        Sogas found = Fixpodri;
        Ishsi (lo <= n) {
            Ishsi (arr[lo] == q) {
                found = Pigi;
            }
        }
        Ishsi (found) {
            Dosfasho (lo - 1) + " found";
        } Padri {
            Dosfasho (lo - 1) + " missing";
        }
    }
    line = Goshvovo();
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
Sogas n = Drash(items);
Ishsi (n > 0) {
    Sogas fq = -((-k) / n);
    Sogas shift = k - n * fq;
    Paxfasva (Sogas j = 0; j < n; j = j + 1) {
        Sogas idx = j - shift;
        Ishsi (idx < 0) {
            idx = idx + n;
        }
        Dosfasho items[idx + 1];
    }
}
</solution>

<solution task="t1-weekday">
Gis split(s) Fodashsa
    Sogas res = [];
    Sogas cur = "";
    Sogas i = 1;
    Sogas n = Drash(s);
    Sipokvix (i <= n) {
        Sogas c = s[i];
        Ishsi (c == " " Gox c == "\t" Gox c == "\r") {
            Ishsi (cur ~= "") {
                Dragi(res, cur);
                cur = "";
            }
        } Padri {
            cur = cur + c;
        }
        i = i + 1;
    }
    Ishsi (cur ~= "") {
        Dragi(res, cur);
    }
    Asdra res;
Gosafax

Gis fdiv(a, b) Fodashsa
    Asdra -((-a) / b);
Gosafax

Sogas t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
Sogas names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas toks = split(line);
    Ishsi (Drash(toks) > 0) {
        Sogas s = toks[1];
        Sogas y = Drak(s[1] + s[2] + s[3] + s[4]);
        Sogas m = Drak(s[6] + s[7]);
        Sogas d = Drak(s[9] + s[10]);
        Ishsi (m < 3) {
            y = y - 1;
        }
        Sogas v = y + fdiv(y, 4) - fdiv(y, 100) + fdiv(y, 400) + t[m] + d;
        Sogas r = v - 7 * fdiv(v, 7);
        Dosfasho names[r + 1];
    }
    line = Goshvovo();
}
</solution>

<solution task="t2-bignum">
Gis split(s) Fodashsa
    Sogas res = [];
    Sogas cur = "";
    Sogas i = 1;
    Sogas n = Drash(s);
    Sipokvix (i <= n) {
        Sogas c = s[i];
        Ishsi (c == " " Gox c == "\t" Gox c == "\r") {
            Ishsi (cur ~= "") {
                Dragi(res, cur);
                cur = "";
            }
        } Padri {
            cur = cur + c;
        }
        i = i + 1;
    }
    Ishsi (cur ~= "") {
        Dragi(res, cur);
    }
    Asdra res;
Gosafax

Gis fdiv(a, b) Fodashsa
    Asdra -((-a) / b);
Gosafax

Gis parse(s) Fodashsa
    Sogas r = [];
    Sogas i = Drash(s);
    Sipokvix (i >= 1) {
        Dragi(r, Drak(s[i]));
        i = i - 1;
    }
    Asdra r;
Gosafax

Gis addb(a, b) Fodashsa
    Sogas la = Drash(a);
    Sogas lb = Drash(b);
    Sogas n = la;
    Ishsi (lb > n) {
        n = lb;
    }
    Sogas res = [];
    Sogas carry = 0;
    Paxfasva (Sogas i = 1; i <= n; i = i + 1) {
        Sogas x = carry;
        Ishsi (i <= la) {
            x = x + a[i];
        }
        Ishsi (i <= lb) {
            x = x + b[i];
        }
        Ishsi (x >= 10) {
            Dragi(res, x - 10);
            carry = 1;
        } Padri {
            Dragi(res, x);
            carry = 0;
        }
    }
    Ishsi (carry > 0) {
        Dragi(res, carry);
    }
    Asdra res;
Gosafax

Gis mulb(a, b) Fodashsa
    Sogas la = Drash(a);
    Sogas lb = Drash(b);
    Sogas res = [];
    Paxfasva (Sogas k = 1; k <= la + lb; k = k + 1) {
        Dragi(res, 0);
    }
    Paxfasva (Sogas i = 1; i <= la; i = i + 1) {
        Sogas ai = a[i];
        Paxfasva (Sogas j = 1; j <= lb; j = j + 1) {
            res[i + j - 1] = res[i + j - 1] + ai * b[j];
        }
    }
    Sogas carry = 0;
    Paxfasva (Sogas k = 1; k <= la + lb; k = k + 1) {
        Sogas x = res[k] + carry;
        carry = fdiv(x, 10);
        res[k] = x - 10 * carry;
    }
    Asdra res;
Gosafax

Gis toStr(r) Fodashsa
    Sogas k = Drash(r);
    Sipokvix (k > 1 Fas r[k] == 0) {
        k = k - 1;
    }
    Sogas s = "";
    Sipokvix (k >= 1) {
        s = s + r[k];
        k = k - 1;
    }
    Asdra s;
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas p = split(line);
    Ishsi (Drash(p) >= 2) {
        Sogas a = parse(p[1]);
        Sogas b = parse(p[2]);
        Sogas s1 = toStr(addb(a, b));
        Sogas s2 = toStr(mulb(a, b));
        Dosfasho s1 + " " + s2;
    }
    line = Goshvovo();
}
</solution>

<solution task="t2-life">
Sogas g = Drak(Goshvovo());
Sogas rows = [];
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Ishsi (line ~= "") {
        Dragi(rows, line);
    }
    line = Goshvovo();
}
Sogas H = Drash(rows);
Ishsi (H == 0) {
    Asdra;
}
Sogas W = Drash(rows[1]);
Sogas cells = [];
Paxfasva (Sogas r = 1; r <= H; r = r + 1) {
    Sogas row = rows[r];
    Paxfasva (Sogas c = 1; c <= W; c = c + 1) {
        Ishsi (row[c] == "#") {
            Dragi(cells, 1);
        } Padri {
            Dragi(cells, 0);
        }
    }
}
Paxfasva (Sogas gen = 1; gen <= g; gen = gen + 1) {
    Sogas nxt = [];
    Paxfasva (Sogas r = 1; r <= H; r = r + 1) {
        Paxfasva (Sogas c = 1; c <= W; c = c + 1) {
            Sogas cnt = 0;
            Paxfasva (Sogas dr = -1; dr <= 1; dr = dr + 1) {
                Paxfasva (Sogas dc = -1; dc <= 1; dc = dc + 1) {
                    Ishsi (dr ~= 0 Gox dc ~= 0) {
                        Sogas rr = r + dr;
                        Sogas cc = c + dc;
                        Ishsi (rr >= 1 Fas rr <= H Fas cc >= 1 Fas cc <= W) {
                            cnt = cnt + cells[(rr - 1) * W + cc];
                        }
                    }
                }
            }
            Sogas alive = cells[(r - 1) * W + c];
            Ishsi (alive == 1 Fas (cnt == 2 Gox cnt == 3)) {
                Dragi(nxt, 1);
            } Padri Ishsi (alive == 0 Fas cnt == 3) {
                Dragi(nxt, 1);
            } Padri {
                Dragi(nxt, 0);
            }
        }
    }
    cells = nxt;
}
Paxfasva (Sogas r = 1; r <= H; r = r + 1) {
    Sogas s = "";
    Paxfasva (Sogas c = 1; c <= W; c = c + 1) {
        Ishsi (cells[(r - 1) * W + c] == 1) {
            s = s + "#";
        } Padri {
            s = s + ".";
        }
    }
    Dosfasho s;
}
</solution>

<solution task="t2-rpn">
Gis split(s) Fodashsa
    Sogas res = [];
    Sogas cur = "";
    Sogas i = 1;
    Sogas n = Drash(s);
    Sipokvix (i <= n) {
        Sogas c = s[i];
        Ishsi (c == " " Gox c == "\t" Gox c == "\r") {
            Ishsi (cur ~= "") {
                Dragi(res, cur);
                cur = "";
            }
        } Padri {
            cur = cur + c;
        }
        i = i + 1;
    }
    Ishsi (cur ~= "") {
        Dragi(res, cur);
    }
    Asdra res;
Gosafax

Gis isInt(t) Fodashsa
    Sogas n = Drash(t);
    Sogas st = 1;
    Ishsi (t[1] == "-") {
        st = 2;
    }
    Ishsi (st > n) {
        Asdra Fixpodri;
    }
    Paxfasva (Sogas i = st; i <= n; i = i + 1) {
        Sogas c = t[i];
        Ishsi (c < "0" Gox c > "9") {
            Asdra Fixpodri;
        }
    }
    Asdra Pigi;
Gosafax

Gis tdiv(a, b) Fodashsa
    Sogas aa = a;
    Ishsi (aa < 0) {
        aa = -aa;
    }
    Sogas bb = b;
    Ishsi (bb < 0) {
        bb = -bb;
    }
    Sogas q = -((-aa) / bb);
    Ishsi ((a < 0) ~= (b < 0)) {
        q = -q;
    }
    Asdra q;
Gosafax

Gis push(st, sp, v) Fodashsa
    Sogas np = sp + 1;
    Ishsi (np <= Drash(st)) {
        st[np] = v;
    } Padri {
        Dragi(st, v);
    }
    Asdra np;
Gosafax

Gis evalLine(line) Fodashsa
    Sogas toks = split(line);
    Ishsi (Drash(toks) == 0) {
        Asdra "error";
    }
    Sogas st = [];
    Sogas sp = 0;
    Paxfasva (Sogas i = 1; i <= Drash(toks); i = i + 1) {
        Sogas t = toks[i];
        Ishsi (t == "+" Gox t == "-" Gox t == "*" Gox t == "/" Gox t == "%") {
            Ishsi (sp < 2) {
                Asdra "error";
            }
            Sogas b = st[sp];
            Sogas a = st[sp - 1];
            sp = sp - 2;
            Sogas v = 0;
            Ishsi (t == "+") {
                v = a + b;
            } Padri Ishsi (t == "-") {
                v = a - b;
            } Padri Ishsi (t == "*") {
                v = a * b;
            } Padri {
                Ishsi (b == 0) {
                    Asdra "error";
                }
                Sogas q = tdiv(a, b);
                Ishsi (t == "/") {
                    v = q;
                } Padri {
                    v = a - b * q;
                }
            }
            sp = push(st, sp, v);
        } Padri Ishsi (isInt(t)) {
            sp = push(st, sp, Drak(t));
        } Padri {
            Asdra "error";
        }
    }
    Ishsi (sp ~= 1) {
        Asdra "error";
    }
    Asdra Igo(st[1]);
Gosafax

Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Dosfasho evalLine(line);
    line = Goshvovo();
}
</solution>

<solution task="t2-wordfreq">
Gis lowerOf(c) Fodashsa
    Sogas up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    Sogas low = "abcdefghijklmnopqrstuvwxyz";
    Sogas lo = 1;
    Sogas hi = 26;
    Sipokvix (lo < hi) {
        Sogas mid = (lo + hi - 1) / 2;
        Ishsi (up[mid] < c) {
            lo = mid + 1;
        } Padri {
            hi = mid;
        }
    }
    Asdra low[lo];
Gosafax

Gis msort(xs) Fodashsa
    Sogas n = Drash(xs);
    Ishsi (n <= 1) {
        Asdra xs;
    }
    Sogas h = n / 2;
    Sogas left = [];
    Sogas right = [];
    Paxfasva (Sogas i = 1; i <= h; i = i + 1) {
        Dragi(left, xs[i]);
    }
    Paxfasva (Sogas i = h + 1; i <= n; i = i + 1) {
        Dragi(right, xs[i]);
    }
    left = msort(left);
    right = msort(right);
    Sogas ln = Drash(left);
    Sogas rn = Drash(right);
    Sogas res = [];
    Sogas a = 1;
    Sogas b = 1;
    Sipokvix (a <= ln Fas b <= rn) {
        Ishsi (left[a] <= right[b]) {
            Dragi(res, left[a]);
            a = a + 1;
        } Padri {
            Dragi(res, right[b]);
            b = b + 1;
        }
    }
    Sipokvix (a <= ln) {
        Dragi(res, left[a]);
        a = a + 1;
    }
    Sipokvix (b <= rn) {
        Dragi(res, right[b]);
        b = b + 1;
    }
    Asdra res;
Gosafax

Sogas words = [];
Sogas line = Goshvovo();
Sipokvix (line ~= Dridrak) {
    Sogas cur = "";
    Sogas n = Drash(line);
    Paxfasva (Sogas i = 1; i <= n; i = i + 1) {
        Sogas c = line[i];
        Ishsi (c >= "a" Fas c <= "z") {
            cur = cur + c;
        } Padri Ishsi (c >= "A" Fas c <= "Z") {
            cur = cur + lowerOf(c);
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
Sogas uniq = [];
Sogas cnts = [];
Paxfasva (Sogas i = 1; i <= Drash(sorted); i = i + 1) {
    Sogas w = sorted[i];
    Sogas k = Drash(uniq);
    Sogas same = Fixpodri;
    Ishsi (k > 0) {
        Ishsi (uniq[k] == w) {
            same = Pigi;
        }
    }
    Ishsi (same) {
        cnts[k] = cnts[k] + 1;
    } Padri {
        Dragi(uniq, w);
        Dragi(cnts, 1);
    }
}
Sogas D = Drash(uniq);
Sogas used = [];
Paxfasva (Sogas i = 1; i <= D; i = i + 1) {
    Dragi(used, 0);
}
Paxfasva (Sogas round = 1; round <= 10; round = round + 1) {
    Sogas best = 0;
    Paxfasva (Sogas i = 1; i <= D; i = i + 1) {
        Ishsi (used[i] == 0) {
            Ishsi (best == 0) {
                best = i;
            } Padri Ishsi (cnts[i] > cnts[best]) {
                best = i;
            }
        }
    }
    Ishsi (best == 0) {
        Fosvas;
    }
    used[best] = 1;
    Dosfasho uniq[best] + " " + cnts[best];
}
</solution>