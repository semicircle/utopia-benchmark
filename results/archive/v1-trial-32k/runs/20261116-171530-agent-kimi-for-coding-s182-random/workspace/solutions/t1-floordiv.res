tosedo substr(s, i, j)
    sheye r <- "";
    sho (sheye k <- i; k <= j; k <- k + 1) {
        r <- r + s[k];
    }
    cha r;
bawoum tosedo

tosedo handle(a, b)
    sheye q <- a / b;
    sheye r <- a - b * q;
    wami q + " " + r;
bawoum tosedo

tosedo split(line)
    sheye space <- 0;
    sheye i <- 0;
    veshim (i < louwo(line)) {
        wesosa (line[i] = " ") {
            space <- i;
        }
        i <- i + 1;
    }
    sheye a <- odresdra(substr(line, 0, space - 1));
    sheye b <- odresdra(substr(line, space + 1, louwo(line) - 1));
    handle(a, b);
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    split(line);
    line <- diwela();
}
