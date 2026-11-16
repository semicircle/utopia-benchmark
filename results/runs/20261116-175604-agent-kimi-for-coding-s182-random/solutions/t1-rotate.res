sheye k <- odresdra(diwela());
sheye items <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(items, line);
    line <- diwela();
}
sheye n <- louwo(items);
wesosa (n > 0) {
    sheye r <- k drossou n;
    wesosa (r < 0) {
        r <- r + n;
    }
    sho (sheye i <- 0; i < n; i <- i + 1) {
        wami items[((n - r) + i) drossou n];
    }
}
