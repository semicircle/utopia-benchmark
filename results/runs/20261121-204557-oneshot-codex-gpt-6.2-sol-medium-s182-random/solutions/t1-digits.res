sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    sheye negative <- n < 0;
    wesosa (negative) {
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
    wesosa (negative) {
        reversed <- -reversed;
    }
    tivou sum;
    wami " " + reversed;
    line <- diwela();
}
