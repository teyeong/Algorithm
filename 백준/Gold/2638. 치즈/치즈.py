import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def fill_outside(x, y, visit):
    cheese[x][y] = 2
    visit[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
            
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if not visit[nx][ny] and (cheese[nx][ny] == 0 or cheese[nx][ny] == 2):
            visit[nx][ny] = 1
            cheese[nx][ny] = 2
            fill_outside(nx, ny, visit)

def fill_inside(x, y):
    cnt = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if cheese[nx][ny] == 2:
            cnt += 1
    
    return cnt

N, M = map(int, input().split())

cheese = []
times = 0

for i in range(N):
    cheese.append(list(map(int, input().split())))

while True:
    times += 1
    visit = [[0 for _ in range(M)] for _ in range(N)]
    temp = []
    fill_outside(0, 0, visit)
    
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 1 and fill_inside(i, j) > 1:
                temp.append((i, j))
    
    for x, y in temp:
        cheese[x][y] = 2
        
    flag = True
    
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 1:
                flag = False
                break
    if flag:
        break

print(times)