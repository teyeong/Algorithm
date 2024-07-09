import sys
input = sys.stdin.readline

T = int(input())

def diagonal(r, c, arr):
    if c > len(arr[0]) - 1:
        return 0
    new_r = (r + 1) % 2
    if c + 2 < len(arr[0]) and arr[new_r][c + 2] > arr[new_r][c + 1]:
        return arr[r][c] + diagonal(new_r, c + 2, arr)
    return arr[r][c] + diagonal(new_r, c + 2, arr)

for _ in range(T):
    n = int(input())
    
    sticker = []
    dp = [[0 for _ in range(n + 1)] for _ in range(2)]
    
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
    
    dp[0][0] = dp[1][0] = 0
    dp[0][1] = sticker[0][0]
    dp[1][1] = sticker[1][0]
    
    for i in range(2, n + 1):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + sticker[0][i - 1]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + sticker[1][i - 1]
    
    print(max(dp[0][n], dp[1][n]))