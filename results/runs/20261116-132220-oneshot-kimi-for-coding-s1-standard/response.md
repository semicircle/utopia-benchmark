<solution task="t0-count">
weltuxle n := leidush(lono());
keit (weltuxle i := 1; i <= n; i := i + 1) {
    leshdei i;
}
</solution>

<solution task="t0-day-names">
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle n := leidush(line);
    yishzit n eixwo
    1: krei
        leshdei "Monday";
    zushox
    2: krei
        leshdei "Tuesday";
    zushox
    3: krei
        leshdei "Wednesday";
    zushox
    4: krei
        leshdei "Thursday";
    zushox
    5: krei
        leshdei "Friday";
    zushox
    6: krei
        leshdei "Saturday";
    zushox
    7: krei
        leshdei "Sunday";
    zushox
    wogeish krei
        leshdei "invalid";
    zushox zushox
    line := lono();
}
</solution>

<solution task="t0-even-odd">
weltuxle even := 0;
weltuxle odd := 0;
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle n := leidush(line);
    nei (n yeil 2 == 0) {
        even := even + 1;
    } wogeish {
        odd := odd + 1;
    }
    line := lono();
}
leshdei "even " + even;
leshdei "odd " + odd;
</solution>

<solution task="t0-factorial">
weltuxle n := leidush(lono());
weltuxle result := 1;
keit (weltuxle i := 2; i <= n; i := i + 1) {
    result := result * i;
}
leshdei result;
</solution>

<solution task="t0-fizzbuzz">
weltuxle n := leidush(lono());
keit (weltuxle i := 1; i <= n; i := i + 1) {
    nei (i yeil 15 == 0) {
        leshdei "FizzBuzz";
    } wogeish nei (i yeil 3 == 0) {
        leshdei "Fizz";
    } wogeish nei (i yeil 5 == 0) {
        leshdei "Buzz";
    } wogeish {
        leshdei i;
    }
}
</solution>

<solution task="t0-hello">
leshdei "Hello, Utopia!";
</solution>

<solution task="t0-reverse-lines">
weltuxle lines := [];
weltuxle line := lono();
krenul (line <> leitchux) {
    koshkil(lines, line);
    line := lono();
}
weltuxle count := dushzosh(lines);
keit (weltuxle i := count - 1; i >= 0; i := i - 1) {
    leshdei lines[i];
}
</solution>

<solution task="t1-digits">
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle n := leidush(line);
    nei (n == 0) {
        leshdei "0 0";
    } wogeish {
        weltuxle neg := n < 0;
        weltuxle x := n;
        nei (neg) {
            x := -x;
        }
        weltuxle sum := 0;
        weltuxle rev := 0;
        krenul (x > 0) {
            weltuxle d := x yeil 10;
            sum := sum + d;
            rev := rev * 10 + d;
            x := x / 10;
        }
        nei (neg) {
            leshdei sum + " -" + rev;
        } wogeish {
            leshdei sum + " " + rev;
        }
    }
    line := lono();
}
</solution>

<solution task="t1-floordiv">
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle space := 0;
    krenul (line[space] <> " ") {
        space := space + 1;
    }
    weltuxle a := leidush(substring(line, 0, space));
    weltuxle b := leidush(substring(line, space + 1, dushzosh(line)));
    weltuxle q := a / b;
    weltuxle r := a - b * q;
    nei (r <> 0 yosheil ((r > 0) <> (b > 0))) {
        q := q - 1;
        r := a - b * q;
    }
    leshdei q + " " + r;
    line := lono();
}

eilyot substring(s, first, past)
    weltuxle result := "";
    keit (weltuxle i := first; i < past; i := i + 1) {
        result := result + s[i];
    }
    chozulni result;
iweil
</solution>

<solution task="t1-palindromes">
eilyot isDigit(c)
    chozulni (c >= "0") elish (c <= "9");
iweil

eilyot isLetter(c)
    chozulni ((c >= "a") elish (c <= "z")) yosheil ((c >= "A") elish (c <= "Z"));
iweil

eilyot lowerChar(c)
    weltuxle upper := ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
    weltuxle lower := ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
    keit (weltuxle i := 0; i < 26; i := i + 1) {
        nei (c == upper[i]) {
            chozulni lower[i];
        }
    }
    chozulni c;
iweil

eilyot normalized(s)
    weltuxle result := "";
    keit (weltuxle i := 0; i < dushzosh(s); i := i + 1) {
        weltuxle c := s[i];
        nei (isDigit(c) yosheil isLetter(c)) {
            result := result + lowerChar(c);
        }
    }
    chozulni result;
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle s := normalized(line);
    weltuxle yes := dut;
    keit (weltuxle i := 0; i < dushzosh(s) / 2; i := i + 1) {
        nei (s[i] <> s[dushzosh(s) - 1 - i]) {
            yes := eikreit;
        }
    }
    nei (yes) {
        leshdei "yes";
    } wogeish {
        leshdei "no";
    }
    line := lono();
}
</solution>

