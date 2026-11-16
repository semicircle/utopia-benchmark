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
weltuxle f := 1;
keit (weltuxle i := 2; i <= n; i := i + 1) {
    f := f * i;
}
leshdei f;
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
keit (weltuxle i := dushzosh(lines) - 1; i >= 0; i := i - 1) {
    leshdei lines[i];
}
</solution>

<solution task="t1-digits">
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle n := leidush(line);
    weltuxle sign := 1;
    nei (n < 0) {
        sign := -1;
        n := -n;
    }
    weltuxle sum := 0;
    weltuxle rev := 0;
    nei (n == 0) {
        sum := 0;
        rev := 0;
    } wogeish {
        krenul (n > 0) {
            weltuxle d := n yeil 10;
            sum := sum + d;
            rev := rev * 10 + d;
            n := n / 10;
        }
    }
    leshdei sum + " " + sign * rev;
    line := lono();
}
</solution>

<solution task="t1-floordiv">
eilyot substr(s, a, b)
    weltuxle r := "";
    keit (weltuxle i := a; i < b; i := i + 1) {
        r := r + s[i];
    }
    chozulni r;
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle i := 0;
    weltuxle len := dushzosh(line);
    krenul (i < len) {
        nei (line[i] == " ") {
            exzulto;
        }
        i := i + 1;
    }
    weltuxle a := leidush(substr(line, 0, i));
    weltuxle b := leidush(substr(line, i + 1, len));
    weltuxle q := a / b;
    weltuxle r := a - b * q;
    nei (r <> 0) {
        nei ((r < 0) <> (b < 0)) {
            q := q - 1;
            r := r + b;
        }
    }
    leshdei q + " " + r;
    line := lono();
}
</solution>

<solution task="t1-palindromes">
eilyot isAlnum(c)
    weltuxle lower := "abcdefghijklmnopqrstuvwxyz";
    weltuxle upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    weltuxle digits := "0123456789";
    keit (weltuxle i := 0; i < 26; i := i + 1) {
        nei (c == lower[i]) {
            chozulni dut;
        }
        nei (c == upper[i]) {
            chozulni dut;
        }
    }
    keit (weltuxle i := 0; i < 10; i := i + 1) {
        nei (c == digits[i]) {
            chozulni dut;
        }
    }
    chozulni eikreit;
iweil

eilyot lowerChar(c)
    weltuxle lower := "abcdefghijklmnopqrstuvwxyz";
    weltuxle upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    keit (weltuxle i := 0; i < 26; i := i + 1) {
        nei (c == lower[i]) {
            chozulni c;
        }
        nei (c == upper[i]) {
            chozulni lower[i];
        }
    }
    chozulni c;
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle clean := "";
    keit (weltuxle i := 0; i < dushzosh(line); i := i + 1) {
        weltuxle c := line[i];
        nei (isAlnum(c)) {
            clean := clean + lowerChar(c);
        }
    }
    weltuxle L := dushzosh(clean);
    weltuxle ok := dut;
    keit (weltuxle i := 0; i < L / 2; i := i + 1) {
        nei (clean[i] <> clean[L - 1 - i]) {
            ok := eikreit;
        }
    }
    nei (ok) {
        leshdei "yes";
    } wogeish {
        leshdei "no";
    }
    line := lono();
}
</solution>

<solution task="t1-rank">
eilyot splitInts(line)
    weltuxle parts := [];
    weltuxle cur := "";
    weltuxle len := dushzosh(line);
    keit (weltuxle i := 0; i < len; i := i + 1) {
        nei (line[i] == " ") {
            nei (cur <> "") {
                koshkil(parts, cur);
            }
            cur := "";
        } wogeish {
            cur := cur + line[i];
        }
    }
    nei (cur <> "") {
        koshkil(parts, cur);
    }
    chozulni parts;
iweil

