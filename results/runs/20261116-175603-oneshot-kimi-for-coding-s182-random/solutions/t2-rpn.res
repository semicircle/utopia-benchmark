tosedo isdigit(c)
    sheye ds <- "0123456789";
    sho (sheye i <- 0; i < 10; i <- i + 1) {
        wesosa (c = ds[i]) {
            cha shilsa;
        }
    }
    cha ishe;
bawoum tosedo

tosedo isnum(t)
    sheye start <- 0;
    wesosa (louwo(t) > 0) {
        wesosa (t[0] = "-") {
            start <- 1;
        }
    }
    wesosa ((louwo(t) - start) < 1) {
        cha ishe;
    }
    sho (sheye i <- start; i < louwo(t); i <- i + 1) {
        wesosa (drol isdigit(t[i])) {
            cha ishe;
        }
    }
    cha shilsa;
bawoum tosedo

tosedo isop(t)
    cha ((t = "+") emsoulve ((t = "-") emsoulve ((t = "*") emsoulve ((t = "/") emsoulve (t = "%")))));
bawoum tosedo

tosedo tokens(s)
    sheye r <- [];
    sheye cur <- "";
    sheye has <- ishe;
    sho (sheye i <- 0; i <= louwo(s); i <- i + 1) {
        wesosa (i = louwo(s)) {
            wesosa (has) {
                omse(r, cur);
            }
        } oli wesosa (s[i] = " ") {
            wesosa (has) {
                omse(r, cur);
                cur <- "";
                has <- ishe;
            }
        } oli {
            cur <- cur + s[i];
            has <- shilsa;
        }
    }
    cha r;
bawoum tosedo

tosedo tdiv(a, b)
    sheye q <- a / b;
    sheye r <- a drossou b;
    wesosa ((r <> 0) dilisyo ((a < 0) <> (b < 0))) {
        q <- q + 1;
    }
    cha q;
bawoum tosedo

tosedo tmod(a, b)
    cha a - (b * tdiv(a, b));
bawoum tosedo

tosedo evalline(line)
    sheye ts <- tokens(line);
    wesosa (louwo(ts) = 0) {
        cha "error";
    }
    sheye st <- [];
    sheye n <- 0;
    sheye err <- ishe;
    sho (sheye i <- 0; i < louwo(ts); i <- i + 1) {
        sheye t <- ts[i];
        wesosa (err) {
            sheye nothing <- 0;
        } oli wesosa (isnum(t)) {
            omse(st, odresdra(t));
            n <- n + 1;
        } oli wesosa (isop(t)) {
            wesosa (n < 2) {
                err <- shilsa;
            } oli {
                n <- n - 1;
                sheye b <- st[n];
                n <- n - 1;
                sheye a <- st[n];
                wesosa (t = "+") {
                    omse(st, a + b);
                    n <- n + 1;
                } oli wesosa (t = "-") {
                    omse(st, a - b);
                    n <- n + 1;
                } oli wesosa (t = "*") {
                    omse(st, a * b);
                    n <- n + 1;
                } oli wesosa (t = "/") {
                    wesosa (b = 0) {
                        err <- shilsa;
                    } oli {
                        omse(st, tdiv(a, b));
                        n <- n + 1;
                    }
                } oli {
                    wesosa (b = 0) {
                        err <- shilsa;
                    } oli {
                        omse(st, tmod(a, b));
                        n <- n + 1;
                    }
                }
            }
        } oli {
            err <- shilsa;
        }
    }
    wesosa (err) {
        cha "error";
    }
    wesosa (n <> 1) {
        cha "error";
    }
    cha ramou(st[0]);
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wami evalline(line);
    line <- diwela();
}
