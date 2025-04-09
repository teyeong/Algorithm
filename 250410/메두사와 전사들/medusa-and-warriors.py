from collections import deque

# 마을 크기 N, 전사 수 M
N, M = map(int, input().split())

# 집, 공원
sr, sc, er, ec = map(int, input().split())

# 전사 초기 위치
warriors_position = list(map(int, input().split()))

# 마을
# 0: 도로
# 1: 비도로
village = [list(map(int, input().split())) for _ in range(N)]

# 메두사 초기 위치 (집)
mx, my = sr, sc
warriors = []
# 전사 초기 위치
for i in range(M):
    x, y = warriors_position[i * 2], warriors_position[i * 2 + 1]
    warriors.append([x, y])

# 상 (x - 1, y)
# 하 (x + 1, y)
# 좌 (x, y - 1)
# 우 (x, y + 1)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 좌우상하
dx2 = [0, 0, -1, 1]
dy2 = [-1, 1, 0, 0]

# 공원으로부터 거리 구하기
distance_map = [[0] * N  for _ in range(N)]
visited = [[False] * N for _ in range(N)]

queue = deque()
queue.append((er, ec))
visited[er][ec] = True

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and village[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
                distance_map[nx][ny] = distance_map[x][y] + 1

# 시작 == 도착
if sr == er and sc == ec:
    print(0)
    exit()
    
# 도착 지점에 갈 수 없는 경우
if distance_map[sr][sc] == 0:
    print(-1)
    exit()

# 메두사 시야각 측정
def sight(x, y, d):
    sight_result = [] # 메두사 시선에 닿는 좌표
    behind = set() # 전사에 의해 가려진 좌표
    stone_result = [] # 돌로 변하는 전사 좌표
    warriors_set = set(map(tuple, warriors))
    
    # for문 조건
    con = []
    
    if d % 2 == 0: # 상, 좌
        con = [-1, -1, -1]
    else: # 하, 우
        con = [1, N, 1]
    
    queue2 = deque()
    
    
    if d < 2: # 상, 하
        for i in range(x + con[0], con[1], con[2]):
            
            # 왼쪽 부분
            for ly in range(y - 1, y - abs(x - i) - 1, -1):
                if ly < 0 or (i, ly) in behind:
                    continue
                sight_result.append([i, ly])
                if (i, ly) in warriors_set:
                    num = warriors.count([i, ly])
                    for _ in range(num):
                        stone_result.append([i, ly])
                    for wx in range(i + con[0], con[1], con[2]):
                        behind.add((wx, ly))
                        for wly in range(ly - 1, ly - abs(i - wx) - 1, -1):
                            if wly < 0 : continue
                            behind.add((wx, wly))
            
            # 오른쪽 부분
            for ry in range(y + 1, y + abs(x - i) + 1):
                if ry >= N or (i, ry) in behind:
                    continue
                sight_result.append([i, ry])
                if (i, ry) in warriors_set:
                    num = warriors.count([i, ry])
                    for _ in range(num):
                        stone_result.append([i, ry])
                    for wx in range(i + con[0], con[1], con[2]):
                        behind.add((wx, ry))
                        for wry in range(ry + 1, ry + abs(i - wx) + 1):
                            if wry >= N: continue
                            behind.add((wx, wry))
                    
            # 중간 부분
            if (i, y) in behind:
                continue
            sight_result.append([i, y])
            if (i, y) in warriors_set:
                num = warriors.count([i, y])
                for _ in range(num):
                    stone_result.append([i, y])
                for wx in range(i + con[0], con[1], con[2]):
                    behind.add((wx, y))
    
    else: # 좌, 우
        for i in range(y + con[0], con[1], con[2]):
            # 왼쪽 부분
            for lx in range(x - 1, x - abs(y - i) - 1, -1):
                if lx < 0 or (lx, i) in behind:
                    continue
                sight_result.append([lx, i])
                if (lx, i) in warriors_set:
                    num = warriors.count([lx, i])
                    for _ in range(num):
                        stone_result.append([lx, i])
                    for wy in range(i + con[0], con[1], con[2]):
                        behind.add((lx, wy))
                        for wlx in range(lx - 1, lx - abs(i - wy) - 1, -1):
                            if wlx < 0: continue
                            behind.add((wlx, wy))
            
            # 오른쪽 부분
            for rx in range(x + 1, x + abs(y - i) + 1):
                if rx >= N or (rx, i) in behind:
                    continue
                sight_result.append([rx, i])
                if (rx, i) in warriors_set:
                    num = warriors.count([rx, i])
                    for _ in range(num):
                        stone_result.append([rx, i])
                    for wy in range(i + con[0], con[1], con[2]):
                        behind.add((rx, wy))
                        for wrx in range(rx + 1, rx + abs(i - wy) + 1):
                            if wrx >= N: continue
                            behind.add((wrx, wy))
                    
            # 중간 부분
            if (x, i) in behind:
                continue
            sight_result.append([x, i])
            if (x, i) in warriors_set:
                num = warriors.count([x, i])
                for _ in range(num):
                    stone_result.append([x, i])
                for wy in range(i + con[0], con[1], con[2]):
                    behind.add((x, wy))
    return sight_result, stone_result

# 전사 이동 함수
def move_warrior(warriors, stone, vision, mx, my, dx, dy):
    # set 설정
    stone_set = set(map(tuple, stone))
    vision_set = set(map(tuple, vision))
    
    # 공격 전사
    attack = []
    # 이동 거리
    distance = 0
    # 이동
    for idx, [x, y] in enumerate(warriors):
        if (x, y) in stone_set: continue
        min_gap = 100
        min_xy = None
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < N and 0 <= ny < N:
                gap = abs(nx - mx) + abs(ny - my)
                if gap < min_gap:
                    min_gap = gap
                    min_xy = (nx, ny)
                elif gap == min_gap:
                    if min_xy in vision_set and (nx, ny) not in vision_set:
                        min_xy = (nx, ny)
        
        
        if min_xy in vision_set:
            continue
        
        warriors[idx][0], warriors[idx][1] = min_xy[0], min_xy[1]
        if warriors[idx][0] == mx and warriors[idx][1] == my:
            # 4. 전사 공격
            attack.append(idx)
        distance += 1
        
    for idx in reversed(attack):
        warriors.pop(idx)
    return warriors, distance, len(attack)

while True:
    # 전사가 이동한 거리 합
    curr_distance = 0
    
    # 메두사로 인해 돌이 된 전사 수
    curr_stone = 0
    
    # 메두사를 공격한 전사 수
    curr_attack = 0
    
    # 1. 메두사의 이동
    min_gap = 100
    min_idx = -1
    for i in range(4):
        nx = mx + dx[i]
        ny = my + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if village[nx][ny] == 0:
                if distance_map[nx][ny] < min_gap:
                    min_gap = distance_map[nx][ny]
                    min_idx = i
    
    mx = mx + dx[min_idx]
    my = my + dy[min_idx]
    if [mx, my] in warriors:
        # 이동한 위치에 전사가 존재하는 경우
        while [mx, my] in warriors:
            warriors.remove([mx, my])
    
    # 2. 메두사의 시선
    real_vision = []
    real_stone = [] # 중복 포함
    for i in range(4):
        temp_vision, temp_stone = sight(mx, my, i)
        if len(temp_stone) > len(real_stone):
            real_vision = temp_vision
            real_stone = temp_stone
    
    # 3. 전사 이동
    # 첫 번째 이동
    warriors, distance1, attack1 = move_warrior(warriors, real_stone, real_vision, mx, my, dx, dy)
    # 두 번째 이동
    warriors, distance2, attack2 = move_warrior(warriors, real_stone, real_vision, mx, my, dx2, dy2)
    
    curr_distance += distance1 + distance2
    curr_stone += len(real_stone)
    curr_attack += attack1 + attack2
                
    if mx == er and my == ec:
        # 종료
        print(0)
        break
    else:
        print(curr_distance, curr_stone, curr_attack, end=' ')
        print()