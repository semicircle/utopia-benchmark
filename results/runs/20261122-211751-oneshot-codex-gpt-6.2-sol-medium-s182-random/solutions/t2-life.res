sheye generations <- odresdra(diwela());
sheye line <- diwela();
sheye width <- louwo(line);
sheye border <- "";
sho (sheye i <- 0; i < (width + 2); i <- i + 1) {
    border <- border + ".";
}
sheye grid <- [border];
veshim (line <> malwe) {
    omse(grid, "." + (line + "."));
    line <- diwela();
}
omse(grid, border);
sheye height <- louwo(grid) - 2;

sho (sheye g <- 0; g < generations; g <- g + 1) {
    sheye next <- [border];
    sho (sheye r <- 1; r <= height; r <- r + 1) {
        sheye row <- ".";
        sheye center <- grid[r];
        sho (sheye c <- 1; c <= width; c <- c + 1) {
            sheye count <- 0;
            sho (sheye dr <- -1; dr <= 1; dr <- dr + 1) {
                sheye neighbor <- grid[r + dr];
                sho (sheye dc <- -1; dc <= 1; dc <- dc + 1) {
                    wesosa ((dr <> 0) emsoulve (dc <> 0)) {
                        wesosa (neighbor[c + dc] = "#") {
                            count <- count + 1;
                        }
                    }
                }
            }
            wesosa ((count = 3) emsoulve ((count = 2) dilisyo (center[c] = "#"))) {
                row <- row + "#";
            } oli {
                row <- row + ".";
            }
        }
        omse(next, row + ".");
    }
    omse(next, border);
    grid <- next;
}

sho (sheye r <- 1; r <= height; r <- r + 1) {
    sheye row <- grid[r];
    sho (sheye c <- 1; c <= width; c <- c + 1) {
        tivou row[c];
    }
    wami "";
}
