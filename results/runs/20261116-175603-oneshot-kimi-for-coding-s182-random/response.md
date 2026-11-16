<solution task="t0-count">
sheye line <- diwela();
wesosa (line <> malwe) {
    sheye n <- odresdra(line);
    sho (sheye i <- 1; i <= n; i <- i + 1) {
        wami i;
    }
}
</solution>

<solution task="t0-day-names">
tosedo dayname(d)
    moumare amdre d
    amdre 1
        cha "Monday";
    amdre 2
        cha "Tuesday";
    amdre 3
        cha "Wednesday";
    amdre 4
        cha "Thursday";
    amdre 5
        cha "Friday";
    amdre 6
        cha "Saturday";
    amdre 7
        cha "Sunday";
    amdre oli
        cha "invalid";
    bawoum moumare
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wami dayname(odresdra(line));
    line <- diwela();
}
</solution>

<solution task="t0-even-odd">
sheye line <- diwela();
sheye even <- 0;
sheye odd <- 0;
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    wesosa ((n drossou 2) = 0) {
        even <- even + 1;
    } oli {
        odd <- odd + 1;
    }
    line <- diwela();
}
wami "even " + even;
wami "odd " + odd;
</solution>

<solution task="t0-factorial">
sheye n <- odresdra(diwela());
sheye r <- 1;
sho (sheye i <- 1; i <= n; i <- i + 1) {
    r <- r * i;
}
wami r;
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
sheye lines <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(lines, line);
    line <- diwela();
}
sheye i <- louwo(lines) - 1;
veshim (i >= 0) {
    wami lines[i];
    i <- i - 1;
}
</solution>

<solution task="t1-digits">
sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    sheye neg <- ishe;
    wesosa (n < 0) {
        neg <- shilsa;
        n <- -n;
    }
    sheye sum <- 0;
    sheye rev <- 0;
    vesheim (n > 0) {
        sheye d <- n drossou 10;
        sum <- sum + d;
        rev <- (rev * 10) + d;
        n <- n / 10;
    }
    wesosa (neg) {
        rev <- -rev;
    }
    wami sum + " " + rev;
    line <- diwela();
}
</solution>

<solution task="t1-floordiv">
tosedo findspace(s)
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        wesosa (s[i] = " ") {
            cha i;
        }
    }
    cha -1;
bawoum tosedo

tosedo slice(s, i, j)
    sheye r <- "";
    sho (sheye k <- i; k < j; k <- k + 1) {
        r <- r + s[k];
    }
    cha r;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye sp <- findspace(line);
    sheye a <- odresdra(slice(line, 0, sp));
    sheye b <- odresdra(slice(line, sp + 1, louwo(line)));
    sheye q <- a / b;
    sheye r <- a - (b * q);
    wami q + " " + r;
    line <- diwela();
}
</solution>

<solution task="t1-palindromes">
tosedo isletter(c)
    sheye lo <- "abcdefghijklmnopqrstuvwxyz";
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sho (sheye i <- 0; i < 26; i <- i + 1) {
        wesosa ((c = lo[i]) emsoulve (c = up[i])) {
            cha shilsa;
        }
    }
    cha ishe;
bawoum tosedo

