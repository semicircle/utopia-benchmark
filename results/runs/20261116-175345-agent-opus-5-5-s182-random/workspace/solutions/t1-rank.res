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

sheye first <- diwela();
wesosa (first = malwe) {
    first <- "";
}
sheye toks <- split(first);
sheye xs <- [];
sho (sheye i <- 0; i < louwo(toks); i <- i + 1) {
    omse(xs, odresdra(toks[i]));
}
sheye n <- louwo(xs);
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(split(line)) > 0) {
        sheye q <- odresdra(line);
        sheye lo <- 0;
        sheye hi <- n;
        veshim (lo < hi) {
            sheye mid <- (lo + hi) / 2;
            wesosa (xs[mid] < q) {
                lo <- mid + 1;
            } oli {
                hi <- mid;
            }
        }
        sheye found <- ishe;
        wesosa (lo < n) {
            found <- xs[lo] = q;
        }
        wesosa (found) {
            wami lo + " found";
        } oli {
            wami lo + " missing";
        }
    }
    line <- diwela();
}
