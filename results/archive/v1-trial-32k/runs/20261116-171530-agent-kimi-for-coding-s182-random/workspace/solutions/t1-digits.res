tosedo isdigit(c)
    cha (c <= "9") dilisyo ("0" <= c);
bawoum tosedo

tosedo handle(n)
    sheye digits <- ramou(n);
    sheye ds <- "";
    sheye i <- 0;
    veshim (i < louwo(digits)) {
        sheye c <- digits[i];
        wesosa (isdigit(c)) {
            ds <- ds + c;
        }
        i <- i + 1;
    }
    sheye sum <- 0;
    sheye rev <- "";
    sheye j <- 0;
    veshim (j < louwo(ds)) {
        sheye c <- ds[j];
        sum <- sum + odresdra(c);
        rev <- c + rev;
        j <- j + 1;
    }
    wesosa (n < 0) {
        wami sum + " -" + odresdra(rev);
    } oli {
        wami sum + " " + odresdra(rev);
    }
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    handle(odresdra(line));
    line <- diwela();
}
