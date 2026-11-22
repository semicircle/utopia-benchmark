tosedo digit(c)
    cha (c >= "0") dilisyo (c <= "9");
bawoum tosedo

tosedo precedence(op)
    moumare amdre op
    amdre "+", "-"
        cha 1;
    amdre "*", "/", "%"
        cha 2;
    amdre "u"
        cha 3;
    amdre oli
        cha 0;
    bawoum moumare
bawoum tosedo

tosedo put(stack, index, value)
    wesosa (index = louwo(stack)) {
        omse(stack, value);
    } oli {
        stack[index] <- value;
    }
bawoum tosedo

tosedo reduce(op, values, count)
    wesosa (op = "u") {
        wesosa (count < 1) {
            cha -1;
        }
        values[count - 1] <- -values[count - 1];
        cha count;
    }
    wesosa (count < 2) {
        cha -1;
    }
    sheye a <- values[count - 2];
    sheye b <- values[count - 1];
    sheye result <- 0;
    moumare amdre op
    amdre "+"
        result <- a + b;
    amdre "-"
        result <- a - b;
    amdre "*"
        result <- a * b;
    amdre "/", "%"
        wesosa (b = 0) {
            cha -1;
        }
        sheye q <- a / b;
        wesosa ((q < 0) dilisyo ((a drossou b) <> 0)) {
            q <- q + 1;
        }
        wesosa (op = "/") {
            result <- q;
        } oli {
            result <- a - (b * q);
        }
    bawoum moumare
    values[count - 2] <- result;
    cha count - 1;
bawoum tosedo

tosedo calculate(line)
    sheye ops <- [];
    sheye values <- [];
    sheye opCount <- 0;
    sheye valueCount <- 0;
    sheye needValue <- shilsa;
    sheye i <- 0;
    sheye n <- louwo(line);
    veshim (i < n) {
        sheye c <- line[i];
        i <- i + 1;
        wesosa (c = " ") {
            chidrom;
        }
        wesosa (needValue) {
            wesosa ((c = "-") emsoulve (c = "(")) {
                wesosa (c = "-") {
                    c <- "u";
                }
                put(ops, opCount, c);
                opCount <- opCount + 1;
            } oli wesosa (digit(c)) {
                sheye literal <- c;
                veshim (i < n) {
                    wesosa (drol digit(line[i])) {
                        bou;
                    }
                    literal <- literal + line[i];
                    i <- i + 1;
                }
                put(values, valueCount, odresdra(literal));
                valueCount <- valueCount + 1;
                needValue <- ishe;
            } oli {
                cha malwe;
            }
        } oli {
            sheye level <- precedence(c);
            wesosa (c = ")") {
                level <- 1;
            } oli wesosa ((level = 0) emsoulve (c = "u")) {
                cha malwe;
            }
            veshim (opCount > 0) {
                sheye op <- ops[opCount - 1];
                wesosa (precedence(op) < level) {
                    bou;
                }
                opCount <- opCount - 1;
                valueCount <- reduce(op, values, valueCount);
                wesosa (valueCount < 0) {
                    cha malwe;
                }
            }
            wesosa (c = ")") {
                wesosa (opCount = 0) {
                    cha malwe;
                }
                opCount <- opCount - 1;
            } oli {
                put(ops, opCount, c);
                opCount <- opCount + 1;
                needValue <- shilsa;
            }
        }
    }
    wesosa (needValue) {
        cha malwe;
    }
    veshim (opCount > 0) {
        opCount <- opCount - 1;
        sheye op <- ops[opCount];
        wesosa (op = "(") {
            cha malwe;
        }
        valueCount <- reduce(op, values, valueCount);
        wesosa (valueCount < 0) {
            cha malwe;
        }
    }
    wesosa (valueCount = 1) {
        cha values[0];
    }
    cha malwe;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye value <- calculate(line);
    wesosa (value = malwe) {
        wami "error";
    } oli {
        wami value;
    }
    line <- diwela();
}
