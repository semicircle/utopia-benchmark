<solution task="t0-count">
sheye n <- odresdra(diwela());
sho (sheye i <- 1; i <= n; i <- i + 1) {
    wami i;
}
</solution>

<solution task="t0-day-names">
sheye names <- ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    wesosa ((n >= 1) dilisyo (n <= 7)) {
        wami names[n - 1];
    } oli {
        wami "invalid";
    }
    line <- diwela();
}
</solution>

<solution task="t0-even-odd">
sheye even <- 0;
sheye odd <- 0;
sheye line <- diwela();
veshim (line <> malwe) {
    wesosa ((odresdra(line) drossou 2) = 0) {
        even <- even + 1;
    } oli {
        odd <- odd + 1;
    }
    line <- diwela();
}
wami "even " + even;
wami "odd " + odd;
</solution>

<solution task="t0-factorial">
sheye n <- odresdra(diwela());
sheye result <- 1;
sho (sheye i <- 2; i <= n; i <- i + 1) {
    result <- result * i;
}
wami result;
</solution>

<solution task="t0-fizzbuzz">
sheye n <- odresdra(diwela());
sho (sheye i <- 1; i <= n; i <- i + 1) {
    wesosa ((i drossou 15) = 0) {
        wami "FizzBuzz";
    } oli wesosa ((i drossou 3) = 0) {
        wami "Fizz";
    } oli wesosa ((i drossou 5) = 0) {
        wami "Buzz";
    } oli {
        wami i;
    }
}
</solution>

<solution task="t0-hello">
wami "Hello, Utopia!";
</solution>

<solution task="t0-reverse-lines">
sheye lines <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(lines, line);
    line <- diwela();
}
sho (sheye i <- louwo(lines) - 1; i >= 0; i <- i - 1) {
    wami lines[i];
}
</solution>

<solution task="t1-digits">
sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    sheye sign <- 1;
    wesosa (n < 0) {
        sign <- -1;
        n <- -n;
    }
    sheye sum <- 0;
    sheye reversed <- 0;
    veshim (n > 0) {
        sheye digit <- n drossou 10;
        sum <- sum + digit;
        reversed <- (reversed * 10) + digit;
        n <- n / 10;
    }
    wami (ramou(sum) + " ") + (sign * reversed);
    line <- diwela();
}
</solution>

<solution task="t1-floordiv">
sheye line <- diwela();
veshim (line <> malwe) {
    sheye left <- "";
    sheye right <- "";
    sheye i <- 0;
    veshim (line[i] <> " ") {
        left <- left + line[i];
        i <- i + 1;
    }
    sho (i <- i + 1; i < louwo(line); i <- i + 1) {
        right <- right + line[i];
    }
    sheye a <- odresdra(left);
    sheye b <- odresdra(right);
    sheye q <- a / b;
    sheye r <- a - (b * q);
    wami (ramou(q) + " ") + r;
    line <- diwela();
}
</solution>

<solution task="t1-palindromes">
tosedo normalize(c)
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        sheye lower <- "abcdefghijklmnopqrstuvwxyz";
        sheye i <- 0;
        veshim (upper[i] <> c) {
            i <- i + 1;
        }
        cha lower[i];
    }
    wesosa (((c >= "a") dilisyo (c <= "z")) emsoulve ((c >= "0") dilisyo (c <= "9"))) {
        cha c;
    }
    cha malwe;
bawoum tosedo

tosedo palindrome(line)
    sheye left <- 0;
    sheye right <- louwo(line) - 1;
    veshim (left < right) {
        sheye a <- normalize(line[left]);
        wesosa (a = malwe) {
            left <- left + 1;
            chidrom;
        }
        sheye b <- normalize(line[right]);
        wesosa (b = malwe) {
            right <- right - 1;
            chidrom;
        }
        wesosa (a <> b) {
            cha ishe;
        }
        left <- left + 1;
        right <- right - 1;
    }
    cha shilsa;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wesosa (palindrome(line)) {
        wami "yes";
    } oli {
        wami "no";
    }
    line <- diwela();
}
</solution>

