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
        sheye n <- odresdra(line);
        moumare amdre n
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
            sheye d <- m drossou 10;
            s <- s + d;
            r <- (r * 10) + d;
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
    sheye res <- [];
    sheye cur <- "";
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        sheye c <- s[i];
        wesosa (c = " ") {
            wesosa (louwo(cur) > 0) {
                omse(res, cur);
                cur <- "";
            }
        } oli {
            cur <- cur + c;
        }
    }
    wesosa (louwo(cur) > 0) {
        omse(res, cur);
    }
    cha res;
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
tosedo lowerOf(c)
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sheye lw <- "abcdefghijklmnopqrstuvwxyz";
    sho (sheye k <- 0; k < 26; k <- k + 1) {
        wesosa (up[k] = c) {
            cha lw[k];
        }
    }
    cha c;
bawoum tosedo

tosedo isPal(s)
    sheye cs <- [];
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        sheye c <- s[i];
        wesosa ((c >= "a") dilisyo (c <= "z")) {
            omse(cs, c);
        } oli wesosa ((c >= "A") dilisyo (c <= "Z")) {
            omse(cs, lowerOf(c));
        } oli wesosa ((c >= "0") dilisyo (c <= "9")) {
            omse(cs, c);
        }
    }
    sheye n <- louwo(cs);
    sho (sheye j <- 0; j < (n / 2); j <- j + 1) {
        wesosa (cs[j] <> cs[(n - 1) - j]) {
            cha ishe;
        }
    }
    cha shilsa;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (isPal(line)) {
        wami "yes";
    } oli {
        wami "no";
    }
    line <- diwela();
}
</solution>

<solution task="t1-rank">
tosedo split(s)
    sheye res <- [];
    sheye cur <- "";
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        sheye c <- s[i];
        wesosa (c = " ") {
            wesosa (louwo(cur) > 0) {
                omse(res, cur);
                cur <- "";
            }
        } oli {
            cur <- cur + c;
        }
    }
    wesosa (louwo(cur) > 0) {
        omse(res, cur);
    }
    cha res;
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
        sheye found <- ishe;
        wesosa (lo < n) {
            wesosa (arr[lo] = q) {
                found <- shilsa;
            }
        }
        wesosa (found) {
            wami ramou(lo) + " found";
        } oli {
            wami ramou(lo) + " missing";
        }
    }
    line <- diwela();
}
</solution>

<solution task="t1-rotate">
sheye k <- odresdra(diwela());
sheye xs <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(xs, line);
    line <- diwela();
}
sheye n <- louwo(xs);
wesosa (n > 0) {
    sheye s <- k drossou n;
    sho (sheye i <- 0; i < n; i <- i + 1) {
        wami xs[(i - s) drossou n];
    }
}
</solution>

<solution task="t1-weekday">
tosedo num(s, st, len)
    sheye v <- 0;
    sho (sheye i <- st; i < (st + len); i <- i + 1) {
        v <- (v * 10) + odresdra(s[i]);
    }
    cha v;
bawoum tosedo

sheye t <- [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
sheye names <- ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(line) >= 10) {
        sheye y <- num(line, 0, 4);
        sheye m <- num(line, 5, 2);
        sheye d <- num(line, 8, 2);
        wesosa (m < 3) {
            y <- y - 1;
        }
        sheye w <- y + (y / 4);
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
    sheye res <- [];
    sheye cur <- "";
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        sheye c <- s[i];
        wesosa (c = " ") {
            wesosa (louwo(cur) > 0) {
                omse(res, cur);
                cur <- "";
            }
        } oli {
            cur <- cur + c;
        }
    }
    wesosa (louwo(cur) > 0) {
        omse(res, cur);
    }
    cha res;
bawoum tosedo

tosedo parse(s)
    sheye r <- [];
    sho (sheye i <- louwo(s) - 1; i >= 0; i <- i - 1) {
        omse(r, odresdra(s[i]));
    }
    cha r;
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
        s <- s + ramou(d[i]);
    }
    cha s;
bawoum tosedo

