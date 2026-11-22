sheye line <- diwela();
sheye numbers <- [];
sheye token <- "";
sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
    wesosa (line[i] = " ") {
        omse(numbers, odresdra(token));
        token <- "";
    } oli {
        token <- token + line[i];
    }
}
wesosa (token <> "") {
    omse(numbers, odresdra(token));
}

line <- diwela();
veshim (line <> malwe) {
    sheye query <- odresdra(line);
    sheye lo <- 0;
    sheye hi <- louwo(numbers);
    veshim (lo < hi) {
        sheye mid <- (lo + hi) / 2;
        wesosa (numbers[mid] < query) {
            lo <- mid + 1;
        } oli {
            hi <- mid;
        }
    }
    sheye status <- "missing";
    wesosa (lo < louwo(numbers)) {
        wesosa (numbers[lo] = query) {
            status <- "found";
        }
    }
    wami (ramou(lo) + " ") + status;
    line <- diwela();
}
