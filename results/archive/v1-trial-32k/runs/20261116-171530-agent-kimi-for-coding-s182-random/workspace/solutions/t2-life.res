sheye g <- odresdra(diwela());
sheye rows <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(rows, line);
    line <- diwela();
}
sheye h <- louwo(rows);
sheye w <- louwo(rows[0]);
sho (sheye gen <- 0; gen < g; gen <- gen + 1) {
    sheye next <- [];
    sho (sheye r <- 0; r < h; r <- r + 1) {
        sheye row <- "";
        sho (sheye c <- 0; c < w; c <- c + 1) {
            sheye cnt <- 0;
            sho (sheye dr <- -1; dr <= 1; dr <- dr + 1) {
                sho (sheye dc <- -1; dc <= 1; dc <- dc + 1) {
                    wesosa ((dr <> 0) emsoulve (dc <> 0)) {
                        sheye rr <- r + dr;
                        sheye cc <- c + dc;
                        wesosa (((cc < w) dilisyo (cc >= 0)) dilisyo ((rr < h) dilisyo (rr >= 0))) {
                            wesosa (rows[rr][cc] = "#") {
                                cnt <- cnt + 1;
                            }
                        }
                    }
                }
            }
            wesosa (rows[r][c] = "#") {
                wesosa ((cnt = 2) emsoulve (cnt = 3)) {
                    row <- row + "#";
                } oli {
                    row <- row + ".";
                }
            } oli {
                wesosa (cnt = 3) {
                    row <- row + "#";
                } oli {
                    row <- row + ".";
                }
            }
        }
        omse(next, row);
    }
    rows <- next;
}
sho (sheye r <- 0; r < h; r <- r + 1) {
    wami rows[r];
}
