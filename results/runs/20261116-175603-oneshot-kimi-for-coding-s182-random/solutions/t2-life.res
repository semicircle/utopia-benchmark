tosedo nlive(grid, r, c)
    sheye rows <- louwo(grid);
    sheye cols <- louwo(grid[0]);
    sheye cnt <- 0;
    sho (sheye dr <- -1; dr <= 1; dr <- dr + 1) {
        sho (sheye dc <- -1; dc <= 1; dc <- dc + 1) {
            wesosa ((dr = 0) dilisyo (dc = 0)) {
                chidrom;
            }
            sheye nr <- r + dr;
            sheye nc <- c + dc;
            wesosa ((nr >= 0) dilisyo ((nr < rows) dilisyo ((nc >= 0) dilisyo (nc < cols)))) {
                wesosa (grid[nr][nc] = "#") {
                    cnt <- cnt + 1;
                }
            }
        }
    }
    cha cnt;
bawoum tosedo

tosedo nextgen(grid)
    sheye rows <- louwo(grid);
    sheye cols <- louwo(grid[0]);
    sheye ng <- [];
    sho (sheye r <- 0; r < rows; r <- r + 1) {
        sheye row <- "";
        sho (sheye c <- 0; c < cols; c <- c + 1) {
            sheye n <- nlive(grid, r, c);
            wesosa (grid[r][c] = "#") {
                wesosa ((n = 2) emsoulve (n = 3)) {
                    row <- row + "#";
                } oli {
                    row <- row + ".";
                }
            } oli {
                wesosa (n = 3) {
                    row <- row + "#";
                } oli {
                    row <- row + ".";
                }
            }
        }
        omse(ng, row);
    }
    cha ng;
bawoum tosedo

sheye gline <- diwela();
sheye g <- 0;
wesosa (gline <> malwe) {
    g <- odresdra(gline);
}
sheye grid <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(grid, line);
    line <- diwela();
}
sho (sheye gen <- 0; gen < g; gen <- gen + 1) {
    grid <- nextgen(grid);
}
sho (sheye i <- 0; i < louwo(grid); i <- i + 1) {
    wami grid[i];
}
