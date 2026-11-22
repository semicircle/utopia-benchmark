<solution task="t0-count">
Atbekis n := Yomheis(Ucheschu()).
Ashes (Atbekis i := 1; i <= n; i := i + 1) {
    Seimyu i.
}
</solution>

<solution task="t0-day-names">
Atbekis days := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
Atbekis line := Ucheschu().
Bitreim (line != Kapluda) {
    Atbekis n := Yomheis(line).
    Umkeim (n < 1) Shei (n > 7), invalid_day.
    Seimyu days[n].
    Yudrese read_next.
invalid_day:
    Seimyu "invalid".
read_next:
    line := Ucheschu().
}
</solution>

<solution task="t0-even-odd">
Atbekis even := 0.
Atbekis odd := 0.
Atbekis line := Ucheschu().
Bitreim (line != Kapluda) {
    Atbekis n := Yomheis(line).
    Umkeim (n Ubok 2) != 0, count_odd.
    even := even + 1.
    Yudrese read_next.
count_odd:
    odd := odd + 1.
read_next:
    line := Ucheschu().
}
Seimyu "even " & even.
Seimyu "odd " & odd.
</solution>

<solution task="t0-factorial">
Atbekis n := Yomheis(Ucheschu()).
Atbekis result := 1.
Ashes (Atbekis i := 2; i <= n; i := i + 1) {
    result := result * i.
}
Seimyu result.
</solution>

<solution task="t0-fizzbuzz">
Atbekis n := Yomheis(Ucheschu()).
Ashes (Atbekis i := 1; i <= n; i := i + 1) {
    Umkeim (i Ubok 15) = 0, fizzbuzz.
    Umkeim (i Ubok 3) = 0, fizz.
    Umkeim (i Ubok 5) = 0, buzz.
    Seimyu i.
    Sabatchi.
fizzbuzz:
    Seimyu "FizzBuzz".
    Sabatchi.
fizz:
    Seimyu "Fizz".
    Sabatchi.
buzz:
    Seimyu "Buzz".
}
</solution>

<solution task="t0-hello">
Seimyu "Hello, Utopia!".
</solution>

<solution task="t0-reverse-lines">
Atbekis lines := [].
Atbekis line := Ucheschu().
Bitreim (line != Kapluda) {
    Tritriba(lines, line).
    line := Ucheschu().
}
Ashes (Atbekis i := Pluchutde(lines); i >= 1; i := i - 1) {
    Seimyu lines[i].
}
</solution>

<solution task="t1-digits">
Dradesde printDigits(n) Kro
    Atbekis negative := n < 0.
    Umkeim Ebakris negative, count_digits.
    n := -n.
count_digits:
    Atbekis sum := 0.
    Atbekis reversed := 0.
    Bitreim (n > 0) {
        Atbekis quotient := -((-n) / 10).
        Atbekis digit := n - (10 * quotient).
        sum := sum + digit.
        reversed := (10 * reversed) + digit.
        n := quotient.
    }
    Umkeim Ebakris negative, print_result.
    reversed := -reversed.
print_result:
    Seimyu sum & " " & reversed.
Kekrako

Atbekis line := Ucheschu().
Bitreim (line != Kapluda) {
    printDigits(Yomheis(line)).
    line := Ucheschu().
}
</solution>

<solution task="t1-floordiv">
Dradesde printFloorDivision(line) Kro
    Atbekis i := 1.
    Atbekis first := "".
    Bitreim (line[i] != " ") {
        first := first & line[i].
        i := i + 1.
    }
    Atbekis second := "".
    Atbekis length := Pluchutde(line).
    Ashes (i := i + 1; i <= length; i := i + 1) {
        second := second & line[i].
    }
    Atbekis a := Yomheis(first).
    Atbekis b := Yomheis(second).
    Atbekis q := a / b.
    Atbekis r := a - (b * q).
    Umkeim r = 0, print_result.
    q := q - 1.
    r := r + b.
print_result:
    Seimyu q & " " & r.
Kekrako

