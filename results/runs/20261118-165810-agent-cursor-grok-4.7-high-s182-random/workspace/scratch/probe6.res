sheye rows <- [];
sheye i <- 0;
sheye row <- [];
veshim (i < 3) {
    row <- [];
    omse(row, i);
    omse(rows, row);
    i <- i + 1;
}
sheye row0 <- rows[0];
row0[0] <- 9;
wami rows;

sheye pairs <- [];
i <- 0;
veshim (i < 3) {
    omse(pairs, [i, 1]);
    i <- i + 1;
}
sheye p <- pairs[1];
p[1] <- 5;
wami pairs;