<solution task="t1-rank">
eilyot substring(s, first, past)
    weltuxle result := "";
    keit (weltuxle i := first; i < past; i := i + 1) {
        result := result + s[i];
    }
    chozulni result;
iweil

eilyot parseInts(line)
    weltuxle result := [];
    weltuxle i := 0;
    krenul (i < dushzosh(line)) {
        krenul (i < dushzosh(line) yosheil line[i] == " ") {
            i := i + 1;
        }
        nei (i >= dushzosh(line)) {
            exzulto;
        }
        weltuxle first := i;
        krenul (i < dushzosh(line) yosheil line[i] <> " ") {
            i := i + 1;
        }
        koshkil(result, leidush(substring(line, first, i)));
    }
    chozulni result;
iweil

eilyot lowerBound(xs, query)
    weltuxle lo := 0;
    weltuxle hi := dushzosh(xs);
    krenul (lo < hi) {
        weltuxle mid := (lo + hi) / 2;
        nei (xs[mid] < query) {
            lo := mid + 1;
        } wogeish {
            hi := mid;
        }
    }
    chozulni lo;
iweil

weltuxle firstLine := lono();
nei (firstLine <> leitchux) {
    weltuxle values := parseInts(firstLine);
    weltuxle line := lono();
    krenul (line <> leitchux) {
        weltuxle q := leidush(line);
        weltuxle pos := lowerBound(values, q);
        weltuxle found := pos < dushzosh(values) yosheil values[pos] == q;
        zulkucho pos + " ";
        nei (found) {
            leshdei "found";
        } wogeish {
            leshdei "missing";
        }
        line := lono();
    }
}
</solution>

<solution task="t1-rotate">
weltuxle k := leidush(lono());
weltuxle items := [];
weltuxle line := lono();
krenul (line <> leitchux) {
    koshkil(items, line);
    line := lono();
}
weltuxle count := dushzosh(items);
nei (count > 0) {
    weltuxle shift := k yeil count;
    nei (shift < 0) {
        shift := shift + count;
    }
    shift := shift yeil count;
    weltuxle start := count - shift;
    keit (weltuxle i := 0; i < count; i := i + 1) {
        leshdei items[(start + i) yeil count];
    }
}
</solution>

<solution task="t1-weekday">
eilyot substring(s, first, past)
    weltuxle result := "";
    keit (weltuxle i := first; i < past; i := i + 1) {
        result := result + s[i];
    }
    chozulni result;
iweil

eilyot dayName(index)
    yishzit index eixwo
    0: krei
        chozulni "Monday";
    zushox
    1: krei
        chozulni "Tuesday";
    zushox
    2: krei
        chozulni "Wednesday";
    zushox
    3: krei
        chozulni "Thursday";
    zushox
    4: krei
        chozulni "Friday";
    zushox
    5: krei
        chozulni "Saturday";
    zushox
    wogeish krei
        chozulni "Sunday";
    zushox zushox
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle y := leidush(substring(line, 0, 4));
    weltuxle m := leidush(substring(line, 5, 7));
    weltuxle d := leidush(substring(line, 8, 10));
    weltuxle ym := y - 1;
    weltuxle days := 365 * ym + ym / 4 - ym / 100 + ym / 400;
    weltuxle leap := (y yeil 4 == 0 yosheil y yeil 100 <> 0) yosheil (y yeil 400 == 0);
    weltuxle monthDays := [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    keit (weltuxle month := 1; month < m; month := month + 1) {
        days := days + monthDays[month - 1];
        nei (month == 2 yosheil leap) {
            days := days + 1;
        }
    }
    days := days + d - 1;
    leshdei dayName(days yeil 7);
    line := lono();
}
</solution>

<solution task="t2-bignum">
eilyot substring(s, first, past)
    weltuxle result := "";
    keit (weltuxle i := first; i < past; i := i + 1) {
        result := result + s[i];
    }
    chozulni result;
iweil

eilyot parseBig(line, first, past)
    weltuxle digits := [];
    keit (weltuxle i := past - 1; i >= first; i := i - 1) {
        koshkil(digits, leidush(line[i]));
    }
    chozulni digits;
iweil

eilyot bigString(digits)
    weltuxle result := "";
    keit (weltuxle i := dushzosh(digits) - 1; i >= 0; i := i - 1) {
        result := result + sheiyidi(digits[i]);
    }
    chozulni result;
iweil

