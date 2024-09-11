import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[0, 0] for _ in range(100001)]
res = dp[1][0] = arr[0]

for i in range(2, n + 1):
    if dp[i - 1][0] < 1:
        dp[i][0] = arr[i - 1]
    else:
        dp[i][0] = dp[i - 1][0] + arr[i - 1]
    dp[i][1] = max(dp[i - 2][0], dp[i - 1][1]) + arr[i - 1]
    res = max(dp[i][0], dp[i][1], res)

print(res)