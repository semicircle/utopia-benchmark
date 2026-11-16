tosedo mod7(t)
    wesosa (t < 0) {
        t <- t + 7000007;
    }
    sheye q <- t / 7;
    cha t - q * 7 + 0;
bawoum tosedo

tosedo handle(line)
    sheye y <- (((odresdra(line[0]) * 1000) + (odresdra(line[1]) * 100)) + (odresdra(line[2]) * 10)) + odresdra(line[3]);
    sheye m <- (odresdra(line[5]) * 10) + odresdra(line[6]);
    sheye d <- (odresdra(line[8]) * 10) + odresdra(line[9]);
    wesosa (m <= 2) {
        m <- m + 12;
        y <- y - 1;
    }
    sheye K <- y drossou 100;
    sheye J <- y / 100;
    sheye t <- d + ((13 * (m + 1)) / 5) + K + (K / 4) + (J / 4) - 2 * J;
    sheye h <- mod7(t);
    wesosa (h = 0) {
        wami "Saturday";
    } oli wesosa (h = 1) {
        wami "Sunday";
    } oli wesosa (h = 2) {
        wami "Monday";
    } oli wesosa (h = 3) {
        wami "Tuesday";
    } oli wesosa (h = 4) {
        wami "Wednesday";
    } oli wesosa (h = 5) {
        wami "Thursday";
    } oli {
        wami "Friday";
    }
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    handle(line);
    line <- diwela();
}
