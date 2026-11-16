<solution task="t0-count">
ohetdi line = nilhino().
ohetdi n = nelchiyul(line).
lemyunom i = 1 thikutli n mitho nethe
    miyol i.
dit
</solution>

<solution task="t0-day-names">
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi d = nelchiyul(line).
    thi torelro d
    torelro 1
        miyol "Monday".
    torelro 2
        miyol "Tuesday".
    torelro 3
        miyol "Wednesday".
    torelro 4
        miyol "Thursday".
    torelro 5
        miyol "Friday".
    torelro 6
        miyol "Saturday".
    torelro 7
        miyol "Sunday".
    torelro thumku
        miyol "invalid".
    dit thi
    line = nilhino().
dit
</solution>

<solution task="t0-even-odd">
ohetdi even = 0.
ohetdi odd = 0.
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    ohetdi n = nelchiyul(line).
    rilniro n kolethul 2 == 0 hutro nethe
        even = even + 1.
    dit thumku nethe
        odd = odd + 1.
    dit
    line = nilhino().
dit
miyol "even " & even.
miyol "odd " & odd.
</solution>

<solution task="t0-factorial">
ohetdi line = nilhino().
ohetdi n = nelchiyul(line).
ohetdi result = 1.
lemyunom i = 1 thikutli n mitho nethe
    result = result * i.
dit
miyol result.
</solution>

<solution task="t0-fizzbuzz">
ohetdi line = nilhino().
ohetdi n = nelchiyul(line).
lemyunom i = 1 thikutli n mitho nethe
    rilniro i kolethul 15 == 0 hutro nethe
        miyol "FizzBuzz".
    dit thumku rilniro i kolethul 3 == 0 hutro nethe
        miyol "Fizz".
    dit thumku rilniro i kolethul 5 == 0 hutro nethe
        miyol "Buzz".
    dit thumku nethe
        miyol i.
    dit
dit
</solution>

<solution task="t0-hello">
miyol "Hello, Utopia!".
</solution>

<solution task="t0-reverse-lines">
ohetdi lines = [].
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    nimhol(lines, line).
    line = nilhino().
dit
lemyunom i = yuyem(lines) - 1 thikutli 0 rodilvul -1 mitho nethe
    miyol lines[i].
dit
</solution>