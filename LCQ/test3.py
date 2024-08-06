matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

n = len(matrix)
l, r = 1, n - 2
t, b = 0, n - 1

while t < b:
    for i in range(r - l + 1):
        matrix[t][l + i], matrix[r - i][t], matrix[b][r - i], matrix[l + i][b] = (
            matrix[r - i][t],
            matrix[b][r - i],
            matrix[l + i][b],
            matrix[t][l + i]
        )
    l += 1
    r -= 1
    t += 1
    b -= 1
    
for row in matrix:
    print(row)