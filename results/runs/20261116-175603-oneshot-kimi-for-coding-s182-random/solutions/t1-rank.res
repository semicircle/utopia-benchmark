tosedo splitints(s)
    sheye r <- [];
    sheye cur <- "";
    sheye has <- ishe;
    sho (sheye i <- 0; i <= louwo(s); i <- i + 1) {
        wesosa (i = louwo(s)) {
            wesosa (has) {
                omse(r, odresdra(cur));
            }
        } oli wesosa (s[i] = " ") {
            wesosa (has) {
                omse(r, odresdra(cur));
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

sheye firstline <- diwela();
sheye xs <- [];
wesosa (firstline <> malwe) {
    xs <- splitints(firstline);
}
sheye line <- diwela();
veshim (line <> malwe) {
    sheye q <- odresdra(line);
    sheye smaller <- 0;
    sheye found <- ishe;
    sho (sheye i <- 0; i < louwo(xs); i <- i + 1) {
        wesosa (xs[i] < q) {
            smaller <- smaller + 1;
        }
        wesosa (xs[i] = q) {
            found <- shilsa;
        }
    }
    wesosa (found) {
        wami smaller + " found";
    } oli {
        wami smaller + " missing";
    }
    line <- diwela();
}
