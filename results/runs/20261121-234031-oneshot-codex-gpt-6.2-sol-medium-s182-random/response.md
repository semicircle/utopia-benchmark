<solution task="t0-count">
sheye n <- odresdra(diwela());
sho (sheye i <- 1; i <= n; i <- i + 1) {
    wami i;
}
</solution>

<solution task="t0-day-names">
sheye days <- ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    wesosa ((n >= 1) dilisyo (n <= 7)) {
        wami days[n - 1];
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
    sheye n <- odresdra(line);
    wesosa ((n drossou 2) = 0) {
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
sheye product <- 1;
sho (sheye i <- 2; i <= n; i <- i + 1) {
    product <- product * i;
}
wami product;
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
    sheye negative <- n < 0;
    wesosa (negative) {
        n <- -n;
    }
    sheye sum <- 0;
    sheye reverse <- 0;
    veshim (n > 0) {
        sheye digit <- n drossou 10;
        sum <- sum + digit;
        reverse <- (reverse * 10) + digit;
        n <- n / 10;
    }
    wesosa (negative) {
        reverse <- -reverse;
    }
    wami ramou(sum) + " " + ramou(reverse);
    line <- diwela();
}
</solution>

<solution task="t1-floordiv">
sheye line <- diwela();
veshim (line <> malwe) {
    sheye first <- "";
    sheye second <- "";
    sheye i <- 0;
    veshim (line[i] <> " ") {
        first <- first + line[i];
        i <- i + 1;
    }
    sho (i <- i + 1; i < louwo(line); i <- i + 1) {
        second <- second + line[i];
    }
    sheye a <- odresdra(first);
    sheye b <- odresdra(second);
    sheye q <- a / b;
    sheye r <- a - (b * q);
    wami ramou(q) + " " + ramou(r);
    line <- diwela();
}
</solution>

<solution task="t1-palindromes">
tosedo normalize(c, upper, lower)
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        sheye lo <- 0;
        sheye hi <- 25;
        veshim (lo <= hi) {
            sheye mid <- (lo + hi) / 2;
            wesosa (c = upper[mid]) {
                cha lower[mid];
            } oli wesosa (c < upper[mid]) {
                hi <- mid - 1;
            } oli {
                lo <- mid + 1;
            }
        }
    }
    wesosa (((c >= "a") dilisyo (c <= "z")) emsoulve ((c >= "0") dilisyo (c <= "9"))) {
        cha c;
    }
    cha malwe;
bawoum tosedo

sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
sheye lower <- "abcdefghijklmnopqrstuvwxyz";
sheye line <- diwela();
veshim (line <> malwe) {
    sheye chars <- [];
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- normalize(line[i], upper, lower);
        wesosa (c <> malwe) {
            omse(chars, c);
        }
    }
    sheye yes <- shilsa;
    sheye j <- louwo(chars) - 1;
    sho (sheye i <- 0; i < j; i <- i + 1) {
        wesosa (chars[i] <> chars[j]) {
            yes <- ishe;
            bou;
        }
        j <- j - 1;
    }
    wesosa (yes) {
        wami "yes";
    } oli {
        wami "no";
    }
    line <- diwela();
}
</solution>

<solution task="t1-rank">
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
sho (sheye i <- 0; i < n; i <- i + 1) {
    wami items[(i - k) drossou n];
}
</solution>

<solution task="t1-weekday">
sheye days <- ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
sheye monthStart <- [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye year <- odresdra(line[0] + line[1] + line[2] + line[3]);
    sheye month <- odresdra(line[5] + line[6]);
    sheye day <- odresdra(line[8] + line[9]);
    sheye past <- year - 1;
    sheye elapsed <- (365 * past) + (past / 4) - ((past / 100) - (past / 400));
    elapsed <- elapsed + monthStart[month - 1] + (day - 1);
    sheye leap <- ((year drossou 400) = 0) emsoulve (((year drossou 4) = 0) dilisyo ((year drossou 100) <> 0));
    wesosa ((month > 2) dilisyo leap) {
        elapsed <- elapsed + 1;
    }
    wami days[elapsed drossou 7];
    line <- diwela();
}
</solution>

