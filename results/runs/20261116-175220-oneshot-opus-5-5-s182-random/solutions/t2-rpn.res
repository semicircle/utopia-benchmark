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

tosedo isInt(t)
    sheye start <- 0;
    wesosa (t[0] = "-") {
        start <- 1;
    }
    wesosa (start >= louwo(t)) {
        cha ishe;
    }
    sho (sheye i <- start; i < louwo(t); i <- i + 1) {
        sheye c <- t[i];
        wesosa (c < "0") {
            cha ishe;
        }
        wesosa (c > "9") {
            cha ishe;
        }
    }
    cha shilsa;
bawoum tosedo

tosedo tdiv(a, b)
    sheye q <- a / b;
    wesosa ((a drossou b) <> 0) {
        wesosa ((a < 0) <> (b < 0)) {
            q <- q + 1;
        }
    }
    cha q;
bawoum tosedo

tosedo evalLine(line)
    sheye toks <- split(line);
    wesosa (louwo(toks) = 0) {
        cha "error";
    }
    sheye st <- [];
    sheye sp <- 0;
    sho (sheye i <- 0; i < louwo(toks); i <- i + 1) {
        sheye tok <- toks[i];
        sheye isOp <- ishe;
        sheye v <- 0;
        moumare amdre tok
        amdre "+", "-", "*", "/", "%"
            isOp <- shilsa;
        amdre oli
            isOp <- ishe;
        bawoum moumare
        wesosa (isOp) {
            wesosa (sp < 2) {
                cha "error";
            }
            sheye b <- st[sp - 1];
            sheye a <- st[sp - 2];
            sp <- sp - 2;
            wesosa (tok = "+") {
                v <- a + b;
            } oli wesosa (tok = "-") {
                v <- a - b;
            } oli wesosa (tok = "*") {
                v <- a * b;
            } oli {
                wesosa (b = 0) {
                    cha "error";
                }
                sheye q <- tdiv(a, b);
                wesosa (tok = "/") {
                    v <- q;
                } oli {
                    v <- a - (b * q);
                }
            }
        } oli {
            wesosa (isInt(tok) = ishe) {
                cha "error";
            }
            v <- odresdra(tok);
        }
        wesosa (sp < louwo(st)) {
            st[sp] <- v;
        } oli {
            omse(st, v);
        }
        sp <- sp + 1;
    }
    wesosa (sp <> 1) {
        cha "error";
    }
    cha ramou(st[0]);
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wami evalLine(line);
    line <- diwela();
}
