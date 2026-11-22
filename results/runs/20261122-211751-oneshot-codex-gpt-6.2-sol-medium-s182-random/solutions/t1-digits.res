sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    sheye sign <- 1;
    wesosa (n < 0) {
        sign <- -1;
        n <- -n;
    }
    sheye sum <- 0;
    sheye reversed <- 0;
    veshim (n > 0) {
        sheye digit <- n drossou 10;
        sum <- sum + digit;
        reversed <- (reversed * 10) + digit;
        n <- n / 10;
    }
    wami (ramou(sum) + " ") + (sign * reversed);
    line <- diwela();
}
