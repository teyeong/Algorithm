from collections import deque
import sys
input = sys.stdin.readline

# 지도 세로 N
# 지도 가로 M
# 주사위 좌표 x, y
# 명령 개수 K
N, M, x, y, K = map(int, input().split())

# 지도
maps = [list(map(int, input().split())) for _ in range(N)]

# 명령
# 1 = 동쪽 (x, y + 1)
# 2 = 서쪽 (x, y - 1)
# 3 = 북쪽 (x - 1, y)
# 4 = 남쪽 (x + 1, y)
orders = list(map(int, input().split()))

# dice[1] = 윗면
# dice[3] = 아랫면
def roll(dice, direction):
    if direction == 1:
        dice[4], dice[1], dice[5], dice[3] = dice[3], dice[4], dice[1], dice[5]
    elif direction == 2:
        dice[1], dice[4], dice[3], dice[5] = dice[5], dice[1], dice[4], dice[3]
    elif direction == 3:
        dice[2], dice[1], dice[0], dice[3] = dice[3], dice[2], dice[1], dice[0]
    elif direction == 4:
        dice[1], dice[2], dice[3], dice[0] = dice[0], dice[1], dice[2], dice[3]
    return dice

# 이동
def move(x, y, direction):
    if direction == 1:
        nx = x
        ny = y + 1
    elif direction == 2:
        nx = x
        ny = y - 1
    elif direction == 3:
        nx = x - 1
        ny = y
    elif direction == 4:
        nx = x + 1
        ny = y
    
    return nx, ny

# 주사위
dice = [0 for _ in range(6)]

for order in orders:
    nx, ny = move(x, y, order)
    
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
    else:
        continue
    
    dice = roll(dice, order)
    
    if maps[x][y] == 0:
        # 칸이 0이면 주사위 바닥면 수를 칸에 복사
        maps[x][y] = dice[3]
    else:
        # 0이 아닌 경우 칸에 쓰인 수가 주사위 바닥면으로 복사됨, 칸은 0이 됨
        dice[3] = maps[x][y]
        maps[x][y] = 0
    print(dice[1])