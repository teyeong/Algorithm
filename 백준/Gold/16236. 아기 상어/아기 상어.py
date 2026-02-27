from collections import deque
import heapq

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

time = 0 # 시간
shark_size = 2 # 상어 크기
babyshark = [0, 0] # 아기 상어 위치

# 아기 상어 초기 위치 구하기
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            babyshark = [i, j]
            break

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 상어와 물고기 사이 이동 거리 계산
def cal_distance(shark, space):
    q = deque()
    q.append((shark[0], shark[1], 0))
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[shark[0]][shark[1]] = True
    cnt = 0
    
    distance = []
    
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == False and space[nx][ny] <= shark_size:
                    # 지나갈 수 있는 공간 (상어 크기 이하)
                    q.append((nx, ny, cnt + 1))
                    visited[nx][ny] = True
                    if 0 < space[nx][ny] < shark_size:
                        # 먹을 수 있는 물고기 후보 (상어 크기보다 작은 물고기)
                        heapq.heappush(distance, (cnt + 1, nx, ny))
    return distance

fish_cnt = 0 # 먹은 물고기 개수 세는 변수
distance = cal_distance(babyshark, space)

while distance:
    dis, x, y = heapq.heappop(distance)
    space[x][y] = 9
    space[babyshark[0]][babyshark[1]] = 0
    babyshark = [x, y]
    fish_cnt += 1

    if fish_cnt == shark_size: # 아기 상어 성장
        fish_cnt = 0
        shark_size += 1
    distance = cal_distance(babyshark, space)
    
    time += dis

print(time)