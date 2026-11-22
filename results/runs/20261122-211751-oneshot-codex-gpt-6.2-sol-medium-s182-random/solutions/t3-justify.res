tosedo writeLine(words, letters, width, last)
    sheye gaps <- louwo(words) - 1;
    tivou words[0];
    wesosa (gaps > 0) {
        sheye spaces <- 1;
        sheye extra <- 0;
        wesosa (drol last) {
            spaces <- (width - letters) / gaps;
            extra <- (width - letters) drossou gaps;
        }
        sho (sheye i <- 0; i < gaps; i <- i + 1) {
            sheye count <- spaces;
            wesosa (i < extra) {
                count <- count + 1;
            }
            sho (sheye j <- 0; j < count; j <- j + 1) {
                tivou " ";
            }
            tivou words[i + 1];
        }
    }
    wami "";
bawoum tosedo

sheye width <- odresdra(diwela());
sheye words <- [];
sheye letters <- 0;
sheye line <- diwela();
veshim (line <> malwe) {
    sheye i <- 0;
    veshim (i < louwo(line)) {
        wesosa (line[i] = " ") {
            i <- i + 1;
            chidrom;
        }
        sheye word <- "";
        veshim (i < louwo(line)) {
            wesosa (line[i] = " ") {
                bou;
            }
            word <- word + line[i];
            i <- i + 1;
        }
        wesosa ((letters + (louwo(words) + louwo(word))) > width) {
            writeLine(words, letters, width, ishe);
            words <- [];
            letters <- 0;
        }
        omse(words, word);
        letters <- letters + louwo(word);
    }
    line <- diwela();
}
wesosa (louwo(words) > 0) {
    writeLine(words, letters, width, shilsa);
}
