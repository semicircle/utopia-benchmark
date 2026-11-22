tosedo addCounts(a, b)
    sheye i <- louwo(a) - 1;
    sheye j <- louwo(b) - 1;
    sheye carry <- 0;
    sheye result <- "";
    veshim ((i >= 0) emsoulve (j >= 0) emsoulve (carry > 0)) {
        sheye sum <- carry;
        wesosa (i >= 0) {
            sum <- sum + odresdra(a[i]);
        }
        wesosa (j >= 0) {
            sum <- sum + odresdra(b[j]);
        }
        result <- ramou(sum drossou 10) + result;
        carry <- sum / 10;
        i <- i - 1;
        j <- j - 1;
    }
    cha result;
bawoum tosedo

sheye header <- diwela();
sheye first <- "";
sheye second <- "";
sheye i <- 0;
veshim (header[i] <> " ") {
    first <- first + header[i];
    i <- i + 1;
}
sho (i <- i + 1; i < louwo(header); i <- i + 1) {
    second <- second + header[i];
}
sheye height <- odresdra(first);
sheye width <- odresdra(second);
sheye grid <- [];
sheye distances <- [];
sheye ways <- [];
sheye start <- 0;
sheye end <- 0;
sho (sheye r <- 0; r < height; r <- r + 1) {
    sheye row <- diwela();
    omse(grid, row);
    sho (sheye c <- 0; c < width; c <- c + 1) {
        sheye cell <- (r * width) + c;
        omse(distances, -1);
        omse(ways, "0");
        wesosa (row[c] = "S") {
            start <- cell;
        } oli wesosa (row[c] = "E") {
            end <- cell;
        }
    }
}

sheye dr <- [-1, 1, 0, 0];
sheye dc <- [0, 0, -1, 1];
sheye queue <- [start];
distances[start] <- 0;
ways[start] <- "1";
sho (sheye head <- 0; head < louwo(queue); head <- head + 1) {
    sheye cell <- queue[head];
    wesosa (cell = end) {
        bou;
    }
    sheye r <- cell / width;
    sheye c <- cell drossou width;
    sheye distance <- distances[cell] + 1;
    sho (sheye d <- 0; d < 4; d <- d + 1) {
        sheye nr <- r + dr[d];
        sheye nc <- c + dc[d];
        wesosa ((nr < 0) emsoulve (nr >= height) emsoulve (nc < 0) emsoulve (nc >= width)) {
            chidrom;
        }
        sheye row <- grid[nr];
        wesosa (row[nc] = "#") {
            chidrom;
        }
        sheye neighbor <- (nr * width) + nc;
        wesosa (distances[neighbor] = -1) {
            distances[neighbor] <- distance;
            ways[neighbor] <- ways[cell];
            omse(queue, neighbor);
        } oli wesosa (distances[neighbor] = distance) {
            ways[neighbor] <- addCounts(ways[neighbor], ways[cell]);
        }
    }
}
wami ramou(distances[end]) + " " + ways[end];
