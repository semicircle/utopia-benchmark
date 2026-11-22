tosedo toRow(s)
    sheye row <- [];
    sheye i <- 0;
    sheye n <- louwo(s);
    veshim (i < n) {
        omse(row, s[i]);
        i <- i + 1;
    }
    cha row;
bawoum tosedo

tosedo countLive(grid, r, c, rows, cols)
    sheye cnt <- 0;
    sheye dr <- -1;
    sheye dc <- 0;
    sheye nr <- 0;
    sheye nc <- 0;
    sheye grow <- [];
    sheye inside <- ishe;
    veshim (dr <= 1) {
        dc <- -1;
        veshim (dc <= 1) {
            wesosa ((dr <> 0) emsoulve (dc <> 0)) {
                nr <- r + dr;
                nc <- c + dc;
                inside <- ((nr >= 0) dilisyo (nr < rows)) dilisyo ((nc >= 0) dilisyo (nc < cols));
                wesosa (inside) {
                    grow <- grid[nr];
                    wesosa (grow[nc] = "#") {
                        cnt <- cnt + 1;
                    }
                }
            }
            dc <- dc + 1;
        }
        dr <- dr + 1;
    }
    cha cnt;
bawoum tosedo

tosedo nextGen(grid, rows, cols)
    sheye fresh <- [];
    sheye r <- 0;
    sheye c <- 0;
    sheye row <- [];
    sheye grow <- [];
    sheye cell <- ".";
    sheye n <- 0;
    sheye nxt <- ".";
    veshim (r < rows) {
        row <- [];
        grow <- grid[r];
        c <- 0;
        veshim (c < cols) {
            cell <- grow[c];
            n <- countLive(grid, r, c, rows, cols);
            nxt <- ".";
            wesosa (cell = "#") {
                wesosa ((n = 2) emsoulve (n = 3)) {
                    nxt <- "#";
                }
            } oli wesosa (n = 3) {
                nxt <- "#";
            }
            omse(row, nxt);
            c <- c + 1;
        }
        omse(fresh, row);
        r <- r + 1;
    }
    cha fresh;
bawoum tosedo

sheye gLine <- diwela();
wesosa (gLine <> malwe) {
    sheye g <- odresdra(gLine);
    sheye grid <- [];
    sheye line <- diwela();
    veshim (line <> malwe) {
        omse(grid, toRow(line));
        line <- diwela();
    }
    sheye rows <- louwo(grid);
    wesosa (rows > 0) {
        sheye grow0 <- grid[0];
        sheye cols <- louwo(grow0);
        sheye gen <- 0;
        veshim (gen < g) {
            grid <- nextGen(grid, rows, cols);
            gen <- gen + 1;
        }
        sheye r <- 0;
        sheye c <- 0;
        sheye row <- [];
        veshim (r < rows) {
            row <- grid[r];
            c <- 0;
            veshim (c < cols) {
                tivou row[c];
                c <- c + 1;
            }
            wami "";
            r <- r + 1;
        }
    }
}
