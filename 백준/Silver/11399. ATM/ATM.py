import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

P.sort()
res = 0
for i in range(N):
    res += P[i] * (N - i)
print(res)