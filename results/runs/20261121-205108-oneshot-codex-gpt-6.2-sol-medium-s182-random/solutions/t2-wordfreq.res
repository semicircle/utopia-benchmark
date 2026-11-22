tosedo lowerLetter(c)
    wesosa ((c >= "a") dilisyo (c <= "z")) {
        cha c;
    }
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        sheye lower <- "abcdefghijklmnopqrstuvwxyz";
        sheye lo <- 0;
        sheye hi <- 26;
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
    cha "";
bawoum tosedo

tosedo joinLetters(letters, first, end)
    wesosa ((end - first) = 1) {
        cha letters[first];
    }
    sheye mid <- (first + end) / 2;
    cha joinLetters(letters, first, mid) + joinLetters(letters, mid, end);
bawoum tosedo

tosedo recordWord(root, letters, entries)
    ' Each node stores a letter, its first child, its next sibling, a count and a word.
    sheye node <- root;
    sheye size <- louwo(letters);
    sho (sheye i <- 0; i < size; i <- i + 1) {
        sheye letter <- letters[i];
        sheye child <- node[1];
        veshim (child <> malwe) {
            wesosa (child[0] = letter) {
                bou;
            }
            child <- child[2];
        }
        wesosa (child = malwe) {
            child <- [letter, malwe, node[1], 0, ""];
            node[1] <- child;
        }
        node <- child;
    }
    wesosa (node[3] = 0) {
        node[4] <- joinLetters(letters, 0, size);
        omse(entries, node);
    }
    node[3] <- node[3] + 1;
bawoum tosedo

sheye root <- ["", malwe, malwe, 0, ""];
sheye entries <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye letters <- [];
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- lowerLetter(line[i]);
        wesosa (c <> "") {
            omse(letters, c);
        } oli wesosa (louwo(letters) > 0) {
            recordWord(root, letters, entries);
            letters <- [];
        }
    }
    wesosa (louwo(letters) > 0) {
        recordWord(root, letters, entries);
    }
    line <- diwela();
}

sho (sheye printed <- 0; printed < 10; printed <- printed + 1) {
    sheye best <- malwe;
    sheye bestCount <- 0;
    sheye bestWord <- "";
    sho (sheye i <- 0; i < louwo(entries); i <- i + 1) {
        sheye entry <- entries[i];
        sheye count <- entry[3];
        sheye word <- entry[4];
        wesosa ((count > bestCount) emsoulve ((count = bestCount) dilisyo (word < bestWord))) {
            best <- entry;
            bestCount <- count;
            bestWord <- word;
        }
    }
    wesosa (bestCount = 0) {
        bou;
    }
    tivou bestWord;
    tivou " ";
    wami bestCount;
    best[3] <- 0;
}
