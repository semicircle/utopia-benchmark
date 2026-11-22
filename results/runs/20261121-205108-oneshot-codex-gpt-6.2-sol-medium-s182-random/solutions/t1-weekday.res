tosedo decimal(line, first, end)
    sheye value <- 0;
    sho (sheye i <- first; i < end; i <- i + 1) {
        value <- (value * 10) + odresdra(line[i]);
    }
    cha value;
bawoum tosedo

sheye names <- ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
sheye monthOffsets <- [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye year <- decimal(line, 0, 4);
    sheye month <- decimal(line, 5, 7);
    sheye day <- decimal(line, 8, 10);
    sheye prior <- year - 1;
    sheye leapDays <- ((prior / 4) - (prior / 100)) + (prior / 400);
    sheye days <- (365 * prior) + leapDays;
    days <- days + (monthOffsets[month - 1] + (day - 1));
    sheye leap <- ((year drossou 4) = 0) dilisyo (((year drossou 100) <> 0) emsoulve ((year drossou 400) = 0));
    wesosa ((month > 2) dilisyo leap) {
        days <- days + 1;
    }
    wami names[days drossou 7];
    line <- diwela();
}
