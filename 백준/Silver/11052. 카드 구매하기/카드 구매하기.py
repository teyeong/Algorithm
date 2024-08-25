import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    max_price = 0
    for j in range(i):
        if max_price < dp[i - j - 1] + P[j]:
            max_price = dp[i - j - 1] + P[j]
    dp[i] = max_price

print(dp[N])