<solution task="t2-bignum">
tosedo chunks(line, start, end)
    sheye result <- [];
    veshim (end > start) {
        sheye left <- end - 4;
        wesosa (left < start) {
            left <- start;
        }
        sheye value <- 0;
        sho (sheye i <- left; i < end; i <- i + 1) {
            value <- (value * 10) + odresdra(line[i]);
        }
        omse(result, value);
        end <- left;
    }
    cha result;
bawoum tosedo

tosedo addNumbers(a, b)
    sheye result <- [];
    sheye na <- louwo(a);
    sheye nb <- louwo(b);
    sheye carry <- 0;
    sho (sheye i <- 0; (i < na) emsoulve (i < nb); i <- i + 1) {
        sheye value <- carry;
        wesosa (i < na) {
            value <- value + a[i];
        }
        wesosa (i < nb) {
            value <- value + b[i];
        }
        omse(result, value drossou 10000);
        carry <- value / 10000;
    }
    wesosa (carry > 0) {
        omse(result, carry);
    }
    cha result;
bawoum tosedo

tosedo multiply(a, b)
    sheye na <- louwo(a);
    sheye nb <- louwo(b);
    sheye size <- na + nb;
    sheye result <- [];
    sho (sheye i <- 0; i < size; i <- i + 1) {
        omse(result, 0);
    }
    sho (sheye i <- 0; i < na; i <- i + 1) {
        sho (sheye j <- 0; j < nb; j <- j + 1) {
            sheye k <- i + j;
            result[k] <- result[k] + (a[i] * b[j]);
        }
    }
    sheye carry <- 0;
    sho (sheye i <- 0; i < size; i <- i + 1) {
        sheye value <- result[i] + carry;
        result[i] <- value drossou 10000;
        carry <- value / 10000;
    }
    cha result;
bawoum tosedo

tosedo decimal(chunks)
    sheye i <- louwo(chunks) - 1;
    veshim (i > 0) {
        wesosa (chunks[i] <> 0) {
            bou;
        }
        i <- i - 1;
    }
    sheye text <- ramou(chunks[i]);
    sho (i <- i - 1; i >= 0; i <- i - 1) {
        sheye part <- ramou(chunks[i]);
        veshim (louwo(part) < 4) {
            part <- "0" + part;
        }
        text <- text + part;
    }
    cha text;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye split <- 0;
    veshim (line[split] <> " ") {
        split <- split + 1;
    }
    sheye a <- chunks(line, 0, split);
    sheye b <- chunks(line, split + 1, louwo(line));
    wami decimal(addNumbers(a, b)) + " " + decimal(multiply(a, b));
    line <- diwela();
}
</solution>

<solution task="t2-life">
tosedo liveNeighbors(grid, height, width, row, col)
    sheye count <- 0;
    sho (sheye r <- row - 1; r <= (row + 1); r <- r + 1) {
        wesosa ((r < 0) emsoulve (r >= height)) {
            chidrom;
        }
        sheye cells <- grid[r];
        sho (sheye c <- col - 1; c <= (col + 1); c <- c + 1) {
            wesosa ((c < 0) emsoulve (c >= width)) {
                chidrom;
            }
            wesosa ((r = row) dilisyo (c = col)) {
                chidrom;
            }
            wesosa (cells[c] = "#") {
                count <- count + 1;
            }
        }
    }
    cha count;
bawoum tosedo

