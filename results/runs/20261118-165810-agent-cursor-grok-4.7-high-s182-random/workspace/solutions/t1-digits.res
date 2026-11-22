sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    wesosa (n = 0) {
        wami "0 0";
    } oli {
        sheye sign <- 1;
        wesosa (n < 0) {
            sign <- -1;
            n <- -n;
        }
        sheye sum <- 0;
        sheye rev <- 0;
        sheye d <- 0;
        veshim (n > 0) {
            d <- n drossou 10;
            sum <- sum + d;
            rev <- (rev * 10) + d;
            n <- n / 10;
        }
        rev <- rev * sign;
        wami sum + " " + rev;
    }
    line <- diwela();
}
