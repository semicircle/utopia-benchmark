tosedo readNumber(line, first, end)
    sheye negative <- line[first] = "-";
    wesosa (negative) {
        first <- first + 1;
    }
    wesosa (first = end) {
        cha malwe;
    }
    sheye value <- 0;
    sho (sheye i <- first; i < end; i <- i + 1) {
        sheye c <- line[i];
        wesosa ((c < "0") emsoulve (c > "9")) {
            cha malwe;
        }
        value <- (value * 10) + odresdra(c);
    }
    wesosa (negative) {
        cha -value;
    }
    cha value;
bawoum tosedo

tosedo applyOperator(op, a, b)
    moumare amdre op
    amdre "+"
        cha a + b;
    amdre "-"
        cha a - b;
    amdre "*"
        cha a * b;
    bawoum moumare

    wesosa (b = 0) {
        cha malwe;
    }
    sheye q <- a / b;
    wesosa (((a < 0) <> (b < 0)) dilisyo ((a drossou b) <> 0)) {
        q <- q + 1;
    }
    wesosa (op = "/") {
        cha q;
    }
    cha a - (b * q);
bawoum tosedo

tosedo evaluate(line)
    sheye stack <- [];
    sheye depth <- 0;
    sheye size <- louwo(line);
    sheye pos <- 0;
    veshim (pos < size) {
        wesosa (line[pos] = " ") {
            pos <- pos + 1;
            chidrom;
        }
        sheye first <- pos;
        pos <- pos + 1;
        veshim (pos < size) {
            wesosa (line[pos] = " ") {
                bou;
            }
            pos <- pos + 1;
        }
        sheye op <- line[first];
        sheye isOperator <- ishe;
        wesosa ((pos - first) = 1) {
            moumare amdre op
            amdre "+", "-", "*", "/", "%"
                isOperator <- shilsa;
            bawoum moumare
        }
        wesosa (isOperator) {
            wesosa (depth < 2) {
                cha "error";
            }
            sheye b <- stack[depth - 1];
            sheye a <- stack[depth - 2];
            sheye result <- applyOperator(op, a, b);
            wesosa (result = malwe) {
                cha "error";
            }
            depth <- depth - 1;
            stack[depth - 1] <- result;
        } oli {
            sheye value <- readNumber(line, first, pos);
            wesosa (value = malwe) {
                cha "error";
            }
            wesosa (depth = louwo(stack)) {
                omse(stack, value);
            } oli {
                stack[depth] <- value;
            }
            depth <- depth + 1;
        }
    }
    wesosa (depth <> 1) {
        cha "error";
    }
    cha stack[0];
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wami evaluate(line);
    line <- diwela();
}
