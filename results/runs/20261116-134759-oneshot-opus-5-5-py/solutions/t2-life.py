import sys
data = sys.stdin.read().split('\n')
lines = [l.strip() for l in data]
lines = [l for l in lines if l != '']
g = int(lines[0])
grid = [list(r) for r in lines[1:]]
H = len(grid)
W = len(grid[0]) if H else 0
for _ in range(g):
    ng = []
    for i in range(H):
        row = []
        for j in range(W):
            c = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    ii = i + di; jj = j + dj
                    if 0 <= ii < H and 0 <= jj < len(grid[ii]) and grid[ii][jj] == '#':
                        c += 1
            alive = grid[i][j] == '#'
            if alive and (c == 2 or c == 3):
                row.append('#')
            elif not alive and c == 3:
                row.append('#')
            else:
                row.append('.')
        ng.append(row)
    grid = ng
out = ["".join(r) for r in grid]
if out:
    sys.stdout.write("\n".join(out) + "\n")
