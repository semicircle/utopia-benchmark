tosedo substr(s, start, end)
    sheye t <- "";
    sheye i <- start;
    veshim (i < end) {
        t <- t + s[i];
        i <- i + 1;
    }
    cha t;
bawoum tosedo

tosedo weekdayIndex(y, m, d)
    sheye t <- [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
    wesosa (m < 3) {
        y <- y - 1;
    }
    sheye v <- y;
    v <- v + (y / 4);
    v <- v - (y / 100);
    v <- v + (y / 400);
    sheye mi <- m - 1;
    v <- v + t[mi];
    v <- v + d;
    cha v drossou 7;
bawoum tosedo

sheye names <- ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye y <- odresdra(substr(line, 0, 4));
    sheye m <- odresdra(substr(line, 5, 7));
    sheye d <- odresdra(substr(line, 8, 10));
    sheye idx <- weekdayIndex(y, m, d);
    wami names[idx];
    line <- diwela();
}
