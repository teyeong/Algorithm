N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
cctvs = []

# 우 좌 하 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 방향
dirs = [
           [[0], [1], [2], [3]], # 1번
            [[0, 1], [2, 3]], # 2번
            [[0, 3], [0, 2], [1, 2], [1, 3]], # 3번
            [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]] # 4번
        ]

# cctv로 감시 구역 설정
def check_blind_spot(y, x, directions, blind_spot):
    pos = set()
    for i in directions:
        cx, cy = x, y
        while 0 <= cx < M and 0 <= cy < N:
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if blind_spot[ny][nx] == 0: # 빈 칸
                    blind_spot[ny][nx] = '#'
                    pos.add((ny, nx))
                elif blind_spot[ny][nx] == 6: # 벽
                    break
            else:
                break
            
            cx, cy = nx, ny
    return blind_spot, pos

for y in range(N):
    for x in range(M):
        if office[y][x] != '#' and 0 < office[y][x] < 6:
            if office[y][x] == 5:
                office, _ = check_blind_spot(y, x, range(4), office)
            else:
                cctvs.append((office[y][x], y, x))

cnt = 0
for y in range(N):
    for x in range(M):
        if office[y][x] == 0:
            cnt += 1

min_blind_spot = cnt

# 각 방향마다 조합해서 탐색
def dfs(idx, office_statement, cnt):
    global min_blind_spot
    
    if idx == len(cctvs):
        min_blind_spot = min(cnt, min_blind_spot)
        return
    
    for d in dirs[cctvs[idx][0] - 1]:
        office_statement, pos = check_blind_spot(cctvs[idx][1], cctvs[idx][2], d, office_statement)
        dfs(idx + 1, office_statement, cnt - len(pos))
        for y, x in pos:
            office_statement[y][x] = 0

dfs(0, office, min_blind_spot)
print(min_blind_spot)