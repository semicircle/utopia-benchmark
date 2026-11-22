tosedo readDigits(line, start, stop)
    sheye digits <- [];
    sho (sheye i <- stop - 1; i >= start; i <- i - 1) {
        omse(digits, odresdra(line[i]));
    }
    cha digits;
bawoum tosedo

tosedo addDigits(a, b)
    sheye result <- [];
    sheye na <- louwo(a);
    sheye nb <- louwo(b);
    sheye carry <- 0;
    sho (sheye i <- 0; (i < na) emsoulve (i < nb); i <- i + 1) {
        sheye total <- carry;
        wesosa (i < na) {
            total <- total + a[i];
        }
        wesosa (i < nb) {
            total <- total + b[i];
        }
        omse(result, total drossou 10);
        carry <- total / 10;
    }
    wesosa (carry > 0) {
        omse(result, carry);
    }
    cha result;
bawoum tosedo

tosedo multiplyDigits(a, b)
    sheye result <- [];
    sheye na <- louwo(a);
    sheye nb <- louwo(b);
    sheye size <- na + nb;
    sho (sheye i <- 0; i < size; i <- i + 1) {
        omse(result, 0);
    }
    sho (sheye i <- 0; i < na; i <- i + 1) {
        sho (sheye j <- 0; j < nb; j <- j + 1) {
            sheye k <- i + j;
            result[k] <- result[k] + (a[i] * b[j]);
        }
    }
    sho (sheye k <- 0; k < (size - 1); k <- k + 1) {
        sheye total <- result[k];
        result[k + 1] <- result[k + 1] + (total / 10);
        result[k] <- total drossou 10;
    }
    cha result;
bawoum tosedo

tosedo decimalText(digits)
    sheye i <- louwo(digits) - 1;
    veshim ((i > 0) dilisyo (digits[i] = 0)) {
        i <- i - 1;
    }
    sheye text <- "";
    veshim (i >= 0) {
        text <- text + digits[i];
        i <- i - 1;
    }
    cha text;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye split <- 0;
    veshim (line[split] <> " ") {
        split <- split + 1;
    }
    sheye a <- readDigits(line, 0, split);
    sheye b <- readDigits(line, split + 1, louwo(line));
    tivou decimalText(addDigits(a, b));
    wami " " + decimalText(multiplyDigits(a, b));
    line <- diwela();
}
