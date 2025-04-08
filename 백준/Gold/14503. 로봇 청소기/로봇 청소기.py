import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
# d: 방향
# 0 = 북쪽 (x - 1, y)
# 1 = 동쪽 (x, y + 1)
# 2 = 남쪽 (x + 1, y)
# 3 = 서쪽 (x, y - 1)

# room 방 상태
# 1: 벽
# 0: 청소 X
# 2: 청소 완료
room = [list(map(int, input().split())) for _ in range(N)]

cnt = 0 # 청소하는 방의 개수

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 좌표 반환 함수
def position(x, y, d):
    if d == 0: x -= 1
    elif d == 1: y += 1
    elif d == 2: x += 1
    elif d == 3: y -= 1
    
    return x, y

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1
    
    clean_flag = False
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        
        if 0 <= nr < N and 0 <= nc < M:
            if room[nr][nc] == 0:
                clean_flag = True
                break

    if clean_flag: # 주위에 청소할 곳이 있는 경우
        while True:
            d = (d - 1) % 4
            
            nr, nc = position(r, c, d)
            if 0 <= nr < N and 0 <= nc < M:
                if room[nr][nc] == 0:
                    r = nr
                    c = nc
                    break
    else: # 주위가 모두 청소된 경우
        nr, nc = position(r, c, (d + 2) % 4)
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] != 1:
            r = nr
            c = nc
        else:
            break
print(cnt)