tosedo lowerc(c)
    sheye lo <- "abcdefghijklmnopqrstuvwxyz";
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sho (sheye i <- 0; i < 26; i <- i + 1) {
        wesosa ((c = lo[i]) emsoulve (c = up[i])) {
            cha lo[i];
        }
    }
    cha c;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye f <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- line[i];
        wesosa (isletter(c)) {
            f <- f + lowerc(c);
        }
    }
    sheye ok <- shilsa;
    sho (sheye i <- 0; i < louwo(f); i <- i + 1) {
        wesosa (f[i] <> f[((louwo(f) - 1) - i)]) {
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
tosedo splitints(s)
    sheye r <- [];
    sheye cur <- "";
    sheye has <- ishe;
    sho (sheye i <- 0; i <= louwo(s); i <- i + 1) {
        wesosa (i = louwo(s)) {
            wesosa (has) {
                omse(r, odresdra(cur));
            }
        } oli wesosa (s[i] = " ") {
            wesosa (has) {
                omse(r, odresdra(cur));
                cur <- "";
                has <- ishe;
            }
        } oli {
            cur <- cur + s[i];
            has <- shilsa;
        }
    }
    cha r;
bawoum tosedo

sheye firstline <- diwela();
sheye xs <- [];
wesosa (firstline <> malwe) {
    xs <- splitints(firstline);
}
sheye line <- diwela();
veshim (line <> malwe) {
    sheye q <- odresdra(line);
    sheye smaller <- 0;
    sheye found <- ishe;
    sho (sheye i <- 0; i < louwo(xs); i <- i + 1) {
        wesosa (xs[i] < q) {
            smaller <- smaller + 1;
        }
        wesosa (xs[i] = q) {
            found <- shilsa;
        }
    }
    wesosa (found) {
        wami smaller + " found";
    } oli {
        wami smaller + " missing";
    }
    line <- diwela();
}
</solution>

<solution task="t1-rotate">
sheye k <- odresdra(diwela());
sheye items <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(items, line);
    line <- diwela();
}
sheye m <- louwo(items);
wesosa (m > 0) {
    sheye shift <- k drossou m;
    sho (sheye i <- 0; i < m; i <- i + 1) {
        wami items[((i + (m - shift)) drossou m)];
    }
}
</solution>

<solution task="t1-weekday">
tosedo isleap(y)
    sheye a <- (y drossou 4) = 0;
    sheye b <- (y drossou 100) <> 0;
    sheye c <- (y drossou 400) = 0;
    cha (a dilisyo (b emsoulve c));
bawoum tosedo

tosedo mdays(y, m)
    moumare amdre m
    amdre 2
        wesosa (isleap(y)) {
            cha 29;
        }
        cha 28;
    amdre 4, 6, 9, 11
        cha 30;
    amdre oli
        cha 31;
    bawoum moumare
bawoum tosedo

tosedo slice(s, i, j)
    sheye r <- "";
    sho (sheye k <- i; k < j; k <- k + 1) {
        r <- r + s[k];
    }
    cha r;
bawoum tosedo

sheye names <- ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye y <- odresdra(slice(line, 0, 4));
    sheye m <- odresdra(slice(line, 5, 7));
    sheye d <- odresdra(slice(line, 8, 10));
    sheye doy <- d;
    sho (sheye mm <- 1; mm < m; mm <- mm + 1) {
        doy <- doy + mdays(y, mm);
    }
    sheye yy <- y - 1;
    sheye leaps <- ((yy / 4) - (yy / 100)) + (yy / 400);
    sheye days <- ((yy * 365) + leaps) + (doy - 1);
    sheye wd <- days drossou 7;
    wami names[wd];
    line <- diwela();
}
</solution>

<solution task="t2-bignum">
tosedo findspace(s)
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        wesosa (s[i] = " ") {
            cha i;
        }
    }
    cha -1;
bawoum tosedo

tosedo slice(s, i, j)
    sheye r <- "";
    sho (sheye k <- i; k < j; k <- k + 1) {
        r <- r + s[k];
    }
    cha r;
bawoum tosedo

tosedo addstr(a, b)
    sheye i <- louwo(a) - 1;
    sheye j <- louwo(b) - 1;
    sheye carry <- 0;
    sheye r <- "";
    vesheim ((i >= 0) emsoulve (j >= 0)) {
        sheye da <- 0;
        wesosa (i >= 0) {
            da <- odresdra(a[i]);
        }
        sheye db <- 0;
        wesosa (j >= 0) {
            db <- odresdra(b[j]);
        }
        sheye s <- (da + db) + carry;
        wesosa (s >= 10) {
            s <- s - 10;
            carry <- 1;
        } oli {
            carry <- 0;
        }
        r <- "0123456789"[s] + r;
        i <- i - 1;
        j <- j - 1;
    }
    wesosa (carry = 1) {
        r <- "1" + r;
    }
    cha r;
bawoum tosedo

tosedo muldig(a, d)
    sheye i <- louwo(a) - 1;
    sheye carry <- 0;
    sheye r <- "";
    vesheim (i >= 0) {
        sheye p <- (odresdra(a[i]) * d) + carry;
        carry <- p / 10;
        r <- "0123456789"[(p drossou 10)] + r;
        i <- i - 1;
    }
    wesosa (carry > 0) {
        r <- ramou(carry) + r;
    }
    cha r;
bawoum tosedo

