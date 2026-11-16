<solution task="t0-count">
sheye n <- odresdra(diwela());
sho (sheye i <- 1; i <= n; i <- i + 1) {
    wami i;
}
</solution>

<solution task="t0-day-names">
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(line) > 0) {
        sheye d <- odresdra(line);
        moumare amdre d
        amdre 1
            wami "Monday";
        amdre 2
            wami "Tuesday";
        amdre 3
            wami "Wednesday";
        amdre 4
            wami "Thursday";
        amdre 5
            wami "Friday";
        amdre 6
            wami "Saturday";
        amdre 7
            wami "Sunday";
        amdre oli
            wami "invalid";
        bawoum moumare
    }
    line <- diwela();
}
</solution>

<solution task="t0-even-odd">
sheye ev <- 0;
sheye od <- 0;
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(line) > 0) {
        sheye n <- odresdra(line);
        wesosa ((n drossou 2) = 0) {
            ev <- ev + 1;
        } oli {
            od <- od + 1;
        }
    }
    line <- diwela();
}
wami "even " + ev;
wami "odd " + od;
</solution>

<solution task="t0-factorial">
sheye n <- odresdra(diwela());
sheye f <- 1;
sho (sheye i <- 2; i <= n; i <- i + 1) {
    f <- f * i;
}
wami f;
</solution>

<solution task="t0-fizzbuzz">
sheye n <- odresdra(diwela());
sho (sheye i <- 1; i <= n; i <- i + 1) {
    wesosa ((i drossou 15) = 0) {
        wami "FizzBuzz";
    } oli wesosa ((i drossou 3) = 0) {
        wami "Fizz";
    } oli wesosa ((i drossou 5) = 0) {
        wami "Buzz";
    } oli {
        wami i;
    }
}
</solution>

<solution task="t0-hello">
wami "Hello, Utopia!";
</solution>

<solution task="t0-reverse-lines">
sheye xs <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(xs, line);
    line <- diwela();
}
sho (sheye i <- louwo(xs) - 1; i >= 0; i <- i - 1) {
    wami xs[i];
}
</solution>

<solution task="t1-digits">
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(line) > 0) {
        sheye n <- odresdra(line);
        sheye neg <- n < 0;
        sheye m <- n;
        wesosa (neg) {
            m <- -n;
        }
        sheye s <- 0;
        sheye r <- 0;
        veshim (m > 0) {
            sheye dg <- m drossou 10;
            s <- s + dg;
            r <- (r * 10) + dg;
            m <- m / 10;
        }
        wesosa (neg) {
            r <- -r;
        }
        wami (ramou(s) + " ") + ramou(r);
    }
    line <- diwela();
}
</solution>

<solution task="t1-floordiv">
tosedo split(s)
    sheye out <- [];
    sheye cur <- "";
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        sheye c <- s[i];
        wesosa (c = " ") {
            wesosa (louwo(cur) > 0) {
                omse(out, cur);
                cur <- "";
            }
        } oli {
            cur <- cur + c;
        }
    }
    wesosa (louwo(cur) > 0) {
        omse(out, cur);
    }
    cha out;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye toks <- split(line);
    wesosa (louwo(toks) >= 2) {
        sheye a <- odresdra(toks[0]);
        sheye b <- odresdra(toks[1]);
        sheye q <- a / b;
        sheye r <- a - (b * q);
        wami (ramou(q) + " ") + ramou(r);
    }
    line <- diwela();
}
</solution>

<solution task="t1-palindromes">
tosedo lowerChar(c)
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sheye lo <- "abcdefghijklmnopqrstuvwxyz";
    sho (sheye i <- 0; i < 26; i <- i + 1) {
        wesosa (up[i] = c) {
            cha lo[i];
        }
    }
    cha c;
bawoum tosedo

tosedo isAlnum(c)
    wesosa ((c >= "0") dilisyo (c <= "9")) {
        cha shilsa;
    }
    wesosa ((c >= "a") dilisyo (c <= "z")) {
        cha shilsa;
    }
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        cha shilsa;
    }
    cha ishe;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye cs <- [];
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- line[i];
        wesosa (isAlnum(c)) {
            wesosa ((c >= "A") dilisyo (c <= "Z")) {
                c <- lowerChar(c);
            }
            omse(cs, c);
        }
    }
    sheye ok <- shilsa;
    sheye n <- louwo(cs);
    sho (i <- 0; i < (n / 2); i <- i + 1) {
        wesosa (cs[i] <> cs[(n - 1) - i]) {
            ok <- ishe;
        }
    }
    wesosa (ok) {
        wami "yes";
    } oli {
        wami "no";
    }
    line <- diwela();
}
</solution>

