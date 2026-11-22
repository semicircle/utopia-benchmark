<solution task="t0-count">
Koke n := Bupuxbo(Pewexpo()).
Gipolu i := 1 Wexdush n Gihe Hehokgi
    Ebi i.
Kobihek
</solution>

<solution task="t0-day-names">
Koke names := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke day := Bupuxbo(line).
    Yopok (day >= 1) Okdro (day <= 7), valid_day.
    Ebi "invalid".
    Uxdrush read_next.
valid_day:
    Ebi names[day].
read_next:
    line := Pewexpo().
Kobihek
</solution>

<solution task="t0-even-odd">
Koke even := 0.
Koke odd := 0.
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke n := Bupuxbo(line).
    Yopok n % 2 == 0, count_even.
    odd := odd + 1.
    Uxdrush read_next.
count_even:
    even := even + 1.
read_next:
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
    Yopok n % 3 == 0, only_fizz.
    Yopok n % 5 == 0, only_buzz.
    Pohuwu n.
both:
    Pohuwu "FizzBuzz".
only_fizz:
    Pohuwu "Fizz".
only_buzz:
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
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke digits := Bupuxbo(line).
    Koke sign := 1.
    Yopok digits >= 0, ready.
    sign := -1.
    digits := -digits.
ready:
    Koke sum := 0.
    Koke reversed := 0.
    Puwadish digits > 0 Gihe Hehokgi
        Koke rest := (digits - 9) / 10.
        Koke digit := digits - (rest * 10).
        sum := sum + digit.
        reversed := (reversed * 10) + digit.
        digits := rest.
    Kobihek
    Ebi sum ++ " " ++ (sign * reversed).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-floordiv">
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke left := "".
    Koke right := "".
    Koke i := 1.
    Puwadish line[i] /= " " Gihe Hehokgi
        left := left ++ line[i].
        i := i + 1.
    Kobihek
    Gipolu j := i + 1 Wexdush Yik(line) Gihe Hehokgi
        right := right ++ line[j].
    Kobihek
    Koke a := Bupuxbo(left).
    Koke b := Bupuxbo(right).
    Koke q := a / b.
    Koke r := a % b.
    Yopok r == 0, print_result.
    q := q - 1.
    r := r + b.
print_result:
    Ebi q ++ " " ++ r.
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-palindromes">
Yokyi normalize(c) {
    Yopok ((c >= "a") Okdro (c <= "z")) Dak ((c >= "0") Okdro (c <= "9")), unchanged.
    Yopok (c < "A") Dak (c > "Z"), ignored.
    Koke upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    Koke lower := "abcdefghijklmnopqrstuvwxyz".
    Koke lo := 1.
    Koke hi := 26.
    Puwadish lo < hi Gihe Hehokgi
        Koke mid := (lo + hi - 1) / 2.
        Yopok upper[mid] < c, upper_half.
        hi := mid.
        Gosh.
upper_half:
        lo := mid + 1.
    Kobihek
    Pohuwu lower[lo].
unchanged:
    Pohuwu c.
ignored:
    Pohuwu Liliga.
}

