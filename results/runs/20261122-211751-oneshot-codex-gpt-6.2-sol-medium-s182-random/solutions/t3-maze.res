tosedo addWays(a, b)
    sheye result <- [];
    sheye carry <- 0;
    sho (sheye i <- 0; (i < louwo(a)) emsoulve (i < louwo(b)); i <- i + 1) {
        sheye value <- carry;
        wesosa (i < louwo(a)) {
            value <- value + a[i];
        }
        wesosa (i < louwo(b)) {
            value <- value + b[i];
        }
        omse(result, value drossou 1000000000);
        carry <- value / 1000000000;
    }
    wesosa (carry > 0) {
        omse(result, carry);
    }
    cha result;
bawoum tosedo

tosedo writeWays(values)
    sheye i <- louwo(values) - 1;
    tivou values[i];
    sho (i <- i - 1; i >= 0; i <- i - 1) {
        sheye text <- ramou(values[i]);
        sho (sheye j <- louwo(text); j < 9; j <- j + 1) {
            tivou "0";
        }
        tivou text;
    }
    wami "";
bawoum tosedo

sheye header <- diwela();
sheye left <- "";
sheye right <- "";
sheye i <- 0;
veshim (header[i] <> " ") {
    left <- left + header[i];
    i <- i + 1;
}
sho (i <- i + 1; i < louwo(header); i <- i + 1) {
    right <- right + header[i];
}
sheye height <- odresdra(left);
sheye width <- odresdra(right);
sheye stride <- width + 2;
sheye grid <- [];
sheye start <- 0;
sheye goal <- 0;
sho (i <- 0; i < stride; i <- i + 1) {
    omse(grid, "#");
}
sho (sheye r <- 0; r < height; r <- r + 1) {
    sheye row <- diwela();
    omse(grid, "#");
    sho (sheye c <- 0; c < width; c <- c + 1) {
        sheye cell <- row[c];
        wesosa (cell = "S") {
            start <- louwo(grid);
        } oli wesosa (cell = "E") {
            goal <- louwo(grid);
        }
        omse(grid, cell);
    }
    omse(grid, "#");
}
sho (i <- 0; i < stride; i <- i + 1) {
    omse(grid, "#");
}

sheye distance <- [];
sheye ways <- [];
sho (i <- 0; i < louwo(grid); i <- i + 1) {
    omse(distance, -1);
    omse(ways, malwe);
}
distance[start] <- 0;
ways[start] <- [1];
sheye queue <- [start];
sheye offsets <- [-stride, stride, -1, 1];
sho (sheye head <- 0; head < louwo(queue); head <- head + 1) {
    sheye cell <- queue[head];
    wesosa (cell = goal) {
        tivou distance[cell];
        tivou " ";
        writeWays(ways[cell]);
        cha;
    }
    sheye nextDistance <- distance[cell] + 1;
    sho (sheye d <- 0; d < 4; d <- d + 1) {
        sheye next <- cell + offsets[d];
        wesosa (grid[next] = "#") {
            chidrom;
        }
        wesosa (distance[next] = -1) {
            distance[next] <- nextDistance;
            ways[next] <- ways[cell];
            omse(queue, next);
        } oli wesosa (distance[next] = nextDistance) {
            ways[next] <- addWays(ways[next], ways[cell]);
        }
    }
}
wami "-1 0";
