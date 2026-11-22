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
    sheye negative <- n < 0;
    wesosa (negative) {
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
    wesosa (negative) {
        reversed <- -reversed;
    }
    tivou sum;
    wami " " + reversed;
    line <- diwela();
}
</solution>
<solution task="t1-floordiv">
sheye line <- diwela();
veshim (line <> malwe) {
    sheye i <- 0;
    sheye first <- "";
    veshim (line[i] <> " ") {
        first <- first + line[i];
        i <- i + 1;
    }
    sheye second <- "";
    sho (i <- i + 1; i < louwo(line); i <- i + 1) {
        second <- second + line[i];
    }
    sheye a <- odresdra(first);
    sheye b <- odresdra(second);
    sheye q <- a / b;
    sheye r <- a - (b * q);
    tivou q;
    wami " " + r;
    line <- diwela();
}
</solution>
<solution task="t1-palindromes">
tosedo normalized(ch)
    wesosa ((ch >= "A") dilisyo (ch <= "Z")) {
        sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        sheye lower <- "abcdefghijklmnopqrstuvwxyz";
        sheye lo <- 0;
        sheye hi <- 26;
        veshim (lo < hi) {
            sheye mid <- (lo + hi) / 2;
            wesosa (upper[mid] < ch) {
                lo <- mid + 1;
            } oli {
                hi <- mid;
            }
        }
        cha lower[lo];
    }
    wesosa (((ch >= "a") dilisyo (ch <= "z")) emsoulve ((ch >= "0") dilisyo (ch <= "9"))) {
        cha ch;
    }
    cha malwe;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye chars <- [];
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye ch <- normalized(line[i]);
        wesosa (ch <> malwe) {
            omse(chars, ch);
        }
    }
    sheye result <- "yes";
    sheye last <- louwo(chars) - 1;
    sho (sheye i <- 0; i < (last - i); i <- i + 1) {
        wesosa (chars[i] <> chars[last - i]) {
            result <- "no";
            bou;
        }
    }
    wami result;
    line <- diwela();
}
</solution>
<solution task="t1-rank">
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
</solution>
<solution task="t1-rotate">
sheye k <- odresdra(diwela());
sheye items <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(items, line);
    line <- diwela();
}
sheye count <- louwo(items);
wesosa (count > 0) {
    sheye shift <- k drossou count;
    sho (sheye i <- 0; i < count; i <- i + 1) {
        wami items[(i - shift) drossou count];
    }
}
</solution>
<solution task="t1-weekday">
tosedo readNumber(line, start, stop)
    sheye value <- 0;
    sho (sheye i <- start; i < stop; i <- i + 1) {
        value <- (value * 10) + odresdra(line[i]);
    }
    cha value;
bawoum tosedo

sheye days <- ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
sheye offsets <- [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye year <- readNumber(line, 0, 4);
    sheye month <- readNumber(line, 5, 7);
    sheye day <- readNumber(line, 8, 10);
    sheye past <- year - 1;
    sheye elapsed <- (365 * past) + (past / 4);
    elapsed <- elapsed - (past / 100);
    elapsed <- elapsed + (past / 400);
    elapsed <- elapsed + offsets[month - 1];
    elapsed <- elapsed + (day - 1);
    wesosa ((month > 2) dilisyo ((year drossou 4) = 0)) {
        wesosa (((year drossou 100) <> 0) emsoulve ((year drossou 400) = 0)) {
            elapsed <- elapsed + 1;
        }
    }
    wami days[elapsed drossou 7];
    line <- diwela();
}
</solution>
<solution task="t2-bignum">
tosedo readDigits(line, start, stop)
    sheye digits <- [];
    sho (sheye i <- stop - 1; i >= start; i <- i - 1) {
        omse(digits, odresdra(line[i]));
    }
    cha digits;
bawoum tosedo

