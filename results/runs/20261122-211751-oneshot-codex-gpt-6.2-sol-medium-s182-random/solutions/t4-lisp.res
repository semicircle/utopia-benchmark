tosedo isInteger(text)
    sheye start <- 0;
    wesosa (text[0] = "-") {
        start <- 1;
    }
    wesosa (start = louwo(text)) {
        cha ishe;
    }
    sho (sheye i <- start; i < louwo(text); i <- i + 1) {
        sheye c <- text[i];
        wesosa ((c < "0") emsoulve (c > "9")) {
            cha ishe;
        }
    }
    cha shilsa;
bawoum tosedo

tosedo isName(form)
    wesosa (form[0] <> "atom") {
        cha ishe;
    }
    sheye text <- form[1];
    cha ((text <> "#t") dilisyo (text <> "#f")) dilisyo (drol isInteger(text));
bawoum tosedo

tosedo atomIs(form, text)
    cha (form[0] = "atom") dilisyo (form[1] = text);
bawoum tosedo

tosedo readForm(tokens, cursor)
    sheye i <- cursor[0];
    sheye token <- tokens[i];
    cursor[0] <- i + 1;
    wesosa (token <> "(") {
        cha ["atom", token];
    }
    sheye parts <- [];
    veshim (tokens[cursor[0]] <> ")") {
        omse(parts, readForm(tokens, cursor));
    }
    cursor[0] <- cursor[0] + 1;
    cha ["form", parts];
bawoum tosedo

tosedo find(env, name)
    veshim (env <> malwe) {
        sheye bindings <- env[1];
        sho (sheye i <- louwo(bindings) - 1; i >= 0; i <- i - 1) {
            sheye entry <- bindings[i];
            wesosa (entry[0] = name) {
                cha entry[1];
            }
        }
        env <- env[0];
    }
    cha malwe;
bawoum tosedo

tosedo bindGlobal(env, name, value)
    sheye bindings <- env[1];
    sho (sheye i <- 0; i < louwo(bindings); i <- i + 1) {
        sheye entry <- bindings[i];
        wesosa (entry[0] = name) {
            entry[1] <- value;
            cha;
        }
    }
    omse(bindings, [name, value]);
bawoum tosedo

tosedo falseValue(value)
    wesosa (value[0] = "bool") {
        cha drol value[1];
    }
    cha ishe;
bawoum tosedo

tosedo makeProcedure(params, first, forms, body, env)
    sheye names <- [];
    sho (sheye i <- first; i < louwo(params); i <- i + 1) {
        sheye param <- params[i];
        wesosa (drol isName(param)) {
            cha malwe;
        }
        omse(names, param[1]);
    }
    cha ["proc", names, forms, body, env];
bawoum tosedo

tosedo sequence(forms, first, env)
    sheye value <- malwe;
    sho (sheye i <- first; i < louwo(forms); i <- i + 1) {
        value <- evaluate(forms[i], env, ishe);
        wesosa (value = malwe) {
            cha malwe;
        }
    }
    cha value;
bawoum tosedo

