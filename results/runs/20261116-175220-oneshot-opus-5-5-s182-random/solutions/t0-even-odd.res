sheye ev <- 0;
sheye od <- 0;
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (louwo(line) > 0) {
        sheye n <- odresdra(line);
        wesosa ((n drossou 2) = 0) {
            ev <- ev + 1;
        } oli {
            od <- od + 1;
        }
    }
    line <- diwela();
}
wami "even " + ev;
wami "odd " + od;
