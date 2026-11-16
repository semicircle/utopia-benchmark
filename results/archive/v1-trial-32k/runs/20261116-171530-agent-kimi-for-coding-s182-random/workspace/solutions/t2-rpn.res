tosedo substr(s, i, j)
    sheye r <- "";
    sho (sheye k <- i; k <= j; k <- k + 1) {
        r <- r + s[k];
    }
    cha r;
bawoum tosedo

tosedo isdigit(c)
    cha (c <= "9") dilisyo ("0" <= c);
bawoum tosedo

tosedo truncdiv(a, b)
    sheye q <- 0;
    wesosa (a >= 0) {
        q <- a / b;
        wesosa (q < 0) {
            q <- 0 - q;
        }
    } oli {
        q <- a / b;
        wesosa (q > 0) {
            q <- 0 - q;
        }
    }
    cha q;
bawoum tosedo

tosedo pop2(stack)
    sheye ns <- [];
    sho (sheye k <- 0; k < louwo(stack) - 2; k <- k + 1) {
        omse(ns, stack[k]);
    }
    cha ns;
bawoum tosedo

tosedo evaluate(line)
    sheye stack <- [];
    sheye i <- 0;
    sheye n <- louwo(line);
    veshim (i < n) {
        wesosa (line[i] = " ") {
            i <- i + 1;
            chidrom;
        }
        sheye j <- i;
        veshim (j < n) {
            wesosa (line[j] = " ") {
                bou;
            }
            j <- j + 1;
        }
        sheye tok <- substr(line, i, j - 1);
        i <- j;
        wesosa (isdigit(tok[0])) {
            sheye t <- tok;
            sheye ok <- shilsa;
            veshim (louwo(t) > 0) {
                wesosa (drol isdigit(t[0])) {
                    ok <- ishe;
                }
                t <- substr(t, 1, louwo(t) - 1);
            }
            wesosa (ok) {
                omse(stack, odresdra(tok));
            } oli {
                cha "error";
            }
        } oli wesosa (tok = "+") {
            wesosa (louwo(stack) < 2) {
                cha "error";
            }
            sheye b <- stack[louwo(stack) - 1];
            sheye a <- stack[louwo(stack) - 2];
            stack <- pop2(stack);
            omse(stack, a + b);
        } oli wesosa (tok = "-") {
            wesosa (louwo(stack) < 2) {
                cha "error";
            }
            sheye b <- stack[louwo(stack) - 1];
            sheye a <- stack[louwo(stack) - 2];
            stack <- pop2(stack);
            omse(stack, a - b);
        } oli wesosa (tok = "*") {
            wesosa (louwo(stack) < 2) {
                cha "error";
            }
            sheye b <- stack[louwo(stack) - 1];
            sheye a <- stack[louwo(stack) - 2];
            stack <- pop2(stack);
            omse(stack, a * b);
        } oli wesosa (tok = "/") {
            wesosa (louwo(stack) < 2) {
                cha "error";
            }
            sheye b <- stack[louwo(stack) - 1];
            sheye a <- stack[louwo(stack) - 2];
            wesosa (b = 0) {
                cha "error";
            }
            sheye q <- truncdiv(a, b);
            stack <- pop2(stack);
            omse(stack, q);
        } oli wesosa (tok = "%") {
            wesosa (louwo(stack) < 2) {
                cha "error";
            }
            sheye b <- stack[louwo(stack) - 1];
            sheye a <- stack[louwo(stack) - 2];
            wesosa (b = 0) {
                cha "error";
            }
            sheye q <- truncdiv(a, b);
            stack <- pop2(stack);
            omse(stack, a - b * q);
        } oli {
            cha "error";
        }
    }
    wesosa (louwo(stack) <> 1) {
        cha "error";
    }
    cha stack[0];
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wami evaluate(line);
    line <- diwela();
}
