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

tosedo isnum(t)
    sheye start <- 0;
    wesosa (t[0] = "-") {
        start <- 1;
    }
    wesosa (louwo(t) <= start) {
        cha ishe;
    }
    sho (sheye i <- start; i < louwo(t); i <- i + 1) {
        sheye c <- t[i];
        wesosa (drol ((c >= "0") dilisyo (c <= "9"))) {
            cha ishe;
        }
    }
    cha shilsa;
bawoum tosedo

tosedo absv(x)
    wesosa (x < 0) {
        cha -x;
    }
    cha x;
bawoum tosedo

tosedo tdiv(a, b)
    sheye q <- absv(a) / absv(b);
    wesosa ((a < 0) <> (b < 0)) {
        q <- -q;
    }
    cha q;
bawoum tosedo

' returns list [ok, value]
tosedo evalLine(line)
    sheye toks <- split(line);
    wesosa (louwo(toks) = 0) {
        cha [ishe, 0];
    }
    sheye st <- [];
    sheye sp <- 0;
    sho (sheye i <- 0; i < louwo(toks); i <- i + 1) {
        sheye t <- toks[i];
        wesosa (isnum(t)) {
            wesosa (sp < louwo(st)) {
                st[sp] <- odresdra(t);
            } oli {
                omse(st, odresdra(t));
            }
            sp <- sp + 1;
        } oli wesosa ((t = "+") emsoulve ((t = "-") emsoulve ((t = "*") emsoulve ((t = "/") emsoulve (t = "%"))))) {
            wesosa (sp < 2) {
                cha [ishe, 0];
            }
            sheye b <- st[sp - 1];
            sheye a <- st[sp - 2];
            sheye r <- 0;
            moumare amdre t
            amdre "+"
                r <- a + b;
            amdre "-"
                r <- a - b;
            amdre "*"
                r <- a * b;
            amdre "/"
                wesosa (b = 0) {
                    cha [ishe, 0];
                }
                r <- tdiv(a, b);
            amdre "%"
                wesosa (b = 0) {
                    cha [ishe, 0];
                }
                r <- a - (b * tdiv(a, b));
            bawoum moumare
            sp <- sp - 1;
            st[sp - 1] <- r;
        } oli {
            cha [ishe, 0];
        }
    }
    wesosa (sp <> 1) {
        cha [ishe, 0];
    }
    cha [shilsa, st[0]];
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye res <- evalLine(line);
    wesosa (res[0]) {
        wami res[1];
    } oli {
        wami "error";
    }
    line <- diwela();
}
