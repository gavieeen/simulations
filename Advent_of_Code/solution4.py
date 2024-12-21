from collections import deque

# Part 1
def getCheatCount1(grid):
    m, n = len(grid), len(grid[0])
    end_r = end_c = -1

    for r, row in enumerate(grid):
        try:
            end_c = row.index('E')
            end_r = r
            break
        except ValueError:
            continue

    dp = [[0] * n for _ in range(m)]
    r, c = end_r, end_c
    dp[r][c] = length = 1
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while grid[r][c] != 'S':

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < m and 0 <= nc < n and
                grid[nr][nc] != '#' and dp[nr][nc] == 0):
                r, c = nr, nc
                break

        length += 1
        dp[r][c] = length

    cheats = 0
    while dp[r][c] > 10:
        
        for dr, dc in directions:
            nr, nc = r + 2 * dr, c + 2 * dc
            if (
                0 <= nr < m
                and 0 <= nc < n
                and dp[nr][nc]
                and dp[r][c] - dp[nr][nc] >= 102
            ):
                # print(dp[r][c], dp[nr][nc])
                cheats += 1

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < m and 0 <= nc < n and
                dp[nr][nc] == dp[r][c] - 1):
                r, c = nr, nc
                break

    return cheats

# Part 2 -> Part 1 modified
def getCheatCount2(grid, cheat_time):
    m, n = len(grid), len(grid[0])
    end_r = end_c = -1

    for r, row in enumerate(grid):
        try:
            end_c = row.index('E')
            end_r = r
            break
        except ValueError:
            continue

    dp = [[0] * n for _ in range(m)]
    r, c = end_r, end_c
    points = [(r, c)]
    dp[r][c] = length = 1
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while grid[r][c] != 'S':

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < m and 0 <= nc < n and
                grid[nr][nc] != '#' and dp[nr][nc] == 0):
                r, c = nr, nc
                break

        length += 1
        dp[r][c] = length
        points.append((r, c))
    
    cheats = 0
    for i, (r1, c1) in enumerate(points):
        for r2, c2 in points[i+1:]:
            # manhattan distance
            man_dist = abs(r2 - r1) + abs(c2 - c1)
            cheats += (man_dist <= cheat_time and dp[r2][c2] - dp[r1][c1] - man_dist >= 100)
    return cheats

test = 'input.txt'
with open(test, "r") as file:
    grid = list(map(list, file.read().strip().split("\n")))

print(getCheatCount1(grid))
print(getCheatCount2(grid, 20))