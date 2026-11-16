sheye e <- 0;
sheye o <- 0;
sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    wesosa ((n drossou 2) = 0) {
        e <- e + 1;
    } oli {
        o <- o + 1;
    }
    line <- diwela();
}
wami "even " + e;
wami "odd " + o;
