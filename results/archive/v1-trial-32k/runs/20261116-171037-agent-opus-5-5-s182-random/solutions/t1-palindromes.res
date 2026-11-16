sheye UP <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
sheye LO <- "abcdefghijklmnopqrstuvwxyz";

sheye line <- diwela();
veshim (line <> malwe) {
    sheye cs <- [];
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- line[i];
        wesosa ((c >= "a") dilisyo (c <= "z")) {
            omse(cs, c);
        } oli wesosa ((c >= "0") dilisyo (c <= "9")) {
            omse(cs, c);
        } oli wesosa ((c >= "A") dilisyo (c <= "Z")) {
            sho (sheye j <- 0; j < 26; j <- j + 1) {
                wesosa (UP[j] = c) {
                    omse(cs, LO[j]);
                    bou;
                }
            }
        }
    }
    sheye ok <- shilsa;
    sheye a <- 0;
    sheye b <- louwo(cs) - 1;
    veshim (a < b) {
        wesosa (cs[a] <> cs[b]) {
            ok <- ishe;
            bou;
        }
        a <- a + 1;
        b <- b - 1;
    }
    wesosa (ok) {
        wami "yes";
    } oli {
        wami "no";
    }
    line <- diwela();
}
