<solution task="t0-count">
sheye n <- odresdra(diwela());
sho (sheye i <- 1; i <= n; i <- i + 1) {
    wami i;
}
</solution>

<solution task="t0-day-names">
sheye line <- diwela();
veshim (line <> malwe) {
    moumare amdre odresdra(line)
    amdre 1
        wami "Monday";
    amdre 2
        wami "Tuesday";
    amdre 3
        wami "Wednesday";
    amdre 4
        wami "Thursday";
    amdre 5
        wami "Friday";
    amdre 6
        wami "Saturday";
    amdre 7
        wami "Sunday";
    amdre oli
        wami "invalid";
    bawoum moumare
    line <- diwela();
}
</solution>

<solution task="t0-even-odd">
sheye evenCount <- 0;
sheye oddCount <- 0;
sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    wesosa ((n drossou 2) = 0) {
        evenCount <- evenCount + 1;
    } oli {
        oddCount <- oddCount + 1;
    }
    line <- diwela();
}
wami "even " + evenCount;
wami "odd " + oddCount;
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
    tivou " ";
    wami reversed;
    line <- diwela();
}
</solution>

<solution task="t1-floordiv">
sheye line <- diwela();
veshim (line <> malwe) {
    sheye i <- 0;
    sheye leftText <- "";
    veshim (line[i] <> " ") {
        leftText <- leftText + line[i];
        i <- i + 1;
    }
    sheye rightText <- "";
    sho (i <- i + 1; i < louwo(line); i <- i + 1) {
        rightText <- rightText + line[i];
    }
    sheye a <- odresdra(leftText);
    sheye b <- odresdra(rightText);
    sheye q <- a / b;
    sheye r <- a - (b * q);
    tivou q;
    tivou " ";
    wami r;
    line <- diwela();
}
</solution>

<solution task="t1-palindromes">
tosedo normalize(c)
    wesosa (((c >= "a") dilisyo (c <= "z")) emsoulve ((c >= "0") dilisyo (c <= "9"))) {
        cha c;
    }
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        sheye lower <- "abcdefghijklmnopqrstuvwxyz";
        sheye lo <- 0;
        sheye hi <- 26;
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
    cha "";
bawoum tosedo

tosedo isPalindrome(line)
    sheye left <- 0;
    sheye right <- louwo(line) - 1;
    veshim (left < right) {
        sheye a <- normalize(line[left]);
        wesosa (a = "") {
            left <- left + 1;
            chidrom;
        }
        sheye b <- normalize(line[right]);
        wesosa (b = "") {
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
    wesosa (isPalindrome(line)) {
        wami "yes";
    } oli {
        wami "no";
    }
    line <- diwela();
}
</solution>

<solution task="t1-rank">
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
</solution>

<solution task="t1-rotate">
sheye k <- odresdra(diwela());
sheye items <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    omse(items, line);
    line <- diwela();
}
sheye size <- louwo(items);
wesosa (size > 0) {
    sho (sheye i <- 0; i < size; i <- i + 1) {
        wami items[(i - k) drossou size];
    }
}
</solution>

<solution task="t1-weekday">
tosedo decimal(line, first, end)
    sheye value <- 0;
    sho (sheye i <- first; i < end; i <- i + 1) {
        value <- (value * 10) + odresdra(line[i]);
    }
    cha value;
bawoum tosedo

sheye names <- ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
sheye monthOffsets <- [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye year <- decimal(line, 0, 4);
    sheye month <- decimal(line, 5, 7);
    sheye day <- decimal(line, 8, 10);
    sheye prior <- year - 1;
    sheye leapDays <- ((prior / 4) - (prior / 100)) + (prior / 400);
    sheye days <- (365 * prior) + leapDays;
    days <- days + (monthOffsets[month - 1] + (day - 1));
    sheye leap <- ((year drossou 4) = 0) dilisyo (((year drossou 100) <> 0) emsoulve ((year drossou 400) = 0));
    wesosa ((month > 2) dilisyo leap) {
        days <- days + 1;
    }
    wami names[days drossou 7];
    line <- diwela();
}
</solution>

<solution task="t2-bignum">
tosedo readDigits(line, first, end)
    sheye digits <- [];
    sho (sheye i <- end - 1; i >= first; i <- i - 1) {
        omse(digits, odresdra(line[i]));
    }
    cha digits;
bawoum tosedo

tosedo carryDigits(digits)
    sho (sheye i <- 0; i < (louwo(digits) - 1); i <- i + 1) {
        sheye value <- digits[i];
        digits[i] <- value drossou 10;
        digits[i + 1] <- digits[i + 1] + (value / 10);
    }
bawoum tosedo

