tosedo num(s, st, len)
    sheye v <- 0;
    sho (sheye i <- st; i < (st + len); i <- i + 1) {
        v <- (v * 10) + odresdra(s[i]);
    }
    cha v;
bawoum tosedo

sheye t <- [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
sheye names <- ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(line) >= 10) {
        sheye y <- num(line, 0, 4);
        sheye m <- num(line, 5, 2);
        sheye d <- num(line, 8, 2);
        wesosa (m < 3) {
            y <- y - 1;
        }
        sheye w <- y + (y / 4);
        w <- w - (y / 100);
        w <- w + (y / 400);
        w <- w + t[m - 1];
        w <- w + d;
        w <- w drossou 7;
        wami names[w];
    }
    line <- diwela();
}
