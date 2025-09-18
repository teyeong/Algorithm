def solution(x, y, n):
    answer = 0
    
    dp = [1000001 for _ in range(y + 1)]
    
    print(dp[0])
    
    dp[x] = 0

    for i in range(x, y + 1):
        if i + n <= y:
            dp[i + n] = min(dp[i] + 1, dp[i + n])
        if i * 2 <= y:
            dp[i * 2] = min(dp[i] + 1, dp[i * 2])
        if i * 3 <= y:
            dp[i * 3] = min(dp[i] + 1, dp[i * 3])
    
    return dp[y] if dp[y] < 1000001 else -1