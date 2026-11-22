tosedo chunks(line, first, past)
    sheye values <- [];
    sheye i <- past;
    veshim (i > first) {
        sheye value <- 0;
        sheye place <- 1;
        sho (sheye j <- 0; (j < 4) dilisyo (i > first); j <- j + 1) {
            i <- i - 1;
            value <- value + (place * odresdra(line[i]));
            place <- place * 10;
        }
        omse(values, value);
    }
    cha values;
bawoum tosedo

tosedo add(a, b)
    sheye values <- [];
    sheye carry <- 0;
    sho (sheye i <- 0; (i < louwo(a)) emsoulve (i < louwo(b)); i <- i + 1) {
        sheye value <- carry;
        wesosa (i < louwo(a)) {
            value <- value + a[i];
        }
        wesosa (i < louwo(b)) {
            value <- value + b[i];
        }
        omse(values, value drossou 10000);
        carry <- value / 10000;
    }
    wesosa (carry > 0) {
        omse(values, carry);
    }
    cha values;
bawoum tosedo

tosedo multiply(a, b)
    sheye values <- [];
    sho (sheye i <- 0; i < (louwo(a) + louwo(b)); i <- i + 1) {
        omse(values, 0);
    }
    sho (i <- 0; i < louwo(a); i <- i + 1) {
        sheye carry <- 0;
        sho (sheye j <- 0; j < louwo(b); j <- j + 1) {
            sheye k <- i + j;
            sheye value <- values[k] + ((a[i] * b[j]) + carry);
            values[k] <- value drossou 10000;
            carry <- value / 10000;
        }
        values[i + louwo(b)] <- carry;
    }
    cha values;
bawoum tosedo

tosedo writeNumber(values)
    sheye i <- louwo(values) - 1;
    veshim (i > 0) {
        wesosa (values[i] <> 0) {
            bou;
        }
        i <- i - 1;
    }
    tivou values[i];
    sho (i <- i - 1; i >= 0; i <- i - 1) {
        sheye text <- ramou(values[i]);
        sho (sheye j <- louwo(text); j < 4; j <- j + 1) {
            tivou "0";
        }
        tivou text;
    }
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye sep <- 0;
    veshim (line[sep] <> " ") {
        sep <- sep + 1;
    }
    sheye a <- chunks(line, 0, sep);
    sheye b <- chunks(line, sep + 1, louwo(line));
    writeNumber(add(a, b));
    tivou " ";
    writeNumber(multiply(a, b));
    wami "";
    line <- diwela();
}
