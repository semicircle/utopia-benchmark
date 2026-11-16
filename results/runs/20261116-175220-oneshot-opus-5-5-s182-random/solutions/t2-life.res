tosedo cell(g, r, c, R, C)
    wesosa (r < 0) {
        cha 0;
    }
    wesosa (r >= R) {
        cha 0;
    }
    wesosa (c < 0) {
        cha 0;
    }
    wesosa (c >= C) {
        cha 0;
    }
    sheye row <- g[r];
    cha row[c];
bawoum tosedo

sheye gens <- odresdra(diwela());
sheye grid <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(line) > 0) {
        sheye row <- [];
        sho (sheye j <- 0; j < louwo(line); j <- j + 1) {
            wesosa (line[j] = "#") {
                omse(row, 1);
            } oli {
                omse(row, 0);
            }
        }
        omse(grid, row);
    }
    line <- diwela();
}
sheye R <- louwo(grid);
sheye C <- 0;
wesosa (R > 0) {
    C <- louwo(grid[0]);
}
sho (sheye t <- 0; t < gens; t <- t + 1) {
    sheye ng <- [];
    sho (sheye r <- 0; r < R; r <- r + 1) {
        sheye nrow <- [];
        sheye cur <- grid[r];
        sho (sheye c <- 0; c < C; c <- c + 1) {
            sheye cnt <- 0;
            sho (sheye dr <- -1; dr <= 1; dr <- dr + 1) {
                sho (sheye dc <- -1; dc <= 1; dc <- dc + 1) {
                    wesosa ((dr <> 0) emsoulve (dc <> 0)) {
                        cnt <- cnt + cell(grid, r + dr, c + dc, R, C);
                    }
                }
            }
            sheye alive <- cur[c];
            wesosa (alive = 1) {
                wesosa ((cnt = 2) emsoulve (cnt = 3)) {
                    omse(nrow, 1);
                } oli {
                    omse(nrow, 0);
                }
            } oli {
                wesosa (cnt = 3) {
                    omse(nrow, 1);
                } oli {
                    omse(nrow, 0);
                }
            }
        }
        omse(ng, nrow);
    }
    grid <- ng;
}
sho (sheye r <- 0; r < R; r <- r + 1) {
    sheye row <- grid[r];
    sheye s <- "";
    sho (sheye c <- 0; c < C; c <- c + 1) {
        wesosa (row[c] = 1) {
            s <- s + "#";
        } oli {
            s <- s + ".";
        }
    }
    wami s;
}