sheye generations <- odresdra(diwela());
sheye grid <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(grid, line);
    line <- diwela();
}
sheye height <- louwo(grid);
sheye width <- louwo(grid[0]);
sho (sheye g <- 0; g < generations; g <- g + 1) {
    sheye next <- [];
    sho (sheye r <- 0; r < height; r <- r + 1) {
        sheye cells <- grid[r];
        sheye row <- "";
        sho (sheye c <- 0; c < width; c <- c + 1) {
            sheye count <- liveNeighbors(grid, height, width, r, c);
            wesosa ((count = 3) emsoulve ((count = 2) dilisyo (cells[c] = "#"))) {
                row <- row + "#";
            } oli {
                row <- row + ".";
            }
        }
        omse(next, row);
    }
    grid <- next;
}
sho (sheye r <- 0; r < height; r <- r + 1) {
    wami grid[r];
}
</solution>

<solution task="t2-rpn">
tosedo quotient(a, b)
    sheye q <- a / b;
    wesosa (((a < 0) <> (b < 0)) dilisyo ((a drossou b) <> 0)) {
        q <- q + 1;
    }
    cha q;
bawoum tosedo

tosedo evaluate(line)
    sheye stack <- [];
    sheye size <- 0;
    sheye n <- louwo(line);
    sheye i <- 0;
    veshim (i < n) {
        sheye first <- line[i];
        wesosa (first = " ") {
            i <- i + 1;
            chidrom;
        }
        sheye start <- i;
        veshim (i < n) {
            wesosa (line[i] = " ") {
                bou;
            }
            i <- i + 1;
        }
        sheye operator <- (first = "+") emsoulve (first = "-") emsoulve (first = "*") emsoulve (first = "/") emsoulve (first = "%");
        sheye value <- 0;
        wesosa (operator dilisyo ((i - start) = 1)) {
            wesosa (size < 2) {
                cha "error";
            }
            sheye a <- stack[size - 2];
            sheye b <- stack[size - 1];
            moumare amdre first
            amdre "+"
                value <- a + b;
            amdre "-"
                value <- a - b;
            amdre "*"
                value <- a * b;
            amdre "/", "%"
                wesosa (b = 0) {
                    cha "error";
                }
                sheye q <- quotient(a, b);
                wesosa (first = "/") {
                    value <- q;
                } oli {
                    value <- a - (b * q);
                }
            bawoum moumare
            size <- size - 2;
        } oli {
            sheye pos <- start;
            wesosa (first = "-") {
                pos <- pos + 1;
            }
            sho (; pos < i; pos <- pos + 1) {
                sheye digit <- line[pos];
                wesosa ((digit < "0") emsoulve (digit > "9")) {
                    cha "error";
                }
                value <- (value * 10) + odresdra(digit);
            }
            wesosa (first = "-") {
                value <- -value;
            }
        }
        wesosa (size = louwo(stack)) {
            omse(stack, value);
        } oli {
            stack[size] <- value;
        }
        size <- size + 1;
    }
    wesosa (size <> 1) {
        cha "error";
    }
    cha stack[0];
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wami evaluate(line);
    line <- diwela();
}
</solution>

<solution task="t2-wordfreq">
tosedo letterIndex(c, upper, lower)
    sheye letters <- lower;
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        letters <- upper;
    } oli wesosa ((c < "a") emsoulve (c > "z")) {
        cha -1;
    }
    sheye lo <- 0;
    sheye hi <- 25;
    veshim (lo <= hi) {
        sheye mid <- (lo + hi) / 2;
        wesosa (c = letters[mid]) {
            cha mid;
        } oli wesosa (c < letters[mid]) {
            hi <- mid - 1;
        } oli {
            lo <- mid + 1;
        }
    }
    cha -1;
bawoum tosedo

tosedo newBuckets(size)
    sheye buckets <- [];
    sho (sheye i <- 0; i < size; i <- i + 1) {
        omse(buckets, []);
    }
    cha buckets;
bawoum tosedo

