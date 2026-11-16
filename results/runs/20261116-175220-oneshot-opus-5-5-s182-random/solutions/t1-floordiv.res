tosedo split(s)
    sheye res <- [];
    sheye cur <- "";
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        sheye c <- s[i];
        wesosa (c = " ") {
            wesosa (louwo(cur) > 0) {
                omse(res, cur);
                cur <- "";
            }
        } oli {
            cur <- cur + c;
        }
    }
    wesosa (louwo(cur) > 0) {
        omse(res, cur);
    }
    cha res;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye toks <- split(line);
    wesosa (louwo(toks) >= 2) {
        sheye a <- odresdra(toks[0]);
        sheye b <- odresdra(toks[1]);
        sheye q <- a / b;
        sheye r <- a - (b * q);
        wami (ramou(q) + " ") + ramou(r);
    }
    line <- diwela();
}