tosedo add(a, b)
    sheye n <- louwo(a);
    wesosa (louwo(b) > n) {
        n <- louwo(b);
    }
    sheye r <- [];
    sheye carry <- 0;
    sho (sheye i <- 0; i < n; i <- i + 1) {
        sheye v <- carry;
        wesosa (i < louwo(a)) {
            v <- v + a[i];
        }
        wesosa (i < louwo(b)) {
            v <- v + b[i];
        }
        omse(r, v drossou 10);
        carry <- v / 10;
    }
    omse(r, carry);
    cha r;
bawoum tosedo

tosedo mul(a, b)
    sheye r <- [];
    sheye total <- louwo(a) + louwo(b);
    sho (sheye i <- 0; i < total; i <- i + 1) {
        omse(r, 0);
    }
    sho (sheye i <- 0; i < louwo(a); i <- i + 1) {
        sho (sheye j <- 0; j < louwo(b); j <- j + 1) {
            r[i + j] <- r[i + j] + (a[i] * b[j]);
        }
    }
    sheye carry <- 0;
    sho (sheye k <- 0; k < louwo(r); k <- k + 1) {
        sheye v <- r[k] + carry;
        r[k] <- v drossou 10;
        carry <- v / 10;
    }
    cha r;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye t <- split(line);
    wesosa (louwo(t) >= 2) {
        sheye a <- parse(t[0]);
        sheye b <- parse(t[1]);
        wami (toStr(add(a, b)) + " ") + toStr(mul(a, b));
    }
    line <- diwela();
}
</solution>

<solution task="t2-life">
tosedo cell(g, r, c, R, C)
    wesosa (r < 0) {
        cha 0;
    }
    wesosa (r >= R) {
        cha 0;
    }
    wesosa (c < 0) {
        cha 0;
    }
    wesosa (c >= C) {
        cha 0;
    }
    sheye row <- g[r];
    cha row[c];
bawoum tosedo

