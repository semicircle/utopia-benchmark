sheye g <- odresdra(diwela());
sheye grid <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(line) > 0) {
        sheye row <- [];
        sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
            wesosa (line[i] = "#") {
                omse(row, 1);
            } oli {
                omse(row, 0);
            }
        }
        omse(grid, row);
    }
    line <- diwela();
}
sheye h <- louwo(grid);
sheye w <- 0;
wesosa (h > 0) {
    w <- louwo(grid[0]);
}
sho (sheye gen <- 0; gen < g; gen <- gen + 1) {
    sheye ng <- [];
    sho (sheye r <- 0; r < h; r <- r + 1) {
        sheye nrow <- [];
        sho (sheye c <- 0; c < w; c <- c + 1) {
            sheye cnt <- 0;
            sho (sheye dr <- -1; dr <= 1; dr <- dr + 1) {
                sho (sheye dc <- -1; dc <= 1; dc <- dc + 1) {
                    sheye rr <- r + dr;
                    sheye cc <- c + dc;
                    wesosa (((dr <> 0) emsoulve (dc <> 0)) dilisyo (((rr >= 0) dilisyo (rr < h)) dilisyo ((cc >= 0) dilisyo (cc < w)))) {
                        cnt <- cnt + grid[rr][cc];
                    }
                }
            }
            sheye alive <- grid[r][c];
            wesosa (cnt = 3) {
                omse(nrow, 1);
            } oli wesosa ((cnt = 2) dilisyo (alive = 1)) {
                omse(nrow, 1);
            } oli {
                omse(nrow, 0);
            }
        }
        omse(ng, nrow);
    }
    grid <- ng;
}
sho (sheye r <- 0; r < h; r <- r + 1) {
    sheye s <- "";
    sho (sheye c <- 0; c < w; c <- c + 1) {
        wesosa (grid[r][c] = 1) {
            s <- s + "#";
        } oli {
            s <- s + ".";
        }
    }
    wami s;
}
