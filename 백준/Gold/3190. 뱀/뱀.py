from collections import deque
import sys
input = sys.stdin.readline

N = int(input()) # 보드의 크기 N
K = int(input()) # 사과의 개수 K

# 사과의 위치 [행, 열]
apples = [list(map(int, input().split())) for _ in range(K)]

L = int(input()) # 뱀의 방향 변환 횟수 L

# 뱀의 방향 변환 정보
change = dict([list(input().split()) for _ in range(L)])

# 보드
# 0 = 빈칸
# 1 = 벽
# 2 = 뱀의 몸
# 3 = 사과
board = [[0] * (N + 2) for _ in range(N + 2)]

# 보드판 벽 세팅
for i in range(N + 2):
    board[i][0] = 1
    board[i][N + 1] = 1
    board[0][i] = 1
    board[N + 1][i] = 1

# 사과 세팅
for x, y in apples:
    board[x][y] = 3

# 뱀 세팅
snake = deque() # 뱀의 몸 위치 좌표 저장 큐
direction = 0 # 초기 방향: 오른쪽
snake.append((1, 1)) # 뱀의 초기 위치
board[1][1] = 2

# 초기 보드판 출력 코드
# for i in range(N + 2):
#     for j in range(N + 2):
#         print(board[i][j], end=' ')
#     print()

time = 0 # 시간초

# 방향 설정
# 0 = 우 (x, y + 1)
# 1 = 하 (x + 1, y)
# 2 = 좌 (x, y - 1)
# 3 = 상 (x - 1, y)

while True:
    time += 1
    
    # 현재 머리의 위치
    x, y = snake[-1]
    
    
    # 새로운 위치로 이동
    if direction == 0:
        nx, ny = x, y + 1
    elif direction == 1:
        nx, ny = x + 1, y
    elif direction == 2:
        nx, ny = x, y - 1
    elif direction == 3:
        nx, ny = x - 1, y
    
    snake.append((nx, ny))
    
    if board[nx][ny] == 0:
        # 빈칸
        tx, ty = snake.popleft()
        board[tx][ty] = 0
        board[nx][ny] = 2
    elif board[nx][ny] == 1 or board[nx][ny] == 2:
        # 벽 or 몸
        break
    elif board[nx][ny] == 3:
        # 사과
        board[nx][ny] = 2
    
    # 방향 전환
    if str(time) in change:
        if change[str(time)] == 'D':
            direction = (direction + 1) % 4
        elif change[str(time)] == 'L':
            direction = (direction - 1) % 4

print(time)