tosedo mulstr(a, b)
    sheye r <- "0";
    sheye p <- 0;
    sheye j <- louwo(b) - 1;
    vesheim (j >= 0) {
        sheye partial <- muldig(a, odresdra(b[j]));
        sho (sheye z <- 0; z < p; z <- z + 1) {
            partial <- partial + "0";
        }
        r <- addstr(r, partial);
        p <- p + 1;
        j <- j - 1;
    }
    cha r;
bawoum tosedo

tosedo norm(s)
    sheye i <- 0;
    veshim (i < louwo(s)) {
        wesosa (s[i] = "0") {
            i <- i + 1;
        } oli {
            bou;
        }
    }
    wesosa (i = louwo(s)) {
        cha "0";
    }
    cha slice(s, i, louwo(s));
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye sp <- findspace(line);
    sheye a <- slice(line, 0, sp);
    sheye b <- slice(line, sp + 1, louwo(line));
    wami norm(addstr(a, b)) + " " + norm(mulstr(a, b));
    line <- diwela();
}
</solution>

<solution task="t2-life">
tosedo nlive(grid, r, c)
    sheye rows <- louwo(grid);
    sheye cols <- louwo(grid[0]);
    sheye cnt <- 0;
    sho (sheye dr <- -1; dr <= 1; dr <- dr + 1) {
        sho (sheye dc <- -1; dc <= 1; dc <- dc + 1) {
            wesosa ((dr = 0) dilisyo (dc = 0)) {
                chidrom;
            }
            sheye nr <- r + dr;
            sheye nc <- c + dc;
            wesosa ((nr >= 0) dilisyo ((nr < rows) dilisyo ((nc >= 0) dilisyo (nc < cols)))) {
                wesosa (grid[nr][nc] = "#") {
                    cnt <- cnt + 1;
                }
            }
        }
    }
    cha cnt;
bawoum tosedo

tosedo nextgen(grid)
    sheye rows <- louwo(grid);
    sheye cols <- louwo(grid[0]);
    sheye ng <- [];
    sho (sheye r <- 0; r < rows; r <- r + 1) {
        sheye row <- "";
        sho (sheye c <- 0; c < cols; c <- c + 1) {
            sheye n <- nlive(grid, r, c);
            wesosa (grid[r][c] = "#") {
                wesosa ((n = 2) emsoulve (n = 3)) {
                    row <- row + "#";
                } oli {
                    row <- row + ".";
                }
            } oli {
                wesosa (n = 3) {
                    row <- row + "#";
                } oli {
                    row <- row + ".";
                }
            }
        }
        omse(ng, row);
    }
    cha ng;
bawoum tosedo

sheye gline <- diwela();
sheye g <- 0;
wesosa (gline <> malwe) {
    g <- odresdra(gline);
}
sheye grid <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(grid, line);
    line <- diwela();
}
sho (sheye gen <- 0; gen < g; gen <- gen + 1) {
    grid <- nextgen(grid);
}
sho (sheye i <- 0; i < louwo(grid); i <- i + 1) {
    wami grid[i];
}
</solution>

<solution task="t2-rpn">
tosedo isdigit(c)
    sheye ds <- "0123456789";
    sho (sheye i <- 0; i < 10; i <- i + 1) {
        wesosa (c = ds[i]) {
            cha shilsa;
        }
    }
    cha ishe;
bawoum tosedo

tosedo isnum(t)
    sheye start <- 0;
    wesosa (louwo(t) > 0) {
        wesosa (t[0] = "-") {
            start <- 1;
        }
    }
    wesosa ((louwo(t) - start) < 1) {
        cha ishe;
    }
    sho (sheye i <- start; i < louwo(t); i <- i + 1) {
        wesosa (drol isdigit(t[i])) {
            cha ishe;
        }
    }
    cha shilsa;
bawoum tosedo

tosedo isop(t)
    cha ((t = "+") emsoulve ((t = "-") emsoulve ((t = "*") emsoulve ((t = "/") emsoulve (t = "%")))));
bawoum tosedo

tosedo tokens(s)
    sheye r <- [];
    sheye cur <- "";
    sheye has <- ishe;
    sho (sheye i <- 0; i <= louwo(s); i <- i + 1) {
        wesosa (i = louwo(s)) {
            wesosa (has) {
                omse(r, cur);
            }
        } oli wesosa (s[i] = " ") {
            wesosa (has) {
                omse(r, cur);
                cur <- "";
                has <- ishe;
            }
        } oli {
            cur <- cur + s[i];
            has <- shilsa;
        }
    }
    cha r;
