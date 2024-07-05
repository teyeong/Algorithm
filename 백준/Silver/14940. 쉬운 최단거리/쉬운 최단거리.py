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
            
            if curr_x < 0 or curr_x >= n or curr_y < 0 or curr_y >= m:
                continue
            
            if land[curr_x][curr_y] == 1:
                land[curr_x][curr_y] = land[x][y] + 1
                queue.append((curr_x, curr_y))

n, m = map(int, input().split())

land = []
queue = deque()

for _ in range(n):
    land.append(list(map(int, input().split())))

for row in range(n):
    for col in range(m):
        if land[row][col] == 2:
            start_x, start_y = row, col
            queue.append((row, col))

bfs()

for i in range(n):
    for j in range(m):
        if land[i][j] == 1: # 도달할 수 없는 위치
            print(-1, end=" ")
        elif land[i][j] == 0: # 원래 갈 수 없는 위치
            print(0, end=" ")
        else:
            print(land[i][j] - 2, end=" ")
    print()