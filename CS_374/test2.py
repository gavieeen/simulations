def min_mult(arr):
    n = len(arr)
    # Create a 2D DP array to store min
    # multiplication costs
    dp = [[0] * n for _ in range(n)]
    
    # Fill the DP array
    # length is the chain length
    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = float('inf')
            
            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], cost)
    
    # Minimum cost is in dp[0][n-1]
    return dp[0][n - 1]


test1 = [10, 100, 5, 50]
print(min_mult(test1))  # 7500