<solution task="t1-rank">
tosedo split(s)
    sheye out <- [];
    sheye cur <- "";
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        sheye c <- s[i];
        wesosa (c = " ") {
            wesosa (louwo(cur) > 0) {
                omse(out, cur);
                cur <- "";
            }
        } oli {
            cur <- cur + c;
        }
    }
    wesosa (louwo(cur) > 0) {
        omse(out, cur);
    }
    cha out;
bawoum tosedo

sheye first <- diwela();
sheye arr <- [];
wesosa (first <> malwe) {
    sheye toks <- split(first);
    sho (sheye i <- 0; i < louwo(toks); i <- i + 1) {
        omse(arr, odresdra(toks[i]));
    }
}
sheye n <- louwo(arr);
sheye line <- diwela();
veshim (line <> malwe) {
    sheye qt <- split(line);
    wesosa (louwo(qt) > 0) {
        sheye q <- odresdra(qt[0]);
        sheye lo <- 0;
        sheye hi <- n;
        veshim (lo < hi) {
            sheye mid <- (lo + hi) / 2;
            wesosa (arr[mid] < q) {
                lo <- mid + 1;
            } oli {
                hi <- mid;
            }
        }
        sheye res <- "missing";
        wesosa (lo < n) {
            wesosa (arr[lo] = q) {
                res <- "found";
            }
        }
        wami (ramou(lo) + " ") + res;
    }
    line <- diwela();
}
</solution>

<solution task="t1-rotate">
sheye kl <- diwela();
wesosa (kl = malwe) {
    cha;
}
sheye k <- odresdra(kl);
sheye items <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(items, line);
    line <- diwela();
}
sheye n <- louwo(items);
wesosa (n = 0) {
    cha;
}
sheye s <- k drossou n;
sho (sheye i <- 0; i < n; i <- i + 1) {
    wami items[(i - s) drossou n];
}
</solution>

<solution task="t1-weekday">
tosedo num(s, a, b)
    sheye v <- 0;
    sho (sheye i <- a; i <= b; i <- i + 1) {
        v <- (v * 10) + odresdra(s[i]);
    }
    cha v;
bawoum tosedo

sheye names <- ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
sheye t <- [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(line) >= 10) {
        sheye y <- num(line, 0, 3);
        sheye m <- num(line, 5, 6);
        sheye d <- num(line, 8, 9);
        wesosa (m < 3) {
            y <- y - 1;
        }
        sheye w <- y;
        w <- w + (y / 4);
        w <- w - (y / 100);
        w <- w + (y / 400);
        w <- w + t[m - 1];
        w <- w + d;
        w <- w drossou 7;
        wami names[w];
    }
    line <- diwela();
}
</solution>

<solution task="t2-bignum">
tosedo split(s)
    sheye out <- [];
    sheye cur <- "";
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        sheye c <- s[i];
        wesosa (c = " ") {
            wesosa (louwo(cur) > 0) {
                omse(out, cur);
                cur <- "";
            }
        } oli {
            cur <- cur + c;
        }
    }
    wesosa (louwo(cur) > 0) {
        omse(out, cur);
    }
    cha out;
bawoum tosedo

tosedo parse(s)
    sheye out <- [];
    sho (sheye i <- louwo(s) - 1; i >= 0; i <- i - 1) {
        omse(out, odresdra(s[i]));
    }
    cha out;
bawoum tosedo

tosedo add(a, b)
    sheye out <- [];
    sheye carry <- 0;
    sheye n <- louwo(a);
    wesosa (louwo(b) > n) {
        n <- louwo(b);
    }
    sho (sheye i <- 0; i < n; i <- i + 1) {
        sheye s <- carry;
        wesosa (i < louwo(a)) {
            s <- s + a[i];
        }
        wesosa (i < louwo(b)) {
            s <- s + b[i];
        }
        omse(out, s drossou 10);
        carry <- s / 10;
    }
    wesosa (carry > 0) {
        omse(out, carry);
    }
    cha out;
bawoum tosedo

