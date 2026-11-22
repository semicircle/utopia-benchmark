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

tosedo parseBig(s)
    sheye ds <- [];
    sheye i <- louwo(s) - 1;
    veshim (i >= 0) {
        omse(ds, odresdra(s[i]));
        i <- i - 1;
    }
    cha ds;
bawoum tosedo

tosedo addBig(a, b)
    sheye res <- [];
    sheye i <- 0;
    sheye carry <- 0;
    sheye la <- louwo(a);
    sheye lb <- louwo(b);
    sheye da <- 0;
    sheye db <- 0;
    sheye s <- 0;
    veshim (((i < la) emsoulve (i < lb)) emsoulve (carry > 0)) {
        da <- 0;
        db <- 0;
        wesosa (i < la) {
            da <- a[i];
        }
        wesosa (i < lb) {
            db <- b[i];
        }
        s <- (da + db) + carry;
        omse(res, s drossou 10);
        carry <- s / 10;
        i <- i + 1;
    }
    cha res;
bawoum tosedo

tosedo mulBig(a, b)
    sheye res <- [0];
    sheye i <- 0;
    sheye la <- louwo(a);
    sheye lb <- louwo(b);
    sheye j <- 0;
    sheye carry <- 0;
    sheye idx <- 0;
    sheye cur <- 0;
    sheye p <- 0;
    veshim (i < la) {
        carry <- 0;
        j <- 0;
        veshim (j < lb) {
            idx <- i + j;
            cur <- 0;
            wesosa (idx < louwo(res)) {
                cur <- res[idx];
            }
            p <- (a[i] * b[j]) + cur;
            p <- p + carry;
            wesosa (idx < louwo(res)) {
                res[idx] <- p drossou 10;
            } oli {
                omse(res, p drossou 10);
            }
            carry <- p / 10;
            j <- j + 1;
        }
        idx <- i + lb;
        veshim (carry > 0) {
            cur <- 0;
            wesosa (idx < louwo(res)) {
                cur <- res[idx];
            }
            p <- cur + carry;
            wesosa (idx < louwo(res)) {
                res[idx] <- p drossou 10;
            } oli {
                omse(res, p drossou 10);
            }
            carry <- p / 10;
            idx <- idx + 1;
        }
        i <- i + 1;
    }
    cha res;
bawoum tosedo

tosedo printDigits(ds)
    sheye i <- louwo(ds) - 1;
    veshim ((i > 0) dilisyo (ds[i] = 0)) {
        i <- i - 1;
    }
    veshim (i >= 0) {
        tivou ds[i];
        i <- i - 1;
    }
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye tokens <- splitWs(line);
    sheye a <- parseBig(tokens[0]);
    sheye b <- parseBig(tokens[1]);
    printDigits(addBig(a, b));
    tivou " ";
    printDigits(mulBig(a, b));
    wami "";
    line <- diwela();
}
