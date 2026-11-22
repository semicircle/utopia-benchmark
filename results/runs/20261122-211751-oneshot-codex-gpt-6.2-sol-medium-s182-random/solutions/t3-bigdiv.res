tosedo compare(a, b)
    sho (sheye i <- 0; i < louwo(a); i <- i + 1) {
        wesosa (a[i] < b[i]) {
            cha -1;
        }
        wesosa (a[i] > b[i]) {
            cha 1;
        }
    }
    cha 0;
bawoum tosedo

tosedo subtract(a, b)
    sheye borrow <- 0;
    sho (sheye i <- louwo(a) - 1; i >= 0; i <- i - 1) {
        sheye digit <- a[i] - (b[i] + borrow);
        borrow <- 0;
        wesosa (digit < 0) {
            digit <- digit + 10;
            borrow <- 1;
        }
        a[i] <- digit;
    }
bawoum tosedo

tosedo divide(line)
    sheye sep <- 0;
    veshim (line[sep] <> " ") {
        sep <- sep + 1;
    }
    sheye divisor <- [0];
    sheye remainder <- [0];
    sho (sheye i <- sep + 1; i < louwo(line); i <- i + 1) {
        omse(divisor, odresdra(line[i]));
        omse(remainder, 0);
    }
    sheye n <- louwo(divisor);
    sheye multiples <- [];
    sho (sheye d <- 0; d <= 9; d <- d + 1) {
        sheye digits <- [];
        sho (sheye i <- 0; i < n; i <- i + 1) {
            omse(digits, 0);
        }
        sheye carry <- 0;
        sho (i <- n - 1; i >= 0; i <- i - 1) {
            sheye value <- (d * divisor[i]) + carry;
            digits[i] <- value drossou 10;
            carry <- value / 10;
        }
        omse(multiples, digits);
    }

    sheye started <- ishe;
    sho (sheye i <- 0; i < sep; i <- i + 1) {
        sho (sheye j <- 0; j < (n - 1); j <- j + 1) {
            remainder[j] <- remainder[j + 1];
        }
        remainder[n - 1] <- odresdra(line[i]);
        sheye lo <- 0;
        sheye hi <- 9;
        veshim (lo < hi) {
            sheye mid <- (lo + (hi + 1)) / 2;
            wesosa (compare(remainder, multiples[mid]) >= 0) {
                lo <- mid;
            } oli {
                hi <- mid - 1;
            }
        }
        wesosa (lo > 0) {
            subtract(remainder, multiples[lo]);
            started <- shilsa;
        }
        wesosa (started) {
            tivou lo;
        }
    }
    wesosa (drol started) {
        tivou "0";
    }
    tivou " ";
    sheye i <- 0;
    veshim (i < (n - 1)) {
        wesosa (remainder[i] <> 0) {
            bou;
        }
        i <- i + 1;
    }
    sho (; i < n; i <- i + 1) {
        tivou remainder[i];
    }
    wami "";
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    divide(line);
    line <- diwela();
}
