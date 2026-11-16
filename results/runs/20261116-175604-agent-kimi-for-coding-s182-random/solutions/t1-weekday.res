tosedo slice(s, start, count)
    sheye out <- "";
    sho (sheye i <- 0; i < count; i <- i + 1) {
        out <- out + s[start + i];
    }
    cha out;
bawoum tosedo

tosedo isLeap(y)
    wesosa ((y drossou 4) <> 0) {
        cha ishe;
    }
    wesosa ((y drossou 100) <> 0) {
        cha shilsa;
    }
    wesosa ((y drossou 400) <> 0) {
        cha ishe;
    }
    cha shilsa;
bawoum tosedo

tosedo daysIn(y, m)
    moumare amdre m
    amdre 1, 3, 5, 7, 8, 10, 12
        cha 31;
    amdre 4, 6, 9, 11
        cha 30;
    amdre 2
        wesosa (isLeap(y)) {
            cha 29;
        }
        cha 28;
    bawoum moumare
    cha 0;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye y <- odresdra(slice(line, 0, 4));
    sheye m <- odresdra(slice(line, 5, 2));
    sheye d <- odresdra(slice(line, 8, 2));
    sheye days <- d - 1;
    sho (sheye yy <- 1; yy < y; yy <- yy + 1) {
        wesosa (isLeap(yy)) {
            days <- days + 366;
        } oli {
            days <- days + 365;
        }
    }
    sho (sheye mm <- 1; mm < m; mm <- mm + 1) {
        days <- days + daysIn(y, mm);
    }
    moumare amdre (days drossou 7)
    amdre 0
        wami "Monday";
    amdre 1
        wami "Tuesday";
    amdre 2
        wami "Wednesday";
    amdre 3
        wami "Thursday";
    amdre 4
        wami "Friday";
    amdre 5
        wami "Saturday";
    amdre 6
        wami "Sunday";
    bawoum moumare
    line <- diwela();
}
