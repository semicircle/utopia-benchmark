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

sheye first <- diwela();
sheye arr <- [];
wesosa (first <> malwe) {
    sheye toks <- split(first);
    sho (sheye i <- 0; i < louwo(toks); i <- i + 1) {
        omse(arr, odresdra(toks[i]));
    }
}
sheye n <- louwo(arr);
sheye line <- diwela();
veshim (line <> malwe) {
    sheye qt <- split(line);
    wesosa (louwo(qt) > 0) {
        sheye q <- odresdra(qt[0]);
        sheye lo <- 0;
        sheye hi <- n;
        veshim (lo < hi) {
            sheye mid <- (lo + hi) / 2;
            wesosa (arr[mid] < q) {
                lo <- mid + 1;
            } oli {
                hi <- mid;
            }
        }
        sheye res <- "missing";
        wesosa (lo < n) {
            wesosa (arr[lo] = q) {
                res <- "found";
            }
        }
        wami (ramou(lo) + " ") + res;
    }
    line <- diwela();
}
