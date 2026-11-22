sheye line <- diwela();
veshim (line <> malwe) {
    sheye i <- 0;
    sheye leftText <- "";
    veshim (line[i] <> " ") {
        leftText <- leftText + line[i];
        i <- i + 1;
    }
    sheye rightText <- "";
    sho (i <- i + 1; i < louwo(line); i <- i + 1) {
        rightText <- rightText + line[i];
    }
    sheye a <- odresdra(leftText);
    sheye b <- odresdra(rightText);
    sheye q <- a / b;
    sheye r <- a - (b * q);
    tivou q;
    tivou " ";
    wami r;
    line <- diwela();
}
