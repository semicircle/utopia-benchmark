tosedo ord(c)
    wesosa (c = "0") { cha 48; }
    wesosa (c = "1") { cha 49; }
    wesosa (c = "2") { cha 50; }
    wesosa (c = "3") { cha 51; }
    wesosa (c = "4") { cha 52; }
    wesosa (c = "5") { cha 53; }
    wesosa (c = "6") { cha 54; }
    wesosa (c = "7") { cha 55; }
    wesosa (c = "8") { cha 56; }
    wesosa (c = "9") { cha 57; }
    cha -1;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye i <- 0;
    sheye neg <- ishe;
    wesosa (line[0] = "-") {
        neg <- shilsa;
        i <- 1;
    }
    sheye sum <- 0;
    sheye rchars <- [];
    veshim (i < louwo(line)) {
        sheye d <- line[i];
        sum <- sum + (ord(d) - 48);
        wesosa ((d <> "0") emsoulve (louwo(rchars) > 0)) {
            omse(rchars, d);
        }
        i <- i + 1;
    }
    sheye revStr <- "";
    wesosa (louwo(rchars) = 0) {
        revStr <- "0";
    }
    sho (sheye t <- 1; t <= louwo(rchars); t <- t + 1) {
        revStr <- revStr + rchars[louwo(rchars) - t];
    }
    sheye rev <- odresdra(revStr);
    wesosa (neg) {
        rev <- -rev;
    }
    wami sum + " " + rev;
    line <- diwela();
}