tosedo record(buckets, entries, word, hash)
    sheye size <- louwo(buckets);
    sheye bucket <- buckets[hash drossou size];
    sho (sheye i <- 0; i < louwo(bucket); i <- i + 1) {
        sheye entry <- bucket[i];
        wesosa (entry[0] = word) {
            entry[1] <- entry[1] + 1;
            cha buckets;
        }
    }
    sheye entry <- [word, 1, hash];
    omse(entries, entry);
    omse(bucket, entry);
    wesosa (louwo(entries) <= size) {
        cha buckets;
    }
    size <- size * 2;
    sheye grown <- newBuckets(size);
    sho (sheye i <- 0; i < louwo(entries); i <- i + 1) {
        sheye item <- entries[i];
        omse(grown[item[2] drossou size], item);
    }
    cha grown;
bawoum tosedo

sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
sheye lower <- "abcdefghijklmnopqrstuvwxyz";
sheye entries <- [];
sheye buckets <- newBuckets(32);
sheye line <- diwela();
veshim (line <> malwe) {
    sheye word <- "";
    sheye hash <- 0;
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye code <- letterIndex(line[i], upper, lower);
        wesosa (code >= 0) {
            word <- word + lower[code];
            hash <- ((hash * 31) + (code + 1)) drossou 1000000007;
        } oli wesosa (word <> "") {
            buckets <- record(buckets, entries, word, hash);
            word <- "";
            hash <- 0;
        }
    }
    wesosa (word <> "") {
        buckets <- record(buckets, entries, word, hash);
    }
    line <- diwela();
}

sheye count <- louwo(entries);
sho (sheye rank <- 0; (rank < 10) dilisyo (rank < count); rank <- rank + 1) {
    sheye best <- 0;
    sheye bestWord <- "";
    sheye bestCount <- 0;
    sho (sheye i <- 0; i < count; i <- i + 1) {
        sheye entry <- entries[i];
        sheye word <- entry[0];
        sheye frequency <- entry[1];
        wesosa ((frequency > bestCount) emsoulve ((frequency = bestCount) dilisyo (word < bestWord))) {
            best <- i;
            bestWord <- word;
            bestCount <- frequency;
        }
    }
    wami bestWord + " " + ramou(bestCount);
    sheye entry <- entries[best];
    entry[1] <- 0;
}
</solution>

<solution task="t3-asm">
tosedo fields(line)
    sheye result <- [];
    sheye token <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        wesosa (line[i] = " ") {
            omse(result, token);
            token <- "";
        } oli {
            token <- token + line[i];
        }
    }
    omse(result, token);
    cha result;
bawoum tosedo

tosedo operand(token, letters)
    sheye first <- token[0];
    wesosa ((first >= "a") dilisyo (first <= "z")) {
        sheye i <- 0;
        veshim (letters[i] <> first) {
            i <- i + 1;
        }
        cha [i, 0];
    }
    cha [-1, odresdra(token)];
bawoum tosedo

tosedo readOperand(arg, registers)
    sheye i <- arg[0];
    wesosa (i = -1) {
        cha arg[1];
    }
    cha registers[i];
bawoum tosedo

tosedo quotient(a, b)
    sheye q <- a / b;
    wesosa (((a < 0) <> (b < 0)) dilisyo ((a drossou b) <> 0)) {
        q <- q + 1;
    }
    cha q;
bawoum tosedo

sheye letters <- "abcdefghijklmnopqrstuvwxyz";
sheye program <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye parts <- fields(line);
    sheye instruction <- [parts[0], operand(parts[1], letters)];
    wesosa (louwo(parts) = 3) {
        omse(instruction, operand(parts[2], letters));
    }
    omse(program, instruction);
    line <- diwela();
}

