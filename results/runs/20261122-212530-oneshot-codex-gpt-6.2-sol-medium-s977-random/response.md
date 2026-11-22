<solution task="t0-count">
Koke n := Bupuxbo(Pewexpo()).
Gipolu i := 1 Wexdush n Gihe Hehokgi
    Ebi i.
Kobihek
</solution>

<solution task="t0-day-names">
Koke days := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke n := Bupuxbo(line).
    Yopok (n < 1) Dak (n > 7), invalid_day.
    Ebi days[n].
    Uxdrush next_line.
invalid_day:
    Ebi "invalid".
next_line:
    line := Pewexpo().
Kobihek
</solution>

<solution task="t0-even-odd">
Koke even := 0.
Koke odd := 0.
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Yopok Bupuxbo(line) % 2 /= 0, count_odd.
    even := even + 1.
    Uxdrush next_line.
count_odd:
    odd := odd + 1.
next_line:
    line := Pewexpo().
Kobihek
Ebi "even " ++ even.
Ebi "odd " ++ odd.
</solution>

<solution task="t0-factorial">
Koke n := Bupuxbo(Pewexpo()).
Koke product := 1.
Gipolu i := 2 Wexdush n Gihe Hehokgi
    product := product * i.
Kobihek
Ebi product.
</solution>

<solution task="t0-fizzbuzz">
Yokyi fizzbuzz(n) {
    Yopok n % 15 == 0, both.
    Yopok n % 3 == 0, three.
    Yopok n % 5 == 0, five.
    Pohuwu n.
both:
    Pohuwu "FizzBuzz".
three:
    Pohuwu "Fizz".
five:
    Pohuwu "Buzz".
}

Koke n := Bupuxbo(Pewexpo()).
Gipolu i := 1 Wexdush n Gihe Hehokgi
    Ebi fizzbuzz(i).
Kobihek
</solution>

<solution task="t0-hello">
Ebi "Hello, Utopia!".
</solution>

<solution task="t0-reverse-lines">
Koke lines := [].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Oxba(lines, line).
    line := Pewexpo().
Kobihek

Gipolu i := Yik(lines) Wexdush 1 Drix -1 Gihe Hehokgi
    Ebi lines[i].
Kobihek
</solution>

