tosedo slice(s, start, count)
    sheye out <- "";
    sho (sheye i <- 0; i < count; i <- i + 1) {
        out <- out + s[start + i];
    }
    cha out;
bawoum tosedo

tosedo ord(c)
    wesosa (c = "0") { cha 48; }
    wesosa (c = "1") { cha 49; }
    wesosa (c = "2") { cha 50; }
    wesosa (c = "3") { cha 51; }
    wesosa (c = "4") { cha 52; }
    wesosa (c = "5") { cha 53; }
    wesosa (c = "6") { cha 54; }
    wesosa (c = "7") { cha 55; }
    wesosa (c = "8") { cha 56; }
    wesosa (c = "9") { cha 57; }
    cha -1;
bawoum tosedo

tosedo parseBig(s)
    sheye ds <- [];
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        omse(ds, ord(s[i]) - 48);
    }
    cha ds;
bawoum tosedo

tosedo toDigits(n)
    sheye ds <- [];
    wesosa (n = 0) {
        omse(ds, 0);
        cha ds;
    }
    veshim (n > 0) {
        omse(ds, n drossou 10);
        n <- n / 10;
    }
    cha reverse(ds);
bawoum tosedo

tosedo toNum(ds)
    sheye n <- 0;
    sho (sheye i <- 0; i < louwo(ds); i <- i + 1) {
        n <- (n * 10) + ds[i];
    }
    cha n;
bawoum tosedo

tosedo reverse(ds)
    sheye m <- louwo(ds);
    sheye out <- [];
    sho (sheye i <- 1; i <= m; i <- i + 1) {
        omse(out, ds[m - i]);
    }
    cha out;
bawoum tosedo

tosedo addNums(a, b)
    sheye i <- louwo(a) - 1;
    sheye j <- louwo(b) - 1;
    sheye carry <- 0;
    sheye out <- [];
    mele {
        sheye s <- carry;
        wesosa (i >= 0) {
            s <- s + a[i];
            i <- i - 1;
        }
        wesosa (j >= 0) {
            s <- s + b[j];
            j <- j - 1;
        }
        omse(out, s drossou 10);
        carry <- s / 10;
    } veshim ((i >= 0) emsoulve (j >= 0) emsoulve (carry > 0));
    cha reverse(out);
bawoum tosedo

tosedo mulNums(a, b)
    sheye res <- [0];
    sheye m <- louwo(b);
    sho (sheye bi <- m - 1; bi >= 0; bi <- bi - 1) {
        sheye carry <- 0;
        sheye cur <- [];
        sho (sheye z <- 0; z < (m - 1) - bi; z <- z + 1) {
            omse(cur, 0);
        }
        sho (sheye ai <- louwo(a) - 1; ai >= 0; ai <- ai - 1) {
            sheye p <- (a[ai] * b[bi]) + carry;
            omse(cur, p drossou 10);
            carry <- p / 10;
        }
        wesosa (carry > 0) {
            omse(cur, carry);
        }
        res <- addNums(res, reverse(cur));
    }
    cha res;
bawoum tosedo

tosedo trim(ds)
    sheye i <- 0;
    sheye m <- louwo(ds);
    sheye goon <- i < m;
    veshim (goon) {
        wesosa (ds[i] = 0) {
            i <- i + 1;
            goon <- i < m;
        } oli {
            goon <- ishe;
        }
    }
    wesosa (i = m) {
        sheye z <- [0];
        cha z;
    }
    cha slice(ds, i, m - i);
bawoum tosedo

tosedo strOf(ds)
    sheye s <- "";
    sho (sheye i <- 0; i < louwo(ds); i <- i + 1) {
        s <- s + ramou(ds[i]);
    }
    cha s;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- louwo(line);
    sheye pos <- 0;
    sheye goon <- pos < n;
    veshim (goon) {
        wesosa (line[pos] = " ") {
            goon <- ishe;
        } oli {
            pos <- pos + 1;
            goon <- pos < n;
        }
    }
    sheye da <- parseBig(slice(line, 0, pos));
    sheye db <- parseBig(slice(line, pos + 1, (n - pos) - 1));
    wami strOf(trim(addNums(da, db))) + " " + strOf(trim(mulNums(da, db)));
    line <- diwela();
}