Atbekis line := Ucheschu().
Bitreim (line != Kapluda) {
    printFloorDivision(line).
    line := Ucheschu().
}
</solution>

<solution task="t1-palindromes">
Dradesde normalize(ch) Kro
    Umkeim (ch >= "A") Yebu (ch <= "Z"), uppercase.
    Umkeim (ch >= "a") Yebu (ch <= "z"), keep_char.
    Umkeim (ch >= "0") Yebu (ch <= "9"), keep_char.
    Bushayei "".
keep_char:
    Bushayei ch.
uppercase:
    Atbekis upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    Atbekis lower := "abcdefghijklmnopqrstuvwxyz".
    Atbekis low := 1.
    Atbekis high := 26.
    Bitreim (low < high) {
        Atbekis mid := ((low + high) - 1) / 2.
        Umkeim upper[mid] < ch, move_low.
        high := mid.
        Sabatchi.
move_low:
        low := mid + 1.
    }
    Bushayei lower[low].
Kekrako

Dradesde palindrome(line) Kro
    Atbekis left := 1.
    Atbekis right := Pluchutde(line).
    Bitreim (left < right) {
        Atbekis a := normalize(line[left]).
        Umkeim a = "", skip_left.
        Atbekis b := normalize(line[right]).
        Umkeim b = "", skip_right.
        Umkeim a != b, mismatch.
        left := left + 1.
        right := right - 1.
        Sabatchi.
skip_left:
        left := left + 1.
        Sabatchi.
skip_right:
        right := right - 1.
    }
    Bushayei "yes".
mismatch:
    Bushayei "no".
Kekrako

Atbekis line := Ucheschu().
Bitreim (line != Kapluda) {
    Seimyu palindrome(line).
    line := Ucheschu().
}
</solution>

<solution task="t1-rank">
Dradesde parseNumbers(line) Kro
    Atbekis numbers := [].
    Atbekis token := "".
    line := line & " ".
    Atbekis length := Pluchutde(line).
    Ashes (Atbekis i := 1; i <= length; i := i + 1) {
        Atbekis ch := line[i].
        Umkeim ch = " ", end_token.
        token := token & ch.
        Sabatchi.
end_token:
        Umkeim token = "", skip_token.
        Tritriba(numbers, Yomheis(token)).
        token := "".
skip_token:
    }
    Bushayei numbers.
Kekrako

Dradesde printRank(numbers, query) Kro
    Atbekis length := Pluchutde(numbers).
    Atbekis low := 1.
    Atbekis high := length + 1.
    Bitreim (low < high) {
        Atbekis mid := ((low + high) - 1) / 2.
        Umkeim numbers[mid] < query, move_low.
        high := mid.
        Sabatchi.
move_low:
        low := mid + 1.
    }
    Atbekis status := "missing".
    Umkeim (low > length) Shei (numbers[low] != query), print_result.
    status := "found".
print_result:
    Seimyu (low - 1) & " " & status.
Kekrako

Atbekis numbers := parseNumbers(Ucheschu()).
Atbekis line := Ucheschu().
Bitreim (line != Kapluda) {
    printRank(numbers, Yomheis(line)).
    line := Ucheschu().
}
</solution>

<solution task="t1-rotate">
Atbekis k := Yomheis(Ucheschu()).
Atbekis items := [].
Atbekis line := Ucheschu().
Bitreim (line != Kapluda) {
    Tritriba(items, line).
    line := Ucheschu().
}
Atbekis length := Pluchutde(items).
Umkeim length = 0, done.
Atbekis index := 1 - (k Ubok length).
Ashes (Atbekis printed := 0; printed < length; printed := printed + 1) {
    Seimyu items[index].
    index := index + 1.
    Umkeim index <= length, next_item.
    index := 1.
next_item:
}
done:
</solution>

<solution task="t1-weekday">
Dradesde floorDivide(n, d) Kro
    Bushayei -((-n) / d).
Kekrako

