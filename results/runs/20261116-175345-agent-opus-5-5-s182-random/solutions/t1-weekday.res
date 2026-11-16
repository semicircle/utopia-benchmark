sheye names <- ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye y <- odresdra(((line[0] + line[1]) + line[2]) + line[3]);
    sheye m <- odresdra(line[5] + line[6]);
    sheye d <- odresdra(line[8] + line[9]);
    wesosa (m <= 2) {
        y <- y - 1;
        m <- m + 12;
    }
    ' days since a fixed epoch: March-based year
    sheye days <- 365 * y;
    days <- days + (y / 4);
    days <- days - (y / 100);
    days <- days + (y / 400);
    days <- days + (((153 * (m - 3)) + 2) / 5);
    days <- days + d;
    wami names[(days + 1) drossou 7];
    line <- diwela();
}
