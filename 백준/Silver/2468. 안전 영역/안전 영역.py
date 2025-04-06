import sys
sys.setrecursionlimit(10 ** 6) # 재귀 깊이 설정

def dfs(x, y, visit, limit):
    visit[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0  or nx >= N or ny < 0 or ny >= N:
            continue
        
        if rain[nx][ny] > limit and visit[nx][ny] == False:
            visit = dfs(nx, ny, visit, limit)
    return visit

N = int(input())

rain = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_height = max(map(max, rain)) # 최대 높이
max_area = 0 # 최대 영역 개수

for limit in range(max_height + 1):
    visit = [[False] * N for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if rain[x][y] > limit and visit[x][y] == False:
                cnt += 1
                visit = dfs(x, y, visit, limit)
    max_area = max(max_area, cnt)
    
print(max_area)