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