<solution task="t1-rank">
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
</solution>

<solution task="t1-rotate">
sheye k <- odresdra(diwela());
sheye items <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(items, line);
    line <- diwela();
}
sheye n <- louwo(items);
wesosa (n > 0) {
    sho (sheye i <- 0; i < n; i <- i + 1) {
        wami items[(i - k) drossou n];
    }
}
</solution>

<solution task="t1-weekday">
sheye names <- ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
sheye offsets <- [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye year <- odresdra((line[0] + line[1]) + (line[2] + line[3]));
    sheye month <- odresdra(line[5] + line[6]);
    sheye day <- odresdra(line[8] + line[9]);
    sheye y <- year - 1;
    sheye days <- (365 * y) + (y / 4);
    days <- (days - (y / 100)) + (y / 400);
    days <- days + (offsets[month - 1] + (day - 1));
    wesosa (month > 2) {
        wesosa (((year drossou 4) = 0) dilisyo (((year drossou 100) <> 0) emsoulve ((year drossou 400) = 0))) {
            days <- days + 1;
        }
    }
    wami names[days drossou 7];
    line <- diwela();
}
</solution>

<solution task="t2-bignum">
tosedo chunks(line, first, past)
    sheye values <- [];
    sheye i <- past;
    veshim (i > first) {
        sheye value <- 0;
        sheye place <- 1;
        sho (sheye j <- 0; (j < 4) dilisyo (i > first); j <- j + 1) {
            i <- i - 1;
            value <- value + (place * odresdra(line[i]));
            place <- place * 10;
        }
        omse(values, value);
    }
    cha values;
bawoum tosedo

tosedo add(a, b)
    sheye values <- [];
    sheye carry <- 0;
    sho (sheye i <- 0; (i < louwo(a)) emsoulve (i < louwo(b)); i <- i + 1) {
        sheye value <- carry;
        wesosa (i < louwo(a)) {
            value <- value + a[i];
        }
        wesosa (i < louwo(b)) {
            value <- value + b[i];
        }
        omse(values, value drossou 10000);
        carry <- value / 10000;
    }
    wesosa (carry > 0) {
        omse(values, carry);
    }
    cha values;
bawoum tosedo

tosedo multiply(a, b)
    sheye values <- [];
    sho (sheye i <- 0; i < (louwo(a) + louwo(b)); i <- i + 1) {
        omse(values, 0);
    }
    sho (i <- 0; i < louwo(a); i <- i + 1) {
        sheye carry <- 0;
        sho (sheye j <- 0; j < louwo(b); j <- j + 1) {
            sheye k <- i + j;
            sheye value <- values[k] + ((a[i] * b[j]) + carry);
            values[k] <- value drossou 10000;
            carry <- value / 10000;
        }
        values[i + louwo(b)] <- carry;
    }
    cha values;
bawoum tosedo

tosedo writeNumber(values)
    sheye i <- louwo(values) - 1;
    veshim (i > 0) {
        wesosa (values[i] <> 0) {
            bou;
        }
        i <- i - 1;
    }
    tivou values[i];
    sho (i <- i - 1; i >= 0; i <- i - 1) {
        sheye text <- ramou(values[i]);
        sho (sheye j <- louwo(text); j < 4; j <- j + 1) {
            tivou "0";
        }
        tivou text;
    }
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye sep <- 0;
    veshim (line[sep] <> " ") {
        sep <- sep + 1;
    }
    sheye a <- chunks(line, 0, sep);
    sheye b <- chunks(line, sep + 1, louwo(line));
    writeNumber(add(a, b));
    tivou " ";
    writeNumber(multiply(a, b));
    wami "";
    line <- diwela();
}
</solution>

<solution task="t2-life">
sheye generations <- odresdra(diwela());
sheye line <- diwela();
sheye width <- louwo(line);
sheye border <- "";
sho (sheye i <- 0; i < (width + 2); i <- i + 1) {
    border <- border + ".";
}
sheye grid <- [border];
veshim (line <> malwe) {
    omse(grid, "." + (line + "."));
    line <- diwela();
}
omse(grid, border);
sheye height <- louwo(grid) - 2;

