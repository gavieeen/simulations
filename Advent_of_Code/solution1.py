from collections import Counter, deque

def isPath(grid, size):
    q = deque([(0, 0)])
    seen = [[False] * size for _ in range(size)]
    seen[0][0] = True
    steps = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while q:
        
        for _ in range(len(q)):
            x, y = q.popleft()
            if x == y == size - 1:
                return True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < size
                    and 0 <= ny < size
                    and not seen[nx][ny]
                    and grid[nx][ny] != '#'
                ):
                    q.append((nx, ny))
                    seen[nx][ny] = True

        steps += 1
        
    return False

test = 'input1.txt'
size = 71
with open(test, "r") as file:
    grid = [['.'] * size for _ in range(size)]

    lines = 0
    for line in file:
        x, y = map(int, line.strip().split(','))
        grid[y][x] = '#'
        lines += 1
        if lines > 1024 and not isPath(grid, size):
            print((x, y))
            break