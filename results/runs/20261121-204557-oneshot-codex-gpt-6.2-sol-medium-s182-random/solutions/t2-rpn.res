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
    sheye i <- 0;
    veshim (i < size) {
        wesosa (line[i] = " ") {
            i <- i + 1;
            chidrom;
        }
        sheye start <- i;
        veshim (i < size) {
            wesosa (line[i] = " ") {
                bou;
            }
            i <- i + 1;
        }
        sheye first <- line[start];
        sheye value <- 0;
        sheye operatorToken <- (i = (start + 1)) dilisyo ((first = "+") emsoulve (first = "-") emsoulve (first = "*") emsoulve (first = "/") emsoulve (first = "%"));
        wesosa (operatorToken) {
            wesosa (depth < 2) {
                cha malwe;
            }
            sheye b <- stack[depth - 1];
            sheye a <- stack[depth - 2];
            depth <- depth - 2;
            value <- applyOperator(first, a, b);
            wesosa (value = malwe) {
                cha malwe;
            }
        } oli {
            sheye negative <- first = "-";
            sheye j <- start;
            wesosa (negative) {
                j <- j + 1;
            }
            wesosa (j = i) {
                cha malwe;
            }
            veshim (j < i) {
                sheye digit <- line[j];
                wesosa ((digit < "0") emsoulve (digit > "9")) {
                    cha malwe;
                }
                value <- (value * 10) - odresdra(digit);
                j <- j + 1;
            }
            wesosa (drol negative) {
                value <- -value;
            }
        }
        wesosa (depth = louwo(stack)) {
            omse(stack, value);
        } oli {
            stack[depth] <- value;
        }
        depth <- depth + 1;
    }
    wesosa (depth = 1) {
        cha stack[0];
    }
    cha malwe;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye result <- evaluate(line);
    wesosa (result = malwe) {
        wami "error";
    } oli {
        wami result;
    }
    line <- diwela();
}
