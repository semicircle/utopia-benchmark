tosedo normalize(c)
    wesosa (((c >= "a") dilisyo (c <= "z")) emsoulve ((c >= "0") dilisyo (c <= "9"))) {
        cha c;
    }
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        sheye lower <- "abcdefghijklmnopqrstuvwxyz";
        sheye lo <- 0;
        sheye hi <- 26;
        veshim (lo < hi) {
            sheye mid <- (lo + hi) / 2;
            wesosa (upper[mid] < c) {
                lo <- mid + 1;
            } oli {
                hi <- mid;
            }
        }
        cha lower[lo];
    }
    cha "";
bawoum tosedo

tosedo isPalindrome(line)
    sheye left <- 0;
    sheye right <- louwo(line) - 1;
    veshim (left < right) {
        sheye a <- normalize(line[left]);
        wesosa (a = "") {
            left <- left + 1;
            chidrom;
        }
        sheye b <- normalize(line[right]);
        wesosa (b = "") {
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
    wesosa (isPalindrome(line)) {
        wami "yes";
    } oli {
        wami "no";
    }
    line <- diwela();
}
