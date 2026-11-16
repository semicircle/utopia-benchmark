sheye kl <- diwela();
wesosa (kl = malwe) {
    cha;
}
sheye k <- odresdra(kl);
sheye items <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(items, line);
    line <- diwela();
}
sheye n <- louwo(items);
wesosa (n = 0) {
    cha;
}
sheye s <- k drossou n;
sho (sheye i <- 0; i < n; i <- i + 1) {
    wami items[(i - s) drossou n];
}