Yokyi palindrome(line) {
    Koke chars := [].
    Gipolu i := 1 Wexdush Yik(line) Gihe Hehokgi
        Koke c := normalize(line[i]).
        Yopok c == Liliga, skip_char.
        Oxba(chars, c).
skip_char:
        Gosh.
    Kobihek
    Koke lo := 1.
    Koke hi := Yik(chars).
    Puwadish lo < hi Gihe Hehokgi
        Yopok chars[lo] /= chars[hi], mismatch.
        lo := lo + 1.
        hi := hi - 1.
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
Yokyi lower_bound(numbers, query) {
    Koke lo := 1.
    Koke hi := Yik(numbers) + 1.
    Puwadish lo < hi Gihe Hehokgi
        Koke mid := (lo + hi - 1) / 2.
        Yopok numbers[mid] < query, upper_half.
        hi := mid.
        Gosh.
upper_half:
        lo := mid + 1.
    Kobihek
    Pohuwu lo.
}

Koke numbers := [].
Koke first := Pewexpo() ++ " ".
Koke token := "".
Gipolu i := 1 Wexdush Yik(first) Gihe Hehokgi
    Koke c := first[i].
    Yopok c == " ", separator.
    token := token ++ c.
    Gosh.
separator:
    Yopok token == "", next_char.
    Oxba(numbers, Bupuxbo(token)).
    token := "".
next_char:
    Gosh.
Kobihek

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke query := Bupuxbo(line).
    Koke position := lower_bound(numbers, query).
    Koke status := "missing".
    Yopok (position <= Yik(numbers)) Okdro (numbers[position] == query), found_query.
    Uxdrush print_result.
found_query:
    status := "found".
print_result:
    Ebi (position - 1) ++ " " ++ status.
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
Koke names := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
Koke month_start := [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke year := Bupuxbo(line[1] ++ line[2] ++ line[3] ++ line[4]).
    Koke month := Bupuxbo(line[6] ++ line[7]).
    Koke day := Bupuxbo(line[9] ++ line[10]).
    Koke prior := year - 1.
    Koke leap_years := ((prior - 3) / 4) - ((prior - 99) / 100) + ((prior - 399) / 400).
    Koke elapsed := (365 * prior) + leap_years + month_start[month] + day - 1.
    Yopok month <= 2, print_day.
    Yopok year % 400 == 0, add_leap_day.
    Yopok (year % 4 /= 0) Dak (year % 100 == 0), print_day.
add_leap_day:
    elapsed := elapsed + 1.
print_day:
    Ebi names[elapsed + 1].
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-bignum">
Yokyi read_chunks(line, first, last) {
    Koke chunks := [].
    Koke chunk := 0.
    Koke place := 1.
    Gipolu pos := last Wexdush first Drix -1 Gihe Hehokgi
        chunk := chunk + (Bupuxbo(line[pos]) * place).
        place := place * 10.
        Yopok place /= 100000000, next_digit.
        Oxba(chunks, chunk).
        chunk := 0.
        place := 1.
next_digit:
        Gosh.
    Kobihek
    Yopok place == 1, done.
    Oxba(chunks, chunk).
done:
    Pohuwu chunks.
}

Yokyi add_chunks(a, b) {
    Koke len_a := Yik(a).
    Koke len_b := Yik(b).
    Koke size := len_a.
    Yopok size >= len_b, allocate.
    size := len_b.
allocate:
    Koke result := [].
    Gipolu i := 1 Wexdush size Gihe Hehokgi
        Koke value := 0.
        Yopok i > len_a, add_b.
        value := a[i].
add_b:
        Yopok i > len_b, keep.
        value := value + b[i].
keep:
        Oxba(result, value).
    Kobihek
    Pohuwu result.
}

Yokyi multiply_chunks(a, b) {
    Koke len_a := Yik(a).
    Koke len_b := Yik(b).
    Koke result := [].
    Gipolu i := 1 Wexdush len_a + len_b - 1 Gihe Hehokgi
        Oxba(result, 0).
    Kobihek
    Gipolu i := 1 Wexdush len_a Gihe Hehokgi
        Gipolu j := 1 Wexdush len_b Gihe Hehokgi
            Koke pos := i + j - 1.
            result[pos] := result[pos] + (a[i] * b[j]).
        Kobihek
    Kobihek
    Pohuwu result.
}

Yokyi decimal_text(chunks) {
    Koke base := 100000000.
    Koke carry := 0.
    Gipolu i := 1 Wexdush Yik(chunks) Gihe Hehokgi
        Koke value := chunks[i] + carry.
        carry := (value - (base - 1)) / base.
        chunks[i] := value - (carry * base).
    Kobihek
    Puwadish carry > 0 Gihe Hehokgi
        Koke quotient := (carry - (base - 1)) / base.
        Oxba(chunks, carry - (quotient * base)).
        carry := quotient.
    Kobihek
    Koke last := Yik(chunks).
    Puwadish (last > 1) Okdro (chunks[last] == 0) Gihe Hehokgi
        last := last - 1.
    Kobihek
    Koke result := Yawishbo(chunks[last]).
    Gipolu j := last - 1 Wexdush 1 Drix -1 Gihe Hehokgi
        Koke digits := Yawishbo(chunks[j]).
        Gipolu pad := Yik(digits) + 1 Wexdush 8 Gihe Hehokgi
            result := result ++ "0".
        Kobihek
        result := result ++ digits.
    Kobihek
    Pohuwu result.
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke separator := 1.
    Puwadish line[separator] /= " " Gihe Hehokgi
        separator := separator + 1.
    Kobihek
    Koke a := read_chunks(line, 1, separator - 1).
    Koke b := read_chunks(line, separator + 1, Yik(line)).
    Koke sum := decimal_text(add_chunks(a, b)).
    Koke product := decimal_text(multiply_chunks(a, b)).
    Ebi sum ++ " " ++ product.
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-life">
Koke generations := Bupuxbo(Pewexpo()).
Koke line := Pewexpo().
Koke width := Yik(line).
Koke border := "".
Gipolu i := 1 Wexdush width + 2 Gihe Hehokgi
    border := border ++ ".".
Kobihek
Koke grid := [border].
Puwadish line /= Liliga Gihe Hehokgi
    Oxba(grid, "." ++ line ++ ".").
    line := Pewexpo().
Kobihek
Oxba(grid, border).
Koke last_row := Yik(grid) - 1.
Koke last_col := width + 1.

Gipolu generation := 1 Wexdush generations Gihe Hehokgi
    Koke next_grid := [border].
    Gipolu row := 2 Wexdush last_row Gihe Hehokgi
        Koke current := grid[row].
        Koke next_row := ".".
        Gipolu col := 2 Wexdush last_col Gihe Hehokgi
            Koke neighbors := 0.
            Gipolu near_row := row - 1 Wexdush row + 1 Gihe Hehokgi
                Koke adjacent := grid[near_row].
                Gipolu near_col := col - 1 Wexdush col + 1 Gihe Hehokgi
                    Yopok (near_row == row) Okdro (near_col == col), skip_neighbor.
                    Yopok adjacent[near_col] /= "#", skip_neighbor.
                    neighbors := neighbors + 1.
skip_neighbor:
                    Gosh.
                Kobihek
            Kobihek
            Yopok (neighbors == 3) Dak ((neighbors == 2) Okdro (current[col] == "#")), live_cell.
            next_row := next_row ++ ".".
            Gosh.
live_cell:
            next_row := next_row ++ "#".
        Kobihek
        Oxba(next_grid, next_row ++ ".").
    Kobihek
    Oxba(next_grid, border).
    grid := next_grid.
Kobihek

Gipolu row := 2 Wexdush last_row Gihe Hehokgi
    Koke cells := grid[row].
    Gipolu col := 2 Wexdush last_col Gihe Hehokgi
        Wuhadi cells[col].
    Kobihek
    Ebi "".
Kobihek
</solution>

<solution task="t2-rpn">
Yokyi parse_integer(token) {
    Koke first := 1.
    Yopok token[1] /= "-", check_digits.
    first := 2.
check_digits:
    Koke size := Yik(token).
    Yopok first > size, invalid.
    Gipolu i := first Wexdush size Gihe Hehokgi
        Koke c := token[i].
        Yopok (c < "0") Dak (c > "9"), invalid.
    Kobihek
    Pohuwu Bupuxbo(token).
invalid:
    Pohuwu Liliga.
}

Yokyi calculate(a, b, op) {
    Dru op Ihedrux
    "+": Hehokgi
        Pohuwu a + b.
    Kobihek
    "-": Hehokgi
        Pohuwu a - b.
    Kobihek
    "*": Hehokgi
        Pohuwu a * b.
    Kobihek
    Kobihek
    Yopok b == 0, zero_divisor.
    Koke q := a / b.
    Koke r := a % b.
    Yopok (r == 0) Dak ((a < 0) /= (b < 0)), rounded.
    q := q - 1.
    r := r + b.
rounded:
    Yopok op == "/", quotient.
    Pohuwu r.
quotient:
    Pohuwu q.
zero_divisor:
    Pohuwu Liliga.
}

Yokyi evaluate(line) {
    Koke text := line ++ " ".
    Koke stack := [].
    Koke depth := 0.
    Koke token := "".
    Gipolu i := 1 Wexdush Yik(text) Gihe Hehokgi
        Koke c := text[i].
        Yopok c == " ", end_token.
        token := token ++ c.
        Gosh.
end_token:
        Yopok token == "", next_char.
        Koke item := token.
        token := "".
        Koke value := Liliga.
        Dru item Ihedrux
        "+", "-", "*", "/", "%": Hehokgi
            Yopok depth < 2, invalid.
            value := calculate(stack[depth - 1], stack[depth], item).
            depth := depth - 2.
        Kobihek
        Hishyeko Hehokgi
            value := parse_integer(item).
        Kobihek Kobihek
        Yopok value == Liliga, invalid.
        depth := depth + 1.
        Yopok depth <= Yik(stack), reuse_slot.
        Oxba(stack, value).
        Gosh.
reuse_slot:
        stack[depth] := value.
next_char:
        Gosh.
    Kobihek
    Yopok depth /= 1, invalid.
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
Yokyi letter_index(c, lower, upper) {
    Koke alphabet := lower.
    Yopok (c >= "a") Okdro (c <= "z"), search.
    Yopok (c < "A") Dak (c > "Z"), separator.
    alphabet := upper.
search:
    Koke lo := 1.
    Koke hi := 26.
    Puwadish lo < hi Gihe Hehokgi
        Koke mid := (lo + hi - 1) / 2.
        Yopok alphabet[mid] < c, upper_half.
        hi := mid.
        Gosh.
upper_half:
        lo := mid + 1.
    Kobihek
    Pohuwu lo.
separator:
    Pohuwu 0.
}

Yokyi empty_table(size) {
    Koke table := [].
    Gipolu i := 1 Wexdush size Gihe Hehokgi
        Oxba(table, 0).
    Kobihek
    Pohuwu table.
}

Yokyi link_entry(table, entry, index) {
    Koke slot := 1 - (entry[3] % Yik(table)).
    entry[4] := table[slot].
    table[slot] := index.
}

Yokyi count_word(table, entries, word, hash) {
    Koke slot := 1 - (hash % Yik(table)).
    Koke index := table[slot].
    // Each entry stores its word, count, hash and next index in the bucket.
    Puwadish index /= 0 Gihe Hehokgi
        Koke entry := entries[index].
        Yopok entry[1] /= word, next_entry.
        entry[2] := entry[2] + 1.
        Pohuwu table.
next_entry:
        index := entry[4].
    Kobihek
    Koke added := [word, 1, hash, 0].
    Oxba(entries, added).
    Yopok Yik(entries) > Yik(table), grow_table.
    link_entry(table, added, Yik(entries)).
    Pohuwu table.
grow_table:
    Koke larger := empty_table(Yik(table) * 2).
    Gipolu i := 1 Wexdush Yik(entries) Gihe Hehokgi
        link_entry(larger, entries[i], i).
    Kobihek
    Pohuwu larger.
}

Koke lower := "abcdefghijklmnopqrstuvwxyz".
Koke upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
Koke entries := [].
Koke table := empty_table(32).
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke text := line ++ " ".
    Koke word := "".
    Koke hash := 0.
    Gipolu i := 1 Wexdush Yik(text) Gihe Hehokgi
        Koke letter := letter_index(text[i], lower, upper).
        Yopok letter == 0, end_word.
        word := word ++ lower[letter].
        hash := (hash * 31 + letter) % 1000000007.
        Gosh.
end_word:
        Yopok word == "", next_char.
        table := count_word(table, entries, word, hash).
        word := "".
        hash := 0.
next_char:
        Gosh.
    Kobihek
    line := Pewexpo().
Kobihek

Gipolu rank := 1 Wexdush 10 Gihe Hehokgi
    Koke best := 0.
    Koke best_count := 0.
    Koke best_word := "".
    Gipolu i := 1 Wexdush Yik(entries) Gihe Hehokgi
        Koke entry := entries[i].
        Koke count := entry[2].
        Koke candidate := entry[1].
        Yopok (count > best_count) Dak ((count == best_count) Okdro (candidate < best_word)), choose.
        Gosh.
choose:
        best := i.
        best_count := count.
        best_word := candidate.
    Kobihek
    Yopok best /= 0, print_word.
    Kewi.
print_word:
    Ebi best_word ++ " " ++ best_count.
    Koke selected := entries[best].
    selected[2] := 0.
Kobihek
</solution>