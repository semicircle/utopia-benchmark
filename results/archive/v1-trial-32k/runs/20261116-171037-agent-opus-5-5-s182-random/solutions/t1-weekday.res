tosedo sub(s, a, b)
    sheye r <- "";
    sho (sheye i <- a; i < b; i <- i + 1) {
        r <- r + s[i];
    }
    cha r;
bawoum tosedo

sheye t <- [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
sheye names <- ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(line) >= 10) {
        sheye y <- odresdra(sub(line, 0, 4));
        sheye m <- odresdra(sub(line, 5, 7));
        sheye d <- odresdra(sub(line, 8, 10));
        wesosa (m < 3) {
            y <- y - 1;
        }
        sheye w <- ((((((y + (y / 4)) - (y / 100)) + (y / 400)) + t[m - 1]) + d) drossou 7);
        wami names[w];
    }
    line <- diwela();
}
