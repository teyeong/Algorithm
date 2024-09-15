import sys
input = sys.stdin.readline

def go(x, y):
    if dp[x][y]:
        return dp[x][y]
    
    if x == N:
        return 0
    if y - stamina[x] > 0:
        dp[x][y] = go(x + 1, y - stamina[x]) + delight[x]
    temp = go(x + 1, y)
    if dp[x][y] < temp:
        dp[x][y] = temp
    return dp[x][y]

N = int(input())
stamina = list(map(int, input().split()))
delight = list(map(int, input().split()))
dp = [[0 for _ in range(111)] for _ in range(22)]

print(go(0, 100))