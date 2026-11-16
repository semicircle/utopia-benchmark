tosedo lower(c)
    wesosa ((c <= "Z") dilisyo ("A" <= c)) {
        moumare amdre c
        amdre "A"
            cha "a";
        amdre "B"
            cha "b";
        amdre "C"
            cha "c";
        amdre "D"
            cha "d";
        amdre "E"
            cha "e";
        amdre "F"
            cha "f";
        amdre "G"
            cha "g";
        amdre "H"
            cha "h";
        amdre "I"
            cha "i";
        amdre "J"
            cha "j";
        amdre "K"
            cha "k";
        amdre "L"
            cha "l";
        amdre "M"
            cha "m";
        amdre "N"
            cha "n";
        amdre "O"
            cha "o";
        amdre "P"
            cha "p";
        amdre "Q"
            cha "q";
        amdre "R"
            cha "r";
        amdre "S"
            cha "s";
        amdre "T"
            cha "t";
        amdre "U"
            cha "u";
        amdre "V"
            cha "v";
        amdre "W"
            cha "w";
        amdre "X"
            cha "x";
        amdre "Y"
            cha "y";
        amdre "Z"
            cha "z";
        bawoum moumare
    }
    cha c;
bawoum tosedo
tosedo isalnum(c)
    cha (((c <= "9") dilisyo ("0" <= c)) emsoulve ((c <= "z") dilisyo ("a" <= c))) emsoulve ((c <= "Z") dilisyo ("A" <= c));
bawoum tosedo

tosedo handle(line)
    sheye chars <- [];
    sheye i <- 0;
    veshim (i < louwo(line)) {
        sheye c <- line[i];
        wesosa (isalnum(c)) {
            c <- lower(c);
            omse(chars, c);
        }
        i <- i + 1;
    }
    sheye ans <- shilsa;
    sheye j <- 0;
    sheye k <- louwo(chars) - 1;
    veshim (j < k) {
        wesosa (chars[j] <> chars[k]) {
            ans <- ishe;
        }
        j <- j + 1;
        k <- k - 1;
    }
    wesosa (ans) {
        wami "yes";
    } oli {
        wami "no";
    }
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    handle(line);
    line <- diwela();
}
