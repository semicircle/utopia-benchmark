tosedo split(s)
    sheye out <- [];
    sheye cur <- "";
    sheye has <- ishe;
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        sheye c <- s[i];
        wesosa ((c = " ") emsoulve (c = "\t")) {
            wesosa (has) {
                omse(out, cur);
                cur <- "";
                has <- ishe;
            }
        } oli {
            cur <- cur + c;
            has <- shilsa;
        }
    }
    wesosa (has) {
        omse(out, cur);
    }
    cha out;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye p <- split(line);
    wesosa (louwo(p) >= 2) {
        sheye a <- odresdra(p[0]);
        sheye b <- odresdra(p[1]);
        sheye q <- a / b;
        sheye r <- a - (b * q);
        wami (q + " ") + r;
    }
    line <- diwela();
}