tosedo builtin(name, args)
    sheye n <- louwo(args);
    moumare amdre name
    amdre "list"
        sheye result <- ["nil"];
        sho (sheye i <- n - 1; i >= 0; i <- i - 1) {
            result <- ["pair", args[i], result];
        }
        cha result;
    amdre "cons"
        wesosa (n = 2) {
            cha ["pair", args[0], args[1]];
        }
        cha malwe;
    amdre "car", "cdr", "not", "null?"
        wesosa (n <> 1) {
            cha malwe;
        }
        sheye value <- args[0];
        wesosa (name = "not") {
            cha ["bool", falseValue(value)];
        }
        wesosa (name = "null?") {
            cha ["bool", value[0] = "nil"];
        }
        wesosa (value[0] <> "pair") {
            cha malwe;
        }
        wesosa (name = "car") {
            cha value[1];
        }
        cha value[2];
    bawoum moumare

    sho (sheye i <- 0; i < n; i <- i + 1) {
        sheye value <- args[i];
        wesosa (value[0] <> "int") {
            cha malwe;
        }
    }
    wesosa ((name = "+") emsoulve (name = "*")) {
        sheye total <- 0;
        wesosa (name = "*") {
            total <- 1;
        }
        sho (sheye i <- 0; i < n; i <- i + 1) {
            sheye value <- args[i];
            wesosa (name = "+") {
                total <- total + value[1];
            } oli {
                total <- total * value[1];
            }
        }
        cha ["int", total];
    }
    wesosa ((name = "-") dilisyo (n = 1)) {
        sheye value <- args[0];
        cha ["int", -value[1]];
    }
    wesosa (n <> 2) {
        cha malwe;
    }
    sheye left <- args[0];
    sheye right <- args[1];
    sheye a <- left[1];
    sheye b <- right[1];
    moumare amdre name
    amdre "-"
        cha ["int", a - b];
    amdre "="
        cha ["bool", a = b];
    amdre "<"
        cha ["bool", a < b];
    amdre ">"
        cha ["bool", a > b];
    amdre "/", "remainder"
        wesosa (b = 0) {
            cha malwe;
        }
        sheye q <- a / b;
        wesosa ((q < 0) dilisyo ((a drossou b) <> 0)) {
            q <- q + 1;
        }
        wesosa (name = "/") {
            cha ["int", q];
        }
        cha ["int", a - (b * q)];
    bawoum moumare
    cha malwe;
bawoum tosedo

tosedo apply(proc, args)
    wesosa (proc[0] = "builtin") {
        cha builtin(proc[1], args);
    }
    wesosa (proc[0] <> "proc") {
        cha malwe;
    }
    sheye params <- proc[1];
    wesosa (louwo(params) <> louwo(args)) {
        cha malwe;
    }
    sheye bindings <- [];
    sho (sheye i <- 0; i < louwo(params); i <- i + 1) {
        omse(bindings, [params[i], args[i]]);
    }
    cha sequence(proc[2], proc[3], [proc[4], bindings]);
bawoum tosedo

tosedo evaluate(form, env, atTop)
    wesosa (form[0] = "atom") {
        sheye text <- form[1];
        wesosa (text = "#t") {
            cha ["bool", shilsa];
        } oli wesosa (text = "#f") {
            cha ["bool", ishe];
        } oli wesosa (isInteger(text)) {
            cha ["int", odresdra(text)];
        }
        cha find(env, text);
    }

    sheye forms <- form[1];
    sheye n <- louwo(forms);
    wesosa (n = 0) {
        cha malwe;
    }
    sheye head <- forms[0];
    wesosa (atomIs(head, "if")) {
        wesosa (n <> 4) {
            cha malwe;
        }
        sheye condition <- evaluate(forms[1], env, ishe);
        wesosa (condition = malwe) {
            cha malwe;
        }
        wesosa (falseValue(condition)) {
            cha evaluate(forms[3], env, ishe);
        }
        cha evaluate(forms[2], env, ishe);
    }
    wesosa (atomIs(head, "lambda")) {
        wesosa (n < 3) {
            cha malwe;
        }
        sheye params <- forms[1];
        wesosa (params[0] <> "form") {
            cha malwe;
        }
        cha makeProcedure(params[1], 0, forms, 2, env);
    }
    wesosa (atomIs(head, "let")) {
        wesosa (n < 3) {
            cha malwe;
        }
        sheye bindingForm <- forms[1];
        wesosa (bindingForm[0] <> "form") {
            cha malwe;
        }
        sheye specs <- bindingForm[1];
        sheye bindings <- [];
        sho (sheye i <- 0; i < louwo(specs); i <- i + 1) {
            sheye spec <- specs[i];
            wesosa (spec[0] <> "form") {
                cha malwe;
            }
            sheye parts <- spec[1];
            wesosa (louwo(parts) <> 2) {
                cha malwe;
            }
            sheye name <- parts[0];
            wesosa (drol isName(name)) {
                cha malwe;
            }
            sheye value <- evaluate(parts[1], env, ishe);
            wesosa (value = malwe) {
                cha malwe;
            }
            omse(bindings, [name[1], value]);
        }
        cha sequence(forms, 2, [env, bindings]);
    }
    wesosa (atomIs(head, "begin")) {
        cha sequence(forms, 1, env);
    }
    wesosa (atomIs(head, "define") emsoulve ((drol atTop) dilisyo atomIs(head, "quote"))) {
        cha malwe;
    }
    sheye proc <- evaluate(head, env, ishe);
    wesosa (proc = malwe) {
        cha malwe;
    }
    sheye args <- [];
    sho (sheye i <- 1; i < n; i <- i + 1) {
        sheye arg <- evaluate(forms[i], env, ishe);
        wesosa (arg = malwe) {
            cha malwe;
        }
        omse(args, arg);
    }
    cha apply(proc, args);
