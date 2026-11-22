sheye k <- odresdra(diwela());
sheye items <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(items, line);
    line <- diwela();
}
sheye size <- louwo(items);
wesosa (size > 0) {
    sho (sheye i <- 0; i < size; i <- i + 1) {
        wami items[(i - k) drossou size];
    }
}