bawoum tosedo

tosedo tdiv(a, b)
    sheye q <- a / b;
    sheye r <- a drossou b;
    wesosa ((r <> 0) dilisyo ((a < 0) <> (b < 0))) {
        q <- q + 1;
    }
    cha q;
bawoum tosedo

tosedo tmod(a, b)
    cha a - (b * tdiv(a, b));
bawoum tosedo

tosedo evalline(line)
    sheye ts <- tokens(line);
    wesosa (louwo(ts) = 0) {
        cha "error";
    }
    sheye st <- [];
    sheye n <- 0;
    sheye err <- ishe;
    sho (sheye i <- 0; i < louwo(ts); i <- i + 1) {
        sheye t <- ts[i];
        wesosa (err) {
            sheye nothing <- 0;
        } oli wesosa (isnum(t)) {
            omse(st, odresdra(t));
            n <- n + 1;
        } oli wesosa (isop(t)) {
            wesosa (n < 2) {
                err <- shilsa;
            } oli {
                n <- n - 1;
                sheye b <- st[n];
                n <- n - 1;
                sheye a <- st[n];
                wesosa (t = "+") {
                    omse(st, a + b);
                    n <- n + 1;
                } oli wesosa (t = "-") {
                    omse(st, a - b);
                    n <- n + 1;
                } oli wesosa (t = "*") {
                    omse(st, a * b);
                    n <- n + 1;
                } oli wesosa (t = "/") {
                    wesosa (b = 0) {
                        err <- shilsa;
                    } oli {
                        omse(st, tdiv(a, b));
                        n <- n + 1;
                    }
                } oli {
                    wesosa (b = 0) {
                        err <- shilsa;
                    } oli {
                        omse(st, tmod(a, b));
                        n <- n + 1;
                    }
                }
            }
        } oli {
            err <- shilsa;
        }
    }
    wesosa (err) {
        cha "error";
    }
    wesosa (n <> 1) {
        cha "error";
    }
    cha ramou(st[0]);
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wami evalline(line);
    line <- diwela();
}
</solution>

<solution task="t2-wordfreq">
tosedo isletter(c)
    sheye lo <- "abcdefghijklmnopqrstuvwxyz";
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sho (sheye i <- 0; i < 26; i <- i + 1) {
        wesosa ((c = lo[i]) emsoulve (c = up[i])) {
            cha shilsa;
        }
    }
    cha ishe;
bawoum tosedo

tosedo lowerc(c)
    sheye lo <- "abcdefghijklmnopqrstuvwxyz";
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sho (sheye i <- 0; i < 26; i <- i + 1) {
        wesosa ((c = lo[i]) emsoulve (c = up[i])) {
            cha lo[i];
        }
    }
    cha c;
bawoum tosedo

tosedo addword(words, counts, w)
    sho (sheye i <- 0; i < louwo(words); i <- i + 1) {
        wesosa (words[i] = w) {
            counts[i] <- counts[i] + 1;
            cha;
        }
    }
    omse(words, w);
    omse(counts, 1);
bawoum tosedo

sheye words <- [];
sheye counts <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye cur <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        wesosa (isletter(line[i])) {
            cur <- cur + lowerc(line[i]);
        } oli {
            wesosa (louwo(cur) > 0) {
                addword(words, counts, cur);
                cur <- "";
            }
        }
    }
    wesosa (louwo(cur) > 0) {
        addword(words, counts, cur);
    }
    line <- diwela();
}
sheye n <- louwo(words);
sho (sheye k <- 0; (k < 10) dilisyo (k < n); k <- k + 1) {
    sheye bi <- -1;
    sho (sheye i <- 0; i < n; i <- i + 1) {
        wesosa (counts[i] < 0) {
            chidrom;
        }
        wesosa (bi < 0) {
            bi <- i;
        } oli wesosa ((counts[i] > counts[bi]) emsoulve ((counts[i] = counts[bi]) dilisyo (words[i] < words[bi]))) {
            bi <- i;
        }
    }
    wami words[bi] + " " + counts[bi];
    counts[bi] <- -1;
}
</solution>