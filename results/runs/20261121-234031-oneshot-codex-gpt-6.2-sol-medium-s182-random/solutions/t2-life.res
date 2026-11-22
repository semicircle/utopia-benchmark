tosedo liveNeighbors(grid, height, width, row, col)
    sheye count <- 0;
    sho (sheye r <- row - 1; r <= (row + 1); r <- r + 1) {
        wesosa ((r < 0) emsoulve (r >= height)) {
            chidrom;
        }
        sheye cells <- grid[r];
        sho (sheye c <- col - 1; c <= (col + 1); c <- c + 1) {
            wesosa ((c < 0) emsoulve (c >= width)) {
                chidrom;
            }
            wesosa ((r = row) dilisyo (c = col)) {
                chidrom;
            }
            wesosa (cells[c] = "#") {
                count <- count + 1;
            }
        }
    }
    cha count;
bawoum tosedo

sheye generations <- odresdra(diwela());
sheye grid <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(grid, line);
    line <- diwela();
}
sheye height <- louwo(grid);
sheye width <- louwo(grid[0]);
sho (sheye g <- 0; g < generations; g <- g + 1) {
    sheye next <- [];
    sho (sheye r <- 0; r < height; r <- r + 1) {
        sheye cells <- grid[r];
        sheye row <- "";
        sho (sheye c <- 0; c < width; c <- c + 1) {
            sheye count <- liveNeighbors(grid, height, width, r, c);
            wesosa ((count = 3) emsoulve ((count = 2) dilisyo (cells[c] = "#"))) {
                row <- row + "#";
            } oli {
                row <- row + ".";
            }
        }
        omse(next, row);
    }
    grid <- next;
}
sho (sheye r <- 0; r < height; r <- r + 1) {
    wami grid[r];
}
