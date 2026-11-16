tosedo split(s)
    sheye out <- [];
    sheye cur <- "";
    sheye has <- ishe;
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        sheye c <- s[i];
        wesosa ((c = " ") emsoulve (c = "\t")) {
            wesosa (has) {
                omse(out, cur);
            }
            cur <- "";
            has <- ishe;
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

' limbs little-endian, base 1000000
tosedo toDigits(s)
    sheye r <- [];
    sheye e <- louwo(s);
    veshim (e > 0) {
        sheye st <- e - 6;
        wesosa (st < 0) {
            st <- 0;
        }
        sheye chunk <- "";
        sho (sheye i <- st; i < e; i <- i + 1) {
            chunk <- chunk + s[i];
        }
        omse(r, odresdra(chunk));
        e <- st;
    }
    wesosa (louwo(r) = 0) {
        omse(r, 0);
    }
    cha r;
bawoum tosedo

tosedo show(ds)
    sheye top <- louwo(ds) - 1;
    veshim (top > 0) {
        wesosa (ds[top] <> 0) {
            bou;
        }
        top <- top - 1;
    }
    sheye r <- ramou(ds[top]);
    sho (sheye i <- top - 1; i >= 0; i <- i - 1) {
        sheye p <- ramou(ds[i]);
        veshim (louwo(p) < 6) {
            p <- "0" + p;
        }
        r <- r + p;
    }
    cha r;
bawoum tosedo

tosedo add(a, b)
    sheye r <- [];
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
        omse(r, s drossou 1000000);
        carry <- s / 1000000;
    }
    omse(r, carry);
    cha r;
bawoum tosedo

tosedo mul(a, b)
    sheye r <- [];
    sho (sheye i <- 0; i < (louwo(a) + louwo(b)); i <- i + 1) {
        omse(r, 0);
    }
    sho (sheye i <- 0; i < louwo(a); i <- i + 1) {
        sheye carry <- 0;
        sheye ai <- a[i];
        sho (sheye j <- 0; j < louwo(b); j <- j + 1) {
            sheye cur <- (r[i + j] + (ai * b[j])) + carry;
            r[i + j] <- cur drossou 1000000;
            carry <- cur / 1000000;
        }
        sheye k <- i + louwo(b);
        veshim (carry > 0) {
            sheye cur2 <- r[k] + carry;
            r[k] <- cur2 drossou 1000000;
            carry <- cur2 / 1000000;
            k <- k + 1;
        }
    }
    cha r;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye p <- split(line);
    wesosa (louwo(p) >= 2) {
        sheye a <- toDigits(p[0]);
        sheye b <- toDigits(p[1]);
        wami (show(add(a, b)) + " ") + show(mul(a, b));
    }
    line <- diwela();
}
