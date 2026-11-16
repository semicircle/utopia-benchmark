sheye k <- odresdra(diwela());
sheye items <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(items, line);
    line <- diwela();
}
sheye m <- louwo(items);
wesosa (m > 0) {
    sheye k2 <- k drossou m;
    wesosa (k2 < 0) {
        k2 <- k2 + m;
    }
    sho (sheye i <- 0; i < m; i <- i + 1) {
        wami items[((i - k2) + m) drossou m];
    }
}
