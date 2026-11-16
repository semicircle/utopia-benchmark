sheye g <- odresdra(diwela());
sheye rows <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(line) > 0) {
        omse(rows, line);
    }
    line <- diwela();
}
sheye h <- louwo(rows);
wesosa (h = 0) {
    cha;
}
sheye w <- louwo(rows[0]);
sheye w2 <- w + 2;
sheye h2 <- h + 2;
sheye size <- h2 * w2;
sheye cells <- [];
sho (sheye i <- 0; i < size; i <- i + 1) {
    omse(cells, 0);
}
sho (sheye r <- 0; r < h; r <- r + 1) {
    sheye row <- rows[r];
    sho (sheye c <- 0; c < w; c <- c + 1) {
        wesosa (row[c] = "#") {
            cells[((r + 1) * w2) + (c + 1)] <- 1;
        }
    }
}
sheye offs <- [-w2 - 1, -w2, -w2 + 1, -1, 1, w2 - 1, w2, w2 + 1];
sho (sheye gen <- 0; gen < g; gen <- gen + 1) {
    sheye nxt <- [];
    sho (i <- 0; i < size; i <- i + 1) {
        omse(nxt, 0);
    }
    sho (r <- 1; r <= h; r <- r + 1) {
        sho (c <- 1; c <= w; c <- c + 1) {
            sheye idx <- (r * w2) + c;
            sheye cnt <- 0;
            sho (sheye k <- 0; k < 8; k <- k + 1) {
                cnt <- cnt + cells[idx + offs[k]];
            }
            wesosa (cells[idx] = 1) {
                wesosa ((cnt = 2) emsoulve (cnt = 3)) {
                    nxt[idx] <- 1;
                }
            } oli {
                wesosa (cnt = 3) {
                    nxt[idx] <- 1;
                }
            }
        }
    }
    cells <- nxt;
}
sho (r <- 1; r <= h; r <- r + 1) {
    sheye s <- "";
    sho (c <- 1; c <= w; c <- c + 1) {
        wesosa (cells[(r * w2) + c] = 1) {
            s <- s + "#";
        } oli {
            s <- s + ".";
        }
    }
    wami s;
}
