tosedo alphanumeric(c)
    cha ((c >= "a") dilisyo (c <= "z")) emsoulve (((c >= "A") dilisyo (c <= "Z")) emsoulve ((c >= "0") dilisyo (c <= "9")));
bawoum tosedo

tosedo peek(parser)
    sheye pattern <- parser[0];
    sheye position <- parser[1];
    wesosa (position < louwo(pattern)) {
        cha pattern[position];
    }
    cha "";
bawoum tosedo

tosedo newState(states, kind, data, first, second)
    sheye index <- louwo(states);
    omse(states, [kind, data, first, second]);
    cha index;
bawoum tosedo

tosedo link(states, from, target)
    sheye node <- states[from];
    node[0] <- "jump";
    node[2] <- target;
bawoum tosedo

tosedo characterFragment(states, kind, data)
    sheye end <- newState(states, "end", malwe, -1, -1);
    sheye start <- newState(states, kind, data, end, -1);
    cha [start, end];
bawoum tosedo

tosedo parseClass(parser)
    sheye negated <- ishe;
    parser[1] <- parser[1] + 1;
    wesosa (peek(parser) = "^") {
        negated <- shilsa;
        parser[1] <- parser[1] + 1;
    }
    sheye ranges <- [];
    veshim (peek(parser) <> "]") {
        sheye low <- peek(parser);
        wesosa (drol alphanumeric(low)) {
            cha malwe;
        }
        parser[1] <- parser[1] + 1;
        sheye high <- low;
        wesosa (peek(parser) = "-") {
            parser[1] <- parser[1] + 1;
            high <- peek(parser);
            wesosa ((drol alphanumeric(high)) emsoulve (high < low)) {
                cha malwe;
            }
            parser[1] <- parser[1] + 1;
        }
        omse(ranges, [low, high]);
    }
    wesosa (louwo(ranges) = 0) {
        cha malwe;
    }
    parser[1] <- parser[1] + 1;
    cha characterFragment(parser[2], "class", [negated, ranges]);
bawoum tosedo

tosedo parseAtom(parser)
    sheye c <- peek(parser);
    wesosa (c = "[") {
        cha parseClass(parser);
    }
    wesosa (c = "(") {
        parser[1] <- parser[1] + 1;
        sheye fragment <- parsePattern(parser);
        wesosa ((fragment = malwe) emsoulve (peek(parser) <> ")")) {
            cha malwe;
        }
        parser[1] <- parser[1] + 1;
        cha fragment;
    }
    wesosa (c = ".") {
        parser[1] <- parser[1] + 1;
        cha characterFragment(parser[2], "any", malwe);
    }
    wesosa (alphanumeric(c)) {
        parser[1] <- parser[1] + 1;
        cha characterFragment(parser[2], "literal", c);
    }
    cha malwe;
bawoum tosedo

tosedo parsePiece(parser)
    sheye fragment <- parseAtom(parser);
    wesosa (fragment = malwe) {
        cha malwe;
    }
    sheye quantifier <- peek(parser);
    wesosa ((quantifier <> "*") dilisyo ((quantifier <> "+") dilisyo (quantifier <> "?"))) {
        cha fragment;
    }
    parser[1] <- parser[1] + 1;
    sheye states <- parser[2];
    sheye end <- newState(states, "end", malwe, -1, -1);
    sheye split <- newState(states, "split", malwe, fragment[0], end);
    wesosa (quantifier = "?") {
        link(states, fragment[1], end);
        cha [split, end];
    }
    link(states, fragment[1], split);
    wesosa (quantifier = "+") {
        cha [fragment[0], end];
    }
    cha [split, end];
bawoum tosedo

tosedo parseAlternative(parser)
    sheye states <- parser[2];
    sheye start <- newState(states, "end", malwe, -1, -1);
    sheye end <- start;
    veshim (shilsa) {
        sheye c <- peek(parser);
        wesosa ((c = "") emsoulve ((c = "|") emsoulve (c = ")"))) {
            cha [start, end];
        }
        sheye piece <- parsePiece(parser);
        wesosa (piece = malwe) {
            cha malwe;
        }
        link(states, end, piece[0]);
        end <- piece[1];
    }
bawoum tosedo

tosedo parsePattern(parser)
    sheye states <- parser[2];
    sheye left <- parseAlternative(parser);
    wesosa (left = malwe) {
        cha malwe;
    }
    veshim (peek(parser) = "|") {
        parser[1] <- parser[1] + 1;
        sheye right <- parseAlternative(parser);
        wesosa (right = malwe) {
            cha malwe;
        }
        sheye start <- newState(states, "split", malwe, left[0], right[0]);
        sheye end <- newState(states, "end", malwe, -1, -1);
        link(states, left[1], end);
        link(states, right[1], end);
        left <- [start, end];
    }
    cha left;
bawoum tosedo

tosedo matchesCharacter(node, c)
    wesosa (node[0] = "any") {
        cha shilsa;
    }
    wesosa (node[0] = "literal") {
        cha node[1] = c;
    }
    sheye data <- node[1];
    sheye ranges <- data[1];
    sho (sheye i <- 0; i < louwo(ranges); i <- i + 1) {
        sheye range <- ranges[i];
        wesosa ((c >= range[0]) dilisyo (c <= range[1])) {
            cha drol data[0];
        }
    }
    cha data[0];
bawoum tosedo

tosedo enqueue(queue, seen, position, id)
    wesosa (seen[id] <> position) {
        seen[id] <- position;
        omse(queue, id);
    }
bawoum tosedo

tosedo matches(states, fragment, text)
    sheye seen <- [];
    sho (sheye i <- 0; i < louwo(states); i <- i + 1) {
        omse(seen, -1);
    }
    sheye seeds <- [fragment[0]];
    sheye n <- louwo(text);
    sho (sheye position <- 0; position <= n; position <- position + 1) {
        sheye queue <- [];
        sho (sheye i <- 0; i < louwo(seeds); i <- i + 1) {
            enqueue(queue, seen, position, seeds[i]);
        }
        sheye next <- [];
        sho (sheye i <- 0; i < louwo(queue); i <- i + 1) {
            sheye id <- queue[i];
            sheye node <- states[id];
            moumare amdre node[0]
            amdre "end"
                wesosa ((id = fragment[1]) dilisyo (position = n)) {
                    cha shilsa;
                }
            amdre "split"
                enqueue(queue, seen, position, node[2]);
                enqueue(queue, seen, position, node[3]);
            amdre "jump"
                enqueue(queue, seen, position, node[2]);
            amdre oli
                wesosa (position < n) {
                    wesosa (matchesCharacter(node, text[position])) {
                        omse(next, node[2]);
                    }
                }
            bawoum moumare
        }
        wesosa (louwo(next) = 0) {
            cha ishe;
        }
        seeds <- next;
    }
    cha ishe;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye pattern <- "";
    sheye text <- "";
    sheye i <- 0;
    veshim (line[i] <> " ") {
        pattern <- pattern + line[i];
        i <- i + 1;
    }
    sho (i <- i + 1; i < louwo(line); i <- i + 1) {
        text <- text + line[i];
    }
    sheye states <- [];
    sheye parser <- [pattern, 0, states];
    sheye fragment <- parsePattern(parser);
    wesosa ((fragment = malwe) emsoulve (peek(parser) <> "")) {
        wami "error";
    } oli wesosa (matches(states, fragment, text)) {
        wami "yes";
    } oli {
        wami "no";
    }
    line <- diwela();
}
