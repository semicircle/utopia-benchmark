# Life

The first line of standard input holds an integer `g` (0 ≤ g ≤ 30). It is
followed by one or more lines of equal length (at most 20 lines of at most
20 characters), a grid of cells: `#` is a live cell and `.` a dead one.

Write a {{.Lang}} program that runs `g` generations of Conway's Game of Life
on the grid and prints the final grid in the same format. In each
generation, every cell looks at its up to eight neighbours (horizontally,
vertically and diagonally adjacent cells): a live cell with two or three
live neighbours stays alive, a dead cell with exactly three live neighbours
becomes alive, and every other cell is dead in the next generation. All
cells change at the same time. Cells outside the grid are always dead: the
grid does not wrap around.