tosedo mul(a, b)
    sheye res <- [];
    sheye total <- louwo(a) + louwo(b);
    sho (sheye i <- 0; i < total; i <- i + 1) {
        omse(res, 0);
    }
    sho (i <- 0; i < louwo(a); i <- i + 1) {
        sho (sheye j <- 0; j < louwo(b); j <- j + 1) {
            res[i + j] <- res[i + j] + (a[i] * b[j]);
        }
    }
    sheye carry <- 0;
    sho (i <- 0; i < louwo(res); i <- i + 1) {
        sheye v <- res[i] + carry;
        res[i] <- v drossou 10;
        carry <- v / 10;
    }
    cha res;
bawoum tosedo

tosedo toStr(d)
    sheye top <- louwo(d) - 1;
    veshim (top > 0) {
        wesosa (d[top] <> 0) {
            bou;
        }
        top <- top - 1;
    }
    sheye s <- "";
    sho (sheye i <- top; i >= 0; i <- i - 1) {
        s <- s + d[i];
    }
    cha s;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye toks <- split(line);
    wesosa (louwo(toks) >= 2) {
        sheye a <- parse(toks[0]);
        sheye b <- parse(toks[1]);
        wami (toStr(add(a, b)) + " ") + toStr(mul(a, b));
    }
    line <- diwela();
}
</solution>

<solution task="t2-life">
sheye g <- odresdra(diwela());
sheye rows <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(line) > 0) {
        omse(rows, line);
    }
    line <- diwela();
}
sheye h <- louwo(rows);
wesosa (h = 0) {
    cha;
}
sheye w <- louwo(rows[0]);
sheye w2 <- w + 2;
sheye h2 <- h + 2;
sheye size <- h2 * w2;
sheye cells <- [];
sho (sheye i <- 0; i < size; i <- i + 1) {
    omse(cells, 0);
}
sho (sheye r <- 0; r < h; r <- r + 1) {
    sheye row <- rows[r];
    sho (sheye c <- 0; c < w; c <- c + 1) {
        wesosa (row[c] = "#") {
            cells[((r + 1) * w2) + (c + 1)] <- 1;
        }
    }
}
sheye offs <- [-w2 - 1, -w2, -w2 + 1, -1, 1, w2 - 1, w2, w2 + 1];
sho (sheye gen <- 0; gen < g; gen <- gen + 1) {
    sheye nxt <- [];
    sho (i <- 0; i < size; i <- i + 1) {
        omse(nxt, 0);
    }
    sho (r <- 1; r <= h; r <- r + 1) {
        sho (c <- 1; c <= w; c <- c + 1) {
            sheye idx <- (r * w2) + c;
            sheye cnt <- 0;
            sho (sheye k <- 0; k < 8; k <- k + 1) {
                cnt <- cnt + cells[idx + offs[k]];
            }
            wesosa (cells[idx] = 1) {
                wesosa ((cnt = 2) emsoulve (cnt = 3)) {
                    nxt[idx] <- 1;
                }
            } oli {
                wesosa (cnt = 3) {
                    nxt[idx] <- 1;
                }
            }
        }
    }
    cells <- nxt;
}
sho (r <- 1; r <= h; r <- r + 1) {
    sheye s <- "";
    sho (c <- 1; c <= w; c <- c + 1) {
        wesosa (cells[(r * w2) + c] = 1) {
            s <- s + "#";
        } oli {
            s <- s + ".";
        }
    }
    wami s;
}
</solution>

<solution task="t2-rpn">
tosedo split(s)
    sheye out <- [];
    sheye cur <- "";
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        sheye c <- s[i];
        wesosa (c = " ") {
            wesosa (louwo(cur) > 0) {
                omse(out, cur);
                cur <- "";
            }
        } oli {
            cur <- cur + c;
        }
    }
    wesosa (louwo(cur) > 0) {
        omse(out, cur);
    }
    cha out;
bawoum tosedo

tosedo isOp(t)
    moumare amdre t
    amdre "+", "-", "*", "/", "%"
        cha shilsa;
    bawoum moumare
    cha ishe;
bawoum tosedo

tosedo isInt(t)
    sheye start <- 0;
    wesosa (t[0] = "-") {
        start <- 1;
    }
    wesosa (start >= louwo(t)) {
        cha ishe;
    }
    sho (sheye i <- start; i < louwo(t); i <- i + 1) {
        sheye c <- t[i];
        wesosa ((c < "0") emsoulve (c > "9")) {
            cha ishe;
        }
    }
    cha shilsa;
bawoum tosedo

tosedo tdiv(a, b)
    sheye q <- a / b;
    wesosa ((q * b) <> a) {
        wesosa ((a < 0) <> (b < 0)) {
            q <- q + 1;
        }
    }
    cha q;