eilyot bigAdd(a, b)
    weltuxle result := [];
    weltuxle carry := 0;
    weltuxle i := 0;
    krenul (i < dushzosh(a) yosheil i < dushzosh(b) yosheil carry <> 0) {
        weltuxle da := 0;
        weltuxle db := 0;
        nei (i < dushzosh(a)) {
            da := a[i];
        }
        nei (i < dushzosh(b)) {
            db := b[i];
        }
        weltuxle total := da + db + carry;
        koshkil(result, total yeil 10);
        carry := total / 10;
        i := i + 1;
    }
    chozulni result;
iweil

eilyot bigMul(a, b)
    weltuxle result := [];
    keit (weltuxle i := 0; i < dushzosh(a); i := i + 1) {
        weltuxle carry := 0;
        keit (weltuxle j := 0; j < dushzosh(b); j := j + 1) {
            weltuxle p := i + j;
            weltuxle current := 0;
            nei (p < dushzosh(result)) {
                current := result[p];
            }
            weltuxle total := current + a[i] * b[j] + carry;
            nei (p < dushzosh(result)) {
                result[p] := total yeil 10;
            } wogeish {
                koshkil(result, total yeil 10);
            }
            carry := total / 10;
        }
        weltuxle p := i + dushzosh(b);
        krenul (carry <> 0) {
            weltuxle current := 0;
            nei (p < dushzosh(result)) {
                current := result[p];
            }
            weltuxle total := current + carry;
            nei (p < dushzosh(result)) {
                result[p] := total yeil 10;
            } wogeish {
                koshkil(result, total yeil 10);
            }
            carry := total / 10;
            p := p + 1;
        }
    }
    krenul (dushzosh(result) > 1 yosheil result[dushzosh(result) - 1] == 0) {
        weltuxle shorter := [];
        keit (weltuxle i := 0; i < dushzosh(result) - 1; i := i + 1) {
            koshkil(shorter, result[i]);
        }
        result := shorter;
    }
    chozulni result;
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle space := 0;
    krenul (line[space] <> " ") {
        space := space + 1;
    }
    weltuxle a := parseBig(line, 0, space);
    weltuxle b := parseBig(line, space + 1, dushzosh(line));
    leshdei bigString(bigAdd(a, b)) + " " + bigString(bigMul(a, b));
    line := lono();
}
</solution>

<solution task="t2-life">
eilyot nextGeneration(grid)
    weltuxle h := dushzosh(grid);
    weltuxle w := dushzosh(grid[0]);
    weltuxle result := [];
    keit (weltuxle r := 0; r < h; r := r + 1) {
        weltuxle row := "";
        keit (weltuxle c := 0; c < w; c := c + 1) {
            weltuxle neighbours := 0;
            keit (weltuxle dr := -1; dr <= 1; dr := dr + 1) {
                keit (weltuxle dc := -1; dc <= 1; dc := dc + 1) {
                    nei (dr == 0 yosheil dc == 0) {
                        weshosho;
                    }
                    weltuxle nr := r + dr;
                    weltuxle nc := c + dc;
                    nei (nr >= 0 yosheil nr < h yosheil nc >= 0 yosheil nc < w yosheil grid[nr][nc] == "#") {
                        neighbours := neighbours + 1;
                    }
                }
            }
            nei (neighbours == 3 yosheil (grid[r][c] == "#" yosheil neighbours == 2)) {
                row := row + "#";
            } wogeish {
                row := row + ".";
            }
        }
        koshkil(result, row);
    }
    chozulni result;
iweil

weltuxle generations := leidush(lono());
weltuxle grid := [];
weltuxle line := lono();
krenul (line <> leitchux) {
    koshkil(grid, line);
    line := lono();
}
keit (weltuxle g := 0; g < generations; g := g + 1) {
    grid := nextGeneration(grid);
}
keit (weltuxle i := 0; i < dushzosh(grid); i := i + 1) {
    leshdei grid[i];
}
</solution>

<solution task="t2-rpn">
eilyot substring(s, first, past)
    weltuxle result := "";
    keit (weltuxle i := first; i < past; i := i + 1) {
        result := result + s[i];
    }
    chozulni result;
iweil

eilyot isDigitChar(c)
    chozulni (c >= "0") elish (c <= "9");
iweil

eilyot isIntegerToken(token)
    weltuxle start := 0;
    nei (dushzosh(token) > 0 yosheil token[0] == "-") {
        start := 1;
    }
    nei (start == dushzosh(token)) {
        chozulni eikreit;
    }
    keit (weltuxle i := start; i < dushzosh(token); i := i + 1) {
        nei (tilteiyo isDigitChar(token[i])) {
            chozulni eikreit;
        }
    }
    chozulni dut;
iweil

