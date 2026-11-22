# Maze paths

The first line of standard input holds two integers, the height `H` and the
width `W` of a grid (each between 1 and 25), separated by one space. The
next `H` lines each hold `W` characters: `.` is an open cell, `#` is a wall,
`S` is the start and `E` is the end. There is exactly one `S` and exactly
one `E`, and both are open cells.

A step moves from an open cell to one of its four neighbors (up, down, left
or right) that is open and inside the grid. There is no wrapping around the
edges.

Write a {{.Lang}} program that prints one line: the smallest number of steps
from `S` to `E`, a space, and the number of different step sequences of that
smallest length. If `E` cannot be reached, print `-1 0`.

For example, for

```
2 3
S..
..E
```

the answer is `3 3`.
