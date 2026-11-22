tosedo normalize(c, upper, lower)
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        sheye lo <- 0;
        sheye hi <- 25;
        veshim (lo <= hi) {
            sheye mid <- (lo + hi) / 2;
            wesosa (c = upper[mid]) {
                cha lower[mid];
            } oli wesosa (c < upper[mid]) {
                hi <- mid - 1;
            } oli {
                lo <- mid + 1;
            }
        }
    }
    wesosa (((c >= "a") dilisyo (c <= "z")) emsoulve ((c >= "0") dilisyo (c <= "9"))) {
        cha c;
    }
    cha malwe;
bawoum tosedo

sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
sheye lower <- "abcdefghijklmnopqrstuvwxyz";
sheye line <- diwela();
veshim (line <> malwe) {
    sheye chars <- [];
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- normalize(line[i], upper, lower);
        wesosa (c <> malwe) {
            omse(chars, c);
        }
    }
    sheye yes <- shilsa;
    sheye j <- louwo(chars) - 1;
    sho (sheye i <- 0; i < j; i <- i + 1) {
        wesosa (chars[i] <> chars[j]) {
            yes <- ishe;
            bou;
        }
        j <- j - 1;
    }
    wesosa (yes) {
        wami "yes";
    } oli {
        wami "no";
    }
    line <- diwela();
}
