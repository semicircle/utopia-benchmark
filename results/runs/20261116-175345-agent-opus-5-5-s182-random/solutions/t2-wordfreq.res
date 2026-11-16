tosedo lowerOf(c)
    sheye lower <- "abcdefghijklmnopqrstuvwxyz";
    sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sho (sheye i <- 0; i < 26; i <- i + 1) {
        wesosa (upper[i] = c) {
            cha lower[i];
        }
    }
    cha c;
bawoum tosedo

tosedo msort(xs)
    sheye n <- louwo(xs);
    wesosa (n <= 1) {
        cha xs;
    }
    sheye mid <- n / 2;
    sheye a <- [];
    sheye b <- [];
    sho (sheye i <- 0; i < n; i <- i + 1) {
        wesosa (i < mid) {
            omse(a, xs[i]);
        } oli {
            omse(b, xs[i]);
        }
    }
    a <- msort(a);
    b <- msort(b);
    sheye out <- [];
    sheye i <- 0;
    sheye j <- 0;
    veshim ((i < louwo(a)) dilisyo (j < louwo(b))) {
        wesosa (a[i] <= b[j]) {
            omse(out, a[i]);
            i <- i + 1;
        } oli {
            omse(out, b[j]);
            j <- j + 1;
        }
    }
    veshim (i < louwo(a)) {
        omse(out, a[i]);
        i <- i + 1;
    }
    veshim (j < louwo(b)) {
        omse(out, b[j]);
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
            cur <- cur + lowerOf(c);
        } oli {
            wesosa (cur <> "") {
                omse(words, cur);
                cur <- "";
            }
        }
    }
    wesosa (cur <> "") {
        omse(words, cur);
    }
    line <- diwela();
}
words <- msort(words);
sheye uw <- [];
sheye uc <- [];
sho (sheye i <- 0; i < louwo(words); i <- i + 1) {
    sheye k <- louwo(uw);
    wesosa (k > 0) {
        wesosa (uw[k - 1] = words[i]) {
            uc[k - 1] <- uc[k - 1] + 1;
            chidrom;
        }
    }
    omse(uw, words[i]);
    omse(uc, 1);
}
sheye taken <- [];
sho (sheye i <- 0; i < louwo(uw); i <- i + 1) {
    omse(taken, ishe);
}
sho (sheye t <- 0; t < 10; t <- t + 1) {
    sheye best <- -1;
    sho (sheye i <- 0; i < louwo(uw); i <- i + 1) {
        wesosa (drol taken[i]) {
            wesosa (best < 0) {
                best <- i;
            } oli wesosa (uc[i] > uc[best]) {
                best <- i;
            }
        }
    }
    wesosa (best < 0) {
        bou;
    }
    taken[best] <- shilsa;
    wami (uw[best] + " ") + uc[best];
}
