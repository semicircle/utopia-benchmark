sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    sheye negative <- n < 0;
    wesosa (negative) {
        n <- -n;
    }
    sheye sum <- 0;
    sheye reverse <- 0;
    veshim (n > 0) {
        sheye digit <- n drossou 10;
        sum <- sum + digit;
        reverse <- (reverse * 10) + digit;
        n <- n / 10;
    }
    wesosa (negative) {
        reverse <- -reverse;
    }
    wami ramou(sum) + " " + ramou(reverse);
    line <- diwela();
}
