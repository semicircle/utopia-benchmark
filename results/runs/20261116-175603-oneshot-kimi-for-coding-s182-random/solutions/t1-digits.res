sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    sheye neg <- ishe;
    wesosa (n < 0) {
        neg <- shilsa;
        n <- -n;
    }
    sheye sum <- 0;
    sheye rev <- 0;
    vesheim (n > 0) {
        sheye d <- n drossou 10;
        sum <- sum + d;
        rev <- (rev * 10) + d;
        n <- n / 10;
    }
    wesosa (neg) {
        rev <- -rev;
    }
    wami sum + " " + rev;
    line <- diwela();
}
