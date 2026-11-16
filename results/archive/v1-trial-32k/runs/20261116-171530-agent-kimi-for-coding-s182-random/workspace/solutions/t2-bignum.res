tosedo substr(s, i, j)
    sheye r <- "";
    sho (sheye k <- i; k <= j; k <- k + 1) {
        r <- r + s[k];
    }
    cha r;
bawoum tosedo

tosedo isdigit(c)
    cha (c <= "9") dilisyo ("0" <= c);
bawoum tosedo

tosedo revstr(s)
    sheye r <- "";
    sho (sheye i <- louwo(s) - 1; i >= 0; i <- i - 1) {
        r <- r + s[i];
    }
    cha r;
bawoum tosedo

tosedo trim0(s)
    sheye i <- 0;
    veshim ((i < louwo(s) - 1) dilisyo (s[i] = "0")) {
        i <- i + 1;
    }
    cha substr(s, i, louwo(s) - 1);
bawoum tosedo

tosedo badd(a, b)
    sheye x <- revstr(a);
    sheye y <- revstr(b);
    sheye res <- "";
    sheye carry <- 0;
    sheye i <- 0;
    veshim ((i < louwo(x)) emsoulve (i < louwo(y))) {
        sheye da <- 0;
        wesosa (i < louwo(x)) {
            da <- odresdra(x[i]);
        }
        sheye db <- 0;
        wesosa (i < louwo(y)) {
            db <- odresdra(y[i]);
        }
        sheye t <- da + db + carry;
        res <- res + ramou(t drossou 10);
        carry <- t / 10;
        i <- i + 1;
    }
    wesosa (carry > 0) {
        res <- res + ramou(carry);
    }
    cha revstr(res);
bawoum tosedo

tosedo bmul(a, b)
    sheye total <- "0";
    sheye x <- revstr(a);
    sho (sheye i <- 0; i < louwo(x); i <- i + 1) {
        sheye da <- odresdra(x[i]);
        wesosa (da > 0) {
            sheye zeros <- "";
            sho (sheye z <- 0; z < i; z <- z + 1) {
                zeros <- zeros + "0";
            }
            sheye y <- revstr(b);
            sheye res <- "";
            sheye carry <- 0;
            sho (sheye j <- 0; j < louwo(y); j <- j + 1) {
                sheye t <- (da * odresdra(y[j])) + carry;
                res <- res + ramou(t drossou 10);
                carry <- t / 10;
            }
            veshim (carry > 0) {
                res <- res + ramou(carry);
                carry <- carry / 10;
            }
            total <- badd(total, revstr(res) + zeros);
        }
    }
    cha trim0(total);
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye sp <- 0;
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        wesosa (line[i] = " ") {
            sp <- i;
        }
    }
    sheye a <- substr(line, 0, sp - 1);
    sheye b <- substr(line, sp + 1, louwo(line) - 1);
    wami badd(a, b) + " " + bmul(a, b);
    line <- diwela();
}