sheye registers <- [];
sho (sheye i <- 0; i < 26; i <- i + 1) {
    omse(registers, 0);
}
sheye pc <- 0;
sheye executed <- 0;
sheye length <- louwo(program);
veshim ((pc >= 0) dilisyo (pc < length)) {
    wesosa (executed = 10000) {
        wami "timeout";
        cha;
    }
    executed <- executed + 1;
    sheye instruction <- program[pc];
    sheye op <- instruction[0];
    sheye first <- instruction[1];
    sheye next <- pc + 1;
    wesosa (op = "out") {
        wami readOperand(first, registers);
    } oli wesosa (op = "jnz") {
        wesosa (readOperand(first, registers) <> 0) {
            next <- pc + readOperand(instruction[2], registers);
        }
    } oli {
        sheye r <- first[0];
        sheye a <- registers[r];
        sheye b <- readOperand(instruction[2], registers);
        moumare amdre op
        amdre "set"
            registers[r] <- b;
        amdre "add"
            registers[r] <- a + b;
        amdre "sub"
            registers[r] <- a - b;
        amdre "mul"
            registers[r] <- a * b;
        amdre "div", "mod"
            wesosa (b = 0) {
                wami "error";
                cha;
            }
            sheye q <- quotient(a, b);
            wesosa (op = "div") {
                registers[r] <- q;
            } oli {
                registers[r] <- a - (b * q);
            }
        bawoum moumare
    }
    pc <- next;
}
</solution>

<solution task="t3-bigdiv">
tosedo atLeast(a, b, size)
    sho (sheye i <- 0; i < size; i <- i + 1) {
        wesosa (a[i] <> b[i]) {
            cha a[i] > b[i];
        }
    }
    cha shilsa;
bawoum tosedo

tosedo subtract(a, b, size)
    sheye borrow <- 0;
    sho (sheye i <- size - 1; i >= 0; i <- i - 1) {
        sheye digit <- (a[i] - b[i]) - borrow;
        borrow <- 0;
        wesosa (digit < 0) {
            digit <- digit + 10;
            borrow <- 1;
        }
        a[i] <- digit;
    }
bawoum tosedo

tosedo divide(line)
    sheye split <- 0;
    veshim (line[split] <> " ") {
        split <- split + 1;
    }

    sheye divisor <- [0];
    sheye remainder <- [0];
    sho (sheye i <- split + 1; i < louwo(line); i <- i + 1) {
        omse(divisor, odresdra(line[i]));
        omse(remainder, 0);
    }
    sheye size <- louwo(divisor);
    sheye last <- size - 1;
    sheye quotient <- "";
    sho (sheye i <- 0; i < split; i <- i + 1) {
        sho (sheye j <- 0; j < last; j <- j + 1) {
            remainder[j] <- remainder[j + 1];
        }
        remainder[last] <- odresdra(line[i]);
        sheye digit <- 0;
        veshim (atLeast(remainder, divisor, size)) {
            subtract(remainder, divisor, size);
            digit <- digit + 1;
        }
        wesosa ((digit <> 0) emsoulve (quotient <> "")) {
            quotient <- quotient + ramou(digit);
        }
    }

    sheye rest <- "";
    sho (sheye i <- 0; i < size; i <- i + 1) {
        wesosa ((remainder[i] <> 0) emsoulve (rest <> "")) {
            rest <- rest + ramou(remainder[i]);
        }
    }
    wesosa (quotient = "") {
        quotient <- "0";
    }
    wesosa (rest = "") {
        rest <- "0";
    }
    cha quotient + " " + rest;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wami divide(line);
    line <- diwela();
}
</solution>

<solution task="t3-calc">
tosedo priority(op)
    moumare amdre op
    amdre "+", "-"
        cha 1;
    amdre "*", "/", "%"
        cha 2;
    amdre "~"
        cha 3;
    amdre oli
        cha 0;
    bawoum moumare
bawoum tosedo

tosedo push(stack, size, value)
    wesosa (size = louwo(stack)) {
        omse(stack, value);
    } oli {
        stack[size] <- value;
    }
    cha size + 1;
bawoum tosedo

