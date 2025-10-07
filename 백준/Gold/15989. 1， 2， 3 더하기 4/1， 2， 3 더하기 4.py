import sys
input = sys.stdin.readline
import math

T = int(input())

dp = [[0] * 4 for _ in range(10001)]
for k in range(1, 4):
    dp[0][k] = 1
for i in range(1, 10001):
    for k in range(1, 4):
        dp[i][k] = dp[i][k - 1]
        if i >= k:
            dp[i][k] += dp[i - k][k]

for _ in range(T):
    n = int(input())
    print(dp[n][3])