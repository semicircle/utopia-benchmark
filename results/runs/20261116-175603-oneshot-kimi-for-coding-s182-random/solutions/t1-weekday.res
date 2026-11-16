tosedo isleap(y)
    sheye a <- (y drossou 4) = 0;
    sheye b <- (y drossou 100) <> 0;
    sheye c <- (y drossou 400) = 0;
    cha (a dilisyo (b emsoulve c));
bawoum tosedo

tosedo mdays(y, m)
    moumare amdre m
    amdre 2
        wesosa (isleap(y)) {
            cha 29;
        }
        cha 28;
    amdre 4, 6, 9, 11
        cha 30;
    amdre oli
        cha 31;
    bawoum moumare
bawoum tosedo

tosedo slice(s, i, j)
    sheye r <- "";
    sho (sheye k <- i; k < j; k <- k + 1) {
        r <- r + s[k];
    }
    cha r;
bawoum tosedo

sheye names <- ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye y <- odresdra(slice(line, 0, 4));
    sheye m <- odresdra(slice(line, 5, 7));
    sheye d <- odresdra(slice(line, 8, 10));
    sheye doy <- d;
    sho (sheye mm <- 1; mm < m; mm <- mm + 1) {
        doy <- doy + mdays(y, mm);
    }
    sheye yy <- y - 1;
    sheye leaps <- ((yy / 4) - (yy / 100)) + (yy / 400);
    sheye days <- ((yy * 365) + leaps) + (doy - 1);
    sheye wd <- days drossou 7;
    wami names[wd];
    line <- diwela();
}
