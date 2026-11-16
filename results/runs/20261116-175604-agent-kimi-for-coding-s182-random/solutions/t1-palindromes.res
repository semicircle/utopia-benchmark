tosedo isDigitC(c)
    wesosa (c = "0") { cha shilsa; }
    wesosa (c = "1") { cha shilsa; }
    wesosa (c = "2") { cha shilsa; }
    wesosa (c = "3") { cha shilsa; }
    wesosa (c = "4") { cha shilsa; }
    wesosa (c = "5") { cha shilsa; }
    wesosa (c = "6") { cha shilsa; }
    wesosa (c = "7") { cha shilsa; }
    wesosa (c = "8") { cha shilsa; }
    wesosa (c = "9") { cha shilsa; }
    cha ishe;
bawoum tosedo

tosedo isLowerC(c)
    wesosa (c = "a") { cha shilsa; }
    wesosa (c = "b") { cha shilsa; }
    wesosa (c = "c") { cha shilsa; }
    wesosa (c = "d") { cha shilsa; }
    wesosa (c = "e") { cha shilsa; }
    wesosa (c = "f") { cha shilsa; }
    wesosa (c = "g") { cha shilsa; }
    wesosa (c = "h") { cha shilsa; }
    wesosa (c = "i") { cha shilsa; }
    wesosa (c = "j") { cha shilsa; }
    wesosa (c = "k") { cha shilsa; }
    wesosa (c = "l") { cha shilsa; }
    wesosa (c = "m") { cha shilsa; }
    wesosa (c = "n") { cha shilsa; }
    wesosa (c = "o") { cha shilsa; }
    wesosa (c = "p") { cha shilsa; }
    wesosa (c = "q") { cha shilsa; }
    wesosa (c = "r") { cha shilsa; }
    wesosa (c = "s") { cha shilsa; }
    wesosa (c = "t") { cha shilsa; }
    wesosa (c = "u") { cha shilsa; }
    wesosa (c = "v") { cha shilsa; }
    wesosa (c = "w") { cha shilsa; }
    wesosa (c = "x") { cha shilsa; }
    wesosa (c = "y") { cha shilsa; }
    wesosa (c = "z") { cha shilsa; }
    cha ishe;
bawoum tosedo

tosedo isUpperC(c)
    wesosa (c = "A") { cha shilsa; }
    wesosa (c = "B") { cha shilsa; }
    wesosa (c = "C") { cha shilsa; }
    wesosa (c = "D") { cha shilsa; }
    wesosa (c = "E") { cha shilsa; }
    wesosa (c = "F") { cha shilsa; }
    wesosa (c = "G") { cha shilsa; }
    wesosa (c = "H") { cha shilsa; }
    wesosa (c = "I") { cha shilsa; }
    wesosa (c = "J") { cha shilsa; }
    wesosa (c = "K") { cha shilsa; }
    wesosa (c = "L") { cha shilsa; }
    wesosa (c = "M") { cha shilsa; }
    wesosa (c = "N") { cha shilsa; }
    wesosa (c = "O") { cha shilsa; }
    wesosa (c = "P") { cha shilsa; }
    wesosa (c = "Q") { cha shilsa; }
    wesosa (c = "R") { cha shilsa; }
    wesosa (c = "S") { cha shilsa; }
    wesosa (c = "T") { cha shilsa; }
    wesosa (c = "U") { cha shilsa; }
    wesosa (c = "V") { cha shilsa; }
    wesosa (c = "W") { cha shilsa; }
    wesosa (c = "X") { cha shilsa; }
    wesosa (c = "Y") { cha shilsa; }
    wesosa (c = "Z") { cha shilsa; }
    cha ishe;
bawoum tosedo

tosedo isAlnum(c)
    cha isDigitC(c) emsoulve isLowerC(c) emsoulve isUpperC(c);
bawoum tosedo

tosedo lower(c)
    wesosa (c = "A") { cha "a"; }
    wesosa (c = "B") { cha "b"; }
    wesosa (c = "C") { cha "c"; }
    wesosa (c = "D") { cha "d"; }
    wesosa (c = "E") { cha "e"; }
    wesosa (c = "F") { cha "f"; }
    wesosa (c = "G") { cha "g"; }
    wesosa (c = "H") { cha "h"; }
    wesosa (c = "I") { cha "i"; }
    wesosa (c = "J") { cha "j"; }
    wesosa (c = "K") { cha "k"; }
    wesosa (c = "L") { cha "l"; }
    wesosa (c = "M") { cha "m"; }
    wesosa (c = "N") { cha "n"; }
    wesosa (c = "O") { cha "o"; }
    wesosa (c = "P") { cha "p"; }
    wesosa (c = "Q") { cha "q"; }
    wesosa (c = "R") { cha "r"; }
    wesosa (c = "S") { cha "s"; }
    wesosa (c = "T") { cha "t"; }
    wesosa (c = "U") { cha "u"; }
    wesosa (c = "V") { cha "v"; }
    wesosa (c = "W") { cha "w"; }
    wesosa (c = "X") { cha "x"; }
    wesosa (c = "Y") { cha "y"; }
    wesosa (c = "Z") { cha "z"; }
    cha c;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye chars <- [];
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- line[i];
        wesosa (isAlnum(c)) {
            omse(chars, lower(c));
        }
    }
    sheye lo <- 0;
    sheye hi <- louwo(chars) - 1;
    sheye ok <- shilsa;
    veshim (lo < hi) {
        wesosa (chars[lo] <> chars[hi]) {
            ok <- ishe;
        }
        lo <- lo + 1;
        hi <- hi - 1;
    }
    wesosa (ok) {
        wami "yes";
    } oli {
        wami "no";
    }
    line <- diwela();
}
