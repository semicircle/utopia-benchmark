tosedo readDigits(line, first, end)
    sheye digits <- [];
    sho (sheye i <- end - 1; i >= first; i <- i - 1) {
        omse(digits, odresdra(line[i]));
    }
    cha digits;
bawoum tosedo

tosedo carryDigits(digits)
    sho (sheye i <- 0; i < (louwo(digits) - 1); i <- i + 1) {
        sheye value <- digits[i];
        digits[i] <- value drossou 10;
        digits[i + 1] <- digits[i + 1] + (value / 10);
    }
bawoum tosedo

tosedo writeDigits(digits)
    sheye i <- louwo(digits) - 1;
    veshim (i > 0) {
        wesosa (digits[i] <> 0) {
            bou;
        }
        i <- i - 1;
    }
    veshim (i >= 0) {
        tivou digits[i];
        i <- i - 1;
    }
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye separator <- 0;
    veshim (line[separator] <> " ") {
        separator <- separator + 1;
    }
    sheye a <- readDigits(line, 0, separator);
    sheye b <- readDigits(line, separator + 1, louwo(line));
    sheye aSize <- louwo(a);
    sheye bSize <- louwo(b);
    sheye size <- aSize + bSize;
    sheye sum <- [];
    sheye product <- [];
    sho (sheye i <- 0; i < size; i <- i + 1) {
        omse(sum, 0);
        omse(product, 0);
    }
    sho (sheye i <- 0; i < aSize; i <- i + 1) {
        sheye digit <- a[i];
        sum[i] <- digit;
        sho (sheye j <- 0; j < bSize; j <- j + 1) {
            sheye position <- i + j;
            product[position] <- product[position] + (digit * b[j]);
        }
    }
    sho (sheye j <- 0; j < bSize; j <- j + 1) {
        sum[j] <- sum[j] + b[j];
    }
    carryDigits(sum);
    carryDigits(product);
    writeDigits(sum);
    tivou " ";
    writeDigits(product);
    wami "";
    line <- diwela();
}
