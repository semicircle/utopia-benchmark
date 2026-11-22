' Real cells occupy IDs 0 through 2573. A rectangle is decomposed into
' products of row and column intervals in two binary segment trees.
' Node fields: state, dependencies, formula tree, error, sum, min, max.

tosedo digit(c)
    cha (c >= "0") dilisyo (c <= "9");
bawoum tosedo

tosedo letter(c)
    cha ((c >= "A") dilisyo (c <= "Z")) emsoulve ((c >= "a") dilisyo (c <= "z"));
bawoum tosedo

tosedo cellId(name, columns)
    sheye n <- louwo(name);
    wesosa ((n < 2) emsoulve (n > 3)) {
        cha -1;
    }
    wesosa ((name[0] < "A") emsoulve (name[0] > "Z")) {
        cha -1;
    }
    wesosa (name[1] = "0") {
        cha -1;
    }
    sheye row <- 0;
    sho (sheye i <- 1; i < n; i <- i + 1) {
        wesosa (drol digit(name[i])) {
            cha -1;
        }
        row <- (row * 10) + odresdra(name[i]);
    }
    sheye column <- 0;
    veshim (columns[column] <> name[0]) {
        column <- column + 1;
    }
    cha ((row - 1) * 26) + column;
bawoum tosedo

tosedo tokenize(line, start, columns)
    sheye tokens <- [];
    sheye n <- louwo(line);
    sheye i <- start;
    veshim (i < n) {
        sheye c <- line[i];
        i <- i + 1;
        wesosa (c = " ") {
            chidrom;
        }
        wesosa (digit(c)) {
            sheye number <- odresdra(c);
            veshim (i < n) {
                wesosa (drol digit(line[i])) {
                    bou;
                }
                number <- (number * 10) + odresdra(line[i]);
                i <- i + 1;
            }
            omse(tokens, ["number", number]);
        } oli wesosa (letter(c)) {
            sheye name <- c;
            veshim (i < n) {
                wesosa (drol (letter(line[i]) emsoulve digit(line[i]))) {
                    bou;
                }
                name <- name + line[i];
                i <- i + 1;
            }
            moumare amdre name
            amdre "SUM", "MIN", "MAX"
                omse(tokens, ["function", name]);
            amdre oli
                sheye id <- cellId(name, columns);
                wesosa (id >= 0) {
                    omse(tokens, ["cell", id]);
                } oli {
                    omse(tokens, ["bad", malwe]);
                }
            bawoum moumare
        } oli {
            moumare amdre c
            amdre "+", "-", "*", "/", "%", "(", ")", ",", ":"
                omse(tokens, [c, malwe]);
            amdre oli
                omse(tokens, ["bad", malwe]);
            bawoum moumare
        }
    }
    omse(tokens, ["end", malwe]);
    cha tokens;
bawoum tosedo

tosedo intervalParts(lo, hi, base)
    sheye parts <- [];
    lo <- lo + base;
    hi <- hi + base;
    veshim (lo <= hi) {
        wesosa ((lo drossou 2) = 1) {
            omse(parts, lo);
            lo <- lo + 1;
        }
        wesosa ((hi drossou 2) = 0) {
            omse(parts, hi);
            hi <- hi - 1;
        }
        lo <- lo / 2;
        hi <- hi / 2;
    }
    cha parts;
bawoum tosedo

tosedo rectangleNode(graph, row, column)
    wesosa ((row >= 128) dilisyo (column >= 32)) {
        cha ((row - 128) * 26) + (column - 32);
    }
    sheye id <- 2574 + ((row * 64) + column);
    wesosa (graph[id] = malwe) {
        sheye first <- 0;
        sheye second <- 0;
        wesosa (row < 128) {
            first <- rectangleNode(graph, row * 2, column);
            second <- rectangleNode(graph, (row * 2) + 1, column);
        } oli {
            first <- rectangleNode(graph, row, column * 2);
            second <- rectangleNode(graph, row, (column * 2) + 1);
        }
        graph[id] <- [0, [first, second], malwe, 0, 0, 0, 0];
    }
    cha id;
bawoum tosedo

tosedo rangeParts(graph, a, b)
    sheye r1 <- a / 26;
    sheye r2 <- b / 26;
    sheye c1 <- a drossou 26;
    sheye c2 <- b drossou 26;
    wesosa (r1 > r2) {
        sheye temp <- r1;
        r1 <- r2;
        r2 <- temp;
    }
    wesosa (c1 > c2) {
        sheye temp <- c1;
        c1 <- c2;
        c2 <- temp;
    }
    sheye rows <- intervalParts(r1, r2, 128);
    sheye columns <- intervalParts(c1, c2, 32);
    sheye parts <- [];
    sho (sheye r <- 0; r < louwo(rows); r <- r + 1) {
        sho (sheye c <- 0; c < louwo(columns); c <- c + 1) {
            omse(parts, rectangleNode(graph, rows[r], columns[c]));
        }
    }
    cha parts;
