from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().strip()) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

# 최단거리니까 bfs
queue = deque()

red = [0, 0] # 빨간 구슬 초기 위치
blue = [0, 0] # 파란 구슬 초기 위치
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue.append((rx, ry, bx, by, 0)) # 초기 값 큐에 넣기

# 벽에 닿을 때까지 이동하는 함수
def roll(x, y, dx, dy):
    dist = 0
    while True:
        if board[x + dx][y + dy] == '#':
            break
        x += dx
        y += dy
        dist += 1
        if board[x][y] == 'O':  # 구멍에 빠짐
            break
    return x, y, dist

while queue:
    rx, ry, bx, by, cnt = queue.popleft()

    # 횟수가 10번 초과인 경우 -> 종료
    if cnt >= 10:
        print(-1)
        exit()

    for i in range(4):
        nrx, nry, r_dist = roll(rx, ry, dx[i], dy[i])
        nbx, nby, b_dist = roll(bx, by, dx[i], dy[i])
        
        # 파란 구슬이 빠진 경우 -> 종료
        if board[nbx][nby] == 'O':
            continue
        
        # 빨간 구슬이 빠진 경우 -> 종료
        if board[nrx][nry] == 'O':
            print(cnt + 1)
            exit()
        
        # 빨간 구슬, 파란 구슬이 겹친 경우 -> 덜 움직인 쪽 이동
        if nrx == nbx and nry == nby:
            if r_dist > b_dist:
                nrx -= dx[i]
                nry -= dy[i]
            else:
                nbx -= dx[i]
                nby -= dy[i]
        
        # 방문하지 않은 경우 큐에 넣기
        if not visited[nrx][nry][nbx][nby]:
            visited[nrx][nry][nbx][nby] = True
            queue.append((nrx, nry, nbx, nby, cnt + 1))
print(-1)