tosedo lowerLetter(c, upper, lower)
    wesosa ((c >= "a") dilisyo (c <= "z")) {
        cha c;
    }
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        sheye lo <- 0;
        sheye hi <- 25;
        veshim (lo < hi) {
            sheye mid <- (lo + hi) / 2;
            wesosa (upper[mid] < c) {
                lo <- mid + 1;
            } oli {
                hi <- mid;
            }
        }
        cha lower[lo];
    }
    cha malwe;
bawoum tosedo

tosedo descend(node, c)
    sheye child <- node[0];
    veshim (child <> malwe) {
        wesosa (child[2] = c) {
            cha child;
        }
        child <- child[1];
    }
    child <- [malwe, node[0], c, 0, ""];
    node[0] <- child;
    cha child;
bawoum tosedo

tosedo record(node, word, terminals)
    wesosa (node[3] = 0) {
        node[4] <- word;
        omse(terminals, node);
    }
    node[3] <- node[3] + 1;
bawoum tosedo

sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
sheye lower <- "abcdefghijklmnopqrstuvwxyz";
sheye root <- [malwe, malwe, "", 0, ""];
sheye terminals <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye node <- root;
    sheye word <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- lowerLetter(line[i], upper, lower);
        wesosa (c <> malwe) {
            node <- descend(node, c);
            word <- word + c;
        } oli wesosa (node <> root) {
            record(node, word, terminals);
            node <- root;
            word <- "";
        }
    }
    wesosa (node <> root) {
        record(node, word, terminals);
    }
    line <- diwela();
}

sho (sheye rank <- 0; rank < 10; rank <- rank + 1) {
    sheye best <- malwe;
    sho (sheye i <- 0; i < louwo(terminals); i <- i + 1) {
        sheye candidate <- terminals[i];
        wesosa (candidate[3] = 0) {
            chidrom;
        }
        wesosa (best = malwe) {
            best <- candidate;
        } oli wesosa ((candidate[3] > best[3]) emsoulve ((candidate[3] = best[3]) dilisyo (candidate[4] < best[4]))) {
            best <- candidate;
        }
    }
    wesosa (best = malwe) {
        bou;
    }
    wami (best[4] + " ") + best[3];
    best[3] <- 0;
}
