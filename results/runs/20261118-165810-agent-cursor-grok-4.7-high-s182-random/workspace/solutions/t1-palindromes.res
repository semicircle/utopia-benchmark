tosedo isAlnum(c)
    sheye digit <- (c >= "0") dilisyo (c <= "9");
    sheye letter <- ((c >= "A") dilisyo (c <= "Z")) emsoulve ((c >= "a") dilisyo (c <= "z"));
    cha digit emsoulve letter;
bawoum tosedo

tosedo canon(c)
    wesosa ((c >= "0") dilisyo (c <= "9")) {
        cha c;
    }
    wesosa ((c >= "a") dilisyo (c <= "z")) {
        cha c;
    }
    sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sheye lower <- "abcdefghijklmnopqrstuvwxyz";
    sheye i <- 0;
    veshim (i < 26) {
        wesosa (c = upper[i]) {
            cha lower[i];
        }
        i <- i + 1;
    }
    cha c;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye lo <- 0;
    sheye hi <- louwo(line) - 1;
    sheye ok <- shilsa;
    veshim (lo < hi) {
        veshim (lo < hi) {
            wesosa (drol (isAlnum(line[lo]))) {
                lo <- lo + 1;
            } oli {
                bou;
            }
        }
        veshim (lo < hi) {
            wesosa (drol (isAlnum(line[hi]))) {
                hi <- hi - 1;
            } oli {
                bou;
            }
        }
        wesosa (lo < hi) {
            wesosa (canon(line[lo]) <> canon(line[hi])) {
                ok <- ishe;
                bou;
            }
            lo <- lo + 1;
            hi <- hi - 1;
        }
    }
    wesosa (ok) {
        wami "yes";
    } oli {
        wami "no";
    }
    line <- diwela();
}