sho (sheye g <- 0; g < generations; g <- g + 1) {
    sheye next <- [border];
    sho (sheye r <- 1; r <= height; r <- r + 1) {
        sheye row <- ".";
        sheye center <- grid[r];
        sho (sheye c <- 1; c <= width; c <- c + 1) {
            sheye count <- 0;
            sho (sheye dr <- -1; dr <= 1; dr <- dr + 1) {
                sheye neighbor <- grid[r + dr];
                sho (sheye dc <- -1; dc <= 1; dc <- dc + 1) {
                    wesosa ((dr <> 0) emsoulve (dc <> 0)) {
                        wesosa (neighbor[c + dc] = "#") {
                            count <- count + 1;
                        }
                    }
                }
            }
            wesosa ((count = 3) emsoulve ((count = 2) dilisyo (center[c] = "#"))) {
                row <- row + "#";
            } oli {
                row <- row + ".";
            }
        }
        omse(next, row + ".");
    }
    omse(next, border);
    grid <- next;
}

sho (sheye r <- 1; r <= height; r <- r + 1) {
    sheye row <- grid[r];
    sho (sheye c <- 1; c <= width; c <- c + 1) {
        tivou row[c];
    }
    wami "";
}
</solution>

<solution task="t2-rpn">
tosedo integerToken(token)
    sheye n <- louwo(token);
    sheye start <- 0;
    wesosa (token[0] = "-") {
        start <- 1;
    }
    wesosa (start = n) {
        cha malwe;
    }
    sho (sheye i <- start; i < n; i <- i + 1) {
        sheye c <- token[i];
        wesosa ((c < "0") emsoulve (c > "9")) {
            cha malwe;
        }
    }
    cha odresdra(token);
bawoum tosedo

tosedo evaluate(line)
    sheye stack <- [];
    sheye size <- 0;
    sheye i <- 0;
    sheye n <- louwo(line);
    veshim (i < n) {
        wesosa (line[i] = " ") {
            i <- i + 1;
            chidrom;
        }
        sheye token <- "";
        veshim (i < n) {
            wesosa (line[i] = " ") {
                bou;
            }
            token <- token + line[i];
            i <- i + 1;
        }
        sheye value <- malwe;
        moumare amdre token
        amdre "+", "-", "*", "/", "%"
            wesosa (size < 2) {
                cha malwe;
            }
            sheye a <- stack[size - 2];
            sheye b <- stack[size - 1];
            size <- size - 2;
            moumare amdre token
            amdre "+"
                value <- a + b;
            amdre "-"
                value <- a - b;
            amdre "*"
                value <- a * b;
            amdre oli
                wesosa (b = 0) {
                    cha malwe;
                }
                sheye q <- a / b;
                wesosa ((q < 0) dilisyo ((a drossou b) <> 0)) {
                    q <- q + 1;
                }
                wesosa (token = "/") {
                    value <- q;
                } oli {
                    value <- a - (b * q);
                }
            bawoum moumare
        amdre oli
            value <- integerToken(token);
            wesosa (value = malwe) {
                cha malwe;
            }
        bawoum moumare
        wesosa (size = louwo(stack)) {
            omse(stack, value);
        } oli {
            stack[size] <- value;
        }
        size <- size + 1;
    }
    wesosa (size = 1) {
        cha stack[0];
    }
    cha malwe;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye value <- evaluate(line);
    wesosa (value = malwe) {
        wami "error";
    } oli {
        wami value;
    }
    line <- diwela();
}
</solution>

<solution task="t2-wordfreq">
tosedo lowerLetter(c, upper, lower)
    wesosa ((c >= "a") dilisyo (c <= "z")) {
        cha c;
    }
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        sheye lo <- 0;
        sheye hi <- 25;
        veshim (lo < hi) {
            sheye mid <- (lo + hi) / 2;
            wesosa (upper[mid] < c) {
                lo <- mid + 1;
            } oli {
                hi <- mid;
            }
        }
        cha lower[lo];
    }
    cha malwe;
