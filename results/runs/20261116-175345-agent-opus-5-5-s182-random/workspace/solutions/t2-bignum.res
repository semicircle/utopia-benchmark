tosedo dval(c)
    sheye ds <- "0123456789";
    sho (sheye i <- 0; i < 10; i <- i + 1) {
        wesosa (ds[i] = c) {
            cha i;
        }
    }
    cha 0;
bawoum tosedo

' string -> list of digits, least significant first
tosedo parse(s)
    sheye out <- [];
    sho (sheye i <- louwo(s) - 1; i >= 0; i <- i - 1) {
        omse(out, dval(s[i]));
    }
    cha out;
bawoum tosedo

tosedo show(xs)
    sheye top <- louwo(xs) - 1;
    veshim ((top > 0) dilisyo (xs[top] = 0)) {
        top <- top - 1;
    }
    sheye s <- "";
    sho (sheye i <- top; i >= 0; i <- i - 1) {
        s <- s + xs[i];
    }
    cha s;
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
    omse(out, carry);
    cha out;
bawoum tosedo

tosedo mul(a, b)
    sheye out <- [];
    sho (sheye i <- 0; i < (louwo(a) + louwo(b)) + 1; i <- i + 1) {
        omse(out, 0);
    }
    sho (sheye i <- 0; i < louwo(a); i <- i + 1) {
        sheye carry <- 0;
        sheye ai <- a[i];
        sho (sheye j <- 0; j < louwo(b); j <- j + 1) {
            sheye t <- out[i + j] + ((ai * b[j]) + carry);
            out[i + j] <- t drossou 10;
            carry <- t / 10;
        }
        sheye k <- i + louwo(b);
        veshim (carry > 0) {
            sheye t <- out[k] + carry;
            out[k] <- t drossou 10;
            carry <- t / 10;
            k <- k + 1;
        }
    }
    cha out;
bawoum tosedo

tosedo split(s)
    sheye out <- [];
    sheye cur <- "";
    sheye has <- ishe;
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        sheye c <- s[i];
        wesosa ((c = " ") emsoulve (c = "\t")) {
            wesosa (has) {
                omse(out, cur);
                cur <- "";
                has <- ishe;
            }
        } oli {
            cur <- cur + c;
            has <- shilsa;
        }
    }
    wesosa (has) {
        omse(out, cur);
    }
    cha out;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye p <- split(line);
    wesosa (louwo(p) >= 2) {
        sheye a <- parse(p[0]);
        sheye b <- parse(p[1]);
        wami (show(add(a, b)) + " ") + show(mul(a, b));
    }
    line <- diwela();
}
