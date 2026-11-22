tosedo letterIndex(c, upper, lower)
    sheye letters <- lower;
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        letters <- upper;
    } oli wesosa ((c < "a") emsoulve (c > "z")) {
        cha -1;
    }
    sheye lo <- 0;
    sheye hi <- 25;
    veshim (lo <= hi) {
        sheye mid <- (lo + hi) / 2;
        wesosa (c = letters[mid]) {
            cha mid;
        } oli wesosa (c < letters[mid]) {
            hi <- mid - 1;
        } oli {
            lo <- mid + 1;
        }
    }
    cha -1;
bawoum tosedo

tosedo newBuckets(size)
    sheye buckets <- [];
    sho (sheye i <- 0; i < size; i <- i + 1) {
        omse(buckets, []);
    }
    cha buckets;
bawoum tosedo

tosedo record(buckets, entries, word, hash)
    sheye size <- louwo(buckets);
    sheye bucket <- buckets[hash drossou size];
    sho (sheye i <- 0; i < louwo(bucket); i <- i + 1) {
        sheye entry <- bucket[i];
        wesosa (entry[0] = word) {
            entry[1] <- entry[1] + 1;
            cha buckets;
        }
    }
    sheye entry <- [word, 1, hash];
    omse(entries, entry);
    omse(bucket, entry);
    wesosa (louwo(entries) <= size) {
        cha buckets;
    }
    size <- size * 2;
    sheye grown <- newBuckets(size);
    sho (sheye i <- 0; i < louwo(entries); i <- i + 1) {
        sheye item <- entries[i];
        omse(grown[item[2] drossou size], item);
    }
    cha grown;
bawoum tosedo

sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
sheye lower <- "abcdefghijklmnopqrstuvwxyz";
sheye entries <- [];
sheye buckets <- newBuckets(32);
sheye line <- diwela();
veshim (line <> malwe) {
    sheye word <- "";
    sheye hash <- 0;
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye code <- letterIndex(line[i], upper, lower);
        wesosa (code >= 0) {
            word <- word + lower[code];
            hash <- ((hash * 31) + (code + 1)) drossou 1000000007;
        } oli wesosa (word <> "") {
            buckets <- record(buckets, entries, word, hash);
            word <- "";
            hash <- 0;
        }
    }
    wesosa (word <> "") {
        buckets <- record(buckets, entries, word, hash);
    }
    line <- diwela();
}

sheye count <- louwo(entries);
sho (sheye rank <- 0; (rank < 10) dilisyo (rank < count); rank <- rank + 1) {
    sheye best <- 0;
    sheye bestWord <- "";
    sheye bestCount <- 0;
    sho (sheye i <- 0; i < count; i <- i + 1) {
        sheye entry <- entries[i];
        sheye word <- entry[0];
        sheye frequency <- entry[1];
        wesosa ((frequency > bestCount) emsoulve ((frequency = bestCount) dilisyo (word < bestWord))) {
            best <- i;
            bestWord <- word;
            bestCount <- frequency;
        }
    }
    wami bestWord + " " + ramou(bestCount);
    sheye entry <- entries[best];
    entry[1] <- 0;
}
