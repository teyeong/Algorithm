import sys
input = sys.stdin.readline

dx = [1, 1, 1]
dy = [-1, 0, 1]

N, M = map(int, input().split())

space = [list(map(int, input().split())) for _ in range(N)]

dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]

def dfs(x, y, d):
    if x == N - 1:
        return space[x][y]
    
    if dp[x][y][d] != float('inf'):
        return dp[x][y][d]
    
    res = []
    for i in range(3):
        if i != d:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                dp[x][y][d] = min(dp[x][y][d], dfs(nx, ny, i) + space[x][y])
        
    return dp[x][y][d]

min_res = float('inf')
for i in range(M):
    for j in range(3):
        min_res = min(min_res, dfs(0, i, j))

print(min_res)