sheye even <- 0;
sheye odd <- 0;
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa ((odresdra(line) drossou 2) = 0) {
        even <- even + 1;
    } oli {
        odd <- odd + 1;
    }
    line <- diwela();
}
wami "even " + even;
wami "odd " + odd;
