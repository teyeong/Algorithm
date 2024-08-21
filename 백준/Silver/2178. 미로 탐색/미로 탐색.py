import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = []
    q.append((0, 0))
    
    while q:
        curr_x, curr_y = q.pop(0)
        for i in range(4):
            x = curr_x + dx[i]
            y = curr_y + dy[i]
            
            if x < 0 or x >= N or y < 0 or y >= M:
                continue
            
            if maze[x][y] == 1:
                q.append((x, y))
                maze[x][y] = maze[curr_x][curr_y] + 1

N, M = map(int, input().split())

maze = []

for _ in range(N):
    maze.append(list(map(int, input().rstrip())))

bfs()
print(maze[-1][-1])