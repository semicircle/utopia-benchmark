tosedo dval(c)
    sheye ds <- "0123456789";
    sho (sheye i <- 0; i < 10; i <- i + 1) {
        wesosa (ds[i] = c) {
            cha i;
        }
    }
    cha -1;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    sheye neg <- n < 0;
    sheye s <- ramou(n);
    sheye sum <- 0;
    sheye rev <- 0;
    sho (sheye i <- louwo(s) - 1; i >= 0; i <- i - 1) {
        sheye d <- dval(s[i]);
        wesosa (d >= 0) {
            sum <- sum + d;
            rev <- (rev * 10) + d;
        }
    }
    wesosa (neg) {
        rev <- -rev;
    }
    wami (sum + " ") + rev;
    line <- diwela();
}
