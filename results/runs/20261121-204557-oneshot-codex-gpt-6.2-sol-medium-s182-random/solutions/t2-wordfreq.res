tosedo lowerLetter(ch)
    wesosa ((ch >= "a") dilisyo (ch <= "z")) {
        cha ch;
    }
    wesosa ((ch < "A") emsoulve (ch > "Z")) {
        cha malwe;
    }
    sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sheye lower <- "abcdefghijklmnopqrstuvwxyz";
    sheye lo <- 0;
    sheye hi <- 26;
    veshim (lo < hi) {
        sheye mid <- (lo + hi) / 2;
        wesosa (upper[mid] < ch) {
            lo <- mid + 1;
        } oli {
            hi <- mid;
        }
    }
    cha lower[lo];
bawoum tosedo

' Each trie node holds its first child, next sibling, letter, count and word.
tosedo findChild(parent, letter)
    sheye child <- parent[0];
    veshim (child <> malwe) {
        wesosa (child[2] = letter) {
            cha child;
        }
        child <- child[1];
    }
    sheye added <- [malwe, parent[0], letter, 0, ""];
    parent[0] <- added;
    cha added;
bawoum tosedo

tosedo recordWord(node, word, entries)
    wesosa (node[3] = 0) {
        node[4] <- word;
        omse(entries, node);
    }
    node[3] <- node[3] + 1;
bawoum tosedo

sheye root <- [malwe, malwe, "", 0, ""];
sheye entries <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye node <- root;
    sheye word <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye letter <- lowerLetter(line[i]);
        wesosa (letter <> malwe) {
            node <- findChild(node, letter);
            word <- word + letter;
        } oli wesosa (node <> root) {
            recordWord(node, word, entries);
            node <- root;
            word <- "";
        }
    }
    wesosa (node <> root) {
        recordWord(node, word, entries);
    }
    line <- diwela();
}

sho (sheye printed <- 0; (printed < 10) dilisyo (printed < louwo(entries)); printed <- printed + 1) {
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
    tivou bestWord;
    wami " " + bestCount;
    best[3] <- 0;
}