bawoum tosedo

tosedo define(forms, global)
    wesosa (louwo(forms) <> 3) {
        cha ishe;
    }
    sheye target <- forms[1];
    sheye name <- target;
    sheye value <- malwe;
    wesosa (target[0] = "form") {
        sheye signature <- target[1];
        wesosa (louwo(signature) = 0) {
            cha ishe;
        }
        name <- signature[0];
        wesosa (drol isName(name)) {
            cha ishe;
        }
        value <- makeProcedure(signature, 1, forms, 2, global);
    } oli {
        wesosa (drol isName(name)) {
            cha ishe;
        }
        value <- evaluate(forms[2], global, ishe);
    }
    wesosa (value = malwe) {
        cha ishe;
    }
    bindGlobal(global, name[1], value);
    cha shilsa;
bawoum tosedo

tosedo writeValue(value)
    moumare amdre value[0]
    amdre "int"
        tivou value[1];
    amdre "bool"
        wesosa (value[1]) {
            tivou "#t";
        } oli {
            tivou "#f";
        }
    amdre "proc", "builtin"
        tivou "#<procedure>";
    amdre "nil"
        tivou "()";
    amdre "pair"
        tivou "(";
        writeValue(value[1]);
        sheye tail <- value[2];
        veshim (tail[0] = "pair") {
            tivou " ";
            writeValue(tail[1]);
            tail <- tail[2];
        }
        wesosa (tail[0] <> "nil") {
            tivou " . ";
            writeValue(tail);
        }
        tivou ")";
    bawoum moumare
bawoum tosedo

tosedo runForm(form, global)
    wesosa (form[0] = "form") {
        sheye parts <- form[1];
        wesosa (louwo(parts) > 0) {
            wesosa (atomIs(parts[0], "define")) {
                wesosa (drol define(parts, global)) {
                    wami "error";
                }
                cha;
            }
        }
    }
    sheye value <- evaluate(form, global, shilsa);
    wesosa (value = malwe) {
        wami "error";
    } oli {
        writeValue(value);
        wami "";
    }
bawoum tosedo

sheye global <- [malwe, []];
sheye names <- ["+", "*", "-", "/", "remainder", "=", "<", ">", "not", "cons", "car", "cdr", "list", "null?"];
sho (sheye i <- 0; i < louwo(names); i <- i + 1) {
    bindGlobal(global, names[i], ["builtin", names[i]]);
}
sheye tokens <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye word <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- line[i];
        wesosa ((c = " ") emsoulve ((c = "(") emsoulve (c = ")"))) {
            wesosa (word <> "") {
                omse(tokens, word);
                word <- "";
            }
            wesosa (c <> " ") {
                omse(tokens, c);
            }
        } oli {
            word <- word + c;
        }
    }
    wesosa (word <> "") {
        omse(tokens, word);
    }
    line <- diwela();
}
sheye cursor <- [0];
veshim (cursor[0] < louwo(tokens)) {
    runForm(readForm(tokens, cursor), global);
}
