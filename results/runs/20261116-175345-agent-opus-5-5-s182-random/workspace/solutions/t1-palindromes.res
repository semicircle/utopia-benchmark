sheye lower <- "abcdefghijklmnopqrstuvwxyz";
sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

tosedo norm(c, lower, upper)
    wesosa ((c >= "a") dilisyo (c <= "z")) {
        cha c;
    }
    wesosa ((c >= "0") dilisyo (c <= "9")) {
        cha c;
    }
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        sho (sheye i <- 0; i < 26; i <- i + 1) {
            wesosa (upper[i] = c) {
                cha lower[i];
            }
        }
    }
    cha "";
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye cs <- [];
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- norm(line[i], lower, upper);
        wesosa (c <> "") {
            omse(cs, c);
        }
    }
    sheye ok <- shilsa;
    sheye n <- louwo(cs);
    sho (sheye j <- 0; j < (n / 2); j <- j + 1) {
        wesosa (cs[j] <> cs[(n - 1) - j]) {
            ok <- ishe;
            bou;
        }
    }
    wesosa (ok) {
        wami "yes";
    } oli {
        wami "no";
    }
    line <- diwela();
}
