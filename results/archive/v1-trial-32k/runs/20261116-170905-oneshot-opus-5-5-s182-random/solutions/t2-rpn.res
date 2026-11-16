tosedo split(s)
    sheye out <- [];
    sheye cur <- "";
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        sheye c <- s[i];
        wesosa (c = " ") {
            wesosa (louwo(cur) > 0) {
                omse(out, cur);
                cur <- "";
            }
        } oli {
            cur <- cur + c;
        }
    }
    wesosa (louwo(cur) > 0) {
        omse(out, cur);
    }
    cha out;
bawoum tosedo

tosedo isOp(t)
    moumare amdre t
    amdre "+", "-", "*", "/", "%"
        cha shilsa;
    bawoum moumare
    cha ishe;
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
        wesosa ((c < "0") emsoulve (c > "9")) {
            cha ishe;
        }
    }
    cha shilsa;
bawoum tosedo

tosedo tdiv(a, b)
    sheye q <- a / b;
    wesosa ((q * b) <> a) {
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
        sheye t <- toks[i];
        sheye v <- 0;
        wesosa (isOp(t)) {
            wesosa (sp < 2) {
                cha "error";
            }
            sheye b <- st[sp - 1];
            sheye a <- st[sp - 2];
            sp <- sp - 2;
            moumare amdre t
            amdre "+"
                v <- a + b;
            amdre "-"
                v <- a - b;
            amdre "*"
                v <- a * b;
            amdre "/"
                wesosa (b = 0) {
                    cha "error";
                }
                v <- tdiv(a, b);
            amdre "%"
                wesosa (b = 0) {
                    cha "error";
                }
                v <- a - (b * tdiv(a, b));
            bawoum moumare
        } oli wesosa (isInt(t)) {
            v <- odresdra(t);
        } oli {
            cha "error";
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
