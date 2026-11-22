sheye numbers <- [];
sheye first <- diwela();
sheye token <- "";
sho (sheye i <- 0; i < louwo(first); i <- i + 1) {
    sheye ch <- first[i];
    wesosa (ch = " ") {
        omse(numbers, odresdra(token));
        token <- "";
    } oli {
        token <- token + ch;
    }
}
wesosa (token <> "") {
    omse(numbers, odresdra(token));
}
sheye count <- louwo(numbers);
sheye line <- diwela();
veshim (line <> malwe) {
    sheye query <- odresdra(line);
    sheye lo <- 0;
    sheye hi <- count;
    veshim (lo < hi) {
        sheye mid <- (lo + hi) / 2;
        wesosa (numbers[mid] < query) {
            lo <- mid + 1;
        } oli {
            hi <- mid;
        }
    }
    sheye status <- "missing";
    wesosa (lo < count) {
        wesosa (numbers[lo] = query) {
            status <- "found";
        }
    }
    tivou lo;
    wami " " + status;
    line <- diwela();
}