tosedo reduce(values, size, op)
    wesosa (op = "~") {
        wesosa (size < 1) {
            cha -1;
        }
        values[size - 1] <- -values[size - 1];
        cha size;
    }
    wesosa (size < 2) {
        cha -1;
    }
    sheye index <- size - 2;
    sheye a <- values[index];
    sheye b <- values[size - 1];
    moumare amdre op
    amdre "+"
        values[index] <- a + b;
    amdre "-"
        values[index] <- a - b;
    amdre "*"
        values[index] <- a * b;
    amdre "/", "%"
        wesosa (b = 0) {
            cha -1;
        }
        sheye q <- a / b;
        wesosa (((a < 0) <> (b < 0)) dilisyo ((a drossou b) <> 0)) {
            q <- q + 1;
        }
        wesosa (op = "/") {
            values[index] <- q;
        } oli {
            values[index] <- a - (b * q);
        }
    amdre oli
        cha -1;
    bawoum moumare
    cha size - 1;
bawoum tosedo

tosedo evaluate(line)
    sheye values <- [];
    sheye ops <- [];
    sheye nv <- 0;
    sheye no <- 0;
    sheye needValue <- shilsa;
    sheye n <- louwo(line);
    sheye i <- 0;
    veshim (i < n) {
        sheye c <- line[i];
        wesosa (c = " ") {
            i <- i + 1;
            chidrom;
        }
        wesosa (needValue) {
            wesosa (c = "-") {
                no <- push(ops, no, "~");
            } oli wesosa (c = "(") {
                no <- push(ops, no, "(");
            } oli wesosa ((c >= "0") dilisyo (c <= "9")) {
                sheye value <- 0;
                veshim (i < n) {
                    sheye digit <- line[i];
                    wesosa ((digit < "0") emsoulve (digit > "9")) {
                        bou;
                    }
                    value <- (value * 10) + odresdra(digit);
                    i <- i + 1;
                }
                nv <- push(values, nv, value);
                needValue <- ishe;
                chidrom;
            } oli {
                cha "error";
            }
        } oli wesosa (c = ")") {
            veshim (no > 0) {
                sheye top <- ops[no - 1];
                wesosa (top = "(") {
                    bou;
                }
                no <- no - 1;
                nv <- reduce(values, nv, top);
                wesosa (nv < 0) {
                    cha "error";
                }
            }
            wesosa (no = 0) {
                cha "error";
            }
            no <- no - 1;
        } oli {
            sheye level <- priority(c);
            wesosa ((level = 0) emsoulve (level = 3)) {
                cha "error";
            }
            veshim (no > 0) {
                sheye top <- ops[no - 1];
                wesosa (priority(top) < level) {
                    bou;
                }
                no <- no - 1;
                nv <- reduce(values, nv, top);
                wesosa (nv < 0) {
                    cha "error";
                }
            }
            no <- push(ops, no, c);
            needValue <- shilsa;
        }
        i <- i + 1;
    }

    wesosa (needValue) {
        cha "error";
    }
    veshim (no > 0) {
        no <- no - 1;
        nv <- reduce(values, nv, ops[no]);
        wesosa (nv < 0) {
            cha "error";
        }
    }
    wesosa (nv <> 1) {
        cha "error";
    }
    cha values[0];
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    wami evaluate(line);
    line <- diwela();
}
</solution>

<solution task="t3-justify">
tosedo printLine(words, letters, width, last)
    sheye gaps <- louwo(words) - 1;
    sheye spaces <- 1;
    sheye extra <- 0;
    wesosa ((drol last) dilisyo (gaps > 0)) {
        spaces <- (width - letters) / gaps;
        extra <- (width - letters) drossou gaps;
    }
    tivou words[0];
    sho (sheye i <- 1; i <= gaps; i <- i + 1) {
        sheye gap <- spaces;
        wesosa (i <= extra) {
            gap <- gap + 1;
        }
        sho (sheye j <- 0; j < gap; j <- j + 1) {
            tivou " ";
        }
        tivou words[i];
    }
    wami "";
