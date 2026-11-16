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
