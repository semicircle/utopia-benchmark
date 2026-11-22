tosedo quotient(a, b)
    sheye q <- a / b;
    wesosa (((a < 0) <> (b < 0)) dilisyo ((a drossou b) <> 0)) {
        q <- q + 1;
    }
    cha q;
bawoum tosedo

tosedo evaluate(line)
    sheye stack <- [];
    sheye size <- 0;
    sheye n <- louwo(line);
    sheye i <- 0;
    veshim (i < n) {
        sheye first <- line[i];
        wesosa (first = " ") {
            i <- i + 1;
            chidrom;
        }
        sheye start <- i;
        veshim (i < n) {
            wesosa (line[i] = " ") {
                bou;
            }
            i <- i + 1;
        }
        sheye operator <- (first = "+") emsoulve (first = "-") emsoulve (first = "*") emsoulve (first = "/") emsoulve (first = "%");
        sheye value <- 0;
        wesosa (operator dilisyo ((i - start) = 1)) {
            wesosa (size < 2) {
                cha "error";
            }
            sheye a <- stack[size - 2];
            sheye b <- stack[size - 1];
            moumare amdre first
            amdre "+"
                value <- a + b;
            amdre "-"
                value <- a - b;
            amdre "*"
                value <- a * b;
            amdre "/", "%"
                wesosa (b = 0) {
                    cha "error";
                }
                sheye q <- quotient(a, b);
                wesosa (first = "/") {
                    value <- q;
                } oli {
                    value <- a - (b * q);
                }
            bawoum moumare
            size <- size - 2;
        } oli {
            sheye pos <- start;
            wesosa (first = "-") {
                pos <- pos + 1;
            }
            sho (; pos < i; pos <- pos + 1) {
                sheye digit <- line[pos];
                wesosa ((digit < "0") emsoulve (digit > "9")) {
                    cha "error";
                }
                value <- (value * 10) + odresdra(digit);
            }
            wesosa (first = "-") {
                value <- -value;
            }
        }
        wesosa (size = louwo(stack)) {
            omse(stack, value);
        } oli {
            stack[size] <- value;
        }
        size <- size + 1;
    }
    wesosa (size <> 1) {
        cha "error";
    }
    cha stack[0];
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wami evaluate(line);
    line <- diwela();
}