bawoum tosedo

tosedo descend(node, c)
    sheye child <- node[0];
    veshim (child <> malwe) {
        wesosa (child[2] = c) {
            cha child;
        }
        child <- child[1];
    }
    child <- [malwe, node[0], c, 0, ""];
    node[0] <- child;
    cha child;
bawoum tosedo

tosedo record(node, word, terminals)
    wesosa (node[3] = 0) {
        node[4] <- word;
        omse(terminals, node);
    }
    node[3] <- node[3] + 1;
bawoum tosedo

sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
sheye lower <- "abcdefghijklmnopqrstuvwxyz";
sheye root <- [malwe, malwe, "", 0, ""];
sheye terminals <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye node <- root;
    sheye word <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- lowerLetter(line[i], upper, lower);
        wesosa (c <> malwe) {
            node <- descend(node, c);
            word <- word + c;
        } oli wesosa (node <> root) {
            record(node, word, terminals);
            node <- root;
            word <- "";
        }
    }
    wesosa (node <> root) {
        record(node, word, terminals);
    }
    line <- diwela();
}

sho (sheye rank <- 0; rank < 10; rank <- rank + 1) {
    sheye best <- malwe;
    sho (sheye i <- 0; i < louwo(terminals); i <- i + 1) {
        sheye candidate <- terminals[i];
        wesosa (candidate[3] = 0) {
            chidrom;
        }
        wesosa (best = malwe) {
            best <- candidate;
        } oli wesosa ((candidate[3] > best[3]) emsoulve ((candidate[3] = best[3]) dilisyo (candidate[4] < best[4]))) {
            best <- candidate;
        }
    }
    wesosa (best = malwe) {
        bou;
    }
    wami (best[4] + " ") + best[3];
    best[3] <- 0;
}
</solution>

<solution task="t3-asm">
tosedo split(line)
    sheye words <- [];
    sheye token <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        wesosa (line[i] = " ") {
            omse(words, token);
            token <- "";
        } oli {
            token <- token + line[i];
        }
    }
    omse(words, token);
    cha words;
bawoum tosedo

tosedo operand(token)
    wesosa ((louwo(token) = 1) dilisyo ((token >= "a") dilisyo (token <= "z"))) {
        sheye alphabet <- "abcdefghijklmnopqrstuvwxyz";
        sheye index <- 0;
        veshim (alphabet[index] <> token) {
            index <- index + 1;
        }
        cha [shilsa, index];
    }
    cha [ishe, odresdra(token)];
bawoum tosedo

tosedo value(arg, registers)
    wesosa (arg[0]) {
        cha registers[arg[1]];
    }
    cha arg[1];
bawoum tosedo

sheye program <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye words <- split(line);
    sheye second <- malwe;
    wesosa (louwo(words) = 3) {
        second <- operand(words[2]);
    }
    omse(program, [words[0], operand(words[1]), second]);
    line <- diwela();
}

sheye registers <- [];
sho (sheye i <- 0; i < 26; i <- i + 1) {
    omse(registers, 0);
}
sheye pc <- 0;
sheye executed <- 0;
veshim ((pc >= 0) dilisyo (pc < louwo(program))) {
    wesosa (executed = 10000) {
        wami "timeout";
        cha;
    }
    executed <- executed + 1;
    sheye instruction <- program[pc];
    sheye op <- instruction[0];
    sheye first <- instruction[1];
    moumare amdre op
    amdre "out"
        wami value(first, registers);
    amdre "jnz"
        wesosa (value(first, registers) <> 0) {
            pc <- pc + value(instruction[2], registers);
            chidrom;
        }
    amdre oli
        sheye index <- first[1];
        sheye a <- registers[index];
        sheye b <- value(instruction[2], registers);
        moumare amdre op
        amdre "set"
            registers[index] <- b;
        amdre "add"
            registers[index] <- a + b;
        amdre "sub"
            registers[index] <- a - b;
        amdre "mul"
            registers[index] <- a * b;
        amdre "div", "mod"
            wesosa (b = 0) {
                wami "error";
                cha;
            }
            sheye q <- a / b;
            wesosa ((q < 0) dilisyo ((a drossou b) <> 0)) {
                q <- q + 1;
            }
            wesosa (op = "div") {
                registers[index] <- q;
            } oli {
                registers[index] <- a - (b * q);
            }
        bawoum moumare
    bawoum moumare
    pc <- pc + 1;
}
</solution>

