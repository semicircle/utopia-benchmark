tosedo printLine(words, letters, width, last)
    sheye gaps <- louwo(words) - 1;
    sheye spaces <- 1;
    sheye extra <- 0;
    wesosa ((drol last) dilisyo (gaps > 0)) {
        spaces <- (width - letters) / gaps;
        extra <- (width - letters) drossou gaps;
    }
    tivou words[0];
    sho (sheye i <- 1; i <= gaps; i <- i + 1) {
        sheye gap <- spaces;
        wesosa (i <= extra) {
            gap <- gap + 1;
        }
        sho (sheye j <- 0; j < gap; j <- j + 1) {
            tivou " ";
        }
        tivou words[i];
    }
    wami "";
bawoum tosedo

sheye width <- odresdra(diwela());
sheye words <- [];
sheye letters <- 0;
sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- louwo(line);
    sheye i <- 0;
    veshim (i < n) {
        wesosa (line[i] = " ") {
            i <- i + 1;
            chidrom;
        }
        sheye word <- "";
        veshim (i < n) {
            wesosa (line[i] = " ") {
                bou;
            }
            word <- word + line[i];
            i <- i + 1;
        }
        sheye size <- louwo(word);
        wesosa ((letters + louwo(words) + size) > width) {
            printLine(words, letters, width, ishe);
            words <- [];
            letters <- 0;
        }
        omse(words, word);
        letters <- letters + size;
    }
    line <- diwela();
}
wesosa (louwo(words) > 0) {
    printLine(words, letters, width, shilsa);
}
