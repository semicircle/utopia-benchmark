tosedo lowerChar(c)
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sheye lo <- "abcdefghijklmnopqrstuvwxyz";
    sho (sheye i <- 0; i < 26; i <- i + 1) {
        wesosa (up[i] = c) {
            cha lo[i];
        }
    }
    cha c;
bawoum tosedo

tosedo isAlnum(c)
    wesosa ((c >= "0") dilisyo (c <= "9")) {
        cha shilsa;
    }
    wesosa ((c >= "a") dilisyo (c <= "z")) {
        cha shilsa;
    }
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        cha shilsa;
    }
    cha ishe;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye cs <- [];
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- line[i];
        wesosa (isAlnum(c)) {
            wesosa ((c >= "A") dilisyo (c <= "Z")) {
                c <- lowerChar(c);
            }
            omse(cs, c);
        }
    }
    sheye ok <- shilsa;
    sheye n <- louwo(cs);
    sho (i <- 0; i < (n / 2); i <- i + 1) {
        wesosa (cs[i] <> cs[(n - 1) - i]) {
            ok <- ishe;
        }
    }
    wesosa (ok) {
        wami "yes";
    } oli {
        wami "no";
    }
    line <- diwela();
}
