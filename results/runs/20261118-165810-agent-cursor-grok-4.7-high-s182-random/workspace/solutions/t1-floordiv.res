tosedo splitWs(s)
    sheye tokens <- [];
    sheye n <- louwo(s);
    sheye i <- 0;
    sheye tok <- "";
    veshim (i < n) {
        wesosa (s[i] = " ") {
            wesosa (louwo(tok) > 0) {
                omse(tokens, tok);
                tok <- "";
            }
            i <- i + 1;
        } oli {
            tok <- tok + s[i];
            i <- i + 1;
        }
    }
    wesosa (louwo(tok) > 0) {
        omse(tokens, tok);
    }
    cha tokens;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye tokens <- splitWs(line);
    sheye a <- odresdra(tokens[0]);
    sheye b <- odresdra(tokens[1]);
    sheye q <- a / b;
    sheye r <- a drossou b;
    wami q + " " + r;
    line <- diwela();
}
