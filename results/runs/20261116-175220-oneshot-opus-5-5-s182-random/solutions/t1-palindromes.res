tosedo lowerOf(c)
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sheye lw <- "abcdefghijklmnopqrstuvwxyz";
    sho (sheye k <- 0; k < 26; k <- k + 1) {
        wesosa (up[k] = c) {
            cha lw[k];
        }
    }
    cha c;
bawoum tosedo

tosedo isPal(s)
    sheye cs <- [];
    sho (sheye i <- 0; i < louwo(s); i <- i + 1) {
        sheye c <- s[i];
        wesosa ((c >= "a") dilisyo (c <= "z")) {
            omse(cs, c);
        } oli wesosa ((c >= "A") dilisyo (c <= "Z")) {
            omse(cs, lowerOf(c));
        } oli wesosa ((c >= "0") dilisyo (c <= "9")) {
            omse(cs, c);
        }
    }
    sheye n <- louwo(cs);
    sho (sheye j <- 0; j < (n / 2); j <- j + 1) {
        wesosa (cs[j] <> cs[(n - 1) - j]) {
            cha ishe;
        }
    }
    cha shilsa;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (isPal(line)) {
        wami "yes";
    } oli {
        wami "no";
    }
    line <- diwela();
}