bawoum tosedo

tosedo evalLine(line)
    sheye toks <- split(line);
    wesosa (louwo(toks) = 0) {
        cha "error";
    }
    sheye st <- [];
    sheye sp <- 0;
    sho (sheye i <- 0; i < louwo(toks); i <- i + 1) {
        sheye t <- toks[i];
        sheye v <- 0;
        wesosa (isOp(t)) {
            wesosa (sp < 2) {
                cha "error";
            }
            sheye b <- st[sp - 1];
            sheye a <- st[sp - 2];
            sp <- sp - 2;
            moumare amdre t
            amdre "+"
                v <- a + b;
            amdre "-"
                v <- a - b;
            amdre "*"
                v <- a * b;
            amdre "/"
                wesosa (b = 0) {
                    cha "error";
                }
                v <- tdiv(a, b);
            amdre "%"
                wesosa (b = 0) {
                    cha "error";
                }
                v <- a - (b * tdiv(a, b));
            bawoum moumare
        } oli wesosa (isInt(t)) {
            v <- odresdra(t);
        } oli {
            cha "error";
        }
        wesosa (sp < louwo(st)) {
            st[sp] <- v;
        } oli {
            omse(st, v);
        }
        sp <- sp + 1;
    }
    wesosa (sp <> 1) {
        cha "error";
    }
    cha ramou(st[0]);
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wami evalLine(line);
    line <- diwela();
}
</solution>

<solution task="t2-wordfreq">
tosedo lowerChar(c)
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sheye lo <- "abcdefghijklmnopqrstuvwxyz";
    sho (sheye i <- 0; i < 26; i <- i + 1) {
        wesosa (up[i] = c) {
            cha lo[i];
        }
    }
    cha c;
bawoum tosedo

tosedo less(x, y, mode)
    wesosa (mode = 1) {
        cha x < y;
    }
    sheye cx <- x[1];
    sheye cy <- y[1];
    wesosa (cx <> cy) {
        cha cx > cy;
    }
    sheye wx <- x[0];
    sheye wy <- y[0];
    cha wx < wy;
bawoum tosedo

tosedo msort(xs, mode)
    sheye n <- louwo(xs);
    wesosa (n <= 1) {
        cha xs;
    }
    sheye mid <- n / 2;
    sheye left <- [];
    sheye right <- [];
    sho (sheye i <- 0; i < n; i <- i + 1) {
        wesosa (i < mid) {
            omse(left, xs[i]);
        } oli {
            omse(right, xs[i]);
        }
    }
    left <- msort(left, mode);
    right <- msort(right, mode);
    sheye out <- [];
    i <- 0;
    sheye j <- 0;
    sheye ln <- louwo(left);
    sheye rn <- louwo(right);
    veshim ((i < ln) dilisyo (j < rn)) {
        wesosa (less(right[j], left[i], mode)) {
            omse(out, right[j]);
            j <- j + 1;
        } oli {
            omse(out, left[i]);
            i <- i + 1;
        }
    }
    veshim (i < ln) {
        omse(out, left[i]);
        i <- i + 1;
    }
    veshim (j < rn) {
        omse(out, right[j]);
        j <- j + 1;
    }
    cha out;
bawoum tosedo

sheye words <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye cur <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- line[i];
        wesosa ((c >= "a") dilisyo (c <= "z")) {
            cur <- cur + c;
        } oli wesosa ((c >= "A") dilisyo (c <= "Z")) {
            cur <- cur + lowerChar(c);
        } oli {
            wesosa (louwo(cur) > 0) {
                omse(words, cur);
                cur <- "";
            }
        }
    }
    wesosa (louwo(cur) > 0) {
        omse(words, cur);
    }
    line <- diwela();
}
sheye sorted <- msort(words, 1);
sheye pairs <- [];
sheye n <- louwo(sorted);
sheye k <- 0;
veshim (k < n) {
    sheye w <- sorted[k];
    sheye cnt <- 0;
    veshim (k < n) {
        wesosa (sorted[k] <> w) {
            bou;
        }
        cnt <- cnt + 1;
        k <- k + 1;
    }
    omse(pairs, [w, cnt]);
}
sheye ps <- msort(pairs, 2);
sheye lim <- louwo(ps);
wesosa (lim > 10) {
    lim <- 10;
}
sho (sheye q <- 0; q < lim; q <- q + 1) {
    sheye p <- ps[q];
    wami (p[0] + " ") + p[1];
}
</solution>