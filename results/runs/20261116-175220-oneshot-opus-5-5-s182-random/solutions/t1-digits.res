sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(line) > 0) {
        sheye n <- odresdra(line);
        sheye neg <- n < 0;
        sheye m <- n;
        wesosa (neg) {
            m <- -n;
        }
        sheye s <- 0;
        sheye r <- 0;
        veshim (m > 0) {
            sheye d <- m drossou 10;
            s <- s + d;
            r <- (r * 10) + d;
            m <- m / 10;
        }
        wesosa (neg) {
            r <- -r;
        }
        wami (ramou(s) + " ") + ramou(r);
    }
    line <- diwela();
}
