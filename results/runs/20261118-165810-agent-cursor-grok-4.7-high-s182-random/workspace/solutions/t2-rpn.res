tosedo divz(a, b)
    sheye q <- a / b;
    sheye r <- a - b * q;
    wesosa (r <> 0) {
        wesosa ((r < 0) <> a < 0) {
            wesosa ((r < 0) = b < 0) {
                q <- q + 1;
            } oli {
                q <- q - 1;
            }
        }
    }
    cha q;
bawoum tosedo

tosedo modz(a, b)
    cha a - b * divz(a, b);
bawoum tosedo

tosedo isDigitChar(c)
    cha (c >= "0") dilisyo (c <= "9");
bawoum tosedo

tosedo isNumber(tok)
    sheye n <- louwo(tok);
    wesosa (n = 0) {
        cha ishe;
    }
    sheye i <- 0;
    wesosa (tok[0] = "-") {
        wesosa (n = 1) {
            cha ishe;
        }
        i <- 1;
    }
    veshim (i < n) {
        wesosa (drol (isDigitChar(tok[i]))) {
            cha ishe;
        }
        i <- i + 1;
    }
    cha shilsa;
bawoum tosedo

tosedo isOp(tok)
    wesosa (louwo(tok) <> 1) {
        cha ishe;
    }
    sheye c <- tok[0];
    cha (c = "+") emsoulve (c = "-") emsoulve (c = "*") emsoulve (c = "/") emsoulve (c = "%");
bawoum tosedo

tosedo splitWs(s)
    sheye tokens <- [];
    sheye n <- louwo(s);
    sheye i <- 0;
    sheye tok <- "";
    veshim (i < n) {
        wesosa (s[i] = " ") {
            wesosa (louwo(tok) > 0) {
                omse(tokens, tok);
                tok <- "";
            }
            i <- i + 1;
        } oli {
            tok <- tok + s[i];
            i <- i + 1;
        }
    }
    wesosa (louwo(tok) > 0) {
        omse(tokens, tok);
    }
    cha tokens;
bawoum tosedo

tosedo push(stack, size, v)
    wesosa (size < louwo(stack)) {
        stack[size] <- v;
    } oli {
        omse(stack, v);
    }
    cha size + 1;
bawoum tosedo

tosedo evalLine(line)
    sheye tokens <- splitWs(line);
    sheye stack <- [];
    sheye size <- 0;
    sheye bad <- ishe;
    sheye ti <- 0;
    sheye nt <- louwo(tokens);
    sheye tok <- "";
    sheye a <- 0;
    sheye b <- 0;
    sheye result <- 0;
    veshim ((ti < nt) dilisyo (drol bad)) {
        tok <- tokens[ti];
        wesosa (isNumber(tok)) {
            size <- push(stack, size, odresdra(tok));
        } oli wesosa (isOp(tok)) {
            wesosa (size < 2) {
                bad <- shilsa;
            } oli {
                size <- size - 1;
                b <- stack[size];
                size <- size - 1;
                a <- stack[size];
                wesosa (((tok = "/") emsoulve (tok = "%")) dilisyo (b = 0)) {
                    bad <- shilsa;
                } oli {
                    result <- 0;
                    wesosa (tok = "+") {
                        result <- a + b;
                    } oli wesosa (tok = "-") {
                        result <- a - b;
                    } oli wesosa (tok = "*") {
                        result <- a * b;
                    } oli wesosa (tok = "/") {
                        result <- divz(a, b);
                    } oli {
                        result <- modz(a, b);
                    }
                    size <- push(stack, size, result);
                }
            }
        } oli {
            bad <- shilsa;
        }
        ti <- ti + 1;
    }
    wesosa ((drol bad) dilisyo (size = 1)) {
        wami stack[0];
    } oli {
        wami "error";
    }
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    evalLine(line);
    line <- diwela();
}
