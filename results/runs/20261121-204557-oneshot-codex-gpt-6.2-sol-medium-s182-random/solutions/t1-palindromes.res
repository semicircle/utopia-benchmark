tosedo normalized(ch)
    wesosa ((ch >= "A") dilisyo (ch <= "Z")) {
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
    }
    wesosa (((ch >= "a") dilisyo (ch <= "z")) emsoulve ((ch >= "0") dilisyo (ch <= "9"))) {
        cha ch;
    }
    cha malwe;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye chars <- [];
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye ch <- normalized(line[i]);
        wesosa (ch <> malwe) {
            omse(chars, ch);
        }
    }
    sheye result <- "yes";
    sheye last <- louwo(chars) - 1;
    sho (sheye i <- 0; i < (last - i); i <- i + 1) {
        wesosa (chars[i] <> chars[last - i]) {
            result <- "no";
            bou;
        }
    }
    wami result;
    line <- diwela();
}
