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
    Yopok (n < 1) Dak (n > 7), invalid.
    Ebi days[n].
    Uxdrush next_line.
invalid:
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
    Koke n := Bupuxbo(line).
    Yopok (n % 2) /= 0, odd_number.
    even := even + 1.
    Uxdrush next_line.
odd_number:
    odd := odd + 1.
next_line:
    line := Pewexpo().
Kobihek
Ebi "even " ++ even.
Ebi "odd " ++ odd.
</solution>

<solution task="t0-factorial">
Koke n := Bupuxbo(Pewexpo()).
Koke result := 1.
Gipolu i := 2 Wexdush n Gihe Hehokgi
    result := result * i.
Kobihek
Ebi result.
</solution>

<solution task="t0-fizzbuzz">
Koke n := Bupuxbo(Pewexpo()).
Gipolu i := 1 Wexdush n Gihe Hehokgi
    Yopok (i % 15) == 0, fizzbuzz.
    Yopok (i % 3) == 0, fizz.
    Yopok (i % 5) == 0, buzz.
    Ebi i.
    Gosh.
fizzbuzz:
    Ebi "FizzBuzz".
    Gosh.
fizz:
    Ebi "Fizz".
    Gosh.
buzz:
    Ebi "Buzz".
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
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke n := Bupuxbo(line).
    Koke negative := n < 0.
    Yopok Gukdidok negative, magnitude_ready.
    n := -n.
magnitude_ready:
    Koke sum := 0.
    Koke reversed := 0.
    Puwadish n > 0 Gihe Hehokgi
        Koke digit := -((-n) % 10).
        sum := sum + digit.
        reversed := (reversed * 10) + digit.
        n := -((-n) / 10).
    Kobihek
    Yopok Gukdidok negative, print_result.
    reversed := -reversed.
print_result:
    Ebi sum ++ " " ++ reversed.
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-floordiv">
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke first := "".
    Koke second := "".
    Koke past_space := Lesh.
    Gipolu i := 1 Wexdush Yik(line) Gihe Hehokgi
        Koke ch := line[i].
        Yopok ch == " ", separator.
        Yopok past_space, second_digit.
        first := first ++ ch.
        Gosh.
second_digit:
        second := second ++ ch.
        Gosh.
separator:
        past_space := Geklabik.
    Kobihek
    Koke a := Bupuxbo(first).
    Koke b := Bupuxbo(second).
    Koke q := a / b.
    Yopok (a % b) == 0, print_result.
    q := q - 1.
print_result:
    Ebi q ++ " " ++ (a - (b * q)).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-palindromes">
Yokyi folded(ch) {
    Yopok (ch >= "0") Okdro (ch <= "9"), unchanged.
    Yopok (ch >= "a") Okdro (ch <= "z"), unchanged.
    Yopok (ch < "A") Dak (ch > "Z"), ignored.
    Koke upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    Koke lower := "abcdefghijklmnopqrstuvwxyz".
    Koke lo := 1.
    Koke hi := 26.
    Puwadish lo <= hi Gihe Hehokgi
        Koke mid := (lo + hi) / 2.
        Yopok ch == upper[mid], matched.
        Yopok ch < upper[mid], search_left.
        lo := mid + 1.
        Gosh.
search_left:
        hi := mid - 1.
        Gosh.
matched:
        Pohuwu lower[mid].
    Kobihek
ignored:
    Pohuwu Liliga.
unchanged:
    Pohuwu ch.
}

