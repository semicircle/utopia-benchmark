sheye k <- odresdra(diwela());
sheye items <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(items, line);
    line <- diwela();
}
sheye count <- louwo(items);
wesosa (count > 0) {
    sheye shift <- k drossou count;
    sho (sheye i <- 0; i < count; i <- i + 1) {
        wami items[(i - shift) drossou count];
    }
}
