tosedo priority(op)
    moumare amdre op
    amdre "+", "-"
        cha 1;
    amdre "*", "/", "%"
        cha 2;
    amdre "~"
        cha 3;
    amdre oli
        cha 0;
    bawoum moumare
bawoum tosedo

tosedo push(stack, size, value)
    wesosa (size = louwo(stack)) {
        omse(stack, value);
    } oli {
        stack[size] <- value;
    }
    cha size + 1;
bawoum tosedo

tosedo reduce(values, size, op)
    wesosa (op = "~") {
        wesosa (size < 1) {
            cha -1;
        }
        values[size - 1] <- -values[size - 1];
        cha size;
    }
    wesosa (size < 2) {
        cha -1;
    }
    sheye index <- size - 2;
    sheye a <- values[index];
    sheye b <- values[size - 1];
    moumare amdre op
    amdre "+"
        values[index] <- a + b;
    amdre "-"
        values[index] <- a - b;
    amdre "*"
        values[index] <- a * b;
    amdre "/", "%"
        wesosa (b = 0) {
            cha -1;
        }
        sheye q <- a / b;
        wesosa (((a < 0) <> (b < 0)) dilisyo ((a drossou b) <> 0)) {
            q <- q + 1;
        }
        wesosa (op = "/") {
            values[index] <- q;
        } oli {
            values[index] <- a - (b * q);
        }
    amdre oli
        cha -1;
    bawoum moumare
    cha size - 1;
bawoum tosedo

tosedo evaluate(line)
    sheye values <- [];
    sheye ops <- [];
    sheye nv <- 0;
    sheye no <- 0;
    sheye needValue <- shilsa;
    sheye n <- louwo(line);
    sheye i <- 0;
    veshim (i < n) {
        sheye c <- line[i];
        wesosa (c = " ") {
            i <- i + 1;
            chidrom;
        }
        wesosa (needValue) {
            wesosa (c = "-") {
                no <- push(ops, no, "~");
            } oli wesosa (c = "(") {
                no <- push(ops, no, "(");
            } oli wesosa ((c >= "0") dilisyo (c <= "9")) {
                sheye value <- 0;
                veshim (i < n) {
                    sheye digit <- line[i];
                    wesosa ((digit < "0") emsoulve (digit > "9")) {
                        bou;
                    }
                    value <- (value * 10) + odresdra(digit);
                    i <- i + 1;
                }
                nv <- push(values, nv, value);
                needValue <- ishe;
                chidrom;
            } oli {
                cha "error";
            }
        } oli wesosa (c = ")") {
            veshim (no > 0) {
                sheye top <- ops[no - 1];
                wesosa (top = "(") {
                    bou;
                }
                no <- no - 1;
                nv <- reduce(values, nv, top);
                wesosa (nv < 0) {
                    cha "error";
                }
            }
            wesosa (no = 0) {
                cha "error";
            }
            no <- no - 1;
        } oli {
            sheye level <- priority(c);
            wesosa ((level = 0) emsoulve (level = 3)) {
                cha "error";
            }
            veshim (no > 0) {
                sheye top <- ops[no - 1];
                wesosa (priority(top) < level) {
                    bou;
                }
                no <- no - 1;
                nv <- reduce(values, nv, top);
                wesosa (nv < 0) {
                    cha "error";
                }
            }
            no <- push(ops, no, c);
            needValue <- shilsa;
        }
        i <- i + 1;
    }

    wesosa (needValue) {
        cha "error";
    }
    veshim (no > 0) {
        no <- no - 1;
        nv <- reduce(values, nv, ops[no]);
        wesosa (nv < 0) {
            cha "error";
        }
    }
    wesosa (nv <> 1) {
        cha "error";
    }
    cha values[0];
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wami evaluate(line);
    line <- diwela();
}
