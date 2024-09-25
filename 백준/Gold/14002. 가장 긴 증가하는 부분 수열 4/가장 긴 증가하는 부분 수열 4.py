import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [[]] * N
dp[0] = [A[0]]

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            t = max(len(dp[i]), len(dp[j]) + 1)
            if t != len(dp[i]):
                dp[i] = list(dp[j] + [A[i]])
        else:
            t = max(len(dp[i]), 1)
            if t != len(dp[i]):
                dp[i] = [A[i]]

res = max(dp, key=len)
print(len(res))
print(" ".join(map(str, res)))