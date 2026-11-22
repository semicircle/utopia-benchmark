sheye kLine <- diwela();
wesosa (kLine <> malwe) {
    sheye k <- odresdra(kLine);
    sheye items <- [];
    sheye line <- diwela();
    veshim (line <> malwe) {
        omse(items, line);
        line <- diwela();
    }
    sheye n <- louwo(items);
    wesosa (n > 0) {
        sheye rot <- k drossou n;
        sheye start <- n - rot;
        sheye i <- 0;
        sheye idx <- 0;
        veshim (i < n) {
            idx <- (start + i) drossou n;
            wami items[idx];
            i <- i + 1;
        }
    }
}