Dradesde weekday(date, days, monthOffsets) Kro
    Atbekis year := Yomheis(date[1] & date[2] & date[3] & date[4]).
    Atbekis month := Yomheis(date[6] & date[7]).
    Atbekis day := Yomheis(date[9] & date[10]).
    Atbekis previous := year - 1.
    Atbekis leapDays := (floorDivide(previous, 4) - floorDivide(previous, 100)) + floorDivide(previous, 400).
    Atbekis elapsed := (365 * previous) + leapDays + monthOffsets[month] + (day - 1).
    Umkeim month <= 2, get_day.
    Umkeim (year Ubok 400) = 0, add_leap_day.
    Umkeim ((year Ubok 4) != 0) Shei ((year Ubok 100) = 0), get_day.
add_leap_day:
    elapsed := elapsed + 1.
get_day:
    Atbekis index := 1 - ((-elapsed) Ubok 7).
    Bushayei days[index].
Kekrako

Atbekis days := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
Atbekis monthOffsets := [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334].
Atbekis line := Ucheschu().
Bitreim (line != Kapluda) {
    Seimyu weekday(line, days, monthOffsets).
    line := Ucheschu().
}
</solution>

<solution task="t2-bignum">
Dradesde readDigits(line, first, last) Kro
    Atbekis digits := [].
    Ashes (Atbekis i := last; i >= first; i := i - 1) {
        Tritriba(digits, Yomheis(line[i])).
    }
    Bushayei digits.
Kekrako

Dradesde carryOf(n) Kro
    Bushayei -((-n) / 10).
Kekrako

Dradesde addDigits(a, b) Kro
    Atbekis aLength := Pluchutde(a).
    Atbekis bLength := Pluchutde(b).
    Atbekis result := [].
    Atbekis carry := 0.
    Ashes (Atbekis i := 1; (i <= aLength) Shei (i <= bLength); i := i + 1) {
        Atbekis total := carry.
        Umkeim i > aLength, add_second.
        total := total + a[i].
add_second:
        Umkeim i > bLength, write_digit.
        total := total + b[i].
write_digit:
        carry := carryOf(total).
        Tritriba(result, total - (10 * carry)).
    }
    Umkeim carry = 0, done.
    Tritriba(result, carry).
done:
    Bushayei result.
Kekrako

Dradesde multiplyDigits(a, b) Kro
    Atbekis aLength := Pluchutde(a).
    Atbekis bLength := Pluchutde(b).
    Atbekis length := aLength + bLength.
    Atbekis result := [].
    Ashes (Atbekis i := 1; i <= length; i := i + 1) {
        Tritriba(result, 0).
    }
    Ashes (Atbekis i := 1; i <= aLength; i := i + 1) {
        Ashes (Atbekis j := 1; j <= bLength; j := j + 1) {
            Atbekis index := (i + j) - 1.
            result[index] := result[index] + (a[i] * b[j]).
        }
    }
    Atbekis carry := 0.
    Ashes (Atbekis i := 1; i <= length; i := i + 1) {
        Atbekis total := result[i] + carry.
        carry := carryOf(total).
        result[i] := total - (10 * carry).
    }
    Bushayei result.
Kekrako

Dradesde decimalText(digits) Kro
    Atbekis i := Pluchutde(digits).
    Bitreim ((i > 1) Yebu (digits[i] = 0)) {
        i := i - 1.
    }
    Atbekis text := "".
    Ashes (; i >= 1; i := i - 1) {
        text := text & digits[i].
    }
    Bushayei text.
Kekrako

Atbekis line := Ucheschu().
Bitreim (line != Kapluda) {
    Atbekis separator := 1.
    Bitreim (line[separator] != " ") {
        separator := separator + 1.
    }
    Atbekis a := readDigits(line, 1, separator - 1).
    Atbekis b := readDigits(line, separator + 1, Pluchutde(line)).
    Seimyu decimalText(addDigits(a, b)) & " " & decimalText(multiplyDigits(a, b)).
    line := Ucheschu().
}
</solution>

