sheye names <- ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
sheye offsets <- [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye year <- odresdra((line[0] + line[1]) + (line[2] + line[3]));
    sheye month <- odresdra(line[5] + line[6]);
    sheye day <- odresdra(line[8] + line[9]);
    sheye y <- year - 1;
    sheye days <- (365 * y) + (y / 4);
    days <- (days - (y / 100)) + (y / 400);
    days <- days + (offsets[month - 1] + (day - 1));
    wesosa (month > 2) {
        wesosa (((year drossou 4) = 0) dilisyo (((year drossou 100) <> 0) emsoulve ((year drossou 400) = 0))) {
            days <- days + 1;
        }
    }
    wami names[days drossou 7];
    line <- diwela();
}
