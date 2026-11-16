sheye k <- odresdra(diwela());
sheye items <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(items, line);
    line <- diwela();
}
sheye m <- louwo(items);
wesosa (m > 0) {
    sheye shift <- k drossou m;
    sho (sheye i <- 0; i < m; i <- i + 1) {
        wami items[((i + (m - shift)) drossou m)];
    }
}