<solution task="t2-life">
Atbekis generations := Yomheis(Ucheschu()).
Atbekis line := Ucheschu().
Atbekis width := Pluchutde(line).
Atbekis border := [].
Ashes (Atbekis i := 1; i <= width + 2; i := i + 1) {
    Tritriba(border, 0).
}
Atbekis grid := [border].
Bitreim (line != Kapluda) {
    Atbekis row := [0].
    Ashes (Atbekis i := 1; i <= width; i := i + 1) {
        Atbekis cell := 0.
        Umkeim line[i] != "#", append_input_cell.
        cell := 1.
append_input_cell:
        Tritriba(row, cell).
    }
    Tritriba(row, 0).
    Tritriba(grid, row).
    line := Ucheschu().
}
Tritriba(grid, border).

Atbekis lastRow := Pluchutde(grid) - 1.
Atbekis lastColumn := width + 1.
Ashes (Atbekis generation := 0; generation < generations; generation := generation + 1) {
    Atbekis nextGrid := [border].
    Ashes (Atbekis r := 2; r <= lastRow; r := r + 1) {
        Atbekis above := grid[r - 1].
        Atbekis middle := grid[r].
        Atbekis below := grid[r + 1].
        Atbekis nextRow := [0].
        Ashes (Atbekis c := 2; c <= lastColumn; c := c + 1) {
            Atbekis left := c - 1.
            Atbekis right := c + 1.
            Atbekis neighbours := above[left] + above[c] + above[right]
                + middle[left] + middle[right]
                + below[left] + below[c] + below[right].
            Atbekis cell := 0.
            Umkeim (neighbours = 3) Shei ((neighbours = 2) Yebu (middle[c] = 1)), live_cell.
            Yudrese append_cell.
live_cell:
            cell := 1.
append_cell:
            Tritriba(nextRow, cell).
        }
        Tritriba(nextRow, 0).
        Tritriba(nextGrid, nextRow).
    }
    Tritriba(nextGrid, border).
    grid := nextGrid.
}

Atbekis symbols := ".#".
Ashes (Atbekis r := 2; r <= lastRow; r := r + 1) {
    Atbekis row := grid[r].
    Ashes (Atbekis c := 2; c <= lastColumn; c := c + 1) {
        Bachet symbols[row[c] + 1].
    }
    Seimyu "".
}
</solution>

<solution task="t2-rpn">
Dradesde truncateDivide(a, b) Kro
    Atbekis q := a / b.
    Umkeim ((a < 0) = (b < 0)) Shei ((a Ubok b) = 0), done.
    q := q - 1.
done:
    Bushayei q.
Kekrako

Dradesde evaluate(line) Kro
    Atbekis stack := [].
    Atbekis size := 0.
    Atbekis length := Pluchutde(line).
    Atbekis i := 1.
    Bitreim (i <= length) {
        Umkeim line[i] != " ", start_token.
        i := i + 1.
        Sabatchi.
start_token:
        Atbekis start := i.
        Bitreim ((i <= length) Yebu (line[i] != " ")) {
            i := i + 1.
        }
        Atbekis ch := line[start].
        Atbekis value := 0.
        Atbekis operator := (ch = "+") Shei (ch = "-") Shei (ch = "*") Shei (ch = "/") Shei (ch = "%").
        Umkeim ((i - start) = 1) Yebu operator, apply_operator.

        Atbekis firstDigit := start.
        Umkeim ch != "-", read_digits.
        firstDigit := firstDigit + 1.
read_digits:
        Umkeim firstDigit = i, invalid.
        Ashes (Atbekis j := firstDigit; j < i; j := j + 1) {
            Atbekis digit := line[j].
            Umkeim (digit < "0") Shei (digit > "9"), invalid.
            value := (10 * value) + Yomheis(digit).
        }
        Umkeim ch != "-", push_value.
        value := -value.
        Yudrese push_value.

apply_operator:
        Umkeim size < 2, invalid.
        Atbekis b := stack[size].
        Atbekis a := stack[size - 1].
        size := size - 2.
        Umkeim (b = 0) Yebu ((ch = "/") Shei (ch = "%")), invalid.
        Sabei ch Triboba
        "+": Kro
            value := a + b.
        Kekrako
        "-": Kro
            value := a - b.
        Kekrako
        "*": Kro
            value := a * b.
        Kekrako
        "/": Kro
            value := truncateDivide(a, b).
        Kekrako
        "%": Kro
            value := a - (b * truncateDivide(a, b)).
        Kekrako
        Kekrako

push_value:
        size := size + 1.
        Umkeim size <= Pluchutde(stack), reuse_slot.
        Tritriba(stack, value).
        Sabatchi.
reuse_slot:
        stack[size] := value.
    }
    Umkeim size != 1, invalid.
    Bushayei stack[1].
