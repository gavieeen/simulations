def precompute_validity(M):
    n = len(M)
    m = len(M[0]) if n > 0 else 0
    # Initialize 4D boolean array for validity of sub-rectangles
    valid = [
        [[[False for _ in range(m)] for _ in range(n)] for _ in range(m)]
        for _ in range(n)
    ]

    # Single-cell sub-rectangles are always valid
    for i in range(n):
        for j in range(m):
            valid[i][j][i][j] = True

    # Check larger sub-rectangles for uniformity
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if (l > j and valid[i][j][k][l - 1] and M[k][l] == M[i][j]) or (
                        k > i and valid[i][j][k - 1][l] and M[k][l] == M[i][j]
                    ):
                        valid[i][j][k][l] = True

    return valid


grid = [
    [1, 2, 3],
    [1, 3, 3],
    [1, 3, 3],
]

valid = precompute_validity(grid)
print(valid[0][2][2][2])