<solution task="t3-bigdiv">
tosedo compare(a, b)
    sho (sheye i <- 0; i < louwo(a); i <- i + 1) {
        wesosa (a[i] < b[i]) {
            cha -1;
        }
        wesosa (a[i] > b[i]) {
            cha 1;
        }
    }
    cha 0;
bawoum tosedo

tosedo subtract(a, b)
    sheye borrow <- 0;
    sho (sheye i <- louwo(a) - 1; i >= 0; i <- i - 1) {
        sheye digit <- a[i] - (b[i] + borrow);
        borrow <- 0;
        wesosa (digit < 0) {
            digit <- digit + 10;
            borrow <- 1;
        }
        a[i] <- digit;
    }
bawoum tosedo

tosedo divide(line)
    sheye sep <- 0;
    veshim (line[sep] <> " ") {
        sep <- sep + 1;
    }
    sheye divisor <- [0];
    sheye remainder <- [0];
    sho (sheye i <- sep + 1; i < louwo(line); i <- i + 1) {
        omse(divisor, odresdra(line[i]));
        omse(remainder, 0);
    }
    sheye n <- louwo(divisor);
    sheye multiples <- [];
    sho (sheye d <- 0; d <= 9; d <- d + 1) {
        sheye digits <- [];
        sho (sheye i <- 0; i < n; i <- i + 1) {
            omse(digits, 0);
        }
        sheye carry <- 0;
        sho (i <- n - 1; i >= 0; i <- i - 1) {
            sheye value <- (d * divisor[i]) + carry;
            digits[i] <- value drossou 10;
            carry <- value / 10;
        }
        omse(multiples, digits);
    }

    sheye started <- ishe;
    sho (sheye i <- 0; i < sep; i <- i + 1) {
        sho (sheye j <- 0; j < (n - 1); j <- j + 1) {
            remainder[j] <- remainder[j + 1];
        }
        remainder[n - 1] <- odresdra(line[i]);
        sheye lo <- 0;
        sheye hi <- 9;
        veshim (lo < hi) {
            sheye mid <- (lo + (hi + 1)) / 2;
            wesosa (compare(remainder, multiples[mid]) >= 0) {
                lo <- mid;
            } oli {
                hi <- mid - 1;
            }
        }
        wesosa (lo > 0) {
            subtract(remainder, multiples[lo]);
            started <- shilsa;
        }
        wesosa (started) {
            tivou lo;
        }
    }
    wesosa (drol started) {
        tivou "0";
    }
    tivou " ";
    sheye i <- 0;
    veshim (i < (n - 1)) {
        wesosa (remainder[i] <> 0) {
            bou;
        }
        i <- i + 1;
    }
    sho (; i < n; i <- i + 1) {
        tivou remainder[i];
    }
    wami "";
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    divide(line);
    line <- diwela();
}
</solution>

<solution task="t3-calc">
tosedo digit(c)
    cha (c >= "0") dilisyo (c <= "9");
bawoum tosedo

tosedo precedence(op)
    moumare amdre op
    amdre "+", "-"
        cha 1;
    amdre "*", "/", "%"
        cha 2;
    amdre "u"
        cha 3;
    amdre oli
        cha 0;
    bawoum moumare
bawoum tosedo

tosedo put(stack, index, value)
    wesosa (index = louwo(stack)) {
        omse(stack, value);
    } oli {
        stack[index] <- value;
    }
bawoum tosedo

