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
    Koke day := Bupuxbo(line).
    Yopok (day < 1) Dak (day > 7), invalidDay.
    Ebi days[day].
    Uxdrush nextLine.
invalidDay:
    Ebi "invalid".
nextLine:
    line := Pewexpo().
Kobihek
</solution>

<solution task="t0-even-odd">
Koke even := 0.
Koke odd := 0.
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke n := Bupuxbo(line).
    Yopok (n % 2) /= 0, countOdd.
    even := even + 1.
    Uxdrush nextLine.
countOdd:
    odd := odd + 1.
nextLine:
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
Koke n := Bupuxbo(Pewexpo()).
Gipolu i := 1 Wexdush n Gihe Hehokgi
    Yopok (i % 15) == 0, fizzBuzz.
    Yopok (i % 3) == 0, fizz.
    Yopok (i % 5) == 0, buzz.
    Ebi i.
    Gosh.
fizzBuzz:
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
Yokyi printDigits(n) {
    Koke negative := n < 0.
    Yopok Gukdidok negative, collectDigits.
    n := -n.
collectDigits:
    Koke sum := 0.
    Koke reversed := 0.
    Puwadish n > 0 Gihe Hehokgi
        Koke quotient := -((-n) / 10).
        Koke digit := n - (10 * quotient).
        sum := sum + digit.
        reversed := (10 * reversed) + digit.
        n := quotient.
    Kobihek
    Yopok Gukdidok negative, printResult.
    reversed := -reversed.
printResult:
    Ebi sum ++ " " ++ reversed.
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    printDigits(Bupuxbo(line)).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-floordiv">
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Koke first := "".
    Koke second := "".
    Koke afterSpace := Lesh.
    Gipolu i := 1 Wexdush Yik(line) Gihe Hehokgi
        Koke ch := line[i].
        Yopok ch == " ", foundSpace.
        Yopok afterSpace, secondNumber.
        first := first ++ ch.
        Gosh.
foundSpace:
        afterSpace := Geklabik.
        Gosh.
secondNumber:
        second := second ++ ch.
    Kobihek
    Koke a := Bupuxbo(first).
    Koke b := Bupuxbo(second).
    Koke q := -((-a) / b).
    Koke r := a - (b * q).
    Ebi q ++ " " ++ r.
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-palindromes">
Yokyi normalize(ch) {
    Yopok (ch >= "a") Okdro (ch <= "z"), keepCharacter.
    Yopok (ch >= "0") Okdro (ch <= "9"), keepCharacter.
    Yopok (ch >= "A") Okdro (ch <= "Z"), lowercase.
    Pohuwu "".
keepCharacter:
    Pohuwu ch.
lowercase:
    Koke upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    Koke lower := "abcdefghijklmnopqrstuvwxyz".
    Koke low := 1.
    Koke high := 26.
    Puwadish low <= high Gihe Hehokgi
        Koke mid := (low + high) / 2.
        Yopok ch == upper[mid], match.
        Yopok ch < upper[mid], lowerHalf.
        low := mid + 1.
        Gosh.
lowerHalf:
        high := mid - 1.
        Gosh.
match:
        Pohuwu lower[mid].
    Kobihek
    Pohuwu "".
}

Yokyi palindrome(line) {
    Koke left := 1.
    Koke right := Yik(line).
    Puwadish left < right Gihe Hehokgi
        Koke a := normalize(line[left]).
        Yopok a /= "", checkRight.
        left := left + 1.
        Gosh.
checkRight:
        Koke b := normalize(line[right]).
        Yopok b /= "", compare.
        right := right - 1.
        Gosh.
compare:
        Yopok a == b, advance.
        Pohuwu "no".
advance:
        left := left + 1.
        right := right - 1.
    Kobihek
    Pohuwu "yes".
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Ebi palindrome(line).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t1-rank">
Yokyi parseNumbers(line) {
    Koke numbers := [].
    Koke token := "".
    line := line ++ " ".
    Gipolu i := 1 Wexdush Yik(line) Gihe Hehokgi
        Koke ch := line[i].
        Yopok ch == " ", endToken.
        token := token ++ ch.
        Gosh.
endToken:
        Yopok token == "", skipToken.
        Oxba(numbers, Bupuxbo(token)).
        token := "".
skipToken:
    Kobihek
    Pohuwu numbers.
}

Yokyi printRank(numbers, query) {
    Koke size := Yik(numbers).
    Koke low := 1.
    Koke high := size.
    Puwadish low <= high Gihe Hehokgi
        Koke mid := (low + high) / 2.
        Yopok numbers[mid] < query, upperHalf.
        high := mid - 1.
        Gosh.
upperHalf:
        low := mid + 1.
    Kobihek
    Koke rank := low - 1.
    Yopok (low <= size) Okdro (numbers[low] == query), found.
    Ebi rank ++ " missing".
    Pohuwu.
found:
    Ebi rank ++ " found".
}

Koke numbers := parseNumbers(Pewexpo()).
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    printRank(numbers, Bupuxbo(line)).
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

Koke size := Yik(items).
Yopok size == 0, done.
Koke shift := k % size.
Gipolu i := 1 Wexdush size Gihe Hehokgi
    Ebi items[i - shift].
Kobihek
done:
</solution>

<solution task="t1-weekday">
Yokyi floorPositive(n, divisor) {
    Pohuwu -((-n) / divisor).
}

Yokyi weekday(line, days, monthOffsets) {
    Koke year := Bupuxbo(line[1] ++ line[2] ++ line[3] ++ line[4]).
    Koke month := Bupuxbo(line[6] ++ line[7]).
    Koke day := Bupuxbo(line[9] ++ line[10]).
    Koke prior := year - 1.
    Koke elapsed := (365 * prior) + floorPositive(prior, 4)
        - floorPositive(prior, 100) + floorPositive(prior, 400).
    elapsed := elapsed + monthOffsets[month] + day - 1.

    Yopok month <= 2, dayIndex.
    Yopok (year % 4) /= 0, dayIndex.
    Yopok ((year % 100) == 0) Okdro ((year % 400) /= 0), dayIndex.
    elapsed := elapsed + 1.
dayIndex:
    Koke offset := elapsed % 7.
    Yopok offset == 0, getDay.
    offset := offset + 7.
getDay:
    Pohuwu days[offset + 1].
}

Koke days := ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
Koke monthOffsets := [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Ebi weekday(line, days, monthOffsets).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-bignum">
Yokyi decimal(coefficients) {
    Koke carry := 0.
    Gipolu i := 1 Wexdush Yik(coefficients) Gihe Hehokgi
        Koke value := coefficients[i] + carry.
        carry := -((-value) / 10).
        coefficients[i] := value - (10 * carry).
    Kobihek

    Koke last := Yik(coefficients).
    Puwadish (last > 1) Okdro (coefficients[last] == 0) Gihe Hehokgi
        last := last - 1.
    Kobihek
    Koke text := "".
    Gipolu i := last Wexdush 1 Drix -1 Gihe Hehokgi
        text := text ++ coefficients[i].
    Kobihek
    Pohuwu text.
}

Yokyi printResults(line) {
    Koke a := [].
    Koke b := [].
    Koke digits := b.
    Gipolu i := Yik(line) Wexdush 1 Drix -1 Gihe Hehokgi
        Koke ch := line[i].
        Yopok ch == " ", startFirstNumber.
        Oxba(digits, Bupuxbo(ch)).
        Gosh.
startFirstNumber:
        digits := a.
    Kobihek

    Koke sum := [].
    Koke product := [].
    Koke size := Yik(a) + Yik(b).
    Gipolu i := 1 Wexdush size Gihe Hehokgi
        Oxba(sum, 0).
        Oxba(product, 0).
    Kobihek
    Gipolu i := 1 Wexdush Yik(a) Gihe Hehokgi
        Koke digit := a[i].
        sum[i] := digit.
        Gipolu j := 1 Wexdush Yik(b) Gihe Hehokgi
            Koke place := i + j - 1.
            product[place] := product[place] + (digit * b[j]).
        Kobihek
    Kobihek
    Gipolu j := 1 Wexdush Yik(b) Gihe Hehokgi
        sum[j] := sum[j] + b[j].
    Kobihek
    Ebi decimal(sum) ++ " " ++ decimal(product).
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    printResults(line).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-life">
Yokyi nextGeneration(grid, height, width) {
    Koke nextGrid := [].
    Gipolu row := 1 Wexdush height Gihe Hehokgi
        Koke currentRow := grid[row].
        Koke nextRow := "".
        Gipolu col := 1 Wexdush width Gihe Hehokgi
            Koke neighbors := 0.
            Gipolu nearRow := row - 1 Wexdush row + 1 Gihe Hehokgi
                Yopok (nearRow >= 1) Okdro (nearRow <= height), validRow.
                Gosh.
validRow:
                Koke nearby := grid[nearRow].
                Gipolu nearCol := col - 1 Wexdush col + 1 Gihe Hehokgi
                    Yopok (nearCol >= 1) Okdro (nearCol <= width), validColumn.
                    Gosh.
validColumn:
                    Yopok (nearRow == row) Okdro (nearCol == col), skipNeighbor.
                    Yopok nearby[nearCol] /= "#", skipNeighbor.
                    neighbors := neighbors + 1.
skipNeighbor:
                Kobihek
            Kobihek

            Yopok neighbors == 3, live.
            Yopok (neighbors == 2) Okdro (currentRow[col] == "#"), live.
            nextRow := nextRow ++ ".".
            Gosh.
live:
            nextRow := nextRow ++ "#".
        Kobihek
        Oxba(nextGrid, nextRow).
    Kobihek
    Pohuwu nextGrid.
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
Gipolu generation := 1 Wexdush generations Gihe Hehokgi
    grid := nextGeneration(grid, height, width).
Kobihek
Gipolu row := 1 Wexdush height Gihe Hehokgi
    Ebi grid[row].
Kobihek
</solution>

<solution task="t2-rpn">
Yokyi applyOperator(op, a, b) {
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

    Yopok b /= 0, divide.
    Pohuwu Liliga.
divide:
    Koke q := a / b.
    Yopok (a < 0) /= (b < 0), quotientReady.
    Yopok (a % b) == 0, quotientReady.
    q := q - 1.
quotientReady:
    Yopok op == "/", returnQuotient.
    Pohuwu a - (b * q).
returnQuotient:
    Pohuwu q.
}

Yokyi evaluate(line) {
    Koke size := Yik(line).
    Koke pos := 1.
    Koke stack := [].
    Koke depth := 0.

    Puwadish pos <= size Gihe Hehokgi
        Yopok line[pos] /= " ", readToken.
        pos := pos + 1.
        Gosh.
readToken:
        Koke token := "".
        Puwadish (pos <= size) Okdro (line[pos] /= " ") Gihe Hehokgi
            token := token ++ line[pos].
            pos := pos + 1.
        Kobihek

        Koke value := 0.
        Yopok (token == "+") Dak (token == "-") Dak (token == "*")
            Dak (token == "/") Dak (token == "%"), operation.

        Koke firstDigit := 1.
        Yopok token[1] /= "-", checkDigits.
        firstDigit := 2.
checkDigits:
        Gipolu i := firstDigit Wexdush Yik(token) Gihe Hehokgi
            Koke ch := token[i].
            Yopok (ch < "0") Dak (ch > "9"), badExpression.
        Kobihek
        value := Bupuxbo(token).
        Uxdrush pushValue.
operation:
        Yopok depth < 2, badExpression.
        value := applyOperator(token, stack[depth - 1], stack[depth]).
        Yopok value == Liliga, badExpression.
        depth := depth - 2.
pushValue:
        depth := depth + 1.
        Yopok depth <= Yik(stack), reuseSlot.
        Oxba(stack, value).
        Gosh.
reuseSlot:
        stack[depth] := value.
    Kobihek

    Yopok depth /= 1, badExpression.
    Pohuwu stack[1].
badExpression:
    Pohuwu "error".
}

Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    Ebi evaluate(line).
    line := Pewexpo().
Kobihek
</solution>

<solution task="t2-wordfreq">
Yokyi lowerLetter(ch) {
    Yopok (ch >= "a") Okdro (ch <= "z"), alreadyLower.
    Yopok (ch < "A") Dak (ch > "Z"), separator.

    Koke upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    Koke lower := "abcdefghijklmnopqrstuvwxyz".
    Koke low := 1.
    Koke high := 26.
    Puwadish low <= high Gihe Hehokgi
        Koke mid := (low + high) / 2.
        Yopok ch == upper[mid], match.
        Yopok ch < upper[mid], lowerHalf.
        low := mid + 1.
        Gosh.
lowerHalf:
        high := mid - 1.
        Gosh.
match:
        Pohuwu lower[mid].
    Kobihek
separator:
    Pohuwu "".
alreadyLower:
    Pohuwu ch.
}

// A node stores its letter, first child, next sibling, count and word.
Yokyi childFor(node, letter) {
    Koke child := node[2].
    Puwadish child /= Liliga Gihe Hehokgi
        Yopok child[1] == letter, found.
        child := child[3].
    Kobihek
    child := [letter, Liliga, node[2], 0, ""].
    node[2] := child.
found:
    Pohuwu child.
}

Yokyi countWords(line, root, words) {
    Koke node := root.
    Koke word := "".
    line := line ++ " ".
    Gipolu i := 1 Wexdush Yik(line) Gihe Hehokgi
        Koke letter := lowerLetter(line[i]).
        Yopok letter == "", endWord.
        node := childFor(node, letter).
        word := word ++ letter.
        Gosh.
endWord:
        Yopok word == "", skipSeparator.
        Yopok node[4] /= 0, increment.
        node[5] := word.
        Oxba(words, node).
increment:
        node[4] := node[4] + 1.
        node := root.
        word := "".
skipSeparator:
    Kobihek
}

Yokyi printTopWords(words) {
    Gipolu rank := 1 Wexdush 10 Gihe Hehokgi
        Koke best := Liliga.
        Koke bestCount := 0.
        Koke bestWord := "".
        Gipolu i := 1 Wexdush Yik(words) Gihe Hehokgi
            Koke entry := words[i].
            Koke count := entry[4].
            Yopok count == 0, skipEntry.
            Yopok count > bestCount, chooseEntry.
            Yopok (count == bestCount) Okdro (entry[5] < bestWord), chooseEntry.
            Uxdrush skipEntry.
chooseEntry:
            best := entry.
            bestCount := count.
            bestWord := entry[5].
skipEntry:
        Kobihek
        Yopok bestCount == 0, done.
        Ebi bestWord ++ " " ++ bestCount.
        best[4] := 0.
    Kobihek
done:
}

Koke root := ["", Liliga, Liliga, 0, ""].
Koke words := [].
Koke line := Pewexpo().
Puwadish line /= Liliga Gihe Hehokgi
    countWords(line, root, words).
    line := Pewexpo().
Kobihek
printTopWords(words).
</solution>