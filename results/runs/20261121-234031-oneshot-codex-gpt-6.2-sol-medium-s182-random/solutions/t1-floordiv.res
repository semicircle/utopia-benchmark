sheye line <- diwela();
veshim (line <> malwe) {
    sheye first <- "";
    sheye second <- "";
    sheye i <- 0;
    veshim (line[i] <> " ") {
        first <- first + line[i];
        i <- i + 1;
    }
    sho (i <- i + 1; i < louwo(line); i <- i + 1) {
        second <- second + line[i];
    }
    sheye a <- odresdra(first);
    sheye b <- odresdra(second);
    sheye q <- a / b;
    sheye r <- a - (b * q);
    wami ramou(q) + " " + ramou(r);
    line <- diwela();
}
