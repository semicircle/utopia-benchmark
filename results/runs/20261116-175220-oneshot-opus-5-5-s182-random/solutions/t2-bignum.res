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