<solution task="t1-digits">
Yokyi digit_result(n) {
    Koke sign := 1.
    Yopok n >= 0, take_digits.
    sign := -1.
    n := -n.
take_digits:
    Koke sum := 0.
    Koke reversed := 0.
    Puwadish n > 0 Gihe Hehokgi
        Koke q := -(-n / 10).
        Koke digit := n - (10 * q).
        sum := sum + digit.
        reversed := reversed * 10 + digit.
        n := q.
    Kobihek
    Pohuwu sum ++ " " ++ (sign * reversed).
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Ebi digit_result(Bupuxbo(line)).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-floordiv">
Yokyi divide_line(line) {
    Koke first := "".
    Koke second := "".
    Koke i := 1.
    Puwadish line[i] /= " " Gihe Hehokgi
        first := first ++ line[i].
        i := i + 1.
    Kobihek
    Gipolu j := i + 1 Wexdush Yik(line) Gihe Hehokgi
        second := second ++ line[j].
    Kobihek
    Koke a := Bupuxbo(first).
    Koke b := Bupuxbo(second).
    Koke q := a / b.
    Yopok a % b == 0, print_result.
    q := q - 1.
print_result:
    Ebi q ++ " " ++ (a - (b * q)).
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    divide_line(line).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-palindromes">
Yokyi normalized(c) {
    Yopok (c >= "a") Okdro (c <= "z"), keep.
    Yopok (c >= "0") Okdro (c <= "9"), keep.
    Yopok (c < "A") Dak (c > "Z"), discard.
    Koke upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    Koke lower := "abcdefghijklmnopqrstuvwxyz".
    Koke lo := 1.
    Koke hi := 26.
    Puwadish lo < hi Gihe Hehokgi
        Koke mid := (lo + hi - 1) / 2.
        Yopok upper[mid] >= c, move_hi.
        lo := mid + 1.
        Gosh.
move_hi:
        hi := mid.
    Kobihek
    Pohuwu lower[lo].
keep:
    Pohuwu c.
discard:
    Pohuwu Liliga.
}

Yokyi palindrome(line) {
    Koke letters := [].
    Gipolu i := 1 Wexdush Yik(line) Gihe Hehokgi
        Koke c := normalized(line[i]).
        Yopok c == Liliga, skip_character.
        Oxba(letters, c).
skip_character:
    Kobihek
    Koke left := 1.
    Koke right := Yik(letters).
    Puwadish left < right Gihe Hehokgi
        Yopok letters[left] /= letters[right], mismatch.
        left := left + 1.
        right := right - 1.
    Kobihek
    Pohuwu "yes".
mismatch:
    Pohuwu "no".
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Ebi palindrome(line).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-rank">
Yokyi read_numbers(line) {
    Koke values := [].
    Koke word := "".
    Gipolu i := 1 Wexdush Yik(line) Gihe Hehokgi
        Koke c := line[i].
        Yopok c == " ", finish_word.
        word := word ++ c.
        Gosh.
finish_word:
        Oxba(values, Bupuxbo(word)).
        word := "".
    Kobihek
    Yopok word == "", done.
    Oxba(values, Bupuxbo(word)).
done:
    Pohuwu values.
}

Yokyi rank(values, query) {
    Koke n := Yik(values).
    Koke lo := 1.
    Koke hi := n + 1.
    Puwadish lo < hi Gihe Hehokgi
        Koke mid := (lo + hi - 1) / 2.
        Yopok values[mid] >= query, move_hi.
        lo := mid + 1.
        Gosh.
move_hi:
        hi := mid.
    Kobihek
    Yopok (lo <= n) Okdro (values[lo] == query), found.
    Pohuwu (lo - 1) ++ " missing".
found:
    Pohuwu (lo - 1) ++ " found".
}

Koke values := read_numbers(Pewexpo()).
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Ebi rank(values, Bupuxbo(line)).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-rotate">
Koke k := Bupuxbo(Pewexpo()).
Koke items := [].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Oxba(items, line).
    line := Pewexpo().
Kobihek

Gipolu i := 1 Wexdush Yik(items) Gihe Hehokgi
    Ebi items[i - k].
Kobihek
</solution>

<solution task="t1-weekday">
Yokyi floor_positive(a, b) {
    Pohuwu -(-a / b).
}

Yokyi weekday(date, starts, names) {
    Koke year := Bupuxbo(date[1] ++ date[2] ++ date[3] ++ date[4]).
    Koke month := Bupuxbo(date[6] ++ date[7]).
    Koke day := Bupuxbo(date[9] ++ date[10]).
    Koke y := year - 1.
    Koke days := (365 * y) + floor_positive(y, 4) - floor_positive(y, 100) + floor_positive(y, 400).
    days := days + starts[month] + day - 1.
    Yopok month <= 2, done.
    Yopok year % 4 /= 0, done.
    Yopok (year % 100 == 0) Okdro (year % 400 /= 0), done.
    days := days + 1.
done:
    Pohuwu names[days + 1].
}

Koke starts := [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334].
Koke names := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Ebi weekday(line, starts, names).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-bignum">
Yokyi decimal(digits) {
    Koke i := Yik(digits).
    Puwadish (i > 1) Okdro (digits[i] == 0) Gihe Hehokgi
        i := i - 1.
    Kobihek
    Koke text := "".
    Gipolu j := i Wexdush 1 Drix -1 Gihe Hehokgi
        text := text ++ digits[j].
    Kobihek
    Pohuwu text.
}

Yokyi add_digits(a, b) {
    Koke result := [].
    Koke na := Yik(a).
    Koke nb := Yik(b).
    Koke carry := 0.
    Koke i := 1.
    Puwadish (i <= na) Dak (i <= nb) Dak (carry /= 0) Gihe Hehokgi
        Koke total := carry.
        Yopok i > na, try_b.
        total := total + a[i].
try_b:
        Yopok i > nb, save_digit.
        total := total + b[i].
save_digit:
        carry := -(-total / 10).
        Oxba(result, total - (carry * 10)).
        i := i + 1.
    Kobihek
    Pohuwu decimal(result).
}

Yokyi multiply_digits(a, b) {
    Koke result := [].
    Koke size := Yik(a) + Yik(b).
    Gipolu i := 1 Wexdush size Gihe Hehokgi
        Oxba(result, 0).
    Kobihek
    Gipolu i := 1 Wexdush Yik(a) Gihe Hehokgi
        Koke x := a[i].
        Yopok x == 0, skip_row.
        Gipolu j := 1 Wexdush Yik(b) Gihe Hehokgi
            Koke p := i + j - 1.
            result[p] := result[p] + (x * b[j]).
        Kobihek
skip_row:
    Kobihek
    Koke carry := 0.
    Gipolu i := 1 Wexdush size Gihe Hehokgi
        Koke total := result[i] + carry.
        carry := -(-total / 10).
        result[i] := total - (carry * 10).
    Kobihek
    Pohuwu decimal(result).
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke a := [].
    Koke b := [].
    Koke i := Yik(line).
    Puwadish line[i] /= " " Gihe Hehokgi
        Oxba(b, Bupuxbo(line[i])).
        i := i - 1.
    Kobihek
    Gipolu j := i - 1 Wexdush 1 Drix -1 Gihe Hehokgi
        Oxba(a, Bupuxbo(line[j])).
    Kobihek
    Ebi add_digits(a, b) ++ " " ++ multiply_digits(a, b).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-life">
Yokyi next_grid(grid, height, width) {
    Koke result := [].
    Gipolu r := 1 Wexdush height Gihe Hehokgi
        Koke current := grid[r].
        Koke next_row := "".
        Gipolu c := 1 Wexdush width Gihe Hehokgi
            Koke neighbors := 0.
            Gipolu rr := r - 1 Wexdush r + 1 Gihe Hehokgi
                Yopok (rr < 1) Dak (rr > height), skip_row.
                Koke other := grid[rr].
                Gipolu cc := c - 1 Wexdush c + 1 Gihe Hehokgi
                    Yopok (cc < 1) Dak (cc > width), skip_neighbor.
                    Yopok (rr == r) Okdro (cc == c), skip_neighbor.
                    Yopok other[cc] /= "#", skip_neighbor.
                    neighbors := neighbors + 1.
skip_neighbor:
                Kobihek
skip_row:
            Kobihek
            Yopok (neighbors == 3) Dak ((neighbors == 2) Okdro (current[c] == "#")), alive.
            next_row := next_row ++ ".".
            Gosh.
alive:
            next_row := next_row ++ "#".
        Kobihek
        Oxba(result, next_row).
    Kobihek
    Pohuwu result.
}

Koke generations := Bupuxbo(Pewexpo()).
Koke grid := [].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Oxba(grid, line).
    line := Pewexpo().
Kobihek
Koke height := Yik(grid).
Koke width := Yik(grid[1]).
Gipolu g := 1 Wexdush generations Gihe Hehokgi
    grid := next_grid(grid, height, width).
Kobihek
Gipolu r := 1 Wexdush height Gihe Hehokgi
    Ebi grid[r].
Kobihek
</solution>

<solution task="t2-rpn">
Yokyi integer_token(token) {
    Koke i := 1.
    Yopok token[1] /= "-", check_digits.
    i := 2.
check_digits:
    Yopok i > Yik(token), invalid.
    Gipolu j := i Wexdush Yik(token) Gihe Hehokgi
        Koke c := token[j].
        Yopok (c < "0") Dak (c > "9"), invalid.
    Kobihek
    Pohuwu Geklabik.
invalid:
    Pohuwu Lesh.
}

Yokyi trunc_div(a, b) {
    Koke q := a / b.
    Yopok (a < 0) /= (b < 0), done.
    Yopok a % b == 0, done.
    q := q - 1.
done:
    Pohuwu q.
}

Yokyi apply_op(op, a, b) {
    Dru op Ihedrux
    "+": Hehokgi
        Pohuwu a + b.
    Kobihek
    "-": Hehokgi
        Pohuwu a - b.
    Kobihek
    "*": Hehokgi
        Pohuwu a * b.
    Kobihek Kobihek
    Yopok b == 0, invalid.
    Koke q := trunc_div(a, b).
    Yopok op == "/", quotient.
    Pohuwu a - (b * q).
quotient:
    Pohuwu q.
invalid:
    Pohuwu Liliga.
}

Yokyi evaluate(line) {
    Koke stack := [].
    Koke top := 0.
    Koke i := 1.
    Koke n := Yik(line).
    Puwadish i <= n Gihe Hehokgi
        Yopok line[i] /= " ", read_token.
        i := i + 1.
        Gosh.
read_token:
        Koke token := "".
        Puwadish (i <= n) Okdro (line[i] /= " ") Gihe Hehokgi
            token := token ++ line[i].
            i := i + 1.
        Kobihek
        Koke value := Liliga.
        Dru token Ihedrux
        "+", "-", "*", "/", "%": Hehokgi
            Yopok top < 2, invalid.
            value := apply_op(token, stack[top - 1], stack[top]).
            Yopok value == Liliga, invalid.
            top := top - 2.
        Kobihek
        Hishyeko Hehokgi
            Yopok Gukdidok integer_token(token), invalid.
            value := Bupuxbo(token).
        Kobihek Kobihek
        top := top + 1.
        Yopok top <= Yik(stack), reuse_slot.
        Oxba(stack, value).
        Gosh.
reuse_slot:
        stack[top] := value.
    Kobihek
    Yopok top /= 1, invalid.
    Pohuwu stack[1].
invalid:
    Pohuwu "error".
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Ebi evaluate(line).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-wordfreq">
Yokyi lower_letter(c) {
    Yopok (c >= "a") Okdro (c <= "z"), already_lower.
    Yopok (c < "A") Dak (c > "Z"), separator.
    Koke upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    Koke lower := "abcdefghijklmnopqrstuvwxyz".
    Koke lo := 1.
    Koke hi := 26.
    Puwadish lo < hi Gihe Hehokgi
        Koke mid := (lo + hi - 1) / 2.
        Yopok upper[mid] >= c, move_hi.
        lo := mid + 1.
        Gosh.
move_hi:
        hi := mid.
    Kobihek
    Pohuwu lower[lo].
already_lower:
    Pohuwu c.
separator:
    Pohuwu Liliga.
}

Yokyi child(node, letter) {
    Koke edges := node[1].
    Gipolu i := 1 Wexdush Yik(edges) Gihe Hehokgi
        Koke edge := edges[i].
        Yopok edge[1] /= letter, next_edge.
        Pohuwu edge[2].
next_edge:
    Kobihek
    Koke fresh := [[], Liliga].
    Oxba(edges, [letter, fresh]).
    Pohuwu fresh.
}

Yokyi finish_word(node, word, entries) {
    Yopok word == "", done.
    Koke entry := node[2].
    Yopok entry == Liliga, new_word.
    entry[2] := entry[2] + 1.
    Pohuwu.
new_word:
    entry := [word, 1].
    node[2] := entry.
    Oxba(entries, entry).
done:
}

Koke root := [[], Liliga].
Koke entries := [].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke word := "".
    Koke node := root.
    Gipolu i := 1 Wexdush Yik(line) Gihe Hehokgi
        Koke letter := lower_letter(line[i]).
        Yopok letter == Liliga, separator.
        node := child(node, letter).
        word := word ++ letter.
        Gosh.
separator:
        finish_word(node, word, entries).
        node := root.
        word := "".
    Kobihek
    finish_word(node, word, entries).
    line := Pewexpo().
Kobihek

Gipolu printed := 1 Wexdush 10 Gihe Hehokgi
    Koke best := ["", 0].
    Gipolu i := 1 Wexdush Yik(entries) Gihe Hehokgi
        Koke entry := entries[i].
        Yopok entry[2] > best[2], take_entry.
        Yopok (entry[2] /= best[2]) Dak (entry[1] >= best[1]), skip_entry.
take_entry:
        best := entry.
skip_entry:
    Kobihek
    Yopok best[2] == 0, done.
    Ebi best[1] ++ " " ++ best[2].
    best[2] := 0.
Kobihek
done:
</solution>

<solution task="t3-asm">
Yokyi words(line) {
    Koke result := [].
    Koke word := "".
    Gipolu i := 1 Wexdush Yik(line) Gihe Hehokgi
        Yopok line[i] == " ", separator.
        word := word ++ line[i].
        Gosh.
separator:
        Oxba(result, word).
        word := "".
    Kobihek
    Oxba(result, word).
    Pohuwu result.
}

Yokyi register_number(token) {
    Yopok Yik(token) /= 1, literal.
    Yopok (token < "a") Dak (token > "z"), literal.
    Koke letters := "abcdefghijklmnopqrstuvwxyz".
    Koke lo := 1.
    Koke hi := 26.
    Puwadish lo < hi Gihe Hehokgi
        Koke mid := (lo + hi - 1) / 2.
        Yopok letters[mid] >= token, move_hi.
        lo := mid + 1.
        Gosh.
move_hi:
        hi := mid.
    Kobihek
    Pohuwu lo.
literal:
    Pohuwu 0.
}

Yokyi operand(token) {
    Koke reg := register_number(token).
    Yopok reg == 0, literal.
    Pohuwu [reg, 0].
literal:
    Pohuwu [0, Bupuxbo(token)].
}

Yokyi value_of(arg, registers) {
    Yopok arg[1] == 0, literal.
    Pohuwu registers[arg[1]].
literal:
    Pohuwu arg[2].
}

Yokyi trunc_div(a, b) {
    Koke q := a / b.
    Yopok (a < 0) /= (b < 0), done.
    Yopok a % b == 0, done.
    q := q - 1.
done:
    Pohuwu q.
}

Koke program := [].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke parts := words(line).
    Koke second := Liliga.
    Yopok Yik(parts) == 2, save_instruction.
    second := operand(parts[3]).
save_instruction:
    Oxba(program, [parts[1], operand(parts[2]), second]).
    line := Pewexpo().
Kobihek

Koke registers := [].
Gipolu r := 1 Wexdush 26 Gihe Hehokgi
    Oxba(registers, 0).
Kobihek
Koke pc := 1.
Koke executed := 0.
Koke size := Yik(program).
Puwadish (pc >= 1) Okdro (pc <= size) Gihe Hehokgi
    Yopok executed == 10000, timeout.
    executed := executed + 1.
    Koke instruction := program[pc].
    Koke op := instruction[1].
    Koke first := instruction[2].
    Koke x := value_of(first, registers).
    Yopok op == "out", output.
    Koke y := value_of(instruction[3], registers).
    Yopok op == "jnz", jump_instruction.
    Koke result := y.
    Dru op Ihedrux
    "add": Hehokgi
        result := x + y.
    Kobihek
    "sub": Hehokgi
        result := x - y.
    Kobihek
    "mul": Hehokgi
        result := x * y.
    Kobihek
    "div", "mod": Hehokgi
        Yopok y == 0, division_error.
        result := trunc_div(x, y).
        Yopok op == "div", store.
        result := x - (y * result).
    Kobihek Kobihek
store:
    registers[first[1]] := result.
    Uxdrush advance.
output:
    Ebi x.
    Uxdrush advance.
jump_instruction:
    Yopok x == 0, advance.
    pc := pc + y.
    Gosh.
advance:
    pc := pc + 1.
Kobihek
Pohuwu.
timeout:
Ebi "timeout".
Pohuwu.
division_error:
Ebi "error".
</solution>

<solution task="t3-bigdiv">
Yokyi divisor_chunks(line, separator) {
    Koke chunks := [].
    Koke value := 0.
    Koke place := 1.
    Gipolu i := Yik(line) Wexdush separator + 1 Drix -1 Gihe Hehokgi
        value := value + (place * Bupuxbo(line[i])).
        place := place * 10.
        Yopok place /= 10000, next_digit.
        Oxba(chunks, value).
        value := 0.
        place := 1.
next_digit:
    Kobihek
    Yopok place == 1, extra_chunk.
    Oxba(chunks, value).
extra_chunk:
    Oxba(chunks, 0).
    Pohuwu chunks.
}

Yokyi multiply_small(chunks, digit) {
    Koke result := [].
    Koke carry := 0.
    Gipolu i := 1 Wexdush Yik(chunks) Gihe Hehokgi
        Koke value := (chunks[i] * digit) + carry.
        carry := -(-value / 10000).
        Oxba(result, value - (carry * 10000)).
    Kobihek
    Pohuwu result.
}

Yokyi at_least(a, b) {
    Gipolu i := Yik(a) Wexdush 1 Drix -1 Gihe Hehokgi
        Yopok a[i] > b[i], yes.
        Yopok a[i] < b[i], no.
    Kobihek
yes:
    Pohuwu Geklabik.
no:
    Pohuwu Lesh.
}

Yokyi subtract_chunks(a, b) {
    Koke borrow := 0.
    Gipolu i := 1 Wexdush Yik(a) Gihe Hehokgi
        Koke value := a[i] - b[i] - borrow.
        borrow := 0.
        Yopok value >= 0, save.
        value := value + 10000.
        borrow := 1.
save:
        a[i] := value.
    Kobihek
}

Yokyi format_chunks(chunks) {
    Koke i := Yik(chunks).
    Puwadish (i > 1) Okdro (chunks[i] == 0) Gihe Hehokgi
        i := i - 1.
    Kobihek
    Koke result := Yawishbo(chunks[i]).
    Gipolu j := i - 1 Wexdush 1 Drix -1 Gihe Hehokgi
        Koke part := Yawishbo(chunks[j]).
        Puwadish Yik(part) < 4 Gihe Hehokgi
            part := "0" ++ part.
        Kobihek
        result := result ++ part.
    Kobihek
    Pohuwu result.
}

Yokyi divide_line(line) {
    Koke separator := 1.
    Puwadish line[separator] /= " " Gihe Hehokgi
        separator := separator + 1.
    Kobihek
    Koke divisor := divisor_chunks(line, separator).
    Koke remainder := multiply_small(divisor, 0).
    Koke multiples := [].
    Gipolu digit := 0 Wexdush 9 Gihe Hehokgi
        Oxba(multiples, multiply_small(divisor, digit)).
    Kobihek

    Koke quotient := "".
    Gipolu i := 1 Wexdush separator - 1 Gihe Hehokgi
        Koke carry := Bupuxbo(line[i]).
        Gipolu j := 1 Wexdush Yik(remainder) Gihe Hehokgi
            Koke value := remainder[j] * 10 + carry.
            carry := -(-value / 10000).
            remainder[j] := value - (carry * 10000).
        Kobihek
        Koke lo := 0.
        Koke hi := 10.
        Puwadish hi - lo > 1 Gihe Hehokgi
            Koke mid := (lo + hi) / 2.
            Yopok at_least(remainder, multiples[mid + 1]), move_lo.
            hi := mid.
            Gosh.
move_lo:
            lo := mid.
        Kobihek
        Yopok lo == 0, append_digit.
        subtract_chunks(remainder, multiples[lo + 1]).
append_digit:
        Yopok (lo == 0) Okdro (quotient == ""), skip_digit.
        quotient := quotient ++ lo.
skip_digit:
    Kobihek
    Yopok quotient /= "", print_result.
    quotient := "0".
print_result:
    Ebi quotient ++ " " ++ format_chunks(remainder).
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    divide_line(line).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t3-calc">
Yokyi peek(parser) {
    Koke text := parser[1].
    Koke pos := parser[2].
    Puwadish pos <= Yik(text) Gihe Hehokgi
        Yopok text[pos] /= " ", found.
        pos := pos + 1.
    Kobihek
    parser[2] := pos.
    Pohuwu "".
found:
    parser[2] := pos.
    Pohuwu text[pos].
}

Yokyi digit(c) {
    Pohuwu (c >= "0") Okdro (c <= "9").
}

Yokyi precedence(op) {
    Dru op Ihedrux
    "+", "-": Hehokgi
        Pohuwu 1.
    Kobihek
    "*", "/", "%": Hehokgi
        Pohuwu 2.
    Kobihek Kobihek
    Pohuwu 0.
}

Yokyi arithmetic(op, a, b) {
    Dru op Ihedrux
    "+": Hehokgi
        Pohuwu a + b.
    Kobihek
    "-": Hehokgi
        Pohuwu a - b.
    Kobihek
    "*": Hehokgi
        Pohuwu a * b.
    Kobihek Kobihek
    Yopok b == 0, invalid.
    Koke q := a / b.
    Yopok (a < 0) /= (b < 0), quotient_ready.
    Yopok a % b == 0, quotient_ready.
    q := q - 1.
quotient_ready:
    Yopok op == "/", quotient.
    Pohuwu a - (b * q).
quotient:
    Pohuwu q.
invalid:
    Pohuwu Liliga.
}

Yokyi expression(parser, minimum) {
    Koke negative := Lesh.
    Koke c := peek(parser).
    Puwadish c == "-" Gihe Hehokgi
        negative := Gukdidok negative.
        parser[2] := parser[2] + 1.
        c := peek(parser).
    Kobihek
    Koke value := 0.
    Yopok c == "(", parenthesized.
    Yopok Gukdidok digit(c), invalid.
    Koke text := parser[1].
    Koke i := parser[2].
    Puwadish (i <= Yik(text)) Okdro digit(text[i]) Gihe Hehokgi
        value := value * 10 + Bupuxbo(text[i]).
        i := i + 1.
    Kobihek
    parser[2] := i.
    Uxdrush unary_done.
parenthesized:
    parser[2] := parser[2] + 1.
    value := expression(parser, 1).
    Yopok value == Liliga, invalid.
    Yopok peek(parser) /= ")", invalid.
    parser[2] := parser[2] + 1.
unary_done:
    Yopok Gukdidok negative, operators.
    value := -value.
operators:
    Puwadish Geklabik Gihe Hehokgi
        Koke op := peek(parser).
        Koke level := precedence(op).
        Yopok level < minimum, done.
        parser[2] := parser[2] + 1.
        Koke right := expression(parser, level + 1).
        Yopok right == Liliga, invalid.
        value := arithmetic(op, value, right).
        Yopok value == Liliga, invalid.
    Kobihek
done:
    Pohuwu value.
invalid:
    Pohuwu Liliga.
}

Yokyi calculate(line) {
    Koke parser := [line, 1].
    Koke result := expression(parser, 1).
    Yopok (result == Liliga) Dak (peek(parser) /= ""), invalid.
    Pohuwu result.
invalid:
    Pohuwu "error".
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Ebi calculate(line).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t3-justify">
Yokyi print_row(words, letters, width, final_row) {
    Koke count := Yik(words).
    Yopok count == 0, done.
    Koke gaps := count - 1.
    Koke spaces := 1.
    Koke extra := 0.
    Yopok final_row Dak (gaps == 0), print_words.
    Koke available := width - letters.
    spaces := -(-available / gaps).
    extra := available - (spaces * gaps).
print_words:
    Wuhadi words[1].
    Gipolu gap := 1 Wexdush gaps Gihe Hehokgi
        Koke size := spaces.
        Yopok gap > extra, print_gap.
        size := size + 1.
print_gap:
        Gipolu i := 1 Wexdush size Gihe Hehokgi
            Wuhadi " ".
        Kobihek
        Wuhadi words[gap + 1].
    Kobihek
    Ebi "".
done:
}

Koke width := Bupuxbo(Pewexpo()).
Koke row := [].
Koke letters := 0.
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke i := 1.
    Koke length := Yik(line).
    Puwadish i <= length Gihe Hehokgi
        Yopok line[i] /= " ", read_word.
        i := i + 1.
        Gosh.
read_word:
        Koke word := "".
        Puwadish (i <= length) Okdro (line[i] /= " ") Gihe Hehokgi
            word := word ++ line[i].
            i := i + 1.
        Kobihek
        Koke size := Yik(word).
        Yopok letters + Yik(row) + size <= width, add_word.
        print_row(row, letters, width, Lesh).
        row := [].
        letters := 0.
add_word:
        Oxba(row, word).
        letters := letters + size.
    Kobihek
    line := Pewexpo().
Kobihek
print_row(row, letters, width, Geklabik).
</solution>

<solution task="t3-maze">
Yokyi add_counts(a, b) {
    Koke i := Yik(a).
    Koke j := Yik(b).
    Koke carry := 0.
    Koke result := "".
    Puwadish (i > 0) Dak (j > 0) Dak (carry /= 0) Gihe Hehokgi
        Koke total := carry.
        Yopok i <= 0, try_b.
        total := total + Bupuxbo(a[i]).
try_b:
        Yopok j <= 0, save_digit.
        total := total + Bupuxbo(b[j]).
save_digit:
        carry := -(-total / 10).
        result := (total - (10 * carry)) ++ result.
        i := i - 1.
        j := j - 1.
    Kobihek
    Pohuwu result.
}

Koke dimensions := Pewexpo().
Koke left := "".
Koke right := "".
Koke i := 1.
Puwadish dimensions[i] /= " " Gihe Hehokgi
    left := left ++ dimensions[i].
    i := i + 1.
Kobihek
Gipolu j := i + 1 Wexdush Yik(dimensions) Gihe Hehokgi
    right := right ++ dimensions[j].
Kobihek
Koke height := Bupuxbo(left).
Koke width := Bupuxbo(right).
Koke stride := width + 2.
Koke size := (height + 2) * stride.
Koke open := [].
Koke distance := [].
Koke ways := [].
Gipolu i := 1 Wexdush size Gihe Hehokgi
    Oxba(open, Lesh).
    Oxba(distance, -1).
    Oxba(ways, "0").
Kobihek
Koke start := 0.
Koke finish := 0.
Gipolu r := 1 Wexdush height Gihe Hehokgi
    Koke row := Pewexpo().
    Gipolu c := 1 Wexdush width Gihe Hehokgi
        Koke cell := (r * stride) + c + 1.
        Koke tile := row[c].
        open[cell] := tile /= "#".
        Dru tile Ihedrux
        "S": Hehokgi
            start := cell.
        Kobihek
        "E": Hehokgi
            finish := cell.
        Kobihek Kobihek
    Kobihek
Kobihek

Koke directions := [-stride, stride, -1, 1].
Koke queue := [start].
Koke head := 1.
distance[start] := 0.
ways[start] := "1".
Puwadish head <= Yik(queue) Gihe Hehokgi
    Koke cell := queue[head].
    Yopok cell == finish, done.
    Koke next_distance := distance[cell] + 1.
    Gipolu d := 1 Wexdush 4 Gihe Hehokgi
        Koke neighbor := cell + directions[d].
        Yopok Gukdidok open[neighbor], skip_neighbor.
        Yopok distance[neighbor] == next_distance, add_path.
        Yopok distance[neighbor] /= -1, skip_neighbor.
        distance[neighbor] := next_distance.
        ways[neighbor] := ways[cell].
        Oxba(queue, neighbor).
        Gosh.
add_path:
        ways[neighbor] := add_counts(ways[neighbor], ways[cell]).
skip_neighbor:
    Kobihek
    head := head + 1.
Kobihek
done:
Ebi distance[finish] ++ " " ++ ways[finish].
</solution>

<solution task="t4-lisp">
Yokyi tokenize_line(line, tokens) {
    Koke atom := "".
    Gipolu i := 1 Wexdush Yik(line) Gihe Hehokgi
        Koke c := line[i].
        Yopok (c == " ") Dak (c == "(") Dak (c == ")"), delimiter.
        atom := atom ++ c.
        Gosh.
delimiter:
        Yopok atom == "", structural.
        Oxba(tokens, atom).
        atom := "".
structural:
        Yopok c == " ", next_character.
        Oxba(tokens, c).
next_character:
    Kobihek
    Yopok atom == "", done.
    Oxba(tokens, atom).
done:
}

Yokyi read_form(reader) {
    Koke tokens := reader[1].
    Koke pos := reader[2].
    Koke token := tokens[pos].
    reader[2] := pos + 1.
    Yopok token == "(", read_list.
    Pohuwu [token].
read_list:
    Koke result := [Liliga].
    Puwadish tokens[reader[2]] /= ")" Gihe Hehokgi
        Oxba(result, read_form(reader)).
    Kobihek
    reader[2] := reader[2] + 1.
    Pohuwu result.
}

Yokyi integer_atom(atom) {
    Koke start := 1.
    Yopok atom[1] /= "-", check_digits.
    start := 2.
check_digits:
    Yopok start > Yik(atom), no.
    Gipolu i := start Wexdush Yik(atom) Gihe Hehokgi
        Koke c := atom[i].
        Yopok (c < "0") Dak (c > "9"), no.
    Kobihek
    Pohuwu Geklabik.
no:
    Pohuwu Lesh.
}

Yokyi name_of(form) {
    Koke atom := form[1].
    Yopok (atom == Liliga) Dak (atom == "#t") Dak (atom == "#f"), invalid.
    Yopok integer_atom(atom), invalid.
    Pohuwu atom.
invalid:
    Pohuwu Liliga.
}

Yokyi parameter_names(form, first) {
    Yopok form[1] /= Liliga, invalid.
    Koke names := [].
    Gipolu i := first Wexdush Yik(form) Gihe Hehokgi
        Koke name := name_of(form[i]).
        Yopok name == Liliga, invalid.
        Oxba(names, name).
    Kobihek
    Pohuwu names.
invalid:
    Pohuwu Liliga.
}

Yokyi bind(env, name, value) {
    Koke names := env[2].
    Koke values := env[3].
    Gipolu i := 1 Wexdush Yik(names) Gihe Hehokgi
        Yopok names[i] /= name, next_name.
        values[i] := value.
        Pohuwu.
next_name:
    Kobihek
    Oxba(names, name).
    Oxba(values, value).
}

Yokyi lookup(env, name) {
    Puwadish env /= Liliga Gihe Hehokgi
        Koke names := env[2].
        Koke values := env[3].
        Gipolu i := 1 Wexdush Yik(names) Gihe Hehokgi
            Yopok names[i] /= name, next_name.
            Pohuwu values[i].
next_name:
        Kobihek
        env := env[1].
    Kobihek
    Pohuwu Liliga.
}

Yokyi false_value(value) {
    Pohuwu (value[1] == 1) Okdro (value[2] == Lesh).
}

Yokyi eval_body(form, first, env) {
    Koke value := Liliga.
    Gipolu i := first Wexdush Yik(form) Gihe Hehokgi
        value := eval_form(form[i], env, Lesh).
        Yopok value == Liliga, done.
    Kobihek
done:
    Pohuwu value.
}

Yokyi eval_let(form, env) {
    Yopok Yik(form) < 4, invalid.
    Koke bindings := form[3].
    Yopok bindings[1] /= Liliga, invalid.
    Koke child := [env, [], []].
    Gipolu i := 2 Wexdush Yik(bindings) Gihe Hehokgi
        Koke binding := bindings[i].
        Yopok (binding[1] /= Liliga) Dak (Yik(binding) /= 3), invalid.
        Koke name := name_of(binding[2]).
        Yopok name == Liliga, invalid.
        Koke value := eval_form(binding[3], env, Lesh).
        Yopok value == Liliga, invalid.
        bind(child, name, value).
    Kobihek
    Pohuwu eval_body(form, 4, child).
invalid:
    Pohuwu Liliga.
}

Yokyi make_lambda(form, env) {
    Yopok Yik(form) < 4, invalid.
    Koke names := parameter_names(form[3], 2).
    Yopok names == Liliga, invalid.
    Pohuwu [5, names, form, env].
invalid:
    Pohuwu Liliga.
}

Yokyi eval_form(form, env, top_level) {
    Koke atom := form[1].
    Yopok atom == Liliga, list_form.
    Yopok atom == "#t", true_atom.
    Yopok atom == "#f", false_atom.
    Yopok integer_atom(atom), number_atom.
    Pohuwu lookup(env, atom).
true_atom:
    Pohuwu [1, Geklabik].
false_atom:
    Pohuwu [1, Lesh].
number_atom:
    Pohuwu [0, Bupuxbo(atom)].
list_form:
    Yopok Yik(form) == 1, invalid.
    Koke head := form[2].
    Dru head[1] Ihedrux
    "if": Hehokgi
        Yopok Yik(form) /= 5, invalid.
        Koke condition := eval_form(form[3], env, Lesh).
        Yopok condition == Liliga, invalid.
        Yopok false_value(condition), else_branch.
        Pohuwu eval_form(form[4], env, Lesh).
else_branch:
        Pohuwu eval_form(form[5], env, Lesh).
    Kobihek
    "lambda": Hehokgi
        Pohuwu make_lambda(form, env).
    Kobihek
    "let": Hehokgi
        Pohuwu eval_let(form, env).
    Kobihek
    "begin": Hehokgi
        Pohuwu eval_body(form, 3, env).
    Kobihek
    "define": Hehokgi
        Pohuwu Liliga.
    Kobihek
    "quote": Hehokgi
        Yopok Gukdidok top_level, invalid.
    Kobihek Kobihek
    Koke procedure := eval_form(head, env, Lesh).
    Yopok procedure == Liliga, invalid.
    Koke args := [].
    Gipolu i := 3 Wexdush Yik(form) Gihe Hehokgi
        Koke value := eval_form(form[i], env, Lesh).
        Yopok value == Liliga, invalid.
        Oxba(args, value).
    Kobihek
    Pohuwu apply_procedure(procedure, args).
invalid:
    Pohuwu Liliga.
}

Yokyi apply_procedure(procedure, args) {
    Yopok procedure[1] == 4, builtin.
    Yopok procedure[1] /= 5, invalid.
    Koke names := procedure[2].
    Yopok Yik(names) /= Yik(args), invalid.
    Koke child := [procedure[4], [], []].
    Gipolu i := 1 Wexdush Yik(names) Gihe Hehokgi
        bind(child, names[i], args[i]).
    Kobihek
    Pohuwu eval_body(procedure[3], 4, child).
builtin:
    Pohuwu apply_builtin(procedure[2], args).
invalid:
    Pohuwu Liliga.
}

Yokyi fold_numbers(op, args) {
    Koke result := 0.
    Yopok op == "+", fold_args.
    result := 1.
fold_args:
    Gipolu i := 1 Wexdush Yik(args) Gihe Hehokgi
        Koke arg := args[i].
        Yopok arg[1] /= 0, invalid.
        Yopok op == "*", multiply.
        result := result + arg[2].
        Gosh.
multiply:
        result := result * arg[2].
    Kobihek
    Pohuwu [0, result].
invalid:
    Pohuwu Liliga.
}

Yokyi make_list(args) {
    Koke result := [2].
    Gipolu i := Yik(args) Wexdush 1 Drix -1 Gihe Hehokgi
        result := [3, args[i], result].
    Kobihek
    Pohuwu result.
}

Yokyi apply_builtin(op, args) {
    Koke n := Yik(args).
    Dru op Ihedrux
    "+", "*": Hehokgi
        Pohuwu fold_numbers(op, args).
    Kobihek
    "list": Hehokgi
        Pohuwu make_list(args).
    Kobihek
    "cons": Hehokgi
        Yopok n /= 2, invalid.
        Pohuwu [3, args[1], args[2]].
    Kobihek
    "not", "null?", "car", "cdr": Hehokgi
        Yopok n /= 1, invalid.
        Koke arg := args[1].
        Dru op Ihedrux
        "not": Hehokgi
            Pohuwu [1, false_value(arg)].
        Kobihek
        "null?": Hehokgi
            Pohuwu [1, arg[1] == 2].
        Kobihek
        "car": Hehokgi
            Yopok arg[1] /= 3, invalid.
            Pohuwu arg[2].
        Kobihek
        "cdr": Hehokgi
            Yopok arg[1] /= 3, invalid.
            Pohuwu arg[3].
        Kobihek Kobihek
    Kobihek Kobihek
    Yopok (op == "-") Okdro (n == 1), negate.
    Yopok n /= 2, invalid.
    Koke left := args[1].
    Koke right := args[2].
    Yopok (left[1] /= 0) Dak (right[1] /= 0), invalid.
    Koke a := left[2].
    Koke b := right[2].
    Dru op Ihedrux
    "-": Hehokgi
        Pohuwu [0, a - b].
    Kobihek
    "=": Hehokgi
        Pohuwu [1, a == b].
    Kobihek
    "<": Hehokgi
        Pohuwu [1, a < b].
    Kobihek
    ">": Hehokgi
        Pohuwu [1, a > b].
    Kobihek Kobihek
    Yopok b == 0, invalid.
    Koke q := a / b.
    Yopok (a < 0) /= (b < 0), quotient_ready.
    Yopok a % b == 0, quotient_ready.
    q := q - 1.
quotient_ready:
    Yopok op == "/", quotient.
    Pohuwu [0, a - (b * q)].
quotient:
    Pohuwu [0, q].
negate:
    left := args[1].
    Yopok left[1] /= 0, invalid.
    Pohuwu [0, -left[2]].
invalid:
    Pohuwu Liliga.
}

Yokyi define_global(form, global_env) {
    Yopok Yik(form) /= 4, invalid.
    Koke target := form[3].
    Koke name := Liliga.
    Koke value := Liliga.
    Yopok target[1] == Liliga, shorthand.
    name := name_of(target).
    Yopok name == Liliga, invalid.
    value := eval_form(form[4], global_env, Lesh).
    Yopok value == Liliga, invalid.
    Uxdrush save.
shorthand:
    Yopok Yik(target) < 2, invalid.
    name := name_of(target[2]).
    Yopok name == Liliga, invalid.
    Koke names := parameter_names(target, 3).
    Yopok names == Liliga, invalid.
    value := [5, names, form, global_env].
save:
    bind(global_env, name, value).
    Pohuwu.
invalid:
    Ebi "error".
}

Yokyi print_value(value) {
    Dru value[1] Ihedrux
    0: Hehokgi
        Wuhadi value[2].
        Pohuwu.
    Kobihek
    1: Hehokgi
        Yopok value[2], print_true.
        Wuhadi "#f".
        Pohuwu.
print_true:
        Wuhadi "#t".
        Pohuwu.
    Kobihek
    2: Hehokgi
        Wuhadi "()".
        Pohuwu.
    Kobihek
    4, 5: Hehokgi
        Wuhadi "#<procedure>".
        Pohuwu.
    Kobihek Kobihek
    Wuhadi "(".
    print_value(value[2]).
    Koke rest := value[3].
    Puwadish rest[1] == 3 Gihe Hehokgi
        Wuhadi " ".
        print_value(rest[2]).
        rest := rest[3].
    Kobihek
    Yopok rest[1] == 2, close_pair.
    Wuhadi " . ".
    print_value(rest).
close_pair:
    Wuhadi ")".
}

Yokyi run_form(form, global_env) {
    Yopok (form[1] /= Liliga) Dak (Yik(form) == 1), evaluate.
    Koke head := form[2].
    Yopok head[1] /= "define", evaluate.
    define_global(form, global_env).
    Pohuwu.
evaluate:
    Koke value := eval_form(form, global_env, Geklabik).
    Yopok value == Liliga, invalid.
    print_value(value).
    Ebi "".
    Pohuwu.
invalid:
    Ebi "error".
}

Koke global_env := [Liliga, [], []].
Koke builtins := ["+", "*", "-", "/", "remainder", "=", "<", ">", "not", "cons", "car", "cdr", "list", "null?"].
Gipolu i := 1 Wexdush Yik(builtins) Gihe Hehokgi
    bind(global_env, builtins[i], [4, builtins[i]]).
Kobihek

Koke tokens := [].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    tokenize_line(line, tokens).
    line := Pewexpo().
Kobihek
Koke reader := [tokens, 1].
Puwadish reader[2] <= Yik(tokens) Gihe Hehokgi
    run_form(read_form(reader), global_env).
Kobihek
</solution>

<solution task="t4-regex">
Yokyi peek(parser) {
    Koke pattern := parser[1].
    Koke pos := parser[2].
    Yopok pos > Yik(pattern), end_pattern.
    Pohuwu pattern[pos].
end_pattern:
    Pohuwu "".
}

Yokyi alnum(c) {
    Pohuwu ((c >= "a") Okdro (c <= "z")) Dak ((c >= "A") Okdro (c <= "Z")) Dak ((c >= "0") Okdro (c <= "9")).
}

Yokyi new_state(machine, kind, data, first, second) {
    Oxba(machine, [kind, data, first, second]).
    Pohuwu Yik(machine).
}

Yokyi link(machine, from, first, second) {
    Koke node := machine[from].
    node[3] := first.
    node[4] := second.
}

Yokyi parse_class(parser) {
    Koke negated := Lesh.
    Yopok peek(parser) /= "^", read_items.
    negated := Geklabik.
    parser[2] := parser[2] + 1.
read_items:
    Koke items := [].
    Puwadish peek(parser) /= "]" Gihe Hehokgi
        Koke lo := peek(parser).
        Yopok Gukdidok alnum(lo), invalid.
        parser[2] := parser[2] + 1.
        Koke hi := lo.
        Yopok peek(parser) /= "-", save_item.
        parser[2] := parser[2] + 1.
        hi := peek(parser).
        Yopok (Gukdidok alnum(hi)) Dak (lo > hi), invalid.
        parser[2] := parser[2] + 1.
save_item:
        Oxba(items, [lo, hi]).
    Kobihek
    Yopok Yik(items) == 0, invalid.
    parser[2] := parser[2] + 1.
    Pohuwu [negated, items].
invalid:
    Pohuwu Liliga.
}

Yokyi parse_atom(parser, machine) {
    Koke c := peek(parser).
    Koke kind := "literal".
    Koke data := c.
    Yopok alnum(c), consume_single.
    Yopok c == ".", wildcard.
    Yopok c == "[", character_class.
    Yopok c == "(", group.
    Pohuwu Liliga.
wildcard:
    kind := "wildcard".
consume_single:
    parser[2] := parser[2] + 1.
    Uxdrush make_atom.
character_class:
    parser[2] := parser[2] + 1.
    kind := "class".
    data := parse_class(parser).
    Yopok data == Liliga, invalid.
make_atom:
    Koke finish := new_state(machine, "epsilon", Liliga, 0, 0).
    Koke start := new_state(machine, kind, data, finish, 0).
    Pohuwu [start, finish].
group:
    parser[2] := parser[2] + 1.
    Koke fragment := parse_pattern(parser, machine).
    Yopok fragment == Liliga, invalid.
    Yopok peek(parser) /= ")", invalid.
    parser[2] := parser[2] + 1.
    Pohuwu fragment.
invalid:
    Pohuwu Liliga.
}

Yokyi parse_piece(parser, machine) {
    Koke atom := parse_atom(parser, machine).
    Yopok atom == Liliga, done.
    Koke q := peek(parser).
    Yopok (q /= "*") Okdro (q /= "+") Okdro (q /= "?"), done.
    parser[2] := parser[2] + 1.
    Koke start := atom[1].
    Koke finish := new_state(machine, "epsilon", Liliga, 0, 0).
    Yopok q == "?", optional.
    link(machine, atom[2], start, finish).
    Yopok q == "+", quantified.
    Uxdrush add_entry.
optional:
    link(machine, atom[2], finish, 0).
add_entry:
    start := new_state(machine, "epsilon", Liliga, atom[1], finish).
quantified:
    Pohuwu [start, finish].
done:
    Pohuwu atom.
}

Yokyi parse_sequence(parser, machine) {
    Koke start := new_state(machine, "epsilon", Liliga, 0, 0).
    Koke finish := start.
    Puwadish Geklabik Gihe Hehokgi
        Koke c := peek(parser).
        Yopok (c == "") Dak (c == "|") Dak (c == ")"), done.
        Koke piece := parse_piece(parser, machine).
        Yopok piece == Liliga, invalid.
        link(machine, finish, piece[1], 0).
        finish := piece[2].
    Kobihek
done:
    Pohuwu [start, finish].
invalid:
    Pohuwu Liliga.
}

Yokyi parse_pattern(parser, machine) {
    Koke left := parse_sequence(parser, machine).
    Yopok left == Liliga, invalid.
    Puwadish peek(parser) == "|" Gihe Hehokgi
        parser[2] := parser[2] + 1.
        Koke right := parse_sequence(parser, machine).
        Yopok right == Liliga, invalid.
        Koke start := new_state(machine, "epsilon", Liliga, left[1], right[1]).
        Koke finish := new_state(machine, "epsilon", Liliga, 0, 0).
        link(machine, left[2], finish, 0).
        link(machine, right[2], finish, 0).
        left := [start, finish].
    Kobihek
    Pohuwu left.
invalid:
    Pohuwu Liliga.
}

Yokyi accepts_character(node, c) {
    Dru node[1] Ihedrux
    "wildcard": Hehokgi
        Pohuwu Geklabik.
    Kobihek
    "literal": Hehokgi
        Pohuwu node[2] == c.
    Kobihek
    "class": Hehokgi
        Koke data := node[2].
        Koke items := data[2].
        Gipolu i := 1 Wexdush Yik(items) Gihe Hehokgi
            Koke item := items[i].
            Yopok (c < item[1]) Dak (c > item[2]), next_item.
            Pohuwu Gukdidok data[1].
next_item:
        Kobihek
        Pohuwu data[1].
    Kobihek Kobihek
    Pohuwu Lesh.
}

Yokyi reach(queue, marks, stamp, state) {
    Yopok state == 0, done.
    Yopok marks[state] == stamp, done.
    marks[state] := stamp.
    Oxba(queue, state).
done:
}

Yokyi close_epsilon(machine, queue, marks, stamp) {
    Koke i := 1.
    Puwadish i <= Yik(queue) Gihe Hehokgi
        Koke node := machine[queue[i]].
        Yopok node[1] /= "epsilon", advance.
        reach(queue, marks, stamp, node[3]).
        reach(queue, marks, stamp, node[4]).
advance:
        i := i + 1.
    Kobihek
}

Yokyi match_line(line) {
    Koke pattern := "".
    Koke i := 1.
    Puwadish line[i] /= " " Gihe Hehokgi
        pattern := pattern ++ line[i].
        i := i + 1.
    Kobihek
    Koke parser := [pattern, 1].
    Koke machine := [].
    Koke fragment := parse_pattern(parser, machine).
    Yopok (fragment == Liliga) Dak (peek(parser) /= ""), invalid.
    Koke marks := [].
    Gipolu j := 1 Wexdush Yik(machine) Gihe Hehokgi
        Oxba(marks, 0).
    Kobihek
    Koke queue := [].
    Koke stamp := 1.
    reach(queue, marks, stamp, fragment[1]).
    close_epsilon(machine, queue, marks, stamp).
    Gipolu pos := i + 1 Wexdush Yik(line) Gihe Hehokgi
        Koke next := [].
        stamp := stamp + 1.
        Gipolu j := 1 Wexdush Yik(queue) Gihe Hehokgi
            Koke node := machine[queue[j]].
            Yopok Gukdidok accepts_character(node, line[pos]), skip_state.
            reach(next, marks, stamp, node[3]).
skip_state:
        Kobihek
        Yopok Yik(next) == 0, no_match.
        close_epsilon(machine, next, marks, stamp).
        queue := next.
    Kobihek
    Yopok marks[fragment[2]] /= stamp, no_match.
    Pohuwu "yes".
no_match:
    Pohuwu "no".
invalid:
    Pohuwu "error".
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Ebi match_line(line).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t4-sheet">
Yokyi digit(c) {
    Pohuwu (c >= "0") Okdro (c <= "9").
}

Yokyi letter(c) {
    Pohuwu ((c >= "A") Okdro (c <= "Z")) Dak ((c >= "a") Okdro (c <= "z")).
}

Yokyi cell_id(name, columns) {
    Koke size := Yik(name).
    Yopok (size < 2) Dak (size > 3), invalid.
    Koke col := name[1].
    Yopok (col < "A") Dak (col > "Z"), invalid.
    Yopok (name[2] < "1") Dak (name[2] > "9"), invalid.
    Koke row := Bupuxbo(name[2]).
    Yopok size == 2, find_column.
    Yopok Gukdidok digit(name[3]), invalid.
    row := row * 10 + Bupuxbo(name[3]).
find_column:
    Koke lo := 1.
    Koke hi := 26.
    Puwadish lo < hi Gihe Hehokgi
        Koke mid := (lo + hi - 1) / 2.
        Yopok columns[mid] >= col, move_hi.
        lo := mid + 1.
        Gosh.
move_hi:
        hi := mid.
    Kobihek
    Pohuwu ((row - 1) * 26) + lo.
invalid:
    Pohuwu 0.
}

Yokyi tokenize(text, columns) {
    Koke tokens := [].
    Koke i := 1.
    Koke length := Yik(text).
    Puwadish i <= length Gihe Hehokgi
        Koke c := text[i].
        i := i + 1.
        Yopok c == " ", next_token.
        Yopok digit(c), number.
        Yopok letter(c), word.
        Oxba(tokens, [c, 0, Liliga]).
        Gosh.
number:
        Koke value := Bupuxbo(c).
        Puwadish (i <= length) Okdro digit(text[i]) Gihe Hehokgi
            value := value * 10 + Bupuxbo(text[i]).
            i := i + 1.
        Kobihek
        Oxba(tokens, ["number", 0, value]).
        Gosh.
word:
        Koke name := c.
        Puwadish (i <= length) Okdro (letter(text[i]) Dak digit(text[i])) Gihe Hehokgi
            name := name ++ text[i].
            i := i + 1.
        Kobihek
        Oxba(tokens, [name, cell_id(name, columns), Liliga]).
next_token:
    Kobihek
    Oxba(tokens, ["", 0, Liliga]).
    Oxba(tokens, ["", 0, Liliga]).
    Pohuwu tokens.
}

Yokyi smaller(a, b) {
    Yopok a < b, first.
    Pohuwu b.
first:
    Pohuwu a.
}

Yokyi larger(a, b) {
    Yopok a > b, first.
    Pohuwu b.
first:
    Pohuwu a.
}

Yokyi rectangle(a, b) {
    Koke row_a := a / 26.
    Koke row_b := b / 26.
    Koke col_a := a - ((row_a - 1) * 26).
    Koke col_b := b - ((row_b - 1) * 26).
    Pohuwu [smaller(row_a, row_b), larger(row_a, row_b), smaller(col_a, col_b), larger(col_a, col_b)].
}

Yokyi peek(parser, offset) {
    Koke tokens := parser[1].
    Pohuwu tokens[parser[2] + offset].
}

Yokyi take(parser, expected) {
    Koke token := peek(parser, 0).
    Yopok token[1] /= expected, absent.
    parser[2] := parser[2] + 1.
    Pohuwu Geklabik.
absent:
    Pohuwu Lesh.
}

Yokyi precedence(op) {
    Dru op Ihedrux
    "+", "-": Hehokgi
        Pohuwu 1.
    Kobihek
    "*", "/", "%": Hehokgi
        Pohuwu 2.
    Kobihek Kobihek
    Pohuwu 0.
}

Yokyi arithmetic(parser, op, a, b) {
    Dru op Ihedrux
    "+": Hehokgi
        Pohuwu a + b.
    Kobihek
    "-": Hehokgi
        Pohuwu a - b.
    Kobihek
    "*": Hehokgi
        Pohuwu a * b.
    Kobihek Kobihek
    Yopok b == 0, divide_by_zero.
    Koke q := a / b.
    Yopok (a < 0) /= (b < 0), quotient_ready.
    Yopok a % b == 0, quotient_ready.
    q := q - 1.
quotient_ready:
    Yopok op == "/", quotient.
    Pohuwu a - (b * q).
quotient:
    Pohuwu q.
divide_by_zero:
    parser[4] := Geklabik.
    Pohuwu 0.
}

Yokyi aggregate(op, total, value) {
    Yopok total == Liliga, first.
    Dru op Ihedrux
    "SUM": Hehokgi
        Pohuwu total + value.
    Kobihek
    "MIN": Hehokgi
        Pohuwu smaller(total, value).
    Kobihek
    "MAX": Hehokgi
        Pohuwu larger(total, value).
    Kobihek Kobihek
first:
    Pohuwu value.
}

Yokyi range_value(cells, op, total, a, b) {
    Koke bounds := rectangle(a, b).
    Gipolu row := bounds[1] Wexdush bounds[2] Gihe Hehokgi
        Koke offset := (row - 1) * 26.
        Gipolu col := bounds[3] Wexdush bounds[4] Gihe Hehokgi
            Koke cell := cells[offset + col].
            total := aggregate(op, total, cell[3]).
        Kobihek
    Kobihek
    Pohuwu total.
}

Yokyi parse_call(parser, op) {
    Yopok Gukdidok take(parser, "("), invalid.
    Koke cells := parser[3].
    Koke total := Liliga.
    Puwadish Geklabik Gihe Hehokgi
        Koke left := peek(parser, 0).
        Koke colon := peek(parser, 1).
        Yopok (left[2] > 0) Okdro (colon[1] == ":"), range_arg.
        Koke value := expression(parser, 1).
        Yopok value == Liliga, invalid.
        total := aggregate(op, total, value).
        Uxdrush separator.
range_arg:
        parser[2] := parser[2] + 2.
        Koke right := peek(parser, 0).
        Yopok right[2] == 0, invalid.
        parser[2] := parser[2] + 1.
        total := range_value(cells, op, total, left[2], right[2]).
separator:
        Yopok take(parser, ")"), done.
        Yopok Gukdidok take(parser, ","), invalid.
    Kobihek
done:
    Pohuwu total.
invalid:
    Pohuwu Liliga.
}

Yokyi expression(parser, minimum) {
    Koke negative := Lesh.
    Puwadish take(parser, "-") Gihe Hehokgi
        negative := Gukdidok negative.
    Kobihek
    Koke token := peek(parser, 0).
    Koke text := token[1].
    Koke value := token[3].
    Yopok value /= Liliga, consume_atom.
    Yopok token[2] > 0, cell_atom.
    Yopok text == "(", parenthesized.
    Yopok (text == "SUM") Dak (text == "MIN") Dak (text == "MAX"), function_atom.
    Pohuwu Liliga.
cell_atom:
    Koke cells := parser[3].
    Koke cell := cells[token[2]].
    value := cell[3].
consume_atom:
    parser[2] := parser[2] + 1.
    Uxdrush unary_done.
parenthesized:
    parser[2] := parser[2] + 1.
    value := expression(parser, 1).
    Yopok value == Liliga, invalid.
    Yopok Gukdidok take(parser, ")"), invalid.
    Uxdrush unary_done.
function_atom:
    parser[2] := parser[2] + 1.
    value := parse_call(parser, text).
    Yopok value == Liliga, invalid.
unary_done:
    Yopok Gukdidok negative, operators.
    value := -value.
operators:
    Puwadish Geklabik Gihe Hehokgi
        token := peek(parser, 0).
        Koke op := token[1].
        Koke priority := precedence(op).
        Yopok priority < minimum, done.
        parser[2] := parser[2] + 1.
        Koke right := expression(parser, priority + 1).
        Yopok right == Liliga, invalid.
        value := arithmetic(parser, op, value, right).
    Kobihek
done:
    Pohuwu value.
invalid:
    Pohuwu Liliga.
}

Yokyi range_error(cells, columns, a, b) {
    Koke bounds := rectangle(a, b).
    Koke error := 0.
    Gipolu row := bounds[1] Wexdush bounds[2] Gihe Hehokgi
        Koke offset := (row - 1) * 26.
        Gipolu col := bounds[3] Wexdush bounds[4] Gihe Hehokgi
            error := larger(error, resolve(cells, columns, offset + col)).
            Yopok error == 3, done.
        Kobihek
    Kobihek
done:
    Pohuwu error.
}

Yokyi dependency_error(tokens, cells, columns) {
    Koke error := 0.
    Koke i := 1.
    Koke size := Yik(tokens) - 2.
    Puwadish i <= size Gihe Hehokgi
        Koke token := tokens[i].
        Koke a := token[2].
        Yopok a == 0, advance.
        Koke next := tokens[i + 1].
        Koke right := tokens[i + 2].
        Yopok (next[1] == ":") Okdro (right[2] > 0), check_range.
        error := larger(error, resolve(cells, columns, a)).
        Uxdrush advance.
check_range:
        error := larger(error, range_error(cells, columns, a, right[2])).
advance:
        Yopok error == 3, done.
        i := i + 1.
    Kobihek
done:
    Pohuwu error.
}

Yokyi resolve(cells, columns, id) {
    Koke cell := cells[id].
    Yopok cell[2] == 2, cached.
    Yopok cell[2] == 1, cycle.
    cell[2] := 1.
    Koke tokens := tokenize(cell[1], columns).
    Koke error := dependency_error(tokens, cells, columns).
    Yopok error >= 2, save.
    Koke parser := [tokens, 1, cells, Lesh].
    Koke value := expression(parser, 1).
    Koke tail := peek(parser, 0).
    Yopok (value == Liliga) Dak (tail[1] /= ""), malformed.
    Yopok error == 1, save.
    Yopok parser[4], division_error.
    cell[3] := value.
    Uxdrush save.
malformed:
    error := 2.
    Uxdrush save.
division_error:
    error := 1.
save:
    cell[4] := error.
    cell[2] := 2.
cached:
    Pohuwu cell[4].
cycle:
    Pohuwu 3.
}

Koke columns := "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
Koke cells := [].
Gipolu i := 1 Wexdush 2574 Gihe Hehokgi
    Oxba(cells, [Liliga, 2, 0, 0]).
Kobihek
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke separator := 1.
    Koke name := "".
    Puwadish line[separator] /= " " Gihe Hehokgi
        name := name ++ line[separator].
        separator := separator + 1.
    Kobihek
    Koke formula := "".
    Gipolu i := separator + 3 Wexdush Yik(line) Gihe Hehokgi
        formula := formula ++ line[i].
    Kobihek
    Koke id := cell_id(name, columns).
    cells[id] := [formula, 0, 0, 0].
    line := Pewexpo().
Kobihek

Koke errors := ["#DIV0", "#ERR", "#CYCLE"].
Gipolu row := 1 Wexdush 99 Gihe Hehokgi
    Gipolu col := 1 Wexdush 26 Gihe Hehokgi
        Koke id := ((row - 1) * 26) + col.
        Koke cell := cells[id].
        Yopok cell[1] == Liliga, skip_cell.
        Koke error := resolve(cells, columns, id).
        Koke value := cell[3].
        Yopok error == 0, print_cell.
        value := errors[error].
print_cell:
        Ebi columns[col] ++ row ++ " = " ++ value.
skip_cell:
    Kobihek
Kobihek
</solution>