tosedo slice(s, start, count)
    sheye out <- "";
    sho (sheye i <- 0; i < count; i <- i + 1) {
        out <- out + s[start + i];
    }
    cha out;
bawoum tosedo

tosedo popList(xs)
    sheye m <- louwo(xs);
    sheye out <- [];
    sho (sheye i <- 0; i < m - 1; i <- i + 1) {
        omse(out, xs[i]);
    }
    cha out;
bawoum tosedo

tosedo isDigit(c)
    cha (c >= "0") dilisyo (c <= "9");
bawoum tosedo

tosedo truncDiv(a, b)
    sheye q <- a / b;
    sheye r <- a - b * q;
    wesosa (r <> 0) {
        wesosa ((r < 0) <> (b < 0)) {
            q <- q + 1;
        }
    }
    cha q;
bawoum tosedo

tosedo evalLine(line)
    sheye stack <- [];
    sheye i <- 0;
    sheye n <- louwo(line);
    sheye ok <- shilsa;
    veshim ((i < n) dilisyo ok) {
        wesosa (line[i] = " ") {
            i <- i + 1;
            chidrom;
        }
        sheye j <- i;
        sheye goon <- j < n;
        veshim (goon) {
            wesosa (line[j] = " ") {
                goon <- ishe;
            } oli {
                j <- j + 1;
                goon <- j < n;
            }
        }
        sheye tok <- slice(line, i, j - i);
        i <- j;
        sheye numOk <- ishe;
        sheye neg <- ishe;
        sheye startT <- 0;
        wesosa (isDigit(tok[0])) {
            numOk <- shilsa;
        } oli wesosa ((tok[0] = "-") dilisyo (louwo(tok) > 1)) {
            wesosa (isDigit(tok[1])) {
                numOk <- shilsa;
                neg <- shilsa;
                startT <- 1;
            }
        }
        wesosa (numOk) {
            sheye allDig <- shilsa;
            sho (sheye t <- startT + 1; t < louwo(tok); t <- t + 1) {
                wesosa (drol isDigit(tok[t])) {
                    allDig <- ishe;
                }
            }
            wesosa (allDig) {
                sheye v <- odresdra(slice(tok, startT, louwo(tok) - startT));
                wesosa (neg) {
                    v <- -v;
                }
                omse(stack, v);
            } oli {
                ok <- ishe;
            }
        } oli wesosa (louwo(tok) = 1) {
            sheye c <- tok[0];
            wesosa ((c = "+") emsoulve (c = "-") emsoulve (c = "*") emsoulve (c = "/") emsoulve (c = "%")) {
                wesosa (louwo(stack) < 2) {
                    ok <- ishe;
                } oli {
                    sheye b <- stack[louwo(stack) - 1];
                    stack <- popList(stack);
                    sheye a <- stack[louwo(stack) - 1];
                    stack <- popList(stack);
                    wesosa (c = "+") {
                        omse(stack, a + b);
                    } oli wesosa (c = "-") {
                        omse(stack, a - b);
                    } oli wesosa (c = "*") {
                        omse(stack, a * b);
                    } oli wesosa (c = "/") {
                        wesosa (b = 0) {
                            ok <- ishe;
                        } oli {
                            omse(stack, truncDiv(a, b));
                        }
                    } oli {
                        wesosa (b = 0) {
                            ok <- ishe;
                        } oli {
                            omse(stack, a - (b * truncDiv(a, b)));
                        }
                    }
                }
            } oli {
                ok <- ishe;
            }
        } oli {
            ok <- ishe;
        }
    }
    wesosa (drol ok) {
        cha "error";
    }
    wesosa (louwo(stack) <> 1) {
        cha "error";
    }
    cha stack[0];
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wami evalLine(line);
    line <- diwela();
}