tosedo writeDigits(digits)
    sheye i <- louwo(digits) - 1;
    veshim (i > 0) {
        wesosa (digits[i] <> 0) {
            bou;
        }
        i <- i - 1;
    }
    veshim (i >= 0) {
        tivou digits[i];
        i <- i - 1;
    }
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye separator <- 0;
    veshim (line[separator] <> " ") {
        separator <- separator + 1;
    }
    sheye a <- readDigits(line, 0, separator);
    sheye b <- readDigits(line, separator + 1, louwo(line));
    sheye aSize <- louwo(a);
    sheye bSize <- louwo(b);
    sheye size <- aSize + bSize;
    sheye sum <- [];
    sheye product <- [];
    sho (sheye i <- 0; i < size; i <- i + 1) {
        omse(sum, 0);
        omse(product, 0);
    }
    sho (sheye i <- 0; i < aSize; i <- i + 1) {
        sheye digit <- a[i];
        sum[i] <- digit;
        sho (sheye j <- 0; j < bSize; j <- j + 1) {
            sheye position <- i + j;
            product[position] <- product[position] + (digit * b[j]);
        }
    }
    sho (sheye j <- 0; j < bSize; j <- j + 1) {
        sum[j] <- sum[j] + b[j];
    }
    carryDigits(sum);
    carryDigits(product);
    writeDigits(sum);
    tivou " ";
    writeDigits(product);
    wami "";
    line <- diwela();
}
</solution>

<solution task="t2-life">
tosedo countNeighbors(grid, row, col, height, width)
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
sho (sheye generation <- 0; generation < generations; generation <- generation + 1) {
    sheye nextGrid <- [];
    sho (sheye row <- 0; row < height; row <- row + 1) {
        sheye cells <- grid[row];
        sheye nextRow <- "";
        sho (sheye col <- 0; col < width; col <- col + 1) {
            sheye neighbors <- countNeighbors(grid, row, col, height, width);
            wesosa ((neighbors = 3) emsoulve ((neighbors = 2) dilisyo (cells[col] = "#"))) {
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
tosedo readNumber(line, first, end)
    sheye negative <- line[first] = "-";
    wesosa (negative) {
        first <- first + 1;
    }
    wesosa (first = end) {
        cha malwe;
    }
    sheye value <- 0;
    sho (sheye i <- first; i < end; i <- i + 1) {
        sheye c <- line[i];
        wesosa ((c < "0") emsoulve (c > "9")) {
            cha malwe;
        }
        value <- (value * 10) + odresdra(c);
    }
    wesosa (negative) {
        cha -value;
    }
    cha value;
bawoum tosedo

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
    sheye pos <- 0;
    veshim (pos < size) {
        wesosa (line[pos] = " ") {
            pos <- pos + 1;
            chidrom;
        }
        sheye first <- pos;
        pos <- pos + 1;
        veshim (pos < size) {
            wesosa (line[pos] = " ") {
                bou;
            }
            pos <- pos + 1;
        }
        sheye op <- line[first];
        sheye isOperator <- ishe;
        wesosa ((pos - first) = 1) {
            moumare amdre op
            amdre "+", "-", "*", "/", "%"
                isOperator <- shilsa;
            bawoum moumare
        }
        wesosa (isOperator) {
            wesosa (depth < 2) {
                cha "error";
            }
            sheye b <- stack[depth - 1];
            sheye a <- stack[depth - 2];
            sheye result <- applyOperator(op, a, b);
            wesosa (result = malwe) {
                cha "error";
            }
            depth <- depth - 1;
            stack[depth - 1] <- result;
        } oli {
            sheye value <- readNumber(line, first, pos);
            wesosa (value = malwe) {
                cha "error";
            }
            wesosa (depth = louwo(stack)) {
                omse(stack, value);
            } oli {
                stack[depth] <- value;
            }
            depth <- depth + 1;
        }
    }
    wesosa (depth <> 1) {
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
tosedo lowerLetter(c)
    wesosa ((c >= "a") dilisyo (c <= "z")) {
        cha c;
    }
    wesosa ((c >= "A") dilisyo (c <= "Z")) {
        sheye upper <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        sheye lower <- "abcdefghijklmnopqrstuvwxyz";
        sheye lo <- 0;
        sheye hi <- 26;
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
    cha "";
bawoum tosedo

tosedo joinLetters(letters, first, end)
    wesosa ((end - first) = 1) {
        cha letters[first];
    }
    sheye mid <- (first + end) / 2;
    cha joinLetters(letters, first, mid) + joinLetters(letters, mid, end);
bawoum tosedo

tosedo recordWord(root, letters, entries)
    ' Each node stores a letter, its first child, its next sibling, a count and a word.
    sheye node <- root;
    sheye size <- louwo(letters);
    sho (sheye i <- 0; i < size; i <- i + 1) {
        sheye letter <- letters[i];
        sheye child <- node[1];
        veshim (child <> malwe) {
            wesosa (child[0] = letter) {
                bou;
            }
            child <- child[2];
        }
        wesosa (child = malwe) {
            child <- [letter, malwe, node[1], 0, ""];
            node[1] <- child;
        }
        node <- child;
    }
    wesosa (node[3] = 0) {
        node[4] <- joinLetters(letters, 0, size);
        omse(entries, node);
    }
    node[3] <- node[3] + 1;
bawoum tosedo

sheye root <- ["", malwe, malwe, 0, ""];
sheye entries <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye letters <- [];
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        sheye c <- lowerLetter(line[i]);
        wesosa (c <> "") {
            omse(letters, c);
        } oli wesosa (louwo(letters) > 0) {
            recordWord(root, letters, entries);
            letters <- [];
        }
    }
    wesosa (louwo(letters) > 0) {
        recordWord(root, letters, entries);
    }
    line <- diwela();
}

sho (sheye printed <- 0; printed < 10; printed <- printed + 1) {
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
    wesosa (bestCount = 0) {
        bou;
    }
    tivou bestWord;
    tivou " ";
    wami bestCount;
    best[3] <- 0;
}
</solution>