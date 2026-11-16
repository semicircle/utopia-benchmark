import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    g = int(lines[0].strip())
    grid = [list(l) for l in lines[1:] if l != ""]
    R = len(grid)
    C = len(grid[0]) if R else 0
    for _ in range(g):
        new = [row[:] for row in grid]
        for r in range(R):
            for c in range(C):
                cnt = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == "#":
                            cnt += 1
                if grid[r][c] == "#":
                    new[r][c] = "#" if cnt == 2 or cnt == 3 else "."
                else:
                    new[r][c] = "#" if cnt == 3 else "."
        grid = new
    sys.stdout.write("\n".join("".join(row) for row in grid) + "\n")

main()
