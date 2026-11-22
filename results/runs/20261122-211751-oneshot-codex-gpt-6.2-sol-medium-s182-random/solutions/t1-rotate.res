sheye k <- odresdra(diwela());
sheye items <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(items, line);
    line <- diwela();
}
sheye n <- louwo(items);
wesosa (n > 0) {
    sho (sheye i <- 0; i < n; i <- i + 1) {
        wami items[(i - k) drossou n];
    }
}
