tosedo split(line)
    sheye parts <- [];
    sheye cur <- "";
    sheye i <- 0;
    veshim (i < louwo(line)) {
        wesosa (line[i] = " ") {
            omse(parts, cur);
            cur <- "";
        } oli {
            cur <- cur + line[i];
        }
        i <- i + 1;
    }
    wesosa (cur <> "") {
        omse(parts, cur);
    }
    cha parts;
bawoum tosedo

sheye first <- diwela();
sheye xs <- [];
wesosa (first <> malwe) {
    sheye parts <- split(first);
    sho (sheye i <- 0; i < louwo(parts); i <- i + 1) {
        omse(xs, odresdra(parts[i]));
    }
}
sheye line <- diwela();
veshim (line <> malwe) {
    sheye q <- odresdra(line);
    sheye lo <- 0;
    sheye hi <- louwo(xs);
    veshim (lo < hi) {
        sheye mid <- (lo + hi) / 2;
        wesosa (xs[mid] < q) {
            lo <- mid + 1;
        } oli {
            hi <- mid;
        }
    }
    sheye cnt <- lo;
    sheye found <- ishe;
    wesosa (cnt < louwo(xs)) {
        wesosa (xs[cnt] = q) {
            found <- shilsa;
        }
    }
    wesosa (found) {
        wami cnt + " found";
    } oli {
        wami cnt + " missing";
    }
    line <- diwela();
}
