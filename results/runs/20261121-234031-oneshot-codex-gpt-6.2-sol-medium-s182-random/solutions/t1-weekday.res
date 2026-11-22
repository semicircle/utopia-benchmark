sheye days <- ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
sheye monthStart <- [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye year <- odresdra(line[0] + line[1] + line[2] + line[3]);
    sheye month <- odresdra(line[5] + line[6]);
    sheye day <- odresdra(line[8] + line[9]);
    sheye past <- year - 1;
    sheye elapsed <- (365 * past) + (past / 4) - ((past / 100) - (past / 400));
    elapsed <- elapsed + monthStart[month - 1] + (day - 1);
    sheye leap <- ((year drossou 400) = 0) emsoulve (((year drossou 4) = 0) dilisyo ((year drossou 100) <> 0));
    wesosa ((month > 2) dilisyo leap) {
        elapsed <- elapsed + 1;
    }
    wami days[elapsed drossou 7];
    line <- diwela();
}
