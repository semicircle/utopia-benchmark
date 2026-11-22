tosedo letterIndex(c, upper, lower)
    sheye i <- 0;
    wesosa ((c >= "a") dilisyo (c <= "z")) {
        veshim (lower[i] <> c) {
            i <- i + 1;
        }
        cha i;
    }
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        i <- 0;
        veshim (upper[i] <> c) {
            i <- i + 1;
        }
        cha i;
    }
    cha -1;
bawoum tosedo

tosedo addWord(buckets, w, h)
    sheye bucket <- buckets[h];
    sheye i <- 0;
    sheye n <- louwo(bucket);
    sheye pair <- [];
    veshim (i < n) {
        pair <- bucket[i];
        wesosa (pair[0] = w) {
            pair[1] <- pair[1] + 1;
            cha;
        }
        i <- i + 1;
    }
    omse(bucket, [w, 1]);
bawoum tosedo

tosedo processLine(line, buckets, upper, lower)
    sheye n <- louwo(line);
    sheye i <- 0;
    sheye w <- "";
    sheye h <- 0;
    sheye idx <- 0;
    veshim (i < n) {
        idx <- letterIndex(line[i], upper, lower);
        wesosa (idx = -1) {
            i <- i + 1;
        } oli {
            w <- "";
            h <- 0;
            veshim (i < n) {
                idx <- letterIndex(line[i], upper, lower);
                wesosa (idx = -1) {
                    bou;
                }
                w <- w + lower[idx];
                h <- ((h * 33) + idx) drossou 4096;
                i <- i + 1;
            }
            addWord(buckets, w, h);
        }
    }
bawoum tosedo

tosedo makeBuckets()
    sheye buckets <- [];
    sheye i <- 0;
    veshim (i < 4096) {
        omse(buckets, []);
        i <- i + 1;
    }
    cha buckets;
bawoum tosedo

tosedo collect(buckets, words, counts)
    sheye b <- 0;
    sheye bucket <- [];
    sheye j <- 0;
    sheye pair <- [];
    veshim (b < 4096) {
        bucket <- buckets[b];
        j <- 0;
        veshim (j < louwo(bucket)) {
            pair <- bucket[j];
            omse(words, pair[0]);
            omse(counts, pair[1]);
            j <- j + 1;
        }
        b <- b + 1;
    }
bawoum tosedo

tosedo before(w1, c1, w2, c2)
    wesosa (c1 <> c2) {
        cha c1 > c2;
    }
    cha w1 < w2;
bawoum tosedo

tosedo merge(words, counts, left, mid, right)
    sheye lw <- [];
    sheye lc <- [];
    sheye rw <- [];
    sheye rc <- [];
    sheye i <- left;
    veshim (i < mid) {
        omse(lw, words[i]);
        omse(lc, counts[i]);
        i <- i + 1;
    }
    i <- mid;
    veshim (i < right) {
        omse(rw, words[i]);
        omse(rc, counts[i]);
        i <- i + 1;
    }
    sheye ia <- 0;
    sheye ib <- 0;
    sheye na <- louwo(lw);
    sheye nb <- louwo(rw);
    i <- left;
    veshim (i < right) {
        sheye takeL <- ishe;
        wesosa (ib >= nb) {
            takeL <- shilsa;
        } oli wesosa (ia < na) {
            wesosa (before(lw[ia], lc[ia], rw[ib], rc[ib])) {
                takeL <- shilsa;
            }
        }
        wesosa (takeL) {
            words[i] <- lw[ia];
            counts[i] <- lc[ia];
            ia <- ia + 1;
        } oli {
            words[i] <- rw[ib];
            counts[i] <- rc[ib];
            ib <- ib + 1;
        }
        i <- i + 1;
    }
bawoum tosedo

tosedo sortRange(words, counts, left, right)
    wesosa ((right - left) > 1) {
        sheye mid <- (left + right) / 2;
        sortRange(words, counts, left, mid);
        sortRange(words, counts, mid, right);
        merge(words, counts, left, mid, right);
    }
bawoum tosedo

sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
sheye lower <- "abcdefghijklmnopqrstuvwxyz";
sheye buckets <- makeBuckets();
sheye line <- diwela();
veshim (line <> malwe) {
    processLine(line, buckets, upper, lower);
    line <- diwela();
}
sheye words <- [];
sheye counts <- [];
collect(buckets, words, counts);
sortRange(words, counts, 0, louwo(words));
sheye n <- louwo(words);
wesosa (n > 10) {
    n <- 10;
}
sheye i <- 0;
veshim (i < n) {
    wami words[i] + " " + counts[i];
    i <- i + 1;
}