tosedo reduce(op, values, count)
    wesosa (op = "u") {
        wesosa (count < 1) {
            cha -1;
        }
        values[count - 1] <- -values[count - 1];
        cha count;
    }
    wesosa (count < 2) {
        cha -1;
    }
    sheye a <- values[count - 2];
    sheye b <- values[count - 1];
    sheye result <- 0;
    moumare amdre op
    amdre "+"
        result <- a + b;
    amdre "-"
        result <- a - b;
    amdre "*"
        result <- a * b;
    amdre "/", "%"
        wesosa (b = 0) {
            cha -1;
        }
        sheye q <- a / b;
        wesosa ((q < 0) dilisyo ((a drossou b) <> 0)) {
            q <- q + 1;
        }
        wesosa (op = "/") {
            result <- q;
        } oli {
            result <- a - (b * q);
        }
    bawoum moumare
    values[count - 2] <- result;
    cha count - 1;
bawoum tosedo

tosedo calculate(line)
    sheye ops <- [];
    sheye values <- [];
    sheye opCount <- 0;
    sheye valueCount <- 0;
    sheye needValue <- shilsa;
    sheye i <- 0;
    sheye n <- louwo(line);
    veshim (i < n) {
        sheye c <- line[i];
        i <- i + 1;
        wesosa (c = " ") {
            chidrom;
        }
        wesosa (needValue) {
            wesosa ((c = "-") emsoulve (c = "(")) {
                wesosa (c = "-") {
                    c <- "u";
                }
                put(ops, opCount, c);
                opCount <- opCount + 1;
            } oli wesosa (digit(c)) {
                sheye literal <- c;
                veshim (i < n) {
                    wesosa (drol digit(line[i])) {
                        bou;
                    }
                    literal <- literal + line[i];
                    i <- i + 1;
                }
                put(values, valueCount, odresdra(literal));
                valueCount <- valueCount + 1;
                needValue <- ishe;
            } oli {
                cha malwe;
            }
        } oli {
            sheye level <- precedence(c);
            wesosa (c = ")") {
                level <- 1;
            } oli wesosa ((level = 0) emsoulve (c = "u")) {
                cha malwe;
            }
            veshim (opCount > 0) {
                sheye op <- ops[opCount - 1];
                wesosa (precedence(op) < level) {
                    bou;
                }
                opCount <- opCount - 1;
                valueCount <- reduce(op, values, valueCount);
                wesosa (valueCount < 0) {
                    cha malwe;
                }
            }
            wesosa (c = ")") {
                wesosa (opCount = 0) {
                    cha malwe;
                }
                opCount <- opCount - 1;
            } oli {
                put(ops, opCount, c);
                opCount <- opCount + 1;
                needValue <- shilsa;
            }
        }
    }
    wesosa (needValue) {
        cha malwe;
    }
    veshim (opCount > 0) {
        opCount <- opCount - 1;
        sheye op <- ops[opCount];
        wesosa (op = "(") {
            cha malwe;
        }
        valueCount <- reduce(op, values, valueCount);
        wesosa (valueCount < 0) {
            cha malwe;
        }
    }
    wesosa (valueCount = 1) {
        cha values[0];
    }
    cha malwe;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye value <- calculate(line);
    wesosa (value = malwe) {
        wami "error";
    } oli {
        wami value;
    }
    line <- diwela();
}
</solution>

<solution task="t3-justify">
tosedo writeLine(words, letters, width, last)
    sheye gaps <- louwo(words) - 1;
    tivou words[0];
    wesosa (gaps > 0) {
        sheye spaces <- 1;
        sheye extra <- 0;
        wesosa (drol last) {
            spaces <- (width - letters) / gaps;
            extra <- (width - letters) drossou gaps;
        }
        sho (sheye i <- 0; i < gaps; i <- i + 1) {
            sheye count <- spaces;
            wesosa (i < extra) {
                count <- count + 1;
            }
            sho (sheye j <- 0; j < count; j <- j + 1) {
                tivou " ";
            }
            tivou words[i + 1];
        }
    }
    wami "";
bawoum tosedo