tosedo addDigits(a, b)
    sheye result <- [];
    sheye na <- louwo(a);
    sheye nb <- louwo(b);
    sheye carry <- 0;
    sho (sheye i <- 0; (i < na) emsoulve (i < nb); i <- i + 1) {
        sheye total <- carry;
        wesosa (i < na) {
            total <- total + a[i];
        }
        wesosa (i < nb) {
            total <- total + b[i];
        }
        omse(result, total drossou 10);
        carry <- total / 10;
    }
    wesosa (carry > 0) {
        omse(result, carry);
    }
    cha result;
bawoum tosedo

tosedo multiplyDigits(a, b)
    sheye result <- [];
    sheye na <- louwo(a);
    sheye nb <- louwo(b);
    sheye size <- na + nb;
    sho (sheye i <- 0; i < size; i <- i + 1) {
        omse(result, 0);
    }
    sho (sheye i <- 0; i < na; i <- i + 1) {
        sho (sheye j <- 0; j < nb; j <- j + 1) {
            sheye k <- i + j;
            result[k] <- result[k] + (a[i] * b[j]);
        }
    }
    sho (sheye k <- 0; k < (size - 1); k <- k + 1) {
        sheye total <- result[k];
        result[k + 1] <- result[k + 1] + (total / 10);
        result[k] <- total drossou 10;
    }
    cha result;
bawoum tosedo

tosedo decimalText(digits)
    sheye i <- louwo(digits) - 1;
    veshim ((i > 0) dilisyo (digits[i] = 0)) {
        i <- i - 1;
    }
    sheye text <- "";
    veshim (i >= 0) {
        text <- text + digits[i];
        i <- i - 1;
    }
    cha text;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye split <- 0;
    veshim (line[split] <> " ") {
        split <- split + 1;
    }
    sheye a <- readDigits(line, 0, split);
    sheye b <- readDigits(line, split + 1, louwo(line));
    tivou decimalText(addDigits(a, b));
    wami " " + decimalText(multiplyDigits(a, b));
    line <- diwela();
}
</solution>
<solution task="t2-life">
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
    sheye nextGrid <- [];
    sho (sheye row <- 0; row < height; row <- row + 1) {
        sheye currentRow <- grid[row];
        sheye nextRow <- "";
        sho (sheye col <- 0; col < width; col <- col + 1) {
            sheye live <- 0;
            sho (sheye r <- row - 1; r <= (row + 1); r <- r + 1) {
                wesosa ((r < 0) emsoulve (r >= height)) {
                    chidrom;
                }
                sheye neighborRow <- grid[r];
                sho (sheye c <- col - 1; c <= (col + 1); c <- c + 1) {
                    wesosa ((c < 0) emsoulve (c >= width)) {
                        chidrom;
                    }
                    wesosa ((r = row) dilisyo (c = col)) {
                        chidrom;
                    }
                    wesosa (neighborRow[c] = "#") {
                        live <- live + 1;
                    }
                }
            }
            wesosa ((live = 3) emsoulve ((live = 2) dilisyo (currentRow[col] = "#"))) {
                nextRow <- nextRow + "#";
            } oli {
                nextRow <- nextRow + ".";
            }
        }
        omse(nextGrid, nextRow);
    }
    grid <- nextGrid;
}
sho (sheye row <- 0; row < height; row <- row + 1) {
    wami grid[row];
}
</solution>
<solution task="t2-rpn">
tosedo applyOperator(op, a, b)
    moumare amdre op
    amdre "+"
        cha a + b;
    amdre "-"
        cha a - b;
    amdre "*"
        cha a * b;
    bawoum moumare
    wesosa (b = 0) {
        cha malwe;
    }
    sheye q <- a / b;
    wesosa (((a < 0) <> (b < 0)) dilisyo ((a drossou b) <> 0)) {
        q <- q + 1;
    }
    wesosa (op = "/") {
        cha q;
    }
    cha a - (b * q);
bawoum tosedo

