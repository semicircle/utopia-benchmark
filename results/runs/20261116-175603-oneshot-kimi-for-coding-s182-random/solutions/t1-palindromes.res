tosedo isletter(c)
    sheye lo <- "abcdefghijklmnopqrstuvwxyz";
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sho (sheye i <- 0; i < 26; i <- i + 1) {
        wesosa ((c = lo[i]) emsoulve (c = up[i])) {
            cha shilsa;
        }
    }
    cha ishe;
bawoum tosedo

tosedo lowerc(c)
    sheye lo <- "abcdefghijklmnopqrstuvwxyz";
    sheye up <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sho (sheye i <- 0; i < 26; i <- i + 1) {
        wesosa ((c = lo[i]) emsoulve (c = up[i])) {
            cha lo[i];
        }
    }
    cha c;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye f <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- line[i];
        wesosa (isletter(c)) {
            f <- f + lowerc(c);
        }
    }
    sheye ok <- shilsa;
    sho (sheye i <- 0; i < louwo(f); i <- i + 1) {
        wesosa (f[i] <> f[((louwo(f) - 1) - i)]) {
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