sheye width <- odresdra(diwela());
sheye words <- [];
sheye letters <- 0;
sheye line <- diwela();
veshim (line <> malwe) {
    sheye i <- 0;
    veshim (i < louwo(line)) {
        wesosa (line[i] = " ") {
            i <- i + 1;
            chidrom;
        }
        sheye word <- "";
        veshim (i < louwo(line)) {
            wesosa (line[i] = " ") {
                bou;
            }
            word <- word + line[i];
            i <- i + 1;
        }
        wesosa ((letters + (louwo(words) + louwo(word))) > width) {
            writeLine(words, letters, width, ishe);
            words <- [];
            letters <- 0;
        }
        omse(words, word);
        letters <- letters + louwo(word);
    }
    line <- diwela();
}
wesosa (louwo(words) > 0) {
    writeLine(words, letters, width, shilsa);
}
</solution>

<solution task="t3-maze">
tosedo addWays(a, b)
    sheye result <- [];
    sheye carry <- 0;
    sho (sheye i <- 0; (i < louwo(a)) emsoulve (i < louwo(b)); i <- i + 1) {
        sheye value <- carry;
        wesosa (i < louwo(a)) {
            value <- value + a[i];
        }
        wesosa (i < louwo(b)) {
            value <- value + b[i];
        }
        omse(result, value drossou 1000000000);
        carry <- value / 1000000000;
    }
    wesosa (carry > 0) {
        omse(result, carry);
    }
    cha result;
bawoum tosedo

tosedo writeWays(values)
    sheye i <- louwo(values) - 1;
    tivou values[i];
    sho (i <- i - 1; i >= 0; i <- i - 1) {
        sheye text <- ramou(values[i]);
        sho (sheye j <- louwo(text); j < 9; j <- j + 1) {
            tivou "0";
        }
        tivou text;
    }
    wami "";
bawoum tosedo

sheye header <- diwela();
sheye left <- "";
sheye right <- "";
sheye i <- 0;
veshim (header[i] <> " ") {
    left <- left + header[i];
    i <- i + 1;
}
sho (i <- i + 1; i < louwo(header); i <- i + 1) {
    right <- right + header[i];
}
sheye height <- odresdra(left);
sheye width <- odresdra(right);
sheye stride <- width + 2;
sheye grid <- [];
sheye start <- 0;
sheye goal <- 0;
sho (i <- 0; i < stride; i <- i + 1) {
    omse(grid, "#");
}
sho (sheye r <- 0; r < height; r <- r + 1) {
    sheye row <- diwela();
    omse(grid, "#");
    sho (sheye c <- 0; c < width; c <- c + 1) {
        sheye cell <- row[c];
        wesosa (cell = "S") {
            start <- louwo(grid);
        } oli wesosa (cell = "E") {
            goal <- louwo(grid);
        }
        omse(grid, cell);
    }
    omse(grid, "#");
}
sho (i <- 0; i < stride; i <- i + 1) {
    omse(grid, "#");
}

sheye distance <- [];
sheye ways <- [];
sho (i <- 0; i < louwo(grid); i <- i + 1) {
    omse(distance, -1);
    omse(ways, malwe);
}
distance[start] <- 0;
ways[start] <- [1];
sheye queue <- [start];
sheye offsets <- [-stride, stride, -1, 1];
sho (sheye head <- 0; head < louwo(queue); head <- head + 1) {
    sheye cell <- queue[head];
    wesosa (cell = goal) {
        tivou distance[cell];
        tivou " ";
        writeWays(ways[cell]);
        cha;
    }
    sheye nextDistance <- distance[cell] + 1;
    sho (sheye d <- 0; d < 4; d <- d + 1) {
        sheye next <- cell + offsets[d];
        wesosa (grid[next] = "#") {
            chidrom;
        }
        wesosa (distance[next] = -1) {
            distance[next] <- nextDistance;
            ways[next] <- ways[cell];
            omse(queue, next);
        } oli wesosa (distance[next] = nextDistance) {
            ways[next] <- addWays(ways[next], ways[cell]);
        }
    }
}
wami "-1 0";
</solution>

<solution task="t4-lisp">
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
</solution>

<solution task="t4-regex">
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
</solution>

<solution task="t4-sheet">
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
</solution>