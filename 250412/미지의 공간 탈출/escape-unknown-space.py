from collections import deque

# 미지 공간 한 변의 길이 N
# 시간의 벽 한 변의 길이 M
# 시간 이상 현상의 개수 F
N, M, F = map(int, input().split())

# 미지의 공간 place
# 0: 빈 곳
# 1: 장애물
# 2: 타임머신 위치
# 3: 시간의 벽 위치
place = [list(map(int, input().split())) for _ in range(N)]

# 동, 서, 남, 북, 윗면 단면도
east = [list(map(int, input().split())) for _ in range(M)]
west = [list(map(int, input().split())) for _ in range(M)]
south = [list(map(int, input().split())) for _ in range(M)]
north = [list(map(int, input().split())) for _ in range(M)]
top = [list(map(int, input().split())) for _ in range(M)]

# 시간 이상 현상 time_wrong
# 초기 위치 (r, c), 확산방향 d, 확산상수 v
time_wrong = [list(map(int, input().split())) for _ in range(F)]

# 시간의 벽
time_wall = []
temp = [-1 for _ in range(M)]
for i in range(3 * M):
    if 0 <= i < M:
        curr = list(reversed(north[M - i - 1]))
        time_wall.append(temp + curr + temp)
    elif M <= i < 2 * M:
        w = []
        e = []
        for j in range(M):
            w.append(west[j][i - M])
            e.append(east[j][2 * M - i - 1])
        curr = list(reversed(w))
        time_wall.append(curr + top[i - M] + e)
    else:
        time_wall.append(temp + south[i - (2 * M)] + temp)

# 남 북 동 서
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 시간의 벽 -> 미지의 공간 갈 수 있는 길 좌표 찾기 (bfs로 구해야 하므로)
start = [-1, -1] # 타임머신 시작 위치
end = [-1, -1] # 탈출구 위치
connect1 = [-1, -1] # 시간의 벽에서 미지의 공간으로 나올 수 있는 위치 (미지의 공간 좌표)
direction = -1 # connect이 연결된 벽 방향
distance = 0 # x, y 좌표 거리
for i in range(M):
    for j in range(M):
        if top[i][j] == 2:
            start = [i, j]
            break

for i in range(N):
    for j in range(N):
        if place[i][j] == 4:
            end = [i, j]
            break

for i in range(N):
    for j in range(N):
        if place[i][j] == 3:
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if place[nx][ny] == 0:
                        connect1 = [nx, ny]
                        direction = k
                        if k < 2: # 남, 북 방향
                            tempy = j - 1
                            while tempy >= 0 and place[i][tempy] == 3:
                                distance += 1
                                tempy -= 1
                        else: # 동, 서 방향
                            tempx = i - 1
                            while tempx >= 0 and place[tempx][j] == 3:
                                distance += 1
                                tempx -= 1
                        break

# 시간의 벽에서 최단 거리 distance_map
time_distance = [[0] * (3 * M) for _ in range(3 * M)]
visited = [[False] * (3 * M) for _ in range(3 * M)]
connect2 = [-1, -1] # 시간의 벽에서 미지의 공간으로 나올 수 있는 위치 (시간의 벽에 있는 좌표)
if direction == 0:
    connect2 = [3 * M - 1, M + tempy + 1]
elif direction == 1:
    connect2 = [0, M + tempy + 1]
elif direction == 2:
    connect2 = [M + tempx + 1, 3 * M - 1]
else:
    connect2 = [M + tempx + 1, 0]

queue = deque()
queue.append(tuple(connect2))
visited[connect2[0]][connect2[1]] = True
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 3 * M and 0 <= ny < 3 * M:
            if time_wall[nx][ny] == -1:
                nx, ny = y, x
            if not visited[nx][ny] and time_wall[nx][ny] == 0 or time_wall[nx][ny] == 2:
                time_distance[nx][ny] = time_distance[x][y] + 1
                queue.append((nx, ny))
                visited[nx][ny] = True

# 시간 이상 현상 좌표
anomaly = set()
# 초기값 세팅
for i in range(F):
    r, c = time_wrong[i][0], time_wrong[i][1]
    anomaly.add((r, c))

# 시간 이상 현상 확산
def disposal(turn):
    # anomaly 변경 여부 flag
    flag = False
    for i in range(F):
        x, y = time_wrong[i][0], time_wrong[i][1]
        d = time_wrong[i][2]
        v = time_wrong[i][3]
        d_idx = (d + 2) % 4 # 방향 인덱스
        for _ in range(turn % v):
            nx = x + dx[d_idx]
            ny = y + dy[d_idx]
            if 0 <= nx < N and 0 <= ny < N:
                if place[nx][ny] == 0 or place[nx][ny] == 4 and (nx, ny) not in anomaly:
                    anomaly.add((nx, ny))
                    time_wrong[i][0] = nx
                    time_wrong[i][1] = ny
                    flag = True
    if tuple(end) in anomaly:
        # 도달 불가
        print(-1)
        exit()
    return flag
    
# 타임머신 이동, 시간 이상 현상 확인
def check_road():
    place_distance = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    queue = deque()
    queue.append(tuple(end))
    visited[end[0]][end[1]] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and place[nx][ny] == 0 and (nx, ny) not in anomaly:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    place_distance[nx][ny] = place_distance[x][y] + 1
    return place_distance
    

# 턴 수
turn = 0
r, c = start[0] + M, start[1] + M
where = 0 # 0: 시간의 벽, 1: 미지의 공간
place_distance = check_road()
if place_distance[connect1[0]][connect1[1]] == 0:
    print(-1)
    exit()
if time_distance[r][c] == 0:
    print(-1)
    exit()
while True:
    turn += 1

    # 타임머신 이동
    if where == 0 and [r, c] == connect2:
        # 현재 위치가 시간의 벽 -> 미지의 공간 넘어가는 위치인 경우
        where = 1
        r, c = connect1
        flag = disposal(turn + place_distance[r][c])
        if flag == True:
            # 미지의 공간 최단 거리 재설정
            place_distance = check_road()
            if connect1 != end and place_distance[r][c] == 0:
                # 도달 불가
                print(-1)
                exit()
    else:
        min_dis = float('inf')
        min_pos = [-1, -1]
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if where == 0:
                # 시간의 벽
                if 0 <= nr < (3 * M) and 0 <= nc < (3 * M):
                    if time_wall[nr][nc] == -1:
                        nr, nc = c, r
                    if time_wall[nr][nc] == 0 and min_dis > time_distance[nr][nc]:
                        min_dis = time_distance[nr][nc]
                        min_pos = [nr, nc]
            else:
                # 미지의 공간
                if 0 <= nr < N and 0 <= nc < N:
                    if (place[nr][nc] == 0 or place[nr][nc] == 4) and (nr, nc) not in anomaly and min_dis > place_distance[nr][nc]:
                        min_dis = place_distance[nr][nc]
                        min_pos = [nr, nc]

        r, c = min_pos
    if where == 1 and place[r][c] == 4:
        # 탈출구 도착
        break
print(turn)