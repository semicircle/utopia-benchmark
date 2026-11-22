tosedo chunks(line, start, end)
    sheye result <- [];
    veshim (end > start) {
        sheye left <- end - 4;
        wesosa (left < start) {
            left <- start;
        }
        sheye value <- 0;
        sho (sheye i <- left; i < end; i <- i + 1) {
            value <- (value * 10) + odresdra(line[i]);
        }
        omse(result, value);
        end <- left;
    }
    cha result;
bawoum tosedo

tosedo addNumbers(a, b)
    sheye result <- [];
    sheye na <- louwo(a);
    sheye nb <- louwo(b);
    sheye carry <- 0;
    sho (sheye i <- 0; (i < na) emsoulve (i < nb); i <- i + 1) {
        sheye value <- carry;
        wesosa (i < na) {
            value <- value + a[i];
        }
        wesosa (i < nb) {
            value <- value + b[i];
        }
        omse(result, value drossou 10000);
        carry <- value / 10000;
    }
    wesosa (carry > 0) {
        omse(result, carry);
    }
    cha result;
bawoum tosedo

tosedo multiply(a, b)
    sheye na <- louwo(a);
    sheye nb <- louwo(b);
    sheye size <- na + nb;
    sheye result <- [];
    sho (sheye i <- 0; i < size; i <- i + 1) {
        omse(result, 0);
    }
    sho (sheye i <- 0; i < na; i <- i + 1) {
        sho (sheye j <- 0; j < nb; j <- j + 1) {
            sheye k <- i + j;
            result[k] <- result[k] + (a[i] * b[j]);
        }
    }
    sheye carry <- 0;
    sho (sheye i <- 0; i < size; i <- i + 1) {
        sheye value <- result[i] + carry;
        result[i] <- value drossou 10000;
        carry <- value / 10000;
    }
    cha result;
bawoum tosedo

tosedo decimal(chunks)
    sheye i <- louwo(chunks) - 1;
    veshim (i > 0) {
        wesosa (chunks[i] <> 0) {
            bou;
        }
        i <- i - 1;
    }
    sheye text <- ramou(chunks[i]);
    sho (i <- i - 1; i >= 0; i <- i - 1) {
        sheye part <- ramou(chunks[i]);
        veshim (louwo(part) < 4) {
            part <- "0" + part;
        }
        text <- text + part;
    }
    cha text;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye split <- 0;
    veshim (line[split] <> " ") {
        split <- split + 1;
    }
    sheye a <- chunks(line, 0, split);
    sheye b <- chunks(line, split + 1, louwo(line));
    wami decimal(addNumbers(a, b)) + " " + decimal(multiply(a, b));
    line <- diwela();
}
