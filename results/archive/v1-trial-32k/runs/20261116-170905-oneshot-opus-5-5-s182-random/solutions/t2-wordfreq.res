tosedo lowerChar(c)
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sheye lo <- "abcdefghijklmnopqrstuvwxyz";
    sho (sheye i <- 0; i < 26; i <- i + 1) {
        wesosa (up[i] = c) {
            cha lo[i];
        }
    }
    cha c;
bawoum tosedo

tosedo less(x, y, mode)
    wesosa (mode = 1) {
        cha x < y;
    }
    sheye cx <- x[1];
    sheye cy <- y[1];
    wesosa (cx <> cy) {
        cha cx > cy;
    }
    sheye wx <- x[0];
    sheye wy <- y[0];
    cha wx < wy;
bawoum tosedo

tosedo msort(xs, mode)
    sheye n <- louwo(xs);
    wesosa (n <= 1) {
        cha xs;
    }
    sheye mid <- n / 2;
    sheye left <- [];
    sheye right <- [];
    sho (sheye i <- 0; i < n; i <- i + 1) {
        wesosa (i < mid) {
            omse(left, xs[i]);
        } oli {
            omse(right, xs[i]);
        }
    }
    left <- msort(left, mode);
    right <- msort(right, mode);
    sheye out <- [];
    i <- 0;
    sheye j <- 0;
    sheye ln <- louwo(left);
    sheye rn <- louwo(right);
    veshim ((i < ln) dilisyo (j < rn)) {
        wesosa (less(right[j], left[i], mode)) {
            omse(out, right[j]);
            j <- j + 1;
        } oli {
            omse(out, left[i]);
            i <- i + 1;
        }
    }
    veshim (i < ln) {
        omse(out, left[i]);
        i <- i + 1;
    }
    veshim (j < rn) {
        omse(out, right[j]);
        j <- j + 1;
    }
    cha out;
bawoum tosedo

sheye words <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye cur <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- line[i];
        wesosa ((c >= "a") dilisyo (c <= "z")) {
            cur <- cur + c;
        } oli wesosa ((c >= "A") dilisyo (c <= "Z")) {
            cur <- cur + lowerChar(c);
        } oli {
            wesosa (louwo(cur) > 0) {
                omse(words, cur);
                cur <- "";
            }
        }
    }
    wesosa (louwo(cur) > 0) {
        omse(words, cur);
    }
    line <- diwela();
}
sheye sorted <- msort(words, 1);
sheye pairs <- [];
sheye n <- louwo(sorted);
sheye k <- 0;
veshim (k < n) {
    sheye w <- sorted[k];
    sheye cnt <- 0;
    veshim (k < n) {
        wesosa (sorted[k] <> w) {
            bou;
        }
        cnt <- cnt + 1;
        k <- k + 1;
    }
    omse(pairs, [w, cnt]);
}
sheye ps <- msort(pairs, 2);
sheye lim <- louwo(ps);
wesosa (lim > 10) {
    lim <- 10;
}
sho (sheye q <- 0; q < lim; q <- q + 1) {
    sheye p <- ps[q];
    wami (p[0] + " ") + p[1];
}