invalid:
    Bushayei "error".
Kekrako

Atbekis line := Ucheschu().
Bitreim (line != Kapluda) {
    Seimyu evaluate(line).
    line := Ucheschu().
}
</solution>

<solution task="t2-wordfreq">
Dradesde normalizeLetter(ch, upper, lower) Kro
    Umkeim (ch >= "a") Yebu (ch <= "z"), lowercase.
    Umkeim (ch < "A") Shei (ch > "Z"), separator.
    Atbekis low := 1.
    Atbekis high := 26.
    Bitreim (low < high) {
        Atbekis mid := ((low + high) - 1) / 2.
        Umkeim upper[mid] < ch, move_low.
        high := mid.
        Sabatchi.
move_low:
        low := mid + 1.
    }
    Bushayei lower[low].
lowercase:
    Bushayei ch.
separator:
    Bushayei "".
Kekrako

Dradesde wordText(line, first, last, upper, lower) Kro
    Umkeim first < last, join_halves.
    Bushayei normalizeLetter(line[first], upper, lower).
join_halves:
    Atbekis mid := ((first + last) - 1) / 2.
    Bushayei wordText(line, first, mid, upper, lower) & wordText(line, mid + 1, last, upper, lower).
Kekrako

// Each trie node stores its count, first child, next sibling, letter and word.
Dradesde childFor(node, letter) Kro
    Atbekis child := node[2].
    Bitreim (child != Kapluda) {
        Umkeim child[4] = letter, found_child.
        child := child[3].
    }
    child := [0, Kapluda, node[2], letter, ""].
    node[2] := child.
found_child:
    Bushayei child.
Kekrako

Dradesde countLine(line, root, words, upper, lower) Kro
    Atbekis length := Pluchutde(line).
    Atbekis node := root.
    Atbekis start := 1.
    Ashes (Atbekis i := 1; i <= length + 1; i := i + 1) {
        Atbekis letter := "".
        Umkeim i > length, classified.
        letter := normalizeLetter(line[i], upper, lower).
classified:
        Umkeim letter = "", end_word.
        node := childFor(node, letter).
        Sabatchi.
end_word:
        Umkeim start = i, next_word.
        Umkeim node[1] != 0, increment_count.
        node[5] := wordText(line, start, i - 1, upper, lower).
        Tritriba(words, node).
increment_count:
        node[1] := node[1] + 1.
        node := root.
next_word:
        start := i + 1.
    }
Kekrako

Atbekis upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
Atbekis lower := "abcdefghijklmnopqrstuvwxyz".
Atbekis root := [0, Kapluda, Kapluda, "", ""].
Atbekis words := [].
Atbekis line := Ucheschu().
Bitreim (line != Kapluda) {
    countLine(line, root, words, upper, lower).
    line := Ucheschu().
}

Atbekis distinct := Pluchutde(words).
Ashes (Atbekis place := 1; (place <= 10) Yebu (place <= distinct); place := place + 1) {
    Atbekis best := Kapluda.
    Ashes (Atbekis i := 1; i <= distinct; i := i + 1) {
        Atbekis entry := words[i].
        Umkeim entry[1] = 0, next_entry.
        Umkeim best = Kapluda, choose_entry.
        Umkeim entry[1] > best[1], choose_entry.
        Umkeim (entry[1] != best[1]) Shei (entry[5] >= best[5]), next_entry.
choose_entry:
        best := entry.
next_entry:
    }
    Seimyu best[5] & " " & best[1].
    best[1] := 0.
}
</solution>