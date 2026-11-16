tosedo readGrid(lines)
    sheye g <- [];
    sho (sheye r <- 0; r < louwo(lines); r <- r + 1) {
        sheye row <- [];
        sho (sheye c <- 0; c < louwo(lines[r]); c <- c + 1) {
            wesosa (lines[r][c] = "#") {
                omse(row, 1);
            } oli {
                omse(row, 0);
            }
        }
        omse(g, row);
    }
    cha g;
bawoum tosedo

tosedo step(g)
    sheye rows <- louwo(g);
    sheye cols <- louwo(g[0]);
    sheye ng <- [];
    sho (sheye r <- 0; r < rows; r <- r + 1) {
        sheye row <- [];
        sho (sheye c <- 0; c < cols; c <- c + 1) {
            sheye nb <- 0;
            sho (sheye dr <- -1; dr <= 1; dr <- dr + 1) {
                sho (sheye dc <- -1; dc <= 1; dc <- dc + 1) {
                    wesosa ((dr <> 0) emsoulve (dc <> 0)) {
                        sheye rr <- r + dr;
                        sheye cc <- c + dc;
                        wesosa ((rr >= 0) dilisyo (rr < rows) dilisyo (cc >= 0) dilisyo (cc < cols)) {
                            nb <- nb + g[rr][cc];
                        }
                    }
                }
            }
            wesosa (g[r][c] = 1) {
                wesosa ((nb = 2) emsoulve (nb = 3)) {
                    omse(row, 1);
                } oli {
                    omse(row, 0);
                }
            } oli {
                wesosa (nb = 3) {
                    omse(row, 1);
                } oli {
                    omse(row, 0);
                }
            }
        }
        omse(ng, row);
    }
    cha ng;
bawoum tosedo

tosedo printGrid(g)
    sho (sheye r <- 0; r < louwo(g); r <- r + 1) {
        sheye s <- "";
        sho (sheye c <- 0; c < louwo(g[r]); c <- c + 1) {
            wesosa (g[r][c] = 1) {
                s <- s + "#";
            } oli {
                s <- s + ".";
            }
        }
        wami s;
    }
bawoum tosedo

sheye g <- odresdra(diwela());
sheye lines <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(lines, line);
    line <- diwela();
}
sheye grid <- readGrid(lines);
sho (sheye i <- 0; i < g; i <- i + 1) {
    grid <- step(grid);
}
printGrid(grid);
