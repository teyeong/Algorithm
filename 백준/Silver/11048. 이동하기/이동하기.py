import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dx = [-1, 0]
dy = [0, -1]

maze = []

for _ in range(N):
    maze.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        temp = 0
        for k in range(2):
            r = dx[k] + i
            c = dy[k] + j
            if r < 0 or r >= N or c < 0 or c >= M:
                continue
            if temp < maze[r][c]:
                temp = maze[r][c]
        maze[i][j] += temp

print(maze[N - 1][M - 1])