weltuxle first := lono();
weltuxle nums := [];
nei (first <> leitchux) {
    weltuxle parts := splitInts(first);
    keit (weltuxle i := 0; i < dushzosh(parts); i := i + 1) {
        koshkil(nums, leidush(parts[i]));
    }
}
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle q := leidush(line);
    weltuxle cnt := 0;
    weltuxle found := eikreit;
    keit (weltuxle i := 0; i < dushzosh(nums); i := i + 1) {
        nei (nums[i] < q) {
            cnt := cnt + 1;
        }
        nei (nums[i] == q) {
            found := dut;
        }
    }
    nei (found) {
        leshdei cnt + " found";
    } wogeish {
        leshdei cnt + " missing";
    }
    line := lono();
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
weltuxle m := dushzosh(items);
nei (m > 0) {
    weltuxle shift := k yeil m;
    nei (shift < 0) {
        shift := shift + m;
    }
    keit (weltuxle i := 0; i < m; i := i + 1) {
        leshdei items[i - shift];
    }
}
</solution>

<solution task="t1-weekday">
eilyot substr(s, a, b)
    weltuxle r := "";
    keit (weltuxle i := a; i < b; i := i + 1) {
        r := r + s[i];
    }
    chozulni r;
iweil

weltuxle cum := [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
weltuxle names := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle y := leidush(substr(line, 0, 4));
    weltuxle mo := leidush(substr(line, 5, 7));
    weltuxle d := leidush(substr(line, 8, 10));
    weltuxle yy := y - 1;
    weltuxle beforeYear := 365 * yy + yy / 4 - yy / 100 + yy / 400;
    weltuxle leap := ((y yeil 4 == 0) elish (y yeil 100 <> 0)) yosheil (y yeil 400 == 0);
    weltuxle beforeMonth := cum[mo - 1];
    nei (leap) {
        nei (mo > 2) {
            beforeMonth := beforeMonth + 1;
        }
    }
    weltuxle elapsed := beforeYear + beforeMonth + (d - 1);
    leshdei names[elapsed yeil 7];
    line := lono();
}
</solution>

<solution task="t2-bignum">
eilyot substr(s, a, b)
    weltuxle r := "";
    keit (weltuxle i := a; i < b; i := i + 1) {
        r := r + s[i];
    }
    chozulni r;
iweil

eilyot splitTwo(line)
    weltuxle i := 0;
    weltuxle len := dushzosh(line);
    krenul (i < len) {
        nei (line[i] == " ") {
            exzulto;
        }
        i := i + 1;
    }
    chozulni [substr(line, 0, i), substr(line, i + 1, len)];
iweil

eilyot parseBig(s)
    weltuxle ds := [];
    keit (weltuxle i := dushzosh(s) - 1; i >= 0; i := i - 1) {
        koshkil(ds, leidush(s[i]));
    }
    chozulni ds;
iweil

eilyot dig(a, i)
    nei (i < dushzosh(a)) {
        chozulni a[i];
    }
    chozulni 0;
iweil

eilyot addBig(a, b)
    weltuxle res := [];
    weltuxle carry := 0;
    weltuxle n := dushzosh(a);
    nei (dushzosh(b) > n) {
        n := dushzosh(b);
    }
    keit (weltuxle i := 0; i < n; i := i + 1) {
        weltuxle s := dig(a, i) + dig(b, i) + carry;
        koshkil(res, s yeil 10);
        carry := s / 10;
    }
    nei (carry > 0) {
        koshkil(res, carry);
    }
    chozulni res;
iweil

eilyot mulBig(a, b)
    weltuxle la := dushzosh(a);
    weltuxle lb := dushzosh(b);
    weltuxle res := [];
    keit (weltuxle i := 0; i < la + lb; i := i + 1) {
        koshkil(res, 0);
    }
    keit (weltuxle i := 0; i < la; i := i + 1) {
        weltuxle carry := 0;
        keit (weltuxle j := 0; j < lb; j := j + 1) {
            weltuxle cur := res[i + j] + a[i] * b[j] + carry;
            res[i + j] := cur yeil 10;
            carry := cur / 10;
        }
        weltuxle k := i + lb;
        krenul (carry > 0) {
            weltuxle cur := res[k] + carry;
            res[k] := cur yeil 10;
            carry := cur / 10;
            k := k + 1;
        }
    }
    chozulni res;
iweil

eilyot bigToString(a)
    weltuxle n := dushzosh(a);
    weltuxle top := n - 1;
    krenul (top > 0) {
        nei (a[top] == 0) {
            top := top - 1;
        } wogeish {
            exzulto;
        }
    }
    weltuxle s := "";
    keit (weltuxle i := top; i >= 0; i := i - 1) {
        s := s + sheiyidi(a[i]);
    }
    chozulni s;
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle parts := splitTwo(line);
    weltuxle a := parseBig(parts[0]);
    weltuxle b := parseBig(parts[1]);
    weltuxle s := addBig(a, b);
    weltuxle p := mulBig(a, b);
    leshdei bigToString(s) + " " + bigToString(p);
    line := lono();
}
</solution>

