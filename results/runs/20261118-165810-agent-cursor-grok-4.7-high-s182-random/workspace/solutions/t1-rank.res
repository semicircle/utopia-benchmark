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

tosedo lowerBound(nums, q)
    sheye lo <- 0;
    sheye hi <- louwo(nums);
    sheye mid <- 0;
    veshim (lo < hi) {
        mid <- (lo + hi) / 2;
        wesosa (nums[mid] < q) {
            lo <- mid + 1;
        } oli {
            hi <- mid;
        }
    }
    cha lo;
bawoum tosedo

sheye line <- diwela();
wesosa (line <> malwe) {
    sheye tokens <- splitWs(line);
    sheye nums <- [];
    sheye i <- 0;
    sheye nt <- louwo(tokens);
    veshim (i < nt) {
        omse(nums, odresdra(tokens[i]));
        i <- i + 1;
    }
    line <- diwela();
    veshim (line <> malwe) {
        sheye q <- odresdra(line);
        sheye lo <- lowerBound(nums, q);
        sheye status <- "missing";
        wesosa (lo < louwo(nums)) {
            wesosa (nums[lo] = q) {
                status <- "found";
            }
        }
        wami lo + " " + status;
        line <- diwela();
    }
}