Yokyi palindrome(line) {
    Koke left := 1.
    Koke right := Yik(line).
    Puwadish left < right Gihe Hehokgi
        Koke a := folded(line[left]).
        Yopok a == Liliga, skip_left.
        Koke b := folded(line[right]).
        Yopok b == Liliga, skip_right.
        Yopok a /= b, mismatch.
        left := left + 1.
        right := right - 1.
        Gosh.
skip_left:
        left := left + 1.
        Gosh.
skip_right:
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
Koke values := [].
Koke first := Pewexpo().
Koke token := "".
Gipolu i := 1 Wexdush Yik(first) Gihe Hehokgi
    Koke ch := first[i].
    Yopok ch == " ", end_token.
    token := token ++ ch.
    Gosh.
end_token:
    Oxba(values, Bupuxbo(token)).
    token := "".
Kobihek
Yopok token == "", read_queries.
Oxba(values, Bupuxbo(token)).
read_queries:
Koke size := Yik(values).
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke query := Bupuxbo(line).
    Koke lo := 1.
    Koke hi := size + 1.
    Puwadish lo < hi Gihe Hehokgi
        Koke mid := hi - ((hi - lo) / 2).
        Yopok values[mid] < query, search_right.
        hi := mid.
        Gosh.
search_right:
        lo := mid + 1.
    Kobihek
    Yopok (lo <= size) Okdro (values[lo] == query), found.
    Ebi (lo - 1) ++ " missing".
    Uxdrush next_query.
found:
    Ebi (lo - 1) ++ " found".
next_query:
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
Koke days := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
Koke month_offsets := [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke year := Bupuxbo(line[1] ++ line[2] ++ line[3] ++ line[4]).
    Koke month := Bupuxbo(line[6] ++ line[7]).
    Koke day := Bupuxbo(line[9] ++ line[10]).
    Koke earlier := year - 1.
    Koke leap_days := -((-earlier) / 4) + ((-earlier) / 100) - ((-earlier) / 400).
    Koke offset := (365 * earlier) + leap_days + month_offsets[month] + day - 1.
    Yopok month <= 2, print_day.
    Yopok (year % 4) /= 0, print_day.
    Yopok ((year % 100) == 0) Okdro ((year % 400) /= 0), print_day.
    offset := offset + 1.
print_day:
    Ebi days[1 - ((-offset) % 7)].
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-bignum">
Yokyi blocks(line, first, last) {
    Koke result := [].
    Puwadish last >= first Gihe Hehokgi
        Koke start := last - 7.
        Yopok start >= first, read_block.
        start := first.
read_block:
        Koke text := "".
        Gipolu i := start Wexdush last Gihe Hehokgi
            text := text ++ line[i].
        Kobihek
        Oxba(result, Bupuxbo(text)).
        last := start - 1.
    Kobihek
    Pohuwu result.
}

Yokyi decimal(parts) {
    Koke base := 100000000.
    Koke last := Yik(parts).
    Gipolu i := 1 Wexdush last - 1 Gihe Hehokgi
        Koke carry := -((-parts[i]) / base).
        parts[i] := parts[i] - (carry * base).
        parts[i + 1] := parts[i + 1] + carry.
    Kobihek
    Puwadish (last > 1) Okdro (parts[last] == 0) Gihe Hehokgi
        last := last - 1.
    Kobihek
    Koke result := Yawishbo(parts[last]).
    Gipolu i := last - 1 Wexdush 1 Drix -1 Gihe Hehokgi
        Koke text := Yawishbo(parts[i]).
        Gipolu pad := Yik(text) Wexdush 7 Gihe Hehokgi
            result := result ++ "0".
        Kobihek
        result := result ++ text.
    Kobihek
    Pohuwu result.
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke space := 1.
    Puwadish line[space] /= " " Gihe Hehokgi
        space := space + 1.
    Kobihek
    Koke a := blocks(line, 1, space - 1).
    Koke b := blocks(line, space + 1, Yik(line)).
    Koke sum := [].
    Koke product := [].
    Gipolu i := 1 Wexdush Yik(a) + Yik(b) Gihe Hehokgi
        Oxba(sum, 0).
        Oxba(product, 0).
    Kobihek
    Gipolu i := 1 Wexdush Yik(a) Gihe Hehokgi
        sum[i] := a[i].
        Gipolu j := 1 Wexdush Yik(b) Gihe Hehokgi
            Koke place := i + j - 1.
            product[place] := product[place] + (a[i] * b[j]).
        Kobihek
    Kobihek
    Gipolu j := 1 Wexdush Yik(b) Gihe Hehokgi
        sum[j] := sum[j] + b[j].
    Kobihek
    Koke sum_text := decimal(sum).
    Koke product_text := decimal(product).
    Ebi sum_text ++ " " ++ product_text.
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-life">
Koke generations := Bupuxbo(Pewexpo()).
Koke grid := [].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Oxba(grid, line).
    line := Pewexpo().
Kobihek
Koke height := Yik(grid).
Koke width := Yik(grid[1]).
Gipolu generation := 1 Wexdush generations Gihe Hehokgi
    Koke next_grid := [].
    Gipolu r := 1 Wexdush height Gihe Hehokgi
        Koke old_row := grid[r].
        Koke next_row := "".
        Gipolu c := 1 Wexdush width Gihe Hehokgi
            Koke nearby := 0.
            Gipolu rr := r - 1 Wexdush r + 1 Gihe Hehokgi
                Yopok (rr < 1) Dak (rr > height), skip_row.
                Koke neighbor_row := grid[rr].
                Gipolu cc := c - 1 Wexdush c + 1 Gihe Hehokgi
                    Yopok (cc < 1) Dak (cc > width), skip_cell.
                    Yopok (rr == r) Okdro (cc == c), skip_cell.
                    Yopok neighbor_row[cc] /= "#", skip_cell.
                    nearby := nearby + 1.
skip_cell:
                    Gosh.
                Kobihek
skip_row:
                Gosh.
            Kobihek
            Yopok (nearby == 3) Dak ((nearby == 2) Okdro (old_row[c] == "#")), live.
            next_row := next_row ++ ".".
            Gosh.
live:
            next_row := next_row ++ "#".
        Kobihek
        Oxba(next_grid, next_row).
    Kobihek
    grid := next_grid.
Kobihek
Gipolu r := 1 Wexdush height Gihe Hehokgi
    Ebi grid[r].
Kobihek
</solution>

<solution task="t2-rpn">
Yokyi is_operator(token) {
    Dru token Ihedrux
    "+", "-", "*", "/", "%": Hehokgi
        Pohuwu Geklabik.
    Kobihek Kobihek
    Pohuwu Lesh.
}

Yokyi apply(op, a, b) {
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
    Yopok b == 0, zero_divisor.
    Koke q := a / b.
    Yopok (a < 0) /= (b < 0), quotient_ready.
    Yopok (a % b) == 0, quotient_ready.
    q := q - 1.
quotient_ready:
    Yopok op == "%", remainder.
    Pohuwu q.
remainder:
    Pohuwu a - (b * q).
zero_divisor:
    Pohuwu Liliga.
}

Yokyi evaluate(line) {
    Koke stack := [].
    Koke size := 0.
    Koke token := "".
    Koke length := Yik(line).
    Gipolu i := 1 Wexdush length + 1 Gihe Hehokgi
        Koke ch := " ".
        Yopok i > length, end_token.
        ch := line[i].
        Yopok ch == " ", end_token.
        token := token ++ ch.
        Gosh.
end_token:
        Yopok token == "", next_character.
        Yopok is_operator(token), reduce_stack.
        Koke start := 1.
        Yopok token[1] /= "-", validate.
        start := 2.
validate:
        Gipolu j := start Wexdush Yik(token) Gihe Hehokgi
            Koke digit := token[j].
            Yopok (digit < "0") Dak (digit > "9"), invalid.
        Kobihek
        Koke value := Bupuxbo(token).
        size := size + 1.
        Yopok size > Yik(stack), append_value.
        stack[size] := value.
        Uxdrush clear_token.
append_value:
        Oxba(stack, value).
        Uxdrush clear_token.
reduce_stack:
        Yopok size < 2, invalid.
        Koke result := apply(token, stack[size - 1], stack[size]).
        Yopok result == Liliga, invalid.
        size := size - 1.
        stack[size] := result.
clear_token:
        token := "".
next_character:
        Gosh.
    Kobihek
    Yopok size /= 1, invalid.
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
Yokyi new_node() {
    Pohuwu [0, [
        Liliga, Liliga, Liliga, Liliga, Liliga, Liliga, Liliga,
        Liliga, Liliga, Liliga, Liliga, Liliga, Liliga,
        Liliga, Liliga, Liliga, Liliga, Liliga, Liliga,
        Liliga, Liliga, Liliga, Liliga, Liliga, Liliga, Liliga
    ]].
}

Yokyi letter_index(ch, letters) {
    Yopok (ch < "A") Dak (ch > "z"), absent.
    Koke lo := 1.
    Koke hi := 52.
    Puwadish lo <= hi Gihe Hehokgi
        Koke mid := (lo + hi) / 2.
        Yopok ch == letters[mid], found.
        Yopok ch < letters[mid], search_left.
        lo := mid + 1.
        Gosh.
search_left:
        hi := mid - 1.
        Gosh.
found:
        Yopok mid <= 26, uppercase.
        Pohuwu mid - 26.
uppercase:
        Pohuwu mid.
    Kobihek
absent:
    Pohuwu 0.
}

Koke root := new_node().
Koke entries := [].
Koke letters := "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".
Koke lower := "abcdefghijklmnopqrstuvwxyz".
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke node := root.
    Koke word := "".
    Koke length := Yik(line).
    Gipolu i := 1 Wexdush length + 1 Gihe Hehokgi
        Yopok i > length, end_word.
        Koke index := letter_index(line[i], letters).
        Yopok index == 0, end_word.
        Koke children := node[2].
        Yopok children[index] /= Liliga, descend.
        children[index] := new_node().
descend:
        node := children[index].
        word := word ++ lower[index].
        Gosh.
end_word:
        Yopok word == "", next_character.
        Koke entry_index := node[1].
        Yopok entry_index /= 0, increment.
        Oxba(entries, [word, 1]).
        node[1] := Yik(entries).
        Uxdrush reset_word.
increment:
        Koke entry := entries[entry_index].
        entry[2] := entry[2] + 1.
reset_word:
        node := root.
        word := "".
next_character:
        Gosh.
    Kobihek
    line := Pewexpo().
Kobihek

Gipolu place := 1 Wexdush 10 Gihe Hehokgi
    Koke best_index := 0.
    Koke best_count := 0.
    Koke best_word := "".
    Gipolu i := 1 Wexdush Yik(entries) Gihe Hehokgi
        Koke entry := entries[i].
        Koke count := entry[2].
        Yopok count == 0, skip_entry.
        Yopok count > best_count, take_entry.
        Yopok (count /= best_count) Dak (entry[1] >= best_word), skip_entry.
take_entry:
        best_index := i.
        best_count := count.
        best_word := entry[1].
skip_entry:
        Gosh.
    Kobihek
    Yopok best_index == 0, done.
    Ebi best_word ++ " " ++ best_count.
    Koke selected := entries[best_index].
    selected[2] := 0.
Kobihek
done:
Pohuwu.
</solution>

<solution task="t3-asm">
Yokyi split(line) {
    Koke parts := [].
    Koke token := "".
    Gipolu i := 1 Wexdush Yik(line) Gihe Hehokgi
        Yopok line[i] == " ", separator.
        token := token ++ line[i].
        Gosh.
separator:
        Oxba(parts, token).
        token := "".
    Kobihek
    Oxba(parts, token).
    Pohuwu parts.
}

Yokyi decode(token) {
    Yopok Yik(token) /= 1, literal.
    Yopok (token < "a") Dak (token > "z"), literal.
    Koke letters := "abcdefghijklmnopqrstuvwxyz".
    Gipolu i := 1 Wexdush 26 Gihe Hehokgi
        Yopok token /= letters[i], next_letter.
        Pohuwu [i, 0].
next_letter:
        Gosh.
    Kobihek
literal:
    Pohuwu [0, Bupuxbo(token)].
}

Yokyi value(registers, operand) {
    Koke index := operand[1].
    Yopok index == 0, literal.
    Pohuwu registers[index].
literal:
    Pohuwu operand[2].
}

Yokyi quotient(a, b) {
    Koke q := a / b.
    Yopok (a < 0) /= (b < 0), ready.
    Yopok (a % b) == 0, ready.
    q := q - 1.
ready:
    Pohuwu q.
}

Koke program := [].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke parts := split(line).
    Koke op := parts[1].
    Koke x := decode(parts[2]).
    Koke y := Liliga.
    Yopok op == "out", store_instruction.
    y := decode(parts[3]).
store_instruction:
    Oxba(program, [op, x, y]).
    line := Pewexpo().
Kobihek

Koke registers := [].
Gipolu i := 1 Wexdush 26 Gihe Hehokgi
    Oxba(registers, 0).
Kobihek
Koke pc := 0.
Koke executed := 0.
Koke limit := Yik(program).
Puwadish (pc >= 0) Okdro (pc < limit) Gihe Hehokgi
    Yopok executed == 10000, timeout.
    executed := executed + 1.
    Koke instruction := program[pc + 1].
    Koke op := instruction[1].
    Koke x := instruction[2].
    Koke y := instruction[3].
    Koke next_pc := pc + 1.
    Yopok op == "out", output.
    Yopok op == "jnz", jump.
    Koke index := x[1].
    Koke a := registers[index].
    Koke b := value(registers, y).
    Dru op Ihedrux
    "set": Hehokgi
        registers[index] := b.
    Kobihek
    "add": Hehokgi
        registers[index] := a + b.
    Kobihek
    "sub": Hehokgi
        registers[index] := a - b.
    Kobihek
    "mul": Hehokgi
        registers[index] := a * b.
    Kobihek
    "div": Hehokgi
        Yopok b == 0, divide_error.
        registers[index] := quotient(a, b).
    Kobihek
    "mod": Hehokgi
        Yopok b == 0, divide_error.
        registers[index] := a - (b * quotient(a, b)).
    Kobihek Kobihek
    Uxdrush advance.
output:
    Ebi value(registers, x).
    Uxdrush advance.
jump:
    Yopok value(registers, x) == 0, advance.
    next_pc := pc + value(registers, y).
advance:
    pc := next_pc.
Kobihek
Pohuwu.
timeout:
Ebi "timeout".
Pohuwu.
divide_error:
Ebi "error".
</solution>

<solution task="t3-bigdiv">
Yokyi at_least(a, b) {
    Yopok Yik(a) == Yik(b), same_length.
    Pohuwu Yik(a) > Yik(b).
same_length:
    Pohuwu a >= b.
}

Yokyi subtract(a, b) {
    Koke borrow := 0.
    Koke j := Yik(b).
    Koke digits := [].
    Koke last_nonzero := 0.
    Gipolu i := Yik(a) Wexdush 1 Drix -1 Gihe Hehokgi
        Koke digit := Bupuxbo(a[i]) - borrow.
        Yopok j < 1, set_borrow.
        digit := digit - Bupuxbo(b[j]).
        j := j - 1.
set_borrow:
        borrow := 0.
        Yopok digit >= 0, save_digit.
        digit := digit + 10.
        borrow := 1.
save_digit:
        Oxba(digits, digit).
        Yopok digit == 0, next_digit.
        last_nonzero := Yik(digits).
next_digit:
        Gosh.
    Kobihek
    Yopok last_nonzero == 0, zero.
    Koke result := "".
    Gipolu i := last_nonzero Wexdush 1 Drix -1 Gihe Hehokgi
        result := result ++ digits[i].
    Kobihek
    Pohuwu result.
zero:
    Pohuwu "0".
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke a := "".
    Koke b := "".
    Koke past_space := Lesh.
    Gipolu i := 1 Wexdush Yik(line) Gihe Hehokgi
        Koke ch := line[i].
        Yopok ch == " ", separator.
        Yopok past_space, divisor_digit.
        a := a ++ ch.
        Gosh.
divisor_digit:
        b := b ++ ch.
        Gosh.
separator:
        past_space := Geklabik.
    Kobihek
    Koke remainder := "0".
    Koke quotient := "".
    Gipolu i := 1 Wexdush Yik(a) Gihe Hehokgi
        Yopok remainder /= "0", append_digit.
        remainder := a[i].
        Uxdrush count_digit.
append_digit:
        remainder := remainder ++ a[i].
count_digit:
        Koke digit := 0.
        Puwadish at_least(remainder, b) Gihe Hehokgi
            remainder := subtract(remainder, b).
            digit := digit + 1.
        Kobihek
        Yopok (quotient == "") Okdro (digit == 0), skip_digit.
        quotient := quotient ++ digit.
skip_digit:
        Gosh.
    Kobihek
    Yopok quotient /= "", print_result.
    quotient := "0".
print_result:
    Ebi quotient ++ " " ++ remainder.
    line := Pewexpo().
Kobihek
</solution>

<solution task="t3-calc">
Yokyi precedence(op) {
    Dru op Ihedrux
    "+", "-": Hehokgi
        Pohuwu 1.
    Kobihek
    "*", "/", "%": Hehokgi
        Pohuwu 2.
    Kobihek
    "~": Hehokgi
        Pohuwu 3.
    Kobihek Kobihek
    Pohuwu 0.
}

Yokyi store(stack, index, item) {
    Yopok index > Yik(stack), append_item.
    stack[index] := item.
    Pohuwu.
append_item:
    Oxba(stack, item).
}

Yokyi apply(op, a, b) {
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
    Yopok b == 0, zero_divisor.
    Koke q := a / b.
    Yopok (a < 0) /= (b < 0), quotient_ready.
    Yopok (a % b) == 0, quotient_ready.
    q := q - 1.
quotient_ready:
    Yopok op == "%", remainder.
    Pohuwu q.
remainder:
    Pohuwu a - (b * q).
zero_divisor:
    Pohuwu Liliga.
}

Yokyi evaluate(line) {
    Koke values := [].
    Koke operators := ["("].
    Koke value_count := 0.
    Koke op_count := 1.
    Koke need_value := Geklabik.
    Koke length := Yik(line).
    Koke i := 1.
    Puwadish i <= (length + 1) Gihe Hehokgi
        // A final synthetic close reduces the initial opening parenthesis.
        Koke ch := ")".
        Yopok i > length, dispatch.
        ch := line[i].
dispatch:
        Yopok ch == " ", advance.
        Yopok Gukdidok need_value, read_operator.
        Yopok ch == "-", unary_minus.
        Yopok ch == "(", push_open.
        Yopok (ch < "0") Dak (ch > "9"), invalid.
        Koke number := 0.
        Puwadish i <= length Gihe Hehokgi
            Koke digit := line[i].
            Yopok (digit < "0") Dak (digit > "9"), end_number.
            number := (number * 10) + Bupuxbo(digit).
            i := i + 1.
        Kobihek
end_number:
        value_count := value_count + 1.
        store(values, value_count, number).
        need_value := Lesh.
        Gosh.
unary_minus:
        op_count := op_count + 1.
        store(operators, op_count, "~").
        Uxdrush advance.
push_open:
        op_count := op_count + 1.
        store(operators, op_count, "(").
        Uxdrush advance.
read_operator:
        Koke level := precedence(ch).
        Yopok ch == ")", reduce.
        Yopok (level == 0) Dak (ch == "~"), invalid.
reduce:
        Puwadish op_count > 0 Gihe Hehokgi
            Koke top := operators[op_count].
            Yopok top == "(", reduced.
            Yopok precedence(top) < level, reduced.
            op_count := op_count - 1.
            Yopok top == "~", negate.
            Yopok value_count < 2, invalid.
            Koke result := apply(top, values[value_count - 1], values[value_count]).
            Yopok result == Liliga, invalid.
            value_count := value_count - 1.
            values[value_count] := result.
            Gosh.
negate:
            Yopok value_count == 0, invalid.
            values[value_count] := -values[value_count].
        Kobihek
reduced:
        Yopok ch == ")", close_group.
        op_count := op_count + 1.
        store(operators, op_count, ch).
        need_value := Geklabik.
        Uxdrush advance.
close_group:
        Yopok op_count == 0, invalid.
        op_count := op_count - 1.
        Yopok (op_count == 0) Okdro (i <= length), invalid.
advance:
        i := i + 1.
    Kobihek
    Yopok (op_count /= 0) Dak (value_count /= 1), invalid.
    Pohuwu values[1].
invalid:
    Pohuwu "error".
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Ebi evaluate(line).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t3-justify">
Yokyi print_line(words, letters, width, full) {
    Koke size := Yik(words).
    Koke gaps := size - 1.
    Koke spaces := gaps.
    Yopok Gukdidok full, print_words.
    spaces := width - letters.
print_words:
    Wuhadi words[1].
    Gipolu i := 2 Wexdush size Gihe Hehokgi
        Koke padding := spaces / gaps.
        Gipolu j := 1 Wexdush padding Gihe Hehokgi
            Wuhadi " ".
        Kobihek
        Wuhadi words[i].
        spaces := spaces - padding.
        gaps := gaps - 1.
    Kobihek
    Ebi "".
}

Koke width := Bupuxbo(Pewexpo()).
Koke words := [].
Koke letters := 0.
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke word := "".
    Koke length := Yik(line).
    Gipolu i := 1 Wexdush length + 1 Gihe Hehokgi
        Yopok i > length, end_word.
        Koke ch := line[i].
        Yopok ch == " ", end_word.
        word := word ++ ch.
        Gosh.
end_word:
        Yopok word == "", next_character.
        Yopok (letters + Yik(words) + Yik(word)) <= width, add_word.
        print_line(words, letters, width, Geklabik).
        words := [].
        letters := 0.
add_word:
        Oxba(words, word).
        letters := letters + Yik(word).
        word := "".
next_character:
        Gosh.
    Kobihek
    line := Pewexpo().
Kobihek
Yopok Yik(words) == 0, done.
print_line(words, letters, width, Lesh).
done:
Pohuwu.
</solution>

<solution task="t3-maze">
Yokyi add_counts(a, b) {
    Koke i := Yik(a).
    Koke j := Yik(b).
    Koke carry := 0.
    Koke result := "".
    Puwadish (i > 0) Dak (j > 0) Dak (carry > 0) Gihe Hehokgi
        Koke digit := carry.
        Yopok i == 0, add_second.
        digit := digit + Bupuxbo(a[i]).
        i := i - 1.
add_second:
        Yopok j == 0, set_carry.
        digit := digit + Bupuxbo(b[j]).
        j := j - 1.
set_carry:
        carry := 0.
        Yopok digit < 10, save_digit.
        digit := digit - 10.
        carry := 1.
save_digit:
        result := Yawishbo(digit) ++ result.
    Kobihek
    Pohuwu result.
}

Koke dimensions := Pewexpo().
Koke h_text := "".
Koke w_text := "".
Koke past_space := Lesh.
Gipolu i := 1 Wexdush Yik(dimensions) Gihe Hehokgi
    Koke ch := dimensions[i].
    Yopok ch == " ", separator.
    Yopok past_space, width_digit.
    h_text := h_text ++ ch.
    Gosh.
width_digit:
    w_text := w_text ++ ch.
    Gosh.
separator:
    past_space := Geklabik.
Kobihek
Koke height := Bupuxbo(h_text).
Koke width := Bupuxbo(w_text).
Koke grid := [].
Koke distance := [].
Koke paths := [].
Koke queue := [].
Koke end_id := 0.
Gipolu r := 1 Wexdush height Gihe Hehokgi
    Koke row := Pewexpo().
    Oxba(grid, row).
    Gipolu c := 1 Wexdush width Gihe Hehokgi
        Koke id := ((r - 1) * width) + c.
        Oxba(distance, -1).
        Oxba(paths, "0").
        Yopok row[c] == "S", start_cell.
        Yopok row[c] == "E", end_cell.
        Gosh.
start_cell:
        distance[id] := 0.
        paths[id] := "1".
        Oxba(queue, [r, c]).
        Gosh.
end_cell:
        end_id := id.
    Kobihek
Kobihek

Koke dr := [-1, 1, 0, 0].
Koke dc := [0, 0, -1, 1].
Koke head := 1.
Puwadish head <= Yik(queue) Gihe Hehokgi
    Koke cell := queue[head].
    head := head + 1.
    Koke r := cell[1].
    Koke c := cell[2].
    Koke id := ((r - 1) * width) + c.
    Yopok id == end_id, print_result.
    Koke next_distance := distance[id] + 1.
    Gipolu direction := 1 Wexdush 4 Gihe Hehokgi
        Koke rr := r + dr[direction].
        Koke cc := c + dc[direction].
        Yopok (rr < 1) Dak (rr > height) Dak (cc < 1) Dak (cc > width), skip_neighbor.
        Koke row := grid[rr].
        Yopok row[cc] == "#", skip_neighbor.
        Koke neighbor := ((rr - 1) * width) + cc.
        Yopok distance[neighbor] == -1, discover.
        Yopok distance[neighbor] /= next_distance, skip_neighbor.
        paths[neighbor] := add_counts(paths[neighbor], paths[id]).
        Gosh.
discover:
        distance[neighbor] := next_distance.
        paths[neighbor] := paths[id].
        Oxba(queue, [rr, cc]).
skip_neighbor:
        Gosh.
    Kobihek
Kobihek
print_result:
Ebi distance[end_id] ++ " " ++ paths[end_id].
</solution>