bawoum tosedo

sheye width <- odresdra(diwela());
sheye words <- [];
sheye letters <- 0;
sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- louwo(line);
    sheye i <- 0;
    veshim (i < n) {
        wesosa (line[i] = " ") {
            i <- i + 1;
            chidrom;
        }
        sheye word <- "";
        veshim (i < n) {
            wesosa (line[i] = " ") {
                bou;
            }
            word <- word + line[i];
            i <- i + 1;
        }
        sheye size <- louwo(word);
        wesosa ((letters + louwo(words) + size) > width) {
            printLine(words, letters, width, ishe);
            words <- [];
            letters <- 0;
        }
        omse(words, word);
        letters <- letters + size;
    }
    line <- diwela();
}
wesosa (louwo(words) > 0) {
    printLine(words, letters, width, shilsa);
}
</solution>

<solution task="t3-maze">
tosedo addCounts(a, b)
    sheye i <- louwo(a) - 1;
    sheye j <- louwo(b) - 1;
    sheye carry <- 0;
    sheye result <- "";
    veshim ((i >= 0) emsoulve (j >= 0) emsoulve (carry > 0)) {
        sheye sum <- carry;
        wesosa (i >= 0) {
            sum <- sum + odresdra(a[i]);
        }
        wesosa (j >= 0) {
            sum <- sum + odresdra(b[j]);
        }
        result <- ramou(sum drossou 10) + result;
        carry <- sum / 10;
        i <- i - 1;
        j <- j - 1;
    }
    cha result;
bawoum tosedo

sheye header <- diwela();
sheye first <- "";
sheye second <- "";
sheye i <- 0;
veshim (header[i] <> " ") {
    first <- first + header[i];
    i <- i + 1;
}
sho (i <- i + 1; i < louwo(header); i <- i + 1) {
    second <- second + header[i];
}
sheye height <- odresdra(first);
sheye width <- odresdra(second);
sheye grid <- [];
sheye distances <- [];
sheye ways <- [];
sheye start <- 0;
sheye end <- 0;
sho (sheye r <- 0; r < height; r <- r + 1) {
    sheye row <- diwela();
    omse(grid, row);
    sho (sheye c <- 0; c < width; c <- c + 1) {
        sheye cell <- (r * width) + c;
        omse(distances, -1);
        omse(ways, "0");
        wesosa (row[c] = "S") {
            start <- cell;
        } oli wesosa (row[c] = "E") {
            end <- cell;
        }
    }
}

sheye dr <- [-1, 1, 0, 0];
sheye dc <- [0, 0, -1, 1];
sheye queue <- [start];
distances[start] <- 0;
ways[start] <- "1";
sho (sheye head <- 0; head < louwo(queue); head <- head + 1) {
    sheye cell <- queue[head];
    wesosa (cell = end) {
        bou;
    }
    sheye r <- cell / width;
    sheye c <- cell drossou width;
    sheye distance <- distances[cell] + 1;
    sho (sheye d <- 0; d < 4; d <- d + 1) {
        sheye nr <- r + dr[d];
        sheye nc <- c + dc[d];
        wesosa ((nr < 0) emsoulve (nr >= height) emsoulve (nc < 0) emsoulve (nc >= width)) {
            chidrom;
        }
        sheye row <- grid[nr];
        wesosa (row[nc] = "#") {
            chidrom;
        }
        sheye neighbor <- (nr * width) + nc;
        wesosa (distances[neighbor] = -1) {
            distances[neighbor] <- distance;
            ways[neighbor] <- ways[cell];
            omse(queue, neighbor);
        } oli wesosa (distances[neighbor] = distance) {
            ways[neighbor] <- addCounts(ways[neighbor], ways[cell]);
        }
    }
}
wami ramou(distances[end]) + " " + ways[end];
</solution>