import sys
input = sys.stdin.readline

# N: 체스판 크기
# K: 말의 개수
N, K = map(int, input().split())

chess_board = [list(map(int, input().split())) for _ in range(N)]
piece = [list(map(int, input().split())) for _ in range(K)]
pos = [[list() for _ in range(N)] for _ in range(N)] # 말이 실제 위치할 장소 저장

# 0, 우,좌,상,하
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def white(x, y, curr):
    # 흰 칸 도착
    pos[x][y] += curr
    for c in curr:
        piece[c] = [x, y, piece[c][2]]
    return len(pos[x][y])

def red(x, y, curr):
    # 빨간 칸 도착
    pos[x][y] += curr[::-1] # 순서 뒤집기
    for c in curr:
        piece[c] = [x, y, piece[c][2]]
    return len(pos[x][y])

def blue(x, y, d, curr, idx):
    # 파란 칸 도착
    length = 0
    
    # 이동 방향 변경
    if d == 1 or d == 3:
        d += 1
    else:
        d -= 1
    
    piece[idx][2] = d # 방향 전환 적용
    
    # 이동할 새 위치
    nx = x + dx[d]
    ny = y + dy[d]
    
    
    if 0 <= nx < N and 0 <= ny < N:
        if chess_board[nx][ny] == 0: # 흰 칸
            length = max(length, white(nx, ny, curr))
        elif chess_board[nx][ny] == 1: # 빨간 칸
            length = max(length, red(nx, ny, curr))
        elif chess_board[nx][ny] == 2: # 파란 칸: 이동 X
            pos[x][y] += curr
            for c in curr:
                piece[c] = [x, y, piece[c][2]]
            length = max(length, len(pos[x][y]))
    else:
        # 파란 칸 취급
        # 이동 X
        pos[x][y] += curr
        for c in curr:
            piece[c] = [x, y, piece[c][2]]
        length = max(length, len(pos[x][y]))
    return length

turn = 0
cnt_4 = 0

# 시작 위치 적용
for i, p in enumerate(piece):
    pos[p[0] - 1][p[1] - 1].append(i) # 말의 id
    piece[i][0], piece[i][1] = p[0] - 1, p[1] - 1 # 1 마이너스 후 업데이트

while turn < 1000:
    turn += 1
    
    # K개의 말 이동
    for i in range(K):
        x, y, d = piece[i]
        # 현재 말이 가장 밑에 있는 경우에만 이동 가능
        if len(pos[x][y]) == 0 or pos[x][y][0] == i:
            curr = pos[x][y] # 현재 말 stack 저장
            pos[x][y] = [] # 비워주기
            
            # 새 위치
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < N and 0 <= ny < N:
                if chess_board[nx][ny] == 0: # 흰 칸
                    cnt_4 = max(cnt_4, white(nx, ny, curr))
                elif chess_board[nx][ny] == 1: # 빨간 칸
                    cnt_4 = max(cnt_4, red(nx, ny, curr))
                elif chess_board[nx][ny] == 2: # 파란 칸
                    cnt_4 = max(cnt_4, blue(x, y, d, curr, i))
            else:
                cnt_4 = max(cnt_4, blue(x, y, d, curr, i)) # 파란 칸 취급
    
    if cnt_4 >= 4:
        break

print(turn if -1 < turn < 1000 else -1)