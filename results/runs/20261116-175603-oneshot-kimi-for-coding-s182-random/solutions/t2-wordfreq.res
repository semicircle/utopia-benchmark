tosedo isletter(c)
    sheye lo <- "abcdefghijklmnopqrstuvwxyz";
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sho (sheye i <- 0; i < 26; i <- i + 1) {
        wesosa ((c = lo[i]) emsoulve (c = up[i])) {
            cha shilsa;
        }
    }
    cha ishe;
bawoum tosedo

tosedo lowerc(c)
    sheye lo <- "abcdefghijklmnopqrstuvwxyz";
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sho (sheye i <- 0; i < 26; i <- i + 1) {
        wesosa ((c = lo[i]) emsoulve (c = up[i])) {
            cha lo[i];
        }
    }
    cha c;
bawoum tosedo

tosedo addword(words, counts, w)
    sho (sheye i <- 0; i < louwo(words); i <- i + 1) {
        wesosa (words[i] = w) {
            counts[i] <- counts[i] + 1;
            cha;
        }
    }
    omse(words, w);
    omse(counts, 1);
bawoum tosedo

sheye words <- [];
sheye counts <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye cur <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        wesosa (isletter(line[i])) {
            cur <- cur + lowerc(line[i]);
        } oli {
            wesosa (louwo(cur) > 0) {
                addword(words, counts, cur);
                cur <- "";
            }
        }
    }
    wesosa (louwo(cur) > 0) {
        addword(words, counts, cur);
    }
    line <- diwela();
}
sheye n <- louwo(words);
sho (sheye k <- 0; (k < 10) dilisyo (k < n); k <- k + 1) {
    sheye bi <- -1;
    sho (sheye i <- 0; i < n; i <- i + 1) {
        wesosa (counts[i] < 0) {
            chidrom;
        }
        wesosa (bi < 0) {
            bi <- i;
        } oli wesosa ((counts[i] > counts[bi]) emsoulve ((counts[i] = counts[bi]) dilisyo (words[i] < words[bi]))) {
            bi <- i;
        }
    }
    wami words[bi] + " " + counts[bi];
    counts[bi] <- -1;
}
