sheye k <- odresdra(diwela());
sheye xs <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(xs, line);
    line <- diwela();
}
sheye n <- louwo(xs);
wesosa (n > 0) {
    sheye s <- k drossou n;
    sho (sheye i <- 0; i < n; i <- i + 1) {
        wami xs[(i - s) drossou n];
    }
}
