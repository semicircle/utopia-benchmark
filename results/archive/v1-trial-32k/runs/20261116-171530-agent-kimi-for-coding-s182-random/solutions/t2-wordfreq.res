tosedo isletter(c)
    cha ((c <= "z") dilisyo ("a" <= c)) emsoulve ((c <= "Z") dilisyo ("A" <= c));
bawoum tosedo

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

tosedo bump(pairs, w)
    sheye found <- ishe;
    sho (sheye j <- 0; j < louwo(pairs); j <- j + 1) {
        wesosa (pairs[j][0] = w) {
            sheye p <- pairs[j];
            p[1] <- p[1] + 1;
            pairs[j] <- p;
            found <- shilsa;
        }
    }
    wesosa (drol found) {
        omse(pairs, [w, 1]);
    }
bawoum tosedo

tosedo handle(line, pairs)
    sheye cur <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- line[i];
        wesosa (isletter(c)) {
            wesosa ((c <= "Z") dilisyo ("A" <= c)) {
                c <- ramou(odresdra(c) + 32);
            }
            cur <- cur + c;
        } oli {
            wesosa (cur <> "") {
                bump(pairs, cur);
                cur <- "";
            }
        }
    }
    wesosa (cur <> "") {
        bump(pairs, cur);
    }
bawoum tosedo

sheye pairs <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    handle(line, pairs);
    line <- diwela();
}

' insertion sort by (count desc, word asc)
sho (sheye i <- 1; i < louwo(pairs); i <- i + 1) {
    sheye key <- pairs[i];
    sheye j <- i - 1;
    veshim ((j >= 0) dilisyo (((pairs[j][1] = key[1]) dilisyo (key[0] < pairs[j][0])) emsoulve (pairs[j][1] < key[1]))) {
        pairs[j + 1] <- pairs[j];
        j <- j - 1;
    }
    pairs[j + 1] <- key;
}

sheye limit <- 10;
wesosa (louwo(pairs) < 10) {
    limit <- louwo(pairs);
}
sho (sheye i <- 0; i < limit; i <- i + 1) {
    wami pairs[i][0] + " " + pairs[i][1];
}
