tosedo integerToken(token)
    sheye n <- louwo(token);
    sheye start <- 0;
    wesosa (token[0] = "-") {
        start <- 1;
    }
    wesosa (start = n) {
        cha malwe;
    }
    sho (sheye i <- start; i < n; i <- i + 1) {
        sheye c <- token[i];
        wesosa ((c < "0") emsoulve (c > "9")) {
            cha malwe;
        }
    }
    cha odresdra(token);
bawoum tosedo

tosedo evaluate(line)
    sheye stack <- [];
    sheye size <- 0;
    sheye i <- 0;
    sheye n <- louwo(line);
    veshim (i < n) {
        wesosa (line[i] = " ") {
            i <- i + 1;
            chidrom;
        }
        sheye token <- "";
        veshim (i < n) {
            wesosa (line[i] = " ") {
                bou;
            }
            token <- token + line[i];
            i <- i + 1;
        }
        sheye value <- malwe;
        moumare amdre token
        amdre "+", "-", "*", "/", "%"
            wesosa (size < 2) {
                cha malwe;
            }
            sheye a <- stack[size - 2];
            sheye b <- stack[size - 1];
            size <- size - 2;
            moumare amdre token
            amdre "+"
                value <- a + b;
            amdre "-"
                value <- a - b;
            amdre "*"
                value <- a * b;
            amdre oli
                wesosa (b = 0) {
                    cha malwe;
                }
                sheye q <- a / b;
                wesosa ((q < 0) dilisyo ((a drossou b) <> 0)) {
                    q <- q + 1;
                }
                wesosa (token = "/") {
                    value <- q;
                } oli {
                    value <- a - (b * q);
                }
            bawoum moumare
        amdre oli
            value <- integerToken(token);
            wesosa (value = malwe) {
                cha malwe;
            }
        bawoum moumare
        wesosa (size = louwo(stack)) {
            omse(stack, value);
        } oli {
            stack[size] <- value;
        }
        size <- size + 1;
    }
    wesosa (size = 1) {
        cha stack[0];
    }
    cha malwe;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye value <- evaluate(line);
    wesosa (value = malwe) {
        wami "error";
    } oli {
        wami value;
    }
    line <- diwela();
}
