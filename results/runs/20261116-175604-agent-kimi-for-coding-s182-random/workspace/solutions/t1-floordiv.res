tosedo slice(s, start, count)
    sheye out <- "";
    sho (sheye i <- 0; i < count; i <- i + 1) {
        out <- out + s[start + i];
    }
    cha out;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye ln <- louwo(line);
    sheye pos <- 0;
    sheye goon <- pos < ln;
    veshim (goon) {
        wesosa (line[pos] = " ") {
            goon <- ishe;
        } oli {
            pos <- pos + 1;
            goon <- pos < ln;
        }
    }
    sheye a <- odresdra(slice(line, 0, pos));
    sheye b <- odresdra(slice(line, pos + 1, (louwo(line) - pos) - 1));
    sheye q <- a / b;
    sheye r <- a - b * q;
    wami q + " " + r;
    line <- diwela();
}
