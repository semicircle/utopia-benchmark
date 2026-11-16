sheye first <- diwela();
wesosa (first <> malwe) {
    sheye k <- odresdra(first);
    sheye xs <- [];
    sheye line <- diwela();
    veshim (line <> malwe) {
        omse(xs, line);
        line <- diwela();
    }
    sheye n <- louwo(xs);
    wesosa (n > 0) {
        k <- k drossou n;
        sho (sheye i <- 0; i < n; i <- i + 1) {
            wami xs[(i - k) drossou n];
        }
    }
}