bawoum tosedo

tosedo dependencies(tokens, graph)
    sheye deps <- [];
    sho (sheye i <- 0; i < (louwo(tokens) - 1); i <- i + 1) {
        sheye token <- tokens[i];
        wesosa (token[0] <> "cell") {
            chidrom;
        }
        omse(deps, token[1]);
        sheye colon <- tokens[i + 1];
        wesosa (colon[0] = ":") {
            sheye next <- tokens[i + 2];
            wesosa (next[0] = "cell") {
                sheye parts <- rangeParts(graph, token[1], next[1]);
                colon[1] <- parts;
                sho (sheye j <- 0; j < louwo(parts); j <- j + 1) {
                    omse(deps, parts[j]);
                }
            }
        }
    }
    cha deps;
bawoum tosedo

tosedo current(parser)
    sheye tokens <- parser[0];
    cha tokens[parser[1]];
bawoum tosedo

tosedo kind(parser)
    sheye token <- current(parser);
    cha token[0];
bawoum tosedo

tosedo parseArgument(parser)
    wesosa (kind(parser) = "cell") {
        sheye tokens <- parser[0];
        sheye colon <- tokens[parser[1] + 1];
        wesosa (colon[0] = ":") {
            wesosa (colon[1] = malwe) {
                cha malwe;
            }
            parser[1] <- parser[1] + 3;
            cha ["range", colon[1]];
        }
    }
    cha parseSum(parser);
bawoum tosedo

tosedo parseFunction(parser, name)
    wesosa (kind(parser) <> "(") {
        cha malwe;
    }
    parser[1] <- parser[1] + 1;
    sheye args <- [];
    veshim (shilsa) {
        sheye arg <- parseArgument(parser);
        wesosa (arg = malwe) {
            cha malwe;
        }
        omse(args, arg);
        sheye next <- kind(parser);
        wesosa (next = ")") {
            parser[1] <- parser[1] + 1;
            cha ["function", name, args];
        }
        wesosa (next <> ",") {
            cha malwe;
        }
        parser[1] <- parser[1] + 1;
    }
bawoum tosedo

tosedo parsePrimary(parser)
    sheye negative <- ishe;
    veshim (kind(parser) = "-") {
        negative <- drol negative;
        parser[1] <- parser[1] + 1;
    }
    sheye token <- current(parser);
    sheye tree <- malwe;
    moumare amdre token[0]
    amdre "number", "cell"
        tree <- token;
        parser[1] <- parser[1] + 1;
    amdre "("
        parser[1] <- parser[1] + 1;
        tree <- parseSum(parser);
        wesosa (kind(parser) <> ")") {
            cha malwe;
        }
        parser[1] <- parser[1] + 1;
    amdre "function"
        parser[1] <- parser[1] + 1;
        tree <- parseFunction(parser, token[1]);
    bawoum moumare
    wesosa ((tree <> malwe) dilisyo negative) {
        cha ["negative", tree];
    }
    cha tree;
bawoum tosedo

tosedo parseProduct(parser)
    sheye tree <- parsePrimary(parser);
    veshim (tree <> malwe) {
        sheye op <- kind(parser);
        wesosa ((op <> "*") dilisyo ((op <> "/") dilisyo (op <> "%"))) {
            bou;
        }
        parser[1] <- parser[1] + 1;
        sheye right <- parsePrimary(parser);
        wesosa (right = malwe) {
            cha malwe;
        }
        tree <- [op, tree, right];
    }
    cha tree;
bawoum tosedo

tosedo parseSum(parser)
    sheye tree <- parseProduct(parser);
    veshim (tree <> malwe) {
        sheye op <- kind(parser);
        wesosa ((op <> "+") dilisyo (op <> "-")) {
            bou;
        }
        parser[1] <- parser[1] + 1;
        sheye right <- parseProduct(parser);
        wesosa (right = malwe) {
            cha malwe;
        }
        tree <- [op, tree, right];
    }
    cha tree;
bawoum tosedo

tosedo combine(name, a, b)
    wesosa (a = malwe) {
        cha b;
    }
    moumare amdre name
    amdre "SUM"
        cha a + b;
    amdre "MIN"
        wesosa (b < a) {
            cha b;
        }
    amdre "MAX"
        wesosa (b > a) {
            cha b;
        }
    bawoum moumare
    cha a;
bawoum tosedo

tosedo aggregate(name, args, graph)
    sheye result <- malwe;
    sheye field <- 4;
    wesosa (name = "MIN") {
        field <- 5;
    } oli wesosa (name = "MAX") {
        field <- 6;
    }
    sho (sheye i <- 0; i < louwo(args); i <- i + 1) {
        sheye arg <- args[i];
        wesosa (arg[0] = "range") {
            sheye parts <- arg[1];
            sho (sheye j <- 0; j < louwo(parts); j <- j + 1) {
                sheye node <- graph[parts[j]];
                result <- combine(name, result, node[field]);
            }
        } oli {
            sheye value <- compute(arg, graph);
            wesosa (value = malwe) {
                cha malwe;
            }
            result <- combine(name, result, value);
        }
    }
    cha result;
