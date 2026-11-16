tosedo findspace(s)
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        wesosa (s[i] = " ") {
            cha i;
        }
    }
    cha -1;
bawoum tosedo

tosedo slice(s, i, j)
    sheye r <- "";
    sho (sheye k <- i; k < j; k <- k + 1) {
        r <- r + s[k];
    }
    cha r;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye sp <- findspace(line);
    sheye a <- odresdra(slice(line, 0, sp));
    sheye b <- odresdra(slice(line, sp + 1, louwo(line)));
    sheye q <- a / b;
    sheye r <- a - (b * q);
    wami q + " " + r;
    line <- diwela();
}
