from typing import List

test1, M1 = [1, 4, 2], 10

print(1 + 3 ** 3)

def neat_printer(words, M):
    n = len(words)
    cache = [float('inf')] * (n + 1)
    cache[n] = 0
    for i in range(n - 1, -1, -1):
        space_remaining = M
        for j in range(i, n):
            length = words[j] + (1 if j != i else 0)
            if length > space_remaining: break
            space_remaining -= length
            cache[i] = min(cache[i], cache[j + 1] + space_remaining ** 3)

    return cache[0]


print(neat_printer(test1, M1))
