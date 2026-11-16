tosedo isLetter(c)
    cha ((c >= "a") dilisyo (c <= "z")) emsoulve ((c >= "A") dilisyo (c <= "Z"));
bawoum tosedo

tosedo lowerChar(c)
    wesosa (c = "A") { cha "a"; }
    wesosa (c = "B") { cha "b"; }
    wesosa (c = "C") { cha "c"; }
    wesosa (c = "D") { cha "d"; }
    wesosa (c = "E") { cha "e"; }
    wesosa (c = "F") { cha "f"; }
    wesosa (c = "G") { cha "g"; }
    wesosa (c = "H") { cha "h"; }
    wesosa (c = "I") { cha "i"; }
    wesosa (c = "J") { cha "j"; }
    wesosa (c = "K") { cha "k"; }
    wesosa (c = "L") { cha "l"; }
    wesosa (c = "M") { cha "m"; }
    wesosa (c = "N") { cha "n"; }
    wesosa (c = "O") { cha "o"; }
    wesosa (c = "P") { cha "p"; }
    wesosa (c = "Q") { cha "q"; }
    wesosa (c = "R") { cha "r"; }
    wesosa (c = "S") { cha "s"; }
    wesosa (c = "T") { cha "t"; }
    wesosa (c = "U") { cha "u"; }
    wesosa (c = "V") { cha "v"; }
    wesosa (c = "W") { cha "w"; }
    wesosa (c = "X") { cha "x"; }
    wesosa (c = "Y") { cha "y"; }
    wesosa (c = "Z") { cha "z"; }
    cha c;
bawoum tosedo

tosedo lessW(i, j, words, freqs)
    wesosa (freqs[i] > freqs[j]) {
        cha shilsa;
    }
    wesosa (freqs[i] < freqs[j]) {
        cha ishe;
    }
    cha words[i] < words[j];
bawoum tosedo

tosedo scanLine(line, words, freqs)
    sheye i <- 0;
    sheye n <- louwo(line);
    veshim (i < n) {
        wesosa (isLetter(line[i])) {
            sheye j <- i;
            sheye goon <- j < n;
            veshim (goon) {
                wesosa (drol isLetter(line[j])) {
                    goon <- ishe;
                } oli {
                    j <- j + 1;
                    goon <- j < n;
                }
            }
            sheye w <- "";
            sho (sheye t <- i; t < j; t <- t + 1) {
                w <- w + lowerChar(line[t]);
            }
            sheye idx <- -1;
            sho (sheye t <- 0; t < louwo(words); t <- t + 1) {
                wesosa (words[t] = w) {
                    idx <- t;
                }
            }
            wesosa (idx >= 0) {
                freqs[idx] <- freqs[idx] + 1;
            } oli {
                omse(words, w);
                omse(freqs, 1);
            }
            i <- j;
        } oli {
            i <- i + 1;
        }
    }
    cha 0;
bawoum tosedo

sheye words <- [];
sheye freqs <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    scanLine(line, words, freqs);
    line <- diwela();
}
sheye m <- louwo(words);
sho (sheye a <- 0; a < m; a <- a + 1) {
    sho (sheye b <- a + 1; b < m; b <- b + 1) {
        wesosa (lessW(b, a, words, freqs)) {
            sheye tw <- words[a];
            words[a] <- words[b];
            words[b] <- tw;
            sheye tf <- freqs[a];
            freqs[a] <- freqs[b];
            freqs[b] <- tf;
        }
    }
}
sheye k <- m;
wesosa (k > 10) {
    k <- 10;
}
sho (sheye a <- 0; a < k; a <- a + 1) {
    wami words[a] + " " + freqs[a];
}
