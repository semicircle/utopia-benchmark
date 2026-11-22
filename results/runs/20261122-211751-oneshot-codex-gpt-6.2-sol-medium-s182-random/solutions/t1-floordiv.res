sheye line <- diwela();
veshim (line <> malwe) {
    sheye left <- "";
    sheye right <- "";
    sheye i <- 0;
    veshim (line[i] <> " ") {
        left <- left + line[i];
        i <- i + 1;
    }
    sho (i <- i + 1; i < louwo(line); i <- i + 1) {
        right <- right + line[i];
    }
    sheye a <- odresdra(left);
    sheye b <- odresdra(right);
    sheye q <- a / b;
    sheye r <- a - (b * q);
    wami (ramou(q) + " ") + r;
    line <- diwela();
}