bawoum tosedo

tosedo compute(tree, graph)
    sheye op <- tree[0];
    moumare amdre op
    amdre "number"
        cha tree[1];
    amdre "cell"
        sheye node <- graph[tree[1]];
        cha node[4];
    amdre "function"
        cha aggregate(tree[1], tree[2], graph);
    amdre "negative"
        sheye value <- compute(tree[1], graph);
        wesosa (value = malwe) {
            cha malwe;
        }
        cha -value;
    bawoum moumare
    sheye a <- compute(tree[1], graph);
    sheye b <- compute(tree[2], graph);
    wesosa ((a = malwe) emsoulve (b = malwe)) {
        cha malwe;
    }
    moumare amdre op
    amdre "+"
        cha a + b;
    amdre "-"
        cha a - b;
    amdre "*"
        cha a * b;
    amdre oli
        wesosa (b = 0) {
            cha malwe;
        }
        sheye q <- a / b;
        wesosa ((q < 0) dilisyo ((a drossou b) <> 0)) {
            q <- q + 1;
        }
        wesosa (op = "/") {
            cha q;
        }
        cha a - (b * q);
    bawoum moumare
bawoum tosedo

tosedo resolve(graph, start)
    sheye root <- graph[start];
    root[0] <- 1;
    sheye stack <- [[start, 0]];
    sheye size <- 1;
    veshim (size > 0) {
        sheye frame <- stack[size - 1];
        sheye id <- frame[0];
        sheye node <- graph[id];
        sheye deps <- node[1];
        sheye i <- frame[1];
        wesosa (i < louwo(deps)) {
            sheye childId <- deps[i];
            sheye child <- graph[childId];
            wesosa (child[0] = 0) {
                child[0] <- 1;
                sheye next <- [childId, 0];
                wesosa (size = louwo(stack)) {
                    omse(stack, next);
                } oli {
                    stack[size] <- next;
                }
                size <- size + 1;
            } oli {
                wesosa (child[0] = 1) {
                    node[3] <- 3;
                } oli wesosa (child[3] > node[3]) {
                    node[3] <- child[3];
                }
                frame[1] <- i + 1;
            }
        } oli {
            wesosa (node[3] = 0) {
                wesosa (id < 2574) {
                    sheye value <- compute(node[2], graph);
                    wesosa (value = malwe) {
                        node[3] <- 1;
                    } oli {
                        node[4] <- value;
                        node[5] <- value;
                        node[6] <- value;
                    }
                } oli {
                    sheye a <- graph[deps[0]];
                    sheye b <- graph[deps[1]];
                    node[4] <- a[4] + b[4];
                    node[5] <- combine("MIN", a[5], b[5]);
                    node[6] <- combine("MAX", a[6], b[6]);
                }
            }
            node[0] <- 2;
            size <- size - 1;
        }
    }
bawoum tosedo

sheye columns <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
sheye zero <- [2, [], malwe, 0, 0, 0, 0];
sheye graph <- [];
sho (sheye i <- 0; i < 2574; i <- i + 1) {
    omse(graph, zero);
}
sho (i <- 2574; i < 18958; i <- i + 1) {
    omse(graph, malwe);
}
sheye line <- diwela();
veshim (line <> malwe) {
    sheye name <- "";
    sheye i <- 0;
    veshim (line[i] <> " ") {
        name <- name + line[i];
        i <- i + 1;
    }
    sheye id <- cellId(name, columns);
    graph[id] <- [0, [], [line, i + 3], 0, 0, 0, 0];
    line <- diwela();
}

sho (sheye id <- 0; id < 2574; id <- id + 1) {
    sheye node <- graph[id];
    wesosa (node = zero) {
        chidrom;
    }
    sheye source <- node[2];
    sheye tokens <- tokenize(source[0], source[1], columns);
    node[1] <- dependencies(tokens, graph);
    sheye parser <- [tokens, 0];
    sheye tree <- parseSum(parser);
    node[2] <- tree;
    wesosa ((tree = malwe) emsoulve (kind(parser) <> "end")) {
        node[3] <- 2;
    }
}
sheye errors <- ["", "#DIV0", "#ERR", "#CYCLE"];
sho (sheye id <- 0; id < 2574; id <- id + 1) {
    sheye node <- graph[id];
    wesosa (node = zero) {
        chidrom;
    }
    wesosa (node[0] = 0) {
        resolve(graph, id);
    }
    tivou columns[id drossou 26];
    tivou (id / 26) + 1;
    tivou " = ";
    wesosa (node[3] = 0) {
        wami node[4];
    } oli {
        wami errors[node[3]];
    }
}