<solution task="t2-life">
weltuxle g := leidush(lono());
weltuxle grid := [];
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle row := [];
    keit (weltuxle i := 0; i < dushzosh(line); i := i + 1) {
        nei (line[i] == "#") {
            koshkil(row, 1);
        } wogeish {
            koshkil(row, 0);
        }
    }
    koshkil(grid, row);
    line := lono();
}
weltuxle rows := dushzosh(grid);
weltuxle cols := 0;
nei (rows > 0) {
    cols := dushzosh(grid[0]);
}
keit (weltuxle gen := 0; gen < g; gen := gen + 1) {
    weltuxle next := [];
    keit (weltuxle r := 0; r < rows; r := r + 1) {
        weltuxle nrow := [];
        weltuxle crow := grid[r];
        keit (weltuxle c := 0; c < cols; c := c + 1) {
            weltuxle cnt := 0;
            keit (weltuxle dr := -1; dr <= 1; dr := dr + 1) {
                keit (weltuxle dc := -1; dc <= 1; dc := dc + 1) {
                    nei (dr == 0) {
                        nei (dc == 0) {
                            weshosho;
                        }
                    }
                    weltuxle nr := r + dr;
                    weltuxle nc := c + dc;
                    nei (nr >= 0) {
                        nei (nr < rows) {
                            nei (nc >= 0) {
                                nei (nc < cols) {
                                    weltuxle rr := grid[nr];
                                    cnt := cnt + rr[nc];
                                }
                            }
                        }
                    }
                }
            }
            weltuxle na := 0;
            nei (crow[c] == 1) {
                nei (cnt == 2) {
                    na := 1;
                }
                nei (cnt == 3) {
                    na := 1;
                }
            } wogeish {
                nei (cnt == 3) {
                    na := 1;
                }
            }
            koshkil(nrow, na);
        }
        koshkil(next, nrow);
    }
    grid := next;
}
keit (weltuxle r := 0; r < rows; r := r + 1) {
    weltuxle s := "";
    weltuxle rr := grid[r];
    keit (weltuxle c := 0; c < cols; c := c + 1) {
        nei (rr[c] == 1) {
            s := s + "#";
        } wogeish {
            s := s + ".";
        }
    }
    leshdei s;
}
</solution>

<solution task="t2-rpn">
eilyot isInt(t)
    weltuxle n := dushzosh(t);
    nei (n == 0) {
        chozulni eikreit;
    }
    weltuxle i := 0;
    nei (t[0] == "-") {
        nei (n == 1) {
            chozulni eikreit;
        }
        i := 1;
    }
    krenul (i < n) {
        weltuxle c := t[i];
        nei (c >= "0") {
            nei (c <= "9") {
                i := i + 1;
                weshosho;
            }
        }
        chozulni eikreit;
    }
    chozulni dut;
iweil

weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle toks := [];
    weltuxle cur := "";
    keit (weltuxle i := 0; i < dushzosh(line); i := i + 1) {
        weltuxle c := line[i];
        nei (c == " ") {
            nei (cur <> "") {
                koshkil(toks, cur);
                cur := "";
            }
        } wogeish {
            cur := cur + c;
        }
    }
    nei (cur <> "") {
        koshkil(toks, cur);
    }
    weltuxle stack := [];
    weltuxle size := 0;
    weltuxle bad := eikreit;
    keit (weltuxle i := 0; i < dushzosh(toks); i := i + 1) {
        weltuxle t := toks[i];
        nei (bad) {
            weshosho;
        }
        weltuxle isop := eikreit;
        weltuxle op := "";
        nei (t == "+") {
            isop := dut;
            op := "+";
        }
        nei (t == "-") {
            isop := dut;
            op := "-";
        }
        nei (t == "*") {
            isop := dut;
            op := "*";
        }
        nei (t == "/") {
            isop := dut;
            op := "/";
        }
        nei (t == "%") {
            isop := dut;
            op := "%";
        }
        nei (isop) {
            nei (size < 2) {
                bad := dut;
            } wogeish {
                weltuxle b := stack[size - 1];
                size := size - 1;
                weltuxle a := stack[size - 1];
                size := size - 1;
                weltuxle res := 0;
                nei (op == "+") {
                    res := a + b;
                }
                nei (op == "-") {
                    res := a - b;
                }
                nei (op == "*") {
                    res := a * b;
                }
                nei (op == "/") {
                    nei (b == 0) {
                        bad := dut;
                    } wogeish {
                        weltuxle q := a / b;
                        weltuxle rr := a - b * q;
                        nei (rr <> 0) {
                            nei ((a < 0) == (b < 0)) {
                                q := q - 1;
                            }
                        }
                        res := q;
                    }
                }
                nei (op == "%") {
                    nei (b == 0) {
                        bad := dut;
                    } wogeish {
                        weltuxle q := a / b;
                        weltuxle rr := a - b * q;
                        nei (rr <> 0) {
                            nei ((a < 0) == (b < 0)) {
                                q := q - 1;
                            }
                        }
                        res := a - b * q;
                    }
                }
                nei (bad) {
                } wogeish {
                    nei (size < dushzosh(stack)) {
                        stack[size] := res;
                    } wogeish {
                        koshkil(stack, res);
                    }
                    size := size + 1;
                }
            }
        } wogeish {
            nei (isInt(t)) {
                weltuxle v := leidush(t);
                nei (size < dushzosh(stack)) {
                    stack[size] := v;
                } wogeish {
                    koshkil(stack, v);
                }
                size := size + 1;
            } wogeish {
                bad := dut;
            }
        }
    }
    nei (bad) {
        leshdei "error";
    } wogeish nei (size <> 1) {
        leshdei "error";
    } wogeish {
        leshdei stack[size - 1];
    }
    line := lono();
}
</solution>

<solution task="t2-wordfreq">
eilyot isLetter(c)
    nei (c >= "a") {
        nei (c <= "z") {
            chozulni dut;
        }
    }
    nei (c >= "A") {
        nei (c <= "Z") {
            chozulni dut;
        }
    }
    chozulni eikreit;
iweil

eilyot lowerChar(c)
    weltuxle lower := "abcdefghijklmnopqrstuvwxyz";
    weltuxle upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    keit (weltuxle i := 0; i < 26; i := i + 1) {
        nei (c == lower[i]) {
            chozulni c;
        }
        nei (c == upper[i]) {
            chozulni lower[i];
        }
    }
    chozulni c;
iweil

eilyot addWord(wlist, clist, w)
    keit (weltuxle j := 0; j < dushzosh(wlist); j := j + 1) {
        nei (wlist[j] == w) {
            clist[j] := clist[j] + 1;
            chozulni leitchux;
        }
    }
    koshkil(wlist, w);
    koshkil(clist, 1);
    chozulni leitchux;
iweil

weltuxle wlist := [];
weltuxle clist := [];
weltuxle line := lono();
krenul (line <> leitchux) {
    weltuxle cur := "";
    keit (weltuxle i := 0; i < dushzosh(line); i := i + 1) {
        weltuxle c := line[i];
        nei (isLetter(c)) {
            cur := cur + lowerChar(c);
        } wogeish {
            nei (cur <> "") {
                addWord(wlist, clist, cur);
                cur := "";
            }
        }
    }
    nei (cur <> "") {
        addWord(wlist, clist, cur);
    }
    line := lono();
}
weltuxle printed := 0;
krenul (printed < 10) {
    weltuxle n := dushzosh(wlist);
    nei (n == 0) {
        exzulto;
    }
    weltuxle best := 0;
    keit (weltuxle i := 1; i < n; i := i + 1) {
        weltuxle better := eikreit;
        nei (clist[i] > clist[best]) {
            better := dut;
        }
        nei (clist[i] == clist[best]) {
            nei (wlist[i] < wlist[best]) {
                better := dut;
            }
        }
        nei (better) {
            best := i;
        }
    }
    leshdei wlist[best] + " " + clist[best];
    weltuxle nw := [];
    weltuxle nc := [];
    keit (weltuxle i := 0; i < n; i := i + 1) {
        nei (i == best) {
            weshosho;
        }
        koshkil(nw, wlist[i]);
        koshkil(nc, clist[i]);
    }
    wlist := nw;
    clist := nc;
    printed := printed + 1;
}
</solution>