sheye gens <- odresdra(diwela());
sheye grid <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(line) > 0) {
        sheye row <- [];
        sho (sheye j <- 0; j < louwo(line); j <- j + 1) {
            wesosa (line[j] = "#") {
                omse(row, 1);
            } oli {
                omse(row, 0);
            }
        }
        omse(grid, row);
    }
    line <- diwela();
}
sheye R <- louwo(grid);
sheye C <- 0;
wesosa (R > 0) {
    C <- louwo(grid[0]);
}
sho (sheye t <- 0; t < gens; t <- t + 1) {
    sheye ng <- [];
    sho (sheye r <- 0; r < R; r <- r + 1) {
        sheye nrow <- [];
        sheye cur <- grid[r];
        sho (sheye c <- 0; c < C; c <- c + 1) {
            sheye cnt <- 0;
            sho (sheye dr <- -1; dr <= 1; dr <- dr + 1) {
                sho (sheye dc <- -1; dc <= 1; dc <- dc + 1) {
                    wesosa ((dr <> 0) emsoulve (dc <> 0)) {
                        cnt <- cnt + cell(grid, r + dr, c + dc, R, C);
                    }
                }
            }
            sheye alive <- cur[c];
            wesosa (alive = 1) {
                wesosa ((cnt = 2) emsoulve (cnt = 3)) {
                    omse(nrow, 1);
                } oli {
                    omse(nrow, 0);
                }
            } oli {
                wesosa (cnt = 3) {
                    omse(nrow, 1);
                } oli {
                    omse(nrow, 0);
                }
            }
        }
        omse(ng, nrow);
    }
    grid <- ng;
}
sho (sheye r <- 0; r < R; r <- r + 1) {
    sheye row <- grid[r];
    sheye s <- "";
    sho (sheye c <- 0; c < C; c <- c + 1) {
        wesosa (row[c] = 1) {
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
    sheye res <- [];
    sheye cur <- "";
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        sheye c <- s[i];
        wesosa (c = " ") {
            wesosa (louwo(cur) > 0) {
                omse(res, cur);
                cur <- "";
            }
        } oli {
            cur <- cur + c;
        }
    }
    wesosa (louwo(cur) > 0) {
        omse(res, cur);
    }
    cha res;
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
        wesosa (c < "0") {
            cha ishe;
        }
        wesosa (c > "9") {
            cha ishe;
        }
    }
    cha shilsa;
bawoum tosedo

tosedo tdiv(a, b)
    sheye q <- a / b;
    wesosa ((a drossou b) <> 0) {
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
        sheye tok <- toks[i];
        sheye isOp <- ishe;
        sheye v <- 0;
        moumare amdre tok
        amdre "+", "-", "*", "/", "%"
            isOp <- shilsa;
        amdre oli
            isOp <- ishe;
        bawoum moumare
        wesosa (isOp) {
            wesosa (sp < 2) {
                cha "error";
            }
            sheye b <- st[sp - 1];
            sheye a <- st[sp - 2];
            sp <- sp - 2;
            wesosa (tok = "+") {
                v <- a + b;
            } oli wesosa (tok = "-") {
                v <- a - b;
            } oli wesosa (tok = "*") {
                v <- a * b;
            } oli {
                wesosa (b = 0) {
                    cha "error";
                }
                sheye q <- tdiv(a, b);
                wesosa (tok = "/") {
                    v <- q;
                } oli {
                    v <- a - (b * q);
                }
            }
        } oli {
            wesosa (isInt(tok) = ishe) {
                cha "error";
            }
            v <- odresdra(tok);
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
tosedo lowerOf(c)
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sheye lw <- "abcdefghijklmnopqrstuvwxyz";
    sho (sheye k <- 0; k < 26; k <- k + 1) {
        wesosa (up[k] = c) {
            cha lw[k];
        }
    }
    cha c;
bawoum tosedo

tosedo msort(a, lo, hi, tmp)
    wesosa ((hi - lo) < 2) {
        cha;
    }
    sheye mid <- (lo + hi) / 2;
    msort(a, lo, mid, tmp);
    msort(a, mid, hi, tmp);
    sheye i <- lo;
    sheye j <- mid;
    sheye k <- lo;
    veshim ((i < mid) dilisyo (j < hi)) {
        wesosa (a[j] < a[i]) {
            tmp[k] <- a[j];
            j <- j + 1;
        } oli {
            tmp[k] <- a[i];
            i <- i + 1;
        }
        k <- k + 1;
    }
    veshim (i < mid) {
        tmp[k] <- a[i];
        i <- i + 1;
        k <- k + 1;
    }
    veshim (j < hi) {
        tmp[k] <- a[j];
        j <- j + 1;
        k <- k + 1;
    }
    sho (k <- lo; k < hi; k <- k + 1) {
        a[k] <- tmp[k];
    }
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
            cur <- cur + lowerOf(c);
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
sheye n <- louwo(words);
sheye tmp <- [];
sho (sheye i <- 0; i < n; i <- i + 1) {
    omse(tmp, "");
}
msort(words, 0, n, tmp);
sheye W <- [];
sheye C <- [];
sho (sheye i <- 0; i < n; i <- i + 1) {
    sheye m <- louwo(W);
    wesosa (m > 0) {
        wesosa (W[m - 1] = words[i]) {
            C[m - 1] <- C[m - 1] + 1;
        } oli {
            omse(W, words[i]);
            omse(C, 1);
        }
    } oli {
        omse(W, words[i]);
        omse(C, 1);
    }
}
sheye d <- louwo(W);
sheye used <- [];
sho (sheye i <- 0; i < d; i <- i + 1) {
    omse(used, ishe);
}
sheye rounds <- 10;
wesosa (d < 10) {
    rounds <- d;
}
sho (sheye r <- 0; r < rounds; r <- r + 1) {
    sheye best <- -1;
    sheye bc <- -1;
    sho (sheye i <- 0; i < d; i <- i + 1) {
        wesosa (used[i] = ishe) {
            wesosa (C[i] > bc) {
                best <- i;
                bc <- C[i];
            }
        }
    }
    used[best] <- shilsa;
    wami (W[best] + " ") + ramou(C[best]);
}
</solution>