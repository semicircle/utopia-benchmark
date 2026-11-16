sheye xs <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(xs, line);
    line <- diwela();
}
sho (sheye i <- louwo(xs) - 1; i >= 0; i <- i - 1) {
    wami xs[i];
}