tosedo evaluate(line)
    sheye stack <- [];
    sheye depth <- 0;
    sheye size <- louwo(line);
    sheye i <- 0;
    veshim (i < size) {
        wesosa (line[i] = " ") {
            i <- i + 1;
            chidrom;
        }
        sheye start <- i;
        veshim (i < size) {
            wesosa (line[i] = " ") {
                bou;
            }
            i <- i + 1;
        }
        sheye first <- line[start];
        sheye value <- 0;
        sheye operatorToken <- (i = (start + 1)) dilisyo ((first = "+") emsoulve (first = "-") emsoulve (first = "*") emsoulve (first = "/") emsoulve (first = "%"));
        wesosa (operatorToken) {
            wesosa (depth < 2) {
                cha malwe;
            }
            sheye b <- stack[depth - 1];
            sheye a <- stack[depth - 2];
            depth <- depth - 2;
            value <- applyOperator(first, a, b);
            wesosa (value = malwe) {
                cha malwe;
            }
        } oli {
            sheye negative <- first = "-";
            sheye j <- start;
            wesosa (negative) {
                j <- j + 1;
            }
            wesosa (j = i) {
                cha malwe;
            }
            veshim (j < i) {
                sheye digit <- line[j];
                wesosa ((digit < "0") emsoulve (digit > "9")) {
                    cha malwe;
                }
                value <- (value * 10) - odresdra(digit);
                j <- j + 1;
            }
            wesosa (drol negative) {
                value <- -value;
            }
        }
        wesosa (depth = louwo(stack)) {
            omse(stack, value);
        } oli {
            stack[depth] <- value;
        }
        depth <- depth + 1;
    }
    wesosa (depth = 1) {
        cha stack[0];
    }
    cha malwe;
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye result <- evaluate(line);
    wesosa (result = malwe) {
        wami "error";
    } oli {
        wami result;
    }
    line <- diwela();
}
</solution>
<solution task="t2-wordfreq">
tosedo lowerLetter(ch)
    wesosa ((ch >= "a") dilisyo (ch <= "z")) {
        cha ch;
    }
    wesosa ((ch < "A") emsoulve (ch > "Z")) {
        cha malwe;
    }
    sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sheye lower <- "abcdefghijklmnopqrstuvwxyz";
    sheye lo <- 0;
    sheye hi <- 26;
    veshim (lo < hi) {
        sheye mid <- (lo + hi) / 2;
        wesosa (upper[mid] < ch) {
            lo <- mid + 1;
        } oli {
            hi <- mid;
        }
    }
    cha lower[lo];
bawoum tosedo

' Each trie node holds its first child, next sibling, letter, count and word.
tosedo findChild(parent, letter)
    sheye child <- parent[0];
    veshim (child <> malwe) {
        wesosa (child[2] = letter) {
            cha child;
        }
        child <- child[1];
    }
    sheye added <- [malwe, parent[0], letter, 0, ""];
    parent[0] <- added;
    cha added;
bawoum tosedo

tosedo recordWord(node, word, entries)
    wesosa (node[3] = 0) {
        node[4] <- word;
        omse(entries, node);
    }
    node[3] <- node[3] + 1;
bawoum tosedo

sheye root <- [malwe, malwe, "", 0, ""];
sheye entries <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye node <- root;
    sheye word <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye letter <- lowerLetter(line[i]);
        wesosa (letter <> malwe) {
            node <- findChild(node, letter);
            word <- word + letter;
        } oli wesosa (node <> root) {
            recordWord(node, word, entries);
            node <- root;
            word <- "";
        }
    }
    wesosa (node <> root) {
        recordWord(node, word, entries);
    }
    line <- diwela();
}

sho (sheye printed <- 0; (printed < 10) dilisyo (printed < louwo(entries)); printed <- printed + 1) {
    sheye best <- malwe;
    sheye bestCount <- 0;
    sheye bestWord <- "";
    sho (sheye i <- 0; i < louwo(entries); i <- i + 1) {
        sheye entry <- entries[i];
        sheye count <- entry[3];
        sheye word <- entry[4];
        wesosa ((count > bestCount) emsoulve ((count = bestCount) dilisyo (word < bestWord))) {
            best <- entry;
            bestCount <- count;
            bestWord <- word;
        }
    }
    tivou bestWord;
    wami " " + bestCount;
    best[3] <- 0;
}
</solution>