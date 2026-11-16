tosedo num(s, a, b)
    sheye v <- 0;
    sho (sheye i <- a; i <= b; i <- i + 1) {
        v <- (v * 10) + odresdra(s[i]);
    }
    cha v;
bawoum tosedo

sheye names <- ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
sheye t <- [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(line) >= 10) {
        sheye y <- num(line, 0, 3);
        sheye m <- num(line, 5, 6);
        sheye d <- num(line, 8, 9);
        wesosa (m < 3) {
            y <- y - 1;
        }
        sheye w <- y;
        w <- w + (y / 4);
        w <- w - (y / 100);
        w <- w + (y / 400);
        w <- w + t[m - 1];
        w <- w + d;
        w <- w drossou 7;
        wami names[w];
    }
    line <- diwela();
}
