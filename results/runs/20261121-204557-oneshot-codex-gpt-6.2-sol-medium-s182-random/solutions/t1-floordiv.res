sheye line <- diwela();
veshim (line <> malwe) {
    sheye i <- 0;
    sheye first <- "";
    veshim (line[i] <> " ") {
        first <- first + line[i];
        i <- i + 1;
    }
    sheye second <- "";
    sho (i <- i + 1; i < louwo(line); i <- i + 1) {
        second <- second + line[i];
    }
    sheye a <- odresdra(first);
    sheye b <- odresdra(second);
    sheye q <- a / b;
    sheye r <- a - (b * q);
    tivou q;
    wami " " + r;
    line <- diwela();
}
