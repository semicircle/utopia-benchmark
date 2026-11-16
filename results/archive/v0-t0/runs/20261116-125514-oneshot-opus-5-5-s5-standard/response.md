<solution task="t0-count">
ohetdi line = nilhino().
ohetdi n = 0.
rilniro line <> emletlel hutro nethe
    n = nelchiyul(line).
dit
lemyunom i = 1 thikutli n mitho nethe
    miyol i.
dit
</solution>

<solution task="t0-day-names">
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    rilniro yuyem(line) > 0 hutro nethe
        ohetdi n = nelchiyul(line).
        thi torelro n
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
    dit
    line = nilhino().
dit
</solution>

<solution task="t0-even-odd">
ohetdi evens = 0.
ohetdi odds = 0.
ohetdi line = nilhino().
konit line <> emletlel mitho nethe
    rilniro yuyem(line) > 0 hutro nethe
        ohetdi n = nelchiyul(line).
        rilniro n kolethul 2 == 0 hutro nethe
            evens = evens + 1.
        dit thumku nethe
            odds = odds + 1.
        dit
    dit
    line = nilhino().
dit
miyol "even " & evens.
miyol "odd " & odds.
</solution>

<solution task="t0-factorial">
ohetdi n = nelchiyul(nilhino()).
ohetdi f = 1.
lemyunom i = 2 thikutli n mitho nethe
    f = f * i.
dit
miyol f.
</solution>

<solution task="t0-fizzbuzz">
ohetdi n = nelchiyul(nilhino()).
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