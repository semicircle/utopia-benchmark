sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    sheye neg <- n < 0;
    wesosa (neg) {
        n <- -n;
    }
    sheye s <- 0;
    sheye r <- 0;
    veshim (n > 0) {
        sheye d <- n drossou 10;
        s <- s + d;
        r <- (r * 10) + d;
        n <- n / 10;
    }
    wesosa (neg) {
        r <- -r;
    }
    wami (s + " ") + r;
    line <- diwela();
}