eilyot evaluate(line)
    weltuxle stack := [];
    weltuxle hadToken := eikreit;
    weltuxle bad := eikreit;
    weltuxle i := 0;
    krenul (i < dushzosh(line) yosheil tilteiyo bad) {
        krenul (i < dushzosh(line) yosheil line[i] == " ") {
            i := i + 1;
        }
        nei (i >= dushzosh(line)) {
            exzulto;
        }
        weltuxle first := i;
        krenul (i < dushzosh(line) yosheil line[i] <> " ") {
            i := i + 1;
        }
        weltuxle token := substring(line, first, i);
        hadToken := dut;
        nei (token == "+" yosheil token == "-" yosheil token == "*" yosheil token == "/" yosheil token == "%") {
            nei (dushzosh(stack) < 2) {
                bad := dut;
            } wogeish {
                weltuxle b := stack[dushzosh(stack) - 1];
                weltuxle a := stack[dushzosh(stack) - 2];
                weltuxle value := 0;
                weltuxle okay := dut;
                nei (token == "+") {
                    value := a + b;
                } wogeish nei (token == "-") {
                    value := a - b;
                } wogeish nei (token == "*") {
                    value := a * b;
                } wogeish nei (token == "/") {
                    nei (b == 0) {
                        okay := eikreit;
                    } wogeish {
                        value := a / b;
                    }
                } wogeish {
                    nei (b == 0) {
                        okay := eikreit;
                    } wogeish {
                        value := a yeil b;
                    }
                }
                nei (okay) {
                    weltuxle next := [];
                    keit (weltuxle j := 0; j < dushzosh(stack) - 2; j := j + 1) {
                        koshkil(next, stack[j]);
                    }
                    koshkil(next, value);
                    stack := next;
                } wogeish {
                    bad := dut;
                }
            }
        } wogeish nei (isIntegerToken(token)) {
            koshkil(stack, leidush(token));
        } wogeish {
            bad := dut;
        }
    }
    nei (bad yosheil tilteiyo hadToken yosheil dushzosh(stack) <> 1) {
        chozulni [dut, 0];
    }
    chozulni [eikreit, stack[0]];
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle answer := evaluate(line);
    nei (answer[0]) {
        leshdei "error";
    } wogeish {
        leshdei answer[1];
    }
    line := lono();
}
</solution>

<solution task="t2-wordfreq">
eilyot substring(s, first, past)
    weltuxle result := "";
    keit (weltuxle i := first; i < past; i := i + 1) {
        result := result + s[i];
    }
    chozulni result;
iweil

eilyot isLetter(c)
    chozulni ((c >= "a") elish (c <= "z")) yosheil ((c >= "A") elish (c <= "Z"));
iweil

eilyot lowerChar(c)
    weltuxle upper := ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
    weltuxle lower := ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
    keit (weltuxle i := 0; i < 26; i := i + 1) {
        nei (c == upper[i]) {
            chozulni lower[i];
        }
    }
    chozulni c;
iweil

eilyot lowerWord(word)
    weltuxle result := "";
    keit (weltuxle i := 0; i < dushzosh(word); i := i + 1) {
        result := result + lowerChar(word[i]);
    }
    chozulni result;
iweil

weltuxle words := [];
weltuxle counts := [];
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle i := 0;
    krenul (i < dushzosh(line)) {
        krenul (i < dushzosh(line) yosheil tilteiyo isLetter(line[i])) {
            i := i + 1;
        }
        nei (i >= dushzosh(line)) {
            exzulto;
        }
        weltuxle first := i;
        krenul (i < dushzosh(line) yosheil isLetter(line[i])) {
            i := i + 1;
        }
        weltuxle word := lowerWord(substring(line, first, i));
        weltuxle foundAt := -1;
        keit (weltuxle j := 0; j < dushzosh(words); j := j + 1) {
            nei (words[j] == word) {
                foundAt := j;
            }
        }
        nei (foundAt < 0) {
            koshkil(words, word);
            koshkil(counts, 1);
        } wogeish {
            counts[foundAt] := counts[foundAt] + 1;
        }
    }
    line := lono();
}
weltuxle used := [];
keit (weltuxle i := 0; i < dushzosh(words); i := i + 1) {
    koshkil(used, eikreit);
}
keit (weltuxle rank := 0; rank < 10 yosheil rank < dushzosh(words); rank := rank + 1) {
    weltuxle best := -1;
    keit (weltuxle i := 0; i < dushzosh(words); i := i + 1) {
        nei (tilteiyo used[i]) {
            nei (best < 0 yosheil counts[i] > counts[best] yosheil (counts[i] == counts[best] yosheil words[i] < words[best])) {
                best := i;
            }
        }
    }
    nei (best < 0) {
        exzulto;
    }
    leshdei words[best] + " " + counts[best];
    used[best] := dut;
}
</solution>