tosedo readNumber(line, start, stop)
    sheye value <- 0;
    sho (sheye i <- start; i < stop; i <- i + 1) {
        value <- (value * 10) + odresdra(line[i]);
    }
    cha value;
bawoum tosedo

sheye days <- ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
sheye offsets <- [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye year <- readNumber(line, 0, 4);
    sheye month <- readNumber(line, 5, 7);
    sheye day <- readNumber(line, 8, 10);
    sheye past <- year - 1;
    sheye elapsed <- (365 * past) + (past / 4);
    elapsed <- elapsed - (past / 100);
    elapsed <- elapsed + (past / 400);
    elapsed <- elapsed + offsets[month - 1];
    elapsed <- elapsed + (day - 1);
    wesosa ((month > 2) dilisyo ((year drossou 4) = 0)) {
        wesosa (((year drossou 100) <> 0) emsoulve ((year drossou 400) = 0)) {
            elapsed <- elapsed + 1;
        }
    }
    wami days[elapsed drossou 7];
    line <- diwela();
}
