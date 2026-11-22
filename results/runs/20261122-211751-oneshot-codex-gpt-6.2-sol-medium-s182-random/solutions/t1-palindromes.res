tosedo normalize(c)
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        sheye lower <- "abcdefghijklmnopqrstuvwxyz";
        sheye i <- 0;
        veshim (upper[i] <> c) {
            i <- i + 1;
        }
        cha lower[i];
    }
    wesosa (((c >= "a") dilisyo (c <= "z")) emsoulve ((c >= "0") dilisyo (c <= "9"))) {
        cha c;
    }
    cha malwe;
bawoum tosedo

tosedo palindrome(line)
    sheye left <- 0;
    sheye right <- louwo(line) - 1;
    veshim (left < right) {
        sheye a <- normalize(line[left]);
        wesosa (a = malwe) {
            left <- left + 1;
            chidrom;
        }
        sheye b <- normalize(line[right]);
        wesosa (b = malwe) {
            right <- right - 1;
            chidrom;
        }
        wesosa (a <> b) {
            cha ishe;
        }
        left <- left + 1;
        right <- right - 1;
    }
    cha shilsa;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (palindrome(line)) {
        wami "yes";
    } oli {
        wami "no";
    }
    line <- diwela();
}
