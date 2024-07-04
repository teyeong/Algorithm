from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
    
        for i in range(4):
            curr_x = x + dx[i]
            curr_y = y + dy[i]
            
            if curr_x < 0 or curr_x >= N or curr_y < 0 or curr_y >= M:
                continue
    
            if tomato[curr_x][curr_y] == 0:
                tomato[curr_x][curr_y] = tomato[x][y] + 1
                queue.append((curr_x, curr_y))

M, N = map(int, input().split())

tomato = []

for _ in range(N):
    tomato.append(list(map(int, input().split())))

queue = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))

bfs()

days = 0

for field in tomato:
    for i in field:
        if i == 0:
            print(-1)
            exit()
    else:
        days = max(days, max(field))

print(days - 1)