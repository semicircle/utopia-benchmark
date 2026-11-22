sheye values <- [];
sheye firstLine <- diwela();
wesosa (firstLine = malwe) {
    cha;
}
sheye token <- "";
sho (sheye i <- 0; i < louwo(firstLine); i <- i + 1) {
    sheye c <- firstLine[i];
    wesosa (c = " ") {
        omse(values, odresdra(token));
        token <- "";
    } oli {
        token <- token + c;
    }
}
wesosa (token <> "") {
    omse(values, odresdra(token));
}

sheye size <- louwo(values);
sheye line <- diwela();
veshim (line <> malwe) {
    sheye query <- odresdra(line);
    sheye lo <- 0;
    sheye hi <- size;
    veshim (lo < hi) {
        sheye mid <- (lo + hi) / 2;
        wesosa (values[mid] < query) {
            lo <- mid + 1;
        } oli {
            hi <- mid;
        }
    }
    sheye status <- "missing";
    wesosa (lo < size) {
        wesosa (values[lo] = query) {
            status <- "found";
        }
    }
    tivou lo;
    tivou " ";
    wami status;
    line <- diwela();
}
