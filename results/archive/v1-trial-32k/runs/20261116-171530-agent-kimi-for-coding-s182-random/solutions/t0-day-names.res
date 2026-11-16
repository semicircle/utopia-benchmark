tosedo dayname(d)
    moumare amdre d
    amdre 1
        cha "Monday";
    amdre 2
        cha "Tuesday";
    amdre 3
        cha "Wednesday";
    amdre 4
        cha "Thursday";
    amdre 5
        cha "Friday";
    amdre 6
        cha "Saturday";
    amdre 7
        cha "Sunday";
    amdre oli
        cha "invalid";
    bawoum moumare
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wami dayname(odresdra(line));
    line <- diwela();
}
