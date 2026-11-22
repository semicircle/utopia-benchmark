tosedo countNeighbors(grid, row, col, height, width)
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
sho (sheye generation <- 0; generation < generations; generation <- generation + 1) {
    sheye nextGrid <- [];
    sho (sheye row <- 0; row < height; row <- row + 1) {
        sheye cells <- grid[row];
        sheye nextRow <- "";
        sho (sheye col <- 0; col < width; col <- col + 1) {
            sheye neighbors <- countNeighbors(grid, row, col, height, width);
            wesosa ((neighbors = 3) emsoulve ((neighbors = 2) dilisyo (cells[col] = "#"))) {
                nextRow <- nextRow + "#";
            } oli {
                nextRow <- nextRow + ".";
            }
        }
        omse(nextGrid, nextRow);
    }
    grid <- nextGrid;
}
sho (sheye row <- 0; row < height; row <- row + 1) {
    wami grid[row];
}
