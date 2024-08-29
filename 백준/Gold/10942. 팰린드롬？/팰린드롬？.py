import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
M = int(input())
dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1
    
for i in range(N - 1):
    if num[i] == num[i + 1]:
        dp[i][i + 1] = 1

for i in range(2, N):
    for j in range(N - i):
        k = j + i
        if num[j] == num[k]:
            if dp[j + 1][k - 1] == 1:
                dp[j][k] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S - 1][E - 1])