tosedo lowerOf(c)
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sheye lw <- "abcdefghijklmnopqrstuvwxyz";
    sho (sheye k <- 0; k < 26; k <- k + 1) {
        wesosa (up[k] = c) {
            cha lw[k];
        }
    }
    cha c;
bawoum tosedo

tosedo msort(a, lo, hi, tmp)
    wesosa ((hi - lo) < 2) {
        cha;
    }
    sheye mid <- (lo + hi) / 2;
    msort(a, lo, mid, tmp);
    msort(a, mid, hi, tmp);
    sheye i <- lo;
    sheye j <- mid;
    sheye k <- lo;
    veshim ((i < mid) dilisyo (j < hi)) {
        wesosa (a[j] < a[i]) {
            tmp[k] <- a[j];
            j <- j + 1;
        } oli {
            tmp[k] <- a[i];
            i <- i + 1;
        }
        k <- k + 1;
    }
    veshim (i < mid) {
        tmp[k] <- a[i];
        i <- i + 1;
        k <- k + 1;
    }
    veshim (j < hi) {
        tmp[k] <- a[j];
        j <- j + 1;
        k <- k + 1;
    }
    sho (k <- lo; k < hi; k <- k + 1) {
        a[k] <- tmp[k];
    }
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
            cur <- cur + lowerOf(c);
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
sheye n <- louwo(words);
sheye tmp <- [];
sho (sheye i <- 0; i < n; i <- i + 1) {
    omse(tmp, "");
}
msort(words, 0, n, tmp);
sheye W <- [];
sheye C <- [];
sho (sheye i <- 0; i < n; i <- i + 1) {
    sheye m <- louwo(W);
    wesosa (m > 0) {
        wesosa (W[m - 1] = words[i]) {
            C[m - 1] <- C[m - 1] + 1;
        } oli {
            omse(W, words[i]);
            omse(C, 1);
        }
    } oli {
        omse(W, words[i]);
        omse(C, 1);
    }
}
sheye d <- louwo(W);
sheye used <- [];
sho (sheye i <- 0; i < d; i <- i + 1) {
    omse(used, ishe);
}
sheye rounds <- 10;
wesosa (d < 10) {
    rounds <- d;
}
sho (sheye r <- 0; r < rounds; r <- r + 1) {
    sheye best <- -1;
    sheye bc <- -1;
    sho (sheye i <- 0; i < d; i <- i + 1) {
        wesosa (used[i] = ishe) {
            wesosa (C[i] > bc) {
                best <- i;
                bc <- C[i];
            }
        }
    }
    used[best] <- shilsa;
    wami (W[best] + " ") + ramou(C[best]);
}
