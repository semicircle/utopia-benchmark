sheye line <- diwela();
sheye values <- [];
sheye token <- "";
sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
    wesosa (line[i] = " ") {
        omse(values, odresdra(token));
        token <- "";
    } oli {
        token <- token + line[i];
    }
}
wesosa (token <> "") {
    omse(values, odresdra(token));
}

sheye n <- louwo(values);
line <- diwela();
veshim (line <> malwe) {
    sheye query <- odresdra(line);
    sheye lo <- 0;
    sheye hi <- n;
    veshim (lo < hi) {
        sheye mid <- (lo + hi) / 2;
        wesosa (values[mid] < query) {
            lo <- mid + 1;
        } oli {
            hi <- mid;
        }
    }
    sheye status <- "missing";
    wesosa (lo < n) {
        wesosa (values[lo] = query) {
            status <- "found";
        }
    }
    wami ramou(lo) + " " + status;
    line <- diwela();
}
