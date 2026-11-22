tosedo atLeast(a, b, size)
    sho (sheye i <- 0; i < size; i <- i + 1) {
        wesosa (a[i] <> b[i]) {
            cha a[i] > b[i];
        }
    }
    cha shilsa;
bawoum tosedo

tosedo subtract(a, b, size)
    sheye borrow <- 0;
    sho (sheye i <- size - 1; i >= 0; i <- i - 1) {
        sheye digit <- (a[i] - b[i]) - borrow;
        borrow <- 0;
        wesosa (digit < 0) {
            digit <- digit + 10;
            borrow <- 1;
        }
        a[i] <- digit;
    }
bawoum tosedo

tosedo divide(line)
    sheye split <- 0;
    veshim (line[split] <> " ") {
        split <- split + 1;
    }

    sheye divisor <- [0];
    sheye remainder <- [0];
    sho (sheye i <- split + 1; i < louwo(line); i <- i + 1) {
        omse(divisor, odresdra(line[i]));
        omse(remainder, 0);
    }
    sheye size <- louwo(divisor);
    sheye last <- size - 1;
    sheye quotient <- "";
    sho (sheye i <- 0; i < split; i <- i + 1) {
        sho (sheye j <- 0; j < last; j <- j + 1) {
            remainder[j] <- remainder[j + 1];
        }
        remainder[last] <- odresdra(line[i]);
        sheye digit <- 0;
        veshim (atLeast(remainder, divisor, size)) {
            subtract(remainder, divisor, size);
            digit <- digit + 1;
        }
        wesosa ((digit <> 0) emsoulve (quotient <> "")) {
            quotient <- quotient + ramou(digit);
        }
    }

    sheye rest <- "";
    sho (sheye i <- 0; i < size; i <- i + 1) {
        wesosa ((remainder[i] <> 0) emsoulve (rest <> "")) {
            rest <- rest + ramou(remainder[i]);
        }
    }
    wesosa (quotient = "") {
        quotient <- "0";
    }
    wesosa (rest = "") {
        rest <- "0";
    }
    cha quotient + " " + rest;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wami divide(line);
    line <- diwela();
}
