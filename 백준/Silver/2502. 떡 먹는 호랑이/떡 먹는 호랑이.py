import sys
input = sys.stdin.readline

D, K = map(int, input().split())

dp = [0] * (D + 1)
ans = [0] * 2
dp[1], dp[2] = 1, 1

while True:
    for i in range(3, D + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    if dp[D] == K:
        print(dp[1], dp[2], sep="\n")
        break
    elif dp[-1] > K:
        dp[1] += 1
        dp[2] = dp[1]
    else:
        dp[2] += 1